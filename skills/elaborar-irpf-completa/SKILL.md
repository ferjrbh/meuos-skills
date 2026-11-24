---
name: elaborar-irpf-completa
description: "ELABORA a declaração de IRPF do zero para contribuintes com várias fontes — empregos, autônomo, aluguéis, ganho de capital, B3, aplicações e entidades no exterior (Lei nº 14.754/2023) e atividade rural. Organiza as fichas, compara declaração completa × desconto simplificado, calcula imposto a pagar ou a restituir com a tabela do IRPF 2026 (ano-calendário 2025) e avisa o que muda no IRPF 2027 (Lei nº 15.270/2025: redução anual, dividendos, IRPFM). DIFERENÇA: `analisar-irpf` REVISA uma pré-preenchida contra documentos; esta MONTA a declaração inteira. Acionar quando o usuário disser \"fazer a declaração\", \"montar o IRPF\", \"elaborar imposto de renda\", \"declaração completa ou simplificada\", \"retificadora\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Elaboração da declaração de IRPF (completa × simplificada)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Monta a Declaração de Ajuste Anual a partir dos documentos do cliente: coleta, organiza por ficha, simula completa × simplificada, calcula o saldo e prepara o plano de pagamento. Vale para o **IRPF 2026 (exercício 2026, ano-calendário 2025)**, com quadro de alerta para o IRPF 2027.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Declaração nova, sem pré-preenchida como base, ou com muitas fontes.
- Retificadora que exige refazer a declaração.
- Não usar para revisar pré-preenchida (`analisar-irpf`) nem para intimação de malha (`diagnosticar-malha-fina-pf`).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Nos exemplos, usar CLIENTE EXEMPLO e valores fictícios.

## Passo a passo (instruções para o agente de IA)

### 1. Parâmetros do IRPF 2026 (ano-calendário 2025)
```
PRAZO: 23/03/2026 a 29/05/2026, 23h59 (Instrução Normativa RFB nº 2.312/2026)

TABELA PROGRESSIVA ANUAL (pergunta 061 do Perguntas e Respostas IRPF 2026)
Base de cálculo anual (R$)        Alíquota   Parcela a deduzir (R$)
até 28.467,20                       0%            0,00
28.467,21 a 33.919,80               7,5%      2.135,04
33.919,81 a 45.012,60              15%        4.679,03
45.012,61 a 55.976,16              22,5%      8.054,97
acima de 55.976,16                 27,5%     10.853,78
(A faixa isenta soma 4 meses a R$ 2.259,20 e 8 meses a R$ 2.428,80 — mudança da tabela em
maio/2025.)

DESCONTO SIMPLIFICADO: 20% dos rendimentos tributáveis, limitado a R$ 16.754,34
DEPENDENTE: R$ 2.275,08 por ano
INSTRUÇÃO: R$ 3.561,50 por pessoa por ano
SAÚDE: sem limite, com documento que identifique prestador e beneficiário
PGBL: até 12% dos rendimentos tributáveis (exige contribuição à previdência oficial)
PENSÃO ALIMENTÍCIA: integral, se judicial ou por escritura pública (art. 733 do CPC)
PAIS/AVÓS DEPENDENTES: rendimentos, tributáveis ou não, até R$ 28.467,20 em 2025

OBRIGATORIEDADE (qualquer uma):
- rendimentos tributáveis acima de R$ 35.584,00
- isentos, não tributáveis ou exclusivos na fonte acima de R$ 200.000,00
- ganho de capital tributável; alienações em bolsa acima de R$ 40.000,00 ou com ganho tributável
- receita bruta rural acima de R$ 177.920,00 (ou compensar prejuízo rural)
- bens acima de R$ 800.000,00 em 31/12/2025
- passou a residente; optou pela isenção de 180 dias na venda de imóvel residencial
- aplicações financeiras, lucros/dividendos ou entidade controlada no exterior; trust
```
Fonte: Perguntas e Respostas IRPF 2026 v1.00 (Receita Federal) e Ministério da Fazenda, notícia de 16/03/2026.

### 2. Entrevista mínima
```
Q1: Ano-calendário e última declaração transmitida (para importar)?
Q2: Fontes de renda: empregos, pró-labore, autônomo, aluguel (pago por PJ ou PF), aposentadoria?
Q3: Ações/FII na B3, cripto, venda de imóvel ou outro bem? GCAP gerado?
Q4: Bens em 31/12 (contas, aplicações, imóveis, veículos, participações)? Dívidas?
Q5: Dependentes (CPF de cada)? Saúde, educação, pensão, PGBL?
Q6: Aplicações, contas, empresas ou trust no exterior (Lei nº 14.754/2023)?
Q7: Atividade rural? Doações incentivadas? Espólio?
```

### 3. Simulação completa × simplificada (Python)
```python
# Tabela anual IRPF 2026 (ano-calendário 2025) — conferir antes de usar em outro ano
FAIXAS = [(28_467.20, 0.0, 0.0), (33_919.80, 0.075, 2_135.04), (45_012.60, 0.15, 4_679.03),
          (55_976.16, 0.225, 8_054.97), (float("inf"), 0.275, 10_853.78)]
LIMITE_SIMPLIFICADO = 16_754.34
DEPENDENTE = 2_275.08

def imposto(base):
    for teto, aliq, deduz in FAIXAS:
        if base <= teto:
            return max(base * aliq - deduz, 0.0)

def irpf_anual(rend_tributavel, deducoes_legais=0.0, dependentes=0, simplificado=False):
    if simplificado:
        deducoes = min(LIMITE_SIMPLIFICADO, rend_tributavel * 0.20)
    else:
        deducoes = deducoes_legais + dependentes * DEPENDENTE
    return round(imposto(max(rend_tributavel - deducoes, 0.0)), 2)

# Exemplo fictício: rendimento R$ 120.000, INSS + saúde + educação R$ 18.000, 2 dependentes
simp = irpf_anual(120_000, simplificado=True)
comp = irpf_anual(120_000, 18_000, 2)
print(f"Simplificada: R$ {simp:,.2f} | Completa: R$ {comp:,.2f}")
print("Escolher:", "Simplificada" if simp <= comp else "Completa")
# O imposto devido ainda é comparado com o IRRF/carnê-leão já pagos para chegar ao saldo.
```

### 4. Estrutura da declaração (fichas)
```
- Identificação, dependentes (CPF obrigatório) e alimentandos
- Rendimentos Tributáveis Recebidos de PJ (salário, pró-labore, aluguel pago por PJ)
- Rendimentos Tributáveis de PF/Exterior (aluguel pago por PF, autônomo a PF — importar do
  Carnê-Leão Web)
- Rendimentos Isentos (lucros e dividendos de resultados até 2025, FGTS, indenizações
  rescisórias, poupança, LCI/LCA, ações até R$ 20.000/mês, imóvel único até R$ 440.000)
- Rendimentos Sujeitos à Tributação Exclusiva (13º, aplicações financeiras no Brasil, JCP, PLR)
- Pagamentos Efetuados (saúde, educação, pensão, PGBL, advogado em ação judicial de rendimento)
- Doações Efetuadas e doações diretamente na declaração (ECA, Idoso — limites próprios)
- Bens e Direitos (situação em 31/12/2024 e 31/12/2025)
- Dívidas e Ônus Reais (acima de R$ 5.000,00 em 31/12)
- Ganhos de Capital (importar do GCAP)
- Renda Variável (resumo mensal; operações comuns e day trade; DARF 6015)
- Atividade Rural (livro-caixa)
- Aplicações Financeiras e Lucros/Dividendos no Exterior (Lei nº 14.754/2023: tributação
  anual a 15% na própria declaração, com compensação de perdas e do imposto pago lá fora;
  entidades controladas: regime de lucros apurados em 31/12 ou opção pela transparência)
- Imposto pago (carnê-leão 0190, ganho de capital 4600, renda variável 6015, complementar 0246)
```

### 5. Pagamento
- Saldo em até 8 quotas mensais; nenhuma abaixo de R$ 50,00; saldo abaixo de R$ 100,00 em quota única.
- 1ª quota ou quota única até 29/05/2026, sem juros; demais no último dia útil de cada mês, com Selic acumulada + 1% no mês do pagamento.
- Código DARF 0211. Atraso: multa de mora de 0,33% ao dia, limitada a 20% (art. 61 da Lei nº 9.430/1996), mais Selic.
- Débito automático (IRPF 2026): para quota única ou a partir da 1ª quota, só se a declaração (original ou retificadora) for entregue até 10/05/2026; entregue de 11 a 29/05/2026, o débito automático vale a partir da 2ª quota. Retificadora entregue depois de 29/05/2026 cancela o débito automático (art. 12 da Instrução Normativa RFB nº 2.312/2026; pergunta 066 do Perguntas e Respostas IRPF 2026). Em outro exercício, conferir as datas na instrução normativa do ano.

### 6. Alerta IRPF 2027 (ano-calendário 2026) — Lei nº 15.270/2025
- **Redução anual** (art. 11-A da Lei nº 9.250/1995): rendimentos tributáveis até R$ 60.000,00 → imposto zero (redução de até R$ 2.694,15); de R$ 60.000,01 a R$ 88.200,00 → redução = R$ 8.429,73 − 0,095575 × rendimentos; acima de R$ 88.200,00 → sem redução. A tabela progressiva anual do ano-calendário 2026 é a soma das tabelas mensais vigentes no ano (art. 1º, parágrafo único, da Lei nº 11.482/2007): antes de simular o IRPF 2027, usar a tabela anual divulgada pela Receita no Perguntas e Respostas do exercício 2027 (não usar a do quadro do passo 1).
- **Dividendos**: retenção de 10% quando uma PJ paga a uma PF mais de R$ 50.000,00 no mês (art. 6º-A da Lei nº 9.250/1995); lucros de resultados até 2025 aprovados até 31/12/2025 ficam fora, se pagos conforme a ata.
- **IRPFM**: renda total acima de R$ 600.000,00; alíquota de 0% a 10% (renda ÷ 60.000 − 10), 10% a partir de R$ 1.200.000,00; deduz o IR já pago, o IR da Lei nº 14.754/2023, a retenção mensal do art. 6º-A e o redutor do art. 16-B (quando a soma com a tributação efetiva da empresa supera a alíquota nominal de IRPJ + CSLL da PJ: 34%, 40% ou 45%). Entram na base, entre outros, dividendos e ganhos em bolsa; ficam fora ganhos de capital (exceto bolsa), poupança, LCI/LCA, CRI/CRA, FII/Fiagro com 100+ cotistas, herança/doação e indenizações (art. 16-A, § 1º).
- Antes de orientar cliente de alta renda, consultar no portal do STF (portal.stf.jus.br) se há ação de controle de constitucionalidade contra a Lei nº 15.270/2025 com decisão que altere sua aplicação, e registrar a data da consulta no parecer.

### 7. Entregável obrigatório
**a) Lista de documentos**
```
[ ] Informe de rendimentos — empregador(es) / fonte(s) PJ
[ ] Informe do INSS (aposentado/pensionista)
[ ] Informes de bancos e corretoras (saldos, aplicações, JCP, dividendos)
[ ] Informe/notas da B3 e DARFs 6015
[ ] Aluguéis: recibos (locatário PF) ou informe (locatário PJ); Carnê-Leão Web
[ ] Saúde: recibos com CPF/CNPJ do prestador e beneficiário; plano de saúde por beneficiário
[ ] Educação (limite anual por pessoa)
[ ] Pensão: decisão judicial ou escritura + comprovantes
[ ] PGBL / Fapi
[ ] GCAP e DARFs 4600
[ ] Bens em 31/12 (escritura, documento do veículo, extratos)
[ ] Dívidas acima de R$ 5.000,00
[ ] Exterior (extratos, impostos pagos lá fora, demonstrações de controladas)
[ ] Doações incentivadas
[ ] Declaração do ano anterior
```
b) Simulação completa × simplificada (Python, passo 3).
c) Declaração transmitida + recibo arquivado por 5 anos.
d) DARFs 0211 (quota única ou quotas).
e) Lista de bens em 31/12 atualizada.
f) Checklist:
```
[ ] Dependentes com CPF e sem duplicidade com outra declaração
[ ] Deduções comprovadas
[ ] GCAP importado
[ ] Renda variável mês a mês
[ ] Bens batendo com extratos/documentos
[ ] Exterior conforme Lei nº 14.754/2023
[ ] Completa × simplificada simuladas
[ ] Sem erro de bloqueio no programa
[ ] Recibo guardado e plano de pagamento enviado
[ ] Alerta IRPF 2027 dado ao cliente (se dividendos > R$ 50.000/mês ou renda > R$ 600.000)
```

## Erros comuns / pontos de atenção
- Dependente declarado também por outro contribuinte (pais separados).
- Filho de 21 a 24 anos sem estar cursando ensino superior ou técnico de 2º grau.
- Pai/mãe com rendimentos acima de R$ 28.467,20 em 2025.
- Recibo de saúde sem identificação do prestador ou do beneficiário.
- Educação com idiomas, cursos livres ou material escolar.
- Venda de ações fora da bolsa sem GCAP.
- Day trade sem DARF mensal.
- Usar a tabela anual de outro ano-calendário (a tabela do passo 1 vale só para o ano-calendário 2025).

## Casos de borda
- **Mudou para o exterior**: Comunicação e Declaração de Saída Definitiva do País (Instrução Normativa SRF nº 208/2002).
- **Indenização trabalhista**: verbas rescisórias previstas em lei são isentas (art. 6º, V, da Lei nº 7.713/1988); PDV também (Súmula 215 do STJ).
- **Criptoativos em exchange no Brasil**: ganho de capital mensal se as alienações do mês passarem de R$ 35.000,00 (DARF 4600). **Em exchange no exterior** (desde 2024): regra da Lei nº 14.754/2023, tributação anual a 15%, sem a isenção de R$ 35.000,00.
- **Sócio que recebeu lucros**: resultados até 2025, isentos (art. 10 da Lei nº 9.249/1995). Pagamentos de 2026 acima de R$ 50.000,00/mês por PJ sofrem retenção de 10%.
- **Falecimento**: declarações de espólio (inicial, intermediárias e final).

## Perguntas que o usuário costuma fazer
- **"Qual compensa, completa ou simplificada?"** A completa compensa quando as deduções legais passam do desconto simplificado (20% limitado a R$ 16.754,34).
- **"Ganho até R$ 5 mil por mês, ainda pago no ajuste?"** A redução da Lei nº 15.270/2025 vale na fonte desde janeiro/2026 e no ajuste a partir do IRPF 2027; o IRPF 2026 segue a tabela do quadro do passo 1.

## Quando escalar
- Malha → `diagnosticar-malha-fina-pf`
- Ganho de capital → `irpf-ganho-capital`
- Aluguel / carnê-leão → `irpf-aluguel-carne-leao`
- B3 → `irpf-investimentos-bolsa`

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei nº 9.250/1995 — art. 8º (deduções), art. 10 (desconto simplificado), arts. 6º-A, 11-A, 16-A e 16-B (incluídos pela Lei nº 15.270/2025).
- Lei nº 11.482/2007 — art. 1º, parágrafo único (tabela anual).
- Lei nº 7.713/1988 — art. 6º (isenções) e art. 8º (carnê-leão).
- Lei nº 9.249/1995 — art. 10 (lucros e dividendos).
- Lei nº 14.754/2023 — aplicações financeiras, entidades controladas e trusts no exterior.
- Lei nº 15.270/2025 — redução do IR, dividendos e IRPFM.
- Lei nº 9.430/1996 — art. 61 (multa e juros de mora).
- Lei nº 13.105/2015 (CPC) — art. 733 (alimentos por escritura pública).
- Decreto nº 9.580/2018 (RIR/2018).
- Instrução Normativa RFB nº 1.500/2014 — normas gerais do IRPF.
- Instrução Normativa RFB nº 2.312/2026 — IRPF 2026.
- Instrução Normativa SRF nº 208/2002 — saída definitiva e não residentes.
- Súmula 215 do STJ — PDV.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
