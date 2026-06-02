---
name: docx
description: |
  Criar, editar e analisar documentos Word (.docx). Usar quando voce pedir para criar
  proposta em Word, editar documento, extrair texto de .docx, converter .doc para .docx,
  aceitar tracked changes, adicionar comentarios, ou produzir qualquer entregavel em formato Word.
  Trigger: 'word', 'docx', 'documento word', 'proposta em word', 'contrato word', 'editar documento'.
  NAO usar quando o entregavel for PDF (usar pdf), HTML, planilha (usar xlsx) ou apresentacao (usar pptx).
  DESAMBIGUACAO: Se voce disser 'documento' ou 'criar documento' sem formato, PERGUNTAR:
  "Qual formato? 1) Word .docx (docx) 2) PDF (pdf) 3) Planilha Excel (xlsx)"
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Documentos Word (.docx) — Guia Completo

## Visao Geral
DOCX e um arquivo ZIP contendo XMLs. Podemos ler, criar e editar de varias formas.

## Referencia Rapida

| Tarefa | Ferramenta | Metodo |
|--------|-----------|--------|
| Ler conteudo | pandoc | `pandoc file.docx -t markdown` |
| Criar novo | docx-js (Node) | Script JS com npm |
| Editar existente | XML direto | Unzip → editar XML → rezip |
| Converter .doc | LibreOffice | `soffice --convert-to docx` |
| Converter para imagem | LibreOffice + pdftoppm | Via PDF intermediario |

## Converter .doc para .docx
```bash
soffice --headless --convert-to docx:"MS Word 2007 XML" input.doc --outdir output/
```

## Ler Conteudo
```bash
# Com pandoc (melhor para texto)
pandoc document.docx -t markdown -o output.md

# Com pandoc (texto puro)
pandoc document.docx -t plain -o output.txt
```

## Criar Novos Documentos com docx-js

### Setup
```bash
mkdir docx-project && cd docx-project
npm init -y
npm install docx
```

### Estrutura Basica
```javascript
const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType } = require('docx');
const fs = require('fs');

const doc = new Document({
    sections: [{
        properties: {
            page: {
                size: { width: 11906, height: 16838 }, // A4 em twips
                margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
            }
        },
        children: [
            new Paragraph({
                children: [new TextRun({ text: "Titulo", bold: true, size: 28 })],
                heading: HeadingLevel.HEADING_1,
            }),
            new Paragraph({
                children: [new TextRun("Texto do paragrafo")],
            }),
        ],
    }],
});

Packer.toBuffer(doc).then(buffer => {
    fs.writeFileSync("output.docx", buffer);
});
```

### Tabelas
```javascript
const { Table, TableRow, TableCell, WidthType, BorderStyle } = require('docx');

new Table({
    rows: [
        new TableRow({
            children: [
                new TableCell({
                    width: { size: 50, type: WidthType.PERCENTAGE },
                    children: [new Paragraph("Celula 1")],
                }),
                new TableCell({
                    width: { size: 50, type: WidthType.PERCENTAGE },
                    children: [new Paragraph("Celula 2")],
                }),
            ],
        }),
    ],
});
```

### Imagens
```javascript
const { ImageRun } = require('docx');

new Paragraph({
    children: [
        new ImageRun({
            data: fs.readFileSync("image.png"),
            transformation: { width: 400, height: 300 },
            altText: { title: "Descricao", description: "Descricao da imagem" },
        }),
    ],
});
```

### Hyperlinks
```javascript
const { ExternalHyperlink } = require('docx');

new Paragraph({
    children: [
        new ExternalHyperlink({
            children: [new TextRun({ text: "Clique aqui", style: "Hyperlink" })],
            link: "https://example.com",
        }),
    ],
});
```

### Headers e Footers
```javascript
const { Header, Footer, PageNumber } = require('docx');

// Na section:
headers: {
    default: new Header({
        children: [new Paragraph("Cabecalho")],
    }),
},
footers: {
    default: new Footer({
        children: [
            new Paragraph({
                children: [
                    new TextRun("Pagina "),
                    new TextRun({ children: [PageNumber.CURRENT] }),
                    new TextRun(" de "),
                    new TextRun({ children: [PageNumber.TOTAL_PAGES] }),
                ],
            }),
        ],
    }),
},
```

## Editar Documentos Existentes

### Workflow de 3 Passos
1. **Descompactar**: Extrair o ZIP e formatar XML
2. **Editar**: Modificar os XMLs diretamente
3. **Recompactar**: Recriar o ZIP

```bash
# 1. Descompactar
mkdir unpacked && cd unpacked
unzip ../document.docx

# 2. Editar XMLs (word/document.xml e o principal)
# Usar Read/Edit tools do Claude

# 3. Recompactar
cd unpacked && zip -r ../modified.docx . -x ".*"
```

### Estrutura Principal do XML
- `word/document.xml` — Conteudo principal
- `word/styles.xml` — Estilos
- `word/numbering.xml` — Listas numeradas/bullets
- `word/_rels/document.xml.rels` — Relacionamentos
- `[Content_Types].xml` — Tipos de conteudo

## Aceitar Tracked Changes
```bash
# Via LibreOffice (se disponivel)
soffice --headless --norestore --convert-to docx input_with_changes.docx
```

## Converter para Imagens
```bash
# Via PDF intermediario
soffice --headless --convert-to pdf document.docx
pdftoppm -png document.pdf output_prefix
```

## Regras Criticas
- **Smart quotes**: Usar entidades XML (`&#x201C;` para ", `&#x201D;` para ")
- **Namespaces**: Manter TODOS os namespaces do XML original
- **IDs unicos**: Cada elemento precisa de ID unico no documento
- **Validacao**: Sempre abrir o .docx resultante para verificar
- **Backup**: SEMPRE fazer backup antes de editar (REGRA #6 do OS)

## Dependencias
- `pandoc` — leitura de conteudo
- `docx` (npm) — criacao de documentos
- `soffice` (LibreOffice) — conversoes e tracked changes
- `defusedxml` (pip) — parse seguro de XML

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
