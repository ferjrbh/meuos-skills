---
name: Criar Apresentacao
description: |
  Cria uma apresentacao completa (HTML navegavel ou arquivo PPTX) a partir de um modelo
  visual previamente criado pela skill "Criar Modelo de Apresentacao" + o conteudo que
  voce informar. A skill entrevista, sugere estrutura, gera e valida.
  Executa quando o usuario diz "criar apresentacao", "montar slides", "fazer uma apresentacao",
  "criar slides", "novo deck", "montar deck", "montar ppt", "criar ppt", "precisa de slides",
  "apresentacao sobre X", "slides sobre X".
version: 1.0
context: meuos
user-invocable: true
argument-hint: "<tema ou briefing da apresentacao — opcional>"
---

---

## 🥇 REGRA DE OURO — HTML que vira PDF certo (novidade · 13-MAI-2026)

Se você (ou o agente) está gerando HTML que será impresso em PDF (Ctrl+P → Salvar como PDF), a regra abaixo é INQUEBRÁVEL:

> **Cada `<div class="page">` (ou `<div class="slide">`) é UMA página A4 / UM slide 16:9 inteiro pré-calibrado pelo designer. O navegador não decide nada — só renderiza.**

NUNCA empilhar múltiplas seções dentro de uma `.page`/`.slide` confiando em `page-break-inside: avoid`. A heurística do Chrome falha. SEMPRE quebrar manualmente em divs separados, 1 por página/slide.

**CSS canônico:**
```css
.page, .slide {
  width: 210mm;           /* A4 portrait; ou 338mm pra 16:9 paisagem */
  min-height: 297mm;      /* A4; ou 190mm pra 16:9 */
  page-break-after: always;
  display: flex;
  flex-direction: column;
  padding: 16mm 18mm;
}
@page { size: A4; margin: 0; }
@media print {
  body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
}
```

**Detalhamento completo:** veja a skill **`Gera HTML to PDF`** (subcategory `office`) — fonte-única dessa regra, com checklist, anti-patterns, e prompt-template pra você pedir certo ao agente.

---


# Criar Apresentacao — Slides Completos em Minutos

## O que esta skill faz

Esta skill monta uma apresentacao de verdade para voce — com capa, secoes, conteudo,
graficos se precisar, e encerramento — usando um MODELO visual que voce ja criou antes
(pela skill "Criar Modelo de Apresentacao"). Voce passa o tema e o conteudo, a skill
estrutura, gera e valida.

Dois formatos disponiveis:
1. **HTML navegavel** — arquivo `.html` que abre no navegador, voce apresenta direto
   da tela ou exporta para PDF (Ctrl+P → Salvar como PDF)
2. **Arquivo PPTX** — arquivo real do PowerPoint, voce pode abrir no PowerPoint/Keynote
   e editar depois

---

## Quando usar

- Quando voce precisa de uma apresentacao (reuniao, pitch, treinamento, pauta, aula)
- Quando quer transformar um documento/briefing em slides
- Quando o usuario diz "criar apresentacao", "montar slides", "fazer um ppt"

---

## Pre-requisito

Voce precisa ter pelo menos UM modelo criado pela skill `criar-modelo-apresentacao`.
Se nao tiver nenhum, esta skill vai avisar e te direcionar para criar um primeiro.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0 — Verificar se existe modelo criado

Antes de qualquer coisa, verificar se a pasta `meus-modelos/` existe no OS do usuario e
se tem pelo menos um subdiretorio com `tokens.json`.

**Se NAO existir nenhum modelo:**

> Para criar uma apresentacao voce precisa primeiro ter um MODELO visual (cores, fonte,
> logo, layouts). Eu vejo que voce ainda nao tem nenhum modelo criado.
>
> Vou te direcionar para a skill **Criar Modelo de Apresentacao** primeiro — ela cria
> o seu padrao visual em uns 5 minutos. Depois volto aqui para montar a apresentacao.
>
> Posso abrir a skill Criar Modelo agora? (sim/nao)

Se `sim`: abrir a skill `criar-modelo-apresentacao` e, apos a skill terminar, retomar
desta mesma skill no PASSO 1.

Se `nao`: encerrar e informar que o usuario pode retomar quando tiver um modelo pronto.

**Se existir UM modelo:**
- Usar esse modelo automaticamente (mostrar qual: "Vou usar seu modelo: {nome_modelo}")
- Avancar para PASSO 1

**Se existirem VARIOS modelos:**

> Voce tem varios modelos. Qual devo usar?
>
> 1. **{nome_modelo_1}** — criado em {data} ({cor_primaria} + {fonte})
> 2. **{nome_modelo_2}** — criado em {data} ({cor_primaria} + {fonte})
> 3. ...
>
> Responde o numero ou o nome. (ou diga "outro" se quiser usar um modelo que nao esta
> nessa lista — vou pedir o path)

Aguardar resposta. Se "outro", pedir path completo e validar que tem `template.html` e
`tokens.json`.

Apos definir o modelo, carregar em memoria:
- `tokens = json.parse(meus-modelos/{nome}/tokens.json)`
- `template_html = read(meus-modelos/{nome}/template.html)` (para copiar o CSS+JS)
- `assets_dir = meus-modelos/{nome}/assets/`

---

### PASSO 1 — Perguntar o formato de saida

> Como voce quer o arquivo final?
>
> 1. **HTML navegavel** — abre no navegador, voce apresenta direto da tela, exporta PDF
>    facil com Ctrl+P. Melhor para apresentar ao vivo.
> 2. **PPTX (PowerPoint)** — arquivo `.pptx` real, abre no PowerPoint ou Keynote, voce
>    edita depois. Melhor se alguem precisa editar.
>
> (Sugestao padrao: 1 — HTML, e o que funciona melhor com seu modelo)

Salvar em `formato = "html" | "pptx"`.

**Se `formato = "pptx"`:**

Verificar se a skill `pptx` (geracao de arquivos PowerPoint) esta disponivel no OS do
usuario.

Se `sim`:
> Beleza, vou usar a skill `pptx` para gerar o arquivo final. Seguindo.

Se `nao`:
> A skill `pptx` (que gera arquivos PowerPoint reais) nao esta instalada no seu MeuOs.
> Tenho 3 opcoes:
>
> 1. **Instalar a skill `pptx` agora** (recomendado — depois ela fica disponivel pra
>    sempre). Ela esta no marketplace do MeuOs.
> 2. **Gerar via Python** direto aqui (um pouco mais lento, mas funciona sem instalar
>    nada). Uso a biblioteca `python-pptx`.
> 3. **Trocar para HTML** (mais rapido, voce pode exportar PDF depois).
>
> O que prefere? (1 / 2 / 3)

Se `1`: orientar a instalar (`skills` → `pptx` → instalar) e depois retomar.
Se `2`: continuar com Python — anotar `modo_pptx = "python"`.
Se `3`: mudar `formato = "html"` e seguir.

---

### PASSO 2 — Capturar o briefing

Perguntar (de forma conversacional, sem sobrecarregar):

> Agora me conta o que voce quer apresentar. Pode ser:
>
> - Um **tema** em 1 frase ("pitch do meu produto para investidores", "treinamento sobre
>   IA para a equipe de vendas")
> - Um **documento** que eu leia e transforme em slides (me passa o caminho ou cola o texto)
> - Uma **estrutura basica** ja pensada (capa + 3 secoes + encerramento) que eu vou encher
>   de conteudo
>
> O que voce tem?

Aguardar resposta. Processar:
- Se for tema curto: aceitar e seguir para PASSO 3 perguntando mais detalhes
- Se for documento: ler o arquivo completo (com `Read`) e extrair pontos principais
- Se for estrutura: confirmar e seguir para PASSO 3

**Perguntar sempre** (mesmo que o briefing seja completo):

> 4 coisas rapidas para calibrar:
>
> 1. **Quanto tempo** a apresentacao vai durar? (5 min / 15 min / 30 min / 1h)
> 2. **Publico** — pra quem e? (clientes / equipe interna / investidores / alunos / publico geral)
> 3. **Tom** — formal, didatico, provocativo, comercial? (sugestao padrao: didatico)
> 4. **Objetivo final** — o que voce quer que o publico faca/pense no fim? (decidir X,
>    aprender Y, aprovar Z, se convencer de W)

Salvar em objeto `briefing`:

```
briefing = {
  tema: string,
  conteudo_base: string | documento_path,
  duracao: "5min" | "15min" | "30min" | "1h",
  publico: string,
  tom: string,
  objetivo: string
}
```

---

### PASSO 3 — Propor estrutura (arco narrativo)

Com base no briefing, propor uma estrutura. Regra geral de slides por duracao:

| Duracao | Quantidade de slides |
|---------|---------------------|
| 5 min | 6-10 slides |
| 15 min | 15-20 slides |
| 30 min | 25-35 slides |
| 1h | 40-60 slides |

**Arco narrativo padrao** (adaptar ao tom e objetivo):

1. **Capa** (1 slide)
2. **Indice** (1 slide)
3. **Contexto/problema** (3-5 slides)
4. **Divisoria de secao**
5. **Proposta/solucao** (5-8 slides)
6. **Divisoria de secao**
7. **Evidencia/dados** (3-5 slides, com graficos)
8. **Divisoria de secao**
9. **Call-to-action / proximos passos** (2-3 slides)
10. **Encerramento** (1 slide com contato)

Ajustes por tom:
- **Comercial/pitch**: incluir pricing, social proof, ROI
- **Didatico**: incluir exemplos, exercicio, FAQ
- **Provocativo**: abrir com BIG NUMBER ou quote, reservar reviravolta no meio
- **Formal**: menos visual, mais texto estruturado, menos BIG NUMBER

Apresentar ao usuario:

```
Estrutura proposta — {briefing.tema}

| Slide | Tipo | Conteudo |
|-------|------|----------|
| 1 | Capa | "{titulo}" |
| 2 | Indice | 4 secoes |
| 3 | Divisoria | Parte 1 — Diagnostico |
| 4 | Conteudo 3 bullets | Problema central |
| 5 | BIG NUMBER | 68% dos negocios nao... |
| ... | ... | ... |
| {N} | Encerramento | Obrigado + {contato} |

Total: {N} slides, ~{min} min estimados.

Posso seguir com essa estrutura? Ou quer ajustar alguma coisa?
(ex: "adicionar slide de comparacao antes da secao 3", "remover o pricing")
```

Aguardar aprovacao. NAO prosseguir sem OK explicito. Ajustar quantas vezes o usuario
pedir.

---

### PASSO 4 — Preencher o conteudo (slide por slide)

Uma vez estrutura aprovada, o agente escreve o conteudo de cada slide. Regra:

- **Max 3 bullets por slide** (ou 1 visual por slide)
- Se precisa de mais: dividir em 2 slides
- **Toda secao de conteudo tem uma frase de impacto** (highlight-box)
- Usar numeros e comparacoes quando possivel
- NUNCA usar emojis — usar SVG inline ou icones Unicode discretos

Para cada slide, gerar objeto:

```
slide = {
  num: int,
  layout: "cover" | "section" | "content" | "split" | "photo-split" | "big-number" |
          "quote" | "chart" | "pricing" | "cta" | "closing" | ...,
  titulo: string,
  label: string | null,
  conteudo: [
    { tipo: "bullet"|"card"|"stat"|"chat"|"timeline", ... }
  ],
  frase_impacto: string | null,
  foto: "foto1"|"foto2"|"foto3" | null,
  section_num: int | null (apenas nos layouts section)
}
```

**Regra de uso das fotos do modelo:**
- Usar foto1/foto2/foto3 rotativamente nos slides com foto
- Se o usuario pedir fotos especificas para a apresentacao (nao as do modelo), pedir path
  local conforme o fluxo do PASSO 2b da skill criar-modelo-apresentacao

**Regra de ritmo visual:**
- Nunca 3+ slides seguidos com mesmo layout
- Intercalar: 2 slides de conteudo → 1 slide de impacto (big number/quote/full-bleed)
  → 2 slides de conteudo → 1 divisoria → repete

---

### PASSO 5 — Gerar o arquivo

**5a. Se `formato = "html"`:**

1. Ler `meus-modelos/{nome}/template.html` para pegar CSS+JS
2. Criar novo arquivo `minhas-apresentacoes/{slug_da_apresentacao}/index.html`
3. Copiar cabecalho (`<head>` com CSS), substituir `<title>` pelo titulo
4. Para cada slide do PASSO 4, gerar o HTML usando as classes correspondentes do catalogo
5. Copiar `<script>` de navegacao (mesmo do template)
6. Copiar a pasta `assets/` do modelo (ou linkar — preferir copiar para ficar
   auto-contido)

Estrutura final:

```
minhas-apresentacoes/
└── {slug}/
    ├── index.html
    └── assets/
        ├── logo.png
        ├── foto1.jpg
        ├── foto2.jpg
        └── foto3.jpg
```

**5b. Se `formato = "pptx"` e skill pptx disponivel:**

Chamar a skill `pptx` com os objetos de slide. A skill pptx mapeia:
- `layout=cover` → slide de titulo com subtitulo
- `layout=content` → titulo + bullets
- `layout=big-number` → titulo + numero gigante centralizado
- `layout=chart` → usar chart nativo do PPTX (barras/donut)
- `layout=table` → tabela nativa
- `layout=photo-split` → imagem + texto 2 colunas
- etc.

Paleta: usar `tokens.cor_primaria` + `tokens.cor_secundaria`.
Fonte: `tokens.fonte_principal`.

Saida: `minhas-apresentacoes/{slug}/apresentacao.pptx`

**5c. Se `formato = "pptx"` e modo Python:**

Gerar um script Python usando `python-pptx`:

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

prs = Presentation()
prs.slide_width = Inches(13.333)   # 16:9
prs.slide_height = Inches(7.5)

PRIMARY = RGBColor.from_string('{cor_primaria}'.lstrip('#'))
# ... gerar os slides ...

prs.save('minhas-apresentacoes/{slug}/apresentacao.pptx')
```

Rodar o script (via Bash tool) e verificar que o arquivo foi criado. Se faltar a
biblioteca `python-pptx`, instalar: `pip install python-pptx`.

---

### PASSO 6 — Auto-validacao

**6a. Para HTML — checagem estatica (sempre roda)**

| Verificacao | Erro se falhar |
|-------------|----------------|
| Arquivo existe e tem tamanho > 10KB | "HTML gerado esta vazio ou corrompido" |
| Numero de slides bate com estrutura aprovada? | "Gerou X slides, esperava Y" |
| Primeiro slide tem `class="slide ... active"` | "Primeiro slide sem active" |
| JS de navegacao presente? | "Navegacao por teclado ausente" |
| Nenhum `{{placeholder}}` restante? | "Tem placeholders nao substituidos" |
| Assets copiadas? | "Pasta assets/ faltando" |

**6b. Para HTML — validacao visual (se Playwright disponivel)**

Perguntar se Playwright esta instalado. Se `sim`:
- Abrir o index.html
- Capturar screenshot do slide 1, meio da apresentacao, e slide final
- Salvar em `minhas-apresentacoes/{slug}/validacao/`
- Reportar: "Validacao visual OK — 3 screenshots salvos"

Se `nao`:
> Para validacao visual automatica, instale o MCP Playwright. Sem ele, rodei so a
> checagem estatica — recomendo que voce abra o arquivo no navegador e confirme
> visualmente antes de usar.

**6c. Para PPTX — abrir e verificar**

- Contar slides gerados (com `python-pptx` abrindo o arquivo)
- Verificar tamanho do arquivo
- Reportar

---

### PASSO 7 — Relatorio final + como usar

**Se HTML:**

```
✓ Apresentacao criada

Arquivo: minhas-apresentacoes/{slug}/index.html
Modelo usado: {nome_modelo}
Slides: {N}
Duracao estimada: {duracao}

Como apresentar:
1. Abra `index.html` no navegador (Chrome, Edge ou Firefox)
2. Pressione F11 para tela cheia
3. Setas ← → ou espaco para navegar
4. Home/End para ir ao primeiro/ultimo
5. Numeros 1-9 para pular direto para um slide

Quer salvar em PDF tambem? (sim/nao)
```

Se `sim`, ensinar:
> Ainda com o arquivo aberto no navegador (use **Chrome** — mais confiavel pra impressao):
> 1. Ctrl+P (ou Cmd+P no Mac)
> 2. Destino: "Salvar como PDF"
> 3. Margens: **Nenhuma** (o tamanho 16:9 ja esta no CSS — nao mexa em orientacao)
> 4. Em "Mais configuracoes": desmarque "Cabecalho e rodape", **marque "Graficos de fundo"** (sem isso, fundos coloridos somem)
> 5. Salvar em `minhas-apresentacoes/{slug}/apresentacao.pdf`
>
> Cada slide vira 1 pagina PDF exata (33.867 x 19.05 cm — padrao PowerPoint 16:9).
> Se algum slide aparecer cortado ou em retrato: confirme que o modelo foi gerado pela
> versao atual da skill `criar-modelo-apresentacao` (precisa ter `@page` e `@media print`
> no template.html — gere de novo se nao tiver).

**Se PPTX:**

```
✓ Apresentacao criada

Arquivo: minhas-apresentacoes/{slug}/apresentacao.pptx
Modelo usado: {nome_modelo}
Slides: {N}

Como usar:
1. Abra o arquivo no PowerPoint, Keynote ou Google Slides
2. Edite se precisar (trocar fotos, ajustar textos)
3. Para apresentar: F5 (PowerPoint) ou tela cheia (Keynote)

Quer exportar em PDF tambem? (sim/nao)
```

Se `sim`, ensinar:
> No PowerPoint: Arquivo → Exportar → Criar PDF → Publicar
> No Keynote: Arquivo → Exportar para → PDF → Melhor qualidade
> Voce tambem pode usar a skill `pdf` do MeuOs se tiver instalada.

---

### PASSO 8 — Captura de aprendizado (opcional)

Se a sessao foi longa (passo 3 teve mais de 3 iteracoes), oferecer:

> Essa apresentacao tem algo especial que voce quer reaproveitar em outras? Posso salvar
> a estrutura em `minhas-apresentacoes/{slug}/estrutura.md` para voce usar de template
> no futuro.

Se `sim`: salvar a estrutura aprovada no PASSO 3 em formato markdown.

---

## Se o usuario pedir "abrir o arquivo" / "me mostra"

Para HTML: dar o path local + comando:
> Abra: `file:///{caminho_absoluto}/minhas-apresentacoes/{slug}/index.html`
> Ou clique duplo no arquivo pelo gerenciador de pastas.

Para PPTX: dar o path e dizer que abre no PowerPoint.

---

## Se o usuario pedir para "refazer um slide" ou "trocar X"

Aceitar edicoes pontuais:
> Qual slide? (numero ou descricao)
> O que voce quer trocar? (texto, layout, foto, cores)

Abrir o HTML, localizar o slide, editar, validar de novo (PASSO 6), reportar.

**NUNCA regenerar o arquivo inteiro por causa de uma edicao pontual** — apenas mudar o
slide especifico. Se o usuario pedir mudanca em 5+ slides, ai sim recomendar regenerar.

---

## Regras de seguranca

- **Sempre confirmar modelo e estrutura antes de gerar** — nunca executar PASSO 4+ sem OK
- **Nunca inventar dados, numeros ou citacoes** — se faltar dado, pedir ao usuario
- **Nunca sobrescrever apresentacao existente** — se `minhas-apresentacoes/{slug}/` ja
  existir, perguntar se sobrescreve ou cria com sufixo `-v2`
- **Nunca exportar PDF sem permissao** — so ensinar se o usuario perguntar
- **Sempre copiar assets para dentro da apresentacao** — manter auto-contida, para
  funcionar offline/em projetor sem internet
- **Se Playwright nao disponivel** — rodar checagem estatica E pedir ao usuario para
  validar visualmente antes de declarar concluido
- **Nunca usar URL de internet para imagens** — seguir a mesma regra do criar-modelo-apresentacao
- **Se o briefing for muito curto** (menos de 20 palavras), perguntar mais detalhes antes
  de propor estrutura — evita gerar apresentacao rasa

---

## Checklist final (antes de declarar concluido)

- [ ] Modelo existente foi identificado e carregado
- [ ] Formato (HTML ou PPTX) foi escolhido pelo usuario
- [ ] Briefing capturado (tema + duracao + publico + tom + objetivo)
- [ ] Estrutura foi proposta e APROVADA
- [ ] Arquivo gerado existe e passou na validacao estatica
- [ ] Validacao visual feita (Playwright ou manual)
- [ ] Usuario sabe onde esta o arquivo e como abrir
- [ ] Se perguntou sobre PDF, foi orientado

---

## Integracao com outras skills

- **Criar Modelo de Apresentacao** — fornece o modelo visual (pre-requisito)
- **pptx** — usada quando o formato e PPTX (se disponivel)
- **playwright** — usada para validacao visual automatica (opcional)
- **pdf** — usada para exportar PDF se o usuario pedir (opcional)
- **Fim do Dia** — captura o aprendizado de "criei a apresentacao X" se for relevante
