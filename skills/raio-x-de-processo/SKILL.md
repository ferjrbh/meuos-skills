---
name: raio-x-de-processo
description: "Entrevista guiada que mapeia um processo da empresa passo a passo (quem faz, quanto tempo leva, quantas vezes acontece, ferramentas, onde trava, onde erra), calcula as horas gastas por mês com a conta à vista, classifica cada passo (eliminar, simplificar, automatizar com regra, usar IA, manter humano) e entrega o ranking de por onde começar mais um primeiro passo para esta semana. Usar quando o usuário disser 'raio-x do processo', 'mapeia esse processo pra mim', 'onde a IA ajuda nesse processo', 'quanto tempo a gente perde com isso', 'por onde começo a automatizar', ou descrever uma rotina da equipe pedindo diagnóstico."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Raio-X de Processo

## O que esta skill faz

Pega um processo que hoje "simplesmente acontece" (fechar o caixa, emitir proposta, cobrar inadimplente, conferir pedido, agendar consulta) e mostra, em números, quanto ele custa em horas e onde está o desperdício. O gestor sai com três coisas: a fotografia do processo passo a passo, a conta das horas por mês (com cada multiplicação visível) e um ranking de por onde começar, com uma ação concreta para esta semana.

**Esta skill não automatiza nada.** Ela diagnostica. A regra é simples: só vale automatizar o que você já entendeu, e só vale entender o que você mediu.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Contexto e escolha do processo

Perguntar em 1 mensagem curta (pular o que o usuário já disse):

> "Antes do raio-x: (1) de qual empresa ou contexto do seu OS é esse processo? (2) qual o nome do processo e onde ele começa e termina (ex.: 'do pedido do cliente até a nota emitida')? (3) quem vai ler o resultado: só você, a equipe ou a diretoria?"

| # | Resposta | O que muda |
|---|---|---|
| 1 | Contexto | Se o usuário tem OS no padrão MeuOS (pastas por contexto, documento mestre, `index.md`), ler o documento mestre daquele contexto para acertar nomes de áreas, ferramentas e siglas. Nunca usar informação de outro contexto |
| 2 | Começo e fim | Delimita o processo. Sem começo e fim claros, o mapa vira "a empresa inteira" e não serve para nada |
| 3 | Leitor | Diretoria: destacar horas e custo. Equipe: destacar onde trava e o que muda no dia a dia |

Se o usuário citar mais de um processo, pedir para escolher **um** agora. Os outros ficam para rodadas seguintes.

### PASSO 1: Entrevista passo a passo

Pedir que o usuário descreva o processo como se estivesse contando para alguém novo, do primeiro ao último passo. Depois, para **cada passo**, completar estas 7 informações, uma rodada de perguntas por vez (no máximo 3 passos por mensagem, para não cansar):

| # | Pergunta | Por que importa |
|---|---|---|
| 1 | Quem faz? (cargo, não nome, se o relatório for circular) | Mostra concentração em uma pessoa só |
| 2 | Quanto tempo leva cada vez? (em minutos) | Base da conta de horas |
| 3 | Quantas vezes acontece? (por dia, semana ou mês) | Base da conta de horas |
| 4 | Qual ferramenta usa? (planilha, sistema, WhatsApp, papel, e-mail) | Mostra retrabalho de copiar e colar |
| 5 | Onde trava? (espera aprovação, falta informação, sistema lento) | Mostra fila e gargalo |
| 6 | Onde costuma dar erro? E com que frequência? | Mostra custo escondido de correção |
| 7 | O que acontece se esse passo não for feito? | Separa o essencial do hábito |

**Regras da entrevista:**
- Tempo e frequência em faixa servem ("entre 10 e 20 minutos"): usar o ponto médio e registrar que é estimativa.
- Se o usuário não souber, registrar "não sei" e sugerir como medir (cronometrar 3 vezes nesta semana). Nunca chutar um número no lugar dele.
- Ler o que o usuário mandar (planilha, print, fluxograma, procedimento escrito) INTEIRO antes de perguntar o que já está lá.

### PASSO 2: Montar a tabela do processo

Devolver a tabela para o usuário conferir antes de qualquer conta:

| # | Passo | Quem faz | Min/vez | Frequência | Ferramenta | Onde trava | Erro comum |
|---|---|---|---|---|---|---|---|
| 1 | Receber pedido por WhatsApp | Atendente | 5 | 40/semana | WhatsApp | Cliente manda incompleto | Falta CNPJ |

Perguntar: "a tabela está fiel ao que acontece de verdade, ou ao que deveria acontecer?". O raio-x é do processo **real**.

### PASSO 3: Calcular as horas por mês com a conta à vista

Converter tudo para mês com fatores fixos e declarados:

| # | Unidade informada | Fator para mês | De onde vem |
|---|---|---|---|
| 1 | Por dia útil | × 21 | média de dias úteis no mês (confirmar com o usuário se a operação roda sábado) |
| 2 | Por semana | × 4,33 | 52 semanas ÷ 12 meses |
| 3 | Por mês | × 1 | já está no mês |

Fórmula por passo: **horas/mês = (minutos por vez × vezes por mês) ÷ 60**.

Mostrar a conta de cada linha por extenso, assim:
`Passo 1: 5 min × (40 × 4,33 = 173,2 vezes/mês) = 866 min ÷ 60 = 14,4 h/mês`

Se o agente tiver como rodar código (Python ou JavaScript), fazer a conta por código e mostrar o resultado; se não tiver, fazer passo a passo por escrito, linha por linha, e conferir a soma no fim. Nunca entregar total "de cabeça".

**Custo em reais é opcional.** Só calcular se o usuário informar o custo-hora (salário + encargos ÷ horas trabalhadas, número que vem dele). Sem esse dado, o relatório fica em horas e diz "custo em reais: não informado".

### PASSO 4: Classificar cada passo

| # | Classe | Quando usar | Exemplo |
|---|---|---|---|
| 1 | Eliminar | Ninguém usa o resultado, ou existe só por hábito | Relatório impresso que ninguém lê |
| 2 | Simplificar | Necessário, mas com etapas demais ou aprovação redundante | Três assinaturas para compra de R$ 50 |
| 3 | Automatizar com regra | Repetitivo, previsível, sempre a mesma lógica "se X então Y" | Copiar dados do formulário para a planilha |
| 4 | Usar IA | Envolve ler, resumir, classificar ou redigir texto variado | Triar e-mails de clientes por assunto |
| 5 | Manter humano | Exige julgamento, relação ou responsabilidade legal | Negociar desconto com cliente grande |

Ordem de raciocínio: primeiro perguntar se dá para **eliminar**, depois **simplificar**, só então automatizar. Automatizar um passo inútil é desperdiçar mais rápido.

### PASSO 5: Ranking de por onde começar

Para cada passo que não é "manter humano", dar nota de 1 a 3 em:

| # | Critério | 1 | 2 | 3 |
|---|---|---|---|---|
| 1 | Ganho (horas/mês liberadas) | menos de 2 h | 2 a 10 h | mais de 10 h |
| 2 | Esforço (inverso: 3 = fácil) | precisa de sistema novo ou TI | precisa de ferramenta que a empresa já tem, com ajuste | dá para fazer esta semana sem comprar nada |
| 3 | Risco (inverso: 3 = baixo) | erro afeta cliente, dinheiro ou obrigação legal | erro é interno e reversível com trabalho | erro é irrelevante ou fácil de desfazer |

**Prioridade = Ganho × Esforço × Risco** (de 1 a 27). Mostrar a multiplicação de cada linha. Ordenar do maior para o menor. Empate: vence o de menor risco.

As faixas de horas são padrão desta skill; se o usuário preferir outras, usar as dele e registrar no relatório.

### PASSO 6: Primeiro passo para esta semana

Escolher o 1º do ranking e transformar em uma ação de até 2 horas, com dono e data:

- Ruim: "automatizar o cadastro de clientes".
- Bom: "na quinta, a atendente cronometra 5 cadastros e o gestor testa um formulário único que já pede CNPJ, para medir se o retrabalho cai".

### PASSO 7: Entregar e guardar

1. Entregar o relatório no template abaixo.
2. Se o usuário tem OS no padrão MeuOS, oferecer guardar no contexto informado no PASSO 0 com o nome `AAAA-MM-DD-raio-x-[processo].md` e atualizar o `index.md`. Sem OS, entregar no chat e oferecer o arquivo .md para download.

---

## Template de saída

```markdown
# Raio-X do processo: [nome do processo]

**Data:** DD/MM/AAAA · **Começa em:** [gatilho] · **Termina em:** [entrega]
**Leitor:** [você / equipe / diretoria] · **Origem dos números:** [estimativa do gestor / medição cronometrada]

## Resumo em 3 linhas
- Total: **XX h/mês** em [N] passos, com [N] pessoas envolvidas. [Se algum passo ficou "não sei": **PARCIAL: faltam N passos**]
- Maior consumo: [passo], com XX h/mês (XX% do total).
- Começar por: [passo], prioridade XX/27.

## O processo hoje
| # | Passo | Quem faz | Min/vez | Frequência | Ferramenta | Onde trava | Erro comum |
|---|---|---|---|---|---|---|---|

## A conta das horas
| # | Passo | Conta | Horas/mês |
|---|---|---|---|
| 1 | ... | 5 min × 173,2 vezes ÷ 60 | 14,4 |
| | **Total** | soma das linhas | **XX,X** [ou **XX,X (PARCIAL: faltam N passos)**] |

Fatores usados: dia útil × 21 · semana × 4,33. Custo em reais: [valor e conta, ou "não informado"].

## Classificação e ranking [PARCIAL: faltam N passos, se algum passo ficou "não sei"]
| # | Passo | Classe | Ganho | Esforço | Risco | Prioridade (G×E×R) |
|---|---|---|---|---|---|---|

Passo com "não sei" não entra na conta: o total e o ranking saem marcados **PARCIAL: faltam N passos** até o número ser medido.

## Primeiro passo desta semana
**O quê:** ... · **Quem:** ... · **Quando:** ... · **Como saber se funcionou:** ...

## O que não foi medido
- [números que vieram como "não sei" e como medir]
```

---

## Regras desta skill

- **Número vem do usuário.** Tempo, frequência e custo-hora são dele. O agente não chuta; registra "não sei" e ensina a medir.
- **Conta sempre à vista.** Toda hora no relatório tem a multiplicação que a gerou.
- **Um processo por vez.** Mapear a empresa inteira numa rodada produz um mapa raso e inútil.
- **Processo real, não o do manual.** Se o usuário descrever o ideal, perguntar o que acontece quando dá errado.
- **Eliminar antes de automatizar.** Toda recomendação de automação ou IA passa antes pela pergunta "esse passo precisa existir?".
- **Nada de prometer ferramenta.** A skill pode citar o tipo de solução (formulário, regra de planilha, assistente de IA), nunca garantir resultado de produto específico.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Contexto, começo e fim do processo e leitor definidos no PASSO 0
- [ ] Cada passo com as 7 informações, ou com "não sei" visível
- [ ] Tabela do processo conferida pelo usuário antes das contas
- [ ] Toda hora/mês com a conta escrita e fatores de conversão declarados
- [ ] Total conferido (soma das linhas bate com o total)
- [ ] Cada passo classificado, com eliminar e simplificar considerados primeiro
- [ ] Ranking com Ganho × Esforço × Risco mostrado linha a linha
- [ ] Primeiro passo com o quê, quem, quando e como medir
- [ ] Seção "o que não foi medido" preenchida
- [ ] Se guardado no OS: nome `AAAA-MM-DD-raio-x-[processo].md` e `index.md` atualizado

Se algum item falhou: corrigir ANTES de declarar concluído. Nunca reportar "feito" com item pendente.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
