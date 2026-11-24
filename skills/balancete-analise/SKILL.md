---
name: balancete-analise
description: "Lê e analisa o balancete mensal antes da entrega ao cliente — integridade (débito = crédito, ativo = passivo + PL, sintética = soma das analíticas, saldo inicial = saldo final anterior), natureza dos saldos (saldo invertido), contas transitórias com saldo, variações relevantes, cruzamento com controles auxiliares, efeito de cada achado no PL e indicadores (liquidez, endividamento, prazos médios, margens, retorno) — e produz o pacote analítico com alertas e recomendações. Use após o fechamento do mês ou quando o usuário mencionar \"analisar balancete\", \"revisar balancete\", \"saldo invertido\", \"conta com saldo estranho\", \"indicadores\", \"liquidez\", \"PMR\", \"pacote ao cliente\" ou \"o balancete pode ser entregue?\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Análise de Balancete

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Prova, primeiro, que o balancete pode ser entregue: confere fechamento, natureza dos saldos, contas que deveriam estar zeradas e os cruzamentos com os controles. Depois mede o efeito de cada achado no resultado e no patrimônio, calcula os indicadores e monta o pacote analítico para o cliente.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Depois do encerramento do mês (D+4 do roteiro da skill `fechamento-mensal`), antes de entregar ao cliente.
- Cliente novo: diagnóstico do balancete recebido.
- Para o relatório executivo de uma página ao dono do negócio, usar o modelo de relatório mensal do seu escritório (não vem neste pacote).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Contas analíticas com nome de sócio ou empregado: citar a conta, não a pessoa.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Ao reaproveitar o pacote de um cliente como modelo para outro, procurar e remover qualquer nome, número ou frase do cliente de origem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: Qual cliente e competência? Tenho o balancete do mês e dos 3 meses anteriores (e o mesmo mês do ano anterior)?
Q2: DRE acumulada disponível? Regime tributário? Entidade com ou sem fins lucrativos?
Q3: Houve fato atípico no mês (rescisão grande, venda de imobilizado, multa, empréstimo novo)?
Q4: Qual a materialidade combinada com o contador (valor em reais e percentual)?
Q5: Há decisões conhecidas do cliente que parecem erro mas são intencionais?
```

### 2. Conferir a leitura
Se o balancete veio em PDF, os totais lidos têm de bater com os totais impressos. Divergência é problema de extração do PDF, não de contabilidade. Atenção: balancete emitido sem as contas de saldo zero omite também contas que tiveram movimento no mês e terminaram zeradas; para conferir movimento, pedir o balancete com todas as contas ou o razão.

### 3. Seis verificações, nesta ordem
**1. Integridade**
- Total de débitos = total de créditos.
- Ativo = passivo + patrimônio líquido, somando o resultado do período ainda não encerrado.
- Cada conta sintética = soma das analíticas (diferença indica valor lançado na conta-mãe).
- Saldo inicial do mês = saldo final do mês anterior (se mudou, houve lançamento retroativo).

**2. Natureza dos saldos**
| Conta | Lado normal | Saldo do lado contrário costuma indicar |
|---|---|---|
| Caixa | devedor | impossível: entrada não lançada ou saída lançada a mais |
| Bancos | devedor | lançamento faltando, ou cheque especial/conta garantida que deve ir para o passivo |
| Clientes | devedor | adiantamento recebido lançado aqui (reclassificar para o passivo) ou recebimento em dobro |
| Estoques | devedor | baixa de custo maior que a entrada |
| Fornecedores | credor | adiantamento pago ou pagamento em dobro (reclassificar para adiantamentos a fornecedores, no ativo) |
| Tributos e salários a pagar | credor | pagamento sem a provisão, ou em duplicidade (reclassificar para tributo a recuperar) |
| Capital social | credor | erro de lançamento. Capital a integralizar é conta redutora própria, de saldo devedor |
| Receitas | credor | estorno maior que a receita, ou conta trocada |
| Custos e despesas | devedor | reembolso, recuperação ou estorno lançado na conta errada |

**3. Contas que deveriam estar zeradas**
Transitórias, "a classificar", "a identificar", adiantamentos antigos, empréstimo já quitado. Toda conta transitória com saldo precisa da lista dos itens que a compõem e da data de cada um. Conta "Outros" ou "Diversos" concentrando saldo relevante é alerta. Conta zerada há mais de 6 meses é candidata a inativação.

**4. Variações**
Comparar cada conta com o mês anterior e, quando houver, com o mesmo mês do ano anterior e com o orçamento. Apontar a variação que passar da materialidade combinada (valor em reais **e** percentual ao mesmo tempo). Na falta de materialidade definida, usar 20% como corte inicial e dizer que é provisório. Variação sem explicação documentada vira pergunta ao cliente.

**5. Cruzamentos com os controles auxiliares**
| Conta do balancete | Tem de bater com |
|---|---|
| Bancos e aplicações | conciliação bancária do mês |
| Clientes | relação de títulos em aberto |
| Fornecedores | relação de notas em aberto |
| Tributos a recolher | declarações transmitidas e guias pagas |
| Salários e encargos a pagar | resumo da folha e guias |
| Provisão de férias e 13º | controle de períodos e avos, com movimento todo mês |
| Imobilizado e depreciação | controle de bens, com depreciação lançada todo mês |
| Empréstimos | contrato e extrato do financiamento |

**6. Efeito de cada achado**
Estimar quanto cada achado muda o resultado e o patrimônio líquido se for corrigido. A soma leva ao **patrimônio líquido ajustado**.

### 4. Classificar os achados (cinco níveis)
| Nível | Uso |
|---|---|
| OK | conferido e correto |
| ATENÇÃO | precisa de explicação; não muda o resultado de forma relevante |
| CRÍTICO | distorce resultado, patrimônio ou tributo |
| AUSENTE | algo que deveria existir não existe (provisão, depreciação, conta, documento) |
| INTENCIONAL | parece erro, mas é decisão conhecida e registrada do cliente ou do contador |

### 5. Indicadores
Indicador é termômetro, não diagnóstico: sempre comparado com o histórico do próprio cliente e, se houver dado confiável, com o setor.
```
Margem bruta         = (receita líquida − custo das vendas) ÷ receita líquida
Margem operacional   = resultado antes do resultado financeiro e dos tributos sobre o lucro ÷ receita líquida
Margem líquida       = resultado do período ÷ receita líquida
EBITDA (LAJIDA)      = resultado antes do resultado financeiro e dos tributos sobre o lucro + depreciação + amortização + exaustão
Liquidez corrente    = ativo circulante ÷ passivo circulante
Liquidez seca        = (ativo circulante − estoques) ÷ passivo circulante
Endividamento        = passivo total (circulante + não circulante) ÷ ativo total
Prazo médio de recebimento (PMR) = clientes ÷ receita bruta do período × dias do período
Prazo médio de pagamento (PMP)   = fornecedores ÷ compras do período × dias do período
Giro do estoque      = custo das vendas do período ÷ estoque médio
Retorno sobre o PL (ROE) = resultado do período ÷ patrimônio líquido
```
- Usar receita e dias do **mesmo período** (receita do mês com 30 dias, ou receita acumulada com os dias decorridos). Receita de um mês com 360 dias distorce o prazo.
- PMR com receita **bruta**, porque o saldo de clientes inclui os tributos da nota.
- Se o PMR for maior que o PMP, a empresa financia o cliente com o próprio caixa: explica lucro com caixa apertado.
- Não usar faixa "saudável" fixa (como "endividamento abaixo de 60%") sem fonte; se usar, dizer que é referência genérica.
- Entidade sem fins lucrativos (ITG 2002 (R1)): o resultado é superávit ou déficit; indicadores de lucro e retorno não se aplicam. Recurso de subvenção ou projeto fica no passivo e vai ao resultado conforme é aplicado (NBC TG 07); recurso já aplicado ainda registrado como "a aplicar" e despesa de um projeto paga com recurso de outro são achados críticos.

Cálculo de apoio (só cálculo, sem acesso a arquivos):
```python
# Indicadores do balancete. Receita e dias devem ser do mesmo período.
def indicadores(rec_bruta, rec_liq, custo_vendas, res_antes_fin_trib, res_liq,
                ac, pc, pnc, ativo_total, estoque_final, estoque_inicial,
                clientes, fornecedores, compras, pl, deprec_amort, dias_periodo):
    estoque_medio = (estoque_inicial + estoque_final) / 2
    return {
        "margem_bruta": (rec_liq - custo_vendas) / rec_liq,
        "margem_operacional": res_antes_fin_trib / rec_liq,
        "margem_liquida": res_liq / rec_liq,
        "ebitda": res_antes_fin_trib + deprec_amort,
        "liquidez_corrente": ac / pc,
        "liquidez_seca": (ac - estoque_final) / pc,
        "endividamento": (pc + pnc) / ativo_total,
        "pmr_dias": clientes / rec_bruta * dias_periodo,
        "pmp_dias": fornecedores / compras * dias_periodo if compras else None,
        "giro_estoque": custo_vendas / estoque_medio if estoque_medio else None,
        "roe": res_liq / pl,
    }

# Exemplo fictício: valores acumulados de 12 meses (360 dias)
i = indicadores(rec_bruta=1_750_000, rec_liq=1_500_000, custo_vendas=900_000,
                res_antes_fin_trib=180_000, res_liq=120_000,
                ac=400_000, pc=300_000, pnc=100_000, ativo_total=1_000_000,
                estoque_final=150_000, estoque_inicial=130_000,
                clientes=200_000, fornecedores=100_000, compras=950_000,
                pl=600_000, deprec_amort=20_000, dias_periodo=360)
for k, v in i.items():
    print(k, v)
```

### 6. Entregável
**a) Pacote analítico (para o contador e, depois de revisado, para o cliente)**
```
COMPETÊNCIA __/____ — CLIENTE EXEMPLO

ACHADOS DA REVISÃO
Nº | Nível | Conta | Achado | Efeito no resultado
PL do balancete R$ __ ± ajustes R$ __ = PL ajustado R$ __

DESTAQUES DO MÊS
- Receita líquida: R$ __ (__% sobre o mês anterior)
- Margem bruta: __% (mês anterior __%)
- Resultado: R$ __
- Caixa e aplicações: R$ __

PRINCIPAIS VARIAÇÕES (acima da materialidade)
1. Conta __ +__% — motivo: __

INDICADORES (com comparação histórica)
- Liquidez corrente: __   - Endividamento: __%   - PMR: __ dias   - PMP: __ dias
- Giro do estoque: __ vezes   - ROE acumulado: __%

RECOMENDAÇÕES
1. __
```
**b)** Memória de cálculo dos indicadores e das variações.
**c)** Lista de alertas (saldo invertido, conta transitória com saldo, conta a inativar, variação não explicada, cruzamento que não bate).

Achado crítico em aberto vai para o relatório ao cliente como ressalva, nunca escondido. O relatório só sai depois da revisão.

## Erros comuns / pontos de atenção
- Entregar o balancete em PDF sem leitura.
- Deixar saldo invertido sem reclassificar (banco negativo no ativo, adiantamento de cliente em clientes).
- Tributos a recuperar parados virando "ativo morto".
- Variação relevante sem comentário.
- Indicador sem comparação (número solto não diz nada).
- Calcular PMR com receita de um mês e 360 dias.
- Apontar todo mês como erro uma decisão já registrada do cliente (usar INTENCIONAL).

## Perguntas que o usuário costuma fazer
- **"Qual percentual de variação devo investigar?"** O combinado com o contador, em valor e em percentual. Sem isso, 20% como corte inicial provisório.
- **"Liquidez abaixo de 1 é sempre ruim?"** Não necessariamente; depende do setor e do ciclo de caixa. Comparar com o histórico do cliente.

## Quando escalar
- DRE gerencial: `dre-gerencial`. Fluxo de caixa: `fluxo-caixa-projetado`.
- Due diligence: `due-diligence-contabil`. Valuation: `valuation-pme`.
- Cruzamento com SPED: `revisao-fiscal-cruzamento-sped`.
- Relatório executivo ao cliente: o modelo de relatório mensal do seu escritório.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre outro formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- NBC TG 26 / CPC 26 (R1) — Apresentação das Demonstrações Contábeis.
- NBC TG 1000 (R1) — Contabilidade para PMEs. Pequenas empresas e microentidades podem adotar a NBC TG 1001 ou a NBC TG 1002 (vigentes para exercícios iniciados a partir de 01/01/2023): conferir a norma adotada pelo cliente.
- ITG 2000 (R1) — Escrituração Contábil.
- ITG 2002 (R1) — Entidade sem Finalidade de Lucros; NBC TG 07 — Subvenção e Assistência Governamentais.
- Resolução CVM nº 156, de 23/06/2022 (em vigor desde 01/08/2022; revogou a Instrução CVM nº 527/2012) — divulgação voluntária de LAJIDA (EBITDA) e LAJIR por companhias abertas; usada aqui só como referência de cálculo.
- Arts. 178 a 187 da Lei nº 6.404/1976 (Lei das S.A.): grupos do balanço e da DRE.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
