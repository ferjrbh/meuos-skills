---
name: irpf-ganho-capital
description: "Apura o ganho de capital de pessoa física na venda de imóveis, participações societárias fora da bolsa, criptoativos e outros bens — alíquotas progressivas de 15% a 22,5% (Lei nº 13.259/2016), isenções (imóvel único até R$ 440.000,00; reinvestimento em imóvel residencial em 180 dias; bens de pequeno valor até R$ 35.000,00/mês; imóvel adquirido até 1969), fatores de redução FR1 e FR2 (art. 40 da Lei nº 11.196/2005), percentual de redução do art. 18 da Lei nº 7.713/1988, GCAP e DARF 4600 até o último dia útil do mês seguinte. Separa cripto em exchange no Brasil (regra mensal) de cripto e aplicações no exterior (Lei nº 14.754/2023). Acionar quando o usuário disser \"vendi imóvel\", \"ganho de capital\", \"GCAP\", \"vendi quotas\", \"vendi cripto\", \"DARF 4600\", \"isenção 180 dias\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Ganho de capital da pessoa física

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Calcula o ganho de capital na alienação de bens e direitos pela pessoa física residente, verifica isenções e reduções, gera a memória para o GCAP (Programa de Apuração dos Ganhos de Capital) e o DARF 4600 com vencimento, e orienta o reflexo na declaração anual.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Venda, permuta com torna, doação ou dação de imóvel, veículo, quotas, ações fora da bolsa, cripto (no Brasil), ouro não ativo financeiro e outros bens.
- Não usar para ações, FII e derivativos negociados em bolsa (`irpf-investimentos-bolsa`) nem para aplicações financeiras no exterior (regra anual da Lei nº 14.754/2023, na `elaborar-irpf-completa`).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Escrituras e contratos ficam na pasta do cliente; nomes de arquivos sem CPF.

## Passo a passo (instruções para o agente de IA)

### 1. Alíquotas (art. 21 da Lei nº 8.981/1995, com redação da Lei nº 13.259/2016)
```
Parcela do ganho                       Alíquota (aplicada por faixa, como degraus)
até R$ 5.000.000,00                    15%
de R$ 5.000.000,01 a R$ 10.000.000,00  17,5%
de R$ 10.000.000,01 a R$ 30.000.000,00 20%
acima de R$ 30.000.000,00              22,5%
```
Vale para imóveis, veículos, **participações societárias e ações fora da bolsa** e criptoativos custodiados/negociados no Brasil. O DARF é o 4600, até o último dia útil do mês seguinte ao do recebimento (na venda a prazo, o imposto é proporcional a cada parcela recebida).

### 2. Isenções e reduções
```
1. Bens de pequeno valor: alienações do mês até R$ 35.000,00 (R$ 20.000,00 para ações
   negociadas em mercado de balcão), somando os bens da mesma natureza
   (art. 22 da Lei nº 9.250/1995, com redação da Lei nº 11.196/2005).
2. Único imóvel até R$ 440.000,00: o titular só possui aquele imóvel (qualquer tipo,
   urbano ou rural) e não fez outra alienação de imóvel, tributada ou não, nos últimos
   5 anos (art. 23 da Lei nº 9.250/1995).
3. Reinvestimento em 180 dias: venda de imóvel RESIDENCIAL e compra de imóvel RESIDENCIAL
   no Brasil em até 180 dias da celebração do contrato (o dia do contrato conta); parcial
   = isenção proporcional; corretagem paga não entra no valor a reinvestir; opção
   irretratável; 1 vez a cada 5 anos (art. 39 da Lei nº 11.196/2005). Vale também para quitar
   débito da aquisição a prazo de imóvel residencial já possuído (ver perguntas frequentes);
   não vale para construção nem compra de terreno (perguntas 576 e 577 do Perguntas e
   Respostas IRPF 2026).
4. Imóvel adquirido até 1969: ganho isento; adquirido de 1970 a 1988: percentual de
   redução por ano de aquisição (art. 18 da Lei nº 7.713/1988).
5. Fatores de redução para IMÓVEIS (qualquer data de aquisição) — art. 40 da Lei nº 11.196/2005:
   FR1 = 1 / 1,0060^m1  (m1 = meses de jan/1996, ou da aquisição se posterior, até nov/2005)
   FR2 = 1 / 1,0035^m2  (m2 = meses de dez/2005, ou da aquisição se posterior, até a alienação)
   Ganho tributável = ganho × (percentual do art. 18, se houver) × FR1 × FR2.
   O GCAP faz a contagem exata dos meses; usar o programa como conferência final.
```
**Não existe** isenção de ganho de capital para "pequeno imóvel rural até 50 ha": a Lei nº 9.393/1996 trata do ITR.

### 3. Criptoativos
- **Exchange ou custódia no Brasil**: se o total alienado no mês (todas as criptos, no Brasil e no exterior) passar de R$ 35.000,00, todo o ganho do mês é tributado pelas alíquotas progressivas, DARF 4600. Troca de uma cripto por outra também é alienação. Informar operações fora de exchange ou em exchange estrangeira pela Coleta Nacional (Instrução Normativa RFB nº 1.888/2019).
- **Exchange ou custódia no exterior, a partir de 2024**: aplicações financeiras no exterior pela Lei nº 14.754/2023 — tributação anual a 15% na declaração, sem a isenção de R$ 35.000,00.
- Fonte: Perguntas e Respostas IRPF 2026 (seção de criptoativos).

### 4. Entrevista mínima
```
Q1: Tipo do bem e valor de alienação (escritura, contrato, nota)?
Q2: Data e custo de aquisição (valor da declaração de bens; escritura; NF; custo médio)?
Q3: Benfeitorias e despesas com comprovante (ITBI, escritura, registro, corretagem paga na
    compra; benfeitorias com NF e informadas na declaração)?
Q4: Corretagem paga na venda?
Q5: Isenções possíveis: único imóvel? reinvestimento residencial? pequeno valor? aquisição até 1988?
Q6: Venda à vista ou a prazo (cronograma de recebimentos)?
```

### 5. Cálculo (Python)
```python
def meses(a_ano, a_mes, b_ano, b_mes):
    return max((b_ano - a_ano) * 12 + (b_mes - a_mes), 0)

def fatores_reducao(aq_ano, aq_mes, al_ano, al_mes):
    """FR1 e FR2 do art. 40 da Lei nº 11.196/2005 (aproximação; o GCAP é a referência)."""
    if (aq_ano, aq_mes) < (2005, 12):
        inicio1 = max((aq_ano, aq_mes), (1996, 1))
        fr1 = 1 / 1.0060 ** meses(*inicio1, 2005, 11)
        inicio2 = (2005, 12)
    else:
        fr1, inicio2 = 1.0, (aq_ano, aq_mes)
    fr2 = 1 / 1.0035 ** meses(*inicio2, al_ano, al_mes)
    return fr1, fr2

def ir_progressivo(ganho):
    faixas = [(5_000_000, 0.15), (10_000_000, 0.175), (30_000_000, 0.20), (float("inf"), 0.225)]
    ir, piso = 0.0, 0.0
    for teto, aliq in faixas:
        if ganho > piso:
            ir += (min(ganho, teto) - piso) * aliq
        piso = teto
    return ir

# Exemplo fictício: imóvel comprado em mar/2010 por R$ 200.000 (+ R$ 5.000 de ITBI/escritura
# + R$ 30.000 de benfeitorias com NF), vendido em jun/2026 por R$ 600.000 (corretagem R$ 18.000)
custo = 200_000 + 5_000 + 30_000
ganho = (600_000 - 18_000) - custo                 # 347.000
fr1, fr2 = fatores_reducao(2010, 3, 2026, 6)       # FR1 = 1 (compra após 2005); FR2 ≈ 0,506
tributavel = ganho * fr1 * fr2                     # ≈ 175.566
print(f"Ganho tributável ≈ R$ {tributavel:,.2f} | IR ≈ R$ {ir_progressivo(tributavel):,.2f} (DARF 4600)")
```

### 6. Custo médio (quotas, ações fora da bolsa, cripto)
```
Compra 1: 100 × R$ 10 = R$ 1.000 | Compra 2: 200 × R$ 13 = R$ 2.600
Estoque 300 unidades, custo R$ 3.600 → custo médio R$ 12
Venda 100 × R$ 18 = R$ 1.800 → custo R$ 1.200 → ganho R$ 600 → IR 15% = R$ 90
(se o total alienado no mês for acima do limite de isenção aplicável)
```

### 7. Entregável obrigatório
a) Memória de cálculo:
```
BEM: __   Adquirido em __/__/__ por R$ __
+ Despesas de aquisição (ITBI, escritura, registro): R$ __
+ Benfeitorias com comprovante: R$ __
= CUSTO: R$ __
Alienado em __/__/__ por R$ __   (−) Corretagem paga: R$ __   = VALOR LÍQUIDO: R$ __
GANHO: R$ __
Reduções: art. 18 da Lei nº 7.713/1988 __% | FR1 __ | FR2 __
GANHO TRIBUTÁVEL: R$ __   IR (faixas da Lei nº 13.259/2016): R$ __
ISENÇÃO? [ ] único imóvel até R$ 440.000 [ ] reinvestimento 180 dias [ ] pequeno valor [ ] até 1969
DARF 4600: R$ __   Vencimento: último dia útil de __/__
```
b) Lançamento no GCAP do ano.
c) Reflexo na declaração: baixa do bem em Bens e Direitos; importação do GCAP; valor isento na ficha própria.
d) Comprovantes arquivados.

## Erros comuns / pontos de atenção
- Atrasar o DARF: multa de mora de 0,33% ao dia, limitada a 20%, mais Selic (art. 61 da Lei nº 9.430/1996); se apurado em fiscalização, multa de ofício de 75% (art. 44, I, da mesma lei).
- Benfeitoria sem comprovante ou não declarada: não entra no custo.
- Isenção do imóvel único já usada (qualquer alienação de imóvel) nos últimos 5 anos.
- Reinvestir em imóvel comercial (só residencial).
- Aplicar 15% fixo em venda de quotas: valem as faixas progressivas.
- Aplicar FR1/FR2 só a imóveis "pré-2017": os fatores valem para qualquer imóvel.
- Cripto: não somar todas as alienações do mês para o limite de R$ 35.000,00.

## Casos de borda
- **Imóvel financiado**: ganho calculado pelo valor total de venda, não pelo líquido recebido.
- **Permuta sem torna**: não há ganho; com torna, ganho proporcional à torna.
- **Doação ou herança**: o doador/espólio pode transferir pelo valor declarado (sem ganho) ou de mercado (a diferença é ganho de capital do doador/espólio); o custo do donatário/herdeiro é o valor da transferência (art. 23 da Lei nº 9.532/1997).
- **Alta renda (IRPF 2027)**: ganhos de capital fora da bolsa ficam FORA da base do IRPFM (art. 16-A, § 1º, da Lei nº 9.250/1995, incluído pela Lei nº 15.270/2025).

## Perguntas que o usuário costuma fazer
- **"Vendi minha única casa por R$ 400 mil. Pago imposto?"** Não, se não vendeu outro imóvel nos últimos 5 anos. Mesmo isento, informar no GCAP/declaração.
- **"Posso usar o dinheiro para quitar o financiamento de outro imóvel?"** Sim, dentro dos 180 dias, se for imóvel RESIDENCIAL já possuído e a dívida for da própria aquisição a prazo ou à prestação desse imóvel (inclusive o financiamento ligado ao instrumento de compra) — art. 2º, § 10, III, da Instrução Normativa SRF nº 599/2005 e Nota SEI nº 48/2018/PGACET/PGFN-MF. Não vale para quitar empréstimo sem ligação com o instrumento de aquisição (ex.: empréstimo de familiar usado para comprar à vista) — pergunta 581 do Perguntas e Respostas IRPF 2026 e Solução de Consulta Cosit nº 14/2025.

## Quando escalar
- Declaração anual → `elaborar-irpf-completa`
- Malha → `diagnosticar-malha-fina-pf`
- Bolsa → `irpf-investimentos-bolsa`

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei nº 8.981/1995 — art. 21 (ganho de capital), com redação da Lei nº 13.259/2016 (alíquotas progressivas).
- Lei nº 9.250/1995 — art. 22 (bens de pequeno valor) e art. 23 (imóvel único).
- Lei nº 11.196/2005 — art. 39 (reinvestimento em 180 dias) e art. 40 (FR1 e FR2).
- Lei nº 7.713/1988 — art. 18 (redução para imóveis adquiridos até 1988).
- Lei nº 9.532/1997 — art. 23 (doação e herança).
- Lei nº 14.754/2023 — aplicações financeiras e criptoativos no exterior.
- Lei nº 9.430/1996 — arts. 44 e 61 (multas).
- Lei nº 15.270/2025 — IRPFM (art. 16-A da Lei nº 9.250/1995).
- Instrução Normativa SRF nº 84/2001 — apuração do ganho de capital.
- Instrução Normativa SRF nº 599/2005 — art. 2º, § 10 (isenção do art. 39 da Lei nº 11.196/2005, inclusive quitação de débito do imóvel residencial já possuído).
- Perguntas e Respostas IRPF 2026 (Receita Federal) — perguntas 573 a 581 (ganho de capital e isenções) e seção de criptoativos.
- Instrução Normativa RFB nº 1.888/2019 — informações de operações com criptoativos.
- Decreto nº 9.580/2018 (RIR/2018) — regulamento do imposto de renda.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
