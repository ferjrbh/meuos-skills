---
name: pdf
description: "Manipular arquivos PDF. Usar quando voce pedir para ler, extrair texto/tabelas de PDF, combinar/mergear PDFs, dividir PDFs, rotacionar paginas, adicionar marca dagua, criar novos PDFs, preencher formularios PDF, criptografar/descriptografar, extrair imagens, ou fazer OCR em PDFs escaneados. Trigger: 'pdf', 'extrair pdf', 'mergear pdf', 'dividir pdf', 'marca dagua', 'formulario pdf', 'OCR'. Se o usuario mencionar .pdf ou pedir para produzir um, usar esta skill."
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Processamento de PDF — Guia Completo

## Quick Start

```python
from pypdf import PdfReader, PdfWriter

# Ler PDF
reader = PdfReader("document.pdf")
print(f"Paginas: {len(reader.pages)}")

# Extrair texto
text = ""
for page in reader.pages:
    text += page.extract_text()
```

## Bibliotecas Python

### pypdf — Operacoes Basicas

#### Mergear PDFs
```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf", "doc3.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)
writer.write("merged.pdf")
```

#### Dividir PDF
```python
reader = PdfReader("document.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    writer.write(f"page_{i+1}.pdf")
```

#### Rotacionar Paginas
```python
reader = PdfReader("document.pdf")
writer = PdfWriter()
for page in reader.pages:
    page.rotate(90)  # 90, 180, 270
    writer.add_page(page)
writer.write("rotated.pdf")
```

#### Marca D'agua
```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("document.pdf")
watermark = PdfReader("watermark.pdf").pages[0]
writer = PdfWriter()

for page in reader.pages:
    page.merge_page(watermark)
    writer.add_page(page)
writer.write("watermarked.pdf")
```

#### Criptografar/Descriptografar
```python
# Criptografar
writer = PdfWriter()
writer.append_pages_from_reader(PdfReader("document.pdf"))
writer.encrypt(user_password="SENHA_DE_LEITURA", owner_password="SENHA_DO_DONO")
writer.write("encrypted.pdf")

# Descriptografar
reader = PdfReader("encrypted.pdf")
reader.decrypt("senha")
writer = PdfWriter()
writer.append_pages_from_reader(reader)
writer.write("decrypted.pdf")
```

#### Extrair Imagens
```python
reader = PdfReader("document.pdf")
for i, page in enumerate(reader.pages):
    for j, image in enumerate(page.images):
        with open(f"image_{i}_{j}.{image.name.split('.')[-1]}", "wb") as f:
            f.write(image.data)
```

### pdfplumber — Extrair Texto com Layout

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        # Texto preservando layout
        text = page.extract_text()

        # Tabelas
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                print(row)
```

### reportlab — Criar PDFs Novos

```python
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib import colors

c = canvas.Canvas("novo.pdf", pagesize=A4)
width, height = A4

# Texto
c.setFont("Helvetica-Bold", 24)
c.drawString(2*cm, height - 3*cm, "Titulo do Documento")

c.setFont("Helvetica", 12)
c.drawString(2*cm, height - 5*cm, "Conteudo do documento aqui.")

# Retangulo colorido
c.setFillColor(colors.HexColor("#c8a97e"))
c.rect(2*cm, height - 8*cm, 10*cm, 2*cm, fill=True)

# Imagem
c.drawImage("logo.png", 2*cm, height - 12*cm, width=5*cm, height=3*cm)

c.showPage()
c.save()
```

### Tabelas com reportlab

```python
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

doc = SimpleDocTemplate("tabela.pdf", pagesize=A4)
styles = getSampleStyleSheet()

data = [
    ['Coluna 1', 'Coluna 2', 'Coluna 3'],
    ['Dado 1', 'Dado 2', 'Dado 3'],
    ['Dado 4', 'Dado 5', 'Dado 6'],
]

table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1d1d1f")),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
]))

doc.build([table])
```

## OCR em PDFs Escaneados

```python
# Requer: pip install pytesseract pdf2image
# + Tesseract instalado no sistema

from pdf2image import convert_from_path
import pytesseract

images = convert_from_path("scanned.pdf")
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image, lang='por')  # Portugues
    print(f"--- Pagina {i+1} ---")
    print(text)
```

## Converter PDF para Imagens

```bash
# Com pdftoppm (poppler-utils)
pdftoppm -png document.pdf output_prefix

# Com Python
from pdf2image import convert_from_path
images = convert_from_path("document.pdf")
for i, img in enumerate(images):
    img.save(f"page_{i+1}.png")
```

## Preencher Formularios PDF

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("form.pdf")
writer = PdfWriter()
writer.append_pages_from_reader(reader)

# Preencher campos
writer.update_page_form_field_values(
    writer.pages[0],
    {"campo_nome": "Fulano da Silva", "campo_email": "email@example.com"},
)
writer.write("filled_form.pdf")
```

## Verificacao de Bounding Boxes (validacao visual)
```python
# Checar se elementos estao dentro dos limites da pagina
from pypdf import PdfReader

reader = PdfReader("document.pdf")
for i, page in enumerate(reader.pages):
    box = page.mediabox
    print(f"Pagina {i+1}: {box.width}x{box.height}")
```

## Dependencias
- `pypdf` — operacoes basicas (merge, split, rotate, encrypt, images)
- `pdfplumber` — extracao de texto/tabelas com layout
- `reportlab` — criacao de PDFs novos
- `pytesseract` + `pdf2image` — OCR
- `pdftoppm` (poppler-utils) — conversao para imagens

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
