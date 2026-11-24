---
name: ecf-escrituracao-contabil-fiscal
description: "Prepara e confere a ECF anual (IN RFB nº 2.004/2021): recuperação da ECD, mapeamento referencial, e-Lalur/e-Lacs (Parte A com adições, exclusões e compensações; Parte B com prejuízo fiscal e base negativa), cálculo de IRPJ/CSLL no Bloco N (Lucro Real), P (Presumido), T (Arbitrado), U (imunes/isentas), e blocos W, X e Y. Prazo: último dia útil de JULHO do ano seguinte. Considera a LC nº 224/2025 (presunção +10% acima de R$ 5 milhões em 2026). Acionar quando o usuário disser \"fazer a ECF\", \"LALUR\", \"e-Lalur\", \"Parte B\", \"prejuízo fiscal\", \"trava de 30%\", \"recuperar ECD na ECF\", \"erro no PVA da ECF\", \"M300\", \"JCP na ECF\". Entrega checklist, LALUR Parte A, Parte B atualizada e cruzamento ECF × ECD × DCTFWeb × EFD-Contribuições. Não apura o IRPJ/CSLL do período corrente (usar a skill de apuração)."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# ECF — Escrituração Contábil Fiscal

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Organiza a ECF depois da ECD: recupera a contabilidade, confere o mapeamento referencial, monta o e-Lalur e o e-Lacs (adições, exclusões e compensações, com controle da Parte B) e confere o cálculo de IRPJ e CSLL no bloco do regime da empresa. Termina com o cruzamento com ECD, DCTFWeb e EFD-Contribuições.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Prazo:** último dia útil de **julho** do ano seguinte (art. 3º da IN RFB nº 2.004/2021). Exemplo:
> ECF 2025 até 31/07/2026. Em extinção, cisão, fusão ou incorporação: evento de janeiro a abril, até o
> último dia útil de julho do mesmo ano; de maio a dezembro, até o último dia útil do terceiro mês
> seguinte ao evento (art. 3º, § 2º). A incorporadora sob o mesmo controle societário da incorporada
> desde o ano anterior não entrega ECF de situação especial (art. 3º, § 3º).
> **2026 (ECF a entregar em 2027):** a LC nº 224/2025 aumentou em 10% os percentuais de presunção do
> Lucro Presumido sobre a parcela da receita bruta anual acima de R$ 5.000.000 (IRPJ desde 01/01/2026;
> CSLL desde 01/04/2026, com limite de R$ 3.750.000 só em 2026). O Manual da ECF de 2026 já prevê o
> rateio por período. Há liminares em TRFs para alguns contribuintes: conferir se o cliente tem decisão
> judicial antes de aplicar a majoração.

## Quando usar
- Preparação anual da ECF (Lucro Real, Presumido, Arbitrado, imunes e isentas).
- Erro de validação no PVA da ECF.
- Controle da Parte B (prejuízo fiscal e base negativa).
- Retificação de ECF anterior.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). A ECF traz sócios e rendimentos pagos a eles: não reproduzir esses dados.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Quem entrega (art. 1º da IN RFB nº 2.004/2021)
Todas as PJ, inclusive equiparadas, de forma centralizada pela matriz. Dispensadas (art. 1º, § 1º): optantes do Simples Nacional; órgãos públicos, autarquias e fundações públicas; PJ inativas (sem nenhuma atividade no ano-calendário). Imunes e isentas entregam (Bloco U). No Lucro Real, a ECF substitui o Lalur (art. 1º, § 2º). A sócia ostensiva entrega uma ECF separada para cada SCP, além da sua (art. 1º, § 3º).

### 2. Estrutura da ECF
```
0  Abertura e identificação (regime, forma de tributação)
C  Informações recuperadas da ECD
E  Informações recuperadas da ECF anterior e cálculo fiscal dos dados da ECD
J  Plano de contas e mapeamento referencial
K  Saldos das contas contábeis e referenciais
L  Lucro líquido — Lucro Real (balanço e DRE)
M  e-Lalur e e-Lacs: M300 (Parte A IRPJ: adições, exclusões, compensação),
   M350 (Parte A CSLL), M410 (lançamentos na Parte B), M500 (controle de saldos Parte B)
N  Cálculo do IRPJ e da CSLL — Lucro Real (estimativas, trimestral, anual)
P  Lucro Presumido (balanço, DRE e cálculo de IRPJ/CSLL)
Q  Demonstrativo do Livro Caixa (Presumido que mantém Livro Caixa)
S  Sociedade Anônima do Futebol (Tributação Específica do Futebol — TEF)
T  Lucro Arbitrado
U  Imunes e isentas
V  DEREX (recursos em moeda estrangeira no exterior)
W  Declaração País-a-País
X  Informações econômicas (inclui operações com o exterior)
Y  Informações gerais (sócios, rendimentos, participações etc.)
9  Encerramento
```
Blocos conforme o Manual de Orientação do Leiaute 12 da ECF (anexo ao ADE Cofis nº 2/2026), válido para o ano-calendário 2025 e situações especiais de 2026. Para a ECF do ano-calendário 2026, usar o manual que a RFB publicar para esse ano.

### 3. Pré-requisito: ECD transmitida
Para quem é obrigado à ECD, a ECF recupera os dados dela. Sem ECD válida (recibo e situação ativa no SPED), a recuperação falha. Usar `ecd-escrituracao-contabil-digital` antes.

### 4. Entrevista mínima
```
Q1: "Ano-calendário + CNPJ + regime (Real trimestral, Real anual, Presumido, Arbitrado, imune/isenta)?"
Q2: "ECD transmitida e ativa (data e recibo)?"
Q3: "Saldos da Parte B (prejuízo fiscal e base negativa) do ano anterior?"
Q4: "Adições e exclusões levantadas? (multas, provisões, JCP, equivalência, dividendos, subvenções)"
Q5: "DARFs de IRPJ/CSLL do ano (estimativas, trimestres, ajuste)?"
Q6 (Presumido 2026): "Receita bruta anual acima de R$ 5 milhões? (LC nº 224/2025)"
```

### 5. Recuperação da ECD
No PVA da ECF, recuperar a ECD do ano e conferir plano de contas, mapeamento, saldos, Balanço e DRE.

### 6. e-Lalur Parte A — adições e exclusões (exemplos com base legal)
```
ADIÇÕES
- Multas por infrações fiscais, salvo as compensatórias e as de infração sem falta de
  pagamento de tributo (art. 41, § 5º, da Lei nº 8.981/1995)
- Provisões não dedutíveis — só são dedutíveis as de férias e 13º e as técnicas
  autorizadas (art. 13, I, da Lei nº 9.249/1995). A PCLD contábil é adicionada; a perda
  só é dedutível nos critérios dos arts. 9º a 14 da Lei nº 9.430/1996
- Tributos com exigibilidade suspensa (art. 41, § 1º, da Lei nº 8.981/1995)
- Brindes (art. 13, VII, da Lei nº 9.249/1995)
- Doações fora das hipóteses e limites legais (art. 13, VI, e § 2º, da Lei nº 9.249/1995)
- Resultado negativo de equivalência patrimonial (art. 23 do Decreto-Lei nº 1.598/1977)
- JCP acima do limite (art. 9º da Lei nº 9.249/1995)
- Ajustes de preço de transferência (Lei nº 14.596/2023)

EXCLUSÕES
- Reversão de provisões antes adicionadas
- Resultado positivo de equivalência patrimonial (art. 23 do Decreto-Lei nº 1.598/1977)
- Dividendos recebidos de PJ brasileira (art. 10 da Lei nº 9.249/1995)
- Variação cambial pelo regime de caixa, quando houver opção
- Subvenção para investimento: até 2023, regime antigo de exclusão; desde 2024, crédito
  fiscal de subvenção da Lei nº 14.789/2023 (não é exclusão)
```
Cada adição ou exclusão precisa de fundamento (lei + artigo) e de documento de suporte.

### 7. Compensação de prejuízo fiscal e base negativa — trava de 30%
```
Compensação máxima no período = 30% do lucro líquido ajustado (depois de adições e exclusões)
IRPJ: art. 15 da Lei nº 9.065/1995 · CSLL (base negativa): art. 16 da Lei nº 9.065/1995
```
Cada compensação baixa o saldo da Parte B (M410/M500). A Parte B nunca fica negativa.

### 8. Cálculo de IRPJ e CSLL
- Lucro Real anual: Bloco N com estimativas mensais e ajuste anual.
- Lucro Real trimestral: quatro trimestres no Bloco N.
- Lucro Presumido: Bloco P, com a majoração da LC nº 224/2025 para 2026 quando aplicável.
- Lucro Arbitrado: Bloco T.

### 9. Erros comuns no PVA
- Conta sem mapeamento referencial.
- DRE recuperada diferente do balancete.
- Compensação acima de 30%.
- Receita da ECF diferente da EFD-Contribuições (alerta de malha PJ).
- JCP acima do limite sem adição.

### 10. Entregável obrigatório

**a) Checklist de pré-validação**
```
[ ] ECD do ano transmitida e ativa (se obrigada)
[ ] Recuperação da ECD sem erros
[ ] Mapeamento referencial 100%
[ ] Adições e exclusões com fundamento (lei + artigo)
[ ] Compensação dentro da trava de 30%
[ ] Parte B atualizada por ano de origem
[ ] DARFs do ano conferidos
[ ] Presumido 2026: majoração da LC nº 224/2025 aplicada (se receita > R$ 5 mi)
[ ] PVA sem erros
[ ] Cruzamento ECF × ECD × DCTFWeb × EFD-Contribuições sem divergência
[ ] Transmissão até o último dia útil de julho
```

**b) LALUR Parte A**
```
LALUR PARTE A — Ano __ — CNPJ __ (EMPRESA EXEMPLO)
Lucro antes do IRPJ/CSLL ......... R$ ___
(+) Adições ...................... R$ ___
(−) Exclusões .................... R$ ___
Lucro ajustado ................... R$ ___
(−) Compensação (até 30%) ........ R$ ___
LUCRO REAL ....................... R$ ___
IRPJ 15% + adicional 10% + CSLL .. R$ ___
```

**c) Parte B atualizada** (prejuízo fiscal e base negativa por ano de origem).

**d) Recibo** arquivado.

**e) Plano de ajuste**, se houver divergência no cruzamento: retificar na ordem ECD → ECF → DCTFWeb.

## Erros comuns / pontos de atenção
- Iniciar a ECF sem recuperar a ECD.
- Compensar prejuízo acima de 30%.
- Parte B com saldo negativo.
- Receita da ECF diferente da EFD-Contribuições.
- JCP acima do limite.
- Tratar subvenção de investimento de 2024 em diante como exclusão (Lei nº 14.789/2023 mudou o regime).
- **Multas** (art. 6º da IN RFB nº 2.004/2021):
  - **Lucro Real** — art. 8º-A do Decreto-Lei nº 1.598/1977 (incluído pela Lei nº 12.973/2014): atraso ou falta, 0,25% por mês-calendário ou fração sobre o lucro líquido antes do IRPJ e da CSLL, limitada a 10%, e com teto de R$ 100.000,00 (receita bruta do ano anterior até R$ 3.600.000,00) ou R$ 5.000.000,00 (demais); inexatidão ou omissão, 3% do valor omitido, inexato ou incorreto, não inferior a R$ 100,00. Reduções da multa por atraso: 90% (até 30 dias após o prazo), 75% (até 60 dias), 50% (antes de procedimento de ofício), 25% (no prazo da intimação). A multa por inexatidão não é devida se corrigida antes de procedimento de ofício e cai à metade se corrigida no prazo da intimação. Sem lucro no período, usa-se o último lucro informado, corrigido pela Selic.
  - **Demais PJ** — art. 12 da Lei nº 8.218/1991: 0,5% da receita bruta (forma exigida), 5% do valor da operação limitado a 1% da receita bruta (omissão/incorreção) e 0,02% por dia de atraso limitado a 1% da receita bruta, com as reduções do parágrafo único desse artigo.
  Não há "mínimo de R$ 5.000".

### Casos de borda
- **Partes relacionadas no exterior**: preço de transferência pela Lei nº 14.596/2023; Declaração País-a-País no Bloco W quando o grupo estiver obrigado. Grupo multinacional sujeito à tributação mínima global: adicional da CSLL da Lei nº 15.079/2024, com regras próprias de declaração definidas pela RFB.
- **Dividendos em 2026**: a Lei nº 15.270/2025 criou retenção sobre dividendos acima de R$ 50 mil por mês à mesma PF; os rendimentos pagos aos sócios são informados no Bloco Y, nos registros indicados no Manual da ECF do ano.
- **SCP**: ECF própria, separada da do sócio ostensivo.
- **Imune/isenta**: Bloco U.
- **Evento societário**: ECF de situação especial no prazo do § 2º do art. 3º da IN RFB nº 2.004/2021.

### Quando encaminhar para outra skill
- ECD pendente → `ecd-escrituracao-contabil-digital`
- Cruzamento → `revisao-fiscal-cruzamento-sped`
- Apuração do Lucro Real → `apuracao-lucro-real`
- Apuração do Presumido → `apuracao-lucro-presumido`
- Recuperação de PIS/COFINS (Tema 69) → `recuperacao-creditos-pis-cofins`

### Autoavaliação
- [ ] ECD recuperada sem erros?
- [ ] Referencial 100%?
- [ ] Adições e exclusões fundamentadas?
- [ ] Trava de 30% respeitada?
- [ ] Parte B atualizada?
- [ ] LC nº 224/2025 considerada (Presumido 2026)?
- [ ] PVA sem erros e cruzamento feito?
- [ ] Recibo arquivado?

## Perguntas que o usuário costuma fazer
- **"Presumido entrega ECF?"** Sim. Só o Simples Nacional, órgãos públicos e inativas são dispensados.
- **"Posso compensar todo o prejuízo de uma vez?"** Não. Até 30% do lucro ajustado em cada período.
- **"A ECF vence junto com a ECD?"** Não. ECD em junho, ECF no último dia útil de julho.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): documento DOCX.
- Este padrão prevalece sobre outros formatos citados acima, exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- IN RFB nº 2.004/2021 — ECF: art. 1º (obrigados, dispensados, SCP), art. 3º (prazo e situação especial), art. 6º (penalidades).
- Decreto-Lei nº 1.598/1977, art. 8º-A (multa da ECF no Lucro Real, incluído pela Lei nº 12.973/2014) e art. 23 (equivalência patrimonial).
- Lei nº 8.218/1991, art. 12 — multas para as demais PJ.
- IN RFB nº 1.700/2017 — IRPJ e CSLL (Lucro Real, Presumido, Arbitrado).
- Lei nº 12.973/2014 — adequação à contabilidade societária.
- Lei nº 9.065/1995, arts. 15 e 16 — trava de 30%.
- Lei nº 9.249/1995, arts. 9º, 10 e 13 — JCP, dividendos, indedutíveis.
- Lei nº 8.981/1995, art. 41, §§ 1º e 5º — tributos suspensos e multas.
- Lei nº 9.430/1996, arts. 9º a 14 — perdas no recebimento de créditos.
- Lei nº 14.789/2023 — crédito fiscal de subvenção para investimento.
- Lei nº 14.596/2023 — preço de transferência.
- Lei nº 15.079/2024 — adicional da CSLL (tributação mínima global).
- LC nº 224/2025 — majoração da presunção acima de R$ 5 milhões.
- Lei nº 15.270/2025 — dividendos e IRPFM.
- Manual de Orientação do Leiaute 12 da ECF (anexo ao ADE Cofis nº 2/2026).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
