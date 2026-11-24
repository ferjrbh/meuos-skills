---
name: valuation-pme
description: "Estima o valor de uma pequena ou média empresa por fluxo de caixa descontado (DCF — FCFF/FCFE), múltiplos de mercado (EV/EBITDA, EV/Receita, P/L) e abordagem patrimonial (piso). Ajusta o EBITDA (Quality of Earnings), projeta 5 anos, calcula o WACC com prêmio de risco Brasil e de tamanho, valor terminal (Gordon ou múltiplo de saída) e sensibilidade WACC × g. Entrega faixa de valor (mínimo, médio, máximo) e relatório para assinatura. Acionar quando o usuário disser \"quanto vale a empresa\", \"valuation\", \"avaliar empresa\", \"preço de venda da empresa\", \"entrada de investidor\", \"sucessão\", \"partilha em divórcio\", \"apuração de haveres\", \"combinação de negócios CPC 15\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Valuation de PME

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Organiza a avaliação econômica de uma PME por três abordagens (DCF, múltiplos e patrimonial), com EBITDA ajustado, premissas documentadas e análise de sensibilidade. O resultado é uma faixa de valor defensável para negociação, captação, sucessão ou partilha, para revisão e assinatura do profissional responsável.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.
> Em **apuração de haveres judicial** (saída de sócio, morte, divórcio), o critério pode ser imposto pelo contrato social ou pela lei (art. 606 do CPC — Lei nº 13.105/2015), e não pelo DCF. Ver "Casos de borda".

## Quando usar
- Cliente vendendo a empresa ou captando investidor.
- Sucessão, entrada/saída de sócio, partilha em divórcio.
- Combinação de negócios (CPC 15) e alocação do preço pago.
- Trabalho típico de 2 a 6 semanas.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Em partilha e sucessão, os dados da família são especialmente sensíveis.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Toda premissa de mercado (taxa livre de risco, prêmios, múltiplos, descontos) precisa de fonte e data. Sem fonte, não usar o número: pedir a fonte ao usuário ou buscá-la em base pública citável e registrar no relatório.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
P1: DREs e balanços dos últimos 3 a 5 anos? Auditados?
P2: Plano de negócios ou projeção de 5 a 10 anos?
P3: Investimentos (CAPEX) históricos e previstos?
P4: Estrutura de capital (dívidas, patrimônio líquido)? Dívidas fora do balanço (avais, garantias)?
P5: Particularidades: dependência de poucos clientes, concorrência, regulação, dependência do sócio?
P6: Finalidade: venda, captação, sucessão, partilha, apuração de haveres? Há cláusula no contrato
    social sobre critério de avaliação?
P7: Regime tributário (Simples, Presumido, Real)? Muda a taxa de imposto do modelo.
```

### 2. EBITDA ajustado (Quality of Earnings) — sempre
```
EBITDA reportado
+ despesas não recorrentes (multas, indenizações, custos da operação de venda)
− receitas não recorrentes (venda de ativo, ganho cambial não operacional)
± pró-labore ajustado a valor de mercado
+ despesas pessoais dos sócios lançadas na empresa
± partes relacionadas a valor de mercado
± provisões a regularizar (PCLD, contingências)
= EBITDA AJUSTADO
```

### 3. Estrutura do DCF (FCFF — fluxo de caixa livre para a firma)
```
EBITDA
(−) depreciação e amortização (D&A)
= EBIT
(−) IR/CSLL sobre o EBIT (taxa do regime da empresa: 34% no Lucro Real com adicional;
    no Presumido e no Simples, usar a carga efetiva projetada)
= NOPAT
(+) D&A
(−) CAPEX
(−) ΔNWC (variação do capital de giro)
= FCFF

EV = Σ FCFF_t / (1+WACC)^t + VT / (1+WACC)^n
Valor do patrimônio (equity) = EV − dívida líquida (inclui dívidas fora do balanço e passivos da DD)
```
Lei nº 15.270/2025: dividendos acima de R$ 50 mil por mês, por pessoa física, têm retenção de 10%, e há o IRPFM para renda acima de R$ 600 mil por ano. Isso não muda o FCFF da empresa, mas muda o valor líquido que chega ao sócio — mostrar à parte quando a finalidade for venda ou sucessão.

### 4. WACC
```
WACC = (E/V) × Ke + (D/V) × Kd × (1 − T)

Ke (custo do capital próprio) = Rf + β × (Rm − Rf) + prêmio de risco país + prêmio de tamanho
Kd (custo da dívida)          = taxa contratada ANTES do imposto
                                (o benefício fiscal entra uma vez só, pelo (1 − T) do WACC;
                                 T = 34% só no Lucro Real; no Presumido/Simples os juros
                                 não reduzem o imposto da mesma forma → usar T próximo de zero)

Coerência de moeda (escolher UMA das formas e não misturar):
(a) Em dólar: Rf = título do Tesouro americano + prêmio de risco país; converter o resultado para
    reais pela diferença de inflação esperada.
(b) Em reais: Rf = título público brasileiro (por exemplo, NTN-B + inflação esperada). Nesse caso
    o risco país JÁ está na taxa: não somar o prêmio Brasil de novo.

Referências que precisam de fonte e data na data-base:
- Rf, prêmio de mercado e prêmio país: buscar os valores vigentes na data-base, com fonte e
  data (Tesouro Nacional para os títulos públicos, Banco Central — Relatório Focus — para a
  inflação esperada, bases públicas de Damodaran para prêmios e betas). Não usar número de
  memória.
- β setorial desalavancado e realavancado pela estrutura da empresa
- Prêmio de tamanho para PME: usar estudo publicado e citado no relatório, justificando o
  percentual escolhido
```

### 5. Capital de giro (NWC)
```
NWC = clientes + estoques − fornecedores (operacional, sem caixa e dívida)
ΔNWC = NWC_t − NWC_(t−1)
```
Crescer a receita exige mais capital de giro, o que reduz o FCFF.

### 6. Cálculo (Python)
Salvar como `.py` e rodar com `python -I -X utf8 arquivo.py`. Valores do exemplo são fictícios.

```python
def dcf(receita_inicial, crescimento, margem_ebitda, capex_pct_rec, da_pct_rec,
        ir_pct, wacc, g, nwc_pct_rec=0.15, anos=5):
    assert wacc > g, "g precisa ser menor que o WACC"
    fcffs, rec_ant = [], receita_inicial
    nwc_ant = receita_inicial * nwc_pct_rec
    for t in range(1, anos + 1):
        rec = rec_ant * (1 + crescimento)
        ebitda = rec * margem_ebitda
        da = rec * da_pct_rec
        nopat = (ebitda - da) * (1 - ir_pct)
        capex = rec * capex_pct_rec
        nwc = rec * nwc_pct_rec
        delta_nwc = nwc - nwc_ant              # variação, não o saldo
        fcffs.append(nopat + da - capex - delta_nwc)
        rec_ant, nwc_ant = rec, nwc
    vt = fcffs[-1] * (1 + g) / (wacc - g)      # Gordon
    pv_fcff = sum(f / (1 + wacc) ** t for t, f in enumerate(fcffs, 1))
    pv_vt = vt / (1 + wacc) ** anos
    return pv_fcff + pv_vt, fcffs, vt, pv_vt

ev, fcffs, vt, pv_vt = dcf(10_000_000, 0.10, 0.20, 0.03, 0.02, 0.34, 0.15, 0.04)
print("EV:", round(ev, 2), "| peso do VT no EV:", f"{pv_vt/ev:.0%}")
print("FCFF ano 1-5:", [round(f) for f in fcffs])

# Sensibilidade WACC × g
for g in (0.03, 0.04, 0.05):
    print(g, [round(dcf(10_000_000, 0.10, 0.20, 0.03, 0.02, 0.34, w, g)[0]) for w in (0.12, 0.14, 0.16, 0.18)])
```
Se o valor terminal responder pela maior parte do EV, revisar as premissas de longo prazo (crescimento g, margem e CAPEX da perpetuidade) e mostrar o peso do VT no relatório.

### 7. Múltiplos de mercado
```
O múltiplo EV/EBITDA vem de base de transações ou de companhias comparáveis, com fonte e
data na data-base (nunca de faixa de memória). Fatores que costumam afastar o múltiplo do
setor e devem ser comentados no laudo:
Setor             O que pesa no múltiplo
Varejo            Margem baixa; sazonalidade
Indústria         Intensidade de capital
SaaS / tecnologia Receita recorrente (ARR)
Serviços B2B      Dependência de pessoas
Saúde             Regulação
Construção        Ciclo de obras

EV/Receita: empresas com prejuízo ou margem em formação (SaaS, scale-ups)
P/L: empresas estáveis e listadas
EV/cliente (telecom, SaaS); EV/loja (varejo)
```
Múltiplos de companhias abertas aplicados a PME pedem desconto de liquidez (DLOM) e, para participação minoritária, desconto de falta de controle (DLOC). Os percentuais vêm de estudo publicado, citado no laudo, e precisam ser justificados para o caso.

### 8. Entregáveis
**a) Modelo DCF**
```
                  Ano 1   Ano 2   Ano 3   Ano 4   Ano 5   VT
Receita líquida   ____    ____    ____    ____    ____    —
Crescimento %     __%     __%     __%     __%     __%     g __%
EBITDA            ____    ____    ____    ____    ____
Margem %          __%     __%     __%     __%     __%
D&A               ____    ____    ____    ____    ____
EBIT              ____    ____    ____    ____    ____
IR/CSLL (__%)     ____    ____    ____    ____    ____
NOPAT             ____    ____    ____    ____    ____
+ D&A             ____    ____    ____    ____    ____
− CAPEX           ____    ____    ____    ____    ____
− ΔNWC            ____    ____    ____    ____    ____
FCFF              ____    ____    ____    ____    ____    ____

WACC __% | g __% | horizonte 5 anos
VP(FCFF) ____ | VP(VT) ____ | EV ____ | dívida líquida ____ | equity ____
```
**b) Sensibilidade WACC × g** (tabela).
**c) Faixa por abordagem**
```
Abordagem          Mín       Médio     Máx
DCF                R$ ____   R$ ____   R$ ____
Múltiplos EBITDA   R$ ____   R$ ____   R$ ____
Patrimonial        R$ ____   R$ ____   R$ ____

FAIXA RECOMENDADA: R$ ____ a R$ ____
PREÇO-ALVO PARA NEGOCIAÇÃO: R$ ____
MÍNIMO ACEITÁVEL: R$ ____
```
**d) Memória de cálculo** do modelo completo.
**e) Relatório final** assinado pelo responsável técnico.

## Erros comuns / pontos de atenção
- EBITDA sem ajustes (itens não recorrentes distorcem).
- Descontar o imposto da dívida duas vezes (Kd já líquido e de novo × (1 − T)).
- Somar prêmio Brasil sobre taxa livre de risco em reais (dupla contagem).
- WACC genérico, sem ajuste de tamanho e risco da PME.
- g igual ou maior que o WACC, ou acima do crescimento nominal de longo prazo da economia.
- Tratar o saldo do capital de giro como se fosse a variação.
- Projeção otimista sem base no histórico.
- Múltiplos de companhias abertas sem desconto de liquidez.
- Esquecer dívidas fora do balanço (avais, garantias, contingências da DD).
- Usar 34% de IR/CSLL para empresa do Presumido ou do Simples.

**Casos de borda**
- **Empresa em estágio inicial / sem receita**: DCF pouco útil; usar EV/Receita ou métodos de pre-money.
- **Holding patrimonial**: abordagem patrimonial com imóveis a valor de mercado (piso).
- **Empresa em descontinuidade**: valor de liquidação (ativos a valor realizável − passivos).
- **Participação minoritária**: aplicar DLOC.
- **Apuração de haveres** (sócio que sai, falece ou é excluído): vale o critério do contrato social; se omisso, o juiz define pelo valor patrimonial apurado em **balanço de determinação** na data da resolução (art. 606 do CPC — Lei nº 13.105/2015; art. 1.031 do Código Civil — Lei nº 10.406/2002). DCF pode servir de apoio, não de critério obrigatório.
- **Combinação de negócios** (CPC 15): o valuation alimenta a alocação do preço (ativos, intangíveis identificáveis pelo CPC 04, ágio por rentabilidade futura).

## Perguntas que o usuário costuma fazer
- **"Quanto vale: 5 vezes o EBITDA?"** Múltiplo é referência de mercado; o valor final cruza DCF, múltiplos e patrimonial.
- **"No divórcio, uso o DCF?"** Depende do acordo ou da decisão judicial; em apuração de haveres, a regra legal é o balanço de determinação, salvo cláusula contratual.
- **"A nova tributação de dividendos reduz o valor?"** Não o EV da empresa, mas o líquido que chega ao sócio vendedor ou herdeiro.

## Formato de entrega
- Cálculos, apurações e conciliações: sempre planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): sempre documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- CPC 15 (NBC TG 15) — combinação de negócios.
- CPC 46 (NBC TG 46) — mensuração do valor justo (hierarquia de dados e técnicas de avaliação).
- CPC 04 (NBC TG 04) — ativo intangível (na alocação do preço).
- CPC 01 (NBC TG 01) — redução ao valor recuperável (impairment).
- Lei nº 13.105/2015 (CPC — Código de Processo Civil) — art. 606 (critério de apuração de haveres).
- Lei nº 10.406/2002 (Código Civil) — art. 1.031 (liquidação da quota do sócio).
- Lei nº 15.270/2025 — tributação de dividendos e IRPFM.
- Lei nº 9.249/1995 e Lei nº 9.430/1996 — alíquotas de IRPJ/CSLL usadas no NOPAT.
- Referência técnica: Damodaran (custo de capital e prêmio de risco país), com fonte e data das planilhas usadas.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
