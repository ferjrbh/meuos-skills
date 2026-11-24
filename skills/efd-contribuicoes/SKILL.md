---
name: efd-contribuicoes
description: "Prepara e confere a EFD-Contribuições mensal (PIS/COFINS e CPRB): escrituração por CST, créditos do não cumulativo, Bloco M (apuração), F500/F550 (regime de caixa ou competência no cumulativo), F600 (retenções sofridas), F150 (estoque de abertura), Bloco P (CPRB) e conciliação com a DCTFWeb/MIT. Prazo: até o 10º dia útil do 2º mês seguinte (art. 7º da IN RFB nº 1.252/2012). Considera a LC nº 224/2025 (tributação parcial de operações isentas/alíquota zero desde 04/2026). Acionar quando o usuário disser \"fazer a EFD-Contribuições\", \"SPED PIS COFINS\", \"erro no PVA da EFD-Contribuições\", \"M200\", \"M600\", \"CST 50\", \"F600\", \"F500\", \"Bloco P\", \"PIS/COFINS não bate com a DCTFWeb\". Entrega validação por amostra de notas, apuração consolidada, cruzamento com DCTFWeb e checklist."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# EFD-Contribuições mensal

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Confere e organiza a escrituração mensal de PIS/COFINS (e da CPRB, quando houver): classificação por CST de cada item, créditos no regime não cumulativo, apuração no Bloco M, retenções sofridas e cruzamento com os débitos informados no MIT/DCTFWeb.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Prazo:** até o **10º dia útil do 2º mês seguinte** ao da escrituração (art. 7º da IN RFB nº 1.252/2012),
> e não "dia 10", inclusive em extinção, incorporação, fusão e cisão. Exemplo: competência
> outubro/2026 vence no 10º dia útil de dezembro/2026.
> **2026:** a LC nº 224/2025 passou a tributar parcialmente (10% da alíquota cheia: PIS 0,165% e
> COFINS 0,76%) várias operações antes isentas ou com alíquota zero, desde 01/04/2026, e limitou
> créditos presumidos a 90%. Antes de classificar CST de isenção ou alíquota zero, conferir se a
> operação foi alcançada pela LC nº 224/2025 e se o cliente tem decisão judicial (há liminares em
> TRFs para alguns contribuintes).

## Quando usar
- Escrituração mensal de PIS/COFINS (Lucro Real não cumulativo, Lucro Presumido cumulativo).
- Empresa na CPRB em transição (Bloco P).
- Erro no PVA da EFD-Contribuições.
- Divergência entre EFD-Contribuições e DCTFWeb/MIT.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Estrutura dos blocos
```
0  Abertura e cadastros (0110 regime de apuração, 0140 estabelecimentos, 0150
   participantes, 0200 itens, 0500 plano de contas)
A  Documentos fiscais de serviços (NFS-e)
C  Documentos fiscais de mercadorias (C100/C170 com CST PIS/COFINS por item)
D  Documentos fiscais de transporte e comunicação
F  Demais documentos e operações: F100 (demais operações), F120/F130 (créditos sobre
   imobilizado), F150 (crédito presumido sobre estoque de abertura), F500/F550
   (consolidação no cumulativo — caixa e competência), F600 (contribuição retida na
   fonte), F700 (deduções diversas)
I  Instituições financeiras e equiparadas
M  Apuração: M100/M105 (créditos PIS), M200/M210 (PIS devido), M500/M505
   (créditos COFINS), M600/M610 (COFINS devida)
P  Apuração da CPRB (P100, P200)
1  Complemento: 1010/1020 (processos), 1100 e 1500 (controle de créditos de PIS e
   COFINS), 1300 e 1700 (controle de retenções na fonte)
9  Encerramento

PRAZO: até o 10º dia útil do 2º mês seguinte ao da escrituração
```
Antes de gerar o arquivo, conferir no Guia Prático da EFD-Contribuições da versão em uso (portal SPED) se houve inclusão ou alteração de registros.

### 2. CST de PIS/COFINS (principais)
```
SAÍDAS
01  Tributável — alíquota básica
02  Tributável — alíquota diferenciada
03  Tributável — alíquota por unidade de medida
04  Tributável monofásica — revenda a alíquota zero
05  Tributável por substituição tributária
06  Alíquota zero
07  Isenta
08  Sem incidência (ex.: exportação de mercadorias)
09  Suspensão
49  Outras saídas

ENTRADAS (não cumulativo)
50  Com direito a crédito — vinculada só a receita tributada no mercado interno
51  Com direito a crédito — vinculada só a receita não tributada no mercado interno
52  Com direito a crédito — vinculada só a receita de exportação
53 a 56  Vinculadas a mais de um tipo de receita (rateio)
60 a 67  Crédito presumido
70  Aquisição sem direito a crédito
71  Aquisição com isenção · 72 com suspensão · 73 a alíquota zero
74  Aquisição sem incidência · 75 por substituição tributária
98  Outras operações de entrada · 99 Outras operações
```
Códigos da Tabela 4.3.3 (CST PIS/COFINS) do Guia Prático da EFD-Contribuições. Atenção às trocas mais comuns: 06 é alíquota zero (não isenção), 07 é isenção, 09 é suspensão e 70 é aquisição sem direito a crédito.

### 3. Entrevista mínima
```
Q1: "CNPJ + competência + regime (não cumulativo / cumulativo / misto / CPRB)?"
Q2: "Tenho os XMLs do mês (NF-e de entrada e saída, NFS-e, CT-e)?"
Q3: "A apuração interna de PIS/COFINS está pronta para conciliação?"
Q4 (cumulativo): "Regime de caixa ou competência? Há receitas monofásicas, exportação, CSRF retida?"
Q5 (CPRB): "A empresa está na desoneração em transição (Lei nº 14.973/2024)?"
Q6 (2026): "Há operações antes isentas ou a alíquota zero alcançadas pela LC nº 224/2025?"
```

### 4. Validação técnica
- Conferir CST por item (amostra mínima de 20 notas).
- Cruzar M200/M600 com a apuração interna.
- Verificar exclusão do ICMS destacado da base de PIS/COFINS (Tema 69 do STF, RE 574.706).
- Verificar exclusão do ICMS da base dos créditos (Lei nº 14.592/2023).
- F600 com as retenções sofridas documentadas.

### 5. Receitas financeiras no não cumulativo
PIS 0,65% e COFINS 4% sobre receitas financeiras (Decreto nº 8.426/2015). Não é alíquota zero.

### 6. Bloco M
```
M100/M105  créditos de PIS por tipo e por CST de origem (50 a 56, 60 a 66)
M200/M210  PIS devido por tipo de contribuição
M500/M505  créditos de COFINS
M600/M610  COFINS devida
```
Créditos sobre insumos seguem o critério de essencialidade e relevância do STJ (REsp 1.221.170, Temas 779 e 780): documentar a ligação de cada item com a atividade.

### 7. F500/F550 e F600
- **F500/F550**: consolidação das receitas no regime cumulativo (F500 caixa; F550 competência).
- **F600**: contribuições retidas na fonte (ex.: CSRF retida pelo cliente sobre serviço prestado).

### 8. Entregável obrigatório

**a) Apuração consolidada**
```
EFD-Contribuições — MM/AAAA — CNPJ __ (EMPRESA EXEMPLO)

Receitas por CST:
  Vendas tributadas — CST 01 ...... R$ X (PIS R$ Y, COFINS R$ Z)
  Exportação — CST 08 ............. R$ X (sem PIS/COFINS)
  Monofásica revenda — CST 04 ..... R$ X (sem PIS/COFINS)

Créditos (não cumulativo):
  Insumos — CST 50 ................ R$ X (PIS R$ Y, COFINS R$ Z)
  Energia — CST 50 ................ R$ X
  Frete na venda — CST 50 ......... R$ X

M200/M600: PIS R$ __ / COFINS R$ __
F600 (retenções sofridas): R$ __
Saldo a recolher: PIS R$ __ / COFINS R$ __   ou saldo credor a transportar: R$ __
```

**b) Cruzamento com a DCTFWeb/MIT**: PIS/COFINS do Bloco M devem bater com os débitos informados no MIT da mesma competência. Qualquer diferença precisa de explicação documentada ou retificação.

**c) Memória de cálculo** (planilha).

**d) Checklist**
```
[ ] Cadastros 0110/0140/0150/0200/0500 atualizados
[ ] CSTs revisados por amostra
[ ] Bloco M batendo com a apuração interna
[ ] ICMS excluído da base (Tema 69) e dos créditos (Lei nº 14.592/2023)
[ ] F500/F550/F600 preenchidos quando aplicável
[ ] Efeitos da LC nº 224/2025 considerados (a partir de 04/2026)
[ ] PVA sem erros
[ ] DCTFWeb/MIT conciliados
[ ] Transmitida até o 10º dia útil do 2º mês seguinte
```

## Erros comuns / pontos de atenção
- CST de entrada com direito a crédito (50) sem o crédito no M105.
- ICMS não excluído da base (Tema 69).
- F600 sem preenchimento: perde a dedução da retenção.
- Receita financeira tratada como alíquota zero no não cumulativo.
- Empresa no cumulativo lançando créditos no Bloco M.
- Esquecer o Bloco P quando a empresa está na CPRB.
- Classificar como isenta ou alíquota zero operação que passou a ter tributação parcial pela LC nº 224/2025 (desde 01/04/2026).
- **Multa** (art. 10 da IN RFB nº 1.252/2012, com redação da IN RFB nº 1.876/2019, que remete ao art. 12 da Lei nº 8.218/1991): 0,5% da receita bruta (forma exigida); 5% do valor da operação, limitada a 1% da receita bruta (omissão/incorreção); 0,02% por dia de atraso sobre a receita bruta, limitada a 1% da receita bruta. A multa do inciso I cai à metade se a obrigação for cumprida antes de procedimento de ofício. Retificação: possível em até 5 anos contados do 1º dia do exercício seguinte ao da escrituração (art. 11 da IN RFB nº 1.252/2012).

### Casos de borda
- **Migração do Presumido para o Real**: crédito presumido sobre o estoque de abertura (art. 11 da Lei nº 10.637/2002 e art. 12 da Lei nº 10.833/2003) no **F150**, não no F600.
- **Lucro Real com receitas que continuam no cumulativo** (art. 10 da Lei nº 10.833/2003 — ex.: serviços hospitalares, transporte coletivo de passageiros, telecomunicações): regime misto, com codificação no 0110.
- **Empresa em recuperação judicial**: escrituração normal; débitos podem ir para parcelamento/transação.
- **Reforma Tributária**: em 2026 a CBS (0,9%) e o IBS (0,1%) são destacados no documento em caráter de teste; não substituem PIS/COFINS na EFD-Contribuições em 2026. A CBS substitui PIS/COFINS a partir de 2027 (LC nº 214/2025).

### Quando encaminhar para outra skill
- Apuração cumulativa detalhada → `calculo-pis-cofins-cumulativo`
- Apuração não cumulativa → `calculo-pis-cofins-nao-cumulativo`
- Recuperação retroativa → `recuperacao-creditos-pis-cofins`
- Cruzamento geral → `revisao-fiscal-cruzamento-sped`

### Autoavaliação
- [ ] CSTs revisados?
- [ ] Bloco M bate com a apuração interna?
- [ ] ICMS excluído (Tema 69)?
- [ ] F500/F550/F600 preenchidos?
- [ ] LC nº 224/2025 considerada?
- [ ] DCTFWeb/MIT cruzada?
- [ ] PVA sem erros e prazo respeitado?

## Perguntas que o usuário costuma fazer
- **"Vence dia 10?"** Não: 10º dia útil do 2º mês seguinte.
- **"Exportação é CST 06?"** Em regra, exportação de mercadorias é receita sem incidência (CST 08); CST 06 é alíquota zero.
- **"A EFD-Contribuições acaba em 2027?"** A CBS substitui PIS/COFINS a partir de 2027 (LC nº 214/2025). Fatos até 2026 continuam escriturados na EFD-Contribuições, inclusive retificações. As obrigações acessórias da CBS serão as que a RFB regulamentar: acompanhar os atos publicados antes de 2027.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): documento DOCX.
- Este padrão prevalece sobre outros formatos citados acima, exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- IN RFB nº 1.252/2012 — EFD-Contribuições (art. 7º: prazo; art. 10: multas, redação da IN RFB nº 1.876/2019; art. 11: retificação).
- IN RFB nº 2.121/2022 — consolidação das normas de PIS/COFINS.
- Lei nº 10.637/2002 (PIS não cumulativo), art. 11 — estoque de abertura.
- Lei nº 10.833/2003 (COFINS não cumulativa), arts. 10 e 12.
- Lei nº 9.718/1998 — regime cumulativo.
- Lei nº 14.592/2023 — exclusão do ICMS da base dos créditos.
- Decreto nº 8.426/2015 — receitas financeiras.
- Lei nº 14.973/2024 — CPRB em transição.
- LC nº 224/2025 — tributação parcial de operações isentas/alíquota zero e limite de créditos presumidos.
- LC nº 214/2025 — CBS/IBS (teste em 2026).
- Lei nº 8.218/1991, art. 12 — multas.
- STF, RE 574.706 (Tema 69); STJ, REsp 1.221.170 (Temas 779 e 780).
- Guia Prático da EFD-Contribuições e Tabela 4.3.3 (portal SPED).
- Perguntas e Respostas Pessoa Jurídica da RFB — capítulo EFD-Contribuições (prazo, multa, retificação).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
