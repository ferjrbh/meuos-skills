---
name: xlsx
description: |
  Manipular planilhas Excel e CSV. Usar quando voce pedir para criar, editar, analisar
  ou corrigir arquivos .xlsx, .xlsm, .csv ou .tsv. Tambem para limpar dados tabulares
  bagunçados, gerar relatorios financeiros, exports de dados, ou converter entre formatos tabulares.
  Trigger: 'planilha', 'excel', 'xlsx', 'csv', 'export dados', 'relatorio financeiro em excel'.
  O entregavel deve ser um arquivo de planilha.
  NAO usar quando o entregavel for Word, HTML, PDF ou script Python.
  NAO ativar com 'DRE' sozinho (DRE pode ser uma tela de dashboard no seu app, nao necessariamente uma planilha).
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Manipulacao de Planilhas Excel/CSV

## Requisitos para Outputs

### Fonte Profissional
- Usar fonte consistente e profissional (Arial, Times New Roman) salvo instrucao contraria

### Zero Erros de Formula
- Todo modelo Excel DEVE ser entregue com ZERO erros de formula (#REF!, #DIV/0!, #VALUE!, #N/A, #NAME?)

### Preservar Templates Existentes
- Ao modificar arquivos existentes, estudar e RESPEITAR formato, estilo e convencoes do original
- Convencoes do template original SEMPRE sobrepoem estas guidelines

## Modelos Financeiros

### Padrao de Cores (convencao do mercado financeiro)
- **Texto azul (0,0,255)**: Inputs hardcoded, numeros que o usuario altera para cenarios
- **Texto preto (0,0,0)**: TODAS as formulas e calculos
- **Texto verde (0,128,0)**: Links puxando de outras abas do mesmo workbook
- **Texto vermelho (255,0,0)**: Links externos para outros arquivos
- **Fundo amarelo (255,255,0)**: Premissas-chave que precisam de atencao

### Formatacao de Numeros
- **Anos**: Formato texto ("2024" nao "2.024")
- **Moeda**: R$ #.##0 formato; SEMPRE especificar unidade nos headers ("Receita (R$ mil)")
- **Zeros**: Usar formatacao para mostrar zeros como "-", incluindo percentuais
- **Percentuais**: Default 0,0% (uma decimal)
- **Multiplos**: Formato 0,0x para multiplos de valuation (EV/EBITDA, P/E)
- **Negativos**: Usar parenteses (123) nao menos -123

### Regras de Formulas

#### Premissas
- Colocar TODAS as premissas (taxas de crescimento, margens, multiplos) em celulas separadas
- Usar referencias de celula ao inves de valores hardcoded
- Exemplo: Usar =B5*(1+$B$6) ao inves de =B5*1,05

#### Prevencao de Erros
- Verificar todas as referencias de celulas
- Checar erros off-by-one em ranges
- Garantir formulas consistentes em todos os periodos de projecao
- Testar com edge cases (valores zero, negativos)

## CRITICO: Usar Formulas, NAO Valores Hardcoded

**Sempre usar formulas Excel ao inves de calcular em Python e hardcodar.**

### ERRADO - Hardcodar Valores
```python
total = df['Sales'].sum()
sheet['B10'] = total  # Hardcoda 5000
```

### CORRETO - Usar Formulas Excel
```python
sheet['B10'] = '=SUM(B2:B9)'
sheet['C5'] = '=(C4-C2)/C2'
sheet['D20'] = '=AVERAGE(D2:D19)'
```

## Workflow Comum

1. **Escolher ferramenta**: pandas para dados, openpyxl para formulas/formatacao
2. **Criar/Carregar**: Criar novo workbook ou carregar existente
3. **Modificar**: Adicionar/editar dados, formulas e formatacao
4. **Salvar**: Escrever no arquivo
5. **Recalcular formulas (SE USAR FORMULAS)**: Usar LibreOffice se disponivel
   ```bash
   python scripts/recalc.py output.xlsx
   ```
6. **Verificar erros**: Checar erros de formula e corrigir

## Leitura e Analise com pandas

```python
import pandas as pd

# Ler Excel
df = pd.read_excel('file.xlsx')  # Default: primeira aba
all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # Todas as abas como dict

# Analisar
df.head()      # Preview
df.info()      # Info de colunas
df.describe()  # Estatisticas

# Escrever
df.to_excel('output.xlsx', index=False)
```

## Criar Novo Excel com openpyxl

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()
sheet = wb.active

sheet['A1'] = 'Hello'
sheet.append(['Row', 'of', 'data'])
sheet['B2'] = '=SUM(A1:A10)'

sheet['A1'].font = Font(bold=True, color='FF0000')
sheet['A1'].fill = PatternFill('solid', start_color='FFFF00')
sheet['A1'].alignment = Alignment(horizontal='center')
sheet.column_dimensions['A'].width = 20

wb.save('output.xlsx')
```

## Editar Excel Existente

```python
from openpyxl import load_workbook

wb = load_workbook('existing.xlsx')
sheet = wb.active

sheet['A1'] = 'Novo Valor'
sheet.insert_rows(2)
sheet.delete_cols(3)

new_sheet = wb.create_sheet('NovaAba')
wb.save('modified.xlsx')
```

## Boas Praticas

### Selecao de Biblioteca
- **pandas**: Melhor para analise, operacoes em massa, export simples
- **openpyxl**: Melhor para formatacao complexa, formulas, features especificas do Excel

### openpyxl
- Indices de celula sao 1-based
- `data_only=True` para ler valores calculados
- **CUIDADO**: Se abrir com `data_only=True` e salvar, formulas sao perdidas permanentemente
- Arquivos grandes: Usar `read_only=True` ou `write_only=True`

### pandas
- Especificar tipos: `pd.read_excel('file.xlsx', dtype={'id': str})`
- Arquivos grandes: `pd.read_excel('file.xlsx', usecols=['A', 'C', 'E'])`
- Datas: `pd.read_excel('file.xlsx', parse_dates=['date_column'])`

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
