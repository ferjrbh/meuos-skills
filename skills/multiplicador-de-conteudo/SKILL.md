---
name: multiplicador-de-conteudo
description: "Transforma uma ideia ou conteúdo-base (artigo, transcrição, aula, ideia solta, thread) em vários formatos prontos para publicar: post de Instagram, carrossel, legenda curta e longa, LinkedIn, blog, e-mail, roteiro de Reels, WhatsApp e X. Entrega tudo num único arquivo HTML com um card por formato e botão de copiar. Usar quando o usuário disser 'multiplica esse conteúdo', 'transforma esse texto em posts', 'faz versões disso para outras redes', 'reaproveita esse artigo', 'quebra essa ideia em vários formatos' ou 'desdobra esse conteúdo'."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Multiplicador de Conteúdo

## O que esta skill faz

Pega um conteúdo que já existe e já é bom (um artigo, a transcrição de uma aula, um áudio, uma ideia anotada) e desdobra em várias peças prontas para publicar, cada uma com a gramática do seu canal. Uma ideia boa vale dez posts: em vez de criar conteúdo novo toda semana, você aproveita melhor o que já produziu.

A entrega final é **um único arquivo HTML** que abre com dois cliques no computador ou no celular: um painel com um card por formato e um botão "Copiar" em cada card. Você abre, copia e cola na rede social. Sem instalar nada.

> **Princípio:** multiplicar não é inventar. A skill expande o que está no conteúdo-base. Se o conteúdo-base é fraco, ela avisa antes de multiplicar.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Descobrir onde o usuário trabalha

Antes de escrever, verificar se o usuário tem um OS organizado (pastas por contexto, documento mestre, `index.md`, `CLAUDE.md` ou `AGENTS.md`).

| # | Situação | O que fazer |
|---|---|---|
| 1 | Tem OS com contextos | Perguntar (ou confirmar em 1 linha, se for óbvio) de qual contexto é o conteúdo: empresa, cliente, projeto, marca pessoal. Trabalhar só dentro dessa pasta |
| 2 | Não tem OS | Seguir normalmente; salvar o HTML na pasta em que o agente foi aberto (ou onde o usuário indicar) |
| 3 | Usa o ChatGPT sem acesso a arquivos | Gerar o HTML completo num bloco de código e instruir o usuário: "copie, cole no Bloco de Notas, salve como `.html` e abra com dois cliques" |

NUNCA misturar material de um contexto com outro.

### PASSO 1: Coletar o que falta (uma mensagem só)

| # | Item | Obrigatório? | Exemplo |
|---|---|---|---|
| 1 | Conteúdo-base | Sim | Texto colado, arquivo, link da transcrição |
| 2 | Objetivo | Sim | Ser lembrado, gerar conversa, ensinar, vender, captar contato |
| 3 | Canais | Não (há padrão, ver PASSO 4) | Instagram, LinkedIn, e-mail, WhatsApp |
| 4 | Público | Se diferente do habitual | Donos de clínica, gestores de loja, pais de alunos |
| 5 | Restrições | Se houver | "sem emoji", "sem falar de preço", "tom mais formal" |

Pular o que o usuário já disse. Se faltar o conteúdo-base ou o objetivo, perguntar antes de gerar.

### PASSO 2: Ler a marca (tom de voz e visual)

Procurar no contexto do OS, nesta ordem: guia de marca, tom de voz, documento mestre (arquivos com nomes como `marca`, `brand`, `tom-de-voz`, `identidade`, `estilo`).

| # | Encontrou | O que aplicar |
|---|---|---|
| 1 | Tom de voz | Vocabulário, formalidade, palavras proibidas, uso de emoji |
| 2 | Cores e fonte | Cores no CSS do HTML (variáveis `--cor-*`) e a fonte no Google Fonts |
| 3 | Nada | Perguntar **uma vez**: "Qual tom você quer? (1) próximo e leve, (2) direto e profissional, (3) inspirador, (4) técnico e didático". Visual: paleta neutra do esqueleto abaixo |

Não inventar cor, slogan nem promessa da marca.

### PASSO 3: Extrair a ideia-mãe e os ângulos

1. Condensar o conteúdo-base em **uma frase**: a ideia-mãe. Ela ancora todos os formatos.
2. Escolher de 3 a 5 ângulos que o conteúdo sustenta de verdade:

| # | Ângulo | Exemplo (escritório de contabilidade fictício) |
|---|---|---|
| 1 | Problema | "Você paga multa de atraso sem saber por quê?" |
| 2 | Solução | "Três passos para nunca mais perder o prazo do imposto" |
| 3 | Prova | "Um cliente nosso reduziu a zero as multas em seis meses" (só se o conteúdo-base trouxer esse caso) |
| 4 | Contraste | "Planilha ou sistema: o que funciona para empresa pequena" |
| 5 | Bastidor | "Por que conferimos tudo duas vezes antes de enviar" |
| 6 | Lista | "Sete documentos que você precisa guardar" |

Se o conteúdo-base não tem número, caso ou depoimento, **não criar**. Ângulo de prova sem prova sai da lista.

### PASSO 4: Escolher os formatos (menos é mais)

Se o usuário não escolheu os canais, propor 3 a 4 pelo objetivo e confirmar em 1 linha:

| # | Objetivo | Formatos padrão |
|---|---|---|
| 1 | Ser lembrado | Carrossel + roteiro de Reels + legenda curta |
| 2 | Gerar conversa | Post de Instagram + LinkedIn + X |
| 3 | Vender | E-mail + WhatsApp + legenda longa |
| 4 | Autoridade | LinkedIn + blog + carrossel |
| 5 | Tráfego para o site | Blog + legenda curta com chamada para o link |

Se o usuário pedir "todos", gerar os dez da tabela do PASSO 5.

### PASSO 5: Escrever cada peça com a regra do canal

| # | Formato | Regra |
|---|---|---|
| 1 | Post de Instagram | Gancho na 1ª linha + dor (2-3 linhas) + solução (3-5 linhas) + chamada final. Até 2.200 caracteres. 5 a 10 hashtags (nicho + amplas) |
| 2 | Carrossel | 7 a 10 slides. Slide 1 = gancho; um assunto por slide, até ~25 palavras; último = chamada para ação. Indicar texto de cada slide e sugestão de imagem |
| 3 | Legenda curta | Até 300 caracteres. Gancho + chamada |
| 4 | Legenda longa | 1.000 a 2.000 caracteres, storytelling, parágrafos curtos |
| 5 | LinkedIn | 1.300 a 1.600 caracteres. Gancho nas 2 primeiras linhas (antes do "ver mais"), uma ideia por parágrafo, pergunta ou convite no fim. Hashtags: 3 no máximo |
| 6 | Blog | Título com a palavra-chave, intro curta, 3 a 5 subtítulos, conclusão com chamada. 600 a 1.200 palavras. Sugerir título SEO e meta descrição (até 155 caracteres) |
| 7 | E-mail | Assunto de 30 a 50 caracteres, pré-cabeçalho de 80 a 100, corpo de 300 a 600 palavras, uma ideia, um botão ou link |
| 8 | Roteiro de Reels | 30 a 60 s: gancho (0-3 s), desenvolvimento, chamada (últimos 5-10 s). Cena por cena: fala + texto na tela + sugestão de imagem |
| 9 | WhatsApp | 200 a 400 caracteres, no máximo 1 emoji, termina em pergunta ou link |
| 10 | X | 1 post de até 280 caracteres OU fio de 4 a 8 posts, cada um com até 280 caracteres |

Regras de escrita para todas as peças:
- Nunca copiar o mesmo texto de um canal para outro: adaptar tom, tamanho e estrutura.
- Preservar a ideia-mãe em todas.
- Contar os caracteres antes de entregar e anotar no card (ex.: "1.412 caracteres").
- Nada de número, depoimento ou resultado que não esteja no conteúdo-base.

### PASSO 6: Montar o arquivo HTML

**Nome:** `AAAA-MM-DD-conteudo-{tema}.html` (data de hoje, tema em minúsculas, sem acento, com hífen). Ex.: `2026-11-14-conteudo-prazo-de-impostos.html`.

**Onde salvar:**

| # | Situação | Pasta |
|---|---|---|
| 1 | O contexto tem pasta `docs/` | `{contexto}/docs/` |
| 2 | O contexto não tem `docs/` | Raiz do contexto |
| 3 | Sem OS | Pasta atual ou a que o usuário indicar |

Se já existir um arquivo com o mesmo nome, acrescentar `-v2`, `-v3` (nunca sobrescrever).

**Regras do HTML:**
- Um arquivo só, autocontido: CSS e JS dentro do próprio arquivo. A única dependência externa permitida é o Google Fonts (opcional; sem internet, cai na fonte do sistema).
- Abre com dois cliques (sem servidor).
- Responsivo: uma coluna no celular, duas ou três no computador; sem rolagem horizontal.
- Um card por formato, com: nome do formato, contagem de caracteres, o texto pronto e o botão "Copiar".
- O texto copiado deve sair limpo, com as quebras de linha, sem HTML.
- No topo: a ideia-mãe, o objetivo e a lista de formatos.
- Escapar `<`, `>` e `&` do texto ao colocar dentro do HTML.

**Esqueleto mínimo (reproduzir e preencher):**

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Conteúdo: {tema}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --cor-fundo: #f6f6f4;      /* trocar pelas cores da marca, se houver */
    --cor-card: #ffffff;
    --cor-texto: #1f2328;
    --cor-suave: #6b7280;
    --cor-destaque: #2f5bea;
    --raio: 12px;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Inter', system-ui, sans-serif; background: var(--cor-fundo); color: var(--cor-texto); line-height: 1.5; padding: 16px; }
  header { max-width: 1200px; margin: 0 auto 24px; }
  header h1 { font-size: 1.5rem; margin-bottom: 8px; }
  header p { color: var(--cor-suave); }
  .grade { max-width: 1200px; margin: 0 auto; display: grid; gap: 16px; grid-template-columns: 1fr; }
  @media (min-width: 720px) { .grade { grid-template-columns: repeat(2, 1fr); } }
  @media (min-width: 1100px) { .grade { grid-template-columns: repeat(3, 1fr); } }
  .card { background: var(--cor-card); border-radius: var(--raio); padding: 16px; box-shadow: 0 1px 3px rgba(0,0,0,.08); display: flex; flex-direction: column; min-width: 0; }
  .card-topo { display: flex; justify-content: space-between; align-items: center; gap: 8px; margin-bottom: 12px; }
  .card h2 { font-size: 1rem; }
  .contagem { font-size: .8rem; color: var(--cor-suave); }
  .texto { white-space: pre-wrap; word-wrap: break-word; font-size: .95rem; flex: 1; margin-bottom: 12px; }
  button.copiar { min-height: 44px; border: 0; border-radius: 8px; background: var(--cor-destaque); color: #fff; font-weight: 600; font-size: 1rem; cursor: pointer; }
  button.copiar:focus-visible { outline: 3px solid var(--cor-texto); outline-offset: 2px; }
  button.copiar.ok { background: #1a7f37; }
</style>
</head>
<body>
<header>
  <h1>{Ideia-mãe em uma frase}</h1>
  <p>Objetivo: {objetivo} · Formatos: {lista} · Gerado em {DD/MM/AAAA}</p>
</header>
<main class="grade">
  <article class="card">
    <div class="card-topo"><h2>LinkedIn</h2><span class="contagem">1.412 caracteres</span></div>
    <div class="texto">{texto pronto, com quebras de linha}</div>
    <button class="copiar" type="button">Copiar</button>
  </article>
  <!-- repetir um <article class="card"> por formato -->
</main>
<script>
  function copiarTexto(texto) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(texto);
    }
    return new Promise(function (ok, erro) {
      var area = document.createElement('textarea');
      area.value = texto;
      area.setAttribute('readonly', '');
      area.style.position = 'fixed';
      area.style.opacity = '0';
      document.body.appendChild(area);
      area.select();
      try { document.execCommand('copy') ? ok() : erro(); } catch (e) { erro(e); }
      document.body.removeChild(area);
    });
  }
  document.querySelectorAll('button.copiar').forEach(function (botao) {
    botao.addEventListener('click', function () {
      var texto = botao.closest('.card').querySelector('.texto').innerText;
      copiarTexto(texto).then(function () {
        botao.textContent = 'Copiado!';
        botao.classList.add('ok');
        setTimeout(function () { botao.textContent = 'Copiar'; botao.classList.remove('ok'); }, 2000);
      }).catch(function () {
        botao.textContent = 'Selecione e copie manualmente';
      });
    });
  });
</script>
</body>
</html>
```

No carrossel e no roteiro de Reels, o texto do card traz a estrutura completa (Slide 1, Slide 2... ou Cena 1, Cena 2...), para que o "Copiar" leve tudo de uma vez.

### PASSO 7: Conferir e entregar

1. Abrir o HTML (no Claude Code, com o navegador ou Playwright, se disponível; senão, pedir ao usuário que abra) e verificar: cards aparecem, o "Copiar" funciona, nada estoura a largura no celular. Se o navegador do agente bloquear arquivo local (`file://`), pedir ao usuário que abra o arquivo e conte o que vê (quantos cards aparecem, se o "Copiar" funcionou, se algo ficou cortado no celular).
2. Entregar ao usuário: caminho completo do arquivo, ideia-mãe em uma linha e a lista de formatos gerados.
3. Se o OS do usuário tiver `index.md` no contexto, oferecer acrescentar a linha do arquivo novo.

---

## Regras desta skill

- **Multiplica, não inventa.** Nenhum número, caso, depoimento ou promessa que não esteja no conteúdo-base ou não tenha vindo do usuário.
- **Cada canal tem sua gramática.** Texto idêntico em dois canais é erro.
- **Limite de caracteres é real.** Conferir e mostrar a contagem em cada card.
- **Marca do usuário vence.** Tom e cores do guia de marca do OS têm prioridade sobre a paleta neutra.
- **Menos formatos bem feitos.** Padrão de 3 a 4 formatos; dez só quando pedido.
- **Um contexto por vez.** Nunca puxar exemplo ou dado de outro contexto do OS.
- **Conteúdo-base fraco se avisa.** Se não há ideia clara, dizer isso e sugerir o que falta antes de gerar.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Contexto confirmado e arquivo salvo dentro dele (em `docs/` se existir)
- [ ] Tom de voz e cores lidos do OS, ou tom perguntado uma única vez
- [ ] Ideia-mãe escrita em uma frase no topo do HTML
- [ ] Cada formato respeita o limite de caracteres e mostra a contagem no card
- [ ] Nenhum texto repetido igual entre canais
- [ ] Zero número, caso ou depoimento inventado
- [ ] HTML único, abre com dois cliques, sem dependência além do Google Fonts
- [ ] Botão "Copiar" testado em pelo menos um card, com alternativa quando a área de transferência falha
- [ ] Sem rolagem horizontal na largura de celular (375 px)
- [ ] Nome no padrão `AAAA-MM-DD-conteudo-{tema}.html`, sem sobrescrever versão anterior
- [ ] Caminho completo do arquivo informado ao usuário

Se algum item falhou: corrigir ANTES de declarar concluído. Nunca reportar "feito" com item pendente.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
