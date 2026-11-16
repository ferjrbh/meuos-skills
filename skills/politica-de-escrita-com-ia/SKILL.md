---
name: politica-de-escrita-com-ia
description: "Entrevista o gestor com 6 perguntas e monta a politica de escrita com IA da empresa dele em 1 pagina, mais a mensagem de lancamento para o time e o checklist de 30 dias. Nao proibe IA: define o que e escrever bem e quem responde pelo que assina, para acabar com o AI slop no time. Usar quando o usuario disser 'criar politica de IA da empresa', 'politica de escrita com IA', 'regra de uso de IA para o time', 'como evitar workslop no meu time', 'entrevista para a politica de IA'."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Politica de escrita com IA (entrevista)

## O que esta skill faz

Conduz uma entrevista curta com o gestor e entrega a politica de escrita com IA da empresa dele: uma pagina que qualquer pessoa le em 3 minutos, com regras claras de quem responde pelo que envia, quando a IA e bem-vinda e o que nunca sai sem leitura humana. A base e a politica publica que a empresa de software Clay publicou em agosto de 2026 (clay.com/blog/ai-writing-policy), mais o filtro de 7 perguntas da skill `filtro-ai-slop`.

A politica nao proibe IA. Proibir tira o ganho real junto com a porcaria.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Combinar a entrevista

> "Vou te fazer 6 perguntas rapidas, uma por vez, e no fim te mostro a politica para aprovar. Pode responder curto."

Uma pergunta por vez, sem jargao. Se a resposta vier vaga, oferecer 2 ou 3 exemplos e deixar escolher.

### PASSO 1: As 6 perguntas

1. **Quem e onde.** Qual a empresa, quantas pessoas escrevem documentos que outros leem, e em quais canais o trabalho circula (WhatsApp, e-mail, Teams ou Slack, documentos, apresentacoes, codigo)?
2. **O que circula.** Quais documentos mais pesam na rotina (relatorio mensal, proposta, ata, apresentacao para diretoria, especificacao, resposta a cliente)? Quais mais chegam "bonitos e vazios"?
3. **Quem revisa.** Quem le e aprova cada tipo de documento? Quanto tempo isso toma hoje, mesmo que no chute?
4. **Onde a IA ajuda.** Em que o time ja usa IA e quer continuar usando (rascunho, pesquisa, revisao de portugues, traducao, codigo, resumo de reuniao)?
5. **O que e proibido.** Sao duas perguntas, fazer as duas: (a) o que nunca pode SAIR sem leitura humana (numero financeiro, contrato, resposta a cliente)? (b) o que nunca pode ser COLADO numa IA (dado pessoal de cliente, saude, RH, segredo comercial)? Existe regra de confidencialidade ou LGPD que ja vale?
6. **Tamanho por canal.** Qual o tamanho maximo aceitavel em cada canal? Sugerir o padrao: WhatsApp 5 linhas, e-mail 1 tela, documento de decisao 1 pagina + anexo.

### PASSO 2: Montar a politica (1 pagina, no tom da empresa)

```
POLITICA DE ESCRITA COM IA · <EMPRESA> · versao <data>

Por que existe: <1 frase com a dor contada na pergunta 2>

1. Voce assina cada frase. Quem envia responde por todo o conteudo. "A IA escreveu essa parte" nao e resposta.
2. Escrever e pensar. O documento e a prova de que alguem pensou no problema; o arquivo e so o recibo.
3. Quem escreve gasta mais tempo do que quem le. Um escreve, muitos leem.
4. Mais longo nao e melhor. Se o texto longo saiu de um pedido curto, mande o pedido.
5. Texto da IA que voce nao revisou so vai marcado: "sugestao da IA, nao revisada".
6. Pedido em cima, resposta primeiro: 1a linha a decisao pedida, 2a a recomendacao, o resto em anexo.
7. Antes de enviar, o filtro de 7 perguntas (abaixo). Vermelho nao sai.

Onde a IA e bem-vinda: <resposta 4>
Nunca sai sem leitura humana: <resposta 5a>
Nunca e colado numa IA: <resposta 5b> (se o gestor nao souber, sugerir: dado pessoal de cliente e qualquer dado coberto pela LGPD)
Tamanho por canal: <resposta 6>
Quem pode devolver um documento: qualquer destinatario, com a frase-padrao abaixo, sem constrangimento.

Filtro de 7 perguntas:
1. Qual decisao ou acao isto destrava?
2. Quem recebe tem contexto suficiente para agir?
3. O que ele ainda vai ter de pesquisar, conferir ou refazer?
4. Cada bloco tem funcao, ou so ocupa espaco?
5. Os numeros chegam ate a fonte original?
6. Quem leu a versao final e responde pelo erro?
7. A resposta principal aparece antes dos detalhes?

Frase-padrao de devolucao: "Antes de eu entrar no merito, me ajuda: qual decisao voce precisa de mim, e de onde vem os numeros X e Y?"

Principios 1 a 5 adaptados da politica publica da Clay (clay.com/blog/ai-writing-policy, ago-2026).
```

Mostrar ao usuario e pedir aprovacao ou ajuste antes de gerar os arquivos.

### PASSO 3: Entregar

1. O arquivo `POLITICA-ESCRITA-IA-<EMPRESA>.md` na pasta do contexto da empresa no OS do usuario. Se ele ainda nao tem um OS organizado, salvar na pasta em que a conversa esta e dizer o caminho. Se ele pedir, gerar tambem uma versao HTML de 1 pagina para imprimir.
2. A mensagem de lancamento para o time: ate 8 linhas, com o porque (a dor da pergunta 2), o que muda na segunda-feira e o aviso de que a IA continua liberada.
3. O checklist de 30 dias:
   - Semana 1: publicar a politica; mudar a ordem dos documentos (decisao primeiro).
   - Semana 2: pedido anexo; filtro de 7 perguntas onde o time envia (assinatura do e-mail interno ou mensagem fixada do grupo).
   - Semana 3: frase-padrao de devolucao combinada; skill `triagem-do-que-chega` para quem recebe muito.
   - Semana 4: medir o tempo medio de revisao e o percentual de documentos devolvidos, comparando com a linha de base da pergunta 3 (o tempo de revisao que o gestor contou). Se o tempo de revisao nao caiu, revisar a politica.

---

## Regras

- Nunca transformar em proibicao de IA. Se o gestor pedir proibicao total, registrar o pedido e explicar em 1 linha que proibir tira o ganho real (num experimento com 758 consultores do BCG, publicado por pesquisadores de Harvard, Wharton e MIT, quem usou IA nas tarefas certas terminou 25,1% mais rapido e com qualidade mais de 40% maior).
- Nao inventar dado da empresa: o que o gestor nao respondeu vira campo em branco marcado, nunca suposicao.
- O texto para o time e do gestor: mostrar e esperar o OK antes de entregar como final.

## Checklist antes de entregar

- [ ] As 6 perguntas feitas, uma por vez
- [ ] Politica cabe em 1 pagina e foi aprovada pelo usuario
- [ ] Mensagem de lancamento com ate 8 linhas
- [ ] Checklist de 30 dias entregue
- [ ] Arquivo salvo na pasta do contexto certo do OS

Se algum item falhou: corrigir ANTES de declarar concluido.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
