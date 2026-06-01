---
name: gera-html-to-pdf
description: "Cria documentos longos em HTML que viram PDFs A4 perfeitos — propostas, lâminas, dossiês, relatórios. Resolve o problema clássico do PDF estourando (título numa página e texto na seguinte, tabela cortada no meio, foto cortando rosto, signature jogada em página vazia). A regra central: cada <div class=\"page\"> é UMA página A4 inteira pré-calibrada pelo agente. Navegador não decide — só renderiza."
---

---
name: Gera HTML to PDF
description: |
  Cria documentos longos em HTML que viram PDFs A4 perfeitos — propostas, lâminas,
  dossiês, relatórios, currículos, white papers. Resolve o problema clássico do PDF
  estourando: título numa página e texto na seguinte, tabela cortada no meio, foto
  cortando rosto, signature jogada em página vazia.
  Executa quando você diz "criar proposta", "gerar PDF", "documento HTML para PDF",
  "lâmina do produto", "white paper", "dossiê", "currículo bonito", "relatório em PDF",
  "criar template de doc longo", "minha proposta tá saindo torta no PDF",
  "PDF tá quebrando", "como fazer PDF que não estoura".
  A regra central: cada `<div class="page">` é UMA página A4 inteira pré-calibrada
  por você (ou pelo agente). O navegador não decide nada — só renderiza.
version: 1.0
context: meuos
user-invocable: true
argument-hint: "(sem argumentos — a skill entrevista o tipo de documento e gera)"
---

# Gera HTML to PDF — Documentos longos que imprimem certo

## Para quem é essa skill

Pra todo mundo que já passou pelo problema clássico:

- Pediu pro agente uma proposta em HTML
- Abriu, ficou bonita na tela
- Mandou imprimir em PDF (Ctrl+P)
- E saiu **quebrada**: título numa página, parágrafo na seguinte, tabela cortada no meio, signature do diretor jogada sozinha em página vazia

Essa skill ensina seu agente a **gerar HTML que vira PDF certinho** — toda vez.

Funciona pra qualquer documento longo: proposta comercial, lâmina de produto, currículo extenso, dossiê, white paper, briefing executivo, relatório de consultoria.

---

## A regra de ouro (o segredo único)

> **Cada `<div class="page">` é UMA página A4 inteira pré-calibrada pelo designer (ou pelo agente). O navegador não decide nada — só renderiza.**

Tudo o que vem abaixo é decorrência disso. Se você entender só essa frase, já resolveu 90% do problema.

---

## Por que dá errado quando você tenta automático

Quando você cria um HTML longo (digamos 3 páginas A4 de conteúdo) numa única `<div>` e pede pro Chrome imprimir em PDF, ele tenta:

1. Calcular quanto cabe em A4 (≈297mm de altura)
2. Procurar um "bom lugar" pra cortar — usando hints como `page-break-inside: avoid`
3. Se não acha lugar bom, corta na hora certa (sem critério claro)

**O problema:** essa heurística falha em conteúdo real. Tabelas grandes ficam órfãs, signature aparece em página em branco, parágrafo cortado no meio.

**A solução:** **não confiar no navegador**. Você (ou o agente) decide ANTES o que cabe em cada página A4, e marca explicitamente com `<div class="page">`.

---

## Anti-padrão (NÃO faça assim)

Esse é o jeito que TODOS os agentes tentam primeiro — e que sempre falha:

```html
<div class="page" style="min-height: 297mm;">
  <section style="page-break-inside: avoid;">Capa</section>
  <section style="page-break-inside: avoid;">Quem somos</section>
  <section style="page-break-inside: avoid;">Diagnóstico</section>
  <section style="page-break-inside: avoid;">Solução</section>
  <section style="page-break-inside: avoid;">Investimento</section>
  <section style="page-break-inside: avoid;">Como funciona</section>
  <section style="page-break-inside: avoid;">Próximos passos</section>
</div>
```

**Resultado:** PDF quebrado. Sempre.

---

## Padrão correto (FAÇA assim)

Cada `<div class="page">` é UMA página A4. O agente decide o que cabe.

```html
<body>

  <!-- Página 1 — Capa -->
  <div class="cover-page">
    <!-- logo, título, cliente, foto, meta -->
  </div>

  <!-- Página 2 — Contexto + Diagnóstico + Solução (cabe em A4) -->
  <div class="page">
    <section>Quem somos</section>
    <section>Diagnóstico</section>
    <section>Solução</section>
    <div class="page-footer">Brand · Doc · Página 2 de 5</div>
  </div>

  <!-- Página 3 — Investimento (cabe em A4) -->
  <div class="page">
    <section>Composição</section>
    <section>Mensal × Anual</section>
    <section>Formas de pagamento</section>
    <div class="page-footer">Brand · Doc · Página 3 de 5</div>
  </div>

  <!-- ...e assim por diante até página N... -->

</body>
```

**Por que funciona:**
- Cada `.page` mede ≤297mm (designer calibrou)
- `page-break-after: always` força quebra exatamente no fim de cada `.page`
- Chrome só renderiza — não toma decisão nenhuma
- Resultado: PDF idêntico à intenção

---

## CSS canônico (copia e cola)

```css
/* ────── PAGE A4 ────── */
.page {
  width: 210mm;
  min-height: 297mm;
  margin: 12mm auto;
  background: #fff;
  position: relative;
  page-break-after: always;
  display: flex;
  flex-direction: column;
  padding: 16mm 18mm;
  box-shadow: 0 4px 24px rgba(0,0,0,.12);
}
.page:last-of-type { page-break-after: auto; }

/* Footer "Página N de M" colado no rodapé via flex */
.page-footer {
  margin-top: auto;
  padding-top: 8mm;
  border-top: 1px solid #e5e7eb;
  display: flex;
  justify-content: space-between;
  font-size: 7pt;
  letter-spacing: 1.5px;
  color: #6b7280;
  text-transform: uppercase;
}

/* ────── COVER PAGE (capa com height FIXA) ────── */
.cover-page {
  width: 210mm;
  height: 297mm;          /* FIXA — não min-height */
  margin: 12mm auto;
  overflow: hidden;
  page-break-after: always;
  display: flex;
  flex-direction: column;
  background: /* sua cor/gradient aqui */;
}

/* ────── @media print ────── */
@media print {
  body {
    background: white;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;     /* preserva cores no PDF */
  }
  .cover-page, .page {
    margin: 0;
    box-shadow: none;
  }
  @page {
    size: A4;
    margin: 0;             /* designer controla via padding interno */
  }
}
```

---

## Como gerar o PDF — 2 caminhos válidos

Você tem 2 jeitos de gerar o PDF, ambos funcionam **desde que o HTML siga a regra de ouro**:

### Caminho 1 — Ctrl+P no navegador (mais simples)

Esse é o caminho do dia-a-dia.

1. Abre o HTML no Chrome (recomendado), Edge ou Firefox
2. **Ctrl+P** (Windows) ou **Cmd+P** (Mac)
3. Configurações na janela de impressão:
   - **Destino**: Salvar como PDF
   - **Tamanho do papel**: A4
   - **Margens**: Nenhuma (zero) — o padding interno das `.page` já cuida
   - **Escala**: Padrão (100%) — NÃO "Ajustar à largura"
   - **Cabeçalhos e rodapés**: DESLIGAR (senão Chrome injeta "Page 1 of N · URL · data")
   - **Gráficos de plano de fundo**: LIGAR (senão fundos coloridos somem)
4. Salvar como PDF

**Resultado funciona perfeito** se o HTML estiver com:
- `@page { size: A4; margin: 0 }` no CSS
- `print-color-adjust: exact` no `@media print`
- Cada `.page` div bem calibrado pra caber em A4

### Caminho 2 — Chrome headless via terminal (automatização)

Pra quando você quer gerar PDF SEM abrir navegador (script, automação, lote):

```bash
# Windows
CHROME="/c/Program Files/Google/Chrome/Application/chrome.exe"
# Mac: CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# Linux: CHROME="/usr/bin/google-chrome"

HTML="path/to/proposta.html"
PDF="path/to/proposta.pdf"

"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$PDF" "file:///$HTML"
```

**Quando usar cada um:**

| Cenário | Caminho |
|---|---|
| Você está no PC, quer gerar 1 proposta | **Ctrl+P** |
| Vai mandar PDF pro cliente | **Ctrl+P** funciona |
| Agente automatizado (n8n, cron, script) | **Chrome headless** |
| Lote de 50 PDFs | **Chrome headless** |

---

## Checklist do agente (validar antes de entregar)

- [ ] Cada `.page` div tem ≤1 página A4 de conteúdo (sem estourar)?
- [ ] CSS `.page` com `display: flex; flex-direction: column`?
- [ ] Footer com `margin-top: auto`?
- [ ] Padding interno consistente entre páginas?
- [ ] ZERO `page-break-inside: avoid` espalhado em sections?
- [ ] `@media print` com `print-color-adjust: exact`?
- [ ] Capa com `height: 297mm` FIXA + `overflow: hidden`?
- [ ] Imagens embedadas base64 (não path relativo)?
- [ ] Fontes via Google Fonts ou system (não local)?
- [ ] Testou abrir o HTML e fazer Ctrl+P pra ver se o PDF sai certo?

---

## Erros comuns e soluções

### "Foto cortou o rosto da pessoa"
**Causa:** estimativa errada de coordenadas. **Solução:** se você sabe Python, usar OpenCV pra detectar face REAL:

```python
import cv2
img = cv2.imread('foto.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml').detectMultiScale(gray, 1.1, 5)
big = sorted(faces, key=lambda f: f[2]*f[3], reverse=True)[0]
cx_percent = (big[0]+big[2]//2)/img.shape[1]*100
cy_percent = (big[1]+big[3]//2)/img.shape[0]*100
# usar como: background-position: {cx_percent}% {cy_percent}%
```

Se não sabe, peça ao agente que tente várias posições (`center 20%`, `center 30%`, `65% 25%`) e mostre print de cada uma — escolhe a que ficou melhor.

### "Página estourando, conteúdo virou pra A4 seguinte vazia"
**Causa:** uma `.page` com mais conteúdo do que cabe em 297mm. **Solução:** dividir em 2 `.page`.

### "Cor de fundo sumiu no PDF"
**Causa:** falta `print-color-adjust: exact` no `@media print`. **Solução:** adicionar. No Ctrl+P, ligar opção "Gráficos de plano de fundo".

### "Headers/footers do Chrome aparecem (Page 1 of N, URL, data)"
**Causa:** no Ctrl+P, opção "Cabeçalhos e rodapés" está ligada. **Solução:** desligar. Via terminal: adicionar `--no-pdf-header-footer`.

### "Imagem aparece local, mas no PDF aparece quebrada"
**Causa:** path relativo da imagem não funciona após mover arquivo. **Solução:** embedar base64 inline OU usar URL absoluta de CDN.

---

## Como pedir certo ao seu agente

Use esse prompt-template quando pedir uma proposta/documento longo:

```
Gere [proposta/lâmina/dossiê] em HTML para [cliente/tema] seguindo a regra de ouro:

CADA <div class="page"> É UMA PÁGINA A4 INTEIRA PRÉ-CALIBRADA.

Quebre o documento em N páginas A4 separadas (1 div .page por página).
NÃO use page-break-inside: avoid espalhado — não funciona. Quebre manualmente em divs.

Estrutura esperada:
- 1 div.cover-page (capa, se for proposta comercial)
- N divs.page (conteúdo, 1 por página A4)

CSS:
- .page com width: 210mm, min-height: 297mm, page-break-after: always,
  display: flex, flex-direction: column, padding: 16mm 18mm
- .cover-page com height: 297mm fixa, overflow: hidden
- @page com size: A4, margin: 0
- @media print com print-color-adjust: exact

Pipeline:
- Eu vou abrir o HTML e gerar PDF via Ctrl+P → Salvar como PDF, papel A4,
  margens zero, sem cabeçalhos/rodapés, gráficos de plano de fundo ligados.

Conteúdo de cada página:
[descrever conteúdo de cada página AQUI — não deixar o agente adivinhar]
```

Adapte detalhes (paleta, fonte, número de páginas) ao seu contexto.

---

## Quando NÃO usar essa skill

- Páginas web responsivas (mobile-first, não A4) — use HTML normal
- Slides 16:9 pra apresentação em tela — use a skill **Criar Apresentação** (foi atualizada também com a mesma regra de ouro)
- Web apps interativos — essa skill é só pra docs estáticos A4
- Documento curto 1 página simples — Word/Markdown direto basta

---

## Quantas páginas por tipo de documento

| Tipo de documento | N páginas A4 típico |
|---|---|
| Proposta de assinatura simples | 4-5 |
| Proposta com customização | 5-6 |
| Proposta de parceria estratégica | 9-14 |
| Lâmina de produto | 2-3 |
| White paper | 8-15 |
| Currículo extenso | 2-3 |
| Relatório executivo mensal | 4-8 |

**Decidir antes de codar**: quais N páginas? Que conteúdo cada uma? Calcular se cabe.

---

## Skills relacionadas

- **Criar Modelo de Apresentação** — gera padrão visual de slides (35 layouts) com a regra de ouro aplicada
- **Criar Apresentação** — usa o modelo + conteúdo pra gerar slides em HTML, também aplicando a regra
- **PDF** — manipulação de PDFs já gerados (merge, split, marca d'água)
- **Fim do Dia** — captura aprendizado de "criei a proposta X" se for relevante

---

## Resumo em uma frase

> **Não confie no navegador pra paginar. Você (ou seu agente) decide ANTES quanto cabe em cada A4 e marca com `<div class="page">`. Pra gerar PDF, Ctrl+P funciona bem (com margem zero + cabeçalho desligado), ou rode Chrome headless `--print-to-pdf` se for automação.**
