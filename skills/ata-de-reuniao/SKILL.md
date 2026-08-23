---
name: ata-de-reuniao
description: "Transforma transcricao, audio ou anotacoes soltas de reuniao em ata pronta: participantes, pauta, decisoes, acoes com dono e prazo, pendencias e proxima reuniao. Usar quando o usuario disser 'faz a ata', 'ata da reuniao', 'transforma essa transcricao em ata', 'registra a reuniao', 'minutas da reuniao', ou enviar uma gravacao/transcricao pedindo organizacao."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Ata de Reuniao

## O que esta skill faz

Pega o material bruto de uma reuniao (transcricao automatica, audio, anotacoes rabiscadas, thread de chat) e devolve uma ata limpa e acionavel: quem estava, o que foi decidido, quem faz o que ate quando, e o que ficou pendente. A ata e o registro que evita a reuniao seguinte comecar com "o que mesmo que a gente combinou?".

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 1: Receber e preparar a fonte

| # | Fonte recebida | O que fazer |
|---|---|---|
| 1 | Transcricao em texto | Ler INTEIRA antes de escrever qualquer linha da ata |
| 2 | Audio/video | Transcrever primeiro (se o agente tiver capacidade); sem capacidade, pedir a transcricao ao usuario |
| 3 | Anotacoes soltas | Ler tudo e pedir ao usuario o que faltar (data, participantes) |
| 4 | Thread de chat/email | Ler a thread completa, na ordem |

**Regra de ouro: a ata so contem o que esta na fonte.** Lacuna e lacuna: o que a fonte nao diz entra como "nao informado" ou vira pergunta ao usuario. NUNCA inventar decisao, prazo, valor ou fala.

### PASSO 2: Extrair os 5 blocos

1. **Participantes** (e ausentes relevantes, se citados)
2. **Decisoes tomadas**: o que foi batido o martelo (decisao e diferente de discussao: "discutimos precos" nao e decisao; "aprovamos o reajuste de 8%" e)
3. **Acoes**: tarefa + dono + prazo
4. **Pendencias**: o que ficou aberto, sem dono ou sem prazo, ou dependendo de terceiro
5. **Proxima reuniao** (data/pauta, se definida)

### PASSO 3: Completar dono e prazo ANTES de finalizar

Acao sem dono e sem prazo nao e acao, e desejo. Antes de entregar a ata:

- Listar ao usuario as acoes que ficaram sem dono ou sem prazo e perguntar as principais.
- O que o usuario nao definir, registrar como "sem dono" / "sem prazo", visivel na tabela, nunca escondido.

### PASSO 4: Montar a ata no template

```markdown
# Ata: [Titulo da reuniao]

**Data:** DD/MM/AAAA · **Hora:** HH:MM as HH:MM · **Canal:** [presencial/video/telefone]
**Participantes:** [nomes]
**Ausentes (se relevante):** [nomes]

## Pauta
1. [item]
2. [item]

## Decisoes
| # | Decisao | Contexto (1 linha) |
|---|---|---|
| 1 | ... | ... |

## Acoes
| # | Acao | Dono | Prazo |
|---|---|---|---|
| 1 | ... | ... | DD/MM |
| 2 | ... | sem dono | sem prazo |

## Pendencias (sem decisao nesta reuniao)
| # | Pendencia | O que destrava |
|---|---|---|
| 1 | ... | ... |

## Proxima reuniao
[data e pauta, ou "nao definida"]
```

### PASSO 5: Revisar contra a fonte

Antes de entregar, reler a ata comparando com a fonte:

- Cada decisao e cada numero (valor, prazo, quantidade) confere com o que foi dito?
- Nomes proprios estao escritos exatamente como o usuario escreve (transcricao automatica erra nome: na duvida, perguntar)?
- Nada foi inventado para "completar" a ata?

### PASSO 6: Entregar e guardar

1. Entregar a ata no chat.
2. Se o usuario tiver um OS organizado, oferecer guardar no contexto certo com o nome `AAAA-MM-DD-ata-[tema].md` e indexar (padrao da skill `organiza-pra-mim`).

---

## Regras desta skill

- **Fonte manda.** Ata e registro, nao interpretacao criativa. Opiniao do agente nao entra.
- **Decisao separada de discussao.** So entra em "Decisoes" o que foi de fato fechado.
- **Numero por escrito e conferido.** Valor, percentual e prazo sao os itens que mais causam briga depois: conferir cada um contra a fonte.
- **Fala sensivel nao vira ata sem confirmacao.** Comentario pessoal, critica a alguem ausente ou assunto confidencial: perguntar ao usuario se entra antes de registrar.
- **Ata longa e ata ruim.** O alvo e caber em 1 pagina. Discussao extensa vira 1 linha de contexto por decisao, nao parafrase da conversa inteira.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Fonte lida/transcrita INTEIRA antes de escrever
- [ ] Toda decisao e todo numero conferidos contra a fonte (zero invencao)
- [ ] Toda acao tem dono e prazo, ou esta marcada "sem dono"/"sem prazo" visivel
- [ ] Pendencias listadas separadas das decisoes
- [ ] Nomes proprios conferidos (transcricao automatica erra nome)
- [ ] Ata cabe em ~1 pagina
- [ ] Usuario confirmou itens sensiveis antes do registro
- [ ] Se foi guardada no OS: nome padronizado + index atualizado

Se algum item falhou: corrigir ANTES de declarar concluido. Nunca reportar "feito" com item pendente.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
