---
name: resumo-executivo
description: "Resume documentos, relatorios ou threads longas no formato de decisao: contexto em 3 linhas, opcoes com pros e contras, recomendacao unica e proximos passos. Usar quando o usuario disser 'resumo executivo', 'resume pra decisao', 'me da o essencial disso', 'nao tenho tempo de ler, resume', 'prepara um brief', ou enviar material longo pedindo sintese para decidir."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Resumo Executivo

## O que esta skill faz

Transforma material longo (relatorio de 40 paginas, thread de 80 emails, proposta densa, documento tecnico) em uma pagina que serve para DECIDIR: o que esta em jogo, quais os caminhos, qual o recomendado e o que fazer em seguida. O leitor do resumo e alguem sem tempo: a decisao vem na primeira linha, o detalhe fica na fonte.

**Resumo executivo nao e encurtamento do texto.** E a resposta a 3 perguntas: o que esta acontecendo, o que da pra fazer, o que voce recomenda.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 1: Ler a fonte INTEIRA

Nao resumir pelo comeco do documento nem pelo sumario dele. Ler tudo: a informacao que muda a decisao costuma estar no meio ou no anexo. Se a fonte for grande demais para uma leitura, ler por blocos e anotar os pontos de decisao de cada bloco antes de sintetizar.

### PASSO 2: Identificar a DECISAO que o material pede

Perguntar-se: "quem pediu este resumo vai fazer O QUE com ele?". Se o material nao pede decisao nenhuma (e um relatorio informativo), o formato muda: vira sintese informativa (ver Variante no fim). Em duvida sobre qual decisao importa, perguntar ao usuario em 1 linha antes de escrever.

### PASSO 3: Montar no template (com limites de tamanho)

```markdown
# Resumo executivo: [tema]

**Decisao pendente:** [a decisao, em 1 frase, logo na primeira linha]

## Contexto (maximo 3 linhas)
[O que esta acontecendo e por que importa agora. 3 linhas. Nao 4.]

## Opcoes
| # | Opcao | Pros | Contras |
|---|---|---|---|
| 1 | ... | ... | ... |
| 2 | ... | ... | ... |

## Recomendacao
[UMA opcao, com o porque em 1-2 linhas. Riscos da propria recomendacao em 1 linha.]

## Proximos passos
| # | Acao | Dono | Prazo |
|---|---|---|---|
| 1 | ... | ... | ... |

## Fonte
[Documento/thread de origem, com caminho ou link, e data]
```

**Limites de tamanho (duros, nao sugestao):**

| # | Bloco | Limite |
|---|---|---|
| 1 | Resumo completo | 1 pagina (~400 palavras) |
| 2 | Contexto | 3 linhas |
| 3 | Opcoes | maximo 4; cada uma em ate 2 linhas de pros + contras |
| 4 | Recomendacao | 1 opcao so, com porque em 1-2 linhas |
| 5 | Proximos passos | maximo 5 acoes |

### PASSO 4: Regras de conteudo

1. **Recomendacao e obrigatoria.** Resumo que termina em "depende" nao ajuda a decidir. Se faltar informacao para recomendar, a recomendacao vira: "falta X para decidir; sugiro obter X primeiro" (isso tambem e uma recomendacao).
2. **Numero citado = numero conferido.** Todo valor, percentual e data do resumo tem que existir na fonte. Zero invencao: na duvida, nao cita.
3. **Jargao traduzido.** O leitor pode nao ser da area. Termo tecnico entra com 1 explicacao entre parenteses ou fica de fora.
4. **Riscos da recomendacao aparecem.** Recomendar sem dizer o risco e vender, nao assessorar.
5. **A fonte fica apontada.** Quem quiser o detalhe sabe onde esta. O resumo nunca substitui a fonte, ele economiza a leitura dela.

### PASSO 5: Entregar e guardar

1. Entregar o resumo no chat (a decisao pendente na primeira linha).
2. Se o usuario tiver um OS organizado, oferecer guardar no contexto certo como `AAAA-MM-DD-resumo-[tema].md` e indexar.

---

## Variante: sintese informativa (quando nao ha decisao)

Material que so informa (ex: relatorio de mercado) segue o mesmo espirito com blocos adaptados: **3 destaques** (1 linha cada) + **o que muda para nos** (2-3 linhas) + **vale ler a fonte inteira?** (sim/nao e por que). Mesmo limite de 1 pagina.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Fonte lida INTEIRA (nao so o comeco/sumario)
- [ ] Decisao pendente identificada e na PRIMEIRA linha
- [ ] Contexto em no maximo 3 linhas
- [ ] Maximo 4 opcoes, cada uma com pros e contras
- [ ] Recomendacao unica presente, com porque e risco
- [ ] Todo numero do resumo conferido contra a fonte
- [ ] Resumo cabe em 1 pagina (~400 palavras)
- [ ] Fonte apontada no fim (caminho/link + data)

Se algum item falhou: corrigir ANTES de declarar concluido. Nunca reportar "feito" com item pendente.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
