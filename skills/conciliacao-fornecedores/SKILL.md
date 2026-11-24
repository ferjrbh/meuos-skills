---
name: conciliacao-fornecedores
description: "Concilia o razão de fornecedores (contas a pagar) nota a nota — notas recebidas × pagamentos × devoluções —, encontra notas em duplicidade, pagamentos em dobro, adiantamentos sem nota (reclassificar para o ativo), notas de serviço com retenções lançadas pelo líquido (IRRF, CSRF, INSS 11%, ISS), juros e multas, descontos obtidos, e prepara a circularização (confirmação de saldo) dos maiores fornecedores. Use quando o usuário fechar o mês, revisar os maiores fornecedores, preparar auditoria, receber cliente novo, ou mencionar \"contas a pagar\", \"fornecedores\", \"saldo devedor em fornecedor\", \"nota em duplicidade\", \"adiantamento a fornecedor\", \"retenção na nota de serviço\", \"circularização\", \"confirmação de saldo\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Conciliação de Fornecedores (Contas a Pagar)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Prova que o saldo de fornecedores é o que a empresa de fato deve, nota a nota. Aponta pagamento em dobro, nota lançada duas vezes, adiantamento perdido na conta de fornecedores e retenção de tributo que sumiu porque a nota foi lançada pelo líquido. Para os maiores saldos, prepara a carta de confirmação ao fornecedor.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Fechamento do mês (D+2 do roteiro da skill `fechamento-mensal`), pelo menos para os maiores fornecedores.
- Auditoria ou revisão com confirmação externa de saldos.
- Cliente novo com saldo de fornecedores herdado.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Fornecedor pessoa física (autônomo, aluguel): não repetir CPF no relatório.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite. As cartas de circularização são **minutas**: quem envia é o contador ou o cliente.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: Qual cliente e competência? Tenho o razão analítico por fornecedor e a relação de notas em aberto?
Q2: Tenho as notas recebidas no mês e os comprovantes de pagamento (boleto, PIX, transferência)?
Q3: Há adiantamentos pagos sem nota ainda?
Q4: Há notas de serviço com retenção (IRRF, CSRF, INSS 11%, ISS)? Regime do prestador (Simples ou não)?
Q5: (auditoria) Quando foi a última confirmação de saldo? Quais fornecedores entram?
```

### 2. Conferência por fornecedor
```
FORNECEDOR EXEMPLO   CNPJ 00.000.000/0001-00
Saldo inicial do razão: R$ __

+ Notas do mês (lançar o passivo pelo líquido a pagar e as retenções em contas próprias):
   NF __  Valor bruto R$ __  Vencimento __/__/__
− Pagamentos do mês:
   Boleto/PIX __  Valor R$ __  Pago em __/__/__
− Devoluções (com nota de devolução)
± Juros, multas e descontos (ver passo 4)

= Saldo esperado: R$ __
Saldo final do razão: R$ __
DIFERENÇA: R$ __ (motivo: __)
```
Fórmula geral: saldo inicial + notas recebidas − pagamentos − devoluções ± juros, multas e descontos = saldo final. O saldo final tem de bater com a relação de notas em aberto e, para os maiores, com a posição informada pelo próprio fornecedor.

### 3. Nota de serviço com retenção: despesa pelo bruto, fornecedor pelo líquido
O tomador lança a despesa pelo valor total da nota. O que foi retido vira obrigação a recolher em contas próprias; o fornecedor recebe o líquido.

Exemplo: nota de serviço profissional de R$ 1.000,00, prestador fora do Simples, município exige retenção de ISS de 5% (valores ilustrativos; a retenção do ISS e a alíquota dependem da lei do município):
```
D Despesa com serviços de terceiros         1.000,00 (bruto da nota)
   C Fornecedores (líquido a pagar)            888,50
   C IRRF retido a recolher (1,5%)              15,00   (código 1708)
   C PIS/COFINS/CSLL retidos a recolher (4,65%) 46,50   (código 5952)
   C ISS retido a recolher (5%)                 50,00   (guia do município)
```
- IRRF e CSRF retidos: informados na EFD-Reinf (R-4020) e recolhidos pela DCTFWeb (DARF gerado nela). INSS de 11% sobre cessão de mão de obra ou empreitada: R-2010 na EFD-Reinf e recolhimento pela DCTFWeb.
- CSRF: dispensada quando o valor retido em um pagamento for de até R$ 10,00 (pagamento de até R$ 215,05 a 4,65%), avaliando cada pagamento isoladamente (art. 31, § 3º, da Lei nº 10.833/2003, com a redação da Lei nº 13.137/2015).
- Prestador optante do Simples Nacional, com declaração entregue, em regra não sofre retenção de IRRF e CSRF; o INSS de 11% só se aplica a optante tributado em anexo que recolhe a contribuição patronal à parte (Anexo IV), e o ISS segue a lei do município.
- Conferir o enquadramento de cada nota antes de lançar (skill ou agente de retenções do tomador): alíquota, código e dispensa variam pelo tipo de serviço.

Lançar pelo líquido diminui a despesa e faz as retenções desaparecerem: a guia não é emitida e o tributo fica sem recolher.

### 4. O que costuma aparecer
| Achado | Tratamento |
|---|---|
| Saldo devedor em um fornecedor | pagamento em duplicidade ou adiantamento: reclassificar para adiantamentos a fornecedores (ativo) e cobrar a nota ou a devolução |
| Adiantamento pago sem nota | adiantamentos a fornecedores (ativo circulante ou longo prazo), nunca como saldo devedor dentro de fornecedores |
| Mesma nota lançada duas vezes | estornar uma |
| Nota recebida e não lançada | lançar na competência da emissão |
| Juros e multa por atraso | despesa financeira, não aumento do custo da compra |
| Desconto por pagamento antecipado (condicional) | receita financeira (descontos obtidos) |
| Desconto incondicional destacado na nota | reduz o custo da compra; já entra pelo valor líquido da nota |
| Devolução de mercadoria sem nota de devolução | não baixar o passivo sem documento: pedir a nota |

### 5. Confirmação de saldo (circularização)
Para os maiores saldos, e sempre em ano de auditoria, pedir ao fornecedor a confirmação do saldo em aberto. Em auditoria independente, o procedimento segue a NBC TA 505 (confirmação externa) e é controlado pelo auditor.

Minuta (o contador ou o cliente envia):
```
EMPRESA EXEMPLO LTDA — CNPJ 00.000.000/0001-00
Ao FORNECEDOR EXEMPLO

Solicitamos confirmar o saldo em aberto em nossos registros em __/__/____, no valor de R$ __.
Havendo divergência, pedimos informar o saldo em seus registros e enviar o extrato analítico das notas em aberto.
Resposta para: [contato do escritório].
```

### 6. Entregável
**a) Planilha consolidada dos maiores fornecedores**
```
Fornecedor          Saldo razão   Saldo confirmado   Diferença   Investigar?
FORNECEDOR EXEMPLO  R$ __         R$ __              R$ __       sim/não
```
**b)** Espelho por fornecedor com as pendências.
**c)** Minutas de confirmação de saldo (se houver auditoria ou fornecedor relevante).
**d)** Lançamentos para regularizar as pendências.
**e)** Checklist:
```
[ ] Saldo de fornecedores = relação de notas em aberto
[ ] Maiores fornecedores conciliados nota a nota
[ ] Saldos devedores reclassificados para adiantamentos a fornecedores
[ ] Notas em duplicidade estornadas
[ ] Notas de serviço com retenção lançadas pelo bruto, retenções em contas próprias e conferidas com a EFD-Reinf
[ ] Juros e multas em despesa financeira; descontos obtidos em receita financeira
[ ] Confirmações de saldo enviadas e respondidas (quando aplicável)
```

## Erros comuns / pontos de atenção
- Nota de serviço com retenção lançada pelo líquido (despesa menor e tributo retido sem recolher).
- Adiantamento deixado em fornecedores como saldo devedor.
- Pagamento feito pelo sócio "por fora", sem registro: passivo ou despesa oculta; registrar com documento (conta-corrente com o sócio).
- Devolução de mercadoria sem nota, gerando duplicidade.
- Cheque pré-datado compensado antes da data esperada (débito inesperado no banco).
- Cadastro de pessoa física como jurídica ou o contrário (CPF × CNPJ), que muda a retenção.

## Casos de borda
- **Fornecedor estrangeiro (importação):** custo com Imposto de Importação, IPI, PIS/COFINS-Importação e ICMS, conforme o regime; variação cambial do passivo até o pagamento.
- **Fornecedor falido ou em recuperação judicial:** a dívida com ele continua devida. A perda existe para o **adiantamento** pago a ele sem entrega: avaliar a redução ao valor recuperável do adiantamento (ativo financeiro).
- **Adiantamento sem nota há mais de 6 meses:** investigar; pode ser empréstimo disfarçado ou pagamento sem contrapartida.
- **Passivo antigo sem cobrança do fornecedor:** não baixar por conta própria; documentar a prescrição ou a renúncia antes de levar ao resultado.

## Perguntas que o usuário costuma fazer
- **"Fornecedor com saldo devedor, deixo assim?"** Não. Reclassificar para adiantamentos a fornecedores e descobrir se é pagamento em dobro ou adiantamento.
- **"Retenção de CSRF de R$ 8,00, preciso reter?"** Não: valor retido de até R$ 10,00 por pagamento é dispensado (art. 31, § 3º, da Lei nº 10.833/2003).
- **"Quantos fornecedores preciso conciliar?"** Todos devem bater com a relação de notas em aberto; os maiores (por exemplo, os 20 maiores saldos) são conferidos nota a nota todo mês.

## Quando escalar
- Conciliação bancária dos pagamentos: `conciliar-extrato-razao`.
- Retenções em detalhe: `retencoes-tributarias-tomador`; EFD-Reinf: `efd-reinf`.
- Provisões e contingências: `fechamento-mensal`.
- Créditos de PIS/COFINS sobre insumos: `recuperacao-creditos-pis-cofins`.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre outro formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- ITG 2000 (R1) — Escrituração Contábil.
- NBC TG 26 / CPC 26 (R1) — Apresentação das Demonstrações Contábeis (classificação de passivos e ativos).
- CPC 48 (NBC TG 48) e NBC TG 1000 (R1), Seção 11 — instrumentos financeiros (passivo com fornecedores, adiantamentos). Pequena empresa e microentidade: NBC TG 1001 e NBC TG 1002, conforme a norma adotada.
- NBC TA 505 — Confirmações Externas (auditoria).
- Retenções na fonte: art. 714 do RIR/2018 (Decreto nº 9.580/2018) para IRRF de serviços profissionais; arts. 30 a 32 da Lei nº 10.833/2003 para a CSRF de 4,65% (dispensa de até R$ 10,00 no art. 31, § 3º, com a redação da Lei nº 13.137/2015); art. 31 da Lei nº 8.212/1991 para a retenção de 11% do INSS; Lei Complementar nº 116/2003 e lei do município para o ISS.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
