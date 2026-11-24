---
name: parcelamento-receita-federal
description: "Compara as saídas para débitos federais — pagamento à vista, parcelamento ordinário ou simplificado da Receita Federal (até 60 parcelas, Lei nº 10.522/2002, parcelas corrigidas pela Selic), parcelamento do Simples Nacional, e transação tributária da PGFN/RFB (Lei nº 13.988/2020: descontos de até 65% e 120 meses, ou até 70% e 145 meses para pessoa física, ME e EPP), incluindo editais vigentes em novembro/2026 e regras para empresas em recuperação judicial. Considera as reduções de multa de ofício do art. 6º da Lei nº 8.218/1991 e o encargo legal da dívida ativa. Acionar quando o usuário disser \"parcelar\", \"parcelamento\", \"transação\", \"Regularize\", \"PGFN\", \"dívida ativa\", \"débito federal\", \"edital de transação\", \"não tenho caixa para pagar imposto\". Entrega: simulação de cenários, roteiro de adesão e calendário de parcelas."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Parcelamento e transação de débitos federais

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Levanta os débitos federais do cliente (Receita Federal e dívida ativa da PGFN), simula cada saída possível e recomenda a de menor custo compatível com o caixa. Depois roteiriza a adesão e monta o calendário de acompanhamento para evitar rescisão.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Débitos federais sem caixa para pagamento à vista.
- Débitos inscritos em dívida ativa (PGFN) com possibilidade de desconto.
- Antes de encerrar empresa com débitos (`encerramento-empresa-baixa`).
- Não usar para débitos estaduais e municipais (programas próprios de cada ente — apenas listar no diagnóstico).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite. A adesão a parcelamento ou transação é ato do contribuinte (ou do procurador) e implica confissão irretratável da dívida: só aderir com autorização expressa do cliente.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: Quem é o devedor (PF ou PJ; regime; ME/EPP?) e onde estão os débitos: RFB (e-CAC, Situação
    Fiscal), PGFN (Regularize), Simples Nacional, Estado, Município?
Q2: Capacidade de pagamento mensal (`fluxo-caixa-projetado`)?
Q3: Já tem parcelamento ou transação ativos? Houve rescisão anterior?
Q4: Algum débito está em discussão administrativa ou judicial? (aderir = desistir)
Q5: Os débitos vêm de auto de infração recente (dentro de 30 dias da ciência)? (redução de multa)
Q6: A empresa está em recuperação judicial?
```

### 2. Modalidades
```
1. PAGAMENTO À VISTA
   Débito em atraso: principal + multa de mora de 0,33% ao dia, limitada a 20%, + Selic
   acumulada + 1% no mês do pagamento (art. 61 da Lei nº 9.430/1996).
   Auto de infração pago em até 30 dias da ciência: multa de ofício reduzida em 50%
   (art. 6º da Lei nº 8.218/1991).

2. PARCELAMENTO ORDINÁRIO / SIMPLIFICADO — RECEITA FEDERAL (Lei nº 10.522/2002)
   - Até 60 parcelas mensais.
   - Parcela mínima: R$ 200,00 (PF) e R$ 500,00 (PJ) (gov.br — serviço "Parcelar dívidas na
     Receita Federal").
   - Cada parcela = valor consolidado ÷ nº de parcelas, acrescida da Selic acumulada desde o
     mês seguinte à consolidação até o mês anterior ao pagamento + 1% no mês do pagamento
     (art. 13 da Lei nº 10.522/2002). NÃO é tabela Price.
   - Multa de mora NÃO é reduzida no parcelamento. Multa de ofício de auto de infração
     parcelado em até 30 dias da ciência: redução de 40% (art. 6º da Lei nº 8.218/1991).
   - Simplificado (art. 14-C da Lei nº 10.522/2002): pedido 100% online, sem garantia; o
     pagamento da 1ª parcela vale como confissão. Desde a Instrução Normativa RFB nº 2.063/2022
     (que consolidou o parcelamento ordinário, o simplificado e o de recuperação judicial e
     revogou a IN RFB nº 1.891/2019) não há mais o teto de R$ 5.000.000,00 para o simplificado.
     A IN RFB nº 2.063/2022 não se aplica aos débitos do Simples Nacional e do MEI.
   - Rescisão: falta de 3 parcelas, consecutivas ou não, ou de 1 parcela estando pagas todas
     as demais (art. 14-B da Lei nº 10.522/2002).
   - Reparcelamento (art. 14-A da Lei nº 10.522/2002): débitos de parcelamento em andamento ou
     rescindido podem ser reparcelados; a 1ª parcela deve ser de 10% do total consolidado, ou
     de 20% se já houver reparcelamento anterior.
   - Pedido no e-CAC > Pagamentos e Parcelamentos.

3. PARCELAMENTO DO SIMPLES NACIONAL (art. 21, § 15, da LC nº 123/2006)
   Até 60 parcelas; parcela mínima de R$ 300,00 para ME/EPP (art. 54, I, da Resolução CGSN
   nº 140/2018); para o MEI, o mínimo é fixado em ato do órgão concessor (conferir no Portal do
   Simples Nacional / PGMEI); parcelas vencem no último dia útil de cada mês; pedido no Portal
   do Simples Nacional / e-CAC.

4. TRANSAÇÃO TRIBUTÁRIA (Lei nº 13.988/2020)
   - Na cobrança da dívida ativa (PGFN, portal Regularize) e no contencioso administrativo ou
     de pequeno valor (editais conjuntos PGFN/RFB, via e-CAC).
   - Limites legais (art. 11, §§ 2º e 3º, com redação da Lei nº 14.375/2022):
       regra geral: desconto de até 65% do total e prazo de até 120 meses;
       PF, ME, EPP, Santas Casas, cooperativas e instituições de ensino: até 70% e 145 meses.
   - O desconto não alcança o principal (incide sobre multa, juros e encargos), salvo
     modalidades específicas previstas em edital.
   - Por adesão (edital) ou individual (débitos acima do limite da Portaria PGFN nº 6.757/2022).
   - Avaliação da capacidade de pagamento pela PGFN define o desconto.

5. EMPRESA EM RECUPERAÇÃO JUDICIAL (Lei nº 14.112/2020)
   Modalidades da Lei nº 10.522/2002, com redação da Lei nº 14.112/2020:
   - art. 10-A, V: até 120 prestações — 0,5% da dívida da 1ª à 12ª, 0,6% da 13ª à 24ª e o
     saldo em até 96 parcelas;
   - art. 10-A, VI: liquidar até 30% com créditos de prejuízo fiscal e base negativa da CSLL e
     parcelar o restante em até 84 parcelas, com os mesmos percentuais mínimos;
   - art. 10-B: até 24 parcelas (3% da 1ª à 6ª, 6% da 7ª à 12ª, saldo em até 12) para os
     tributos ali indicados;
   - art. 10-C: transação com a PGFN para dívida ativa, quitação em até 120 meses e redução
     de até 70%.
   Pedido conjugado com o processo de RJ → advogado parceiro.

6. PROGRAMAS ESPECIAIS (PERT, PRR, PERSE etc.)
   Encerrados. Só considerar se houver programa novo publicado em lei.
```

### 3. Editais em aberto (situação em 15/11/2026 — notícia da PGFN de 02/10/2026)
```
Edital PGDAU nº 6/2026 (regra geral e capacidade de pagamento; PF e PJ com dívida de até
  R$ 45 milhões) — descontos de até 70%, entrada em até 12 parcelas e saldo em até
  133 meses; prazo prorrogado pelo Edital PGDAU nº 10/2026: adesão até 29/01/2027, 19h;
  alcança débitos inscritos até 03/07/2026 nas modalidades que não são de pequeno valor.
Edital PGDAU nº 9/2026 (Desenrola MEI — dívida ativa de até R$ 20.000,00) — até 29/01/2027.
Desenrola MEI Pequeno Valor (Portaria PGFN nº 2.970/2026 — débitos de até 5 salários mínimos,
  código 1537) — adesão de 01/10/2026 a 29/01/2027; até 60 meses, desconto de 50%.
Edital PGDAU nº 12/2026 (FGTS e contribuição da LC nº 110/2001, passivo de até R$ 45 milhões)
  — adesão até 29/01/2027, 19h; sem desconto sobre valores devidos ao trabalhador.
Edital PGDAU nº 8/2026 (Desenrola Rural — agricultores familiares e cooperativas) — prazo
  ajustado pelo Edital PGDAU nº 10/2026: conferir a data-limite no Regularize antes de orientar.
Edital de Transação Conjunto PGFN/RFB nº 4/2026 (contencioso de IRRF de investidores não
  residentes) — adesão até 29/12/2026, 19h; devedor contumaz (Lei Complementar nº 225/2026)
  não pode aderir.
```
Sempre reconferir no Regularize, no e-CAC e no Diário Oficial antes de aderir: editais mudam com frequência e são prorrogados.

### 4. Cuidados com a dívida ativa (PGFN)
- Débito inscrito tem **encargo legal de 20%** (art. 1º do Decreto-Lei nº 1.025/1969), reduzido a 10% se a dívida for paga antes do ajuizamento da execução fiscal (art. 3º do Decreto-Lei nº 1.569/1977). Na transação, o encargo pode ser objeto de desconto conforme o edital.
- Atualização pela Selic, como na Receita Federal (não TR).
- Pode haver protesto da CDA e inclusão no CADIN mesmo durante negociação, até a adesão ser formalizada.
- Garantias (penhora, fiança, seguro-garantia) em execuções fiscais podem ser mantidas.

### 5. Simulação (Python)
```python
def ordinario(consolidado, parcelas=60, selic_mensal=0.0115, minimo=500.0):
    """Parcelamento da RFB: parcela-base fixa + Selic acumulada (simples) + 1% no mês do pagamento.
    selic_mensal é premissa (usar a projeção do momento); minimo: 500 PJ / 200 PF."""
    n = min(parcelas, max(int(consolidado // minimo), 1))
    base = consolidado / n
    total = sum(base * (1 + selic_mensal * (k - 1) + 0.01) for k in range(1, n + 1))
    return n, round(base, 2), round(total, 2)

def transacao(divida, desconto=0.0, parcelas=60, entrada_pct=0.0):
    """Transação: desconto e entrada conforme o edital e a capacidade de pagamento.
    Na prática as parcelas também são corrigidas pela Selic."""
    liquido = divida * (1 - desconto)
    entrada = liquido * entrada_pct
    return round(entrada, 2), round((liquido - entrada) / parcelas, 2), round(liquido, 2)

# Exemplo fictício: débito consolidado de R$ 120.000 (PJ)
print(ordinario(120_000))                   # 60 parcelas-base de R$ 2.000 + Selic → total ≈ R$ 161.910
print(transacao(120_000, 0.30, 60, 0.06))   # entrada R$ 5.040 + 60 × R$ 1.316 (antes da Selic)
```

### 6. Sequência de adesão
```
1. Diagnóstico: e-CAC (Situação Fiscal / Relatório de Pendências) + Regularize (dívida ativa).
2. Separar débitos: em discussão (decidir se desiste), declarados, de auto de infração, do Simples.
3. Simular cada modalidade (passo 5) e comparar com o caixa.
4. Aderir (com autorização do cliente):
   - e-CAC: parcelamento RFB e transações do contencioso;
   - Regularize: dívida ativa e editais PGFN;
   - Portal do Simples: débitos do Simples/MEI.
5. Pagar a 1ª parcela/entrada no prazo (sem ela o pedido não produz efeito).
6. Acompanhar mensalmente (regra de rescisão do passo 2).
7. Emitir certidão positiva com efeitos de negativa (art. 206 do CTN — Lei nº 5.172/1966):
   o parcelamento suspende a exigibilidade (art. 151, VI, do CTN), mas não gera CND "negativa".
```

### 7. Entregável obrigatório
a) Comparativo de cenários:
```
DÉBITO CONSOLIDADO: R$ __ (RFB R$ __ | PGFN R$ __ | Simples R$ __)

CENÁRIO 1 — À VISTA: R$ __ (multa de mora/ofício + Selic) | impacto no caixa: −R$ __
CENÁRIO 2 — PARCELAMENTO RFB: __ parcelas de R$ __ + Selic | total estimado R$ __
            (redução de 40% da multa de ofício, se auto de infração em até 30 dias)
CENÁRIO 3 — TRANSAÇÃO (edital __/2026, se elegível): desconto R$ __ | entrada R$ __ |
            __ parcelas de R$ __ | total R$ __
CENÁRIO 4 — DISCUTIR (administrativo/judicial): custo, chance de êxito, garantia exigida
            (avaliação de advogado parceiro)

RECOMENDAÇÃO: __   JUSTIFICATIVA: __
```
b) Comprovante de adesão (nº do pedido/acordo).
c) Calendário de parcelas com vencimentos.
d) Certidão positiva com efeitos de negativa, após a 1ª parcela.
e) Plano de monitoramento mensal.

## Erros comuns / pontos de atenção
- Aderir sem simular (às vezes o à vista com redução de multa sai mais barato).
- Usar fórmula de tabela Price: o parcelamento federal é parcela fixa + Selic acumulada.
- Prometer redução de 50% da multa de mora no parcelamento ordinário: a redução legal é da multa de OFÍCIO (art. 6º da Lei nº 8.218/1991).
- Incluir débito em discussão sem avisar o cliente: a adesão implica desistência e confissão.
- Esquecer débitos previdenciários e do FGTS (FGTS tem regras próprias da Caixa/Ministério do Trabalho).
- Ignorar o encargo legal de 20% da dívida ativa na comparação.
- Atrasar parcelas: 3 em atraso (seguidas ou não) = rescisão.

## Casos de borda
- **Cliente em recuperação judicial**: modalidades específicas (Lei nº 14.112/2020) → advogado parceiro.
- **Débito em discussão judicial**: aderir exige desistência da ação e renúncia ao direito (Lei nº 13.988/2020 e editais).
- **Vários parcelamentos / reparcelamento**: permitido, com 1ª parcela de 10% do consolidado, ou 20% se já houve reparcelamento (art. 14-A da Lei nº 10.522/2002).
- **Pessoa física com débito de IRPF**: parcela mínima de R$ 200,00; avaliar transação de pequeno valor se inscrito.

## Perguntas que o usuário costuma fazer
- **"Parcelando, já consigo a certidão?"** Sim, a certidão positiva com efeitos de negativa, depois do pagamento da 1ª parcela.
- **"A PGFN dá desconto no principal?"** Em regra não; o desconto incide sobre multa, juros e encargos, limitado a 65% (ou 70% para PF/ME/EPP) do total.
- **"Até quando posso aderir ao edital?"** Edital PGFN nº 6/2026 até 29/01/2027 (conferir no Regularize).

## Quando escalar
- Discutir judicialmente → advogado parceiro com OAB
- Recuperação judicial → advogado parceiro
- Auto de infração ainda não inscrito → `resposta-fiscalizacao-intimacao`
- Fluxo de caixa para definir a parcela → `fluxo-caixa-projetado`

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei nº 10.522/2002 — arts. 10 a 14-F (parcelamento; art. 13, Selic; art. 14-B, rescisão; art. 10-A, recuperação judicial).
- Lei nº 8.218/1991 — art. 6º (redução da multa de ofício).
- Lei nº 9.430/1996 — art. 61 (multa e juros de mora).
- Lei nº 13.988/2020 — transação tributária (art. 11, com redação da Lei nº 14.375/2022).
- Lei nº 14.375/2022 — limites de desconto e prazo da transação.
- Lei nº 14.112/2020 — recuperação judicial.
- Lei Complementar nº 123/2006 — art. 21, § 15 (parcelamento do Simples).
- Lei nº 5.172/1966 (CTN) — art. 151, VI (suspensão da exigibilidade), art. 206 (certidão positiva com efeitos de negativa).
- Decreto-Lei nº 1.025/1969 — encargo legal.
- Portaria PGFN nº 6.757/2022 — transação na dívida ativa.
- Editais PGDAU nº 6/2026, 8/2026, 9/2026, 10/2026 e 12/2026; Portaria PGFN nº 2.970/2026 (Desenrola MEI Pequeno Valor); Edital de Transação Conjunto PGFN/RFB nº 4/2026.
- Decreto-Lei nº 1.569/1977 — art. 3º (redução do encargo legal a 10%).
- Lei nº 10.522/2002 — arts. 10-A a 10-C (recuperação judicial), 14-A (reparcelamento), 14-C (simplificado).
- Instrução Normativa RFB nº 2.063/2022 — parcelamento ordinário, simplificado e de empresa em recuperação judicial na RFB (revogou a IN RFB nº 1.891/2019).
- Resolução CGSN nº 140/2018 — art. 54 (parcelamento do Simples: parcela mínima e vencimento).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
