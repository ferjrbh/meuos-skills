---
name: lancamentos-contabeis-padrao
description: "Catálogo de lançamentos contábeis (débito e crédito) para as operações do dia a dia — vendas com tributos como redutores da receita bruta, compras com crédito de tributos, imobilizado e CIAP, folha com encargos e provisões (CPC 33), tributos sobre o lucro, empréstimos pelo custo amortizado (CPC 48), equivalência patrimonial (CPC 18), perdas esperadas com clientes (CPC 48) e arrendamento do lado do locatário (CPC 06 R2). Acionar quando o usuário disser \"como lanço\", \"modelo de lançamento\", \"débito e crédito de\", \"partida de\", \"contabilizar venda/compra/folha/empréstimo/leasing\", \"conferir lançamento\" ou estiver revisando livros. Entrega: lançamento com débito, crédito, valor e histórico explicativo, mais o alerta dos erros típicos."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Lançamentos contábeis padrão

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Entrega o lançamento correto (débito, crédito, valor e histórico) para a operação pedida, cruzado com o documento de origem (nota, contrato, folha). Usa os códigos de um plano-modelo (o da skill `plano-contas-cpc`) apenas como referência: no cliente, vale sempre o código do plano dele.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Dúvida sobre como contabilizar uma operação.
- Conferência de lançamentos feitos pelo sistema ou por outra pessoa.
- Montagem de regras de integração (fiscal e folha para contábil).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Histórico de folha cita a competência, não o nome nem o salário de cada empregado.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e escritura.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista
```
Q1: Qual operação? (venda, compra, folha, empréstimo, arrendamento etc.)
Q2: Tenho a nota ou o contrato? Posso ler?
Q3: Regime tributário (Simples, Presumido, Real)? Define se há crédito de tributos.
Q4: Plano de contas do cliente já mapeado? Provisões mensais configuradas no sistema?
```

### 2. Regras gerais
- Débito = crédito em todo lançamento (partidas dobradas).
- Regime de competência (art. 177 da Lei nº 6.404/1976).
- Histórico explicativo, nunca "diversos": número da nota ou do contrato, data, contraparte e competência.

### 3. Catálogo (códigos do plano-modelo, só como referência)

#### Venda de mercadoria com tributos e baixa do estoque
Exemplo (Lucro Presumido, PIS e COFINS cumulativos): venda de R$ 10.000; ICMS 17% (1.700); PIS 0,65% (65); COFINS 3% (300); custo do estoque R$ 6.000. Alíquotas apenas ilustrativas: usar as da UF e do regime do cliente.
```
(1) Receita bruta:
D 1.1.2.01 Clientes (ou 1.1.1.02 Banco, se à vista) ...... 10.000
   C 4.1.1.01 Venda de Mercadorias ....................... 10.000
(2) Tributos sobre a venda (redutores da receita bruta):
D 4.2.1.01 (−) ICMS sobre Vendas ......................... 1.700
   C 2.1.4.01 ICMS a Recolher ............................ 1.700
D 4.2.1.02 (−) PIS sobre Receitas ........................    65
   C 2.1.4.02 PIS a Recolher .............................    65
D 4.2.1.03 (−) COFINS sobre Receitas .....................   300
   C 2.1.4.03 COFINS a Recolher ..........................   300
(3) Baixa do estoque pelo custo:
D 5.1.1.01 CMV ........................................... 6.000
   C 1.1.3.01 Mercadorias para Revenda ................... 6.000

Recebimento: D Banco / C Clientes.
Juros por atraso recebidos: D Banco / C 4.4 Receitas financeiras.
```

#### Compra para revenda com crédito de tributos (não cumulativo)
Os tributos recuperáveis estão **dentro** do valor da nota: o fornecedor recebe o total da nota e o estoque fica pelo valor líquido dos créditos.
Exemplo (Lucro Real, PIS e COFINS não cumulativos): nota de R$ 5.000; ICMS 17% (850). Desde 01/05/2023, o ICMS destacado na nota de aquisição fica **fora** da base do crédito de PIS e COFINS (inciso III do § 2º do art. 3º da Lei nº 10.637/2002 e da Lei nº 10.833/2003, incluído pela Lei nº 14.592/2023). Base do crédito = 5.000 − 850 = 4.150; PIS 1,65% = 68,48; COFINS 7,6% = 315,40. Alíquota de ICMS apenas ilustrativa: usar a da operação.
```
D 1.1.3.01 Mercadorias para Revenda (líquido) ............ 3.766,12
D 1.1.4.01 ICMS a Recuperar ..............................   850,00
D 1.1.4.02 PIS a Recuperar ...............................    68,48
D 1.1.4.03 COFINS a Recuperar ............................   315,40
   C 2.1.1.01 Fornecedores Nacionais ..................... 5.000,00
```
No Simples Nacional ou no regime cumulativo não há crédito de PIS/COFINS: o valor vai ao estoque (e o ICMS só se houver crédito admitido).

#### Imobilizado com crédito de ICMS (CIAP)
Exemplo: máquina com nota de R$ 59.000, com ICMS de R$ 9.000 destacado e creditável.
```
Aquisição:
D 1.2.3.03 Máquinas e Equipamentos ....................... 50.000
D ICMS a Recuperar — CIAP (curto e longo prazo) ..........  9.000
   C 2.1.1.01 Fornecedores Nacionais ..................... 59.000
Mensalmente (1/48 do crédito, proporcional às saídas tributadas — art. 20, § 5º, da Lei Complementar nº 87/1996):
D 1.1.4.01 ICMS a Recuperar (apuração do mês) ............ parcela do mês
   C ICMS a Recuperar — CIAP ............................. parcela do mês
Parcela não aproveitada (saídas isentas ou não tributadas): baixar como custo ou despesa.
Depreciação mensal (vida útil de 10 anos, linear):
D 5.2.2.08 Depreciação (ou 5.1.3 se o bem é da produção) .  416,67
   C 1.2.3.99 (−) Depreciação Acumulada ..................  416,67
```
A vida útil contábil segue o CPC 27 (estimativa da empresa); a taxa fiscal da Receita é outra referência e pode diferir.

#### Folha de pagamento (competência)
```
(1) Salários e retenções:
D 5.2.1.01 Salários ...................................... 50.000
   C 2.1.3.01 Salários a Pagar ........................... 38.500
   C 2.1.3.04 INSS a Recolher (retido do empregado) ......  4.500
   C 2.1.3.06 IRRF sobre Salários a Recolher .............  3.000
   C 2.1.3.xx Descontos a repassar (VT, plano de saúde) ..  4.000
(2) Encargos patronais (exemplo):
D 5.2.1.02 Encargos Sociais .............................. 18.000
   C 2.1.3.04 INSS a Recolher (empresa, RAT e terceiros) . 14.000
   C 2.1.3.05 FGTS a Recolher ............................  4.000
(3) Provisões mensais (CPC 33):
D 5.2.1.03 Provisão de Férias + 1/3 + Encargos ...........  6.000
   C 2.1.3.02 Provisão de Férias + 1/3 ...................  6.000
D 5.2.1.04 Provisão de 13º + Encargos ....................  4.500
   C 2.1.3.03 Provisão de 13º Salário ....................  4.500
```
Os encargos das provisões podem ficar em subconta própria do passivo (INSS e FGTS sobre provisões). No Simples Nacional, a contribuição patronal da maioria dos anexos está dentro do DAS; no Anexo IV ela é recolhida à parte. Mão de obra da produção vai para custo (5.1.2), não para despesa.

#### Tributos sobre o lucro
```
D 5.6.1.01 IRPJ — Corrente ......... 12.000  |  C 2.1.4.04 IRPJ a Recolher ... 12.000
D 5.6.1.02 CSLL — Corrente .........  4.500  |  C 2.1.4.05 CSLL a Recolher ...  4.500
```
Lançar antes do encerramento do resultado (`fechamento-mensal`).

#### Empréstimo (custo amortizado — CPC 48)
```
Captação (líquido creditado):
D 1.1.1.02 Banco ......................................... 98.500
D Custos de transação a apropriar (redutora do passivo) ..  1.500
   C 2.1.2.01 Empréstimos Bancários ...................... 100.000
Juros do mês (taxa efetiva, incluindo a apropriação dos custos de transação):
D 5.4.1.01 Juros Passivos ................................ valor do mês
   C 2.1.2.01 Empréstimos (e/ou baixa da redutora) ....... valor do mês
Pagamento da parcela:
D 2.1.2.01 Empréstimos ................................... parcela
   C 1.1.1.02 Banco ...................................... parcela
```
Parcela que vence em mais de 12 meses fica no não circulante (2.2.1); reclassificar a cada fechamento.

#### Equivalência patrimonial (CPC 18 (R2))
```
Lucro da investida × percentual de participação:
D 1.2.2 Investimentos ............................. 30.000
   C Resultado de Equivalência Patrimonial ........ 30.000
Dividendos declarados pela investida:
D Dividendos a Receber ............................ 10.000
   C 1.2.2 Investimentos .......................... 10.000
Recebimento:
D 1.1.1.02 Banco .................................. 10.000
   C Dividendos a Receber ......................... 10.000
```
Sem balanço ou balancete da investida, não há como calcular: pedir o documento.

#### Perdas esperadas com clientes (CPC 48)
```
Constituição ou reforço (pela matriz do histórico do próprio cliente — `conciliacao-clientes`):
D 5.2.2.13 Perda Esperada em Créditos ...... 5.000
   C 1.1.2.05 (−) Perda Esperada — PCLD ..... 5.000
Cliente provisionado que pagou:
   D 1.1.1.02 Banco ........................ 5.000
      C 1.1.2.01 Clientes ................... 5.000      (o recebimento baixa o CLIENTE, não a provisão)
   D 1.1.2.05 (−) Perda Esperada — PCLD .... 5.000
      C Reversão de Perda Esperada (resultado) 5.000      (revisão da estimativa)
Baixa do incobrável:
   D 1.1.2.05 (−) Perda Esperada — PCLD
      C 1.1.2.01 Clientes
```
A perda esperada não é dedutível no Lucro Real quando registrada (art. 13 da Lei nº 9.249/1995); a dedução fiscal segue os arts. 9º a 14 da Lei nº 9.430/1996 (detalhes na skill `conciliacao-clientes`).

#### Arrendamento — locatário (CPC 06 (R2))
Exemplo coerente: valor presente de R$ 200.000, 60 parcelas mensais, taxa incremental de 1% ao mês → parcela de R$ 4.448,89.
```
Início:
D 1.2.3.09 Direito de Uso — Arrendamentos ........ 200.000,00
   C 2.1.2.03 Passivo de Arrendamento — CP ....... parcela dos próximos 12 meses
   C 2.2.1.03 Passivo de Arrendamento — LP ....... restante
Mês 1 (juros = saldo do passivo × taxa = 200.000 × 1%):
D 2.1.2.03 Passivo de Arrendamento (principal) ...   2.448,89
D 5.4.1.05 Juros sobre Arrendamento ..............   2.000,00
   C 1.1.1.02 Banco ..............................   4.448,89
Amortização do direito de uso (linear, 200.000 / 60):
D Despesa (ou custo) de Amortização do Direito de Uso  3.333,33
   C (−) Amortização Acumulada do Direito de Uso ....  3.333,33
```
Isenções opcionais de reconhecimento: arrendamento de curto prazo (prazo de 12 meses ou menos, sem opção de compra) e de ativo de baixo valor (CPC 06 (R2), itens 5 a 8). O valor de referência de cerca de US$ 5.000 vem da base de conclusões do IFRS 16, não do texto do CPC.

### 4. Entregável
**a)** Lançamento com débito, crédito, valor e histórico explicativo (nota, data, partes, competência).
**b)** Cruzamento com a nota ou o contrato.
**c)** Memória dos lançamentos do dia ou do mês, salva na pasta do cliente.

## Erros comuns / pontos de atenção
- "Diversos" no histórico: sempre detalhar (nota, contrato, ata).
- Receita lançada já líquida de tributos: o certo é receita bruta + redutores (art. 187 da Lei nº 6.404/1976).
- Esquecer a baixa do estoque (CMV) na venda.
- Compra com crédito: somar os tributos por fora do valor da nota (o fornecedor recebe o total da nota).
- Compra com crédito jogada 100% no estoque (perde o crédito).
- Recebimento de cliente provisionado creditado na PCLD em vez de em Clientes.
- Provisão de férias e 13º não lançada todo mês (CPC 33 — competência).
- Depreciação de bem produtivo lançada como despesa (é custo).
- Empréstimo lançado como receita ou despesa (é passivo + juros pela competência).
- Bem de valor unitário até R$ 1.200,00: pode ser deduzido como despesa para fins fiscais (art. 313 do Decreto nº 9.580/2018 (RIR/2018)); na contabilidade, vale a política de materialidade da empresa.
- Equivalência sem documentação da investida.
- Débito ≠ crédito.

### Quando escalar
- Plano de contas → `plano-contas-cpc`
- Conciliações → `conciliar-extrato-razao`, `conciliacao-fornecedores`, `conciliacao-clientes`
- Imobilizado e depreciação → `ativo-imobilizado-depreciacao`
- Fechamento → `fechamento-mensal`

### Autoavaliação
- [ ] Histórico explicativo com nota ou contrato?
- [ ] Provisões mensais (CPC 33)?
- [ ] Tributo sobre venda como redutor da receita bruta?
- [ ] Débito = crédito?
- [ ] Regime tributário conferido antes de lançar créditos?
- [ ] Cruzamento com o documento?

## Formato de entrega
- Cálculos, apurações e conciliações: entregar sempre planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar sempre documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Perguntas que o usuário costuma fazer
- **"O ICMS da compra entra no estoque?"** Se é recuperável, não: vai para ICMS a recuperar e o estoque fica pelo líquido. Se não há crédito, entra no custo.
- **"Cliente pagou um título que estava na PCLD. Como lanço?"** Recebimento contra Clientes; depois reverta a provisão contra o resultado.
- **"Aluguel virou arrendamento?"** Pelo CPC 06 (R2), o locatário reconhece direito de uso e passivo, salvo as isenções de curto prazo e baixo valor.

## Base legal usada nesta skill
- Arts. 177 (competência), 183 (critérios de avaliação) e 187 (DRE) da Lei nº 6.404/1976; Lei nº 11.638/2007.
- CPC 00 (R2) — Estrutura Conceitual; CPC 26 (R1) — apresentação; CPC 27 — imobilizado; CPC 33 (R1) — benefícios a empregados; CPC 48 — instrumentos financeiros (custo amortizado e perdas esperadas); CPC 18 (R2) — equivalência patrimonial; CPC 06 (R2) — arrendamentos (itens 5 a 8, isenções).
- Art. 20, § 5º, da Lei Complementar nº 87/1996 — crédito de ICMS do ativo imobilizado em 48 parcelas (CIAP).
- Art. 313 do Decreto nº 9.580/2018 (RIR/2018) — dedução de bens de pequeno valor (até R$ 1.200,00).
- Art. 13 da Lei nº 9.249/1995 e arts. 9º a 14 da Lei nº 9.430/1996 — dedutibilidade das perdas com créditos.
- Art. 3º, § 2º, III, da Lei nº 10.637/2002 e da Lei nº 10.833/2003 (incluído pela Lei nº 14.592/2023) — ICMS fora da base do crédito de PIS e COFINS.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
