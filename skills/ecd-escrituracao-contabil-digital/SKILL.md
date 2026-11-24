---
name: ecd-escrituracao-contabil-digital
description: "Prepara, diagnostica e valida a ECD anual (SPED Contábil — Livro Diário, Razão, balancetes e demonstrações) pela IN RFB nº 2.003/2021. Prazo: último dia útil de JUNHO do ano seguinte (redação da IN RFB nº 2.142/2023). Confere obrigatoriedade (Lucro Real; Lucro Presumido sem Livro Caixa ou que distribui lucro isento acima da base; imunes e isentas acima de R$ 4,8 milhões; SCP em livro próprio), plano de contas com referencial (I051), amarração de saldos, Bloco J e assinaturas. Acionar quando o usuário disser \"fazer a ECD\", \"SPED contábil\", \"erro no PVA da ECD\", \"conta sem referencial\", \"saldo inicial não bate\", \"J100\", \"J150\", \"I200\", \"I250\", \"prazo da ECD\". Entrega checklist de pré-validação, diagnóstico do TXT, lançamentos modelo e plano de correção."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# ECD — Escrituração Contábil Digital

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Ajuda a gerar, conferir e corrigir a ECD antes da transmissão ao SPED: obrigatoriedade, estrutura dos blocos, plano de contas com mapeamento ao Plano de Contas Referencial (PCR) da Receita, amarração dos saldos com o ano anterior, demonstrações do Bloco J e assinaturas. Se o cliente mandar o arquivo TXT, a skill lê e aponta os problemas.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Prazo correto:** a ECD vence no **último dia útil de junho** do ano seguinte ao da escrituração
> (art. 5º da IN RFB nº 2.003/2021, com redação da IN RFB nº 2.142/2023), até 23h59min59s de
> Brasília. Exemplo: ECD 2025 até 30/06/2026; ECD 2026 até 30/06/2027. O prazo de maio não vale mais.
> Em extinção, cisão, fusão ou incorporação (art. 5º, § 3º): evento de janeiro a maio, até o último
> dia útil de junho do mesmo ano; de junho a dezembro, até o último dia útil do mês seguinte ao evento.
> Não se aplica à incorporadora que já estava sob o mesmo controle societário da incorporada desde
> o ano-calendário anterior (art. 5º, § 4º).

## Quando usar
- Preparação anual da ECD.
- Erro de validação no PVA da ECD.
- Dúvida sobre quem é obrigado.
- Retificação (substituição) de ECD anterior.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). O TXT da ECD traz nomes e CPFs de sócios e signatários: ler para diagnosticar, sem reproduzir esses dados.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem. Os comandos abaixo só leem o arquivo; não alteram nada.

## Passo a passo (instruções para o agente de IA)

### 1. Quem é obrigado (art. 3º da IN RFB nº 2.003/2021)
```
REGRA: PJ, inclusive equiparadas, imunes e isentas, obrigadas a manter escrituração
contábil pela legislação comercial.

NÃO SE APLICA (§ 1º):
- optantes do Simples Nacional (salvo ME/EPP que recebeu aporte de investidor-anjo,
  arts. 61-A a 61-D da LC nº 123/2006 — § 2º)
- órgãos públicos, autarquias e fundações públicas
- PJ inativas (sem nenhuma atividade no ano, inclusive aplicação financeira)
- imunes e isentas com receitas, doações, incentivos, subvenções etc. abaixo de
  R$ 4.800.000,00 no ano (ou proporcional ao período)
- Lucro Presumido que mantém Livro Caixa com toda a movimentação financeira
  (art. 45, parágrafo único, da Lei nº 8.981/1995) — MAS fica obrigado se distribuir,
  sem IRRF, lucro acima da base de cálculo do imposto diminuída dos tributos devidos (§ 3º)
- Itaipu Binacional

LIVRO PRÓPRIO (§ 5º): SCP enquadrada na obrigatoriedade; PJ com recursos em moeda
estrangeira no exterior (art. 8º da Lei nº 11.371/2006); Empresa Simples de Crédito.

CONSTRUÇÃO CIVIL dispensada da EFD ICMS/IPI: apresenta o Registro de Inventário na
ECD como livro auxiliar (§ 4º).
```
Atenção: o limite de R$ 4,8 milhões vale só para as **imunes e isentas**. Para o Lucro Presumido, o critério é o Livro Caixa e a distribuição de lucros, não o faturamento.

### 2. Estrutura da ECD
```
Bloco 0  Abertura, identificação, participantes
Bloco C  Informações recuperadas da ECD anterior (saldos para amarração)
Bloco I  Lançamentos contábeis
         I010 identificação da escrituração · I012 livros auxiliares · I030 termo de abertura
         I050 plano de contas · I051 plano de contas REFERENCIAL · I052 códigos de
         aglutinação · I053 subcontas correlatas
         I075 históricos padronizados · I100 centros de custos
         I150/I155 saldos periódicos · I157 transferência de saldos do plano anterior
         I200/I250 lançamentos e partidas
         I300/I310 balancetes diários · I350/I355 saldos das contas de resultado
         antes do encerramento · I500 a I555 Razão Auxiliar com leiaute parametrizável
Bloco J  Demonstrações e termos
         J005 demonstrações contábeis (período e cabeçalho) · J100 Balanço Patrimonial
         J150 DRE · J210 DLPA/DMPL · J215 fatos que alteram lucros acumulados/PL
         J800 outras informações (arquivo RTF: notas explicativas, relatório da
         administração, parecer dos auditores) · J801 termo de verificação para
         substituição da ECD · J900 termo de encerramento · J930 signatários da
         escrituração · J932 signatários do termo de verificação (ECD substituta)
         J935 auditores independentes
Bloco K  Conglomerados econômicos (demonstrações consolidadas)
Bloco 9  Controle e encerramento
```
Antes de gerar o arquivo, conferir no Manual de Orientação do Leiaute da ECD publicado no portal SPED para o ano da escrituração se algum registro foi incluído ou alterado.

### 3. Entrevista mínima
```
Q1: "Ano-calendário + CNPJ + regime tributário? (Presumido: tem Livro Caixa? distribuiu lucro acima da base?)"
Q2: "A ECD do ano anterior foi transmitida? Posso usá-la para conferir os saldos iniciais?"
Q3: "Tenho o TXT ou o balancete + DRE + plano de contas com referencial?"
Q4: "Há auditoria independente (J935)? Notas explicativas (J800)?"
Q5: "Certificados digitais válidos do contador (CRC ativo) e do representante legal?"
```

### 4. Leitura do TXT (somente leitura)
```bash
head -5 /caminho/ecd.txt                     # cabeçalho (0000)
grep -c "^|I200|" /caminho/ecd.txt           # quantidade de lançamentos
grep -c "^|I250|" /caminho/ecd.txt           # quantidade de partidas
grep -c "^|I050|" /caminho/ecd.txt           # contas do plano
grep -c "^|I051|" /caminho/ecd.txt           # mapeamentos referenciais
```
Conferências antes do PVA:
- Toda conta analítica do I050 tem I051 (referencial)?
- Saldos iniciais iguais aos saldos finais da ECD anterior (Bloco C ajuda)?
- Soma das partidas I250 = valor do I200, débitos = créditos?
- J100 fecha (Ativo = Passivo + PL)? J150 bate com o balancete?
- Termos de abertura e encerramento e signatários corretos?

### 5. Saldos iniciais
Os saldos iniciais de cada conta devem ser iguais aos saldos finais da ECD anterior. Cliente novo, sem ECD anterior: saldos do balanço de abertura, com explicação em nota (J800).

### 6. Plano referencial (registro I051)
Cada conta analítica precisa de código do Plano de Contas Referencial publicado pela RFB no portal SPED (a RFB atualiza o PCR; mapear com a versão do ano). Conta sem referencial = erro no PVA.
```
Conta da empresa (exemplo)     Código referencial (exemplo ilustrativo)
1.1.1.02.01 Banco c/c          <código da conta "bancos" na tabela referencial do ano>
2.1.1 Fornecedores             <código da conta "fornecedores" na tabela referencial do ano>
```
Não usar códigos referenciais de memória: buscar sempre na tabela vigente para o tipo de PJ.

### 7. Lançamentos I200/I250 (modelo ilustrativo)
```
|I200|001|15012026|9500,00|N|||
|I250|1.1.1.01.01||9500,00|D|||Venda à vista NF 12345||||
|I250|3.1.1.01.01||9500,00|C|||Receita de venda de mercadorias NF 12345||||
```
- I200 (campos na ordem): REG · NUM_LCTO (número) · DT_LCTO (data DDMMAAAA) · VL_LCTO (valor) · IND_LCTO (N normal; E encerramento de contas de resultado; X extemporâneo) · DT_LCTO_EXT (data dos fatos, só no extemporâneo) · VL_LCTO_MF (valor em moeda funcional, quando houver).
- I250 (campos na ordem): REG · COD_CTA (conta analítica) · COD_CCUS (centro de custos) · VL_DC (valor) · IND_DC (D/C) · NUM_ARQ (documento arquivado) · COD_HIST_PAD (histórico padrão do I075) · HIST (histórico) · COD_PART (participante do 0150) · VL_DC_MF e IND_DC_MF (moeda funcional, quando houver).
Histórico explicativo, nunca "conforme documentos".

### 8. Validação no PVA da ECD
Erros frequentes: conta analítica sem referencial; saldo inicial divergente; partidas que não fecham; natureza da conta errada; Balanço que não fecha (resultado não encerrado ou conta transitória com saldo).

### 9. Assinatura e transmissão
- Assinatura com certificado digital ICP-Brasil: contador (CRC ativo) e representante legal.
- Transmissão pelo PVA/Receitanet; guardar o recibo.
- Autenticação: o recibo de entrega da ECD faz a autenticação dos livros (Decreto nº 8.683/2016), sem passar pela Junta Comercial.

### 10. Entregável obrigatório

**a) Checklist de pré-validação**
```
[ ] Obrigatoriedade confirmada (art. 3º da IN RFB nº 2.003/2021)
[ ] 100% das contas analíticas com I051
[ ] Saldo inicial = saldo final da ECD anterior
[ ] Resultado encerrado; J100 fecha; J150 bate com o balancete
[ ] J800 anexado quando exigido; J935 se houver auditoria
[ ] PVA sem erros
[ ] Termos e signatários corretos; certificados válidos
[ ] Transmissão até o último dia útil de junho
```

**b) Diagnóstico do TXT**
```
Contas (I050): X · Referenciais (I051): Y · Lançamentos (I200): Z · Partidas (I250): W
Período: __/__/__ a __/__/__
ALERTAS: contas sem referencial · lançamentos com D ≠ C · saldos iniciais divergentes
```

**c) Lançamentos modelo**, quando o cliente pedir.

**d) Recibo de transmissão** arquivado.

## Erros comuns / pontos de atenção
- Usar o prazo antigo (31/05). Vale o último dia útil de junho.
- Saldo inicial divergente da ECD anterior.
- Conta sem I051.
- Partidas que não fecham.
- Histórico genérico.
- Signatário sem CRC ativo.
- Transmitir a ECF sem a ECD válida (a ECF, que vence no último dia útil de julho, recupera dados da ECD).
- **Multas** (art. 11 da IN RFB nº 2.003/2021, que remete ao art. 12 da Lei nº 8.218/1991):
  - não atender à forma exigida para registros e arquivos: 0,5% da receita bruta do período;
  - omitir ou informar incorretamente: 5% do valor da operação, limitada a 1% da receita bruta;
  - atraso: 0,02% por dia, sobre a receita bruta do período, limitada a 1% da receita bruta;
  - quem usa o SPED tem redução: metade, se cumprir depois do prazo mas antes de procedimento de ofício; 75%, se cumprir no prazo da intimação (parágrafo único do art. 12 da Lei nº 8.218/1991).
  A entidade não obrigada que entrega a ECD por opção não sofre essas multas (parágrafo único do art. 11 da IN RFB nº 2.003/2021). Não há "mínimo de R$ 5.000".

### Casos de borda
- **Cliente novo sem ECD anterior**: saldos do balanço de abertura; explicar em J800.
- **SCP**: ECD em livro próprio, quando enquadrada na obrigatoriedade.
- **Empresa em recuperação judicial**: ECD continua obrigatória.
- **Auditoria independente**: informar em J935 e anexar o parecer em J800 quando aplicável.
- **Saída do Simples no meio do ano**: ECD do período fora do Simples; saldo inicial = saldo na data da transição.

### Quando encaminhar para outra skill
- ECF depois da ECD → `ecf-escrituracao-contabil-fiscal`
- Cruzamento geral → `revisao-fiscal-cruzamento-sped`
- Plano de contas e referencial → `plano-contas-cpc`
- Fechamento mensal pendente → `fechamento-mensal`

### Autoavaliação
- [ ] Obrigatoriedade conferida?
- [ ] Referencial 100%?
- [ ] Saldos iniciais conferidos?
- [ ] Bloco J batendo com o balancete?
- [ ] PVA sem erros?
- [ ] Recibo arquivado?
- [ ] ECF agendada até o último dia útil de julho?

## Perguntas que o usuário costuma fazer
- **"Meu cliente do Presumido fatura R$ 6 milhões. É obrigado à ECD?"** O faturamento não decide. Se mantém Livro Caixa e não distribui lucro isento acima da base presumida (menos os tributos), está dispensado; senão, é obrigado. Na prática, quem tem contabilidade completa para distribuir lucro acima da base precisa da ECD.
- **"A ECD vence em maio?"** Não. Último dia útil de junho.
- **"Preciso registrar o livro na Junta?"** Não; a autenticação é feita pelo recibo do SPED.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): documento DOCX.
- Este padrão prevalece sobre outros formatos citados acima, exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- IN RFB nº 2.003/2021 — ECD: art. 3º (obrigados e dispensados), art. 5º (prazo), art. 11 (penalidades).
- IN RFB nº 2.142/2023 — prazo no último dia útil de junho.
- Lei nº 8.218/1991, art. 12 — multas.
- Lei nº 8.981/1995, art. 45, parágrafo único — Livro Caixa no Lucro Presumido.
- LC nº 123/2006, arts. 61-A a 61-D — investidor-anjo (exceção do Simples).
- Lei nº 11.371/2006, art. 8º — recursos em moeda estrangeira no exterior.
- Decreto nº 8.683/2016 — autenticação dos livros pelo SPED.
- Lei nº 6.404/1976 e Lei nº 11.638/2007 — demonstrações contábeis.
- CPC 26 (R1) — apresentação das demonstrações.
- Manual de Orientação do Leiaute da ECD (portal SPED — versão do ano da escrituração).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
