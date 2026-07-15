---
name: otimizar-os
description: |
  Manutencao completa da documentacao de um contexto do seu OS em UM fluxo so: CONFERIR (os
  documentos batem com a realidade? drift de conteudo) + OTIMIZAR (estrutura, tamanho, promocao
  de regras). Funde e substitui as antigas skills separadas de organizar/compactar e de conferir docs.
  Analisa, propoe um plano e executa somente com a sua aprovacao.
  Executa quando o usuario diz "otimizar os", "compactar docs", "higienizar mds", "organizar contexto",
  "arquivos grandes", "reduzir documentos", "scan de saude", "splittar md", "mds orfaos",
  "confere mds", "confere docs", "auditar documentacao", "docs batem com a realidade?",
  "verificar documentacao", "docs drift", "sincronizar docs com codigo", "doc desatualizada".
  Default (sem flag) = confere primeiro (corrige conteudo), depois otimiza (estrutura).
version: 5.0
context: meuos
user-invocable: true
argument-hint: "[contexto] [--so-confere | --so-otimiza] (sem args = pergunta o contexto e roda as 2 fases)"
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Otimizar OS — Conferir + Otimizar a Documentacao de um Contexto

> **Duas fases, um fluxo.** A **FASE A (Conferir)** valida se os numeros e fatos dos seus documentos
> batem com a fonte-da-verdade (o codigo, o banco, as automacoes) — isso e drift de CONTEUDO.
> A **FASE B (Otimizar)** compacta, splitta, arquiva e promove regras — isso e drift de ESTRUTURA/tamanho.
>
> **Por que juntas?** Nao adianta organizar (mover, resumir, splittar) um documento que esta dizendo
> numeros errados — voce so estaria arrumando a bagunca em cima de informacao falsa. Entao a ordem
> natural e: **primeiro corrigir o conteudo (A), depois arrumar a estrutura (B)**.
>
> **Default (sem flag): A -> B.** Use `--so-confere` para so conferir o conteudo, ou `--so-otimiza`
> para so mexer na estrutura.

---

## O que esta skill faz (em uma frase)

Ela olha todos os documentos `.md` de UM contexto do seu OS, checa se o que eles afirmam ainda e
verdade, corrige o que estiver errado, e depois organiza/compacta o que estiver crescendo demais —
sempre te mostrando um plano e esperando o seu "pode ir" antes de qualquer mudanca.

> Duas analogias que ajudam:
> - **Conferir (Fase A)** e o **inventario fisico da loja**: de tempos em tempos alguem confere se o
>   que o sistema diz que tem na prateleira esta MESMO na prateleira. Se ninguem confere, o estoque
>   vira ficcao e todo mundo para de confiar nele.
> - **Otimizar (Fase B)** e a **arrumacao do armario**: separar o que e roupa do dia-a-dia (fica a mao)
>   do que e roupa de estacao (vai pra caixa la em cima), sem jogar nada fora.

---

## Quando usar

- Depois de uma sprint intensa (muita coisa mudou no produto/projeto).
- Quando o `changelog.md` cresceu 5+ entradas desde a ultima conferencia.
- Antes de compartilhar seus documentos com um socio, cliente ou parceiro.
- Quando alguem aponta uma inconsistencia ("ue, essa tabela nao existe mais?").
- Quando o agente alertou (na rotina de fim-do-dia) que ha arquivo com semaforo 🔴 ou drift de numeros.
- Ritual mensal ou trimestral de higiene, ou quando voce quiser "limpar o terreno".

---

# REGRA CRITICA — Identificar o contexto (antes de tudo)

**Esta skill SEMPRE roda em UM contexto por vez.** Antes de qualquer scan ou edicao, saber exatamente
qual pasta sera trabalhada:

- Se voce informou na chamada: usar esse.
- Se ficou obvio pela conversa: usar esse.
- Se houver duvida: **PERGUNTAR** —
  `"Em qual contexto vou rodar o otimizar-os? (ex: Pessoal / Consultoria/ClienteA / Produtos/MeuApp / Raiz)"`

**NUNCA escanear o OS inteiro de uma vez.** Se quiser cuidar de varios contextos, rodar a skill uma vez
por contexto. **Escopo**: opera SO nos arquivos da pasta do contexto escolhido — nunca toca outro contexto.

**Nota sobre profundidade:** seu OS pode estar em qualquer formato — adaptar ao que existir:
- **Flat (1 nivel):** arquivos direto na raiz.
- **Com pastas (2 niveis):** raiz + pastas de contexto.
- **Com subpastas (3 niveis):** raiz + pastas + subpastas.

Pastas sempre ignoradas no scan de tamanho: `historico/`, `tmp/`, `node_modules/`, `.git/`, `.meuos/`, `bkp/`.

---

# NUCLEO COMPARTILHADO (roda uma vez — serve as duas fases)

## N1 — Scan e dashboard de saude (semaforo UNICO)

Listar TODOS os `.md` do contexto escolhido (raiz do contexto + subpastas). Para o **scan de tamanho**,
ignorar `historico/`, `tmp/`, `node_modules/`, `.git/`, `bkp/`. Mas, para a **caca de orfaos (N3)**,
VARRER as subpastas (`docs/`, `prompts/`, `artefatos/`, etc.) — e la que arquivo perdido costuma se esconder.

Para cada arquivo: nome (com path) · numero de linhas · tamanho em KB · quantidade de `## ` · data de modificacao.
Apresentar uma tabela com o semaforo:

```
Relatorio de Saude — [Contexto]
Data: [DATA]

| Arquivo | Linhas | Tamanho | Status |
|---------|--------|---------|--------|
| claude.md | 95 | 6KB | 🟢 ok |
| CLIENTEA_DOCUMENTO_MESTRE.md | 487 | 28KB | 🔴 muito grande |
| aprendizados_do_dia.md | 220 | 14KB | 🟡 atencao |
| changelog.md | 210 | 18KB | 🟢 ok |
```

### Semaforo (tabela UNICA — vale para as duas fases)

| Tipo de arquivo | 🟢 OK | 🟡 Atencao | 🔴 Precisa de acao |
|---|---|---|---|
| `claude.md` | menos de 200 linhas | 200-300 | mais de 300 -> split em satelite |
| `*MESTRE.md` (qualquer nivel) | menos de 300 linhas | 300-500 | mais de 500 -> extrair secoes densas |
| Satelite tematico (ex: `CLIENTE_tech_api.md`) | menos de 25KB | 25-40KB | mais de 40KB -> split por tema |
| `changelog.md` | menos de 30KB | 30-50KB | mais de 50KB -> arquivar antigos em `historico/` |
| `aprendizados_do_dia.md` | menos de 200 linhas | 200-250 | mais de 250 -> migrar antigos p/ changelog/mestre |
| `index.md` | menos de 100 linhas | 100-150 | mais de 150 |
| Outros `.md` | menos de 20KB | 20-35KB | mais de 35KB |

### Custo fixo da sessao (o numero que REALMENTE importa)

Alem do tamanho de cada arquivo, somar os arquivos que carregam em TODA sessao do contexto —
`claude.md` raiz + `claude.md` do contexto + `*MESTRE.md` + `aprendizados_do_dia.md` + (se houver)
o `MEMORY.md` do agente. Reportar o total estimado em tokens (~1 linha ≈ 15 tokens) e a meta:

> `Custo fixo atual: ~18k tokens/sessao (mestre 7k + aprendizados 6k + claude.md 3k + memory 2k). Meta apos organizacao: ~9k.`

Esse e o numero que importa — e o que voce "paga" em TODA mensagem, nao o tamanho de um arquivo isolado.

## N2 — Descobrir as fontes-da-verdade disponiveis (para a Fase A)

Ler o `claude.md` e o `*MESTRE.md` do contexto procurando sinais de ONDE a realidade vive, e mapear
cada sinal para a fonte que responde:

| Sinal encontrado no documento | Fonte-da-verdade | Como checar |
|---|---|---|
| Menciona `github.com/USUARIO/REPO` ou existe pasta de repo clonado | Repo | clone local (busca/ls) OU um MCP de GitHub configurado |
| Menciona projeto Supabase (ref ou URL `*.supabase.co`) | Supabase | MCP de Supabase que corresponda ao projeto |
| Menciona workflows / IDs / "n8n" | n8n | MCP/API do n8n |
| Menciona lib externa versionada (Next.js, Stripe, etc.) | Documentacao oficial | consultar a doc oficial sob demanda (custa — so quando necessario) |

**Nao assumir a ferramenta pelo nome** — detectar qualquer MCP de GitHub/Supabase/n8n que estiver
configurado e usar o que corresponder ao contexto. Se uma fonte NAO estiver disponivel: **sinalizar mas
prosseguir**. Se NENHUMA fonte externa existir (so documentos), rodar em **modo consistencia-interna**:
detectar apenas contradicoes entre documentos, duplicacoes, orfaos e arquivos grandes — sem validar
numeros contra uma fonte externa. Voce pode ter so 1-2 fontes; a skill adapta o cardapio sem reclamar.

## N3 — Orfaos e ponteiros quebrados (drift interno — SEMPRE)

- **Orfao**: um `.md` que existe no disco (geralmente escondido numa subpasta) mas **nao tem ponteiro** no
  `index.md`, nem no `*MESTRE.md`, nem no `claude.md` do contexto. Sem ponteiro, o agente futuro nao sabe
  que aquele arquivo existe — conhecimento se perde silenciosamente.
- **Ponteiro quebrado**: o `index.md` ou o MESTRE citam um `.md` que nao existe mais (foi renomeado/movido).

Proposta padrao: adicionar o ponteiro (no `index.md`, e no MESTRE se for relevante) OU, se o conteudo
estiver obsoleto, arquivar em `historico/`. **NUNCA decidir sozinho** se um arquivo e relevante ou lixo —
apresentar a tabela e perguntar.

## N4 — Copias multiplas: espelho vs repo (cravar a fonte ANTES de editar) ⭐

Um mesmo documento pode ter DUAS copias: uma dentro do **repo** de codigo (`repo-*/DOC.md`, onde editar
significa fazer um commit) e um **espelho** na pasta do contexto (onde editar so mexe no arquivo local).
**Contra a intuicao, a copia do repo costuma estar MAIS atualizada** — porque e atualizada junto com cada
mudanca de codigo. Antes de corrigir qualquer documento que tenha espelho:

1. Atualizar o clone local do repo (`git pull`).
2. Comparar (`diff`) a copia do repo com o espelho -> cravar qual e a fonte-da-verdade.
3. Corrigir na fonte certa e re-sincronizar o espelho a partir dela. **Nunca editar so o espelho defasado**
   (voce corrige num lugar que ninguem le, e o erro volta no proximo sync).

## Gate "no piso, sem acao"

Antes de montar qualquer plano, verificar se ha mesmo o que fazer. Se depois do scan tudo esta 🟢, OU o
que passa do limite e majoritariamente **conteudo perene ja curado** (sem numeros errados, sem temporal
velho de mais de 60 dias, sem duplicata, sem secao densa extraivel), entao **parar aqui**:

> `"Este contexto ja esta no piso — o que carrega e conteudo perene necessario e os numeros batem. Rodar de novo so deterioraria os arquivos. Sem acao."`

**Nunca inventar plano quando nao ha ganho real.** Compactar conteudo perene irredutivel piora o OS — e o
oposto do objetivo da skill.

---

# FASE A — CONFERIR (drift de conteudo vs fonte-da-verdade)

> Objetivo: os numeros e fatos dos documentos batem com a realidade? Extrair as afirmacoes verificaveis,
> checar contra a fonte, apresentar o drift para aprovacao, corrigir. **Nunca inventar** um dado. **Nunca apagar.**
> (Pule esta fase inteira se rodou com `--so-otimiza`.)

## A1 — Bloco canonico de numeros (fonte unica de contagens) ⭐

**Principio anti-drift**: um numero (`N tabelas`, `N edge functions`, `N policies`, `N rotas`) deve morar
em UM lugar so. Escolha, por contexto, **um bloco canonico** — tipicamente o topo do documento tecnico/de
schema, marcado com `> Verificado ao vivo: DATA` — que e o UNICO documento com as contagens. Os demais
documentos **referenciam** esse bloco em vez de repetir o numero.

Por que isso importa: se o numero "24 tabelas" aparece copiado em 4 arquivos, no dia em que virar 25 voce
teria que lembrar de trocar nos 4 (e nunca lembra). Se ele mora num lugar so e os outros apontam pra la,
voce troca uma vez. Entao a Fase A valida 1 bloco canonico contra o vivo e varre os outros documentos so
buscando *contradicao com ele*. Se achar o mesmo numero repetido em varios arquivos, **propor colapsar as
copias em um ponteiro** pro bloco canonico.

## A2 — Extrair as afirmacoes verificaveis

Para cada documento ativo, procurar (por padrao de texto) as afirmacoes que dao pra checar contra a realidade:

1. **Contagens numericas**: numero seguido de `tabelas | edge functions | rotas | policies | prompts | workflows | telas | componentes | funcoes | intents`.
2. **Linhas de arquivo**: "arquivo X com ~N linhas".
3. **Modelos de IA citados**: `GPT-4`, `Claude Sonnet/Opus/Haiku`, `Gemini 2.x`, etc.
4. **Versoes declaradas**: `v1.2`, "Documento v2".
5. **Status de pendencias**: itens `[ ]` (aberto) e `[x]` (feito) em listas.
6. **URLs e IDs**: repos, projetos, workflows.
7. **Nomes de tabela/funcao/endpoint** entre crases (backticks).

Guardar cada afirmacao como `(arquivo, linha, tipo, valor)`. **Deduplicar** por `(tipo, valor)` para nao
checar a mesma coisa 5 vezes.

## A3 — Verificar cada afirmacao contra a fonte (em lote)

| Tipo de afirmacao | Como verificar |
|---|---|
| "N tabelas" | Listar tabelas no Supabase e contar |
| "N edge functions" | Listar functions + conferir a pasta no repo |
| "N policies" | SQL de contagem em `pg_policies` (schema `public`) |
| "N workflows" | Listar workflows no n8n (filtrar pelo dono/prefixo do contexto) |
| "N rotas" / "N telas" | Buscar no repo (pasta de router/telas) |
| "Arquivo X ~N linhas" | `wc -l` no clone local (tolerar +/- 10%) |
| "A IA principal e o modelo Y" | Buscar no codigo qual modelo e chamado de fato |
| "[x] pendencia resolvida" | Cruzar com changelog/codigo — foi mesmo resolvida? |

Fonte indisponivel -> marcar como **"nao verificavel neste ambiente"** e seguir. Nunca "chutar" o resultado.

## A4 — Inventario: total vivo + amostra curada + ponteiro (NAO regenerar de cabeca) ⭐

Quando a lista do documento esta defasada (ex: o doc lista 13 edge functions, mas existem 30), a tentacao e
reescrever a lista completa de memoria. **Nao faca isso** — voce acabaria inventando itens que nao confirmou
(e inventar dado e proibido). O padrao correto e:

- Corrigir o **total** (a contagem ao vivo, que voce checou).
- Manter/expandir uma **amostra curada** so com os itens cuja descricao voce confirmou na fonte.
- Deixar um **ponteiro pra fonte viva** (ex: "lista completa no painel do Supabase / `supabase functions list`").
- Rotular a lista explicitamente como **"nucleo curado"**, nunca como "lista completa".

Assim o documento fica honesto: um total correto + os itens que voce de fato conhece + o caminho pra ver o resto.

## A5 — Roteamento: doc local vs doc de repo (onde a edicao vai parar) ⭐

Antes de editar, classificar o alvo — porque "salvar" significa coisas diferentes dependendo de onde o
arquivo vive:

- **Doc local** (na pasta do contexto — satelite, `index.md`, `aprendizados_do_dia.md`): editar direto no
  arquivo. Livre para referenciar outros arquivos locais.
- **Doc de repo** (mora dentro de `repo-*/`, ex: `DOCUMENTACAO.md`): editar = **fazer commit** no repo.
  E esse documento **deve ser auto-contido** — nao pode referenciar a estrutura de pastas do seu OS (nada de
  "ver o MESTRE", "ver a pasta historico/"), porque quem le o repo nao enxerga o seu OS. Commitar SO o arquivo
  de documentacao (nunca arquivos de build ou temporarios).

## A6 — Montar 3 tabelas de drift para aprovacao (SEMPRE apresentar na integra)

**Tabela 1 — Ajustes de conteudo** (o que esta escrito errado):
```
| # | Arquivo:linha | Trecho atual | Mudanca proposta | Motivo (fonte-da-verdade) |
|---|---------------|--------------|------------------|---------------------------|
| A1 | MESTRE.md:L23 | "23 tabelas" | "24 tabelas" | Supabase lista 24 |
| A2 | CLIENTEA_TECH_API.md:L11 | "16 rotas" | "17 rotas (inclui /relatorios)" | busca no router = 17 |
```

**Tabela 2 — Estrutura / metadados** (orfaos, ponteiros quebrados, arquivos grandes, info vencida):
```
| # | Arquivo | Status sugerido | Motivo |
|---|---------|-----------------|--------|
| S1 | analise_antiga.md | Adicionar ponteiro no index OU arquivar | Arquivo orfao |
| S2 | MESTRE.md (580 linhas) | Marcar p/ split na Fase B | Acima de 500 linhas (🔴) |
| S3 | PLANO_SPRINT.md secao 2 | Remover secao | Informacao vencida (tudo executado) |
```

**Tabela 3 — Pendencias soltas para consolidar no MESTRE**:
```
| # | Pendencia | Onde estava | Sugestao |
|---|-----------|-------------|----------|
| P1 | Migrar modulo X | CLIENTEA_TECH_NOTAS.md | Promover ao MESTRE, secao Backlog |
```

**Regra de ouro**: apresentar TODAS as linhas, mesmo se a tabela ficar longa. Nao filtrar por "importancia"
— quem decide o que importa e voce.

Aprovados os ajustes, executar com **edicao cirurgica** (mexer so no trecho aprovado, nada ao redor). Se um
ajuste falhar, reportar e seguir com os demais — nao abortar o lote.

## A7 — Carimbo de frescor (orcamento de validade) ⭐

Todo documento que tem numeros ganha, no topo, um carimbo `> Verificado ao vivo: DD-MMM-AAAA` depois da
checagem. A skill sempre re-carimba ao validar. E — importante — ela **sinaliza qualquer documento de numeros
cujo carimbo esteja com mais de 45 dias**, mesmo sem outro gatilho. Esse carimbo velho e o sinal mais barato
de que uma doc pode ter silenciosamente defasado enquanto ninguem olhava.

Terminada a Fase A (ajustes aplicados e re-carimbados), seguir para a Fase B — a menos que voce tenha rodado
com `--so-confere`.

---

# FASE B — OTIMIZAR (estrutura / tamanho / promocao)

> Objetivo: reduzir o custo fixo e organizar. Classificar o conteudo por TIPO ANTES de olhar a idade.
> (Pule esta fase inteira se rodou com `--so-confere`.)

## B1 — Classificar o conteudo por TIPO (criterio primario, antes da idade)

Antes de olhar quantos dias tem o conteudo, classificar cada bloco pelo seu TIPO:

| Tipo | O que e | O que acontece |
|---|---|---|
| **Permanente** | Regras do negocio, padroes, convencoes, "nunca fazer X", config ativa | **Fica onde esta** — nao importa a idade, nunca compactar |
| **Promovivel** | Regra perene que voce usa em TODA sessao e devia estar no MESTRE | **Promover** (ver B4, com aprovacao) |
| **Temporario** | Entregas concluidas, bugs corrigidos, decisoes pontuais, status datados | Compacta conforme a idade (ver B2) |
| **Ultrapassado** | Status que nao vale mais, pesquisa ja usada, decisao substituida | **Arquivar** (`historico/` ou changelog) |

**Como identificar o tipo:**
- Contem "nunca", "sempre", "regra", "padrao", "obrigatorio" -> provavelmente **permanente**.
- Data especifica + resultado pontual ("Bug X corrigido em DD/MM") -> **temporario**.
- Referencia a estado passado ("aguardando X" quando X ja aconteceu) -> **ultrapassado**.
- Config de stack/schema em uso -> **permanente**.

## B2 — Idade (SO para conteudo temporario)

| Idade | O que fazer |
|---|---|
| Menos de 30 dias | Nao mexer — conteudo ativo |
| 30 a 60 dias | Condensar (3 paragrafos viram 3 linhas) |
| 60 a 90 dias | Condensar obrigatoriamente + mover detalhes para o changelog |
| Mais de 90 dias | Manter so 1 linha de resumo + ponteiro para o changelog |

## B3 — Split de secoes densas · arquivo do changelog · obsoletos

- **Secao densa**: quando um `*MESTRE.md` tem uma secao com mais de 50 linhas sobre UM unico tema, ela e
  candidata a virar um arquivo separado (satelite) na mesma pasta, com um ponteiro no MESTRE.
- **Changelog grande**: quando passa de 50KB, **quebrar por data** — mover as entradas antigas para arquivos
  datados em `historico/` (ex: `historico/CHANGELOG_2026_Q1.md` por trimestre), mantendo no changelog vivo
  so as entradas recentes + o cabecalho.
- **Obsoletos**: pesquisa/analise pontual ja concluida, status vencido -> mover para `historico/`.

## B4 — Promocao para o MESTRE (a "mielinizacao") + a regra da mesa e da gaveta

Algumas entradas nos aprendizados sao regras perenes (nao aprendizados datados). Elas nao deveriam ficar no
`aprendizados_do_dia.md` (que e um arquivo rolante). Mas o destino certo depende de COM QUE FREQUENCIA a
regra e usada:

| A regra e consultada... | Destino | Por que |
|---|---|---|
| em TODA sessao (ex: "nunca cruzar dados deste cliente") | **MESTRE** (secao de regras) | o mestre ja carrega toda sessao — custo zero adicional |
| so quando UM tema aparece (ex: taxas por perfil, regra de um modulo) | **satelite read-on-demand** + ponteiro de 1 linha no mestre | tira o peso da sessao; o agente abre o satelite so quando o assunto surge |

> Analogia: o MESTRE e a **mesa** (so o que pego toda hora). O satelite e a **gaveta** (guardo e abro quando
> o tema surge). Promover regra de tema especifico pra mesa nao reduz o imposto fixo — so muda de bolso.
> Mover pra gaveta reduz.

**Quando criar um satelite (as DUAS condicoes precisam ser verdade):**
1. O MESTRE ja esta **grande** (🟡 acima de 300 linhas; prioridade se 🔴 acima de 500). Mestre pequeno nao justifica satelite.
2. Ha **massa suficiente** sobre aquele tema (~40+ linhas sobre UM assunto). Nao criar satelite para 10 linhas — fragmenta sem ganho.

Candidatos a promocao: regra que vale pra TODA sessao + referenciada com frequencia + do tipo "NUNCA/SEMPRE"
+ mais de 30 dias sem contestacao. Apresentar a tabela `# | regra | origem | sugestao` e perguntar. **NUNCA
promover sem aprovacao.** Depois de aprovar, para cada regra: (1) vai para o destino certo; (2) e removida dos
aprendizados (para nao duplicar); (3) e registrada no changelog.

> ⚠️ **NUNCA promover regra operacional para o `soul.md`.** O soul trata SO de carater, comportamento e
> personalidade do agente — deve ser leve. Regra operacional (taxas, fluxos, "sempre fazer X no produto") vai
> para claude.md / mestre / satelite, nunca para o soul.

## B5 — Cemiterio de tarefas concluidas no MESTRE

A rotina de fim-do-dia cria linhas de referencia ao migrar tarefas (`~~[x] tarefa~~ -> ver changelog [data]`).
Elas se acumulam no MESTRE, que carrega em TODA sessao. A partir de ~15 dessas linhas-fantasma, colapsar todas
em UM unico ponteiro:
> `**Tarefas concluidas:** historico completo no changelog.`

## Plano + Execucao + Verificacao (Fase B)

1. **Plano**: apresentar uma lista NUMERADA, agrupada por tipo (resumir / split / arquivar / manter-sem-acao-com-justificativa),
   com o path completo de cada arquivo. Perguntar: `"Posso executar o plano completo? Ou prefere aprovar item por item?"`
   **NUNCA executar sem resposta.**
2. **Execucao** (so os itens aprovados):
   - **Resumir**: ler a secao original ANTES (nao perder nada) -> reescrever compacto -> conferir que nenhum link quebrou.
   - **Split**: criar o satelite com um cabecalho apontando pra cima (`> Documento pai: NOME_MESTRE.md`) e, no
     MESTRE, deixar um ponteiro apontando pra baixo (`> **[TEMA]:** resumo. Documento completo: [arquivo.md]`).
     Isso e o **ponteiro dos dois lados** — mantem a navegacao clara nos dois sentidos.
   - **Arquivar**: mover para `historico/` (criar a pasta se nao existir). **Nunca apagar.**
   - **Antes/depois**: para toda alteracao em arquivo existente, mostrar o trecho antes e depois e confirmar.
3. **Verificacao**: tabela `| arquivo | antes | depois | reducao |`.
4. **Atualizar o `index.md`** JUNTO com cada acao (nao esperar o final): adicionar entrada do satelite novo,
   remover entrada do que foi arquivado, atualizar data e contadores. Cada contexto tem seu `index.md`; a raiz
   tem o index geral que aponta pros contextos.

**Limite:** no maximo **3 satelites novos** por execucao — para nao fragmentar demais.

---

# Sensor de drift + integracao com o fim-do-dia (para manter "sempre atualizado") ⭐

O jeito de manter os documentos SEMPRE em dia nao e rodar esta skill inteira na mao toda hora — e um
**gatilho barato e automatico**:

- Toda vez que a skill roda, ela grava um carimbo em `{contexto}/historico/.last-otimizar-os` com:
  ```
  ULTIMA_EXECUCAO=AAAA-MM-DDTHH:MM
  CONTAGENS=tabelas:24,edge_functions:30,policies:52
  AJUSTES_CONTEUDO=N
  ITENS_ESTRUTURA=M
  FONTES=github,supabase,n8n,fs
  ```
- Na rotina de **fim-do-dia**, o agente le esse carimbo e roda um **ping de drift** bem barato (poucas
  contagens via a fonte do contexto), comparando com o que estava salvo. **So se houver diferenca** (ou o
  carimbo de frescor estiver com mais de 45 dias, ou o changelog cresceu 5+ entradas), ele sugere:
  > `"Detectei drift de numeros / doc velha — quer rodar o otimizar-os (fase confere)?"`
- O fim-do-dia **apenas sugere** — **NUNCA roda a skill sozinho.**

Assim voce so paga o custo de rodar a skill inteira quando ha mesmo o que corrigir.

---

## Regras de seguranca (valem para as duas fases)

- **NUNCA executar** ajuste, compactacao, split ou arquivamento **sem a sua aprovacao explicita.**
- **NUNCA apagar conteudo** — apenas mover (para `historico/` ou changelog).
- **NUNCA inventar** dado, lista ou contagem — se a fonte nao confirma, e "nao verificavel" ou vira ponteiro
  pra fonte viva. Hipotese nao e fato.
- **NUNCA resumir** regra de negocio fundamental, independente da idade.
- **NUNCA quebrar um link** — todo split deixa ponteiro dos dois lados.
- **NUNCA modificar** arquivos de outro contexto.
- **SEMPRE ler** o arquivo antes de editar (para nao perder nada) e verificar depois da edicao.
- **SEMPRE mostrar antes/depois** em alteracoes de arquivo existente.
- **SEMPRE apresentar as tabelas na integra**, mesmo longas — voce decide o que aprova.

## Convencao de nomes

- Satelite: `CONTEXTO_AREA_NOME.md` (AREA comum: TECH, COMERCIAL, PRODUTO, MKT, BI, DECISOES, CX, ANALISE) —
  ou simplesmente `CONTEXTO_nome-descritivo.md`. O importante e o nome dizer do que se trata.
- Arquivo do changelog: `historico/CHANGELOG_AAAA_Q[1-4].md`. Obsoleto: `historico/NOME_ORIGINAL.md`.

## O que esta skill NAO faz

- **NAO captura aprendizados conceituais novos** (isso e da rotina de fim-do-dia).
- **NAO altera codigo, banco ou automacoes** — so documentacao (a Fase A LE as fontes, nao as muda).
- **NAO faz auditoria de seguranca.**
- **NAO gera documento novo do zero** — so confere e organiza o que ja existe.

---

> **Nota:** esta skill FUNDE as antigas `otimizar-os` (organizar/compactar) + `confere-mds` (conferir docs
> contra a realidade) em um fluxo unico (jul/2026). A skill `confere-mds` foi **aposentada** — tudo que ela
> fazia agora vive aqui na **Fase A (Conferir)**.

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
