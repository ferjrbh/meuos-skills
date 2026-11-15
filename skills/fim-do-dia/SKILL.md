---
name: fim-do-dia
description: |
  Rotina de encerramento do dia de trabalho. Executa quando o usuario diz
  "revisao diaria", "fechar o dia", "encerrar", "fim do dia", "vamos fechar",
  "pode fechar", "encerra ai", "wrap-up", "encerrar sessao".
  O agente SINTETIZA a sessao e o usuario so confirma (uma tabela numerada; no maximo 2 aprovacoes).
  AVALIA os arquivos antes de escrever (gate anti-duplicacao e anti-verborragia), salva
  aprendizados no lugar certo, migra tarefas concluidas e atualiza pendencias no documento
  mestre do contexto ativo.
version: 5.5
context: meuos
user-invocable: true
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Fim do Dia — Encerramento da Sessao

## O que esta skill faz

Esta skill fecha a sessao de trabalho em poucos minutos. O agente resume o que aconteceu (o que fizemos, o que aprendemos, o que fica pendente), voce confirma numa tabela, e cada coisa vai para o arquivo certo: aprendizados, changelog e documento mestre. Ao final, avisa se algum arquivo esta ficando pesado.

---

## 🖥️ COMO FALAR COM O USUARIO (padrao visual, vale para a execucao inteira)

1. **Cabecalho de 1 linha** em cada mensagem: `**Fim do dia · [contexto] · registro**`, depois (so se houver) `**Fim do dia · [contexto] · manutencao**` e, por ultimo, `**Fim do dia · [contexto] · fecho**`. Sem numero de etapa: so se sabe se havera manutencao depois dos passos 2 a 6.
2. **Uma frase de resumo em negrito ANTES de qualquer tabela** (ex.: "Sessao com 2 entregas, 1 aprendizado e 1 pendencia nova.").
3. **Uma tabela numerada so** para aprovar, com as colunas `# | O que vou registrar | Onde fica`. "Onde fica" usa o nome que o usuario conhece (Documento mestre, Aprendizados, Changelog, Satelite, Index), nunca caminho de arquivo.
4. **Aprovacao:** se o agente tiver caixa de opcoes clicaveis (no Claude Code, a ferramenta de pergunta ao usuario), abrir com 3 opcoes: "Aprovar tudo", "Escolher itens", "Nao mexer em nada". Em "Escolher itens", ou onde nao houver a caixa, o usuario responde "tudo" ou os numeros (ex.: 1, 2 e 4).
5. **No maximo 2 aprovacoes por execucao:** (1) o que registrar (PASSO 1); (2) so se houver, a manutencao (migracoes por limite, instrucao morta, extracao para satelite, index fora do formato ou ausente), tudo junto numa segunda tabela, mostrada UMA vez, no PASSO 6.5. Os passos 2 a 6 so JUNTAM candidatos; nenhum deles abre pergunta propria.
6. **Tamanho em leve, atencao e pesado** (🟢 🟡 🔴), com barra de 10 blocos so no que estiver 🟡 ou 🔴: `🟡 ▰▰▰▰▰▰▰▰▱▱ 13 KB de 15`. A barra mede o tamanho contra o limite de "pesado" do guia (os numeros dos exemplos desta skill sao ilustrativos; o limite vem sempre do guia). Tokens so como previsao. Nunca valor em dinheiro.
7. **So os termos do treinamento:** documento mestre, satelite, aprendizados, changelog, index, ponteiro, contexto. Nao usar com o usuario: frontmatter, drift, gate, custo fixo, read-on-demand.
8. **Fecho fixo** (PASSO 7): cartao de 4 linhas: Feito, Nao feito, Saude, Sugestao.

## 📏 ONDE ESTAO OS LIMITES DE TAMANHO

Os limites (linhas e KB de cada arquivo, alvo ao enxugar, tamanho da entrada de aprendizado) moram em UM lugar: a secao **"Limites de tamanho"** do `guia_do_os.md` da raiz do OS. Ler a tabela de la ao iniciar. Se o guia nao tiver essa secao (guia anterior a versao 4): avisar em 1 linha que o guia esta desatualizado, sugerir a skill `otimizar-os` (ela atualiza o guia) e, nesta execucao, ler a tabela direto do catalogo (so leitura): `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/meuos-do-zero/templates/guia_do_os.md`. Sem guia atualizado e sem internet: pular o PASSO 5 e dizer isso no fecho.

---

## 📜 CONTRATO POR ARQUIVO (decide ONDE cada informacao entra)

| Arquivo | O que entra | O que NUNCA entra |
|---|---|---|
| `claude.md` (contexto) | SO regra **RIGIDA de operacao** do contexto (config, limites inviolaveis). Mexer aqui = **excecao da excecao** | Caso do dia, status, decisao de negocio, historico |
| `aprendizados_do_dia.md` | **Caixa de entrada** de regra/padrao/anti-pattern reutilizavel que AINDA NAO tem satelite do tema — objetivo, pouco texto (tamanho maximo da entrada: tabela "Limites de tamanho" do guia). Tema que ja tem satelite: a regra (1 linha) entra direto em "Regras vigentes" dele e a entrada completa, sem reescrever, em "Historico" com a data (aplicando o modelo no satelite, se ainda nao tiver). **Excecao: satelite ja 🔴 pesado nao recebe nada; a regra fica aqui nos aprendizados desta vez** | Narrativa, historia da investigacao, evento pontual, regra de tema que ja tem satelite |
| `changelog.md` | **O LAR do caso pontual**: o que foi feito, incidentes, narrativas com data (append-only) | Regra viva (essa mora nos arquivos acima) |
| `*MESTRE.md` | O documento **VIVO** — mexe quase toda sessao: descricao do contexto, objetivos, **decisoes estrategicas/taticas, planos**, status, pendencias, ponteiros pros satelites | Spec densa (→ satelite), medicao/inventario (→ satelite), historico (→ changelog), caso do dia |
| **SATELITE** (`CONTEXTO_tema.md`, modelo `satelite.md`) | Detalhe DURAVEL de UM tema: spec, inventario, medicao com data, evidencia, historico analitico. Criado sob demanda (nunca vazio "pra constar"), pelo modelo: frontmatter com `abrir_quando` · `> Documento pai` · Regras vigentes no topo · Detalhe · Historico no fim. Lido quando o "abrir quando" bate | Status atual e "com quem esta a bola" (isso e do MESTRE; o satelite nunca reconta status) |
| `index.md` | Catalogo **100% completo** dos .md do contexto — todo satelite listado, sem excecao. Entrada no formato unico: `- [arquivo](arquivo) — abrir quando: tema A, tema B` (1 linha; o trecho depois de "abrir quando:" tem ate 80 caracteres) | Conteudo; descricao longa (o que o arquivo E cabe no nome; a entrada diz QUANDO abrir) |
| `soul.md` (raiz) | SO personalidade/comportamento do agente, de altissima necessidade | Regra operacional; qualquer coisa que caiba em outro lugar |

**Os 2 gatilhos de roteamento (valem em TODA escrita, mesmo com o MESTRE pequeno):**
- Antes de gravar **estado mutavel** (status, fase, proximo passo, pendencia, "onde paramos") fora do
  MESTRE → PARAR: estado vai pro MESTRE.
- Antes de gravar **medicao/inventario** (contagem, tamanho, percentual, "medido em", lista densa)
  dentro do MESTRE → PARAR: vai pro satelite do tema, com data; o MESTRE recebe so um ponteiro de
  1 linha, sem repetir o numero. A casa se decide na ESCRITA, pela natureza do fato, nunca na faxina
  pelo tamanho do arquivo.

**⚡ Escrever e excecao, nao obrigacao.** A rotina AVALIA todos os arquivos, mas so ESCREVE onde
ha item que sobreviveu ao gate (PASSO 1.5). Sessao sem material pra um arquivo = arquivo INTOCADO.
Nunca escrever "pra constar" — escrita desnecessaria e o que incha os arquivos.

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

**Principio:** o agente faz o trabalho de sintese, o usuario apenas valida ou ajusta. Nunca fazer pergunta aberta ("o que voce fez hoje?"): apresentar a sintese pronta e pedir confirmacao.

**Fluxo:**

1. **Sintetizar a sessao** lendo o historico da conversa atual + o `aprendizados_do_dia.md` recente do contexto + os itens concluidos do documento mestre (PASSO 3: `[x]` ou a marca de concluido que o contexto usa, como ✅). Sao 3 blocos (o que fizemos, o que aprendemos, o que fica pendente), e qualquer um pode estar vazio. Passar cada item pelo GATE (PASSO 1.5) ANTES de montar a tabela, para ela ja mostrar o destino certo.

2. **Apresentar ao usuario** no padrao visual, numa tabela so:

```
**Fim do dia · [contexto] · registro**

**Sessao com 2 entregas, 1 aprendizado e 1 pendencia nova.**

| # | O que vou registrar | Onde fica |
|---|---|---|
| 1 | Proposta do cliente revisada | Changelog |
| 2 | Planilha de custos atualizada | Changelog |
| 3 | Aprendizado: confirmar o prazo antes de enviar proposta | Aprendizados |
| 4 | Pendencia: enviar a proposta revisada | Documento mestre |
| 5 | 3 tarefas concluidas saem do documento mestre e vao para o changelog | Changelog |
```

   Em seguida, a aprovacao (caixa de opcoes: "Aprovar tudo", "Escolher itens", "Nao mexer em nada"; sem caixa: `Responda "tudo", os numeros que valem ou o que ajustar.`). Sessao sem nada a registrar: dizer isso em 1 frase e ir direto ao PASSO 5.

3. **Aguardar resposta** — o usuario pode:
   - "Confirmado, pode salvar"
   - "Tira o item 2 dos aprendizados, o resto OK"
   - "Adiciona X em pendencias"
   - "Nao teve aprendizado novo hoje, segue so com o que fizemos"
   - "Sessao foi de leitura/discussao, nao tem nada pra registrar — pula"

4. **Aplicar a decisao** (⚠️ TODO item confirmado ja passou pelo GATE DE ESCRITA — PASSO 1.5; item que o usuario acrescentou na resposta passa agora):
   - Se houver "o que fizemos" confirmado → vai pro changelog (PASSO 3)
   - Se houver "o que aprendemos" confirmado → vai pro `aprendizados_do_dia.md` SE sobreviver ao gate; caso pontual vira changelog
   - Se houver "o que fica pra amanha" confirmado → atualiza pendencias no `*MESTRE.md` (PASSO 4)
   - Se o usuario disse "pula" ou "nao tem nada" → nao gravar nada e seguir para PASSO 5 (saude dos arquivos)

**REGRA CRITICA — nao forcar conteudo:**
- Sessao pode ter sido **so de leitura/analise** sem entregas → "O QUE FIZEMOS" pode listar so a discussao sem ir pro changelog
- Sessao pode ter zero aprendizados novos → "O QUE APRENDEMOS" fica vazio e nada vai pro aprendizados
- Sessao pode nao gerar pendencias novas → "O QUE FICA PRA AMANHA" so lista pendencias antigas
- **NUNCA inventar** aprendizados ou pendencias para "preencher" os 3 blocos. Se esta vazio, esta vazio. Forcar registro polui os arquivos.

---

### PASSO 1.5 — GATE DE ESCRITA — avaliar ANTES de gravar (OBRIGATORIO)

Nenhum item confirmado vai direto pros arquivos. Cada item passa por este gate ANTES de qualquer
edicao em `claude.md`, `aprendizados_do_dia.md` ou `*MESTRE.md`. Motivo: os arquivos crescem por
escrita redundante e verbosa na ENTRADA — a limpeza depois nao compensa.

**1 — Ler o alvo INTEIRO.** Antes de escrever num arquivo, ler o arquivo completo (nao so o comeco).
Sem saber o que ja existe, toda escrita e duplicata em potencial.

**2 — Anti-duplicacao (busca obrigatoria).** Extrair 2-3 palavras-chave do item e buscar em
claude.md + `*MESTRE.md` + aprendizados + satelites do contexto.
- Tema JA coberto → **EDITAR a entrada/regra existente** (incorporar o novo, atualizar a data). NUNCA criar segunda entrada do mesmo tema.
- E **reincidencia** de regra ja escrita (o problema aconteceu de novo)? → NAO e aprendizado novo: 1 linha no changelog + no maximo 1 frase de reforco na regra existente.

**3 — Teste de relevancia (filtro caso-pontual).** Perguntar: *"daqui a 3 meses, isso muda como
eu trabalho neste contexto?"*
- **NAO** (incidente resolvido, bug corrigido, evento datado, historia da investigacao) → **changelog** (1-2 bullets). Nada no aprendizados.
- **SIM** → extrair SO a regra generalizavel; a narrativa do caso vai pro changelog, nunca dentro da entrada.

**4 — Orcamento de escrita (anti-verborragia).**
- Entrada nova: dentro do **tamanho maximo de entrada da tabela do guia**. Insight = a regra. Solucao = o procedimento. Nao fazer = 1 frase.
- Proibido na entrada: historia da investigacao, "caso real: ...", justificativa da regra.
- **Max 3 entradas novas por sessao** — o excedente e quase sempre caso pontual → changelog.

**5 — Teto duro (entra um, sai um; a saida mira a folga).** Arquivo-alvo JA 🔴 pesado pela tabela
"Limites de tamanho" do guia → escrita nova SO entra se sair volume equivalente na MESMA rodada
(condensar/migrar antes, com aprovacao). Ao migrar, levar o arquivo para o "alvo ao enxugar" da
tabela, nao para 1 byte abaixo do corte: tirar so o equivalente ao que entra deixa o arquivo
grudado no teto e o alerta volta na sessao seguinte. Destino: satelite do tema (protocolo de mudanca
de casa do PASSO 5.5, passo 4).

**6 — claude.md e excecao da excecao; MESTRE e o destino vivo.** O claude.md do contexto so recebe
escrita se for regra RIGIDA de operacao — quase nunca acontece. Decisao de negocio/estrategia/
tatica/plano → **MESTRE** (documento vivo, mexe quase toda sessao).

**7 — Fato conferivel leva fonte e data.** Numero, data, preco, prazo, nome ou status que vai ser
gravado: registrar de onde veio e quando foi conferido (ex.: `fonte: planilha de clientes, conferido
em DD/MM/AAAA`). O usuario disse na conversa → `fonte: informado pelo dono em DD/MM/AAAA`. Sem fonte
→ gravar com a marca `nao verificado`. Nunca completar numero de cabeca.

---

### PASSO 2 — Salvar aprendizados

Com os aprendizados confirmados no PASSO 1 (e que sobreviveram ao gate), escrever no arquivo `aprendizados_do_dia.md` do contexto ativo. Nenhum aprendizado confirmado → pular este passo; o arquivo fica intocado.

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

**Higiene (os numeros vem da tabela "Limites de tamanho" do guia; medir linhas E KB, vale o pior):**
arquivo 🔴 pesado, mais entradas que o maximo do guia ou entrada acima do tamanho maximo → propor a manutencao:
entrada longa → CONDENSAR (tirar a narrativa; o trecho cortado vai em 1-2 linhas para o changelog, se ainda nao
estiver la) · evento pontual → `changelog.md` · regra de UM tema → satelite do tema, so se ele existe e esta
leve · entradas antigas do mesmo tema → agrupar numa so. Itens concluidos no documento mestre → sempre migram
(PASSO 3). A higiene roda mesmo quando nenhum aprendizado novo foi gravado.

Os candidatos NAO sao mostrados agora: entram na lista de manutencao, apresentada UMA vez no PASSO 6.5
(a unica outra aprovacao da execucao). **NUNCA migrar sem aprovacao.**
Promover entrada para satelite = a regra (1 linha, o "Solucao"/"Nao fazer") entra em "Regras vigentes"; a entrada
completa, sem reescrever, entra em "Historico" com a data; conferir que os dois estao la e so entao remover do aprendizados.

---

### PASSO 3 — Migrar tarefas concluidas

Ler o documento mestre do contexto ativo. Ele pode se chamar `documento_mestre.md` (padrao do MeuOS) ou qualquer nome terminando em "mestre.md" (ex.: `CLIENTEA_DOCUMENTO_MESTRE.md`). **Buscar SEM diferenciar maiusculas de minusculas** (em Mac e Linux, `*MESTRE.md` nao encontra `documento_mestre.md`). Nesta skill, `*MESTRE.md` significa esse arquivo, com qualquer caixa.

Identificar todos os itens marcados como concluidos (formato `[x]`).

**Para cada item concluido:**
1. Adicionar no `changelog.md` com a data de hoje:

```markdown
### [DATA] — [Titulo curto]

- [Item concluido 1]
- [Item concluido 2]
- [Decisao tomada, se houver]
```

2. No `*MESTRE.md`, **REMOVER a linha do item `[x]`**: o changelog acabou de receber a entrada
   com a data, ele JA e o registro. **NAO deixar linha riscada** (`~~[x] tarefa~~`): linha riscada
   e custo fixo que o mestre paga em toda sessao so pra dizer "isto ja foi feito". Garantir que o
   bloco de pendencias tenha (criada UMA unica vez, na primeira execucao) a nota estatica:

```markdown
> **Tarefas concluidas nao ficam listadas aqui.** Historico completo, com data, no `changelog.md`.
```

3. **EXCECAO (conclusao que REVERTE uma regra/decisao vigente)**: ex, o mestre dizia "NAO fazer X"
   e a tarefa concluida liberou X): so remover a linha deixaria o mestre afirmando a regra velha,
   e o agente seguinte obedeceria a instrucao morta. Neste caso:
   - Atualizar a regra **no ponto do mestre onde ela vive**, em linguagem afirmativa (o que vale HOJE)
   - Registrar a transicao (regra antiga → nova, com data e motivo) no `changelog.md`
   - O mestre expressa o estado ATUAL; a historia da mudanca mora no changelog. Nunca manter linha
     riscada como "correcao historica" dentro do mestre.

**IMPORTANTE:** Nunca remover conteudo do documento mestre sem aprovacao. Os itens concluidos ja aparecem como UMA linha da tabela do PASSO 1 ("N tarefas concluidas saem do documento mestre e vao para o changelog"); se o usuario pedir, listar quais sao. Nao abrir pergunta separada para isso.

---

### PASSO 3.5 — Instrucao morta (checagem rapida, so no que a sessao mexeu)

Uma tarefa concluida ou uma decisao nova pode deixar para tras uma frase que ja nao vale (ex.: o
documento mestre ainda diz "aguardando aprovacao do cliente" e o cliente aprovou hoje). Agente que
ler isso amanha obedece a instrucao morta.

1. Para cada item confirmado no PASSO 1, extrair 1-2 palavras-chave e buscar SO nos arquivos que
   carregam em toda sessao do contexto: documento mestre, `claude.md` do contexto e
   `aprendizados_do_dia.md`, mais o satelite de pendencias e os satelites em que voce escreveu hoje. Nao varrer os
   demais satelites nem outros contextos (isso e do `otimizar-os`). Corrigir uma frase desatualizada num satelite
   pesado e permitido: nao aumenta o arquivo.
2. Achou frase que o item de hoje contradiz → guardar como candidato da tabela de manutencao (PASSO 6.5):
   `| N | Atualizar "aguardando aprovacao do cliente" para "aprovado em DD/MM" | Documento mestre |`.
3. **Sempre conferir antes de propor:** ler o trecho inteiro em volta; na duvida se ainda vale,
   a linha entra na tabela de manutencao com a marca `(decisao sua)` e so muda se o usuario responder. Nada muda sem aprovacao. A transicao (antes → depois) vai no changelog.
4. Nao achou nada → seguir em silencio.

---

### PASSO 4 — Atualizar pendencias

Com as pendencias confirmadas no PASSO 1, atualizar a lista de pendencias no documento mestre do contexto ativo:

- Adicionar novas pendencias informadas pelo usuario (formato `[ ] [descricao]`) — **ANTES, buscar
  nas pendencias existentes E no `CONTEXTO_backlog.md`, se existir**: se o tema ja esta la, atualizar a linha existente
  (pendencia que volta a andar SAI do backlog e volta ao MESTRE), nunca duplicar
- Pendencia nova = 1-2 linhas (o que + o que destrava) — spec e historico nao moram aqui
- **Gatilho do satelite**: se a atualizacao carrega medicao, inventario ou spec (numeros/listas densas),
  isso NAO entra no mestre: vai pro satelite do tema (com data), e o mestre recebe so o ponteiro de
  1 linha. Vale mesmo com o mestre pequeno (ver os 2 gatilhos no CONTRATO POR ARQUIVO).
- Manter as pendencias antigas que continuam abertas
- Atualizar a data de "Ultima atualizacao" no cabecalho do documento mestre (se ele tiver frontmatter, a data e o campo `updated`; nao criar a linha de texto)

---

### PASSO 5 — Verificar saude dos arquivos

Medir linhas E KB do documento mestre, do `aprendizados_do_dia.md` e do `changelog.md` do contexto
ativo (so o ativo) e classificar em 🟢 leve, 🟡 atencao ou 🔴 pesado pela tabela "Limites de tamanho"
do guia. **Vale o PIOR entre linhas e KB**: um documento mestre de 199 "linhas" que sao paragrafos
inteiros pode pesar 60 KB e passar batido no check de linhas.

O resultado NAO vira tabela propria: entra na linha "Saude" do fecho (PASSO 7). Tudo 🟢 → 1 linha.
So detalhar com barra quando houver 🟡 ou 🔴:

```
Saude  🟢 aprendizados · 🟢 changelog · 🟡 documento mestre ▰▰▰▰▰▰▰▱▱▱ 27 KB de 40
```

**Sugerir o Otimizar OS no MAXIMO 1x por semana, e so se houver volume.** Antes de sugerir, ler (arquivo ausente = o Otimizar OS nunca rodou neste contexto: o teto de cadencia esta cumprido, vale so a porta de volume)
`{contexto}/historico/.last-otimizar-os` (guarda `ULTIMA_EXECUCAO`, `LAST_SUGGESTED`, `CONTAGENS`, `FRESCOR`).
So sugerir se as DUAS condicoes forem verdade:

1. **Porta de volume** (ha motivo real — senao, silencio, mesmo passada a semana):
   - arquivo 🔴 REDUTIVEL (temporal velho / cemiterio de tarefas / secao densa extraivel); OU
   - `aprendizados_do_dia.md` grande por excesso de regra perene (extraivel para satelite); OU
   - **drift de numeros**: reconferir 2-4 contagens vivas (tabelas/rotas/etc. na fonte-da-verdade do contexto) vs `CONTAGENS` salvas — se mudou, ha volume; OU
   - carimbo `Verificado ao vivo` com mais de 45 dias; OU o `changelog.md` cresceu 5+ entradas desde a ultima execucao.
2. **Teto de cadencia**: `hoje - max(ULTIMA_EXECUCAO, LAST_SUGGESTED)` for de **7 dias ou mais**.

Ao sugerir, gravar `LAST_SUGGESTED=<hoje>` no `.last-otimizar-os` (segura o lembrete na semana, mesmo se voce recusar).
- Texto da linha "Sugestao" do fecho (nao e pergunta; o usuario roda se quiser): `rodar o Otimizar OS neste contexto: [informacao desatualizada / arquivo pesado] (ultima vez: [data])`
- Se for o `aprendizados_do_dia.md` inchado de regra perene: `rodar o Otimizar OS: os aprendizados viraram deposito de regras; ele leva cada uma para o satelite do tema`
- Conteudo perene ja curado (piso) e sem drift → **NAO sugerir nada**. Repetir alerta sem acao possivel e ruido.

---

### PASSO 5.5 — Descompressao do documento mestre (condicional)

**Executar SOMENTE se o documento mestre do contexto ativo estiver 🟡 ou 🔴 (pela tabela do guia) OU tiver uma secao com 30+ linhas sobre UM tema**. Documento mestre 🟢 leve e sem secao longa: pular, mesmo que a sessao tenha tido entrega grande.

**Objetivo:** manter o documento mestre legivel em menos de 5 minutos. Escopo, status, pendencias e ponteiros ficam la. Detalhes densos saem para arquivos separados.

**Fluxo (as propostas viram candidatos da tabela de manutencao do PASSO 6.5; nenhuma pergunta aqui):**

1. **Medir linhas E KB do documento mestre.** 🟢 leve e sem secao de 30+ linhas de um tema: pular.
2. **Identificar secoes densas** — qualquer secao com mais de 30 linhas de conteudo detalhado sobre UM tema especifico (decisoes por data, especificacoes de modulo, mapeamentos, etc.).
3. **Propor extracao ao usuario** listando as secoes candidatas. Para cada uma, procurar no `index.md` um satelite do mesmo tema: existe → propor ACRESCENTAR nele (satelite existente mantem o nome; ao acrescentar, aplicar o modelo NELE — frontmatter com `abrir_quando` + secao "Regras vigentes" no topo — sem reorganizar o que ja estava dentro); nao existe → propor satelite novo pelo modelo `satelite.md` (frontmatter `updated/context/type: satelite/status: vivo/abrir_quando` · `> Documento pai:` · `## Regras vigentes` · `## Detalhe` · `## Historico`), nome `CONTEXTO_tema.md` (mesmo que os satelites vizinhos usem outro padrao de nome), com o "abrir quando" preenchido.
4. **Se aprovado:** seguir o protocolo de mudanca de casa: copiar SEM reescrever (resumir e outro passo, com aprovacao propria) → conferir item a item que toda regra, numero, data, nome e link da origem esta no destino, e mostrar a lista → so entao remover do mestre → 1 linha no changelog ("movido X de A para B"). Dentro do satelite, a secao extraida vai para "Detalhe" (spec, inventario, processo) ou "Historico" (bloco datado); em "Regras vigentes" entra so regra de 1 linha.
5. **Substituir no mestre** por UMA linha no formato unico: `- [CONTEXTO_tema.md](CONTEXTO_tema.md) — abrir quando: tema A, tema B` (o trecho depois de "abrir quando:" tem ate 80 caracteres). A linha entra SEMPRE no `index.md`. No mestre ela vive em UM lugar, a secao "Satelites deste contexto" (criar a secao no primeiro ponteiro, se o mestre nao tiver), e so entra se a secao tiver menos de 15 linhas (regra do guia: o documento mestre lista os satelites do dia a dia; a lista completa e o index). No lugar da secao extraida nao fica nada.
6. **Limite:** maximo 3 arquivos separados novos por execucao (evita fragmentacao).

**Convencao de nomes:** `CONTEXTO_tema.md` — prefixo do contexto em maiusculas, tema em minusculas com `_`. Uma convencao so, a mesma do modelo `satelite.md` e do `otimizar-os`. Satelite antigo com outro nome NAO e renomeado (renomear quebra link em silencio).

**Exemplos:** `CLIENTEA_asaas.md`, `MINHA_EMPRESA_roadmap_produto.md`.

---

### PASSO 5.7 — Scan da memoria do Claude Code (condicional)

Este passo so se aplica a quem usa **Claude Code** como agente. Se o usuario usa ChatGPT/Codex, Cursor, CoWork ou outra ferramenta, pular (nesses agentes nao existe a pasta de memoria do Claude Code).

1. Verificar se existe a pasta `~/.claude/projects/{working-dir-encoded}/memory/` — esta e a memoria do Claude Code para o diretorio atual.
2. Se nao existir: pular silenciosamente, sem mencionar.
3. Se existir, contar as linhas do `MEMORY.md` e o numero de arquivos de topico na pasta.
4. **Alertar so se exceder os limites:**

| Metrica | Alerta se |
|---------|-----------|
| `MEMORY.md` | 🟡 ou 🔴 pela tabela do guia |
| Arquivos de topico | 🟡 ou 🔴 pela tabela do guia |
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

**Meta: 100% dos .md do contexto listados — sem excecao.** Satelite fora do index = documento
invisivel que vira duplicata no futuro. A correcao e imediata (index e catalogo, nao conteudo).

**Index do contexto ativo:**
Se o arquivo `index.md` existir na pasta do contexto que esta sendo fechado:
1. Listar todos os arquivos `.md` nessa pasta
2. Comparar com o `index.md` atual (e com os sub-indices que ele listar) — **cross-check: TODO satelite da pasta tem entrada no index ou num sub-indice?** Faltando → adicionar na hora, mesmo com o index pesado (e catalogo: o teto de arquivo pesado nao vale para ele), e dizer no fecho quantos entraram
3. Para arquivos novos (satelites criados durante o dia): adicionar entrada no formato unico: `- [arquivo](arquivo) — abrir quando: tema A, tema B` (1 linha; o trecho depois de "abrir quando:" tem ate 80 caracteres)
3b. Entrada existente fora do formato unico (sem "abrir quando" ou com o trecho acima de 80 caracteres): o fim-do-dia so corrige as entradas dos arquivos criados ou alterados HOJE (candidatos da tabela de manutencao, PASSO 6.5). **Nunca reescrever o index em massa aqui**: mais de 5 entradas antigas fora do formato → nao mexer e por na linha "Sugestao" do fecho "rodar o Otimizar OS (ele arruma o index inteiro numa passada)".
4. Para arquivos removidos ou renomeados: atualizar
5. Atualizar a data no cabecalho

Se o `index.md` NAO existir no contexto:
- Candidato da tabela de manutencao (PASSO 6.5): `| N | Criar o index deste contexto, com todos os arquivos listados | Index |`
- Aprovado: listar todos os arquivos da pasta com links, no formato unico

**Index da raiz:**
Se houve mudanca em qualquer arquivo da raiz do OS (novo arquivo, rename), atualizar tambem o `index.md` da raiz.

> Cada contexto tem seu proprio index.md. A raiz tem o index geral que aponta para os contextos.

---

### PASSO 6.5 — Tabela de manutencao (so se houver candidatos; UMA vez)

Juntar os candidatos reunidos nos passos 2 (aprendizados pesados), 3.5 (instrucao morta), 5.5 (secao densa
do documento mestre) e 6 (index fora do formato ou ausente). Nenhum candidato → pular este passo.
Havendo, mostrar UMA tabela, no mesmo formato da primeira:

```
**Fim do dia · [contexto] · manutencao**

**Seus aprendizados estao pesados e ha 1 frase desatualizada no documento mestre.**

| # | O que vou registrar | Onde fica |
|---|---|---|
| 1 | Mover "Erro de cadastro duplicado" (evento ja resolvido) | Changelog |
| 2 | Mover a regra "API de pagamento so leitura" | Satelite de pagamentos |
| 3 | Atualizar "aguardando aprovacao do cliente" para "aprovado em DD/MM" | Documento mestre |
| 4 | Encurtar 2 entradas do index para o formato padrao | Index |
```

Mesma aprovacao da primeira tabela (caixa de opcoes ou numeros). O que fica como esta nao entra na
tabela. So o aprovado e executado, seguindo o protocolo de cada passo (mudanca de casa: copiar, conferir
item a item, so entao remover). Recusado ou sem resposta → nada muda e isso vai em "Nao feito" no fecho.

---

### PASSO 7 — Resumo final

Fechar com o cartao fixo de 4 linhas (sem caminho de arquivo, sem termo tecnico):

```
**Fim do dia · [contexto] · fecho**

**Feito**      2 entregas, 1 aprendizado e 1 pendencia registrados · index atualizado
**Nao feito**  nada ficou de fora  (ou: o que o usuario recusou / o que nao foi possivel)
**Saude**      🟢 aprendizados · 🟢 changelog · 🟡 documento mestre (ficando pesado)
**Sugestao**   rodar o Otimizar OS neste contexto esta semana  (ou: nenhuma)
```

No maximo UMA sugestao, e so se as regras do PASSO 5 permitirem.

Se houve uma analise longa na sessao que ainda NAO esta salva em arquivo, usar a linha "Sugestao" para isso
(`salvar a analise de hoje como arquivo do contexto`), sem abrir pergunta.

---

## Formato de saida

**aprendizados_do_dia.md** — novas entradas adicionadas no topo da sua categoria (Regras de Negocio, Estrategicos ou Tecnicos), antes das anteriores:
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
- Itens `[x]` migrados pro changelog e REMOVIDOS da lista (sem linha riscada; a nota estatica
  "Tarefas concluidas nao ficam listadas aqui" cobre o historico)
- Conclusao que reverteu regra: regra atualizada no proprio mestre em linguagem afirmativa
- Novas pendencias `[ ]` adicionadas

---

## Regras de seguranca

- **Nunca apagar conteudo que nao foi preservado**: item concluido so sai do mestre DEPOIS de
  registrado no changelog, e com aprovacao. Remover sem registrar antes e perda de historico
- **Nunca migrar itens concluidos sem confirmacao** do usuario
- **Nunca inventar aprendizados** — registrar apenas o que saiu da sessao e o usuario confirmou na tabela
- **Nunca acessar arquivos de outro contexto** sem permissao explicita
- **Nunca declarar concluido** sem ter AVALIADO o `aprendizados_do_dia.md` e o documento mestre. Avaliar nao e escrever: sessao sem material deixa o arquivo intocado
- **Se o usuario aprovar so parte da tabela**, gravar so o aprovado e listar o resto em "Nao feito" no fecho
- **Fato conferivel sem fonte** entra marcado `nao verificado`; nunca completar numero, data ou nome de cabeca
- **Nunca assumir que o OS e flat** — sempre verificar a estrutura real antes de agir
- **🔒 NUNCA mexer no `soul.md` nem promover regras para ele.** O soul trata SO de carater, comportamento e perfil do agente — deve ser leve e objetivo. Regrinhas operacionais (taxas, fluxos, "sempre fazer X no produto") NAO sao comportamento: vao para claude.md / mestre / satelite. Se algo parecer de soul, perguntar ao usuario antes — nunca escrever no soul por conta propria.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Todo item confirmado passou pelo GATE DE ESCRITA (PASSO 1.5) antes de ser gravado
- [ ] Itens `[x]` estao no changelog com a data de hoje e SAIRAM do mestre (zero linhas riscadas novas)
- [ ] Conclusao que reverteu regra: mestre atualizado em linguagem afirmativa + transicao no changelog
- [ ] Nenhuma medicao/inventario denso entrou no mestre (foi pro satelite, com ponteiro de 1 linha)
- [ ] Toda mudanca de casa (mestre → satelite) seguiu o protocolo: copiar, conferir item a item com a lista mostrada, so entao remover
- [ ] Satelite novo nasceu pelo modelo (`abrir_quando` + Regras vigentes no topo) e tem a linha unica no index (e no mestre, se a secao de satelites tiver menos de 15 linhas)
- [ ] Pendencias atualizadas sem duplicar tema existente (nem no backlog) + data de "Ultima atualizacao" no cabecalho (ou `updated` do frontmatter)
- [ ] index.md do contexto cobre 100% dos .md (satelites criados hoje incluidos), toda entrada no formato unico ("abrir quando" com ate 80 caracteres)
- [ ] Nada foi migrado ou removido sem aprovacao do usuario
- [ ] No maximo 2 aprovacoes pedidas (o que registrar + manutencao), cada uma em UMA tabela numerada
- [ ] Nenhuma frase que os itens de hoje contradizem ficou no documento mestre, no claude.md do contexto ou nos aprendizados (PASSO 3.5)
- [ ] Numero, data, preco, prazo, nome e status gravados hoje tem fonte e data, ou a marca `nao verificado`
- [ ] Falas ao usuario so com os termos do treinamento, sem caminho de arquivo e sem valor em dinheiro
- [ ] Fecho no cartao fixo de 4 linhas (PASSO 7)

Se algum item falhou: corrigir ANTES de declarar concluido. Nunca reportar "feito" com item pendente.

---

## Casos de borda (regras que valem sobre os passos acima)

1. **Satelite de destino ja 🔴 pesado.** Nunca gravar regra nova nem mover entrada para um satelite pesado. A regra fica no `aprendizados_do_dia.md` desta vez (ele e a caixa de entrada). Medir o satelite ANTES de escrever nele.
2. **O que e uma entrada de aprendizado:** comeca num titulo `## Titulo (DD/MM)` e vai ate o proximo titulo `## `, `# ` ou `---`. Titulo de categoria (`# REGRAS DE NEGOCIO`, indice) nao e entrada. Linha em branco e linha de fonte (`fonte: ...`) nao contam para o tamanho.
3. **Maximo de 3 entradas novas por sessao:** regra gravada direto em satelite tambem conta.
4. **Formato do contexto vence o modelo.** Changelog, pendencias, marca de concluido e nomes dos arquivos que JA existem seguem o formato do contexto (ex.: `## 15-NOV-2026 · titulo`, bolinhas no lugar de `[ ]`). Os modelos desta skill valem para arquivo vazio. Satelite NOVO nasce sempre como `CONTEXTO_tema.md`, com o mesmo prefixo dos vizinhos. O "backlog" e o satelite de pendencias paradas que o index listar, com qualquer nome; se o contexto guarda a mesma pendencia no mestre e no backlog, manter assim.
5. **Nota "Tarefas concluidas nao ficam listadas aqui":** criar so quando houver item concluido a migrar.
6. **Fatos da sessao que ja estao no changelog:** nao repetir; gravar so o que falta e dizer isso na frase de resumo. Se a sessao e o changelog divergem num numero, vale o registro mais recente, com a fonte anotada.
7. **Ao montar a tabela de registro, a mesma linha pede duas coisas** (a pendencia do tema que tambem tem um numero desatualizado): resolver as duas nessa linha.
8. **Conferencia da mudanca de casa:** mostrar em ate 5 linhas, logo antes do fecho.
9. **Linha "Saude" do fecho:** os 3 arquivos do PASSO 5, mais o que estiver 🔴 entre index, satelite tocado hoje e memoria do agente (PASSO 5.7). E o unico lugar dessas notas.
10. **Linha "Sugestao" e o teto semanal:** a sugestao de rodar o Otimizar OS sempre obedece ao teto do PASSO 5. Dentro da semana, o problema aparece em "Saude" e a sugestao fica em branco.
11. **`.last-otimizar-os` ausente:** se o changelog registra uma execucao do Otimizar OS, usar essa data; se nao, tratar como nunca rodou. Ao sugerir, criar o arquivo so com a linha `LAST_SUGGESTED=AAAA-MM-DD`.
12. **Aplicar o modelo num satelite antigo** ao escrever nele (etiqueta do arquivo + "Regras vigentes"): entra na linha da tabela em que a escrita foi aprovada ("...e por o satelite no modelo padrao").
13. **Tamanho:** KB e o tamanho do arquivo em disco.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)

## Regra dual-agent (obrigatória)
Este OS tem DOIS arquivos de entrada equivalentes: `claude.md` (Claude) e `AGENTS.md` (ChatGPT/Codex) — na raiz e em cada contexto. **Se esta skill editar um arquivo de entrada, espelhe a mesma mudança na entrada irmã da mesma pasta** (se ela existir). Nunca deixe as duas divergirem. Cada regra mora em um lugar só (regra 3 do `guia_do_os.md`); regra operacional nunca vai para o `soul.md`.
