---
name: filtro-ai-slop
description: "Filtro anti AI slop para QUEM ENVIA: antes de mandar um documento, slide, relatorio, ata, e-mail ou codigo feito com ajuda de IA, roda 7 perguntas e 4 testes, aponta as frases que voce nao conseguiria defender e devolve semaforo verde, amarelo ou vermelho com o que ajustar. Nao detecta 'se foi IA': mede quanto trabalho o documento transfere para quem recebe. Usar quando o usuario disser 'passa no filtro', 'filtro anti slop', 'isso esta pronto para mandar?', 'revisa antes de eu enviar', 'isso e workslop?', 'confere se nao estou mandando porcaria'."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Filtro anti AI slop (quem envia)

## O que esta skill faz

A IA deixou barato produzir texto, slide, relatorio e codigo. Nao deixou barato pensar. Quando alguem envia algo longo, polido e sem decisao, sem fonte e sem dono, o trabalho nao some: ele muda de mesa, e quem recebe tem de interpretar, conferir e refazer. Pesquisadores chamaram isso de **workslop**: conteudo de IA que parece bom, mas nao tem substancia.

Esta skill roda ANTES de voce apertar enviar. O criterio nao e de onde veio o texto, e **quanto ele cobra de quem recebe**. Se o destinatario precisa terminar o seu raciocinio, voce nao entregou trabalho: entregou trabalho para ele.

Para quem RECEBE um documento, use a skill `triagem-do-que-chega`. Para criar a regra da empresa, use `politica-de-escrita-com-ia`.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Entrada

Pedir, em 1 mensagem curta (pular o que o usuario ja disse):

> "Para passar no filtro: (1) cole o documento ou o arquivo; (2) para quem vai e por qual canal (WhatsApp, e-mail, documento de decisao, apresentacao, codigo)? (3) se tiver, cole tambem o pedido ou prompt que gerou o documento."

Sem o pedido original, o teste 9 fica como "nao medido".

### PASSO 1: As 7 perguntas

| # | Pergunta | Falha quando |
|---|---|---|
| 1 | Qual decisao ou acao isto destrava? | Nao da para dizer em uma frase |
| 2 | Quem recebe tem contexto suficiente para agir? | Depende de conversa que ele nao viu, sigla sem explicacao, anexo faltando |
| 3 | O que ele ainda vai ter de pesquisar, conferir, resumir ou refazer? | A lista tem mais de 2 itens |
| 4 | Cada bloco tem funcao, ou so ocupa espaco? | Ha paragrafo que, cortado, nao faz falta |
| 5 | Os numeros e afirmacoes chegam a fonte original? | Numero sem fonte, fonte de segunda mao, numeros que se contradizem no proprio documento |
| 6 | Quem leu a versao final e responde pelo erro? | Ninguem nomeado, ou "a IA fez essa parte" |
| 7 | A resposta principal aparece antes dos detalhes? | A decisao pedida esta no fim, ou nao esta |

### PASSO 2: Os 4 testes extras

Inspirados na politica publica de escrita com IA da empresa Clay (agosto de 2026):

| # | Teste | Como medir |
|---|---|---|
| 8 | **Assinatura:** voce sustenta cada frase? | Listar as frases que o autor nao saberia defender numa pergunta do revisor: afirmacao generica, numero sem origem, conclusao que nao decorre do texto. Cada uma: cortar ou reescrever com as palavras do autor |
| 9 | **Pedido curto, texto longo** | Se o documento tem mais de 5 vezes o tamanho do pedido, sugerir mandar o pedido (ou um resumo de 5 linhas) no lugar do documento |
| 10 | **Citacao de IA marcada** | Perguntar ao usuario: "tem trecho aqui que voce nao revisou?". Se tiver, ele sai do documento ou vai marcado: "sugestao da IA, nao revisada" |
| 11 | **Teto pelo canal** | WhatsApp ate 5 linhas · e-mail ate 1 tela · documento de decisao 1 pagina + anexo · apresentacao com 1 mensagem por lamina e numero com fonte no rodape |

**Contradicao interna** (o mesmo indicador com dois valores no mesmo documento) e vermelho automatico.

### PASSO 3: Entregar o resultado (sempre neste formato, curto)

```
SEMAFORO: 🟢 / 🟡 / 🔴
Decisao que destrava: <1 frase, ou "nao encontrei">
Falhou em: <numeros das perguntas e testes>
Corrigir antes de enviar:
1. <acao objetiva>
2. ...
Frases que voce nao sustentaria: <lista curta, com o trecho>
```

Regra da cor (aplicar nesta ordem):

- 🔴 **Vermelho:** falhou a pergunta 1 (nenhuma decisao) OU a 6 (ninguem responde) OU ha contradicao interna OU sao necessarias mais de 3 correcoes. Parece pronto, mas transfere o trabalho. Nao sai.
- 🟡 **Amarelo:** ate 3 correcoes objetivas (fonte, ordem, tamanho, contexto) e nenhuma falha que da vermelho.
- 🟢 **Verde:** nenhuma correcao necessaria. Pode enviar.

Se o documento esta no formato errado para o canal (por exemplo, um artigo enviado como documento de decisao), a primeira correcao e trocar o formato: 1 pagina com a decisao, o resto em anexo.

---

## Regras

- Nunca reescrever o documento inteiro por conta propria. Apontar e, se o usuario pedir, reescrever so os trechos apontados: reescrita de quem nao tem a ideia completa perde sentido.
- Nunca dizer "isto foi escrito por IA". O filtro mede custo transferido, nao origem.
- Nunca inventar fonte para numero sem fonte: marcar "sem fonte".

## Checklist antes de entregar

- [ ] As 7 perguntas e os 4 testes foram aplicados
- [ ] Contradicao interna conferida (mesmo indicador, valores diferentes)
- [ ] Semaforo justificado pelos itens que falharam
- [ ] Nenhuma reescrita alem do que o usuario pediu

Se algum item falhou: corrigir ANTES de declarar concluido.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
