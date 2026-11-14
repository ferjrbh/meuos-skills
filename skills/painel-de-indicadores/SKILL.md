---
name: painel-de-indicadores
description: "Transforma planilha (xlsx ou csv) ou números colados em um painel visual de indicadores, em um único arquivo HTML autocontido com a marca do usuário: entende a pergunta de negócio e o público, inventaria a base antes de calcular, calcula todo número por código e mostra de onde veio cada um, escolhe de 4 a 8 indicadores, usa gráficos simples, destaca o que importa e diz o que fazer com isso. Abre no celular e imprime em PDF. Usar quando o usuário disser 'faz um painel dessa planilha', 'transforma esses números em dashboard', 'quero um relatório visual pra diretoria', 'monta os indicadores do mês', 'painel de vendas', ou enviar uma planilha pedindo visualização."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Painel de Indicadores

## O que esta skill faz

Pega a planilha que o gestor já tem (vendas, atendimento, financeiro, estoque, produção) e entrega um painel de uma tela: de 4 a 8 números que respondem a uma pergunta de negócio, gráficos simples, os destaques do período e o que fazer com isso. Tudo em **um único arquivo HTML** que abre no navegador, funciona no celular, imprime em PDF com Ctrl+P e pode ser enviado por e-mail ou WhatsApp.

O que diferencia de "um gráfico bonito": nenhum número é calculado de cabeça. A base é contada e conferida antes, cada indicador é calculado por código e o painel mostra, no rodapé, de qual coluna e qual conta saiu cada número.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Pergunta de negócio, público e marca

Perguntar em 1 mensagem curta (pular o que o usuário já disse):

> "Antes do painel: (1) de qual empresa ou contexto do seu OS são esses dados? (2) qual pergunta o painel precisa responder (ex.: 'estamos vendendo mais ou menos que no mês passado, e por quê')? (3) quem vai ver: diretoria, cliente ou equipe? (4) qual o período?"

| # | Resposta | O que muda |
|---|---|---|
| 1 | Contexto | Com OS no padrão MeuOS: ler o documento mestre daquele contexto para pegar definições (o que conta como venda, como cliente ativo), metas e a identidade visual (cores, fonte, logo). Nunca misturar dados de contextos diferentes |
| 2 | Pergunta | Escolhe os indicadores. Indicador que não ajuda a responder a pergunta fica de fora |
| 3 | Público | Diretoria: poucos números, tendência e comparação com meta. Cliente: sem dado interno nem custo. Equipe: detalhe operacional |
| 4 | Período | Define o recorte e a comparação (mês anterior, mesmo mês do ano anterior, meta) |

**Marca:** se o OS tiver guia de marca, usar cores, fonte e logo de lá. Se não tiver, perguntar: "quer usar as cores e o logo da empresa? Me passe 2 cores (código ou print) e o arquivo do logo; se preferir, uso um padrão neutro".

### PASSO 1: Inventário da base (antes de qualquer conta)

Ler o arquivo INTEIRO por código e reportar ao usuário:

| # | Item | O que dizer |
|---|---|---|
| 1 | Tamanho | Nº de linhas e colunas de cada aba ou arquivo |
| 2 | Colunas | Nome e tipo provável (data, número, texto) |
| 3 | Datas | Data mínima e máxima; meses sem nenhum registro |
| 4 | Duplicadas | Linhas repetidas por inteiro e chaves repetidas (ex.: mesmo nº de pedido) |
| 5 | Vazios | Quantas células vazias nas colunas que vão ser usadas |
| 6 | Estranhos | Valores negativos, zerados, datas no futuro, textos em coluna de número |
| 7 | Linhas vazias e duplicadas | Dizer explicitamente quantas linhas inteiramente vazias e quantas duplicadas foram encontradas, e o que foi feito com cada grupo. Leitores de CSV pulam linha vazia em silêncio: contar as linhas do arquivo bruto e comparar com as que o leitor devolveu |

Perguntar como tratar o que apareceu (ex.: "há 12 pedidos duplicados: removo ou são parcelas?"). **Não limpar dado sem confirmar.** Registrar cada decisão de tratamento para o rodapé do painel.

Se os números vierem colados no chat, montar a tabela, mostrar ao usuário e pedir confirmação antes de seguir.

### PASSO 2: Escolher de 4 a 8 indicadores

Propor a lista, cada um com definição e fórmula, e pedir aprovação:

| # | Indicador | Definição | Fórmula | Colunas usadas |
|---|---|---|---|---|
| 1 | Faturamento do mês | Soma das vendas faturadas no período | soma(valor) onde status = faturado | data, valor, status |

Comparação só com referência que existe na base ou que o usuário informou (meta, mês anterior). Sem meta informada, não inventar meta.

### PASSO 3: Calcular tudo por código

- Usar Python (biblioteca padrão: `csv`, `json`; para .xlsx, `openpyxl` se já estiver instalado) ou JavaScript. Não instalar nada sem avisar o usuário.
- Em script Python, a primeira linha depois dos imports deve ser `sys.stdout.reconfigure(encoding="utf-8")` (evita erro de acento no terminal do Windows).
- Chamar `python3`; se não existir, `python`. Sem nenhum dos dois, fazer a conta em JavaScript num script à parte (fora do painel) ou avisar o usuário e parar antes de qualquer número. O HTML entregue nunca recalcula a partir da base.
- Mostrar o script e a saída. Cada indicador sai com: valor, fórmula, colunas e filtros aplicados.
- Conferência cruzada: somar por um caminho e por outro (ex.: total do mês = soma dos totais por vendedor). Se não bater, investigar antes de seguir.
- No ChatGPT sem análise de dados ou em agente sem execução de código: fazer a conta por escrito, passo a passo, no relatório ao usuário. O HTML recebe só os resultados, cada um marcado "conta manual, conferir".

### PASSO 4: Montar o HTML

Regras do arquivo:
- **Um arquivo só**, com CSS e logo dentro (logo embutido em base64 ou como SVG).
- **Só números agregados.** O HTML leva apenas o que aparece na tela: totais, médias e as séries dos gráficos, já calculados. Nunca a base bruta, nunca colunas pessoais (nome, CPF, telefone, e-mail, endereço de cliente). Quem receber o arquivo por e-mail ou WhatsApp pode abrir o código-fonte.
- **Gráficos simples:** barra para comparar categorias, linha para evolução no tempo, número grande para indicador único. Nada de pizza 3D, velocímetro ou eixo cortado que exagera diferença. No máximo uma cor de destaque por gráfico.
- **Biblioteca de gráfico:** preferir SVG puro, desenhado no próprio HTML. Se usar biblioteca, só de CDN com a versão exata na URL (ex.: Chart.js pelo cdnjs, com o número completo da versão) e com os atributos `integrity` (hash SRI publicado pelo CDN) e `crossorigin="anonymous"` na tag `<script>`. Conferir que a URL abre antes de entregar.
- **Celular:** layout em coluna única abaixo de 600px, texto mínimo de 14px, nada de rolagem lateral.
- **Impressão:** regra `@media print` que remove botões, evita quebra de página no meio de um gráfico e força fundo branco.
- **Acessibilidade:** contraste legível, cor nunca é a única forma de informação (usar também rótulo ou seta ▲▼).

### PASSO 5: Destaques e "o que fazer com isso"

- **3 destaques**, uma frase cada, com o número que sustenta (ex.: "Região Sul caiu 18% contra outubro: R$ 42 mil → R$ 34,4 mil").
- **O que fazer com isso:** 1 a 3 ações sugeridas, marcadas como sugestão. Causa que não está nos dados é hipótese e aparece como hipótese ("pode ser efeito do feriado; confirmar com a equipe").

### PASSO 6: Conferir e entregar

1. Abrir o HTML (no navegador, se o agente tiver acesso) e conferir: cada número do painel bate com a saída do script, o layout funciona em largura de celular, a impressão cabe nas páginas. Se o navegador do agente bloquear arquivo local (`file://`), pedir ao usuário que abra o arquivo e conte o que vê (números, gráficos, se algo ficou cortado no celular).
2. Entregar o arquivo com nome `AAAA-MM-DD-painel-[tema].html`. No ChatGPT sem acesso a arquivos: entregar o HTML completo num bloco de código e explicar: "copie, cole no Bloco de Notas, salve como `.html` e abra com dois cliques".
3. Com OS no padrão MeuOS, oferecer guardar no contexto do PASSO 0 (na pasta de entregas do contexto) e registrar no `index.md`. Guardar também o script, para atualizar o painel no mês seguinte com a planilha nova.

---

## Template de saída (estrutura do HTML)

```html
<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>[Tema] · [Período]</title>
  <style>
    :root { --cor-1: [cor principal]; --cor-2: [cor de destaque]; --fundo: #ffffff; --texto: #1f2328; }
    body { font-family: [fonte da marca], system-ui, sans-serif; background: var(--fundo); color: var(--texto); margin: 0; padding: 16px; }
    .kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 160px), 1fr)); gap: 12px; }
    @media (max-width: 600px) { .kpis { grid-template-columns: 1fr; } }
    @media print { .nao-imprimir { display: none; } section { break-inside: avoid; } }
  </style>
</head>
<body>
  <header>[logo] <h1>[Pergunta de negócio]</h1> <p>[Período] · atualizado em DD/MM/AAAA</p></header>
  <section class="kpis">[4 a 8 cartões: valor, rótulo, variação ▲▼ contra a referência]</section>
  <section>[gráfico 1: evolução no tempo]</section>
  <section>[gráfico 2: comparação por categoria]</section>
  <section><h2>Destaques</h2>[3 frases com número]</section>
  <section><h2>O que fazer com isso</h2>[1 a 3 sugestões]</section>
  <footer>
    <h2>De onde vem cada número</h2>
    <div style="overflow-x:auto"><table>[# · Indicador · Fórmula · Colunas · Filtros]</table></div>
    <p>Base: [arquivo], [N] linhas, [data mín] a [data máx]. Tratamentos: [duplicadas removidas, vazios ignorados...]</p>
  </footer>
</body>
</html>
```

---

## Regras desta skill

- **Pergunta antes de gráfico.** Sem pergunta de negócio, o painel vira enfeite.
- **Inventário antes de conta.** Ninguém calcula nada antes de contar linhas, datas, duplicadas e vazios.
- **Todo número por código (ou conta manual por escrito, marcada "conferir") e com endereço.** O rodapé diz fórmula, colunas e filtros de cada indicador.
- **Dado não se limpa sem perguntar.** Duplicada, vazio e valor estranho têm tratamento confirmado pelo usuário.
- **Sem meta inventada, sem causa inventada.** Comparação só com referência real; causa fora dos dados é hipótese.
- **Painel para cliente não leva dado interno** (custo, margem, nome de funcionário) sem autorização.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Pergunta de negócio, público, período e contexto definidos
- [ ] Marca aplicada (do OS ou informada) ou padrão neutro aceito
- [ ] Inventário da base reportado (com o número de linhas vazias e duplicadas e o que foi feito com elas) e tratamentos confirmados
- [ ] 4 a 8 indicadores aprovados, cada um com fórmula
- [ ] Todo número calculado por código (ou marcado "conta manual, conferir") e conferido por caminho cruzado
- [ ] Script Python com `sys.stdout.reconfigure(encoding="utf-8")`, se usado
- [ ] HTML em arquivo único, só com os números agregados da tela (sem base bruta nem coluna pessoal)
- [ ] Gráficos simples em SVG puro, ou biblioteca de CDN com versão exata, `integrity` e `crossorigin="anonymous"`
- [ ] Funciona em largura de celular e imprime em PDF sem cortar gráfico (conferido pelo agente ou pelo usuário, se `file://` estiver bloqueado)
- [ ] Destaques com número e "o que fazer" marcado como sugestão
- [ ] Rodapé "de onde vem cada número" completo
- [ ] Se guardado no OS: `AAAA-MM-DD-painel-[tema].html` + script, e `index.md` atualizado

Se algum item falhou: corrigir ANTES de declarar concluído. Nunca reportar "feito" com item pendente.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
