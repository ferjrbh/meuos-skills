---
name: MeuOS do Zero
description: |
  Monta, conserta e organiza o seu OS pessoal do ZERO — pra quem esta chegando ao modelo MeuOS,
  reconectou uma pasta fora do padrao, ou instalou as skills/arquivos errado. Roda na pasta atual
  (Claude Code, app ChatGPT/Codex, VSCode, Cursor, etc.), detecta em qual agente esta rodando,
  confirma se e a pasta certa, escaneia o que existe, infere seus contextos e confirma com voce,
  CLASSIFICA os arquivos .md avulsos propondo um destino pra cada um, e cria/repara a estrutura
  canonica DUAL (claude.md + AGENTS.md, soul.md, guia_do_os.md + contextos com
  documento_mestre/aprendizados_do_dia/changelog/index) usando os templates oficiais do MeuOS.
  Tambem verifica se as skills estao instaladas no lugar certo DO SEU agente. Nao-destrutiva:
  nunca apaga nem sobrescreve conteudo sem mostrar — no maximo MOVE, com aprovacao. Para
  aprender o modelo a fundo e manter as skills atualizadas, aponta pro curso em www.meuos.com.br.
  Executa quando o usuario diz "meuos do zero", "configurar meu os", "comecar meu os", "montar meu os",
  "instalei errado", "meu os ta baguncado", "nao tenho os ainda", "organizar meu os do zero",
  "consertar minha instalacao", "setup do os", "arrumar meu os", "organizar esta pasta no padrao".
version: 1.1
context: meuos
user-invocable: true
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# MeuOS do Zero — Montar, Consertar e Organizar seu OS

## O que esta skill faz

Esta skill coloca o seu OS pessoal no padrao MeuOS — seja porque voce esta **comecando do zero**
(ainda nao tem nada montado), porque **reconectou uma pasta** que ainda nao esta no padrao, ou
porque **instalou algo errado** (skill na pasta errada, arquivos faltando, estrutura torta).
Ela olha a pasta onde voce esta trabalhando, mostra o que falta ou esta fora do lugar, propoe um
destino para cada arquivo solto, e monta/conserta tudo **com a sua aprovacao** — usando os
templates oficiais do MeuOS.

> Esta e a skill do **dia zero**. Depois que seu OS estiver de pe, o dia a dia roda com as outras:
> `fim do dia` (ao encerrar), `otimizar OS` (quando os arquivos crescerem), `otimizar custo` (mensal).

---

## Quando usar

- Voce acabou de chegar ao MeuOS e ainda nao tem a estrutura de arquivos montada
- Conectou/reconectou uma pasta no MeuOS e o app avisou que ela esta fora do padrao
- Instalou as skills ou criou arquivos no lugar errado e quer arrumar
- Seu OS esta baguncado / incompleto e voce quer deixar no padrao
- Quando o usuario diz "meuos do zero", "configurar meu os", "comecar meu os", "arrumar meu os"

---

## Modelo canonico do MeuOS (o alvo) — DUAL desde 18-JUL-2026

O MeuOS fala **dois cerebros**: Claude e ChatGPT. Cada agente le uma porta de entrada diferente,
mas as REGRAS moram num lugar so — as entradas sao finas e nunca divergem.

**Na raiz do OS:**
| Arquivo | Para que serve |
|---------|----------------|
| `claude.md` | Entrada do CLAUDE — regras globais. Identidade, regras, mapa de contextos |
| `AGENTS.md` | Entrada do CHATGPT/Codex — fina, aponta pro claude.md ("leia-o como se fosse este arquivo") |
| `soul.md` | Personalidade do agente — tom, postura, papel. Leve, so comportamento |
| `guia_do_os.md` | Explica como o OS funciona |
| `index.md` | Catalogo geral — aponta pra tudo e pro index de cada contexto |

**Em cada contexto (pasta):**
| Arquivo | Para que serve |
|---------|----------------|
| `claude.md` | Regras especificas do contexto |
| `AGENTS.md` | Entrada ChatGPT do contexto — fina, aponta pro claude.md ao lado |
| `documento_mestre.md` | Documento vivo: escopo, status, pendencias, proximos passos |
| `aprendizados_do_dia.md` | Captura de conhecimento: Insight + Solucao + Nao fazer |
| `changelog.md` | Historico do que foi feito (append-only) |
| `index.md` | Catalogo da pasta |

**Sinais auxiliares** (podem existir — nunca sao problema):
- `.meuos/skills/` — skills instaladas pelo caminho ChatGPT/Codex (ficam DENTRO da pasta do OS)
- `MEMORY.md` — memoria persistente que o proprio agente cria com o tempo (nao vem do wizard)

> O OS pode ser **flat** (tudo na raiz), **com pastas** (raiz + contextos) ou **com subpastas**
> (raiz + pastas + subpastas). A skill se adapta ao que existir — nunca assume que e flat.
>
> **Regra anti-drift**: as entradas (claude.md e AGENTS.md) sao FINAS. Regra viva mora no
> soul.md (comportamento) e nos documentos de cada contexto — nunca duplicada nas duas entradas.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0 — Confirmar a pasta de trabalho (SEMPRE primeiro)

A skill trabalha na **pasta onde o agente esta rodando agora** (Claude Code, app ChatGPT em modo
Codex, VSCode, Cursor, etc.). Antes de qualquer coisa, mostrar o diretorio atual e confirmar:

> `"Estou rodando na pasta [CAMINHO_ATUAL]. E aqui que estao (ou vao ficar) os arquivos do seu OS —
> a pasta que voce quer que eu leia, analise e organize? Se nao for, abra seu agente na pasta certa
> ou me diga qual e."`

**Nao prosseguir sem confirmacao.** Se o usuario indicar outra pasta, usar essa.

### PASSO 0.5 — Detectar QUAL agente esta rodando (dual-agent)

Identifique-se: voce e o **Claude** (Claude Code/Desktop/CLI) ou o **ChatGPT/Codex** (app ChatGPT,
Codex CLI)? Isso muda DOIS caminhos ao longo da skill — anote e use consistentemente:

| | Rodando no Claude | Rodando no ChatGPT/Codex |
|---|---|---|
| Pasta de skills | `~/.claude/skills/{slug}/SKILL.md` | `.meuos/skills/{slug}/SKILL.md` (dentro da pasta do OS) |
| Registro extra | — | cada skill referenciada na secao `## Skills instaladas` do AGENTS.md da raiz |

Em outro agente (Cursor, Gemini CLI, etc.), pergunte ao usuario qual cerebro ele considera o
principal e use o caminho correspondente.

---

### PASSO 1 — Checar instalacao das skills

Verificar a pasta de skills **do agente detectado no PASSO 0.5**. Conferir se as **skills core do
MeuOS** estao presentes e validas (frontmatter ok, no lugar certo):

`meuos-do-zero` · `fim-do-dia` · `otimizar-os` · `otimizar-custo` · `conferir-entrega`

Para cada skill faltando, no lugar errado, ou com arquivo quebrado, anotar como item a corrigir no
diagnostico (PASSO 3). A correcao (PASSO 6) baixa a versao oficial do repo publico:
`https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/{slug}/SKILL.md`
e salva no caminho do SEU agente (tabela do PASSO 0.5).

> Nao reinstalar nada aqui — so diagnosticar. A correcao acontece no PASSO 6, com aprovacao.

---

### PASSO 2 — Escanear o OS atual

Escanear a pasta confirmada (ate 2 niveis de profundidade) para entender o que existe:

1. **Estrutura**: e flat, com pastas, ou com subpastas? Quais pastas parecem ser contextos?
2. **Arquivos canonicos na raiz**: existe `claude.md`? `AGENTS.md`? `soul.md`? `guia_do_os.md`?
   `index.md`? (`MEMORY.md` e `.meuos/` sao sinais auxiliares — registre se existirem.)
3. **Por contexto**: cada pasta-contexto tem `claude.md`, `AGENTS.md`, `documento_mestre.md`,
   `aprendizados_do_dia.md`, `changelog.md`, `index.md`?
4. **Inferir os contextos**: a partir das pastas e arquivos, deduzir quais sao os contextos de
   trabalho do usuario (ex: pastas com nome de cliente, projeto, area).
5. **Listar os .md AVULSOS**: todo arquivo .md que nao e canonico (na raiz ou solto em pastas) —
   anotacoes, rascunhos, docs antigos, exportacoes. Eles sao materia-prima do PASSO 4.5.

---

### PASSO 3 — Diagnostico (mostrar antes de agir)

Apresentar uma tabela do que esta ✓ certo, ✗ faltando, ⚠️ torto. Exemplo:

```
Diagnostico do seu OS (pasta [NOME]):

RAIZ
✓ Pasta existe
✗ Falta claude.md (suas regras globais — o agente esta sem norte)
✗ Falta AGENTS.md (a entrada do ChatGPT — sem ela o Codex trabalha "cego")
✗ Falta soul.md (personalidade do agente)
⚠️ index.md nao existe

CONTEXTOS (inferidos)
⚠️ "Cliente X" e "Financeiro" existem como pastas, mas sem documento_mestre.md nem aprendizados_do_dia.md

ARQUIVOS AVULSOS (11 .md sem lugar definido)
⚠️ notas-reuniao-maio.md, ideias.md, processos-antigos.md … (destino proposto no plano)

SKILLS (agente: Claude)
⚠️ otimizar-os instalada em ~/.claude/otimizar-os/ (errado) — o certo e ~/.claude/skills/otimizar-os/
✗ conferir-entrega nao instalada
```

---

### PASSO 4 — Mini-entrevista (so o essencial)

Coletar **apenas** o minimo para personalizar os arquivos — pulando o que o scan ja respondeu.
Nunca fazer um questionario longo (o onboarding completo e o aprofundamento ficam no curso, PASSO 7).

1. **Identidade**: `"Como quer que eu te chame? E em 1 linha: o que voce faz?"`
2. **Papel do agente**: `"Como prefere que eu atue? (a) direto ao ponto (b) didatico, com contexto
   e analogias (c) consultivo, apresentando opcoes e trade-offs"`
3. **Confirmar contextos** (a partir do PASSO 2): `"Pelo que li na sua pasta, voce tem estes contextos:
   [A, B, C]. Confere? Quer adicionar ou remover algum?"`

Se a pasta estiver vazia (sem contextos a inferir), perguntar: `"Quais sao seus contextos de trabalho?
Ex: um cliente, um projeto, financas pessoais."`

---

### PASSO 4.5 — Classificar os .md avulsos (o coracao da organizacao)

Para CADA arquivo avulso do PASSO 2, **ler o comeco do arquivo** (titulo + primeiras linhas bastam)
e propor um destino — em tabela, pra aprovacao em bloco:

| Destino proposto | Quando |
|---|---|
| **Mover pra pasta do contexto [X]** | o conteudo claramente pertence aquele contexto (cliente, projeto, area) |
| **Fundir num canonico** | e uma versao solta do que o canonico deveria conter (ex: "minhas regras.md" → conteudo vira secao do claude.md; "historico.md" → changelog.md) |
| **Manter como satelite** | doc de referencia vivo e especifico — fica na pasta do contexto com nome claro |
| **`historico/` do contexto** | doc antigo/concluido que vale guardar mas nao vale ler sempre |
| **Deixar onde esta** | quando o usuario preferir — a proposta e sugestao, nunca imposicao |

Regras desta etapa:
- **NUNCA apagar** arquivo do usuario — no maximo MOVER ou FUNDIR (fundir = copiar o conteudo pro
  destino e mover o original pra `historico/`), sempre com aprovacao.
- Arquivo ilegivel/ambiguo → perguntar, nunca chutar destino.
- Mostrar a tabela completa ANTES de mover qualquer coisa; o usuario pode aprovar em bloco ou
  ajustar linha a linha.

---

### PASSO 5 — Plano de acao (sempre antes de executar)

Apresentar lista NUMERADA do que sera criado/corrigido/movido, indicando que **nada e feito sem
aprovacao**:

```
Plano (nada e criado sem seu OK):
1. Criar claude.md na raiz (suas regras + mapa dos contextos) — template MeuOS
2. Criar AGENTS.md na raiz (entrada do ChatGPT, apontando pro claude.md)
3. Criar soul.md e guia_do_os.md na raiz
4. Criar index.md da raiz
5. Em cada contexto (A, B, C): criar claude.md, AGENTS.md, documento_mestre.md,
   aprendizados_do_dia.md, changelog.md, index.md
6. Mover 8 arquivos avulsos conforme a tabela aprovada (3 pro contexto A, 2 fundidos, 3 pro historico/)
7. Mover a skill otimizar-os pra pasta certa + instalar conferir-entrega

Posso executar tudo, ou prefere aprovar item por item?
```

**NUNCA executar sem resposta do usuario.**

---

### PASSO 6 — Execucao (somente com aprovacao)

Para cada item aprovado:

**6a. Criar arquivo a partir do template oficial**
1. Baixar o template correspondente do repo publico:
   `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/meuos-do-zero/templates/{arquivo}`
   - Raiz: `claude-raiz.md` · `agents-raiz.md` · `soul.md` · `guia_do_os.md` · `index-raiz.md`
   - Contexto: `contexto-claude.md` · `agents-contexto.md` · `documento-mestre.md` ·
     `aprendizados-do-dia.md` · `changelog.md` · `index-contexto.md`
2. Substituir os marcadores pelas respostas da mini-entrevista:
   `{{NOME}}` · `{{NOME_OS}}` · `{{IDENTIDADE}}` · `{{PAPEL_AGENTE}}` · `{{ESTILO}}` · `{{CONTEXTO}}` · `{{LISTA_CONTEXTOS}}` · `{{DATA}}`
3. Salvar com o **nome final correto** (ex: `documento-mestre.md` → `documento_mestre.md`;
   `agents-raiz.md` → `AGENTS.md` na raiz; `agents-contexto.md` → `AGENTS.md` na pasta do contexto).

**6b. Nao-destrutivo — regra de ouro**
- Se o arquivo **ja existe**, NUNCA sobrescrever direto. Mostrar o que tem hoje vs o template e
  perguntar: completar o que falta, ou deixar como esta.
- **Caso especial AGENTS.md**: se o claude.md ja existe com conteudo proprio (customizado), o
  AGENTS.md criado e o PONTEIRO FINO do template (aponta pro claude.md) — NUNCA uma copia do
  conteudo. Copiar criaria duas fontes que divergem com o tempo.
- So criar do zero o que **nao existe**. Mover so o que foi aprovado no PASSO 4.5.

**6c. Corrigir skills (se aprovado)**
- Baixar a skill do repo publico e salvar no caminho do SEU agente (tabela do PASSO 0.5).
- Rodando no ChatGPT/Codex: alem de salvar em `.meuos/skills/`, adicionar a referencia na secao
  `## Skills instaladas` do AGENTS.md da raiz (criar a secao se nao existir).
- Se estava na pasta errada, criar no lugar certo e avisar o usuario sobre a copia antiga.

**6d. Confirmar cada criacao** — ao final, listar os arquivos criados/corrigidos/movidos.

---

### PASSO 7 — Fechamento + curso

Fechar mostrando o resultado e apontando pro aprofundamento (a skill **nao** ensina o modelo a
fundo — isso e o curso):

> `"Pronto — seu OS esta de pe e organizado, falando Claude E ChatGPT. 🎯`
> `Pra aprender a tirar o maximo dele e manter suas skills sempre atualizadas, faca o curso e entre`
> `na comunidade em www.meuos.com.br — e la que ensinamos o modelo a fundo e publicamos as novas`
> `versoes das skills.`
> `No dia a dia: feche com 'fim do dia'; quando os arquivos crescerem, 'otimizar OS'; mensalmente,`
> `'otimizar custo'."`

---

## Regras de seguranca

- **Sempre confirmar a pasta de trabalho** antes de escanear (PASSO 0) — evita montar OS no lugar errado
- **Nunca executar sem aprovacao** — diagnostico e plano primeiro, acao depois
- **Nunca APAGAR arquivo do usuario** — no maximo mover/fundir, com aprovacao (o original preservado em `historico/`)
- **Nunca sobrescrever conteudo existente** sem mostrar antes/depois e perguntar
- **Nunca inventar** os contextos do usuario — inferir e confirmar
- **Nunca duplicar regras entre claude.md e AGENTS.md** — a entrada do outro agente e sempre o ponteiro fino
- **Nunca fazer questionario longo** — so o essencial; o resto e o curso
- **Nunca colocar regra operacional no soul.md** — soul e so personalidade/comportamento, leve
- Usar **sempre os templates oficiais** do repo (nao improvisar estrutura)

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
