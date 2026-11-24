---
name: irpf-aluguel-carne-leao
description: "Calcula o carnê-leão (recolhimento mensal obrigatório — art. 8º da Lei nº 7.713/1988), DARF código 0190, sobre rendimentos recebidos de pessoa física ou do exterior sem retenção na fonte: aluguel pago por PF, autônomo que presta serviço a PF, rendimentos do exterior (pensão alimentícia recebida não entra — ADI 5.422). Aplica a tabela mensal de 2026, as exclusões do aluguel (impostos e taxas do imóvel, condomínio, despesa de cobrança/administração), deduções (dependente R$ 189,59, pensão, INSS, livro-caixa) ou desconto simplificado mensal (R$ 607,20) e a redução da Lei nº 15.270/2025 (imposto zero até R$ 5.000,00/mês; redução parcial até R$ 7.350,00). Acionar quando o usuário disser \"carnê-leão\", \"aluguel de pessoa física\", \"recebo de PF\", \"autônomo para pessoa física\", \"rendimento do exterior\", \"DARF 0190\". Não confundir com IRRF retido por PJ."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Carnê-leão (aluguel e demais rendimentos de PF e do exterior)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Apura, mês a mês, o carnê-leão devido pelo contribuinte pessoa física residente que recebe de pessoa física ou do exterior. Entrega o cálculo, o DARF 0190 com vencimento e a orientação de lançamento no Carnê-Leão Web, que alimenta a declaração anual.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Locador PF com locatário PF.
- Profissional autônomo/liberal que recebe de PF.
- Rendimentos do trabalho ou de aluguel recebidos do exterior.
- Não usar quando o pagador é PJ: a PJ retém o IRRF (skill/agente `calculo-irrf-folha`; aluguel pago por PJ a PF = código 3208).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Nome de arquivos de memória sem CPF: `carne_leao_<CLIENTE>_<AAAAMM>.xlsx`.

## Passo a passo (instruções para o agente de IA)

### 1. Parâmetros 2026
```
TABELA PROGRESSIVA MENSAL (vigente desde maio/2025; não alterada pela Lei nº 15.270/2025)
Base mensal (R$)             Alíquota   Parcela a deduzir (R$)
até 2.428,80                  0%           0,00
2.428,81 a 2.826,65           7,5%       182,16
2.826,66 a 3.751,05          15%         394,16
3.751,06 a 4.664,68          22,5%       675,49
acima de 4.664,68            27,5%       908,73

Dependente: R$ 189,59/mês | Desconto simplificado mensal: R$ 607,20 (opcional, substitui
as deduções legais do mês)

REDUÇÃO DA LEI Nº 15.270/2025 (art. 3º-A da Lei nº 9.250/1995), aplicada DEPOIS da tabela,
em função dos RENDIMENTOS TRIBUTÁVEIS do mês (não da base):
   até R$ 5.000,00               → imposto zerado (redução de até R$ 312,89)
   R$ 5.000,01 a R$ 7.350,00     → redução = 978,62 − 0,133145 × rendimentos (limitada ao imposto)
   acima de R$ 7.350,00          → sem redução
A Receita informa que a redução vale também para o carnê-leão (rendimento tributável de até
R$ 7.350,00 — Anexo X da Instrução Normativa RFB nº 1.500/2014), e o Carnê-Leão Web a aplica.
No aluguel, as exclusões do passo 4 (IPTU, condomínio, administração) saem do valor recebido
antes do cálculo; por isso o cálculo abaixo mede a faixa da redução pelo aluguel APÓS as
exclusões. Como a Receita não detalha esse ponto no Perguntas e Respostas, conferir o
resultado do mês no Carnê-Leão Web, que é o sistema oficial: se divergir, usar o valor do
sistema e anotar a diferença na memória de cálculo.

DARF código 0190 — vencimento: último dia útil do mês seguinte ao do recebimento.
DARF abaixo de R$ 10,00: não se emite; somar ao(s) mês(es) seguinte(s).
```
Fontes: art. 3º-A da Lei nº 9.250/1995 (incluído pela Lei nº 15.270/2025); Perguntas e Respostas IRPF 2026, perguntas 266 e 267.

### 2. Quando se aplica
```
PAGADOR PF ......................... carnê-leão (o contribuinte recolhe)
PAGADOR NO EXTERIOR ................ carnê-leão (com compensação do imposto pago lá fora,
                                      limitada ao imposto brasileiro — tratados ou reciprocidade)
PAGADOR PJ ......................... IRRF na fonte pela PJ — NÃO é carnê-leão
```
Observação: rendimentos de aplicações financeiras no exterior seguem a Lei nº 14.754/2023 (tributação anual na declaração), não o carnê-leão.

### 3. Entrevista mínima
```
Q1: Competência, valor recebido e quem pagou (PF, exterior ou PJ)?
Q2: Tipo: aluguel, serviço autônomo, exterior? (pensão alimentícia recebida não entra)
Q3 (aluguel): o locador pagou IPTU, condomínio, taxa de administração da imobiliária?
Q4: Dependentes (com CPF)? Pensão alimentícia paga (decisão judicial ou escritura)?
Q5: Contribuição ao INSS paga como contribuinte individual no mês?
Q6 (autônomo): despesas de livro-caixa do mês?
Q7 (exterior): imposto pago no exterior e país (há acordo ou reciprocidade)?
```

### 4. Aluguel — exclusões permitidas (quando o encargo foi só do locador)
- Impostos, taxas e emolumentos incidentes sobre o imóvel (ex.: IPTU, taxa de lixo do próprio imóvel).
- Aluguel pago pela locação do imóvel sublocado.
- Despesas pagas para cobrança ou recebimento (ex.: taxa de administração da imobiliária, comissão de plataforma digital em locação por temporada).
- Despesas de condomínio.
- **Não** excluem: reparos, benfeitorias, taxa de limpeza ou estacionamento cobrada do locatário, taxa de associação de proprietários.

Base: art. 14 da Lei nº 7.739/1989 e arts. 30 e 31 da Instrução Normativa RFB nº 1.500/2014 (pergunta 445 do Perguntas e Respostas IRPF 2026).

### 5. Cálculo (Python)
```python
FAIXAS = [(2_428.80, 0.0, 0.0), (2_826.65, 0.075, 182.16), (3_751.05, 0.15, 394.16),
          (4_664.68, 0.225, 675.49), (float("inf"), 0.275, 908.73)]

def tabela(base):
    for teto, aliq, deduz in FAIXAS:
        if base <= teto:
            return max(base * aliq - deduz, 0.0)

def carne_leao(recebido, exclusoes=0.0, dependentes=0, pensao=0.0, inss=0.0,
               livro_caixa=0.0, simplificado=False, ir_exterior=0.0):
    rend = recebido - exclusoes                      # rendimento tributável do mês
    ded = 607.20 if simplificado else dependentes * 189.59 + pensao + inss + livro_caixa
    base = max(rend - ded, 0.0)
    ir = tabela(base)
    # Redução da Lei nº 15.270/2025 — pelo rendimento, não pela base
    if rend <= 5_000:
        red = ir
    elif rend <= 7_350:
        red = min(max(978.62 - 0.133145 * rend, 0.0), ir)
    else:
        red = 0.0
    devido = ir - red
    compensa = min(ir_exterior, devido)              # imposto pago no exterior
    return dict(rendimento=round(rend, 2), base=round(base, 2), tabela=round(ir, 2),
                reducao=round(red, 2), darf_0190=round(devido - compensa, 2))

# Exemplo 1 — aluguel R$ 5.000, IPTU R$ 200, condomínio R$ 600, 2 dependentes
print(carne_leao(5_000, 800, 2))      # rendimento 4.200 → tabela 184,19 → redução 184,19 → DARF 0,00
# Exemplo 2 — aluguel R$ 7.000, sem exclusões: comparar deduções legais × simplificado
print(carne_leao(7_000))                     # DARF 969,67
print(carne_leao(7_000, simplificado=True))  # DARF 802,69 → escolher o menor
```

### 6. Carnê-Leão Web
Fica no e-CAC / Meu Imposto de Renda (Receita Federal). O contribuinte — ou o contador com procuração eletrônica — lança os rendimentos e as deduções do mês, emite o DARF 0190 e, na declaração anual, importa os dados. Não é sistema do INSS.

### 7. Entregável obrigatório
**a) Memória mensal**
```
LOCADOR: CLIENTE EXEMPLO   Locatário: PF   Imóvel: __   Competência: __/2026

Aluguel recebido ..................................... 5.000,00
(−) IPTU (parcela do mês, paga pelo locador) .......... 200,00
(−) Condomínio pago pelo locador ...................... 600,00
(−) Taxa de administração ............................... 0,00
= RENDIMENTO TRIBUTÁVEL ............................... 4.200,00
(−) Dependentes (2 × 189,59) ........................... 379,18
= BASE ................................................ 3.820,82
Tabela: 3.820,82 × 22,5% − 675,49 ...................... 184,19
(−) Redução Lei nº 15.270/2025 (rendimento até 5.000) .. 184,19
= CARNÊ-LEÃO DEVIDO ...................................... 0,00
DARF 0190: não há valor a recolher
```
b) Lançamento no Carnê-Leão Web (cliente, ou contador com procuração).
c) DARF 0190 com valor e vencimento (quando houver imposto).
d) Orientação anual: importar o Carnê-Leão Web na declaração.
e) Checklist mensal:
```
[ ] Pagador é PF ou exterior (não PJ)
[ ] Exclusões do aluguel com comprovante e ônus do locador
[ ] Deduções legais × desconto simplificado comparados
[ ] Redução da Lei nº 15.270/2025 aplicada pelo rendimento
[ ] DARF 0190 gerado e pago (ou acumulado se < R$ 10,00)
[ ] Carnê-Leão Web atualizado
```
f) Checklist anual:
```
[ ] Todos os meses lançados
[ ] Importação na declaração
[ ] Compensação do imposto pago no exterior conferida
[ ] Ajuste anual: o carnê-leão é antecipação; a soma com outras rendas pode gerar imposto
    a pagar na declaração
```

## Erros comuns / pontos de atenção
- Não excluir IPTU/condomínio pagos pelo locador.
- Achar que a imobiliária "retém" o carnê-leão: ela não retém IR quando o locatário é PF. O locador recolhe o carnê-leão sobre o aluguel menos a taxa de administração e demais exclusões. Se o locatário for PJ, a PJ retém o IRRF.
- Atraso no DARF: multa de mora de 0,33% ao dia, limitada a 20%, mais Selic e 1% no mês do pagamento (art. 61 da Lei nº 9.430/1996). Se o fisco apurar carnê-leão não recolhido, cabe multa isolada de 50% sobre o valor mensal não pago (art. 44, II, "a", da Lei nº 9.430/1996).
- Rendimento abaixo da faixa isenta ou zerado pela redução: lançar mesmo assim, porque soma no ajuste anual.
- Imposto pago no exterior maior que o brasileiro: compensação limitada ao imposto brasileiro.
- INSS do autônomo: quem presta a PF recolhe como contribuinte individual (20% no plano normal ou 11% no plano simplificado, sobre o salário mínimo) — conferir antes de deduzir.

## Casos de borda
- **Pensão alimentícia recebida**: NÃO entra no carnê-leão nem é tributada na declaração anual. O STF afastou a incidência de IR sobre a pensão alimentícia decorrente do direito de família (ADI 5.422, transitada em julgado em 05/11/2022). Na declaração, informar em "Rendimentos Isentos e Não Tributáveis", tipo "26 – Outros", com a natureza do rendimento. Quem declarou como tributável de 2020 a 2022 pode retificar (pergunta 223 do Perguntas e Respostas IRPF 2026; Solução de Consulta Cosit nº 165/2024).
- **Aluguel de imóvel rural a PF**: carnê-leão, salvo se for parceria rural (atividade rural).
- **Residente que trabalha para empresa ou plataforma no exterior**: carnê-leão sobre cada recebimento. Conversão: a moeda estrangeira vira dólar pelo valor fixado pela autoridade monetária do país de origem na data do recebimento e, depois, real pelo dólar de compra do Banco Central do último dia útil da primeira quinzena do mês anterior ao do recebimento (pergunta 266 do Perguntas e Respostas IRPF 2026).
- **Locação por temporada (plataformas)**: comissão da plataforma pode ser excluída.

## Perguntas que o usuário costuma fazer
- **"Recebo R$ 4.500 de aluguel. Pago carnê-leão em 2026?"** Pela redução da Lei nº 15.270/2025, o imposto mensal fica zerado até R$ 5.000,00 de rendimento; lance no Carnê-Leão Web mesmo assim.
- **"Posso usar o desconto simplificado no carnê-leão?"** Sim, o desconto simplificado mensal de R$ 607,20 substitui as deduções legais do mês; compare e use o melhor.
- **"Se no mês não deu imposto, no ano também não dá?"** Não necessariamente: no ajuste anual todas as rendas se somam.

## Quando escalar
- Declaração anual → `elaborar-irpf-completa`
- Malha → `diagnosticar-malha-fina-pf`
- Venda do imóvel locado → `irpf-ganho-capital`
- Pagador PJ → `calculo-irrf-folha`

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei nº 7.713/1988 — art. 8º (carnê-leão).
- Lei nº 9.250/1995 — art. 4º (deduções mensais) e art. 3º-A (redução mensal, incluído pela Lei nº 15.270/2025).
- Lei nº 15.270/2025 — redução do imposto a partir de janeiro/2026.
- Lei nº 7.739/1989 — art. 14 (exclusões do aluguel).
- Lei nº 9.430/1996 — art. 44, II, "a" (multa isolada) e art. 61 (multa e juros de mora).
- Instrução Normativa RFB nº 1.500/2014 — arts. 30 e 31 (exclusões do aluguel) e regras do carnê-leão.
- Decreto nº 9.580/2018 (RIR/2018) — regulamento do imposto de renda.
- STF, ADI 5.422 (trânsito em julgado em 05/11/2022) — pensão alimentícia não tributável; Solução de Consulta Cosit nº 165/2024.
- Perguntas e Respostas IRPF 2026 (Receita Federal) — perguntas 223 (pensão), 266 e 267 (carnê-leão) e 445 (exclusões do aluguel).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
