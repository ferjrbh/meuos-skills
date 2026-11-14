---
name: conversa-dificil
description: "Prepara o gestor para uma conversa difícil (feedback negativo, cobrança de resultado, desligamento, negociação de preço ou prazo, dizer não a cliente ou chefe): entende a situação e o objetivo, monta o roteiro com abertura, fatos observáveis, impacto, pedido claro e escuta, antecipa as reações prováveis com resposta para cada uma, lista frases a evitar e oferece ensaio com o agente no papel da outra pessoa. Para mensagem escrita, gera versão direta e versão cuidadosa. Usar quando o usuário disser 'preciso ter uma conversa difícil', 'como eu falo isso pro meu funcionário', 'vou ter que demitir alguém', 'como digo não pro cliente', 'me ajuda a negociar o prazo', 'quero ensaiar essa conversa', ou pedir ajuda para escrever uma mensagem delicada."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Conversa Difícil

## O que esta skill faz

Ajuda o gestor a entrar preparado na conversa que ele está adiando. Em vez de improvisar sob pressão, ele chega com um roteiro curto, sabe o que quer sair da conversa, já pensou nas reações mais prováveis da outra pessoa e, se quiser, ensaiou antes com o agente fazendo o papel do outro lado.

A base do método é separar **fato** (o que qualquer câmera filmaria) de **julgamento** (o que o gestor concluiu), dizer o **impacto** concreto e terminar com um **pedido** claro. Firme no conteúdo, respeitoso na forma.

> ⚠️ **Alerta de risco jurídico.** Desligamento por justa causa, suspeita de assédio, discriminação, acidente de trabalho, gestante, afastamento por saúde ou qualquer situação que possa virar processo: **envolva RH e jurídico antes da conversa.** A skill ajuda na forma de falar; não decide se o desligamento ou a punição pode ser feito, nem como.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Contexto e tipo de conversa

Perguntar em 1 mensagem curta (pular o que o usuário já disse):

> "Para preparar a conversa: (1) de qual empresa ou contexto do seu OS é isso? (2) com quem é a conversa (cargo e relação com você: liderado, par, chefe, cliente, fornecedor, sócio)? (3) vai ser ao vivo, por vídeo ou por mensagem escrita? (4) quando?"

| # | Resposta | O que muda |
|---|---|---|
| 1 | Contexto | Com OS no padrão MeuOS: ler o documento mestre daquele contexto só para entender papéis e combinados (ex.: política de prazos, metas). Não registrar nada pessoal sobre a outra pessoa no OS sem pedido explícito. Nunca misturar contextos |
| 2 | Relação | Muda o poder na conversa: com liderado o gestor decide; com chefe ou cliente ele propõe |
| 3 | Canal | Ao vivo: roteiro + reações + ensaio. Escrito: duas versões de mensagem (PASSO 5) |
| 4 | Quando | Se for hoje, ir direto ao roteiro enxuto |

**Checagem de risco:** se a situação envolver qualquer item do alerta acima, mostrar o alerta antes de seguir e perguntar se RH ou jurídico já foi envolvido.

### PASSO 1: Entender a situação

Perguntar, um bloco só:
1. O que aconteceu? Peça exemplos concretos, com data ou ocasião.
2. Isso já foi conversado antes? O que foi combinado?
3. O que você quer que mude depois da conversa? (o **objetivo**: um comportamento, um acordo, uma decisão comunicada)
4. O que está em jogo para você e para a outra pessoa? (emprego, cliente, relação, dinheiro, reputação)
5. Qual o seu limite? O que você aceita ceder e o que não aceita?
6. O que você imagina que a outra pessoa pensa da situação?

Se o usuário só trouxer julgamentos ("ele é desleixado", "o cliente é folgado"), pedir o fato por trás: "o que exatamente ele fez ou deixou de fazer, e quando?".

### PASSO 2: Montar o roteiro em 5 partes

| # | Parte | O que é | Duração na conversa |
|---|---|---|---|
| 1 | Abertura | Diz o assunto logo no início, sem rodeio e sem elogio-sanduíche | 1 frase |
| 2 | Fatos | O que aconteceu, observável, com exemplo e data | 2 a 3 frases |
| 3 | Impacto | O que isso causou (cliente, equipe, resultado, dinheiro) | 1 a 2 frases |
| 4 | Pedido | O que precisa mudar ou o que foi decidido, com prazo quando couber | 1 frase |
| 5 | Escuta | Pergunta aberta e silêncio para a outra pessoa responder | o tempo que precisar |

Em desligamento já decidido, o "pedido" vira **comunicação da decisão**, que não está em negociação; a escuta serve para acolher e explicar os próximos passos práticos (que o usuário confirma com RH).

### PASSO 3: Antecipar 3 a 5 reações

Listar as reações mais prováveis para aquele perfil e situação, com uma resposta sugerida para cada:

| # | Reação provável | O que pode estar por trás | Resposta sugerida |
|---|---|---|---|
| 1 | Nega ("isso não aconteceu") | Defesa | Voltar ao fato com data, sem discutir intenção |
| 2 | Culpa outra pessoa | Proteção | Reconhecer o contexto e voltar ao que é dela |
| 3 | Chora ou fica em silêncio | Impacto emocional | Pausar, oferecer água ou tempo, não recuar no conteúdo |
| 4 | Ataca ("e você, que...") | Contra-ataque | Anotar o ponto, combinar de tratar depois, voltar ao assunto |
| 5 | Concorda rápido demais | Querer encerrar | Pedir que diga com as palavras dela o que vai mudar |

Ajustar as reações ao caso real; os exemplos acima são ponto de partida, não lista fixa.

### PASSO 4: Frases a evitar

Apontar no rascunho do usuário e listar no roteiro as frases que costumam piorar: generalizações ("você sempre", "você nunca"), rótulos ("você é irresponsável"), comparações com colegas, ameaça vaga, promessa que o gestor não pode cumprir, e pedido de desculpas pelo conteúdo ("desculpa, mas..."). Para cada uma, oferecer a troca.

### PASSO 5: Mensagem escrita (quando o canal for escrito)

Gerar duas versões, as duas com fato, impacto e pedido:
- **Direta:** curta, objetiva, para quem prefere ir ao ponto ou quando já houve conversa antes.
- **Cuidadosa:** reconhece a relação e o contexto, mesmo conteúdo, tom mais acolhedor.

Recomendar uma das duas e dizer por quê. Lembrar que assunto sensível (desligamento, advertência) por escrito deve passar por RH antes do envio.

### PASSO 6: Ensaio (oferecer sempre)

Perguntar: "Quer ensaiar? Eu faço o papel de [pessoa], com a reação mais provável. Diga quando quiser parar."

Durante o ensaio:
- O agente responde como a outra pessoa responderia, de forma realista (nem fácil demais, nem caricata).
- Uma rodada por vez; o usuário pode pedir "mais difícil" ou "outra reação".
- Ao final, sair do papel e dar feedback em 3 pontos: o que funcionou, o que soou como julgamento ou ameaça, e uma frase para trocar.

### PASSO 7: Entregar e guardar

1. Entregar o roteiro no template abaixo.
2. Com OS no padrão MeuOS, **perguntar** se quer guardar (conversa difícil costuma ser sensível). Se sim, nome `AAAA-MM-DD-conversa-[tema].md`, sem nome completo da outra pessoa no título, e atualizar o `index.md`.

---

## Template de saída

```markdown
# Roteiro: conversa sobre [tema]

**Com:** [cargo/relação] · **Quando:** [data] · **Canal:** [ao vivo/vídeo/escrito]
**Objetivo:** [o que precisa estar diferente depois da conversa]
**Meu limite:** [o que aceito ceder / o que não aceito]
**Risco jurídico:** [nenhum identificado / RH e jurídico envolvidos em DD/MM]

## Roteiro
1. **Abertura:** "..."
2. **Fatos:** "..."
3. **Impacto:** "..."
4. **Pedido:** "..."
5. **Escuta:** "..." (e silêncio)

## Reações prováveis
| # | Se a pessoa... | Eu respondo... |
|---|---|---|

## Frases a evitar
| # | Evitar | Trocar por |
|---|---|---|

## Fechamento
- Combinado: [o que ficou acertado]
- Próximo ponto de checagem: [data]
```

---

## Regras desta skill

- **Fato antes de julgamento.** Todo roteiro se apoia em fatos que o usuário informou. O agente não inventa episódio, data ou fala.
- **Não diagnosticar a outra pessoa.** Nada de rótulo psicológico ("ele é narcisista", "ela tem ansiedade").
- **Risco jurídico tem prioridade.** Diante de justa causa, assédio, discriminação ou situação protegida, o alerta vem antes do roteiro, e a orientação é envolver RH e jurídico.
- **Firmeza sem crueldade.** O roteiro não humilha, não ameaça e não expõe a pessoa a terceiros.
- **Sigilo.** Detalhes da conversa não vão para o OS sem o usuário pedir, e nunca para outro contexto.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Contexto, relação, canal e data definidos no PASSO 0
- [ ] Checagem de risco jurídico feita, com alerta mostrado quando aplicável
- [ ] Objetivo e limite do usuário registrados
- [ ] Roteiro com as 5 partes, fatos observáveis e sem rótulos
- [ ] 3 a 5 reações prováveis com resposta para cada
- [ ] Frases a evitar com troca sugerida
- [ ] Se escrito: versões direta e cuidadosa, com recomendação
- [ ] Ensaio oferecido (e feedback dado, se aconteceu)
- [ ] Guardar no OS só com autorização, nome `AAAA-MM-DD-conversa-[tema].md`

Se algum item falhou: corrigir ANTES de declarar concluído. Nunca reportar "feito" com item pendente.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
