---
name: conciliar-extrato-razao
description: "Faz o casamento item a item entre o extrato bancário (OFX, CSV ou PDF) e o razão contábil da conta banco. Aponta lançamentos sem par, tarifas, IOF, juros e rendimentos não contabilizados, diferenças de data e de valor, e gera a lista de ajustes a lançar, fechando com diferença zero. Diferença para a skill analisar-extrato-bancario, que classifica as transações do extrato e concilia saldos de forma consolidada; esta cruza extrato e razão linha a linha para achar o que falta contabilizar. Acionar quando o usuário disser \"conciliar extrato com razão\", \"batimento bancário\", \"conciliação item a item\", \"o banco não bate com a contabilidade\", \"lista de pendências da conciliação\" ou enviar extrato e razão juntos."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Conciliar extrato bancário × razão contábil

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Compara, linha por linha, o extrato do banco com o razão da conta banco na contabilidade. Cada movimento de um lado procura o seu par no outro; o que sobra recebe um motivo e uma ação. O resultado é o espelho de conciliação com diferença final zero e a lista de lançamentos que faltam no razão.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Fechamento do mês, antes de gerar o balancete (passo D+2 do roteiro da skill `fechamento-mensal`).
- Cliente novo com saldo de banco que não bate com o extrato.
- Saldo de banco invertido ou parado no balancete.
- Para conciliar cartões e credenciadoras, usar `conciliacao-cartoes-credenciadora`; para fornecedores e clientes, `conciliacao-fornecedores` e `conciliacao-clientes`.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Extrato traz nomes e CPFs de quem pagou ou recebeu PIX: na resposta, identificar pelo primeiro nome ou pela função ("pagamento a empregado"), nunca pelo CPF.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e lança.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: Cliente (CNPJ), conta (banco, agência, conta corrente) e competência?
Q2: Tenho o extrato do mês (OFX/CSV/PDF), o razão contábil da conta e o saldo inicial?
Q3: Há cheques emitidos ou pagamentos agendados ainda não compensados?
Q4: Há PIX ou depósito recebido sem identificação no mês?
```

### 2. Validar o extrato antes de usar
- Titular, conta e período corretos.
- Saldo inicial do extrato igual ao saldo final do mês anterior.
- Saldo recalculado linha a linha igual ao saldo impresso.
- Extrato em PDF escaneado: extrair por OCR e conferir as somas com os totais impressos no próprio extrato antes de usar.

### 3. Casar os movimentos
1. **Um para um:** mesmo valor, mesmo sentido, data próxima.
2. **Em grupo:** um lançamento para vários movimentos (folha paga em vários PIX, tributos pagos juntos) ou o contrário.
3. **Classificar o que sobrou:** falta lançar · em trânsito · lançado em duplicidade · valor divergente.

### 4. Lançamento padrão por tipo de movimento
Códigos de um plano-modelo, só como referência (usar sempre o código do plano do cliente):
```
Movimento                      Lançamento
Recebimento de cliente         D 1.1.1.02 Banco / C 1.1.2.01 Clientes
Crédito sem identificação      D Banco / C conta transitória do passivo (2.1.5 Outras obrigações) até achar a origem
Pagamento a fornecedor         D 2.1.1.01 Fornecedores / C Banco
Tarifa bancária e IOF          D 5.4 Despesas financeiras (subconta tarifas / IOF) / C Banco
Rendimento de aplicação        D Banco ou Aplicação (líquido) + D IRRF a compensar (retido) / C 4.4 Receitas financeiras (bruto)
Aplicação e resgate            D Aplicação / C Banco (e o contrário): é transferência, não receita
Parcela de empréstimo          D 2.1.2.01 Empréstimos (principal) + D 5.4 Juros passivos / C Banco
Folha (pagamento)              D 2.1.3.01 Salários a pagar / C Banco (baixa do passivo já provisionado)
Tributos (pagamento)           D 2.1.4 Tributo a recolher / C Banco
Transferência entre contas     D Banco destino / C Banco origem, registrada uma vez só
Transferência a sócio/ligada   conta de mútuo ou conta-corrente entre as partes (nunca despesa ou receita)
Estorno                        lançamento ao contrário do lançamento estornado
```

### 5. Pendências
**Só no extrato (falta lançar no razão):** tarifas, juros, IOF, rendimentos, débitos automáticos, devoluções, estornos.
**Só no razão (ainda não passou no banco):** cheques emitidos não compensados, pagamentos agendados, depósitos em trânsito, erro de digitação.

Fórmula de fechamento:
```
Saldo do razão no fim do mês
+ créditos que estão no extrato e ainda não foram lançados
− débitos que estão no extrato e ainda não foram lançados
− depósitos lançados no razão que o banco ainda não creditou (em trânsito)
+ pagamentos lançados no razão que o banco ainda não debitou (cheque ou agendamento)
= Saldo do extrato no fim do mês            → diferença: zero
```
Como lembrar: o que está só no razão é desfeito (sinal trocado); o que está só no extrato é acrescentado (sinal do banco).

### 6. Entregável
**a) Espelho de conciliação:**
```
Conta: 1.1.1.02.01 Banco Exemplo c/c 0000-0   Período __/__/__ a __/__/__
Saldo inicial razão: R$ __  =  Saldo inicial extrato: R$ __ (conferido)

ITENS DO EXTRATO COM LANÇAMENTO:
__/__ PIX cliente CLIENTE EXEMPLO     +5.000,00   D Banco / C Clientes
__/__ Tarifa de manutenção               −25,00   D Desp. financeiras / C Banco
__/__ IOF                                −12,00   D Desp. financeiras / C Banco
__/__ Rendimento aplicação (líq.)        +85,00   D Banco + D IRRF a compensar / C Receita financeira (bruto)
... (todos os itens)

SÓ NO RAZÃO (ainda não no extrato):
- Cheque 000123 a FORNECEDOR EXEMPLO   −1.500,00 (compensação prevista em __)
- Depósito em trânsito CLIENTE EXEMPLO   +800,00

Saldo final razão (após lançar os itens só do extrato):  R$ __
+ Cheques/pagamentos não compensados:                    R$ __
− Depósitos em trânsito:                                 R$ __
= Saldo conciliado:                                      R$ __
Saldo final extrato:                                     R$ __
DIFERENÇA:                                               R$ 0,00 (tem de ser zero)
```
**b) Lista de lançamentos a fazer** (o que está só no extrato), já com débito, crédito e histórico.
**c) Memória de cálculo** salva na pasta do cliente, na competência (não em pasta temporária).
**d) Checklist:**
```
[ ] Saldo inicial do razão = saldo inicial do extrato
[ ] Todos os itens do extrato com lançamento ou com pendência explicada
[ ] Tarifas e IOF lançados
[ ] Rendimentos reconhecidos pelo bruto, com o IRRF retido em conta própria
[ ] Cheques e agendamentos pendentes mapeados
[ ] Depósitos em trânsito identificados
[ ] Diferença final zero
[ ] Espelho arquivado na pasta da competência
```

## Erros comuns / pontos de atenção
- Conciliar só pelo saldo final: dois erros de sinal contrário se anulam e o saldo "fecha" errado.
- Tarifas e IOF acumulados em "Outros".
- Crédito sem identificação lançado como receita: pode ser aporte de sócio, empréstimo ou devolução.
- Recebimento de cliente lançado como receita (a receita já entrou pela nota fiscal).
- Pagamento de folha ou tributo lançado de novo como despesa (o passivo já estava provisionado).
- Resgate de aplicação tratado como receita: receita é só o rendimento.
- Rendimento lançado pelo líquido, sem o IRRF retido.
- Cheque comum: baixa-se o banco na emissão e o cheque não compensado vira item da conciliação. Cheque pré-datado entregue ao fornecedor: a obrigação continua em fornecedores (ou em conta de cheques a compensar) até a data combinada; não baixar o banco antes.
- Sistema "auto-conciliando" sem revisão por amostragem.
- Diferença de centavos: investigar, não "arredondar".
- Arquivo de importação que sumiu da pasta normalmente já foi importado: confirmar antes de gerar outro.

### Casos de borda
- **Conta bloqueada por penhora:** movimentação atípica (bloqueio e transferência judicial) — lançar contra conta de depósito judicial/bloqueio e investigar.
- **Boleto pago em duplicidade:** valor pago a mais vai para conta a receber/recuperar do fornecedor até a devolução.
- **PIX agendado e estornado:** dois lançamentos opostos, ou nenhum se ambos no mesmo dia e o cliente preferir — registrar a decisão.

### Quando escalar
- Cartões e credenciadoras → `conciliacao-cartoes-credenciadora`
- Fornecedores divergentes → `conciliacao-fornecedores`
- Clientes e perdas esperadas → `conciliacao-clientes`
- Fechamento completo do mês → `fechamento-mensal`
- Gerar o arquivo para importar os lançamentos no seu sistema contábil → seguir o layout de importação do próprio sistema

### Autoavaliação
- [ ] Saldo inicial conferido?
- [ ] Cada item do extrato lançado ou explicado?
- [ ] Pendências mapeadas com data prevista?
- [ ] Diferença final zero?
- [ ] Espelho arquivado?

## Formato de entrega
- Cálculos, apurações e conciliações: entregar sempre planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar sempre documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Perguntas que o usuário costuma fazer
- **"O saldo bate, preciso conferir item a item?"** Sim. Saldo que bate pode esconder dois erros que se anulam.
- **"Posso deixar a diferença para o mês que vem?"** Não. Diferença sem explicação vira bola de neve (trava do D+2 do fechamento mensal).
- **"PIX sem nome, lanço como receita?"** Não. Vai para conta transitória do passivo até descobrir a origem.

## Base legal usada nesta skill
- ITG 2000 (R1) — Escrituração Contábil (aprovada inicialmente pela Resolução CFC nº 1.330/2011): escrituração completa, com documentação de suporte; retificação de lançamento por estorno, transferência ou complementação (itens 31 a 36).
- NBC TG Estrutura Conceitual — representação fidedigna da informação contábil.
- Art. 177 da Lei nº 6.404/1976 — escrituração pelo regime de competência.
- CPC 48 — instrumentos financeiros (aplicações financeiras e empréstimos pelo custo amortizado).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
