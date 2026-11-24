---
name: calcular-das-simples-nacional
description: "Calcula o DAS mensal do Simples Nacional a partir do faturamento — separa as receitas, define o Anexo (I a V) e o fator R, aplica a RBT12 e o sublimite estadual e entrega o cálculo passo a passo, memória de cálculo e checklist contra o PGDAS-D. Diferença: a skill 'conferir-apuracao-simples-nacional' valida um PGDAS-D já preenchido cruzando com as notas; esta faz o cálculo do zero quando só há o faturamento. Use quando o usuário enviar faturamento de optante, pedir para \"calcular o DAS\", \"gerar DAS\", ou falar de \"alíquota efetiva\", \"RBT12\", \"fator R\", \"anexo\", \"sublimite\", \"PGDAS-D\". Não use para MEI (use 'apuracao-mei')."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Calcular o DAS do Simples Nacional

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Calcula o DAS do mês pela alíquota efetiva, que depende da RBT12 (receita bruta dos 12 meses anteriores ao mês apurado). Separa receitas com tratamento especial (ST, monofásico, exportação, ISS retido), decide entre Anexo III e V pelo fator R e confere o sublimite de ICMS/ISS. Entrega memória de cálculo, valor do DAS com vencimento e checklist para conferir no PGDAS-D.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Cálculo mensal do DAS de optante (ME ou EPP).
- Conferência do valor que o PGDAS-D gerou.
- Dúvida de anexo, fator R ou sublimite.
- Planejamento: simular o efeito da folha no fator R.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Para o fator R basta o total da folha; não pedir salário por empregado.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Antes de calcular, confirmar que a empresa ainda é optante (pode ter sido excluída sem saber).

## Passo a passo (instruções para o agente de IA)

### 1. Tabelas (LC nº 123/2006, Anexos I a V, redação da LC nº 155/2016; vigentes em 2026)
```
ANEXO I — Comércio                 ANEXO II — Indústria
Faixa  RBT12 até     Nominal  PD       Faixa  RBT12 até   Nominal  PD
1      180.000       4,00%        0    1      180.000     4,50%        0
2      360.000       7,30%    5.940    2      360.000     7,80%    5.940
3      720.000       9,50%   13.860    3      720.000    10,00%   13.860
4    1.800.000      10,70%   22.500    4    1.800.000    11,20%   22.500
5    3.600.000      14,30%   87.300    5    3.600.000    14,70%   85.500
6    4.800.000      19,00%  378.000    6    4.800.000    30,00%  720.000

ANEXO III — Serviços (e fator R ≥ 28%)   ANEXO V — Serviços (fator R < 28%)
1      180.000       6,00%        0    1      180.000    15,50%        0
2      360.000      11,20%    9.360    2      360.000    18,00%    4.500
3      720.000      13,50%   17.640    3      720.000    19,50%    9.900
4    1.800.000      16,00%   35.640    4    1.800.000    20,50%   17.100
5    3.600.000      21,00%  125.640    5    3.600.000    23,00%   62.100
6    4.800.000      33,00%  648.000    6    4.800.000    30,50%  540.000

ANEXO IV — Construção, limpeza, vigilância, obras, advocacia
(CPP — INSS patronal — fica FORA do DAS)
1      180.000       4,50%        0    4    1.800.000    14,00%   39.780
2      360.000       9,00%    8.100    5    3.600.000    22,00%  183.780
3      720.000      10,20%   12.420    6    4.800.000    33,00%  828.000

PD = parcela a deduzir

LIMITES 2026
Simples: R$ 4.800.000/ano · MEI: R$ 81.000/ano
Sublimite ICMS/ISS 2026: R$ 3.600.000 em todos os estados e no DF
  (Portaria CGSN nº 54/2025; o sublimite opcional de R$ 1.800.000 do
  art. 19 da LC nº 123/2006 só vale no estado que o adotar no ano)
Vencimento do DAS: dia 20 do mês seguinte
DEFIS: até 31 de março do ano seguinte
```

### 2. Fórmulas
```
Alíquota efetiva = [(RBT12 × alíquota nominal) − parcela a deduzir] ÷ RBT12
DAS do mês = receita do mês × alíquota efetiva
(art. 18, §§ 1º e 1º-A, da LC nº 123/2006)
```
A alíquota nominal nunca é aplicada direto sobre a receita.

### 3. Entrevista mínima (uma pergunta por vez)
```
P1: "CNPJ + competência + faturamento bruto do mês?"
P2 (mais de uma atividade): "Comércio, indústria, serviço ou misto? Separe o valor de cada um."
P3 (serviço): "Qual a atividade exata? (TI, engenharia, medicina etc.)"
P4 (Anexo III/V): "Total da folha paga nos últimos 12 meses (salários, pró-labore, 13º, férias, CPP efetivamente recolhida — inclusive a do DAS — e FGTS)?"
P5: "RBT12 (receita dos 12 meses ANTERIORES ao mês)?"
P6: "Tem ST, monofásico, ISS retido pelo tomador, exportação ou filial em outra UF?"
```
Se faltar algo periférico, declare a suposição ("Assumindo sem ST e sem ISS retido. Corrija se errado.") e siga.

### 4. Cálculo (rodar em Python, nunca de cabeça)
```python
# DAS do Simples Nacional — alíquota efetiva por anexo.
ANEXOS = {
    "I":   [(180_000, .04, 0), (360_000, .073, 5_940), (720_000, .095, 13_860),
            (1_800_000, .107, 22_500), (3_600_000, .143, 87_300), (4_800_000, .19, 378_000)],
    "III": [(180_000, .06, 0), (360_000, .112, 9_360), (720_000, .135, 17_640),
            (1_800_000, .16, 35_640), (3_600_000, .21, 125_640), (4_800_000, .33, 648_000)],
    "V":   [(180_000, .155, 0), (360_000, .18, 4_500), (720_000, .195, 9_900),
            (1_800_000, .205, 17_100), (3_600_000, .23, 62_100), (4_800_000, .305, 540_000)],
}

def aliquota_efetiva(anexo, rbt12):
    for teto, nominal, pd in ANEXOS[anexo]:
        if rbt12 <= teto:
            return ((rbt12 * nominal) - pd) / rbt12
    raise ValueError("RBT12 acima de R$ 4,8 mi: fora do Simples")

def anexo_por_fator_r(folha_12m, rbt12):
    fator_r = folha_12m / rbt12
    return ("III" if fator_r >= 0.28 else "V"), fator_r

# Exemplo: TI, RBT12 600.000, receita do mês 50.000, folha 12m 200.000
anexo, fr = anexo_por_fator_r(200_000, 600_000)
ae = aliquota_efetiva(anexo, 600_000)
print(f"Fator R {fr:.2%} -> Anexo {anexo}; alíquota efetiva {ae:.4%}; DAS R$ {50_000*ae:,.2f}")
# Esperado: Anexo III; 10,5600%; R$ 5.280,00
```
Mais de um anexo: calcule cada um separado e some. Mostre a alíquota com 4 casas.

### 5. Fator R (art. 18, §§ 5º-J, 5º-K, 5º-M e 24, da LC nº 123/2006; art. 26 da Resolução CGSN nº 140/2018)
```
Fator R = folha paga nos 12 meses anteriores ÷ RBT12
Folha = remunerações de empregados e avulsos (com 13º) + pró-labore e autônomos
        + CPP efetivamente recolhida (inclusive a recolhida dentro do DAS) + FGTS
        (NÃO entram distribuição de lucros, aluguéis, bolsa de estagiário e pagamentos a MEI)
≥ 28% → Anexo III      < 28% → Anexo V
```
- Atividades sujeitas ao fator R (vão ao V se o fator for menor que 28%): TI e desenvolvimento de software no estabelecimento, engenharia, arquitetura, medicina (inclusive laboratorial) e enfermagem, odontologia, fisioterapia, psicologia, fonoaudiologia e outras de saúde da lista, medicina veterinária, publicidade, auditoria, consultoria, perícia, despachante, tradução, representação comercial (art. 18, §§ 5º-B, XVI e XVIII a XXI, 5º-D e 5º-I).
- **Não** dependem do fator R: **advocacia** (Anexo IV, CPP por fora), **escritório de contabilidade** (Anexo III direto, § 5º-B, XIV) e **corretagem de seguros** (Anexo III direto, § 5º-B, XVII).
- **Empresa com menos de 13 meses** (regra até 2026): proporcionalize a RBT12 = (receita dos meses anteriores ÷ nº de meses) × 12, e faça o mesmo com a folha. No 1º mês, use a receita do próprio mês × 12 (Resolução CGSN nº 140/2018, arts. 21 e 26; pergunta 5.4 do Perguntas e Respostas do Simples Nacional).
- **A partir de 2027**: a RBT12 e a folha passam a ser as dos 12 meses antecedentes ao mês anterior ao período de apuração; nos 2 primeiros meses de atividade aplica-se a 1ª faixa, sem proporcionalização (Perguntas e Respostas do Simples Nacional, perguntas 5.3.2, 5.4.2 e 5.11).

### 6. Tratamentos especiais
**ICMS-ST e monofásicos** (combustíveis, autopeças, medicamentos, cosméticos, bebidas frias): separe a receita e tire da alíquota efetiva a parte do ICMS (ST) ou do PIS + COFINS (monofásico), usando a partilha do anexo.
```
Partilha do Anexo I, 4ª faixa (LC nº 123/2006, Anexo I; igual na 3ª e na 5ª faixas):
IRPJ 5,50% · CSLL 3,50% · COFINS 12,74% · PIS 2,76% · CPP 42,00% · ICMS 33,50%
(soma = 100%)
```
**Exportação**: sem ICMS, ISS, PIS, COFINS e IPI. No Anexo I, 4ª faixa, sobra 51% da alíquota efetiva (IRPJ + CSLL + CPP): com efetiva entre 7,575% e 9,45%, a exportação fica entre cerca de 3,86% e 4,82%.

**ISS retido pelo tomador**: não mexa na receita. Calcule o DAS normal e informe o ISS retido no campo próprio do PGDAS-D, que tira o ISS do DAS (art. 21, §4º, da LC nº 123/2006).

**Sublimite estourado** (receita acumulada no ano acima de R$ 3,6 mi em 2026): ICMS e ISS passam a ser pagos fora do DAS, no regime normal do estado/município; os tributos federais seguem no DAS. Excesso de até 20% no ano: efeito a partir do ano seguinte. Acima de 20%: efeito a partir do mês seguinte ao excesso (art. 20 da LC nº 123/2006).

**Exclusão por excesso**: receita acumulada no ano acima de R$ 4,8 mi → exclusão a partir de 1º de janeiro seguinte. Acima de R$ 5,76 mi (20% a mais) → exclusão a partir do mês seguinte ao excesso (art. 30 da LC nº 123/2006; pergunta 4.3 do Perguntas e Respostas do Simples Nacional).

**Filial em outra UF**: a apuração é do CNPJ (matriz + filiais) e a receita é informada por estabelecimento; o sublimite é por UF.

### 7. Reforma Tributária e Simples
- Em 2026 (ano-teste) a optante não precisa destacar CBS/IBS. A NF-e de optante (CRT 1, 2 e 4) sem os grupos de CBS/IBS passa a ser rejeitada a partir de 04/01/2027.
- A opção pelo regime regular de CBS/IBS (fora do DAS) é semestral, com janelas em setembro e março. A do 1º semestre de 2027 foi feita de 01/09 a 30/10/2026 e pode ser cancelada, de forma irretratável, de 03/11 a 20/12/2026 (Resolução CGSN nº 186/2026, com os prazos alterados pela Resolução CGSN nº 194/2026). Pergunte se o cliente optou: isso muda o DAS de 2027, não o de 2026.
- Em 2027 o regime de caixa deixa de existir no Simples (pergunta 5.7 do Perguntas e Respostas do Simples Nacional).

### 8. Entregável obrigatório
**a) Tabela de receitas separadas**
```
Tipo                         Receita    Anexo  Tratamento
Comércio normal              80.000     I      padrão
Comércio com ST              20.000     I      sem ICMS (33,50% da efetiva, 4ª faixa)
Serviço de TI                50.000     III    fator R 32% → Anexo III
Total                        150.000
```
**b) Cálculo passo a passo** de cada anexo (alíquota efetiva com 4 casas) e DAS por anexo.
**c) Memória de cálculo** com colunas `anexo, faixa, rbt12, aliq_nominal, parcela_deduzir, aliq_efetiva, receita_mes, das_anexo, observacao`.
**d) DAS final** com vencimento explícito (ex.: competência 12/2026 → "20/01/2027, quarta-feira"). Se o dia 20 cair em feriado ou fim de semana (ex.: 20/11, Dia da Consciência Negra, feriado nacional pela Lei nº 14.759/2023), conferir no Portal do Simples a data que o PGDAS-D imprime na guia.
**e) Conferência no PGDAS-D**: lançar as receitas separadas como na tabela; tolerância de R$ 0,01. Divergência maior indica erro de classificação, RBT12 ou fator R.
**f) Checklist (7 itens)**
```
[ ] Empresa ainda optante (consulta no Portal do Simples)
[ ] CNAE bate com a receita declarada
[ ] RBT12 = 12 meses ANTERIORES (não o acumulado do ano)
[ ] Receita com ST, monofásico e exportação separada
[ ] Fator R com folha completa (inclui pró-labore, 13º, férias, CPP — também a do DAS — e FGTS)
[ ] Sublimite estadual conferido
[ ] ISS retido informado no campo próprio do PGDAS-D
```

### 9. Casos de borda
- **Mudou de anexo no meio do ano** (fator R subiu ou caiu): calcule por competência, sem retroagir.
- **RBT12 acima de R$ 4,5 mi**: alertar já, o limite está perto → `analise-tributaria-regime`.
- **DAS do PGDAS-D diferente do seu cálculo**: o sistema quase sempre está certo; revise a classificação, a RBT12 e o fator R.
- **Atrasos** (duas multas diferentes):
  - **Pagamento** do DAS em atraso: multa de mora de 0,33% por dia, limitada a 20%, mais juros de mora pela Selic (art. 35 da LC nº 123/2006 c/c art. 61 da Lei nº 9.430/1996).
  - **Entrega** do PGDAS-D fora do prazo: 2% ao mês-calendário ou fração sobre os tributos declarados, ainda que pagos, limitada a 20%, com mínimo de R$ 50,00 por mês de referência; reduzida à metade se a declaração for entregue antes de procedimento de ofício (art. 38-A, I, e §§ 2º e 3º, da LC nº 123/2006).
- **DAS abaixo de R$ 10,00**: não é emitido; o valor é somado aos meses seguintes e recolhido pelo "DAS Avulso" quando passar de R$ 10,00 (art. 44 da Resolução CGSN nº 140/2018).
- **Empresa em recuperação judicial**: segue apurando o Simples normalmente; débitos anteriores seguem o plano.

### 10. Quando escalar
- Estourou R$ 4,8 mi → `apuracao-lucro-presumido` + `analise-tributaria-regime`.
- DAS pago a maior por não ter separado ST ou monofásico nos últimos 5 anos → revisão do PGDAS-D e pedido de restituição pelo próprio aplicativo (o Tema 69 do STF não se aplica ao Simples).
- Intimação da Receita sobre o DAS → `resposta-fiscalizacao-intimacao`.
- MEI que estourou → `apuracao-mei`.
- Dúvida de DAS de meses passados → `revisao-fiscal-cruzamento-sped`.

## Erros comuns / pontos de atenção
- Usar a receita do mês, ou o acumulado do ano, como RBT12.
- Aplicar a alíquota nominal direto na receita.
- Misturar receita com ST ou monofásica com a receita normal.
- Esquecer o fator R em serviço intelectual, ou deixar pró-labore e FGTS fora da folha.
- Pôr advocacia ou contabilidade no fator R.
- Calcular o Anexo IV e esquecer o INSS patronal pago fora do DAS.
- Empresa nova: comparar meses parciais sem proporcionalizar.

## Perguntas que o usuário costuma fazer
- "Por que o DAS subiu se o faturamento do mês caiu?" Porque a alíquota depende da RBT12, que pode ter subido.
- "Quanto de folha preciso para ficar no Anexo III?" 28% da RBT12, com folha completa (inclui CPP e FGTS).
- "A LC 224/2025 mudou o Simples?" Não: a LC nº 224/2025 não alterou a LC nº 123/2006 nem as tabelas e partilhas dos Anexos.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre os formatos citados acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- LC nº 123/2006: art. 18 (cálculo, §§ 1º, 1º-A, 5º-B, 5º-D, 5º-I, 5º-J, 5º-K, 5º-M e 24), art. 19 e art. 20 (sublimites), art. 21, §4º (ISS retido), art. 30 (exclusão), art. 35 (multa de mora), art. 38-A (multa do PGDAS-D); Anexos I a V (redação da LC nº 155/2016).
- Lei nº 9.430/1996, art. 61 (multa de mora de 0,33% ao dia, limite de 20%).
- Resolução CGSN nº 140/2018: arts. 21 e 26 (RBT12 e fator R, inclusive de empresa nova), art. 44 (DAS abaixo de R$ 10,00), DEFIS anual.
- Portaria CGSN nº 54/2025 (sublimite de 2026).
- Resolução CGSN nº 186/2026, alterada pela Resolução CGSN nº 194/2026 (opção pelo regime regular de CBS/IBS e prazos para 2027).
- Perguntas e Respostas do Simples Nacional (CGSN, atualizado em 09/10/2026), perguntas 4.3, 5.3, 5.4, 5.7, 5.11 e 5.15.
- Emenda Constitucional nº 132/2023, LC nº 214/2025 e Ato Conjunto RFB/CGIBS nº 4/2026.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
