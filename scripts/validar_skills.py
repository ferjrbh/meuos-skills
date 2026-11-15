"""Valida todas as skills do catalogo. Roda no GitHub a cada push (ver .github/workflows/validar-skills.yml).
Uso local: python scripts/validar_skills.py
"""
import pathlib, re, sys
import yaml

RAIZ = pathlib.Path(__file__).resolve().parent.parent
AUTOR = "Fernando Lúcio · Aion Group"
RODAPE = ("> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · "
          "Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)")
NOME_OK = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

erros = []
pastas = sorted(p for p in (RAIZ / "skills").iterdir() if p.is_dir())
for pasta in pastas:
    arq = pasta / "SKILL.md"
    if not arq.exists():
        erros.append(f"{pasta.name}: falta o SKILL.md"); continue
    texto = arq.read_text(encoding="utf-8").replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---\n", texto, re.S)
    if not m:
        erros.append(f"{pasta.name}: cabecalho (frontmatter) ausente ou mal fechado"); continue
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        erros.append(f"{pasta.name}: YAML invalido no cabecalho ({str(e).splitlines()[0]})"); continue
    if not isinstance(fm, dict):
        erros.append(f"{pasta.name}: cabecalho nao e um mapa YAML"); continue
    nome = fm.get("name")
    if nome != pasta.name:
        erros.append(f"{pasta.name}: name '{nome}' precisa ser igual ao nome da pasta")
    elif not NOME_OK.match(str(nome)):
        erros.append(f"{pasta.name}: name so com minusculas, numeros e hifen")
    if not str(fm.get("description") or "").strip():
        erros.append(f"{pasta.name}: description vazia")
    if fm.get("version") in (None, ""):
        erros.append(f"{pasta.name}: falta version")
    if fm.get("author") != AUTOR:
        erros.append(f"{pasta.name}: author fora do padrao ('{fm.get('author')}')")
    if texto.count(RODAPE) != 1:
        erros.append(f"{pasta.name}: rodape oficial aparece {texto.count(RODAPE)}x (esperado 1)")
    if texto.count("```") % 2:
        erros.append(f"{pasta.name}: bloco de codigo aberto e nao fechado")

print(f"{len(pastas)} skills conferidas, {len(erros)} problema(s)")
for e in erros:
    print(" -", e)
sys.exit(1 if erros else 0)
