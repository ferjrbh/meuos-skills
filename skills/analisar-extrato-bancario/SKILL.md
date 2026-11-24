---
name: analisar-extrato-bancario
description: "Lê extratos bancários (PDF ou OFX) e relatórios de caixa, classifica cada transação contabilmente, concilia o saldo do extrato com o saldo do razão item a item e entrega diagnóstico com divergências e lançamentos a fazer. Use quando o usuário enviar extrato bancário, OFX, relatório de caixa, ou mencionar \"conciliação bancária\", \"extrato\", \"OFX\", \"movimentação financeira\", \"saldo de caixa\", \"TED/PIX\", \"tarifa bancária\", \"aplicação financeira\", \"classificar transações do banco\", \"conferir razão com extrato\" ou \"saldo não bate\". Acione também para revisar saldo de banco ou caixa e identificar transações não classificadas, mesmo sem citar norma (ITG 2000 (R1), NBC TG 1000 (R1) Seção 7, NBC TG 03)."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Analisar Extrato Bancário e de Caixa

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Lê o extrato do banco (PDF ou OFX) ou o relatório de caixa, classifica cada movimento com a sugestão de lançamento a débito e a crédito e concilia o saldo do extrato com o saldo do razão contábil, linha a linha. Entrega a lista do que falta lançar, do que está em trânsito e do que precisa de informação do cliente.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Fechamento do mês, antes do balancete (etapa D+2 do roteiro da skill `fechamento-mensal`).
- Cliente novo com saldo de banco que não bate com o razão.
- Classificação de um lote de transações de banco ou caixa ainda não lançadas.
- Para o casamento linha a linha com o razão e o espelho arquivado, usar `conciliar-extrato-razao`.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Extratos trazem nome e CPF de quem pagou ou recebeu PIX: no relatório, identificar a contraparte pelo mínimo necessário (nome abreviado ou "CLIENTE EXEMPLO"), sem repetir CPF.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Receber e validar o documento
Tipos aceitos:
- Extrato bancário em PDF (formato do banco). PDF escaneado (imagem): extrair o texto por OCR e conferir as somas contra os totais impressos no próprio extrato antes de usar; PDF nativo com texto duplicado ou embaralhado: filtrar a camada de texto real antes de ler. Nunca usar extração sem essa conferência.
- Extrato em OFX: extrair BANKID, ACCTID, DTSTART, DTEND, LEDGERBAL e cada STMTTRN (DTPOSTED, TRNAMT, MEMO, FITID). O FITID é o identificador único do movimento: usar para evitar lançar o mesmo item duas vezes.
- Relatório de movimentação de caixa (PDF ou texto).

Antes de classificar, validar o extrato:
1. Titular, banco, agência, conta e período corretos.
2. Saldo inicial igual ao saldo final do extrato do mês anterior.
3. Saldo recalculado linha a linha igual ao saldo final impresso. Divergência aqui é problema de leitura do arquivo, não de contabilidade.

Pedir também o razão da conta contábil e o saldo inicial do razão. Sem o razão, fazer só a classificação e avisar que a conciliação ficou pendente.

### 2. Classificar cada transação
Contas citadas pelo nome. Usar sempre o código do plano de contas do cliente.

**Entradas (créditos no extrato)**
| Natureza | Débito | Crédito | Atenção |
|---|---|---|---|
| Recebimento de cliente | Banco | Clientes | Não lançar como receita: a receita já entrou pela nota fiscal |
| Resgate de aplicação | Banco | Aplicações financeiras | Resgate não é receita. Receita é só o rendimento |
| Rendimento de aplicação | Aplicações ou Banco (líquido) e IRRF a compensar (retido) | Receita financeira (bruto) | Lançar o rendimento bruto, com o imposto retido em conta própria |
| Aporte de capital | Banco | Capital social a integralizar (baixa) ou Adiantamento para futuro aumento de capital | Só vai a capital com alteração contratual registrada; sem ela, perguntar se é adiantamento ou empréstimo do sócio |
| Empréstimo recebido | Banco | Empréstimos e financiamentos | Conferir com o contrato |
| Transferência de outra conta da mesma empresa | Banco (destino) | Banco (origem) | Registrar uma vez só, como transferência |
| Crédito sem identificação | Banco | Conta transitória no passivo (valores a identificar) | Nunca lançar como receita: pode ser aporte, empréstimo ou devolução |

**Saídas (débitos no extrato)**
| Natureza | Débito | Crédito | Atenção |
|---|---|---|---|
| Pagamento a fornecedor | Fornecedores | Banco | Baixa do passivo já registrado pela nota |
| Pagamento de salários | Salários a pagar | Banco | Não lançar como despesa de novo: a folha já foi provisionada |
| Recolhimento de INSS, FGTS, IRRF, DAS, DARF | Tributo ou encargo a recolher | Banco | Mesma regra: baixa do passivo |
| Tarifa bancária, IOF | IOF e tarifas bancárias (despesa financeira) | Banco | Não deixar acumular como diferença |
| Juros e encargos de empréstimo | Empréstimos (principal) e Juros passivos (despesa) | Banco | Separar principal de juros pelo contrato |
| Aplicação financeira | Aplicações financeiras | Banco | Transferência, não despesa |
| Saída para sócio | depende da natureza: Pró-labore a pagar, Lucros/dividendos a pagar ou Mútuo a receber de sócio | Banco | Perguntar a natureza. Lucro distribuído precisa de lucro apurado; sem isso, é empréstimo ao sócio |
| Transferência para empresa ligada | Conta-corrente ou mútuo com a empresa ligada | Banco | Nunca lançar como despesa |

**Transações com histórico genérico** ("TED", "PIX", "Transferência", "Pagamento"): marcar como **não identificadas** e listar para o cliente. Nunca presumir a natureza.

### 3. Conciliar o saldo, item a item
Casar primeiro um para um (mesmo valor, mesmo sentido, data próxima), depois em grupo (um lançamento para vários movimentos, como folha paga por vários PIX). Conciliar só pelo saldo final esconde erros que se compensam.

Estrutura da conciliação (pelos dois lados):
```
Saldo no extrato bancário (data final)            R$ [X]
(+) Depósitos lançados no razão e ainda não creditados pelo banco (em trânsito)   R$ [X]
(−) Pagamentos lançados no razão e ainda não debitados (cheques, agendamentos)   R$ [X]
(=) Saldo ajustado do extrato                     R$ [X]

Saldo na conta contábil (razão)                   R$ [X]
(+) Créditos do extrato ainda não lançados (rendimentos, recebimentos)   R$ [X]
(−) Débitos do extrato ainda não lançados (tarifas, IOF, débitos automáticos)   R$ [X]
(=) Saldo contábil ajustado                       R$ [X]

Diferença (tem de ser zero)                       R$ [X]
```
Os itens da segunda parte viram **lançamentos a fazer**. Os itens em trânsito não geram lançamento: devem aparecer no extrato do mês seguinte (conferir no próximo fechamento).

Exemplo (dados fictícios):
```
Saldo do razão em 31/10 ...........................  42.180,35
(−) tarifa de outubro, só no extrato ...............     −86,40
(+) rendimento da aplicação, só no extrato .........    +312,77
(=) Saldo contábil ajustado ........................  42.406,72
Saldo do extrato em 31/10 ..........................  47.806,72
(−) pagamento lançado em 31/10, debitado em 03/11 ..  −5.400,00
(=) Saldo ajustado do extrato ......................  42.406,72   → diferença 0,00
```

### 4. Validações específicas
- **Caixa (dinheiro em espécie):** o saldo nunca pode ser credor (negativo). Saldo credor indica pagamento lançado sem a entrada correspondente ou entrada não lançada.
- **Banco com saldo credor no razão:** se o extrato também está negativo, é uso de cheque especial ou conta garantida e deve ser apresentado no passivo (empréstimos), não como banco negativo no ativo.
- **Aplicações como equivalentes de caixa:** só quando são de curto prazo, de alta liquidez, prontamente conversíveis em valor conhecido de caixa e com risco insignificante de mudança de valor, normalmente com vencimento de até três meses contados da data da aquisição (item 7.2 da NBC TG 1000 (R1) e NBC TG 03 — Demonstração dos Fluxos de Caixa). Aplicação de prazo maior ou com risco de valor fica fora do caixa na DFC.
- **Diferença de centavos:** investigar; não lançar como "arredondamento" sem saber a origem.

### 5. Formato de saída
Entregar, nesta ordem:
1. Identificação da conta (banco, agência, conta, período) e resultado da validação do extrato.
2. Tabela de transações classificadas (data, valor, histórico, débito, crédito, status: conciliado / falta lançar / em trânsito / não identificado / duplicidade / valor divergente).
3. Bloco de transações não identificadas, para o cliente informar a natureza.
4. Conciliação no formato do passo 3.
5. Lista de lançamentos a fazer.
6. Resumo executivo (totais de entradas e saídas, diferença final, alertas).

## Erros comuns / pontos de atenção
- Lançar recebimento de cliente como receita (receita contada duas vezes).
- Lançar pagamento de salário ou tributo como despesa, quando o passivo já estava provisionado.
- Tratar resgate de aplicação como receita.
- Lançar a saída e a entrada de uma transferência entre contas da mesma empresa como dois fatos diferentes.
- Crédito sem identificação lançado como receita.
- Arquivo OFX importado duas vezes (conferir FITID e se o arquivo já foi importado antes de gerar outro).
- Relatório de razão que mostra o saldo na natureza da conta pode enganar quem deduz débito e crédito pelo sinal.

## Perguntas que o usuário costuma fazer
- **"Não tenho o razão, dá para fazer?"** Dá para classificar as transações; a conciliação fica pendente até receber o razão e o saldo contábil.
- **"Esse PIX sem nome eu lanço como receita?"** Não. Vai para uma conta transitória no passivo até o cliente dizer o que é.
- **"CDB com liquidez diária é equivalente de caixa?"** Normalmente sim, se puder ser resgatado a qualquer momento sem perda relevante de valor; conferir as condições do título.

## Restrições
- Nunca omitir transações: todas aparecem no relatório.
- Não conciliar definitivamente nem lançar no sistema: a skill analisa e aponta; o contador decide e lança.

## Base legal usada nesta skill
- ITG 2000 (R1) — Escrituração Contábil (CFC): registro de todos os fatos, documentação de suporte e retificação de lançamentos.
- NBC TG 1000 (R1) — Contabilidade para Pequenas e Médias Empresas, Seção 7 (Demonstração dos Fluxos de Caixa; item 7.2, equivalentes de caixa) e Seção 11 (Instrumentos Financeiros Básicos — caixa, contas a receber e a pagar, empréstimos). Pequenas empresas (receita bruta anual acima de R$ 4,8 milhões até R$ 78 milhões) podem adotar a NBC TG 1001, e microentidades (até R$ 4,8 milhões, limite do art. 3º, II, da Lei Complementar nº 123/2006), a NBC TG 1002, ambas vigentes para exercícios iniciados a partir de 01/01/2023.
- NBC TG 03 (CPC 03) — Demonstração dos Fluxos de Caixa: conceito de caixa e equivalentes de caixa.
- Estrutura Conceitual (NBC TG Estrutura Conceitual / CPC 00 (R2)): representação fidedigna.
- Art. 177 da Lei nº 6.404/1976 (Lei das S.A.): regime de competência e escrituração.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
