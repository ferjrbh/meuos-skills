---
name: decisao-dificil
description: "Copiloto de decisão para o gestor: enquadra a decisão em uma frase, lista as opções (inclusive não fazer nada), define critérios com peso escolhido pelo gestor, faz as contas com conta explícita (custo, retorno, payback, cenários pessimista, base e otimista), avalia riscos e reversibilidade, roda um pré-mortem, diz o que mudaria a decisão e entrega uma recomendação única com o primeiro passo, em uma página para levar à diretoria ou ao sócio. Usar quando o usuário disser 'estou em dúvida entre', 'me ajuda a decidir', 'vale a pena investir em', 'contrato ou não contrato', 'qual opção eu escolho', 'preciso levar essa decisão pro sócio', ou descrever um dilema com dinheiro, gente ou prazo em jogo."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Decisão Difícil

## O que esta skill faz

Organiza uma decisão que está travada (contratar ou não, abrir filial, trocar de fornecedor, comprar o sistema, aceitar o cliente grande com margem baixa) em uma página que dá para levar à diretoria ou ao sócio. O gestor sai com a decisão escrita em uma frase, as opções lado a lado, os números com a conta à vista em três cenários, os riscos de cada caminho, o que pode dar errado e uma recomendação única com o primeiro passo.

**A skill não decide pelo gestor.** Ela deixa a decisão com o critério dele, os números dele e os riscos à mostra. A recomendação é do agente, assinada como recomendação; a decisão continua sendo de quem responde por ela.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Contexto e enquadramento

Perguntar em 1 mensagem curta (pular o que o usuário já disse):

> "Para organizar a decisão: (1) de qual empresa ou contexto do seu OS ela é? (2) qual é a decisão, em uma frase? (3) até quando precisa ser tomada? (4) quem decide junto com você ou aprova?"

| # | Resposta | O que muda |
|---|---|---|
| 1 | Contexto | Com OS no padrão MeuOS: ler o documento mestre daquele contexto (metas, caixa, decisões anteriores sobre o tema) e citar de onde veio cada dado usado. Nunca misturar contextos |
| 2 | Decisão | Reescrever no formato **"Devemos [ação] até [data], sim ou não?"** ou **"Qual entre A, B e C para [objetivo]?"**. Confirmar com o usuário antes de seguir |
| 3 | Prazo | Decisão para hoje: versão enxuta (opções, números base, recomendação). Com mais prazo: completo |
| 4 | Quem aprova | Define a linguagem da página final |

Se o usuário descrever um problema e não uma decisão ("as vendas caíram"), ajudar a chegar na decisão ("cortamos o vendedor externo ou investimos em mídia?") antes de qualquer conta.

### PASSO 1: Opções

Listar de 2 a 4 opções. **"Não fazer nada / manter como está" entra sempre**, com o custo de ficar parado. Perguntar se existe uma opção intermediária (testar pequeno, adiar com data, fazer metade). Opção que o usuário descarta logo de cara pode ficar fora, registrando o motivo.

### PASSO 2: Critérios com peso do gestor

Propor de 3 a 6 critérios (ex.: retorno financeiro, caixa necessário, risco, tempo até o resultado, impacto na equipe, encaixe com a estratégia) e **pedir ao gestor os pesos**, somando 100%. O agente não define peso; pode sugerir uma distribuição e pedir confirmação.

Notas de 1 a 5 por opção em cada critério, com uma linha de justificativa. A nota final é a média ponderada, com a conta à vista:
`Opção A: (4 × 30%) + (2 × 25%) + (5 × 20%) + (3 × 25%) = 1,2 + 0,5 + 1,0 + 0,75 = 3,45`

### PASSO 3: Números com conta explícita

Pedir ao usuário os números que ele tem: investimento inicial, custo mensal, receita ou economia esperada por mês, prazo. **Todo número vem do usuário, de documento dele ou de fonte pública citada com link e data.** O que faltar fica como "não informado" e vira pergunta; o agente não preenche com "média de mercado" de memória.

Calcular para cada opção, em três cenários definidos com o usuário (ex.: pessimista = 60% do retorno esperado, base = 100%, otimista = 130%; o gestor ajusta os percentuais):

| # | Indicador | Fórmula |
|---|---|---|
| 1 | Resultado mensal | retorno mensal − custo mensal |
| 2 | Payback (meses) | investimento inicial ÷ resultado mensal (se resultado ≤ 0: "não se paga") |
| 3 | Resultado em 12 meses | (resultado mensal × 12) − investimento inicial |
| 4 | Caixa máximo exposto | o ponto mais baixo do saldo acumulado (investimento inicial negativo + resultados mês a mês), em valor positivo; com resultado mensal fixo e positivo, é o próprio investimento inicial; com resultado mensal zero ou negativo, escrever "não se paga" |

**A conta é feita por código** (Python ou JavaScript) quando o agente tiver como executar, mostrando o script e o resultado. Sem execução de código, fazer passo a passo por escrito, uma linha por conta, e reconferir os totais. Nunca entregar número "de cabeça".

Se a decisão não é financeira (ex.: promover A ou B), pular este passo e dizer isso na página final.

### PASSO 4: Riscos e reversibilidade

| # | Opção | Principal risco | Probabilidade (baixa/média/alta) | Reversível? | Custo de voltar atrás |
|---|---|---|---|---|---|

Probabilidade é julgamento do gestor; o agente sugere e pergunta. **Decisão reversível e barata de desfazer pede menos análise; irreversível pede mais.** Dizer isso explicitamente.

### PASSO 5: Pré-mortem

Pedir ao gestor: "Imagine que estamos daqui a 1 ano e a opção escolhida deu muito errado. Por quê?". Coletar 3 a 5 motivos (o agente pode sugerir os que o gestor não citou). Para cada motivo, um sinal de alerta que dá para acompanhar e uma ação para reduzir a chance.

### PASSO 6: O que mudaria a decisão

Listar de 1 a 3 fatos que, se forem diferentes do que se supôs, invertem a recomendação (ex.: "se o fornecedor não aceitar contrato de 6 meses", "se o retorno ficar abaixo de R$ X por mês"). Calcular, quando possível, o **ponto de virada**: o valor que empata as duas melhores opções.

### PASSO 7: Recomendação e primeiro passo

Uma opção só, com o porquê em 2 linhas e o risco principal em 1 linha. Se faltar dado crítico, a recomendação é "obter X antes de decidir, até [data]". Fechar com o primeiro passo: ação, dono e data.

### PASSO 8: Entregar e guardar

1. Entregar a página no template abaixo.
2. Com OS no padrão MeuOS, oferecer guardar no contexto do PASSO 0 como `AAAA-MM-DD-decisao-[tema].md` e atualizar o `index.md`. Sugerir revisitar em 90 dias para comparar o que aconteceu com o que se previu.

---

## Template de saída (1 página)

```markdown
# Decisão: [frase da decisão]

**Prazo:** DD/MM · **Decide:** [quem] · **Preparado em:** DD/MM/AAAA
**Recomendação:** [opção], porque [motivo em 1 linha]. Principal risco: [1 linha].

## Opções
| # | Opção | Em uma linha |
|---|---|---|
| 1 | Não fazer nada | custo de ficar parado: ... |

## Critérios (pesos definidos por [quem])
| # | Critério | Peso | Opção 1 | Opção 2 | Opção 3 |
|---|---|---|---|---|---|
| | **Nota ponderada** | 100% | x,xx | x,xx | x,xx |

## Números (base: [fonte dos dados])
| # | Opção | Cenário | Resultado mensal | Payback | Resultado 12 meses | Caixa máximo exposto |
|---|---|---|---|---|---|---|

Conta: [script ou passo a passo]. Não informado: [lista].

## Riscos
| # | Opção | Risco | Probabilidade | Reversível? |
|---|---|---|---|---|

## Pré-mortem: se der errado em 1 ano, terá sido porque...
| # | Motivo | Sinal de alerta | Como reduzir |
|---|---|---|---|

## O que mudaria a decisão
- ...

## Primeiro passo
**O quê:** ... · **Quem:** ... · **Até:** ...
```

---

## Regras desta skill

- **Número com origem.** Cada número diz de onde veio: usuário, documento (nome) ou fonte pública (link e data). Sem origem, não entra.
- **Conta por código ou por escrito, nunca de cabeça.**
- **Peso é do gestor.** O agente sugere, o gestor define.
- **"Não fazer nada" sempre na mesa.** Ficar parado também custa.
- **Uma recomendação só.** "Depende" não ajuda; se falta dado, a recomendação é buscar o dado.
- **Cabe em uma página.** Detalhe extra vai em anexo, não na página principal.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Decisão escrita em uma frase e confirmada pelo usuário
- [ ] "Não fazer nada" entre as opções
- [ ] Pesos dos critérios definidos pelo gestor, somando 100%
- [ ] Nota ponderada com a conta à vista
- [ ] Números com origem declarada e conta por código ou passo a passo
- [ ] Três cenários calculados (ou dito por que a decisão não é financeira)
- [ ] Riscos e reversibilidade de cada opção
- [ ] Pré-mortem com sinal de alerta e ação
- [ ] O que mudaria a decisão listado
- [ ] Recomendação única com primeiro passo, dono e data
- [ ] Se guardado no OS: nome `AAAA-MM-DD-decisao-[tema].md` e `index.md` atualizado

Se algum item falhou: corrigir ANTES de declarar concluído. Nunca reportar "feito" com item pendente.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
