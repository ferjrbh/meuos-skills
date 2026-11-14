---
name: criador-wireframe
description: "Desenha o esboço de uma tela (wireframe) em HTML autocontido antes de construir: faz uma entrevista curta, lê a marca do seu OS (cores, fonte, logo) ou usa uma paleta neutra, gera a tela responsiva para celular e computador com os estados vazio, carregando e erro, salva com versão (v1, v2...) e entrega o prompt para levar ao Lovable ou ao Claude Code. Usar quando o usuário disser 'cria um wireframe', 'faz um esboço da tela', 'como seria a tela de X', 'rascunho da interface', 'mockup da página' ou 'desenha essa tela antes de construir'."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Criador de Wireframe

## O que esta skill faz

Ajustar uma tela depois que ela está construída custa caro: cada mudança é um novo pedido à ferramenta, com risco de quebrar o que já funcionava. Ajustar um esboço custa quase nada. Esta skill desenha a tela antes, num arquivo HTML que abre com dois cliques no computador ou no celular, para você ver, mostrar para quem decide, pedir ajustes e só então construir.

O esboço respeita a sua marca (se ela estiver no seu OS), funciona no celular e no computador, mostra os estados que costumam ser esquecidos (lista vazia, carregando, erro) e vem com o prompt pronto para a ferramenta de construção.

> **Princípio:** desenhar primeiro, construir depois. E wireframe que ignora a marca e a tela que já existe é retrabalho garantido.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Localizar o projeto e a marca

| # | Situação | O que fazer |
|---|---|---|
| 1 | Tem OS com contextos | Confirmar o contexto do produto. Procurar nele, nesta ordem: guia de marca (arquivos com `marca`, `brand`, `identidade`, `estilo`), documento mestre, spec da tela (`spec-*.md`), wireframes anteriores (`wireframe-*.html`) |
| 2 | Já existe app ou site do produto | Ler a tela atual ou o código da página para copiar o padrão: cabeçalho, cards, botões, textos reais |
| 3 | Sem OS e sem marca | Usar a paleta neutra do esqueleto abaixo e avisar o usuário em 1 linha |

Da marca, aproveitar só o que está escrito: cores em hexadecimal, fontes, logo (caminho do arquivo), tom dos textos. **Não inventar cor nem slogan.** Se o guia não define algo (ex.: cor de erro), usar o neutro e dizer.

NUNCA usar marca, texto ou dado de outro contexto do OS.

### PASSO 1: Entrevista curta (uma mensagem)

Perguntar só o que falta:

| # | Pergunta | Exemplo de resposta |
|---|---|---|
| 1 | O que esta tela faz? Qual é a ação principal? | "Mostrar os pedidos do dia e marcar como entregue" |
| 2 | Quem usa e onde (celular, computador, os dois)? | "O entregador, no celular, na rua" |
| 3 | Que informação aparece? | "Nome do cliente, endereço, horário, status" |
| 4 | Que ações a pessoa pode fazer? | "Marcar entregue, ligar para o cliente, ver no mapa" |
| 5 | É tela nova ou mudança de uma que existe? | "Mudança da lista atual" |

Se o pedido for vago ("faz a tela de perfil"), perguntar: "Quer a página inteira ou só uma seção?". Uma pergunta bem feita evita três versões erradas.

### PASSO 2: Esqueleto em texto (validação rápida)

Antes do HTML, mostrar a estrutura em blocos e pedir OK. Leva um minuto e evita desenhar a coisa errada:

```text
Tela: Pedidos do dia (celular)
┌──────────────────────────────┐
│ [CABEÇALHO] Logo · Sair      │
├──────────────────────────────┤
│ Hoje, 12 pedidos · 4 feitos  │
│ [Filtro: Todos | Pendentes]  │
├──────────────────────────────┤
│ [CARD] Cliente · Endereço    │
│        14h-15h · Pendente    │
│        [Marcar entregue]     │
│ [CARD] ...                   │
├──────────────────────────────┤
│ Vazio: "Nenhum pedido hoje"  │
└──────────────────────────────┘
```

Se o usuário pedir direto o HTML, pular esta etapa.

### PASSO 3: Planejar o visual em 4 linhas

Antes de escrever o HTML, decidir e anotar:
1. **Paleta:** 4 a 6 cores com nome e hex (fundo, texto, texto suave, destaque, erro, sucesso), vindas da marca ou neutras.
2. **Tipografia:** fonte dos títulos e do texto.
3. **Layout:** uma frase (ex.: "lista em cards, ação principal fixa embaixo no celular").
4. **Uma ação principal por tela**, com destaque; o resto recua.

Evitar o visual genérico de IA: fundo creme com serifa e acento terracota, fundo quase preto com uma cor neon, ou três cards iguais lado a lado como seção de "vantagens" sem motivo. Se a marca define o visual, a marca vence.

### PASSO 4: Gerar o HTML

**Regras:**
- Arquivo único, autocontido: CSS dentro do `<style>`, JS mínimo dentro do `<script>`. Única dependência externa permitida: Google Fonts (sem internet, cai na fonte do sistema). Nada de Tailwind ou Bootstrap por CDN.
- Abre com dois cliques, sem servidor.
- Celular primeiro (375 px) e ajuste para computador com `@media`.
- Selo "WIREFRAME" visível, para ninguém confundir com a tela final.
- Texto plausível do produto, nunca "Lorem ipsum". Nomes de pessoas fictícios e variados; nada de dado real de cliente.
- Imagem vira caixa cinza tracejada com a descrição (`[Foto do produto]`).
- Componente que ainda não existe no produto ganha a etiqueta "NOVO".
- Quando fizer sentido, mostrar os estados **vazio, carregando e erro** (botões de alternância no topo do wireframe, ou blocos lado a lado identificados).

**Esqueleto mínimo (adaptar):**

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Wireframe: {tela} · v1</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --cor-fundo: #f7f7f5;     /* trocar pelas cores da marca, se houver */
    --cor-card: #ffffff;
    --cor-texto: #1f2328;
    --cor-suave: #5f6670;
    --cor-destaque: #2f5bea;
    --cor-erro: #b42318;
    --cor-sucesso: #1a7f37;
    --raio: 10px;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Inter', system-ui, sans-serif; background: var(--cor-fundo); color: var(--cor-texto); line-height: 1.5; }
  /* selo em fluxo normal, acima da barra de estados: nunca cobre os botões Vazio/Carregando/Erro no celular */
  .selo { display: block; background: #000; color: #fff; font-size: 11px; padding: 6px 16px; text-align: right; }
  .estados { display: flex; gap: 8px; flex-wrap: wrap; padding: 12px 16px; background: #e9e9e6; font-size: 14px; }
  .estados button { min-height: 44px; padding: 0 14px; border: 1px solid #bbb; border-radius: 8px; background: #fff; cursor: pointer; }
  .estados button[aria-pressed="true"] { background: var(--cor-texto); color: #fff; }
  header { display: flex; justify-content: space-between; align-items: center; padding: 16px; background: var(--cor-card); }
  main { max-width: 960px; margin: 0 auto; padding: 16px; }
  .card { background: var(--cor-card); border-radius: var(--raio); padding: 16px; margin-bottom: 12px; box-shadow: 0 1px 3px rgba(0,0,0,.08); }
  .btn-principal { display: block; width: 100%; min-height: 48px; border: 0; border-radius: 8px; background: var(--cor-destaque); color: #fff; font-size: 1rem; font-weight: 600; cursor: pointer; }
  .btn-principal:focus-visible, .estados button:focus-visible { outline: 3px solid var(--cor-texto); outline-offset: 2px; }
  .img-placeholder { background: #eee; border: 2px dashed #bbb; color: #666; display: flex; align-items: center; justify-content: center; text-align: center; min-height: 140px; padding: 16px; border-radius: var(--raio); }
  .novo { font-size: 11px; background: #fff3cd; color: #7a5a00; padding: 2px 6px; border-radius: 4px; }
  .estado { display: none; }
  .estado.ativo { display: block; }
  .vazio, .erro { text-align: center; padding: 32px 16px; }
  .erro { color: var(--cor-erro); }
  @media (min-width: 768px) {
    .btn-principal { width: auto; padding: 0 24px; }
    .lista { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
  }
</style>
</head>
<body>
<div class="selo">WIREFRAME · {tela} · v1 · {DD/MM/AAAA}</div>
<nav class="estados" aria-label="Ver estados da tela">
  <button type="button" data-estado="cheio" aria-pressed="true">Com dados</button>
  <button type="button" data-estado="vazio" aria-pressed="false">Vazio</button>
  <button type="button" data-estado="carregando" aria-pressed="false">Carregando</button>
  <button type="button" data-estado="erro" aria-pressed="false">Erro</button>
</nav>
<header><strong>{Logo}</strong><span>{menu}</span></header>
<main>
  <h1>{Título da tela}</h1>
  <section class="estado ativo" data-estado="cheio">
    <div class="lista">
      <article class="card"><!-- conteúdo plausível --></article>
    </div>
    <button class="btn-principal" type="button">{Ação principal}</button>
  </section>
  <section class="estado vazio" data-estado="vazio"><p>{Mensagem que convida à ação}</p></section>
  <section class="estado" data-estado="carregando"><p>Carregando...</p></section>
  <section class="estado erro" data-estado="erro"><p>{O que houve e como resolver}</p></section>
</main>
<script>
  document.querySelectorAll('.estados button').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('.estados button').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      document.querySelectorAll('section.estado').forEach(function (s) { s.classList.toggle('ativo', s.dataset.estado === b.dataset.estado); });
    });
  });
</script>
</body>
</html>
```

**Nome e versão:** `wireframe-{tela}-v1.html` (tela em minúsculas, sem acento, com hífen). Cada rodada de ajustes vira `v2`, `v3`; **nunca sobrescrever** a versão anterior, porque o histórico mostra o que foi decidido.

**Onde salvar:** pasta do contexto do produto (em `docs/` se existir). Sem OS: pasta atual. No ChatGPT sem acesso a arquivos: entregar o HTML num bloco de código e explicar: "cole no Bloco de Notas, salve como `.html` e abra com dois cliques".

### PASSO 5: Conferir a qualidade antes de entregar

Se o agente tiver navegador (Playwright MCP ou similar), abrir o arquivo em 375 px e 1440 px e olhar. Senão, revisar o código item a item e pedir ao usuário que abra no celular. Se o navegador do agente bloquear arquivo local (`file://`), pedir ao usuário que abra o arquivo e conte o que vê (o selo e os botões de estado aparecem inteiros? algo ficou cortado ou sobreposto no celular?).

| # | Item | Critério |
|---|---|---|
| 1 | Rolagem horizontal | Nenhuma em 375 px |
| 2 | Área de toque | Botões e links com pelo menos 44 px de altura |
| 3 | Contraste | Texto legível sobre o fundo (padrão WCAG AA); nada de botão claro com texto claro |
| 4 | Ação principal | Uma só por tela, a mais destacada, ao alcance do polegar no celular |
| 5 | Estados | Vazio convida à ação; carregando mostra que algo acontece; erro diz o que houve e como resolver |
| 6 | Rótulos | Todo campo tem rótulo visível, não só texto de exemplo |
| 7 | Ação perigosa | Excluir ou cancelar pequeno, longe da ação principal, com confirmação |
| 8 | Padrões conhecidos | Logo leva ao início, menu e conta onde a pessoa espera |
| 9 | Fim do fluxo | Sucesso tem confirmação clara, não termina em tela em branco |
| 10 | Texto | Sem "Lorem ipsum", sem erro de português, botões dizem o que fazem ("Salvar pedido", não "OK") |
| 11 | Marca | Cores e fontes batem com o guia de marca (quando existe) |
| 12 | Teclado | Foco visível ao navegar com Tab |

Item reprovado se corrige antes de entregar.

### PASSO 6: Entregar e iterar

1. Informar o caminho completo do arquivo e pedir: "Abra no celular e no computador e me diga o que mudar."
2. Ajustes pedidos geram a próxima versão (`v2`), com uma linha no topo do arquivo dizendo o que mudou.
3. Quando o usuário aprovar, oferecer o prompt para a ferramenta de construção:

```text
Construa esta tela seguindo o wireframe aprovado (arquivo {wireframe-{tela}-vN.html}, anexado).

Objetivo da tela: {1 frase}
Quem usa: {perfil}, principalmente no {celular/computador}
Informações exibidas: {lista}
Ação principal: {ação}; ações secundárias: {lista}
Estados obrigatórios: vazio ("{texto}"), carregando, erro ("{texto}") e sucesso ("{texto}")
Visual: cores {hex}, fonte {fonte}; manter o padrão das outras telas do app
Celular primeiro: funciona em 375 px, botões com pelo menos 44 px, sem rolagem horizontal
Componentes marcados como NOVO não existem ainda: crie-os
Não mude outras telas.
```

No Lovable, anexar o HTML ou uma captura de tela junto com o prompt. No Claude Code ou Cursor, informar o caminho do arquivo e pedir que leia o wireframe antes de codar.

4. Se o OS do usuário tiver `index.md` no contexto, oferecer registrar o wireframe aprovado.

---

## Regras desta skill

- **Ler antes de desenhar.** Marca, spec e tela atual do produto vêm antes do primeiro traço.
- **Marca do usuário vence.** Paleta neutra só quando não há guia de marca.
- **Esboço, não tela final.** Selo "WIREFRAME" sempre visível.
- **HTML único e autocontido.** Abre com dois cliques; só Google Fonts como dependência.
- **Celular e computador.** Toda tela funciona nos dois.
- **Estados não se esquecem.** Vazio, carregando e erro aparecem quando a tela tem dados.
- **Versão nova, arquivo novo.** Nunca sobrescrever a versão anterior.
- **Zero invenção.** Sem cor, slogan, número ou componente inventado como se existisse; o que é novo leva a etiqueta "NOVO".
- **Sem dado real.** Exemplos com nomes e números fictícios.
- **Wireframe não é código de produção.** Construir a tela é o passo seguinte, com aprovação do usuário.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Contexto confirmado; marca, spec e tela atual lidos (ou ausência informada)
- [ ] Entrevista cobriu objetivo, usuário, dispositivo, informações e ações
- [ ] Esqueleto em texto aprovado (ou usuário pediu direto o HTML)
- [ ] HTML único, abre com dois cliques, só Google Fonts de dependência
- [ ] Selo "WIREFRAME" com tela, versão e data
- [ ] Funciona em 375 px sem rolagem horizontal e em 1440 px
- [ ] Botões com pelo menos 44 px; contraste legível; foco visível
- [ ] Uma ação principal por tela
- [ ] Estados vazio, carregando e erro presentes quando fazem sentido
- [ ] Texto plausível, sem Lorem ipsum, sem dado real
- [ ] Salvo como `wireframe-{tela}-vN.html` sem sobrescrever versão anterior
- [ ] Caminho completo informado e prompt de construção oferecido após aprovação

Se algum item falhou: corrigir ANTES de declarar concluído. Nunca reportar "feito" com item pendente.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
