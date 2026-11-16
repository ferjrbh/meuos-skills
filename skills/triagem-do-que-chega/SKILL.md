---
name: triagem-do-que-chega
description: "Triagem para QUEM RECEBE um documento (PDF, apresentacao, relatorio, ata, e-mail longo, proposta, codigo) e precisa sobreviver a enxurrada de material feito com IA. Devolve em ate 8 linhas o que estao pedindo de voce, quais fatos tem fonte, o que falta para decidir e um semaforo; no vermelho, escreve a devolucao educada ao autor. Nunca reescreve o documento do outro. Usar quando o usuario disser 'triagem disso', 'o que esse documento quer de mim?', 'vale ler isso?', 'resume o que importa', 'isso e workslop?' sobre algo que recebeu, 'me ajuda a devolver isso'."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Triagem do que chega (quem recebe)

## O que esta skill faz

Quando alguem envia um documento bonito, longo e sem decisao, o trabalho que faltou cai na sua mesa: entender o objetivo, conferir os fatos, achar as fontes, decidir o que importa. Esta skill e a sua defesa. Ela le o que chegou e devolve, em poucas linhas, o que voce precisa saber para agir, ou a mensagem para devolver o documento ao autor.

Para revisar algo que VOCE vai enviar, use a skill `filtro-ai-slop`.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Entrada

Pedir, em 1 mensagem curta (pular o que o usuario ja disse):

> "Para a triagem: (1) cole o documento ou o arquivo; (2) quem mandou e qual a sua relacao com essa pessoa (chefe, colega, fornecedor, cliente)?"

### PASSO 1: Ler e classificar

Ler o documento inteiro e responder, sem enfeite:

```
SEMAFORO: 🟢 / 🟡 / 🔴
1. Pedem de voce: <decisao ou acao, com prazo se houver; ou "nao esta claro">
2. Fatos com fonte: <os 2 ou 3 que importam, com a fonte>
3. Afirmacoes sem fonte: <lista curta>
4. Contradicoes: <dentro do proprio documento, ou "nenhuma">
5. Falta para decidir: <o que voce precisaria saber e nao esta la>
6. Tempo honesto de leitura: <minutos>, e o que da para pular
```

- 🟢 **Verde:** da para decidir com o que veio.
- 🟡 **Amarelo:** da para decidir pedindo 1 ou 2 coisas objetivas ao autor.
- 🔴 **Vermelho:** parece pronto, mas o trabalho foi transferido. Nao ha pedido claro, ha contradicao ou faltam as fontes do que sustenta a conclusao.

### PASSO 2: No amarelo, o pedido curto

```
Oi, <nome>. Para eu decidir, me manda so: <item 1> e <item 2>. Obrigado.
```

### PASSO 3: No vermelho, a devolucao

Escrever a mensagem ao autor, curta e sem ironia, no canal em que o documento chegou. Ajustar o tom pela relacao informada no PASSO 0: para chefe ou cliente, mais formal e comecando pelo agradecimento; para colega ou fornecedor, direto.

```
Oi, <nome>. Antes de eu entrar no merito, me ajuda com 3 pontos:
1. Qual decisao voce precisa de mim?
2. <a contradicao ou a afirmacao sem fonte, citando o trecho>
3. <o que falta>
Com isso eu consigo responder rapido.
```

Mostrar ao usuario e esperar o OK dele antes de considerar a mensagem (do PASSO 2 ou 3) pronta para envio.

---

## Regras

- **Nunca reescrever o documento do outro.** Reescrever e aceitar a conta transferida. Resumir para o usuario, sim; consertar para o autor, nao.
- Nunca dizer "isso foi feito por IA". A devolucao fala do que falta, nao da origem.
- Fonte e a original. Materia que cita um estudo nao e fonte do estudo: marcar "de segunda mao".
- Documento de cliente fica no contexto daquele cliente no seu OS; nunca misturar com outro.

## Checklist antes de entregar

- [ ] Resposta em ate 8 linhas, no formato do PASSO 1
- [ ] Contradicoes internas conferidas
- [ ] Nenhuma reescrita do documento original
- [ ] Pedido (amarelo) ou devolucao (vermelho) mostrado ao usuario antes de enviar

Se algum item falhou: corrigir ANTES de declarar concluido.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
