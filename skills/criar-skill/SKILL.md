---
name: Criar Skill
description: |
  Cria uma skill nova para o seu agente a partir de uma tarefa que voce ja faz e quer padronizar —
  transforma o SEU jeito de fazer em um procedimento reutilizavel (SKILL.md) que o agente executa
  sozinho nas proximas vezes, sem voce precisar explicar tudo de novo. Conduz a entrevista
  (o que faz, quando dispara, formato da entrega, o que nunca fazer), escreve o rascunho com o
  template oficial, testa com 2-3 pedidos reais e instala na pasta certa do SEU agente
  (Claude Code ou app ChatGPT/Codex). Tambem conserta skill existente que nao esta disparando
  ou que entrega fora do formato. Executa quando o usuario diz "criar skill", "criar uma skill",
  "transformar isso em skill", "virar skill", "ensinar meu agente a fazer X sempre assim",
  "padronizar essa tarefa", "toda vez que eu pedir X, faca Y", "salvar esse processo",
  "melhorar minha skill", "minha skill nao dispara", "skill do zero", "documentar meu jeito de fazer".
version: 1.0
context: meuos
user-invocable: true
argument-hint: "[tarefa ou nome da skill] (sem args = entrevista do zero)"
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Criar Skill — Transforme o seu jeito de fazer em procedimento do agente

## O que esta skill faz

Ela pega uma tarefa que voce ja pediu (e corrigiu) algumas vezes e transforma em uma **skill**:
um arquivo de instrucoes que o seu agente le e segue sozinho toda vez que o assunto aparecer.
Voce ensina uma vez, com calma; o agente repete sempre, do seu jeito.

> **Analogia:** uma skill e o **POP da sua empresa** — o procedimento operacional padrao que voce
> entregaria a um funcionario novo no primeiro dia. Sem POP, cada um faz do seu jeito e voce vive
> corrigindo. Com POP, o novato entrega no padrao da casa desde a primeira vez. A diferenca aqui
> e que o "funcionario" e o seu agente de IA — e ele nunca esquece o procedimento.

---

## Quando criar uma skill (e quando NAO)

**Crie uma skill quando:**
- Voce ja pediu a MESMA tarefa 2-3 vezes e teve que explicar/corrigir de novo a cada vez.
- Existe um "jeito certo" seu: formato, ordem, tom, modelo de documento, checklist.
- Outra pessoa (ou outro agente) vai precisar executar igual, sem voce do lado.

**NAO crie uma skill quando:**
- E tarefa de uma vez so — explique no pedido e pronto.
- O que voce quer e algo rodando SOZINHO em horario marcado (relatorio toda segunda as 8h,
  cobranca automatica). Isso e **automacao** (n8n, crons), nao skill: skill so roda quando
  voce ou o agente puxam o assunto numa conversa.
- Ja existe uma skill da biblioteca que cobre — melhorar a existente vence criar uma concorrente.

---

## Anatomia de uma skill

Uma skill e uma pasta com um unico arquivo obrigatorio:

```
minha-skill/
└── SKILL.md
```

O `SKILL.md` tem duas partes, e cada uma tem um papel diferente:

1. **Frontmatter** (o bloco entre `---` no topo) — os metadados. O campo mais importante e a
   `description`: e por ELA que o agente decide sozinho se ativa a skill ou nao. O agente le
   todas as descricoes das skills instaladas e escolhe pela que combina com o seu pedido.
2. **Corpo** (o resto do arquivo) — o procedimento em si: passos, formato de entrega, exemplos,
   o que nunca fazer.

> Pense assim: a `description` e a **placa da loja** (faz o cliente entrar); o corpo e o
> **manual de atendimento** (o que acontece la dentro). Placa ruim = loja vazia = skill que
> nunca dispara, mesmo com manual perfeito.

---

## Passo 1 — Entrevista (4 perguntas, antes de escrever)

Responda (ou deixe o agente perguntar) estas 4 perguntas. Sem elas, a skill nasce vaga:

1. **O que a skill faz?** Em 1 frase, com o resultado final claro.
   ("Monta a proposta comercial no meu modelo, com precos da tabela vigente.")
2. **Quando ela deve disparar?** Liste 5-10 frases REAIS que voce diria no dia a dia —
   do jeito que voce fala, incluindo abreviacao e informalidade.
   ("faz a proposta pro cliente X", "monta o orcamento", "manda a proposta padrao")
3. **Qual o formato da entrega?** Documento? Tabela? Mensagem pronta? Com quais secoes,
   em qual ordem, salvo onde?
4. **O que ela NUNCA deve fazer?** Os limites: nao enviar sem sua aprovacao, nao inventar
   preco, nao mexer em outro contexto, nao prometer prazo que nao existe.

Se a conversa atual JA CONTEM a tarefa feita (voce acabou de fazer junto com o agente e disse
"vira skill"), o agente extrai as respostas do proprio historico — os passos executados, as
correcoes que voce fez no caminho — e so confirma com voce antes de escrever.

---

## Passo 2 — Rascunho com o template oficial

Escreva (ou peca pro agente escrever) usando este esqueleto:

```markdown
---
name: Nome da Skill
description: |
  O que ela faz + resultado final. Executa quando o usuario diz
  "frase real 1", "frase real 2", "frase real 3", "frase real 4", "frase real 5".
version: 1.0
---

# Nome da Skill

## O que esta skill faz
[1-2 frases, com o resultado final]

## Passo a passo
1. [Primeiro passo — em imperativo: "Leia...", "Pergunte...", "Monte..."]
2. [Segundo passo]
3. [Confirmar com o usuario antes de qualquer acao externa ou irreversivel]

## Formato da entrega
[Secoes, ordem, onde salvar. Se tem modelo, cole o modelo aqui.]

## O que NUNCA fazer
- [Limite 1]
- [Limite 2]

## Exemplo
Pedido: "[frase real do usuario]"
Entrega esperada: [como fica o resultado]
```

**Regras de escrita que fazem diferenca:**
- **Imperativo direto** ("Leia o arquivo X", "Pergunte o prazo") — instrucao vaga gera execucao vaga.
- **Explique o porque** dos passos criticos ("confira o preco na tabela ANTES de escrever,
  porque preco desatualizado ja causou retrabalho") — o agente respeita mais a regra quando
  entende a razao dela.
- **Inclua 1 exemplo real** de pedido + entrega. Um exemplo bom vale mais que tres paragrafos
  de descricao.
- **Curta e magra.** Skill boa cabe em 1-2 telas. Se esta virando um manual de 500 linhas,
  provavelmente sao DUAS skills disfarcadas de uma — separe.

---

## Passo 3 — A descricao e o gatilho (capriche nela)

A `description` merece atencao especial porque e a unica parte que o agente le SEMPRE.
Tres regras:

1. **Diga o que faz E quando usar**, no mesmo texto.
2. **Liste as frases de gatilho reais** do Passo 1 ("Executa quando o usuario diz...").
3. **Seja generosa, nao timida.** O erro comum e a descricao curta demais que nunca dispara.
   Inclua variacoes: formal e informal, com e sem o nome da skill, sinonimos que voce usa.

Teste rapido: leia so a descricao e se pergunte — "se eu pedisse [frase do dia a dia],
o agente saberia que e essa skill?". Se a resposta e "talvez", adicione a frase na lista.

---

## Passo 4 — Teste real (antes de dar por pronta)

Nao declare a skill pronta sem testar. O teste e simples:

1. **Abra uma conversa NOVA** (importante: sem o historico de hoje, para o agente depender
   so da skill) e faca 2-3 pedidos reais, do jeito que voce falaria numa terca-feira qualquer.
2. **Avalie:** disparou sozinha? Seguiu os passos? Entregou no formato? Respeitou os limites?
3. **Corrija a SKILL, nao so o resultado.** Se voce precisou corrigir a entrega, volte no
   SKILL.md e ajuste a instrucao que falhou. Corrigir so o resultado conserta hoje;
   corrigir a skill conserta para sempre — e essa e a diferenca entre ter um POP vivo
   e ter um papel na gaveta.

---

## Passo 5 — Instalar no SEU agente

A skill funciona nos dois cerebros que o MeuOS suporta — o lugar de salvar e que muda:

| Agente | Onde salvar | Como ativa |
|---|---|---|
| **Claude** (Claude Code/Desktop, VSCode, Cursor) | `~/.claude/skills/{slug}/SKILL.md` | automatico — o Claude le a descricao e ativa quando o tema surge |
| **ChatGPT** (app Codex, CLI) | `.meuos/skills/{slug}/SKILL.md` na pasta do OS + 1 linha de referencia na secao "## Skills instaladas" do `AGENTS.md` | o agente le a skill quando o AGENTS.md aponta pra ela |

O `{slug}` e o nome da pasta: minusculo, sem espaco, sem acento (ex: `proposta-comercial`).
Crie a pasta se nao existir e confirme a instalacao pedindo ao agente: "quais skills voce
tem instaladas?".

---

## Seguranca — regras inviolaveis

- **NUNCA coloque dado sensivel dentro da skill:** senha, token, chave de API, CPF, dado de
  cliente, valores de contrato. A skill e um arquivo que se copia, compartilha e sincroniza —
  trate como documento publico da empresa.
- Se o procedimento PRECISA de um dado sensivel, a skill diz **ONDE buscar** ("leia a chave do
  arquivo de credenciais", "peca ao usuario na hora"), nunca carrega o dado no texto.
- **Acao externa exige confirmacao:** se a skill envia e-mail, publica, paga ou apaga algo,
  o passo correspondente deve dizer "confirmar com o usuario antes". Skill nao e licenca
  para o agente agir sozinho no mundo.

---

## Erros comuns (aprenda no atalho)

| Erro | Sintoma | Conserto |
|---|---|---|
| **Skill-polvo** | Uma skill que faz proposta + relatorio + e-mail + planilha | Separar: 1 skill = 1 tarefa com comeco, meio e fim |
| **Descricao timida** | A skill existe mas nunca dispara | Voltar ao Passo 3: mais frases de gatilho, mais variacoes |
| **Skills gemeas** | Duas skills disparam pro mesmo pedido e o agente escolhe errado | Fundir as duas, ou deixar explicito na descricao de cada uma quando NAO usar |
| **Manual copiado** | Colou um manual de 40 paginas dentro do SKILL.md | Destilar: so os passos e limites; detalhe extenso vira arquivo de referencia separado |
| **Skill congelada** | O processo mudou, a skill ficou velha e o agente segue o padrao antigo | Tratar a skill como documento vivo: mudou o processo, atualiza a skill na hora (e sobe a `version`) |

---

## Evoluir a skill

Toda vez que a skill errar ou o seu processo mudar:
1. Ajuste o SKILL.md (a instrucao especifica que falhou, nao o arquivo inteiro).
2. Suba a `version` no frontmatter (1.0 → 1.1) — assim voce sabe qual versao esta instalada onde.
3. Se voce usa os dois agentes, espelhe a mudanca nas duas instalacoes (Claude e ChatGPT).

---

## O que esta skill NAO faz

- **Nao cria automacao agendada** (coisa que roda sozinha em horario fixo) — isso e n8n/cron;
  skill e procedimento de conversa.
- **Nao publica na biblioteca oficial do MeuOS** — sua skill e sua, instalada no seu agente.
  Para dominar o modelo e receber as skills oficiais atualizadas: www.meuos.com.br.
- **Nao substitui o seu julgamento** — a skill padroniza a execucao; a decisao de negocio
  continua sendo sua.
