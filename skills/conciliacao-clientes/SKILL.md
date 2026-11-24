---
name: conciliacao-clientes
description: "Concilia o razão de clientes (contas a receber) título a título — notas emitidas × recebimentos × devoluções —, monta a antiguidade da carteira (aging: a vencer, até 30, 31-90, 91-180, 181-360, mais de 360 dias), calcula a perda esperada pela matriz de provisão com o histórico do próprio cliente (CPC 48) e separa a perda fiscal dedutível no Lucro Real (art. 9º da Lei nº 9.430/1996, com os limites de R$ 15 mil, R$ 100 mil e R$ 50 mil do § 7º para créditos inadimplidos desde 07/10/2014). Use quando o usuário fechar balancete, revisar a carteira, precisar atualizar a PCLD/perda esperada, dar baixa de crédito incobrável, ou mencionar \"contas a receber\", \"aging\", \"inadimplência\", \"PCLD\", \"perda esperada\", \"baixa de cliente\", \"Lei 9.430\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Conciliação de Clientes (Contas a Receber)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Prova que o saldo de clientes no balancete é a soma, título a título, do que foi faturado e ainda não foi recebido. Organiza a carteira por tempo de atraso, calcula a perda esperada com base no histórico do próprio cliente e separa o que pode ser deduzido no imposto de renda, que segue regras próprias e diferentes da contabilidade.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Fechamento do mês (D+2 e D+3 do roteiro da skill `fechamento-mensal`): conciliação e revisão da perda esperada.
- Revisão da carteira com cliente inadimplente relevante, em recuperação judicial ou falência.
- Avaliação de baixa fiscal de crédito incobrável (Lucro Real).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Devedor pessoa física: identificar pelo código ou nome abreviado, sem CPF; lista de inadimplentes não sai do contexto do cliente.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Cobrança judicial, protesto e notificação extrajudicial com efeito jurídico são encaminhados a advogado (OAB). A skill só informa o status de cobrança exigido pela regra fiscal.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: Qual cliente e competência? Tenho o razão de clientes e a relação de títulos em aberto (por devedor e por título)?
Q2: Regime tributário (Lucro Real, Presumido, Simples)? Norma contábil (CPCs completos ou NBC TG 1000)?
Q3: Existe política de perda esperada? Tenho o histórico de recebimento dos últimos 12 a 24 meses por faixa de atraso?
Q4: Há devedor em recuperação judicial, falência, com título protestado ou em cobrança judicial?
Q5: Há acordos, renegociações ou devedores que são empresas ligadas, sócios ou parentes deles?
```

### 2. Conciliar o saldo
```
Saldo inicial de clientes + notas emitidas no mês − recebimentos − devoluções e abatimentos = saldo final
```
O saldo final tem de ser igual à relação de títulos em aberto. Diferença costuma ser: recebimento lançado em receita, nota cancelada sem estorno, adiantamento recebido lançado em clientes, PIX baixado no cliente errado. Recebimento parcial baixa só a parte recebida.

### 3. Antiguidade da carteira (aging)
Faixas sugeridas: a vencer · até 30 dias · 31 a 90 · 91 a 180 · 181 a 360 · mais de 360. A faixa sozinha não diz muito: a evolução de um mês para o outro diz.

### 4. Perda esperada contábil
**Empresa que adota os CPCs completos (CPC 48):** reconhecer a perda que espera ter, não só a que já aconteceu. Para contas a receber de clientes sem componente de financiamento relevante, usar a abordagem simplificada (perda esperada para toda a vida do crédito) por **matriz de provisão com o histórico do próprio cliente**:
1. Para cada faixa, apurar nos últimos 12 a 24 meses quanto do saldo daquela faixa acabou não sendo recebido.
2. Dividir o não recebido pelo saldo da faixa: é o percentual de perda da faixa.
3. Ajustar o percentual se houver motivo concreto para o futuro ser diferente do passado (crise do setor, cliente grande em dificuldade).
4. Aplicar os percentuais à carteira atual.
5. Devedor em recuperação judicial, falência ou com título protestado sai da matriz e é avaliado individualmente.

Não existe percentual padrão de mercado. Matriz copiada de outra empresa não representa a carteira deste cliente.

**Empresa que adota a NBC TG 1000 (R1) (PME):** a Seção 11 usa o modelo de perda **incorrida**: reconhecer a perda quando houver evidência objetiva de que o crédito não será recebido (atraso relevante, dificuldade financeira do devedor, recuperação judicial), avaliando individualmente os créditos relevantes e em grupo os demais. A (R1) é a revisão vigente em 15/11/2026; se o CFC publicar nova revisão da norma para PME, conferir se o modelo de perda mudou antes de aplicar.

Exemplo de matriz (percentuais do histórico de um cliente fictício):
| Faixa | Saldo | Perda histórica | Perda esperada |
|---|---|---|---|
| A vencer | 180.000,00 | 0,4% | 720,00 |
| Até 30 dias | 42.000,00 | 1,5% | 630,00 |
| 31 a 90 | 15.500,00 | 6,0% | 930,00 |
| 91 a 180 | 8.200,00 | 25,0% | 2.050,00 |
| Mais de 180 | 6.300,00 | 60,0% | 3.780,00 |
| **Total** | **252.000,00** | | **8.110,00** |

Perda esperada já registrada 6.900,00 → ajuste do mês 1.210,00. Se a necessária for menor que a registrada, a diferença volta como reversão.

Cálculo de apoio (só cálculo, sem acesso a arquivos):
```python
# Matriz de provisão: percentuais vêm do HISTÓRICO do próprio cliente (não usar percentual de mercado)
def perda_esperada(aging, matriz):
    return sum(valor * matriz.get(faixa, 0) for faixa, valor in aging.items())

aging = {"a_vencer": 180_000, "ate_30": 42_000, "31_90": 15_500, "91_180": 8_200, "mais_180": 6_300}
matriz = {"a_vencer": 0.004, "ate_30": 0.015, "31_90": 0.06, "91_180": 0.25, "mais_180": 0.60}
necessaria = perda_esperada(aging, matriz)   # 8.110,00
registrada = 6_900
print(f"Necessária: R$ {necessaria:,.2f}  Ajuste: R$ {necessaria - registrada:,.2f}")
```

### 5. Lançamentos (contas pelo nome; usar o código do plano do cliente)
```
Constituição ou reforço da perda esperada:
  D Perda esperada em créditos (despesa)          C (−) Perda esperada — PCLD (redutora de clientes)

Cliente paga um título que estava provisionado:
  D Banco                                         C Clientes
  D (−) Perda esperada — PCLD                     C Reversão de perda esperada (resultado)
  (ou o ajuste fica no recálculo da matriz do mês)

Baixa de crédito considerado incobrável:
  D (−) Perda esperada — PCLD (até o valor provisionado)
  D Perda com créditos incobráveis (despesa, pelo que faltar)
  C Clientes
```
Atenção: o recebimento é sempre a crédito de **clientes**, nunca a crédito da conta de perda esperada.

### 6. Perda fiscal (só para o Lucro Real)
- A perda esperada contábil **não é dedutível** quando registrada: provisões são indedutíveis (art. 13, I, da Lei nº 9.249/1995), exceto férias e 13º. Adicionar no e-Lalur e no e-Lacs, controlar na Parte B e, se aplicável, reconhecer IR e CSLL diferidos (CPC 32).
- A dedução só ocorre quando o crédito cumpre as condições do art. 9º da Lei nº 9.430/1996. Para contratos **inadimplidos a partir de 07/10/2014** (§ 7º, incluído pela Lei nº 13.097/2015):

| Situação | Pode deduzir quando |
|---|---|
| Devedor com insolvência declarada em sentença | a partir da sentença |
| Sem garantia, até R$ 15.000,00 por operação | vencido há mais de 6 meses, sem exigir cobrança judicial |
| Sem garantia, acima de R$ 15.000,00 até R$ 100.000,00 por operação | vencido há mais de 1 ano, sem exigir cobrança judicial, mantida a cobrança administrativa |
| Sem garantia, acima de R$ 100.000,00 | vencido há mais de 1 ano, com procedimentos judiciais iniciados e mantidos |
| Com garantia, até R$ 50.000,00 | vencido há mais de 2 anos, sem exigir cobrança judicial ou arresto das garantias |
| Com garantia, acima de R$ 50.000,00 | vencido há mais de 2 anos, com procedimentos judiciais ou arresto das garantias iniciados e mantidos |
| Devedor falido ou em recuperação judicial | na parcela que exceder o que o devedor se comprometeu a pagar |

- Contratos inadimplidos **antes** de 07/10/2014 seguem o § 1º: até R$ 5.000,00 (6 meses); acima de R$ 5.000,00 até R$ 30.000,00 (1 ano, mantida a cobrança administrativa); acima de R$ 30.000,00 (1 ano, com cobrança judicial); com garantia, 2 anos com cobrança judicial ou arresto.
- **Nunca dedutível:** perda com empresa controladora, controlada, coligada ou interligada, nem com sócio, titular, administrador ou acionista controlador, ou parente deles até o terceiro grau (art. 9º, § 6º, da Lei nº 9.430/1996).
- Registro contábil da perda dedutível: débito em resultado e crédito em clientes ou na conta redutora (art. 10 da Lei nº 9.430/1996). Se a cobrança judicial for abandonada, a perda deduzida é estornada.
- Encargos financeiros contabilizados como receita sobre crédito vencido há mais de 2 meses podem ser excluídos do lucro líquido (art. 11 da Lei nº 9.430/1996); em regra, só depois de tomadas as providências judiciais de cobrança (art. 11, § 1º), ressalvados os créditos de menor valor que dispensam cobrança judicial — conferir o enquadramento no texto do artigo.
- Crédito já deduzido e depois recuperado, a qualquer título, volta a ser tributado (art. 12 da Lei nº 9.430/1996).
- Lucro Presumido e Simples: a perda não muda o imposto, mas o registro contábil continua obrigatório.

### 7. Entregável
**a) Tabela de antiguidade e perda esperada** (modelo do passo 4), com perda registrada, necessária e ajuste a lançar.
**b) Lista de créditos que já cumprem a condição fiscal** (Lucro Real): devedor (código), valor por operação, data de vencimento, data do inadimplemento (antes ou depois de 07/10/2014), garantia, status de cobrança, enquadramento no art. 9º.
**c) Lançamentos a fazer.**
**d) Checklist:**
```
[ ] Saldo de clientes = relação de títulos em aberto
[ ] Maiores devedores conciliados título a título
[ ] Antiguidade atualizada e comparada com o mês anterior
[ ] Perda esperada recalculada pela matriz histórica (ou perda incorrida, se PME)
[ ] Devedores em RJ, falência ou protesto avaliados individualmente
[ ] Créditos com condição fiscal identificados (Lucro Real) e Lalur ajustado
[ ] Juros e multas recebidos lançados como receita financeira
[ ] Adiantamentos de clientes no passivo
```

## Erros comuns / pontos de atenção
- PIX recebido com identificação errada, baixado no cliente errado.
- Recebimento parcial baixando a nota inteira.
- Perda esperada não atualizada (ativo superavaliado).
- Tratar a perda esperada contábil como dedutível no imposto.
- Usar os limites antigos (R$ 5 mil e R$ 30 mil) para créditos inadimplidos depois de 07/10/2014.
- Deduzir perda de crédito com sócio ou empresa ligada.
- Crédito que já cumpre a condição fiscal e não é baixado (adia a dedução sem necessidade).
- Juros e multa recebidos não lançados (receita financeira subestimada).
- Desconto incondicional dado na nota não registrado como redução da receita.
- Adiantamento recebido de cliente lançado em clientes (saldo invertido).

## Casos de borda
- **Devedor em recuperação judicial ou falência:** avaliação individual da perda esperada (CPC 48); fiscalmente, dedução da parcela que exceder o valor que o devedor se comprometeu a pagar. Não usar o CPC 25, que não trata de ativos financeiros.
- **Acordo com desconto:** o desconto concedido na renegociação do crédito é despesa (descontos concedidos — despesa financeira, ou perda), não redução da receita da venda já registrada. Lançamentos: D Banco / C Clientes pelo recebido; D Descontos concedidos / C Clientes pelo restante. No Lucro Real, a dedutibilidade depende do caso: documentar o acordo e analisar com o contador responsável se o valor se enquadra como perda no recebimento de crédito (condições do art. 9º da Lei nº 9.430/1996) antes de deduzir; a recuperação posterior volta a ser tributada (art. 12 da mesma lei).

## Perguntas que o usuário costuma fazer
- **"Qual percentual de PCLD uso para 90 dias?"** O que o histórico do próprio cliente mostrar. Não há percentual padrão.
- **"Posso deduzir a PCLD no Lucro Real?"** A provisão, não. A perda, quando cumprir o art. 9º da Lei nº 9.430/1996.
- **"Cliente do Presumido precisa de PCLD?"** Sim, na contabilidade. Só o efeito fiscal é que não existe.

## Quando escalar
- Cobrança judicial, protesto, notificação com efeito jurídico: advogado parceiro (OAB).
- Cartões: `conciliacao-cartoes-credenciadora`.
- Inadimplência que aperta o caixa: `fluxo-caixa-projetado`.
- Ajustes no Lalur: `apuracao-lucro-real`.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre outro formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- CPC 48 (NBC TG 48) — Instrumentos Financeiros: perda esperada, abordagem simplificada para contas a receber.
- CPC 47 (NBC TG 47) — Receita de Contrato com Cliente.
- CPC 32 — Tributos sobre o Lucro (IR diferido).
- NBC TG 1000 (R1), Seção 11 — Instrumentos Financeiros Básicos (perda por redução ao valor recuperável de ativo financeiro, para PME). Pequena empresa e microentidade: NBC TG 1001 e NBC TG 1002, conforme a norma adotada.
- Art. 9º (caput, §§ 1º, 6º e 7º), art. 10, art. 11 e art. 12 da Lei nº 9.430/1996: dedução de perdas no recebimento de créditos, registro, encargos e recuperação. § 7º incluído pela Lei nº 13.097/2015 (conversão da Medida Provisória nº 656/2014), para contratos inadimplidos a partir de 07/10/2014.
- Art. 13, I, da Lei nº 9.249/1995: indedutibilidade das provisões.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
