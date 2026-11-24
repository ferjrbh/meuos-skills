---
name: irpf-investimentos-bolsa
description: "Apura o IR mensal da pessoa física em renda variável na B3 — operações comuns com ações (15%, isenção se as vendas de ações no mercado à vista do mês forem até R$ 20.000,00), day trade (20%, sem isenção), FII e Fiagro (venda de cota a 20%; rendimento isento só com 100+ cotistas, negociação exclusiva em bolsa e cotista com menos de 10%), ETF, BDR, opções e futuros (sem a isenção de R$ 20.000,00). Compensa prejuízos por categoria, desconta o IRRF (\"dedo-duro\") e gera DARF 6015 até o último dia útil do mês seguinte. Indica quando cripto vai para `irpf-ganho-capital` e o que muda no IRPF 2027 (IRPFM). Acionar quando o usuário disser \"ações\", \"B3\", \"day trade\", \"swing trade\", \"FII\", \"ETF\", \"BDR\", \"DARF 6015\", \"nota de corretagem\", \"prejuízo a compensar\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# IR sobre investimentos em bolsa (renda variável)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Lê as notas de corretagem e apura, mês a mês, o imposto de renda da pessoa física em operações na bolsa, separando operações comuns e day trade, controlando custo médio e prejuízos acumulados, e gerando o DARF 6015 e a planilha anual para a declaração.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Cliente PF com operações na B3 (ações, FII, Fiagro, ETF, BDR, opções, futuros).
- Revisão de DARFs de renda variável em atraso.
- Não usar para cripto (`irpf-ganho-capital`), ações vendidas fora da bolsa (`irpf-ganho-capital`) nem aplicações no exterior (Lei nº 14.754/2023, na `elaborar-irpf-completa`).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Não pedir senha da corretora; trabalhar com notas e informes exportados pelo cliente.
- Planilha anual sem CPF no nome: `renda_variavel_<CLIENTE>_<ANO>.xlsx`.

## Passo a passo (instruções para o agente de IA)

### 1. Tabela de tributação
```
Tipo                              IR      Isenção                         IRRF na fonte        DARF
Ações — operações comuns          15%     vendas de AÇÕES no mercado à    0,005% sobre vendas  6015
  (mercado à vista)                       vista do mês até R$ 20.000,00
Day trade (qualquer ativo)        20%     nenhuma                         1% sobre o resultado 6015
FII / Fiagro — venda de cota      20%     nenhuma                         0,005%               6015
FII / Fiagro — rendimento         isento se: cotas negociadas exclusivamente em bolsa/balcão
  distribuído                     organizado, fundo com no mínimo 100 cotistas, cotista com
                                  menos de 10% das cotas/rendimentos e cotas de pessoas ligadas
                                  abaixo de 30%; caso contrário, IRRF de 20%
ETF de renda variável             15% (comum) / 20% (day trade), sem isenção            6015
ETF de renda fixa                 regra própria (tributação na fonte por prazo médio)
BDR                               15% / 20%, sem isenção                                6015
Opções, termo, futuros            15% / 20%, sem isenção                                6015
Tesouro Direto, CDB, debêntures   tabela regressiva 22,5% a 15%, retido na fonte
LCI, LCA, CRI, CRA, poupança      isentos para PF

DARF 6015: vencimento no último dia útil do mês seguinte; valor abaixo de R$ 10,00 acumula.
O IRRF retido ("dedo-duro") é deduzido do imposto do mês (ou dos meses seguintes no mesmo ano).
```
Fontes: Lei nº 11.033/2004 (art. 3º, com redação da Lei nº 14.754/2023), Lei nº 8.668/1993, Instrução Normativa RFB nº 1.585/2015, Perguntas e Respostas IRPF 2026.

### 2. Compensação de prejuízos
```
Operações comuns × operações comuns (ações, opções, futuros, ETF, BDR): compensam entre si
Day trade × day trade: somente entre si
Comum × day trade: NÃO se cruzam
FII/Fiagro: prejuízo só compensa ganho em FII/Fiagro
Prejuízo não prescreve enquanto informado mês a mês na declaração.
Prejuízo de mês com vendas até R$ 20.000,00 também é acumulado; o lucro isento não consome prejuízo.
```

### 3. Entrevista mínima
```
Q1: Competência e notas de corretagem do mês (todas as corretoras)?
Q2: Tipos de operação: ações à vista, day trade, FII/Fiagro, ETF, BDR, derivativos?
Q3: Custo médio de cada ativo em carteira (inclusive bonificações e desdobramentos)?
Q4: Prejuízos acumulados por categoria até o mês anterior?
Q5: IRRF retido (0,005% e 1%) — informe da corretora?
```

### 4. Cálculo (Python)
```python
def operacoes_comuns(vendas_acoes_vista, resultado, prejuizo_acum=0.0, irrf_005=0.0,
                     isencao_aplicavel=True):
    """isencao_aplicavel=False para ETF, BDR, opções e futuros (sem a isenção de R$ 20 mil)."""
    if resultado < 0:                                   # prejuízo sempre acumula
        return 0.0, 0.0, prejuizo_acum - resultado
    if isencao_aplicavel and vendas_acoes_vista <= 20_000:
        return 0.0, 0.0, prejuizo_acum                  # lucro isento não consome prejuízo
    base = max(resultado - prejuizo_acum, 0.0)
    novo_prej = max(prejuizo_acum - resultado, 0.0)
    ir = base * 0.15
    return round(ir, 2), round(max(ir - irrf_005, 0.0), 2), round(novo_prej, 2)

def day_trade(resultado, prejuizo_day=0.0, irrf_1=0.0):
    if resultado < 0:
        return 0.0, 0.0, prejuizo_day - resultado
    base = max(resultado - prejuizo_day, 0.0)
    ir = base * 0.20
    return round(ir, 2), round(max(ir - irrf_1, 0.0), 2), round(max(prejuizo_day - resultado, 0.0), 2)

# Exemplo fictício: vendas de ações R$ 23.000, lucro R$ 8.000, prejuízo anterior R$ 2.000
ir, pagar, prej = operacoes_comuns(23_000, 8_000, 2_000, irrf_005=1.15)
print(f"Comuns — IR R$ {ir:,.2f} | DARF 6015 R$ {pagar:,.2f} | prejuízo restante R$ {prej:,.2f}")
# → IR 900,00 | DARF 898,85 | prejuízo 0,00
```

### 5. Entregável obrigatório
a) Apuração mensal:
```
COMPETÊNCIA __/2026   INVESTIDOR: CLIENTE EXEMPLO

OPERAÇÕES COMUNS
Vendas de ações no mercado à vista: R$ 23.000 (> R$ 20.000 → tributa)
Resultado: R$ 8.000 | Prejuízo a compensar: R$ 2.000 | Base: R$ 6.000
IR 15%: R$ 900,00 | (−) IRRF 0,005%: R$ 1,15 | DARF 6015: R$ 898,85

DAY TRADE: resultado R$ 0 | DARF: R$ 0
FII/FIAGRO (venda de cotas): resultado R$ 0 | DARF: R$ 0
TOTAL DARF 6015: R$ 898,85 — vencimento: último dia útil de __/2026
```
b) Planilha anual: mês, vendas, resultado por categoria, prejuízo acumulado por categoria, IR, IRRF, DARF pago.
c) DARFs 6015 prontos (o cliente ou o contador emite no Sicalc; a skill não paga).
d) Reflexo na declaração: ficha Renda Variável mês a mês (comuns, day trade, FII) e Bens e Direitos em 31/12 pelo custo de aquisição.

## Erros comuns / pontos de atenção
- Aplicar a isenção de R$ 20.000,00 a ETF, BDR, FII, opções ou futuros (só vale para ações no mercado à vista).
- Calcular a isenção pelo lucro: o limite é sobre o total de VENDAS do mês.
- Cruzar prejuízo de operações comuns com day trade.
- Custo médio sem bonificações (custo informado pela empresa) e sem desdobramentos/grupamentos.
- Não declarar cada FII em Bens e Direitos em 31/12.
- Considerar isento rendimento de FII com menos de 100 cotistas (o critério antigo era 50).
- Esquecer que a pré-preenchida de 2026 já traz IRRF de renda variável: a divergência vira malha.

## Casos de borda
- **Operações estruturadas (long-short)**: cada perna segue sua natureza; pode haver comum e day trade no mesmo dia.
- **Stock options (plano de opção de compra de ações — art. 168, § 3º, da Lei nº 6.404/1976)**: o STJ fixou em 11/09/2024, no Tema repetitivo 1.226 (REsp 2.069.644/SP e REsp 2.074.564/SP), que o plano tem natureza mercantil: não incide IRPF no exercício da opção (compra das ações) e incide IRPF como ganho de capital quando o beneficiário revende as ações com ganho. Se as ações forem vendidas na bolsa, apurar aqui como renda variável; fora da bolsa, `irpf-ganho-capital`. Conferir se o caso concreto é mesmo plano do art. 168, § 3º (pagamentos em dinheiro que substituem o ganho das opções podem ter outro tratamento).
- **Cripto em exchange estrangeira**: Lei nº 14.754/2023 (anual, 15%) — fora desta skill.
- **Alta renda (IRPF 2027)**: ganhos em bolsa tributados pelo ganho líquido ENTRAM na base do IRPFM (renda total acima de R$ 600.000,00); rendimentos de FII/Fiagro com 100+ cotistas ficam fora (art. 16-A, § 1º, da Lei nº 9.250/1995, incluído pela Lei nº 15.270/2025).
- **Mudança de regras de aplicações financeiras**: a Medida Provisória nº 1.303/2025, que alterava a tributação de aplicações e cripto, perdeu a eficácia em outubro de 2025 sem conversão em lei; continuam valendo as regras desta skill. No início de cada ano, conferir em planalto.gov.br se nova lei alterou a tributação de renda variável e aplicações antes de usar a tabela do passo 1.

## Perguntas que o usuário costuma fazer
- **"Vendi R$ 19 mil em ações e lucrei R$ 3 mil. Pago?"** Não: vendas do mês até R$ 20.000,00 no mercado à vista são isentas (informar como isento na declaração).
- **"Tive prejuízo no day trade. Posso abater do lucro das ações?"** Não; só de lucro futuro em day trade.
- **"Dividendo de FII é isento?"** Sim, se o fundo cumprir os requisitos (100+ cotistas, negociação exclusiva em bolsa, cotista com menos de 10%).

## Quando escalar
- Declaração anual → `elaborar-irpf-completa`
- Cripto, ações fora da bolsa → `irpf-ganho-capital`
- Malha → `diagnosticar-malha-fina-pf`

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei nº 11.033/2004 — art. 3º (isenções; FII/Fiagro), com redação da Lei nº 14.754/2023.
- Lei nº 8.668/1993 — arts. 17 e 18 (tributação de FII).
- Lei nº 8.981/1995 — arts. 72 e seguintes (renda variável).
- Lei nº 9.250/1995 — art. 16-A (IRPFM, incluído pela Lei nº 15.270/2025).
- Lei nº 13.043/2014 — regras de mercado de capitais.
- Lei nº 14.754/2023 — aplicações financeiras e cripto no exterior.
- Instrução Normativa RFB nº 1.585/2015 — tributação de aplicações financeiras e renda variável.
- Instrução Normativa RFB nº 1.500/2014 — normas gerais do IRPF.
- Decreto nº 9.580/2018 (RIR/2018) — regulamento do imposto de renda.
- Lei nº 6.404/1976 — art. 168, § 3º (plano de opção de compra de ações).
- STJ, Tema repetitivo 1.226 (REsp 2.069.644/SP e REsp 2.074.564/SP, julgado em 11/09/2024) — stock options: natureza mercantil, IR na revenda com ganho.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
