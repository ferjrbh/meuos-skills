---
name: plano-contas-cpc
description: "Estrutura o plano de contas do cliente com todas as contas analíticas mapeadas para o plano referencial da ECD, aderente aos CPCs (26 apresentação, 27 imobilizado, 04 intangível, 47 receita, 48 instrumentos financeiros, 06 R2 arrendamento, 25 provisões, 33 benefícios a empregados), com DRE estruturada e lista de provisões mensais a configurar no sistema. Acionar quando o usuário disser \"plano de contas\", \"montar plano de contas\", \"implantar cliente\", \"abrir empresa\", \"migrar de sistema\", \"mapeamento referencial\", \"conta sem referencial\", \"erro no PVA da ECD por referencial\" ou \"configurar provisões no sistema\". Entrega: plano em planilha (código, tipo, nome, natureza, referencial), matriz referencial e lista de provisões mensais."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Plano de contas aderente aos CPCs

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Monta ou revisa o plano de contas do cliente: grupos na ordem da Lei nº 6.404/1976, contas sintéticas e analíticas bem separadas, contas redutoras onde a norma pede, natureza de cada conta conforme a ECD e código referencial em todas as analíticas. Parte do plano-modelo do passo 2 e adapta ao porte, à atividade, ao regime e ao tipo societário do cliente.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Implantação de cliente novo ou abertura de empresa.
- Migração de sistema contábil.
- Erro de "conta sem referencial" ou de natureza no PVA da ECD ou da ECF.
- Revisão de plano inflado ou com conta "Outros" virando depósito.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Não criar conta com nome de pessoa física (sócio, empregado) quando um código ou apelido resolve.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e importa no sistema.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: CNPJ, atividade, porte (faturamento estimado), regime tributário e tipo societário (Ltda., S.A., SLU, associação)?
Q2: Qual é o sistema contábil do escritório? Dá para importar um plano padrão?
Q3: Provisões mensais (férias, 13º, perdas esperadas) já configuradas?
Q4: Imobilizado relevante? Usa CIAP?
Q5: Tem arrendamento (aluguel de longo prazo, leasing) a reconhecer pelo CPC 06 (R2)?
Q6: Norma adotada: completa (CPCs), NBC TG 1000 (PME), NBC TG 1001 (pequena empresa) ou NBC TG 1002 (microentidade)?
```

### 2. Estrutura do plano-modelo
```
1 ATIVO
1.1 CIRCULANTE
1.1.1 Disponibilidades (caixa, bancos, aplicações de liquidez imediata)
1.1.2 Clientes (com 1.1.2.05 (−) Perda Esperada — PCLD, redutora — CPC 48)
1.1.3 Estoques (com 1.1.3.06 (−) Ajuste a valor realizável líquido — CPC 16)
1.1.4 Tributos a recuperar (ICMS, PIS, COFINS, IPI, IRPJ/CSLL antecipados)
1.1.5 Outros (adiantamentos, despesas antecipadas)
1.2 NÃO CIRCULANTE
1.2.1 Realizável a longo prazo
1.2.2 Investimentos (CPC 18 — equivalência)
1.2.3 Imobilizado (CPC 27 — com 1.2.3.99 (−) depreciação acumulada; direito de uso 1.2.3.09 — CPC 06 R2)
1.2.4 Intangível (CPC 04 — com 1.2.4.99 (−) amortização acumulada)

2 PASSIVO
2.1 CIRCULANTE (fornecedores, empréstimos e arrendamento CP, trabalhistas, tributárias, outras)
2.2 NÃO CIRCULANTE (empréstimos e arrendamento LP, parcelamentos, provisões CPC 25)

3 PATRIMÔNIO LÍQUIDO (capital, reservas de capital, ajustes de avaliação patrimonial, reservas de lucros, lucros/prejuízos acumulados, redutoras)
4 RECEITAS (4.1 bruta · 4.2 deduções · 4.3 outras operacionais · 4.4 financeiras)
5 CUSTOS E DESPESAS (5.1 custos · 5.2 administrativas · 5.3 comerciais · 5.4 financeiras · 5.5 outras · 5.6 IRPJ/CSLL)
6 APURAÇÃO DO RESULTADO (transitório; zera no encerramento)
```
Se o sistema do cliente usa outra numeração (por exemplo, o plano padrão do sistema contábil do cliente), manter a numeração dele e aplicar a mesma lógica. Registrar no cadastro de cada cliente qual dígito inicial é receita, custo e despesa: as rotinas de zeramento e de importação de extrato do sistema contábil dependem disso.

### 3. Colunas obrigatórias da planilha do plano
```
codigo_empresa | tipo (S/A) | nome | natureza_ECD | codigo_referencial | observacao
1.1.1.02.01    | A | Banco Exemplo c/c 0000-0          | 01 | 1.01.01.01.02 | 
1.1.2.01       | A | Clientes — Mercado Nacional       | 01 | 1.01.02.01.01 |
1.1.2.05       | A | (−) Perda Esperada — PCLD         | 01 | 1.01.02.01.05 | redutora, saldo credor
1.1.3.01       | A | Mercadorias para Revenda          | 01 | 1.01.03.01.01 |
2.1.1.01       | A | Fornecedores Nacionais            | 02 | (conferir na tabela) |
3.5.1.01       | A | Lucros Acumulados                 | 03 | (conferir na tabela) |
4.1.1.01       | A | Venda de Mercadorias              | 04 | (conferir na tabela) |
4.2.1.01       | A | (−) ICMS sobre Vendas             | 04 | (conferir na tabela) |
5.1.1.01       | A | CMV                               | 04 | (conferir na tabela) |
```
- **Tipo:** S = sintética (só totaliza, não recebe lançamento); A = analítica (recebe lançamento).
- **Natureza (código da ECD, registro I050):** 01 contas de ativo · 02 contas de passivo · 03 patrimônio líquido · 04 contas de resultado (receitas, custos e despesas) · 05 contas de compensação · 09 outras. Conta redutora fica com a natureza do grupo em que está (a PCLD é 01, apesar do saldo credor).
- **Referencial:** os códigos acima servem só de exemplo. Antes de entregar, conferir cada código na tabela do plano de contas referencial da Receita Federal vigente para o tipo de entidade e o regime do cliente (a tabela é publicada no Portal SPED e carregada no PVA; o plano escolhido é indicado no campo COD_PLAN_REF do registro 0000 da ECD). A conta analítica de resultado (04) só pode apontar para referencial também de resultado: o PVA acusa erro quando a natureza da conta referencial difere da natureza da conta mapeada.
- **Onde o mapeamento é exigido:** na ECD, o registro I051 (plano referencial) passa a ser obrigatório quando o campo COD_PLAN_REF do registro 0000 é preenchido; a ECF usa o mapeamento referencial (registro J051, recuperado da ECD ou informado nela). Mapear 100% das analíticas evita retrabalho nas duas.

### 4. Provisões mensais a configurar no sistema
```
- Férias + 1/3 + encargos: (salário + médias) / 12 × 4/3 × (1 + % encargos), por empregado e mês
- 13º + encargos: (salário + médias) / 12 × (1 + % encargos), por empregado e mês
- % encargos (regime geral): INSS empresa 20% + RAT 1% a 3% (ajustado pelo FAP) + terceiros (conforme o FPAS) + FGTS 8%
  No Simples Nacional, só FGTS para a maioria dos anexos; Anexo IV recolhe o INSS patronal à parte.
- Perda esperada (CPC 48): matriz montada com o histórico de perdas do próprio cliente (`conciliacao-clientes`); sem percentual "de mercado"
- Ajuste de estoques ao valor realizável líquido (CPC 16)
- Provisões para contingências (CPC 25): provável = provisiona; possível = só nota explicativa; remota = nada
```

### 5. Arrendamento (CPC 06 (R2)) — locatário
Ativo 1.2.3.09 Direito de uso e passivo de arrendamento (2.1.2.03 CP e 2.2.1.03 LP). Todo mês: amortização do direito de uso e juros do passivo.
Isenções opcionais: prazo de 12 meses ou menos (sem opção de compra) e ativo de baixo valor (CPC 06 (R2), itens 5 a 8). O valor de cerca de US$ 5.000 é referência da base de conclusões do IFRS 16, não texto do CPC.

### 6. DRE estruturada (CPC 26 (R1) e art. 187 da Lei nº 6.404/1976)
```
Receita bruta                                  (4.1)
(−) Deduções (tributos sobre venda, devoluções, descontos incondicionais)   (4.2)
= Receita líquida
(−) CMV / CPV / CSP                             (5.1)
= Lucro bruto
(−) Despesas operacionais (administrativas, comerciais, outras)   (5.2, 5.3, 5.5)
(+) Outras receitas operacionais                (4.3)
= Resultado antes do resultado financeiro
(+) Receitas financeiras (4.4)  (−) Despesas financeiras (5.4)
= LAIR
(−) IRPJ e CSLL correntes e diferidos            (5.6)
= Lucro líquido
```
O IPI destacado não compõe a receita bruta (art. 12, § 4º, do Decreto-Lei nº 1.598/1977); se o sistema registra o faturamento com IPI, a conta de IPI fica como dedução apenas para chegar à receita bruta correta.

### 7. Entregável
**a)** Plano de contas em planilha com as colunas do passo 3.
**b)** Matriz referencial completa (todas as analíticas de natureza 01 a 04).
**c)** Lista de provisões mensais com fórmulas (passo 4).
**d)** DRE estruturada (passo 6).
**e) Checklist:**
```
[ ] Uma conta para cada natureza relevante, sem conta criada para um lançamento só
[ ] Sintéticas e analíticas distinguidas; sintética bloqueada para lançamento
[ ] Natureza ECD (01/02/03/04/05/09) em todas as contas
[ ] 100% das analíticas de natureza 01 a 04 com referencial conferido na tabela vigente
[ ] Redutoras: depreciação (1.2.3.99), amortização (1.2.4.99), PCLD (1.1.2.05), ajuste de estoque (1.1.3.06)
[ ] Tributos a recuperar separados dos a recolher
[ ] Receitas financeiras fora da receita operacional
[ ] Provisões mensais configuradas (férias, 13º, perdas esperadas, contingências)
[ ] Tipo societário verificado (S.A. × Ltda.) para Lucros Acumulados
[ ] Arrendamentos avaliados (CPC 06 R2)
[ ] Plano documentado e importado no sistema
```

## Erros comuns / pontos de atenção
- Conta "Outros" virando depósito.
- Imobilizado sem conta redutora de depreciação.
- Tributos a recolher misturados com a recuperar.
- Falta de provisão mensal de férias e 13º.
- Receita financeira dentro da receita operacional (distorce lucro bruto e EBITDA).
- Conta analítica sem referencial ou com natureza errada: a ECD não valida.
- Usar 4, 5, 6 e 7 como "natureza" da ECD para receita, custo, despesa e outros: na ECD, todo resultado é 04; 05 é compensação e 09 é outras.
- Conta sintética recebendo lançamento.
- S.A. mantendo saldo credor em Lucros Acumulados sem destinação (art. 202, § 6º, da Lei nº 6.404/1976). Em Ltda., o saldo pode ficar até a deliberação dos sócios sobre o balanço (art. 1.078, I, da Lei nº 10.406/2002 (Código Civil)).

### Casos de borda
- **PME (NBC TG 1000), pequena empresa (NBC TG 1001) e microentidade (NBC TG 1002):** simplificações permitidas por cada norma, mas a estrutura do plano é a mesma. A ITG 1000 traz modelos de plano de contas para microentidade e pequena empresa.
- **Holding patrimonial:** foco em investimentos, equivalência (CPC 18) e propriedade para investimento (CPC 28).
- **Cooperativa:** sobras e perdas no lugar de lucro e prejuízo; contas próprias de atos cooperativos.
- **Associação ou fundação (terceiro setor):** superávit/déficit, patrimônio social e subvenções (ITG 2002 (R1) e CPC 07).
- **Zona Franca de Manaus e áreas de livre comércio:** benefícios próprios em tributos a recuperar.

### Quando escalar
- Lançamentos por operação → `lancamentos-contabeis-padrao`
- Imobilizado e depreciação → `ativo-imobilizado-depreciacao`
- ECD e ECF → `ecd-escrituracao-contabil-digital` e `ecf-escrituracao-contabil-fiscal`
- Fechamento → `fechamento-mensal`

### Autoavaliação
- [ ] Planilha com código, tipo, nome, natureza ECD e referencial?
- [ ] 100% das analíticas mapeadas e conferidas na tabela vigente?
- [ ] Provisões configuradas?
- [ ] DRE estruturada pelo CPC 26?
- [ ] Redutoras criadas?
- [ ] Arrendamento avaliado?
- [ ] Documentado para o sistema?

## Formato de entrega
- Cálculos, apurações e conciliações: entregar sempre planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar sempre documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Perguntas que o usuário costuma fazer
- **"Onde acho o plano referencial?"** Na tabela do plano de contas referencial publicada pela Receita Federal no Portal SPED (sped.rfb.gov.br) e carregada no PVA, escolhida pelo tipo de entidade e pelo regime do cliente (campo COD_PLAN_REF do registro 0000 da ECD). Usar sempre a versão da tabela do ano-calendário da escrituração.
- **"PCLD é natureza 01 ou 02?"** 01: é redutora do ativo, mesmo com saldo credor.
- **"Ltda. pode deixar lucro acumulado?"** Pode, até os sócios deliberarem. S.A. não.

## Base legal usada nesta skill
- Arts. 176, 177, 178 (grupos e ordem), 179, 182, 183, 187 e 202, § 6º, da Lei nº 6.404/1976; Lei nº 11.638/2007.
- Art. 1.065 (balanço patrimonial e de resultado ao fim do exercício) e art. 1.078, I (deliberação dos sócios sobre o balanço), da Lei nº 10.406/2002 (Código Civil) — sociedade limitada.
- IN RFB nº 2.003/2021 — Escrituração Contábil Digital (ECD); Manual de Orientação do Leiaute da ECD, registros 0000 (campo COD_PLAN_REF), I050 (natureza da conta) e I051 (plano referencial). ECF: registro J051 (plano referencial).
- CPC 00 (R2), CPC 26 (R1), CPC 16, CPC 27, CPC 04 (R1), CPC 18 (R2), CPC 25, CPC 28, CPC 33 (R1), CPC 47, CPC 48, CPC 06 (R2), CPC 07.
- NBC TG 1000 (R1) (PME); NBC TG 1001 (pequena empresa); NBC TG 1002 (microentidade); ITG 1000 (modelos para microentidade e pequena empresa); ITG 2002 (R1) (terceiro setor).
- Art. 12, § 4º, do Decreto-Lei nº 1.598/1977 — IPI fora da receita bruta.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
