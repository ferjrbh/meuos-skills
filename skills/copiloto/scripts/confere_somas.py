#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere se as parcelas de uma tabela fecham o total, do jeito que o leitor confere: somando o que está impresso.

Regra da casa: arredonda-se cada parcela e somam-se as parcelas arredondadas. Arredondar o total calculado
produz tabela que não fecha na conta de quem lê.

Uso:
  python3 confere_somas.py --partes "39,9; 38,8; 4,5; 3,7; 10,0; 3,1" --total "100"
  python3 confere_somas.py --partes "..." --total "..." --casas 1
  python3 confere_somas.py --csv tabela.csv --coluna valor [--rotulo nome] [--linha-total Total]

Aceita formato brasileiro (1.234,56) e americano (1,234.56). Só biblioteca padrão.
"""
import csv, re, sys
for _s in (sys.stdout, sys.stderr):  # Windows grava em cp1252 quando a saida nao e terminal: forca UTF-8
    try:
        _s.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def limpa(s):
    """Tira moeda, %, espaços; troca o sinal de menos tipográfico; parêntese contábil vira negativo."""
    s = str(s).strip().replace("R$", "").replace("%", "").replace("\u00a0", "").replace(" ", "")
    s = s.replace("\u2212", "-").replace("\u2013", "-")
    if s.startswith("(") and s.endswith(")"):
        s = "-" + s[1:-1]
    return s


def num(s):
    s = limpa(s)
    if not s:
        return None
    if re.fullmatch(r"-?\d{1,3}(\.\d{3})+(,\d+)?|-?\d+,\d+", s):
        s = s.replace(".", "").replace(",", ".")
    else:
        s = s.replace(",", "")
    try:
        return float(s)
    except ValueError:
        return None


def casas_de(txts):
    c = 0
    for t in txts:
        u = limpa(t).lstrip("-")
        m = re.search(r"[.,](\d+)$", u)
        if m and not re.fullmatch(r"\d{1,3}(\.\d{3})+", u):
            c = max(c, len(m.group(1)))
    return c


def br(x, casas):
    s = f"{x:,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def conferir(partes_txt, total_txt, casas=None, rotulos=None):
    partes = [num(p) for p in partes_txt]
    if any(p is None for p in partes):
        print("⚠️ Parcela que não é número:", [t for t, p in zip(partes_txt, partes) if p is None])
        partes = [p for p in partes if p is not None]
    total = num(total_txt) if total_txt is not None else None
    if casas is None:
        casas = casas_de(list(partes_txt) + ([total_txt] if total_txt else []))
    soma = sum(partes)
    tol = 0.5 * 10 ** (-casas) if casas else 0.5
    print(f"Parcelas: {len(partes)} · casas decimais impressas: {casas}")
    print(f"Soma das parcelas como estão impressas: {br(soma, casas)}")
    if total is None:
        print("Sem total impresso para comparar.")
        return 0
    dif = soma - total
    print(f"Total impresso: {br(total, casas)} · diferença: {br(dif, casas)}")
    if abs(dif) < 1e-9:
        print("✅ Fecha na conta do leitor.")
        return 0
    if abs(dif) <= tol * len(partes):
        print(f"🟡 Não fecha por arredondamento (diferença dentro de meia unidade por parcela). O leitor vai ver a conta "
              f"não bater. Correção: ajustar a maior parcela em {br(-dif, casas)} ou mostrar o total como a soma das "
              f"parcelas impressas, com nota.")
        return 1
    print("🔴 Não fecha, e a diferença é maior que o arredondamento explica: falta parcela, sobra parcela ou o total é de outra base.")
    return 2


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(1)
    casas = int(a[a.index("--casas") + 1]) if "--casas" in a else None
    if "--partes" in a:
        partes = [p for p in re.split(r"[;\n]", a[a.index("--partes") + 1]) if p.strip()]
        total = a[a.index("--total") + 1] if "--total" in a else None
        sys.exit(conferir(partes, total, casas))
    if "--csv" in a:
        arq, col = a[a.index("--csv") + 1], a[a.index("--coluna") + 1]
        rot = a[a.index("--rotulo") + 1] if "--rotulo" in a else None
        lt = a[a.index("--linha-total") + 1].lower() if "--linha-total" in a else "total"
        txt = open(arq, encoding="utf-8-sig").read()
        sep = ";" if txt[:2000].count(";") > txt[:2000].count(",") else ","
        linhas = list(csv.DictReader(txt.splitlines(), delimiter=sep))
        partes, total = [], None
        for l in linhas:
            nome = (l.get(rot) or "") if rot else " ".join(l.values())
            if lt in nome.lower():
                total = l[col]
            else:
                partes.append(l[col])
        sys.exit(conferir(partes, total, casas))
    print(__doc__)


if __name__ == "__main__":
    main()
