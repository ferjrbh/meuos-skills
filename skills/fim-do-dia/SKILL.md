---
name: Revisao Diaria
description: |
  Rotina de encerramento do dia de trabalho. Executa quando o usuario diz
  "revisao diaria", "fechar o dia", "encerrar", "fim do dia", "vamos fechar",
  "pode fechar", "encerra ai", "wrap-up", "encerrar sessao".
  Guia 3 perguntas rapidas, salva aprendizados, migra tarefas concluidas
  e atualiza pendencias no documento mestre do contexto ativo.
version: 3.3
context: meuos
user-invocable: true
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Revisao Diaria — Encerramento do Dia

## O que esta skill faz

Esta skill guia voce por uma rotina rapida de fechamento do dia de trabalho — menos de 10 minutos. Ela faz tres perguntas simples sobre o que aconteceu hoje, salva os aprendizados no lugar certo, move tarefas concluidas para o historico e deixa suas pendencias atualizadas para o proximo dia. Ao final, avisa se algum arquivo esta crescendo demais e precisa de organizacao.

---

## Quando usar

- Ao final de qualquer sessao de trabalho produtiva
- Quando quiser registrar uma decisao importante antes de esquecer
- Quando quiser deixar o contexto organizado antes de uma pausa longa
- Quando o agente sugerir proativamente ao perceber que a sessao foi longa

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0 — Identificar o contexto e mapear a estrutura

Antes de qualquer acao, identificar qual contexto esta sendo fechado:
- Se o usuario informou: usar esse
- Se ficou obvio pela conversa: usar esse
- Se houver duvida: perguntar `"Em qual contexto estamos fechando o dia? (Pessoal / [Nome da Empresa]?)"`

**Nota sobre profundidade do OS:** O usuario pode ter um OS em qualquer uma destas configuracoes — adaptar ao que existir:
- **Flat (1 nivel):** arquivos diretamente na raiz do OS
- **Com pastas (2 niveis):** raiz + pastas de contexto (ex: `Consultoria/`)
- **Com subpastas (3 niveis):** raiz + pastas + subpastas (ex: `Consultoria/ClienteA/`)

Ao iniciar, fazer um scan rapido da estrutura ate 2 niveis de profundidade para entender o que existe. Exemplo de estrutura com 3 niveis:

```
MeuOS/                              ← raiz (nivel 0)
├── claude.md
├── soul.md
├── aprendizados_do_dia.md
├── changelog.md
├── Consultoria/                    ← pasta (nivel 1)
│   ├── claude.md
│   ├── aprendizados_do_dia.md
│   ├── changelog.md
│   ├── ClienteB/                   ← subpasta (nivel 2)
│   │   ├── CLIENTEB_DOCUMENTO_MESTRE.md
│   │   ├── aprendizados_do_dia.md
│   │   └── changelog.md
│   └── ClienteA/
│       ├── CLIENTEA_DOCUMENTO_MESTRE.md
│       ├── aprendizados_do_dia.md
│       └── changelog.md
└── Produtos/
    └── ...
```

O contexto ativo pode ser qualquer nivel. Identificar exatamente qual pasta esta sendo fechada e trabalhar nela.

---

### PASSO 1 — Sintetizar e Confirmar (informar antes de gravar)

**Principio:** o agente faz o trabalho de sintese, o usuario apenas valida ou ajusta. Nunca perguntar perguntas abertas — apresentar uma sintese da sessao e pedir confirmacao/ajuste.

**Fluxo:**

1. **Sintetizar a sessao** lendo o historico da conversa atual + o `aprendizados_do_dia.md` recente do contexto. Estruturar em 3 blocos (qualquer um pode estar vazio):

```
Sintese da sessao de hoje no contexto [CONTEXTO]:

📌 O QUE FIZEMOS:
- [item 1 — entrega/decisao/correcao]
- [item 2]
(ou "Sessao de discussao/analise — sem entregas concretas")

💡 O QUE APRENDEMOS:
- [aprendizado 1 — formato Insight/Solucao/Nao fazer]
- [aprendizado 2]
(ou "Sem aprendizados novos relevantes nesta sessao")

🔜 O QUE FICA PRA AMANHA:
- [pendencia nova ou antiga que continua aberta]
(ou "Nenhuma pendencia nova — pendencias antigas seguem em aberto no MESTRE")
```

2. **Apresentar ao usuario** e pedir:
   > `"Confere essa sintese? Pode confirmar, ajustar, adicionar ou remover qualquer item."`

3. **Aguardar resposta** — o usuario pode:
   - "Confirmado, pode salvar"
   - "Tira o item 2 dos aprendizados, o resto OK"
   - "Adiciona X em pendencias"
   - "Nao teve aprendizado novo hoje, segue so com o que fizemos"
   - "Sessao foi de leitura/discussao, nao tem nada pra registrar — pula"

4. **Aplicar a decisao**:
   - Se houver "o que fizemos" confirmado → vai pro changelog (PASSO 3)
   - Se houver "o que aprendemos" confirmado → vai pro `aprendizados_do_dia.md` (formato Insight/Solucao/Nao fazer)
   - Se houver "o que fica pra amanha" confirmado → atualiza pendencias no `*MESTRE.md` (PASSO 4)
   - Se o usuario disse "pula" ou "nao tem nada" → nao gravar nada e seguir para PASSO 5 (saude dos arquivos)

**REGRA CRITICA — nao forcar conteudo:**
- Sessao pode ter sido **so de leitura/analise** sem entregas → "O QUE FIZEMOS" pode listar so a discussao sem ir pro changelog
- Sessao pode ter zero aprendizados novos → "O QUE APRENDEMOS" fica vazio e nada vai pro aprendizados
- Sessao pode nao gerar pendencias novas → "O QUE FICA PRA AMANHA" so lista pendencias antigas
- **NUNCA inventar** aprendizados ou pendencias para "preencher" os 3 blocos. Se esta vazio, esta vazio. Forcar registro polui os arquivos.

---

### PASSO 2 — Salvar aprendizados

Com base na resposta da Pergunta 2, escrever no arquivo `aprendizados_do_dia.md` do contexto ativo.

**Localizar o arquivo correto:** buscar `aprendizados_do_dia.md` na pasta exata do contexto que esta sendo fechado. Com 3 niveis, cada pasta tem o seu proprio — usar o da pasta correta. Exemplos:
- Fechando contexto raiz: `aprendizados_do_dia.md` na raiz
- Fechando contexto Consultoria/ClienteA: `Consultoria/ClienteA/aprendizados_do_dia.md`

**Formato de cada entrada:**

```markdown
## [Titulo curto descritivo] (DD/MM)

**Insight:** [O que foi aprendido — 1 a 2 frases diretas]

**Solucao:** [Como foi resolvido ou qual foi a decisao tomada — 1 a 2 frases]

**Nao fazer:** [Regra que evita repetir o problema — 1 frase clara]
```

**Ordem no arquivo (mais importante primeiro):**
1. Regras de Negocio (decisoes sobre como o produto/empresa funciona)
2. Estrategicos (decisoes de produto, posicionamento, modelo)
3. Tecnicos (ferramentas, bugs, integracoes)

**Regra de compactacao:** se o arquivo `aprendizados_do_dia.md` ja tiver mais de 25 entradas, agrupar entradas antigas sobre o mesmo tema em uma entrada unica antes de adicionar as novas.

**Limites de higiene (apresentar candidatos a migracao para o changelog quando qualquer um for ultrapassado):**

| Metrica | Limite | Acao se exceder |
|---------|--------|-----------------|
| Linhas do `aprendizados_do_dia.md` | mais de 250 | Propor migracao de entradas antigas para `changelog.md` |
| Numero de entradas `## ` | mais de 25 | Propor migracao/agrupamento |
| Items `[x]` no `*MESTRE.md` | mais de 0 | Migrar para `changelog.md` (ver PASSO 3) |

Se algum limite for ultrapassado, apresentar tabela numerada ao usuario com os candidatos a migracao:

```
| # | Entrada | Sugestao | Destino |
|---|---------|----------|---------|
| 1 | Incidente Fraude CNPJ (03/04) | Migrar | changelog.md |
| 2 | API Asaas = so GET (regra permanente) | Promover | *MESTRE.md secao Regras |
| 3 | Bug no envio de email (31/03) | Migrar | changelog.md |
| 4 | Padrao de prompt OpenAI (ativo) | Manter | aprendizados_do_dia.md |
```

O usuario responde quais aprovar (ex: "1 e 3 sim") e so o aprovado e movido. **NUNCA migrar sem aprovacao.**

---

### PASSO 3 — Migrar tarefas concluidas

Ler o arquivo `*MESTRE.md` do contexto ativo. O documento mestre pode ter qualquer nome terminando em `MESTRE.md` — exemplos: `CLIENTEA_DOCUMENTO_MESTRE.md`, `CLIENTEB_DOCUMENTO_MESTRE.md`, `CLIENTEC_DOCUMENTO_MESTRE.md`. Buscar pelo pattern `*MESTRE.md` na pasta do contexto.

Identificar todos os itens marcados como concluidos (formato `[x]`).

**Para cada item concluido:**
1. Adicionar no `changelog.md` com a data de hoje:

```markdown
### [DATA] — [Titulo curto]

- [Item concluido 1]
- [Item concluido 2]
- [Decisao tomada, se houver]
```

2. No `*MESTRE.md`, substituir o item `[x]` por uma linha de referencia:

```markdown
- ~~[x] [Descricao da tarefa]~~ → ver changelog [DATA]
```

**IMPORTANTE:** Nunca apagar conteudo do documento mestre sem mostrar ao usuario o que sera movido e pedir confirmacao. Mostrar lista resumida e perguntar:
> `"Encontrei X itens concluidos. Posso migrá-los para o changelog?"`

---

### PASSO 4 — Atualizar pendencias

Com base na resposta da Pergunta 3, atualizar a lista de pendencias no `*MESTRE.md` do contexto ativo:

- Adicionar novas pendencias informadas pelo usuario (formato `[ ] [descricao]`)
- Manter as pendencias antigas que continuam abertas
- Atualizar a data de "Ultima atualizacao" no cabecalho do documento mestre

---

### PASSO 5 — Verificar saude dos arquivos

Verificar o tamanho dos arquivos do contexto ativo e apresentar um relatorio rapido. Cobrir todos os arquivos da pasta do contexto sendo fechado (nao escanear outros contextos neste passo — apenas o ativo).

| Arquivo | Status |
|---------|--------|
| `*MESTRE.md` | 🟢 OK / 🟡 Atencao / 🔴 Grande |
| `aprendizados_do_dia.md` | 🟢 OK / 🟡 Atencao / 🔴 Grande |
| `changelog.md` | 🟢 OK / 🟡 Atencao / 🔴 Grande |

**Regras de semaforo:**
| Arquivo | 🟢 OK | 🟡 Atencao | 🔴 Grande |
|---------|-------|-----------|---------|
| `*MESTRE.md` | menos de 300 linhas | 300 a 500 | mais de 500 |
| `aprendizados_do_dia.md` | menos de 200 linhas | 200 a 250 | mais de 250 |
| `changelog.md` | menos de 30KB | 30 a 50KB | mais de 50KB |

**Sugerir o Otimizar OS no MAXIMO 1x por semana, e so se houver volume.** Antes de sugerir, ler
`{contexto}/historico/.last-otimizar-os` (guarda `ULTIMA_EXECUCAO`, `LAST_SUGGESTED`, `CONTAGENS`, `FRESCOR`).
So sugerir se as DUAS condicoes forem verdade:

1. **Porta de volume** (ha motivo real — senao, silencio, mesmo passada a semana):
   - arquivo 🔴 REDUTIVEL (temporal velho / cemiterio de tarefas / secao densa extraivel); OU
   - `aprendizados_do_dia.md` grande por excesso de regra perene (extraivel para satelite); OU
   - **drift de numeros**: reconferir 2-4 contagens vivas (tabelas/rotas/etc. na fonte-da-verdade do contexto) vs `CONTAGENS` salvas — se mudou, ha volume; OU
   - carimbo `Verificado ao vivo` com mais de 45 dias; OU o `changelog.md` cresceu 5+ entradas desde a ultima execucao.
2. **Teto de cadencia**: `hoje - max(ULTIMA_EXECUCAO, LAST_SUGGESTED)` for de **7 dias ou mais**.

Ao sugerir, gravar `LAST_SUGGESTED=<hoje>` no `.last-otimizar-os` (segura o lembrete na semana, mesmo se voce recusar).
- Sugestao geral: `"Identifiquei [numeros defasados / arquivos compactaveis]. Recomendo rodar o Otimizar OS. Quer agora? (ultima vez: [data])"`
- Se for o `aprendizados_do_dia.md` inchado de regra perene: `"Seu aprendizados virou deposito de regras. O Otimizar OS extrai pra satelite e deixa o log curto. Quer rodar?"`
- Conteudo perene ja curado (piso) e sem drift → **NAO sugerir nada**. Repetir alerta sem acao possivel e ruido.

---

### PASSO 5.5 — Descompressao do documento mestre (condicional)

**Executar SOMENTE se o `*MESTRE.md` do contexto ativo tiver mais de 300 linhas**, OU se houve entregas significativas na sessao (modulo inteiro, integracao completa, decisao arquitetural grande). Em sessoes curtas ou de manutencao, pular.

**Objetivo:** manter o documento mestre legivel em menos de 5 minutos. Escopo, status, pendencias e ponteiros ficam la. Detalhes densos saem para arquivos separados.

**Fluxo (com aprovacao do usuario em cada passo):**

1. **Contar as linhas do mestre.** Se menos de 300, pular.
2. **Identificar secoes densas** — qualquer secao com mais de 30 linhas de conteudo detalhado sobre UM tema especifico (decisoes por data, especificacoes de modulo, mapeamentos, etc.).
3. **Propor extracao ao usuario** listando as secoes candidatas e o nome do arquivo separado sugerido, usando a convencao `CONTEXTO_AREA_TEMA.md`.
4. **Se aprovado:** criar o arquivo separado na mesma pasta do mestre.
5. **Substituir no mestre** por um ponteiro de 2 a 3 linhas: resumo curto + `ver CONTEXTO_AREA_TEMA.md`.
6. **Limite:** maximo 3 arquivos separados novos por execucao (evita fragmentacao).

**Convencao de nomes:**
- `CONTEXTO` = prefixo do projeto (CLIENTEA, CLIENTEC, MINHA_EMPRESA, etc.)
- `AREA` = area tematica (TECH, PRODUTO, COMERCIAL, MKT, DECISOES, etc.)
- `TEMA` = assunto especifico (DECISOES_ABRIL, INTEGRACAO_API_X, etc.)

**Exemplos:** `CLIENTEA_TECH_DECISOES.md`, `MINHA_EMPRESA_PRODUTO_ROADMAP.md`.

---

### PASSO 5.7 — Scan da memoria do Claude Code (condicional)

Este passo so se aplica a quem usa **Claude Code** como agente. Se o usuario usa Cursor, CoWork ou outra ferramenta, pular.

1. Verificar se existe a pasta `~/.claude/projects/{working-dir-encoded}/memory/` — esta e a memoria do Claude Code para o diretorio atual.
2. Se nao existir: pular silenciosamente, sem mencionar.
3. Se existir, contar as linhas do `MEMORY.md` e o numero de arquivos de topico na pasta.
4. **Alertar so se exceder os limites:**

| Metrica | Alerta se |
|---------|-----------|
| `MEMORY.md` linhas | mais de 100 |
| Arquivos de topico | mais de 15 |
| Algum topico sem modificacao ha mais de 90 dias | 1 ou mais |

5. **Apenas OBSERVAR — NAO sugerir o Otimizar Custo aqui.** Se a memoria estiver acima do limiar com item
   redutivel, no maximo registrar uma nota passiva de 1 linha (`"memoria do agente acima do limiar nominal"`).
   **O lembrete de rodar o Otimizar Custo passou a ser responsabilidade do Otimizar OS (teto de 1x por mes),
   justamente para nao pulverizar lembrete de custo em toda sessao de fim-do-dia.** A memoria do agente e
   GLOBAL (uma so para o OS todo); pedir para limpa-la em todo fim-do-dia de todo contexto vira ruido.

> **REGRA — nao reclamar a toa:** nunca sugerir rodar uma skill que nao tem o que reduzir, e nunca repetir o
> mesmo alerta toda sessao. Alerta recorrente sem acao possivel e ruido (e o "auto-criticar" que incomoda).

**Nao executar nem sugerir limpeza de memoria aqui** — quem lembra do `Otimizar Custo` (no maximo 1x/mes) e o `Otimizar OS`.

---

### PASSO 6 — Atualizar index.md (raiz + contexto ativo)

**Index do contexto ativo:**
Se o arquivo `index.md` existir na pasta do contexto que esta sendo fechado:
1. Listar todos os arquivos `.md` nessa pasta
2. Comparar com o `index.md` atual
3. Para arquivos novos (satelites criados durante o dia): adicionar entrada com link
4. Para arquivos removidos ou renomeados: atualizar
5. Atualizar a data no cabecalho

Se o `index.md` NAO existir no contexto:
- Sugerir ao usuario: `"Este contexto nao tem um index.md (catalogo de arquivos). Quer que eu crie?"`
- Se sim: listar todos os arquivos da pasta com links

**Index da raiz:**
Se houve mudanca em qualquer arquivo da raiz do OS (novo arquivo, rename), atualizar tambem o `index.md` da raiz.

> Cada contexto tem seu proprio index.md. A raiz tem o index geral que aponta para os contextos.

---

### PASSO 7 — Resumo final

Apresentar ao usuario um resumo do que foi feito:

```
Revisao Diaria concluida ✓

Contexto fechado: [path do contexto — ex: Consultoria/ClienteA]
Aprendizados salvos: [X novas entradas em aprendizados_do_dia.md]
Tarefas migradas: [X itens movidos para changelog]
Pendencias atualizadas: [X novas + X antigas mantidas]
Saude dos arquivos: [tudo ok / X arquivos precisam de atencao]
Index.md: [atualizado / criado / nao existia]
```

Se houve uma analise longa, comparacao detalhada ou deep dive durante a sessao, oferecer:
> `"Essa analise vale ser salva como arquivo separado? Posso gravar como CONTEXTO_analise_titulo.md"`

---

## Formato de saida

**aprendizados_do_dia.md** — novas entradas adicionadas no topo, antes das entradas anteriores:
```markdown
## [Titulo] (DD/MM)
**Insight:** ...
**Solucao:** ...
**Nao fazer:** ...
```

**changelog.md** — entrada adicionada no topo (mais recente primeiro):
```markdown
### DD/MM/AAAA — [Titulo da sessao]
- [O que foi feito]
- [Decisao tomada]
- Itens concluidos: [lista]
```

**`*MESTRE.md`** — atualizacao pontual:
- Cabecalho com nova data de "Ultima atualizacao"
- Itens `[x]` substituidos por referencias ao changelog
- Novas pendencias `[ ]` adicionadas

---

## Regras de seguranca

- **Nunca apagar conteudo** — apenas mover para o changelog com referencia
- **Nunca migrar itens concluidos sem confirmacao** do usuario
- **Nunca inventar aprendizados** — registrar apenas o que o usuario informou
- **Nunca acessar arquivos de outro contexto** sem permissao explicita
- **Nunca declarar concluido** sem ter atualizado pelo menos o aprendizados_do_dia.md e o *MESTRE.md
- **Se o usuario nao responder uma das 3 perguntas**, prosseguir com o que foi respondido e deixar a secao em branco com nota "(nao registrado nesta sessao)"
- **Nunca assumir que o OS e flat** — sempre verificar a estrutura real antes de agir
- **🔒 NUNCA mexer no `soul.md` nem promover regras para ele.** O soul trata SO de carater, comportamento e perfil do agente — deve ser leve e objetivo. Regrinhas operacionais (taxas, fluxos, "sempre fazer X no produto") NAO sao comportamento: vao para claude.md / mestre / satelite. Se algo parecer de soul, perguntar ao usuario antes — nunca escrever no soul por conta propria.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
