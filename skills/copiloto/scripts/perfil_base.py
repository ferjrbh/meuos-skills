#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Perfil de base: o inventário que vem antes de qualquer conta.

Lê CSV e Excel (.xlsx) de um arquivo ou de uma pasta e responde, por arquivo e por coluna:
linhas, colunas, vazios, zeros, negativos, valores únicos, mínimo e máximo (número e data),
soma, chaves candidatas, linhas repetidas, datas guardadas como texto e suspeita de corte
(limite de linhas do Excel). Entre arquivos, cruza as colunas de identificador nos dois sentidos.

Só biblioteca padrão. Se o openpyxl estiver instalado, usa para ler Excel; senão, lê o .xlsx direto.

Uso:
  python3 perfil_base.py <arquivo-ou-pasta> [mais arquivos...] [--chave arquivo.csv:col1+col2] [--max-linhas N]
"""
import csv, io, os, re, sys, zipfile, statistics
for _s in (sys.stdout, sys.stderr):  # Windows grava em cp1252 quando a saida nao e terminal: forca UTF-8
    try:
        _s.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
from collections import Counter, defaultdict
from datetime import date
from xml.etree import ElementTree as ET

csv.field_size_limit(10**9)
LIMITE_EXCEL = {1048575, 1048576}
DATA_PADROES = [
    (re.compile(r"^(\d{4})-(\d{2})-(\d{2})"), "AAAA-MM-DD", lambda m: (int(m[1]), int(m[2]), int(m[3]))),
    (re.compile(r"^(\d{2})/(\d{2})/(\d{4})$"), "DD/MM/AAAA", lambda m: (int(m[3]), int(m[2]), int(m[1]))),
    (re.compile(r"^(\d{2})-(\d{2})-(\d{4})$"), "DD-MM-AAAA", lambda m: (int(m[3]), int(m[2]), int(m[1]))),
    (re.compile(r"^(\d{4})-(\d{2})$"), "AAAA-MM", lambda m: (int(m[1]), int(m[2]), 1)),
    (re.compile(r"^(\d{4})/(\d{2})$"), "AAAA/MM", lambda m: (int(m[1]), int(m[2]), 1)),
]
NUM_BR = re.compile(r"^-?\d{1,3}(\.\d{3})+(,\d+)?$|^-?\d+,\d+$")
NUM_EN = re.compile(r"^-?\d{1,3}(,\d{3})+(\.\d+)?$|^-?\d+(\.\d+)?$")
ID_NOME = re.compile(r"(^id$|_id$|^id_|^cod|codigo|cnpj|cpf|matricula|^sku|^pedido|^cliente$|^loja$|^conta$|^contrato$)", re.I)


def numero(txt):
    """Converte texto em número entendendo formato brasileiro e americano. Devolve None se não for número."""
    if txt is None:
        return None
    if isinstance(txt, (int, float)):
        return float(txt)
    s = str(txt).strip().replace("R$", "").replace(" ", "").replace(" ", "")
    if s.endswith("%"):
        s = s[:-1]
    if not s or s in {"-", "--"}:
        return None
    if NUM_BR.match(s):
        return float(s.replace(".", "").replace(",", "."))
    if NUM_EN.match(s):
        return float(s.replace(",", ""))
    return None


def data(txt):
    s = str(txt).strip()
    for rx, nome, f in DATA_PADROES:
        m = rx.match(s)
        if m:
            try:
                a, me, d = f(m)
                return date(a, me, d), nome
            except ValueError:
                return None, None
    return None, None


# ---------------------------------------------------------------- leitura
def ler_csv(caminho):
    bruto = open(caminho, "rb").read()
    for enc in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            texto = bruto.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    amostra = texto[:20000]
    try:
        dialeto = csv.Sniffer().sniff(amostra, delimiters=",;\t|")
        sep = dialeto.delimiter
    except csv.Error:
        sep = ";" if amostra.count(";") > amostra.count(",") else ","
    linhas = list(csv.reader(io.StringIO(texto), delimiter=sep))
    if not linhas:
        return {"(arquivo)": ([], [])}, enc, sep
    return {"(arquivo)": (linhas[0], linhas[1:])}, enc, sep


def ler_xlsx(caminho):
    try:
        import openpyxl  # noqa
        wb = openpyxl.load_workbook(caminho, read_only=True, data_only=True)
        abas = {}
        for ws in wb.worksheets:
            vals = [["" if v is None else v for v in row] for row in ws.iter_rows(values_only=True)]
            vals = [r for r in vals if any(str(c).strip() for c in r)]
            if vals:
                abas[ws.title] = ([str(c) for c in vals[0]], vals[1:])
        return abas, "openpyxl"
    except ImportError:
        pass
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    z = zipfile.ZipFile(caminho)
    comp = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", ns):
            comp.append("".join(t.text or "" for t in si.iter("{%s}t" % ns["m"])))
    wbx = ET.fromstring(z.read("xl/workbook.xml"))
    nomes = [s.get("name") for s in wbx.find("m:sheets", ns)]
    abas = {}
    for i, nome in enumerate(nomes, 1):
        p = f"xl/worksheets/sheet{i}.xml"
        if p not in z.namelist():
            continue
        linhas = []
        for row in ET.fromstring(z.read(p)).iter("{%s}row" % ns["m"]):
            cel = {}
            for c in row.findall("m:c", ns):
                ref = re.match(r"([A-Z]+)", c.get("r", "A")).group(1)
                col = 0
                for ch in ref:
                    col = col * 26 + ord(ch) - 64
                v = c.find("m:v", ns)
                if c.get("t") == "s" and v is not None:
                    val = comp[int(v.text)]
                elif c.get("t") == "inlineStr":
                    val = "".join(t.text or "" for t in c.iter("{%s}t" % ns["m"]))
                else:
                    val = v.text if v is not None else ""
                cel[col] = val
            if cel:
                linhas.append([cel.get(k, "") for k in range(1, max(cel) + 1)])
        if linhas:
            abas[nome] = ([str(c) for c in linhas[0]], linhas[1:])
    return abas, "leitor interno (sem openpyxl)"


# ---------------------------------------------------------------- perfil
def perfil_coluna(nome, valores):
    n = len(valores)
    vazios = sum(1 for v in valores if str(v).strip() == "")
    cheios = [v for v in valores if str(v).strip() != ""]
    nums = [numero(v) for v in cheios]
    nums_ok = [x for x in nums if x is not None]
    datas = [data(v) for v in cheios]
    datas_ok = [d for d, _ in datas if d]
    fmts = Counter(f for d, f in datas if d)
    unicos = len(set(map(str, cheios)))
    out = {"coluna": nome, "vazios": vazios, "unicos": unicos, "n": n}
    if cheios and len(datas_ok) >= 0.9 * len(cheios):
        out["tipo"] = "data"
        out["min"], out["max"] = min(datas_ok), max(datas_ok)
        out["formato"] = ", ".join(fmts)
        if any(f in ("DD/MM/AAAA", "DD-MM-AAAA") for f in fmts):
            lex = sorted(map(str, cheios))
            out["alerta"] = (f"data guardada como texto ({out['formato']}): ordem alfabética daria {lex[0]} a {lex[-1]}, "
                             f"a real é {out['min']} a {out['max']}")
    elif cheios and len(nums_ok) >= 0.9 * len(cheios):
        out["tipo"] = "número"
        out["min"], out["max"], out["soma"] = min(nums_ok), max(nums_ok), sum(nums_ok)
        out["zeros"] = sum(1 for x in nums_ok if x == 0)
        out["negativos"] = sum(1 for x in nums_ok if x < 0)
        if len(nums_ok) >= 20:
            srt = sorted(nums_ok)
            p99 = srt[int(0.99 * (len(srt) - 1))]
            mediana = statistics.median(srt)
            out["acima_p99x3"] = sum(1 for x in nums_ok if p99 > 0 and x > 3 * p99)
            out["mediana"] = mediana
        texto_num = sum(1 for v in cheios if isinstance(v, str) and numero(v) is not None and re.search(r"[.,]", v))
        if texto_num and any(isinstance(v, (int, float)) for v in cheios):
            out["alerta"] = "mistura de número e número guardado como texto"
    else:
        out["tipo"] = "texto"
        espacos = sum(1 for v in cheios if isinstance(v, str) and v != v.strip())
        if espacos:
            out["alerta"] = f"{espacos} valores com espaço sobrando nas pontas"
        caixa = defaultdict(set)
        for v in set(map(str, cheios)):
            caixa[v.strip().lower()].add(v)
        variantes = sum(1 for k, s in caixa.items() if len(s) > 1)
        if variantes:
            out["alerta"] = (out.get("alerta", "") + f" · {variantes} grafias que só diferem em maiúscula ou espaço").strip(" ·")
    return out


def fmt(x):
    if isinstance(x, float):
        if abs(x) >= 1000:
            return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return f"{x:.4g}".replace(".", ",")
    return str(x)


def perfil_tabela(rotulo, cab, linhas, chaves_pedidas):
    rel = []
    ncol = len(cab)
    rel.append(f"\n## {rotulo}\n")
    rel.append(f"- Linhas de dado (sem o cabeçalho): **{len(linhas)}** · colunas: **{ncol}**")
    if len(linhas) + 1 in LIMITE_EXCEL or len(linhas) in LIMITE_EXCEL:
        rel.append("- ⚠️ **O número de linhas bate com o limite do Excel (1.048.575 ou 1.048.576): a base pode ter sido cortada.**")
    larg = Counter(len(l) for l in linhas)
    if len(larg) > 1:
        rel.append(f"- ⚠️ Linhas com número de colunas diferente: {dict(larg)}")
    tuplas = [tuple(map(str, l)) for l in linhas]
    rep = len(tuplas) - len(set(tuplas))
    rel.append(f"- Linhas inteiras repetidas: **{rep}**" + (" ⚠️" if rep else ""))
    colunas = []
    for j, nome in enumerate(cab):
        vals = [l[j] if j < len(l) else "" for l in linhas]
        colunas.append(perfil_coluna(nome or f"coluna_{j+1}", vals))
    cand = [c["coluna"] for c in colunas if c["unicos"] == len(linhas) and c["vazios"] == 0 and len(linhas) > 1
            and (c["tipo"] != "número" or ID_NOME.search(c["coluna"]))]
    rel.append(f"- Colunas sem nenhum valor repetido (chave candidata): {', '.join(cand) if cand else 'nenhuma'}")
    rel.append("\n| coluna | tipo | vazios | únicos | mín | máx | soma | observação |\n|---|---|---|---|---|---|---|---|")
    for c in colunas:
        obs = []
        if c.get("zeros"):
            obs.append(f"{c['zeros']} zeros")
        if c.get("negativos"):
            obs.append(f"{c['negativos']} negativos")
        if c.get("acima_p99x3"):
            obs.append(f"{c['acima_p99x3']} acima de 3× o p99")
        if c.get("formato"):
            obs.append(c["formato"])
        if c.get("alerta"):
            obs.append("⚠️ " + c["alerta"])
        rel.append(f"| {c['coluna']} | {c['tipo']} | {c['vazios']} | {c['unicos']} | {fmt(c.get('min', ''))} | "
                   f"{fmt(c.get('max', ''))} | {fmt(c.get('soma', ''))} | {'; '.join(obs)} |")
    for chave in chaves_pedidas:
        idx = [cab.index(k) for k in chave if k in cab]
        if len(idx) != len(chave):
            rel.append(f"\n- Chave pedida {'+'.join(chave)}: coluna não encontrada")
            continue
        cont = Counter(tuple(str(l[i]) for i in idx) for l in linhas)
        dup = {k: v for k, v in cont.items() if v > 1}
        rel.append(f"\n- Multiplicidade da chave **{'+'.join(chave)}**: {len(cont)} valores distintos em {len(linhas)} linhas · "
                   f"repetidos: **{len(dup)}**" + (f" ⚠️ exemplos: {list(dup.items())[:3]}" if dup else " ✅"))
    print("\n".join(rel))
    return colunas


def norm_id(v):
    x = numero(v) if not isinstance(v, str) or re.fullmatch(r"-?[\d.,]+", str(v).strip()) else None
    if x is not None and float(x).is_integer():
        return str(int(x))
    return str(v).strip()


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    chaves = defaultdict(list)
    alvos = []
    i = 0
    while i < len(args):
        if args[i] == "--chave":
            arq, cols = args[i + 1].split(":", 1)
            chaves[os.path.basename(arq)].append(cols.split("+"))
            i += 2
        elif args[i] == "--max-linhas":
            i += 2
        else:
            alvos.append(args[i])
            i += 1
    arquivos = []
    for a in alvos:
        if os.path.isdir(a):
            for nome in sorted(os.listdir(a)):
                if nome.lower().endswith((".csv", ".xlsx", ".xlsm", ".txt", ".tsv")) and not nome.startswith("~$"):
                    arquivos.append(os.path.join(a, nome))
        else:
            arquivos.append(a)
    print("# Perfil da base\n")
    print("Inventário antes de qualquer conta: contar, testar a chave, olhar as datas e cruzar os arquivos.")
    ids = {}  # (rotulo, coluna) -> set de valores
    for arq in arquivos:
        base = os.path.basename(arq)
        try:
            if arq.lower().endswith((".xlsx", ".xlsm")):
                abas, leitor = ler_xlsx(arq)
                print(f"\n# {base}  (Excel, {len(abas)} aba(s), lido por {leitor})")
                tabelas = [(f"{base} · aba {k}", v) for k, v in abas.items()]
            else:
                tabs, enc, sep = ler_csv(arq)
                print(f"\n# {base}  (texto, codificação {enc}, separador '{sep}')")
                tabelas = [(base, v) for v in tabs.values()]
        except Exception as e:  # arquivo corrompido ou formato inesperado
            print(f"\n# {base}\n- ⚠️ não consegui ler: {e}")
            continue
        for rotulo, (cab, linhas) in tabelas:
            cols = perfil_tabela(rotulo, cab, linhas, chaves.get(base, []))
            for j, c in enumerate(cols):
                nome = c["coluna"]
                if ID_NOME.search(nome) or (c["tipo"] == "texto" and c["unicos"] > 0.5 * max(1, len(linhas))):
                    ids[(rotulo, nome)] = set(norm_id(l[j]) for l in linhas if j < len(l) and str(l[j]).strip())
    print("\n# Cruzamento entre arquivos (colunas de identificador com o mesmo nome)\n")
    por_nome = defaultdict(list)
    for (rot, col), vals in ids.items():
        por_nome[col.lower()].append((rot, vals))
    achou = False
    for col, lista in por_nome.items():
        if len(lista) < 2:
            continue
        achou = True
        uniao = set().union(*(v for _, v in lista))
        todos = set.intersection(*(v for _, v in lista))
        print(f"- **{col}**: {len(uniao)} valores no conjunto dos arquivos · {len(todos)} aparecem em todos")
        for rot, v in lista:
            falta = uniao - v
            marca = f" ⚠️ faltam {len(falta)} (ex.: {sorted(falta)[:5]})" if falta else " ✅ tem todos"
            print(f"  - {rot}: {len(v)}{marca}")
    if not achou:
        print("- Nenhuma coluna de identificador em comum entre os arquivos.")
    print("\nPróximo passo: bater os totais com uma fonte de fora (sistema oficial, balanço, painel) antes de concluir.")


if __name__ == "__main__":
    main()
