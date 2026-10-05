#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extrai todos os números de uma peça (deck, documento, planilha, página, PDF) com o lugar onde
cada um aparece, entendendo o formato brasileiro: R$ 1.234,56 · 20,4% · 3,2 p.p. · R$ 36,6 mi · 2 bi · 15 mil.

Depois procura dois sinais de erro:
  1. o mesmo rótulo aparecendo com valores diferentes (ex.: "margem 8,4%" numa tela e "margem 8,7%" noutra);
  2. o mesmo valor aparecendo com rótulos diferentes (pode ser a mesma métrica com nomes trocados).

Formatos: .pptx .docx .xlsx .md .txt .html .csv .pdf (PDF usa o pdftotext, se estiver instalado).
Só biblioteca padrão.

Uso:
  python3 extrai_numeros.py <arquivo> [--csv saida.csv] [--sem-notas]
"""
import csv, html, os, re, shutil, subprocess, sys, zipfile
for _s in (sys.stdout, sys.stderr):  # Windows grava em cp1252 quando a saida nao e terminal: forca UTF-8
    try:
        _s.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
from collections import defaultdict
from xml.etree import ElementTree as ET

UNID = r"(?:mi|milh(?:ão|ões|oes)|bi|bilh(?:ão|ões|oes)|mil|k|mm|MM)\b"
RX = re.compile(
    r"(?P<moeda>R\$|US\$|\$|€)?\s?"
    r"(?P<num>-?\d{1,3}(?:\.\d{3})+(?:,\d+)?|-?\d+(?:,\d+)?|-?\d+(?:\.\d+)?)"
    r"\s?(?P<suf>%|p\.?p\.?|pp\b|x\b|×|" + UNID + r")?",
    re.I)
MULT = {"mil": 1e3, "k": 1e3, "mi": 1e6, "milhão": 1e6, "milhões": 1e6, "milhoes": 1e6, "mm": 1e6,
        "bi": 1e9, "bilhão": 1e9, "bilhões": 1e9, "bilhoes": 1e9}
STOP = set("""a o as os de da do das dos e em no na nos nas um uma para por com que se sobre ao à é foi ser são
mais menos entre até cada como seu sua the of and in to vs x r mês ano anos dia dias total""".split())


def para_float(num, suf):
    s = num
    if re.fullmatch(r"-?\d{1,3}(\.\d{3})+(,\d+)?", s) or "," in s:
        s = s.replace(".", "").replace(",", ".")
    try:
        v = float(s)
    except ValueError:
        return None
    if suf:
        k = suf.lower().rstrip(".")
        v *= MULT.get(k, 1)
    return v


def unidade(m):
    suf = (m.group("suf") or "").lower().replace(".", "")
    moeda = m.group("moeda") or ""
    if suf == "%":
        return "%"
    if suf in ("pp", "p p"):
        return "p.p."
    if suf in ("x", "×"):
        return "vezes"
    if moeda:
        return moeda.upper()
    return ""


# ---------------------------------------------------------------- leitura por formato
def blocos_pptx(caminho, notas=True):
    z = zipfile.ZipFile(caminho)
    a = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
    slides = sorted([n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)],
                    key=lambda n: int(re.search(r"(\d+)", n.split("/")[-1]).group(1)))
    for n in slides:
        k = int(re.search(r"slide(\d+)", n).group(1))
        root = ET.fromstring(z.read(n))
        for i, p in enumerate(root.iter(a + "p"), 1):
            t = "".join(x.text or "" for x in p.iter(a + "t")).strip()
            if t:
                yield f"tela {k}", t
        if notas:
            nn = f"ppt/notesSlides/notesSlide{k}.xml"
            if nn in z.namelist():
                t = " ".join(x.text or "" for x in ET.fromstring(z.read(nn)).iter(a + "t")).strip()
                if t:
                    yield f"tela {k} (notas)", t


def blocos_docx(caminho):
    z = zipfile.ZipFile(caminho)
    w = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    for i, p in enumerate(ET.fromstring(z.read("word/document.xml")).iter(w + "p"), 1):
        t = "".join(x.text or "" for x in p.iter(w + "t")).strip()
        if t:
            yield f"parágrafo {i}", t


def blocos_xlsx(caminho):
    try:
        import openpyxl
    except ImportError:
        print("⚠️ Para ler .xlsx o extrator usa o openpyxl. Sem ele, rode perfil_base.py na planilha.", file=sys.stderr)
        return
    wb = openpyxl.load_workbook(caminho, read_only=True, data_only=True)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            rot = ""
            for c in row:
                if c.value is None:
                    continue
                if isinstance(c.value, str) and not re.search(r"\d", c.value):
                    rot = c.value
                    continue
                yield f"{ws.title}!{c.coordinate}", f"{rot} {c.value}".strip()


def blocos_texto(caminho):
    txt = open(caminho, encoding="utf-8", errors="replace").read()
    if caminho.lower().endswith((".html", ".htm")):
        txt = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", txt, flags=re.S | re.I)
        txt = re.sub(r"<br\s*/?>|</(p|div|li|tr|h\d)>", "\n", txt, flags=re.I)
        txt = html.unescape(re.sub(r"<[^>]+>", " ", txt))
    for i, linha in enumerate(txt.splitlines(), 1):
        if linha.strip():
            yield f"linha {i}", linha.strip()


def blocos_pdf(caminho):
    if not shutil.which("pdftotext"):
        print("⚠️ pdftotext não encontrado: instale o poppler ou exporte a peça em .docx/.pptx.", file=sys.stderr)
        return
    out = subprocess.run(["pdftotext", "-layout", caminho, "-"], capture_output=True, text=True).stdout
    for pg, pagina in enumerate(out.split("\f"), 1):
        for linha in pagina.splitlines():
            if linha.strip():
                yield f"página {pg}", re.sub(r"\s{2,}", "  ", linha.strip())


def blocos(caminho, notas=True):
    ext = caminho.lower().rsplit(".", 1)[-1]
    if ext == "pptx":
        return blocos_pptx(caminho, notas)
    if ext == "docx":
        return blocos_docx(caminho)
    if ext in ("xlsx", "xlsm"):
        return blocos_xlsx(caminho)
    if ext == "pdf":
        return blocos_pdf(caminho)
    return blocos_texto(caminho)


# ---------------------------------------------------------------- extração
def palavras(txt):
    return [w for w in re.findall(r"[a-zà-ú]{3,}", txt.lower()) if w not in STOP]


def extrair(caminho, notas=True):
    itens = []
    for local, txt in blocos(caminho, notas):
        for m in RX.finditer(txt):
            num = m.group("num")
            # ignora anos, datas e números de tela soltos sem unidade
            if re.fullmatch(r"(19|20)\d{2}", num) and not m.group("suf") and not m.group("moeda"):
                continue
            if re.match(r"\d{1,2}[/-]\d{1,2}", txt[m.start():m.start() + 6]):
                continue
            v = para_float(num, m.group("suf") if (m.group("suf") or "").lower().rstrip(".") in MULT else None)
            if v is None:
                continue
            ini, fim = max(0, m.start() - 70), min(len(txt), m.end() + 50)
            antes = re.split(r"[.;:!?](?:\s|$)|\(|\n", txt[max(0, m.start() - 90):m.start()])[-1]
            antes = antes.split(" ", 1)[-1] if m.start() > 90 else antes
            itens.append({"local": local, "valor": v, "texto": m.group(0).strip(), "unidade": unidade(m),
                          "contexto": txt[ini:fim].replace("\n", " "), "rotulo": " ".join(palavras(antes)[-3:])})
    return itens


def fmt(v):
    if abs(v) >= 1e9:
        return f"{v/1e9:.2f} bi".replace(".", ",")
    if abs(v) >= 1e6:
        return f"{v/1e6:.2f} mi".replace(".", ",")
    s = f"{v:,.4f}".rstrip("0").rstrip(".")
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)
    caminho = args[0]
    saida = args[args.index("--csv") + 1] if "--csv" in args else None
    itens = extrair(caminho, notas="--sem-notas" not in args)
    print(f"# Números de {os.path.basename(caminho)}\n")
    print(f"{len(itens)} números encontrados em {len(set(i['local'] for i in itens))} lugares.\n")
    print("| lugar | como está escrito | valor | unidade | rótulo provável | contexto |\n|---|---|---|---|---|---|")
    for it in itens:
        ctx = it["contexto"].replace("|", "/")
        print(f"| {it['local']} | {it['texto']} | {fmt(it['valor'])} | {it['unidade']} | {it['rotulo']} | {ctx} |")
    # sinal 1: mesmo rótulo, valores diferentes
    por_rot = defaultdict(list)
    for it in itens:
        if it["rotulo"] and it["unidade"] in ("%", "p.p.", "R$", "US$", "vezes"):
            por_rot[(it["rotulo"], it["unidade"])].append(it)
    print("\n## Mesmo rótulo com valores diferentes (conferir se é a mesma métrica)\n")
    n = 0
    for (rot, un), lst in por_rot.items():
        vals = sorted(set(round(i["valor"], 6) for i in lst))
        if len(vals) > 1 and len(set(i["local"] for i in lst)) > 1:
            n += 1
            print(f"- **{rot}** ({un}): " + " · ".join(f"{i['texto']} em {i['local']}" for i in lst))
    if not n:
        print("- nenhum caso encontrado pelo rótulo (a conferência fina continua com quem revisa)")
    # sinal 2: mesmo valor, rótulos diferentes
    print("\n## Mesmo valor com rótulos diferentes (pode ser a mesma métrica com nomes trocados)\n")
    por_val = defaultdict(list)
    for it in itens:
        if it["unidade"] in ("%", "R$") and it["rotulo"]:
            por_val[(round(it["valor"], 4), it["unidade"])].append(it)
    n = 0
    for (v, un), lst in por_val.items():
        rots = set(i["rotulo"] for i in lst)
        if len(rots) > 1:
            n += 1
            print(f"- {fmt(v)} {un}: " + " · ".join(f"\"{i['rotulo']}\" em {i['local']}" for i in lst))
    if not n:
        print("- nenhum caso")
    if saida:
        with open(saida, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["local", "texto", "valor", "unidade", "rotulo", "contexto"])
            w.writeheader()
            w.writerows(itens)
        print(f"\nTabela completa gravada em {saida}")


if __name__ == "__main__":
    main()
