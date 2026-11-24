---
name: efd-icms-ipi
description: "Prepara e confere a EFD ICMS/IPI mensal (SPED Fiscal — Convênio ICMS s/nº/1970, Convênio ICMS 143/2006 e Ajuste SINIEF 2/2009): C100/C170/C190 (mercadorias), D (transporte), E110/E111/E116 (apuração do ICMS), E200 (ICMS-ST), E300 (DIFAL), E520/E530 (IPI), G (CIAP), H (inventário) e K (produção e estoque). Prazo definido pela legislação de cada UF. Acionar quando o usuário disser \"fazer o SPED Fiscal\", \"EFD ICMS IPI\", \"erro no PVA\", \"ajuste E111\", \"Tabela 5.1.1\", \"Bloco K\", \"CIAP\", \"inventário no Bloco H\", \"DIFAL E300\", \"conferir XML com a EFD\". Entrega validação dos XMLs, apuração E110/E520, ajustes E111 com código da UF, checklist e roteiro de transmissão."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# EFD ICMS/IPI mensal

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Confere a escrituração fiscal digital de ICMS e IPI do mês: notas de entrada e saída contra os XMLs, CFOP e CST, apuração do ICMS próprio, do ICMS-ST, do DIFAL e do IPI, ajustes com código da tabela da UF, CIAP, inventário e Bloco K. Aponta pendências antes do PVA.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Prazo:** não há prazo nacional único — o Ajuste SINIEF 2/2009 deixa o prazo para a legislação de
> cada UF (há UFs com dia 20 e outras com dia 25 do mês seguinte, por exemplo). Para cada
> estabelecimento, conferir o prazo no regulamento do ICMS e no portal da Secretaria da Fazenda da UF
> e registrá-lo no calendário do cliente.

## Quando usar
- Escrituração mensal de contribuinte do ICMS e/ou do IPI.
- Erro no PVA da EFD ICMS/IPI.
- Inventário anual (Bloco H), CIAP (Bloco G) e Bloco K.
- Retificação de EFD de mês anterior.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). XMLs de venda a consumidor podem trazer CPF: não reproduzir.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem. Os comandos abaixo só leem os XMLs.

## Passo a passo (instruções para o agente de IA)

### 1. Quem entrega
Contribuintes do ICMS e/ou do IPI, conforme o Ajuste SINIEF 2/2009 e a legislação da UF. Optantes do Simples Nacional, em regra, são dispensados (salvo exigência específica da UF). A obrigatoriedade **não depende do regime de IRPJ** (Real ou Presumido), e sim de ser contribuinte do ICMS/IPI e da regra da UF. Consulta: serviço "Consultar a obrigatoriedade de entrega da EFD ICMS/IPI" (gov.br).

### 2. Estrutura dos blocos
```
0  Abertura e cadastros (0150 participantes, 0200 itens com NCM, 0300 bens do CIAP)
B  Escrituração do ISS (só Distrito Federal)
C  Documentos fiscais de mercadorias (C100 cabeçalho, C170 itens, C190 analítico)
D  Documentos fiscais de serviços de transporte e comunicação (D100 CT-e)
E  Apuração: E110 ICMS próprio, E111 ajustes, E116 obrigações a recolher;
   E200/E210 ICMS-ST por UF; E300/E310 DIFAL e FCP; E500/E520/E530 IPI
G  CIAP — crédito de ICMS do ativo imobilizado em 48 parcelas
H  Inventário físico (H005/H010)
K  Controle da produção e do estoque (indústria e atacadista equiparado, conforme cronograma)
1  Outras informações (1010 obrigatoriedade de registros, 1100 exportação, 1300 combustíveis etc.)
9  Encerramento
```
Crédito extemporâneo de ICMS: o aproveitamento segue a regra da UF (algumas exigem autorização prévia) e, em regra, é lançado como ajuste no E111 com o código da Tabela 5.1.1 da UF. Conferir a legislação da UF e as instruções do Guia Prático antes de escriturar.

### 3. Entrevista mínima
```
Q1: "CNPJ + competência + UF (matriz e filiais têm EFD própria por estabelecimento)?"
Q2: "Tenho acesso aos XMLs (NF-e de entrada/saída, CT-e)? Qual pasta?"
Q3: "Indústria ou atacadista equiparado? (Bloco K conforme cronograma do Ajuste SINIEF 25/2016)"
Q4 (fevereiro): "Inventário de 31/12 levantado?"
Q5: "Saldo credor anterior? Benefícios fiscais (Zona Franca, ALC, decreto estadual)?"
```

### 4. Leitura dos XMLs (somente leitura)
```bash
ls /pasta/xmls/*.xml | wc -l                                  # quantos XMLs
grep -h "<vNF>" /pasta/xmls/*.xml | head -5                   # amostra de valores
grep -ho "<CFOP>....</CFOP>" /pasta/xmls/*.xml | sort | uniq -c | sort -rn | head -10   # CFOPs
```

### 5. C170/C190 (modelo ilustrativo)
```
|C170|001|PROD0001|Produto X|10|UN|1500,00|0,00|0|000|5102|...|
|C190|000|5102|18,00|1500,00|1500,00|270,00|...|
```
O C190 consolida por CST + CFOP + alíquota e alimenta a apuração. Campos exatos: Guia Prático da EFD ICMS/IPI.

### 6. Apuração do ICMS próprio (E110)
```
Total de débitos (saídas) ..................... R$ ____
(+) Ajustes a débito / estornos de crédito ..... R$ ____  (E111)
Total de créditos (entradas) .................. R$ ____
(+) Ajustes a crédito / estornos de débito ..... R$ ____  (E111)
Saldo credor do período anterior .............. R$ ____
Saldo devedor apurado ......................... R$ ____
(−) Deduções .................................. R$ ____
ICMS a recolher ............................... R$ ____  (detalhado no E116)
Saldo credor a transportar .................... R$ ____
```
Identificar os campos do E110 pelos nomes do Guia Prático, não por números de posição.
Ajustes do E111 usam o código da **Tabela 5.1.1** da UF (cada UF publica a sua).

### 7. CIAP (Bloco G — 48 parcelas)
```
Crédito mensal = (ICMS do bem ÷ 48) × (saídas tributadas e exportação ÷ total das saídas)
```
Base: art. 20, § 5º, da LC nº 87/1996. G110 controla o período; G125 o bem. Bem do imobilizado sem CIAP: crédito não aproveitado.

### 8. Inventário (Bloco H)
Estoque de 31/12 informado na EFD do período de **fevereiro** do ano seguinte (regra geral do Guia Prático; algumas UFs têm regra própria). Cada item: código, unidade, quantidade, valor unitário e total.

### 9. Bloco K
Obrigatório para indústria e atacadista equiparado, conforme o cronograma e o tipo de escrituração (completa ou simplificada) do Ajuste SINIEF 25/2016; para o IPI, ver também a IN RFB nº 1.652/2016. O enquadramento depende de cada estabelecimento (CNAE, faturamento e regra da UF): conferir no cronograma do ajuste e na legislação da UF antes de dispensar ou exigir o Bloco K. Pontos de atenção:
- Consumo de insumos (K235) coerente com a ficha técnica do produto.
- Estoque escriturado (K200) coerente com o inventário (H010) no fim do ano.

### 10. Validação no PVA
Zero erros. Frequentes:
- CFOP incompatível com a operação (ex.: 5.949 usado para venda).
- CST/CSOSN incompatível com o regime do emitente (CSOSN só para emitente do Simples).
- DIFAL mal escriturado no E300.
- Soma do C190 diferente do E110.
- Item do C170 sem 0200.

### 11. Entregável obrigatório

**a) Apuração E110 + E200 + E300 + E520** (débitos × créditos × saldo por tributo).

**b) Ajustes E111** com código da Tabela 5.1.1 da UF, por motivo.

**c) Memória** (planilha agregada por CFOP/CST).

**d) Recibo** de transmissão (assinatura com certificado digital e envio pelo PVA/Receitanet).

**e) Checklist**
```
[ ] Todos os XMLs do mês escriturados (XML × EFD sem divergência)
[ ] CFOP e CST revisados (amostra de 20 notas)
[ ] CIAP atualizado (G125 do mês)
[ ] Ajustes E111 com código da Tabela 5.1.1 da UF
[ ] DIFAL no E300
[ ] PVA sem erros
[ ] Saldo apurado igual ao do sistema fiscal
[ ] Inventário no Bloco H (EFD de fevereiro)
[ ] Prazo da UF respeitado
```

## Erros comuns / pontos de atenção
- CFOP genérico para venda (usar 5.102, 5.405 etc. conforme o caso).
- CST/CSOSN incompatível com o regime.
- Bloco K sem coerência com a ficha técnica.
- Imobilizado sem CIAP.
- CT-e não escriturado: perde crédito do frete.
- Inventário de 31/12 não informado na EFD de fevereiro.
- Aplicar regra de obrigatoriedade pelo regime de IRPJ ("Lucro Real sempre; Presumido depende do estado" não é o critério).

### Casos de borda
- **Zona Franca de Manaus/ALC**: benefícios de ICMS e IPI próprios; conferir códigos de ajuste e CST.
- **Brindes e amostras**: CFOP 5.910/6.910; tributação conforme a UF.
- **Devoluções**: CFOP 1.201/2.201 (entrada) e 5.201/6.201 (saída), com crédito/débito espelho.
- **Transferência entre estabelecimentos do mesmo titular**: não há incidência do ICMS (STF, ADC 49); a LC nº 204/2023 regulou a transferência do crédito. Conferir a regra da UF para a escrituração.
- **Reforma Tributária**: em 2026 a NF-e passa a destacar CBS e IBS em caráter de teste; a EFD ICMS/IPI continua para ICMS e IPI. A cada nova versão do Guia Prático, conferir as notas de alteração do leiaute.

### Quando encaminhar para outra skill
- ICMS-ST e DIFAL detalhados → `calculo-icms-icms-st`
- IPI mensal → `calculo-ipi`
- Cruzamento geral → `revisao-fiscal-cruzamento-sped`
- Restituição de ICMS-ST pago a maior (STF, Tema 201) → skill de recuperação de créditos

### Autoavaliação
- [ ] XMLs lidos e quantidade conferida?
- [ ] CFOP/CST revisados?
- [ ] CIAP atualizado?
- [ ] Ajustes E111 com código correto?
- [ ] DIFAL no E300?
- [ ] Bloco K conferido (se aplicável)?
- [ ] PVA sem erros e prazo da UF respeitado?
- [ ] Recibo arquivado?

## Perguntas que o usuário costuma fazer
- **"Empresa do Lucro Presumido entrega EFD ICMS/IPI?"** Se for contribuinte do ICMS ou do IPI e não for dispensada pela UF, sim. O regime de IRPJ não decide.
- **"O inventário vai na EFD de dezembro?"** Em regra, na de fevereiro do ano seguinte.
- **"Posso retificar a EFD de um mês antigo?"** Sim, observando as regras do Ajuste SINIEF 2/2009 e da UF (algumas exigem autorização depois do prazo).

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): documento DOCX.
- Este padrão prevalece sobre outros formatos citados acima, exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- Convênio ICMS s/nº, de 15/12/1970 — Sistema Nacional Integrado de Informações Econômico-Fiscais.
- Convênio ICMS 143/2006 — institui a EFD.
- Ajuste SINIEF 2/2009 — EFD ICMS/IPI (obrigatoriedade, prazo remetido à UF, retificação).
- Ajuste SINIEF 25/2016 — Bloco K.
- LC nº 87/1996 (Lei Kandir), art. 20, § 5º — CIAP.
- LC nº 190/2022 — DIFAL.
- LC nº 204/2023 — transferência entre estabelecimentos do mesmo titular.
- STF, ADC 49 — não incidência do ICMS na transferência.
- Convênio ICMS 142/2018 — regras gerais do ICMS-ST.
- IN RFB nº 1.652/2016 — obrigatoriedade do Livro de Registro de Controle da Produção e do Estoque (Bloco K) na EFD ICMS/IPI para estabelecimentos industriais e equiparados, no âmbito do IPI.
- Guia Prático da EFD ICMS/IPI e Tabela 5.1.1 da UF (portal SPED e portais estaduais).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
