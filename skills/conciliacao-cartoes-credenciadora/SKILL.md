---
name: conciliacao-cartoes-credenciadora
description: "Concilia as vendas no cartão e no PIX por maquininha (Cielo, Stone, Rede, GetNet, PagSeguro, SafraPay, Mercado Pago e outras) com os repasses da credenciadora — separa taxa por transação (MDR), antecipação, cancelamentos, contestações (chargeback), vale-refeição e PIX, controla o saldo a receber da credenciadora e reconhece a receita pelo valor BRUTO, com a taxa como despesa à parte. Use quando o cliente for comércio ou e-commerce com volume de cartão, quando a conciliação de cartões do mês não fechar, houver antecipação de recebíveis, ou o usuário mencionar \"maquininha\", \"credenciadora\", \"MDR\", \"taxa de cartão\", \"repasse\", \"antecipação\", \"chargeback\", \"cartões a receber\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Conciliação de Cartões e Credenciadoras

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Compara três fontes: as vendas do sistema do cliente (PDV/ERP), o relatório de vendas da credenciadora e os repasses que caíram no banco. Controla o saldo a receber de cada credenciadora, separa as taxas e as antecipações, e propõe os lançamentos com a receita pelo valor bruto.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Fechamento do mês de cliente com vendas no cartão (D+2 do roteiro da skill `fechamento-mensal`).
- Saldo de "cartões a receber" que não bate ou que zera logo depois da venda.
- Mês com antecipação de recebíveis, contestações ou troca de credenciadora.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Relatórios de credenciadora podem trazer nome do portador e parte do número do cartão: não reproduzir.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Não acessar o portal da credenciadora com senha do cliente: pedir que o cliente exporte os relatórios.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: Qual cliente e competência? Quais credenciadoras e quais canais (loja física, e-commerce, gateway)?
Q2: Tenho o relatório de vendas e o relatório de recebimentos (agenda/extrato de repasses) de cada credenciadora?
Q3: Quais as taxas contratadas por modalidade? Houve antecipação no mês?
Q4: Houve contestações (chargeback), cancelamentos, vale-refeição/alimentação?
Q5: O sistema do cliente lança a venda pelo bruto e a taxa à parte, ou pelo líquido do repasse?
```

### 2. Modalidades (referência de mercado, conferir sempre o contrato do cliente)
```
Modalidade                          Prazo usual de repasse          Taxa (referência de mercado)
Débito                              D+1 ou D+2                      ~1,0 a 1,5%
Crédito à vista                     D+30                            ~1,8 a 3,0%
Crédito parcelado pelo lojista      cada parcela a cada 30 dias     ~2,0 a 3,5%
Crédito parcelado pelo emissor      como crédito à vista (D+30)     taxa do crédito; os juros são cobrados do comprador pelo banco emissor, não afetam o lojista
Vale-refeição/alimentação           conforme a bandeira             ~3,5 a 5,0%
PIX por maquininha/QR da credenciadora  D+0 ou D+1                  ~0,3 a 1,0%
PIX direto na conta da empresa      imediato                        tarifa do banco, se houver
Antecipação de recebíveis           imediato                        desconto proporcional ao prazo antecipado
```
Os percentuais são só ordem de grandeza: a conciliação usa a taxa do contrato e a do relatório.

### 3. Controle do saldo a receber, por credenciadora
```
Saldo inicial a receber
+ vendas no cartão do período (pelo valor bruto)
− taxas cobradas
− valores antecipados e custo da antecipação
− cancelamentos e contestações
− repasses creditados no banco
= saldo final a receber          → bate com a agenda de recebíveis da credenciadora
```
Casar também: total de vendas do PDV/ERP = total de vendas do relatório da credenciadora; repasses do relatório = créditos no extrato bancário.

### 4. Lançamentos (contas pelo nome; usar o código do plano do cliente)
**Venda no crédito, R$ 1.000,00, taxa 2,5%:**
```
Na venda (receita pelo BRUTO):
  D Valores a receber de credenciadora     1.000,00
  C Receita de vendas                       1.000,00
Taxa (na competência da venda):
  D Despesa com taxas de cartão                25,00
  C Valores a receber de credenciadora         25,00
No repasse (D+30):
  D Banco                                    975,00
  C Valores a receber de credenciadora        975,00
```
**Venda parcelada pelo lojista:** R$ 1.200,00 em 3 parcelas, taxa de 3,2% = 38,40. Na venda, D Valores a receber 1.200,00 / C Receita 1.200,00; taxa D Despesa 38,40 / C Valores a receber 38,40; em cada repasse mensal, D Banco 387,20 / C Valores a receber 387,20. O saldo a receber fica aberto nos meses seguintes.

**Antecipação de recebíveis (desconto de 25,00 sobre 975,00 a receber):**
```
  D Banco                                         950,00
  D Despesa financeira — antecipação de recebíveis  25,00
  C Valores a receber de credenciadora             975,00
```
O custo da antecipação é despesa financeira, nunca redução da receita de vendas.

**Cancelamento ou contestação (chargeback):**
```
Venda cancelada ou devolvida (ainda não repassada):
  D Vendas canceladas / devoluções (redutora da receita)
  C Valores a receber de credenciadora
Contestação de venda já repassada, debitada pela credenciadora:
  D Vendas canceladas (se a venda é desfeita) ou Perdas com contestações (se a mercadoria foi entregue e a contestação é por fraude)
  C Banco (ou Valores a receber de credenciadora, se descontado de repasses futuros)
Taxa cobrada pela contestação:
  D Despesa com taxas de cartão
  C Banco ou Valores a receber de credenciadora
```
Se houver como cobrar o comprador, registrar o valor em clientes em vez de perda.

**Classificação da taxa por transação (MDR):** registrar em conta própria ("Despesa com taxas de cartão"). Se fica em despesas comerciais ou em despesas financeiras é política contábil da empresa: escolher, documentar e manter igual todo mês. A antecipação é sempre despesa financeira.

### 5. Efeito tributário
A base dos tributos sobre a venda (Simples Nacional, PIS, COFINS, ICMS, ISS) é a receita **bruta**: a taxa da credenciadora não reduz a base. Venda lançada pelo líquido do repasse faz o cliente recolher a menos e cria divergência com as informações que as instituições de pagamento enviam ao fisco. Para os estados, essas informações vão na DIMP — Declaração de Informações de Meios de Pagamento (Convênio ICMS nº 134/2016 e alterações), cruzada pelas Secretarias da Fazenda com as vendas declaradas pelo contribuinte.

### 6. Entregável
**a) Tabela vendas × repasses, por credenciadora (exemplo fictício)**
```
CREDENCIADORA: CREDENCIADORA EXEMPLO   Período: 10/2026

Total de vendas no PDV/ERP:                R$ 100.000,00
Total de vendas no relatório da credenciadora: R$ 100.000,00 (diferença 0,00)

REPASSES DO MÊS:
  Débito:                                  R$ 25.000,00
  PIX por QR:                              R$ 10.000,00
  Crédito à vista de setembro:             R$ 30.000,00
  Parcelas de vendas anteriores:           R$ 15.000,00
  Antecipações:                            R$ 10.000,00
                                           ─────────────
Total bruto repassado:                     R$ 90.000,00
(−) taxas, antecipação e tarifas:          R$  4.500,00
                                           ─────────────
Total líquido creditado no banco:          R$ 85.500,00

SALDO A RECEBER (fim do mês):              R$ 60.000,00  (bate com a agenda da credenciadora)
CONTESTAÇÕES DO MÊS:                       R$ 1.200,00 (3 transações)
CANCELAMENTOS:                             R$ 800,00
```
**b)** Lançamentos consolidados do mês.
**c)** Memória de cálculo por modalidade.
**d)** Alerta: se o sistema do cliente reconhece a receita pelo líquido, pedir o ajuste (CPC 47: receita pelo preço da transação, com a taxa como despesa).

## Erros comuns / pontos de atenção
- Receita lançada pelo valor líquido do repasse (distorce a DRE e reduz a base de tributos).
- Antecipação registrada como receita financeira ou como redução da venda (é despesa financeira).
- Vendas parceladas sem controle das parcelas futuras (saldo a receber zerado logo após a venda é sinal de lançamento pelo líquido).
- Vale-refeição tratado como cartão de crédito (taxa e prazo diferentes).
- E-commerce com gateway e credenciadora: duas taxas, que precisam aparecer separadas.
- Contestação lançada a débito de valores a receber (aumenta o ativo em vez de reduzir).

## Casos de borda
- **Cliente novo na credenciadora:** retenção de parte das vendas como reserva de garantia; controlar em conta própria até a liberação.
- **Loja física e e-commerce na mesma empresa:** conciliar por canal, com relatórios separados.
- **Troca ou encerramento de contrato com a credenciadora:** acompanhar o recebimento do saldo residual até zerar.
- **Preço diferente por forma de pagamento:** permitido (Lei nº 13.455/2017). O desconto dado ao cliente para pagar no PIX ou no dinheiro, quando incondicional e destacado na nota, reduz a receita; a taxa da credenciadora não.

## Perguntas que o usuário costuma fazer
- **"Posso lançar só o que caiu no banco?"** Não. A receita é o valor que o cliente pagou; a taxa é despesa à parte.
- **"MDR é despesa financeira?"** Depende da política contábil da empresa (comercial ou financeira); o importante é conta própria e critério uniforme. A antecipação é sempre financeira.

## Quando escalar
- Conciliação bancária dos repasses: `conciliar-extrato-razao`.
- Cliente com aperto de caixa por antecipações frequentes: `fluxo-caixa-projetado`.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre outro formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- CPC 47 (NBC TG 47) — Receita de Contrato com Cliente: receita pelo preço da transação (valor a que a entidade tem direito).
- CPC 48 (NBC TG 48) — Instrumentos Financeiros: valores a receber da credenciadora como ativo financeiro.
- Lei nº 13.455/2017: autoriza a diferenciação de preços em função do prazo ou do instrumento de pagamento.
- Art. 187 da Lei nº 6.404/1976 (Lei das S.A.): receita bruta e deduções na DRE.
- NBC TG 1000 (R1), Seções 11 e 23 (instrumentos financeiros básicos e receitas), para PME; pequena empresa e microentidade, NBC TG 1001 e NBC TG 1002, conforme a norma adotada.
- Convênio ICMS nº 134/2016 (CONFAZ) — informações das instituições e intermediadores de pagamento aos estados (DIMP).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
