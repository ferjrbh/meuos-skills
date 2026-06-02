---
name: pptx
description: |
  Criar, editar e ler apresentacoes PowerPoint (.pptx). Gera ARQUIVO .pptx real para download/envio.
  Trigger: 'powerpoint', 'pptx', 'arquivo pptx', 'editar pptx', 'ler pptx', 'abrir pptx'.
  DESAMBIGUACAO: Se voce disser 'slides', 'apresentacao', 'PPT', 'montar slides' sem especificar formato, PERGUNTAR:
  "Qual formato? 1) HTML navegavel (apresentacao interativa via navegador) 2) Arquivo .pptx real para download/envio (pptx)"
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Apresentacoes PowerPoint (.pptx) — Guia Completo

## Referencia Rapida

| Tarefa | Ferramenta | Metodo |
|--------|-----------|--------|
| Ler conteudo | markitdown | `markitdown presentation.pptx` |
| Criar do zero | PptxGenJS (Node) | Script JS com npm |
| Editar existente | XML direto | Unzip → editar XML → rezip |
| Gerar thumbnails | LibreOffice + pdftoppm | Via PDF intermediario |
| Converter para imagens | LibreOffice | `soffice --convert-to pdf` → `pdftoppm` |

## Ler Conteudo

```bash
# Com markitdown (melhor)
pip install markitdown
markitdown presentation.pptx

# Extrair XML para inspecao
mkdir unpacked && cd unpacked && unzip ../presentation.pptx
```

## Criar do Zero com PptxGenJS

### Setup
```bash
mkdir pptx-project && cd pptx-project
npm init -y
npm install pptxgenjs
```

### Estrutura Basica
```javascript
const pptxgen = require('pptxgenjs');
const pres = new pptxgen();

// Layout padrao: 16:9
pres.layout = 'LAYOUT_WIDE'; // 13.33" x 7.5"

// Slide titulo
let slide = pres.addSlide();
slide.addText('Titulo da Apresentacao', {
    x: 0.5, y: 2.5, w: '90%',
    fontSize: 36, bold: true,
    color: '1d1d1f',  // Preto
    fontFace: 'Inter',
    align: 'center',
});

// Slide com conteudo
let slide2 = pres.addSlide();
slide2.addText('Subtitulo', {
    x: 0.5, y: 0.5, w: '90%',
    fontSize: 24, bold: true, color: 'c8a97e',  // Dourado
});
slide2.addText('Conteudo do slide aqui com explicacoes detalhadas.', {
    x: 0.5, y: 1.5, w: '90%',
    fontSize: 14, color: '424245',
});

pres.writeFile({ fileName: 'apresentacao.pptx' });
```

### Listas e Bullets
```javascript
slide.addText([
    { text: 'Item 1', options: { bullet: true, fontSize: 14, breakLine: true } },
    { text: 'Item 2', options: { bullet: true, fontSize: 14, breakLine: true } },
    { text: 'Item 3', options: { bullet: true, fontSize: 14 } },
], { x: 0.5, y: 2.0, w: '90%' });
```

### Imagens
```javascript
// De arquivo
slide.addImage({
    path: 'logo.png',
    x: 0.5, y: 0.5, w: 2.0, h: 1.5,
});

// De URL
slide.addImage({
    path: 'https://example.com/image.png',
    x: 0.5, y: 3.0, w: 4.0, h: 3.0,
});
```

### Shapes
```javascript
slide.addShape(pres.ShapeType.rect, {
    x: 0.5, y: 5.0, w: 12, h: 0.5,
    fill: { color: 'c8a97e' },  // Barra dourada
});

slide.addShape(pres.ShapeType.roundRect, {
    x: 1, y: 2, w: 4, h: 2,
    fill: { color: 'f5f5f7' },
    line: { color: '86868b', width: 1 },
    rectRadius: 0.2,
    shadow: { type: 'outer', blur: 6, offset: 3, color: '000000', opacity: 0.2 },
});
```

### Tabelas
```javascript
let rows = [
    [
        { text: 'Metrica', options: { bold: true, fill: { color: '1d1d1f' }, color: 'ffffff' } },
        { text: 'Valor', options: { bold: true, fill: { color: '1d1d1f' }, color: 'ffffff' } },
    ],
    ['Receita', 'R$ 1.2M'],
    ['Margem', '32%'],
];

slide.addTable(rows, {
    x: 0.5, y: 2.0, w: 8,
    fontSize: 12,
    border: { type: 'solid', color: '86868b', pt: 0.5 },
    colW: [4, 4],
});
```

### Charts
```javascript
let chartData = [
    { name: 'Q1', labels: ['Jan', 'Fev', 'Mar'], values: [100, 120, 150] },
    { name: 'Q2', labels: ['Abr', 'Mai', 'Jun'], values: [130, 145, 160] },
];

slide.addChart(pres.charts.BAR, chartData, {
    x: 0.5, y: 1.5, w: 8, h: 4,
    showTitle: true,
    title: 'Vendas por Trimestre',
    showValue: true,
    chartColors: ['c8a97e', '1d1d1f'],
});
```

### Background de Slide
```javascript
// Cor solida
slide.background = { color: '1d1d1f' };

// Imagem
slide.background = { path: 'background.jpg' };
```

## Editar Apresentacao Existente

### Workflow de 3 Passos
```bash
# 1. Descompactar
mkdir unpacked && cd unpacked && unzip ../presentation.pptx

# 2. Editar XMLs
# ppt/slides/slide1.xml, slide2.xml, etc.
# ppt/slideLayouts/, ppt/slideMasters/

# 3. Recompactar
cd unpacked && zip -r ../modified.pptx . -x ".*"
```

### Estrutura do PPTX
- `ppt/presentation.xml` — Metadata da apresentacao
- `ppt/slides/slide*.xml` — Conteudo de cada slide
- `ppt/slideLayouts/` — Layouts reutilizaveis
- `ppt/slideMasters/` — Masters com estilos base
- `ppt/media/` — Imagens e midia
- `ppt/_rels/` — Relacionamentos

## Paletas de Cores Sugeridas

### Elegante (preto & dourado)
- Preto: #1d1d1f | Dourado: #c8a97e | Cinzas: #f5f5f7, #86868b, #424245

### Profissional Clean
- Navy: #1e3a5f | Branco: #ffffff | Cinza: #f0f0f0 | Accent: #3498db

### Tech/Startup
- Dark: #0d1117 | Primary: #58a6ff | Secondary: #238636 | Text: #c9d1d9

## Design — Boas Praticas
- **Tipografia**: Maximo 2 fontes (titulo + corpo). Inter e excelente para ambas
- **Espacamento**: Minimo 0.5" de margem em todos os lados
- **Hierarquia**: Titulo 28-36pt, Subtitulo 20-24pt, Corpo 14-18pt
- **Cores**: Maximo 3-4 cores por slide. Usar contraste alto
- **Conteudo**: Maximo 6 bullets por slide. 1 ideia = 1 slide
- **Imagens**: Alta resolucao. Evitar clip art ou imagens genericas

## QA — Verificacao de Qualidade
1. Verificar texto cortado ou sobreposto
2. Confirmar alinhamento consistente entre slides
3. Checar contraste de cores (legibilidade)
4. Validar que todas as imagens carregam
5. Testar em diferentes proporcoes de tela

## Converter para Imagens
```bash
# Via LibreOffice
soffice --headless --convert-to pdf presentation.pptx
pdftoppm -png presentation.pdf slide
```

## Dependencias
- `pptxgenjs` (npm) — criacao de PPTX
- `markitdown` (pip) — leitura de conteudo
- `soffice` (LibreOffice) — conversoes
- `pdftoppm` (poppler-utils) — PDF para imagens

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
