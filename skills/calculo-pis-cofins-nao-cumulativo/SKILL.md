---
name: calculo-pis-cofins-nao-cumulativo
description: "Apuração mensal de PIS (1,65%) e COFINS (7,6%) no regime não cumulativo (Lucro Real), com débitos × créditos, conceito de insumo do STJ (REsp 1.221.170, Temas 779 e 780: essencialidade ou relevância), exclusão do ICMS da base dos débitos (Tema 69) e dos créditos (Lei nº 14.592/2023), receita financeira (Decreto nº 8.426/2015), exportação com manutenção de créditos, crédito sobre estoque de abertura, LC nº 224/2025 e DARFs 6912 e 5856. Acionar quando o usuário disser \"PIS e COFINS do Lucro Real\", \"não cumulativo\", \"9,25%\", \"crédito de insumo\", \"Tema 779\", \"crédito de energia/aluguel/depreciação\", \"frete na venda\", \"EPI\", \"saldo credor de PIS/COFINS\", \"ressarcimento\", \"receita financeira 0,65% e 4%\", \"DARF 6912 ou 5856\". Não usar para recuperar períodos passados (usar recuperacao-creditos-pis-cofins). Entrega: apuração do mês, análise de créditos por categoria, saldo credor e checklist."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Apuração de PIS/COFINS não cumulativo

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Apura o PIS e a COFINS do mês corrente no Lucro Real: calcula os débitos sobre as receitas, identifica e classifica os créditos permitidos (insumos, energia, aluguéis, depreciação, fretes etc.), separa PIS e COFINS (cada um com seu saldo credor) e indica os DARFs. Documenta o fundamento de cada crédito para uma eventual fiscalização.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Reforma Tributária.** 2026 é ano-teste: CBS 0,9% e IBS 0,1% destacados e compensáveis integralmente com o PIS/COFINS devido, sem recolhimento para quem cumpre as obrigações acessórias (Emenda Constitucional nº 132/2023; Lei Complementar nº 214/2025). **A partir de 2027 o PIS e a COFINS são extintos e substituídos pela CBS**; os saldos credores seguem as regras de transição da LC nº 214/2025. Use a skill `reforma-tributaria-transicao`.

> **LC nº 224/2025.** Desde 01/04/2026 operações antes isentas ou com alíquota zero passam a 10% da alíquota do sistema padrão (art. 4º, §4º, I, da LC nº 224/2025); no não cumulativo, **PIS 0,165% + COFINS 0,76%** (art. 4º, §3º, III). Créditos presumidos e fictícios têm aproveitamento limitado a 90% do valor original, e o excedente é cancelado (art. 4º, §4º, IV); créditos regulares por entradas tributadas não são afetados. Conferir também a IN RFB nº 2.305/2025 e a Nota Técnica EFD-Contribuições nº 12/2026 (registros de ajuste M110/M115, M220/M225, M510/M515, M620/M625).

## Quando usar
- Empresa no Lucro Real (regra geral do não cumulativo).
- Conferência de EFD-Contribuições (Bloco M), DARFs e saldo credor.
- Análise de quais gastos geram crédito.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
1. CNPJ (pode ser de exemplo), competência e receitas segregadas: vendas, serviços, financeiras, locação, exportação, monofásicas, receitas do art. 10 da Lei nº 10.833/2003 (que ficam no cumulativo).
2. ICMS destacado nas saídas (Tema 69).
3. Notas de entrada com CST de crédito (50 a 56) — consultar XML se houver.
4. Gastos: energia, aluguel pago a PJ, arrendamento mercantil, depreciação, fretes, EPI, uniforme, vale-transporte, manutenção, software.
5. Saldo credor anterior **de PIS e de COFINS separadamente**; houve migração recente do Presumido para o Real?

### 2. Parâmetros
```
ALÍQUOTAS
PIS 1,65% | COFINS 7,60% (total 9,25%)
Receitas financeiras: PIS 0,65% | COFINS 4% (art. 1º do Decreto nº 8.426/2015)
  JCP recebido: PIS 1,65% | COFINS 7,6% (art. 1º, § 2º)
  Alíquota zero mantida para variações monetárias em função da taxa de câmbio de
  operações de exportação de bens e serviços e de obrigações contraídas pela pessoa
  jurídica, inclusive empréstimos e financiamentos (art. 1º, § 3º, I e II).
Operações antes isentas/alíquota zero, desde 01/04/2026: PIS 0,165% + COFINS 0,76% (LC nº 224/2025)

DARF E PRAZO
PIS não cumulativo: 6912 | COFINS não cumulativo: 5856
(8109 e 2172 são os códigos do cumulativo — usar só para receitas do art. 10 da Lei nº 10.833/2003)
Vencimento: dia 25 do mês seguinte, antecipando se não for dia útil (art. 10 da
  Lei nº 10.637/2002 e art. 11 da Lei nº 10.833/2003, redação da Lei nº 11.933/2009)
DCTFWeb (MIT): último dia útil do mês seguinte (IN RFB nº 2.248/2025)
EFD-Contribuições: até o 10º dia útil do 2º mês seguinte

EXCLUSÕES DA BASE DOS DÉBITOS
ICMS destacado (STF, Tema 69); vendas canceladas e descontos incondicionais;
IPI e ICMS-ST destacados (não compõem a receita bruta);
ISS — STF, Tema 118 (RE 592.616), julgado em 21/10/2026: antes de excluir,
verificar no portal do STF se o acórdão já foi publicado e se houve
modulação; se não foi publicado, avisar o usuário: "o acórdão do Tema 118
do STF ainda não foi publicado".
```

### 3. Cálculo (Python, para mostrar a memória)
```python
# PIS/COFINS não cumulativo — débitos x créditos, com saldo credor SEPARADO por tributo
def pis_cofins_nc(receita_tributavel, exclusoes, base_creditos, rec_financeira=0,
                  saldo_pis_anterior=0, saldo_cofins_anterior=0):
    base_debito = receita_tributavel - exclusoes          # exclusões: ICMS destacado, cancelamentos...
    pis_db = base_debito * 0.0165 + rec_financeira * 0.0065
    cof_db = base_debito * 0.076 + rec_financeira * 0.04
    pis_cr = base_creditos * 0.0165                       # base de crédito já SEM o ICMS da compra
    cof_cr = base_creditos * 0.076
    pis_saldo = pis_db - pis_cr - saldo_pis_anterior
    cof_saldo = cof_db - cof_cr - saldo_cofins_anterior
    return {
        'pis_debito': round(pis_db, 2), 'pis_credito': round(pis_cr, 2),
        'cofins_debito': round(cof_db, 2), 'cofins_credito': round(cof_cr, 2),
        'pis_a_recolher_6912': round(max(0, pis_saldo), 2),
        'cofins_a_recolher_5856': round(max(0, cof_saldo), 2),
        'saldo_credor_pis': round(max(0, -pis_saldo), 2),
        'saldo_credor_cofins': round(max(0, -cof_saldo), 2),
    }

print(pis_cofins_nc(2_000_000, exclusoes=240_000, base_creditos=940_000))
# PIS: 29.040,00 - 15.510,00 = 13.530,00 | COFINS: 133.760,00 - 71.440,00 = 62.320,00
```

### 4. Créditos (art. 3º das Leis nº 10.637/2002 e nº 10.833/2003)
**Conceito de insumo** — STJ, REsp 1.221.170/PR (Temas 779 e 780, relator Min. Napoleão Nunes Maia Filho, julgado em 22/02/2018): é insumo o bem ou serviço **essencial ou relevante** para a produção ou a prestação do serviço. A RFB aplica o entendimento pelo Parecer Normativo Cosit/RFB nº 5/2018. Não basta "incorporar ao produto", e também não vale "toda despesa".

**Créditos previstos em lei**
- Bens para revenda (exceto monofásicos e substituição tributária).
- Insumos: matéria-prima, produto intermediário, embalagem e serviços aplicados na produção.
- Energia elétrica e térmica consumida nos estabelecimentos.
- Aluguéis de prédios, máquinas e equipamentos pagos a PJ.
- Contraprestações de arrendamento mercantil pagas a PJ (exceto se a arrendadora for optante do Simples) — art. 3º, V.
- Depreciação de máquinas, equipamentos e outros bens do imobilizado usados na produção, com três opções: (a) pelos encargos de depreciação; (b) em 48 meses (art. 3º, § 14, da Lei nº 10.833/2003); (c) **crédito integral no mês da aquisição** para máquinas e equipamentos novos destinados à produção (art. 1º da Lei nº 11.774/2008, com redação da Lei nº 12.546/2011).
- Edificações e benfeitorias: pela depreciação ou em 24 meses (art. 6º da Lei nº 11.488/2007).
- Frete e armazenagem na operação de venda, quando pagos pelo vendedor (art. 3º, IX).
- Vale-transporte, vale-refeição e uniforme: crédito expresso só para empresas de limpeza, conservação e manutenção (art. 3º, X); para as demais, discutir pelo conceito de insumo.
- Importação: PIS-Importação 2,1% e COFINS-Importação 9,65% (regra geral) geram crédito (art. 15 da Lei nº 10.865/2004).

**Créditos pelo conceito de insumo (defensáveis, documentar)**
- EPI exigido por norma regulamentadora (aceito pelo PN Cosit nº 5/2018).
- Manutenção de máquinas da produção; combustível e lubrificante de frota da atividade-fim.
- Treinamento técnico obrigatório; software essencial à produção.
- **Frete de produto acabado entre estabelecimentos da mesma empresa**: **não gera crédito** (Súmula CARF nº 217, vigente desde 04/10/2024, alinhada ao STJ); o mesmo vale para fretes entre estabelecimentos para formar lotes de exportação. Tomar esse crédito é risco alto de glosa. Não confundir com o frete na aquisição de insumos (Súmula CARF nº 188) nem com o frete na venda (art. 3º, IX).

**Vedados**
- Mão de obra paga a pessoa física (art. 3º, § 2º, I).
- Bens ou serviços não sujeitos ao pagamento da contribuição, inclusive isentos revendidos ou usados em produtos com alíquota zero, isentos ou não alcançados (art. 3º, § 2º, II).
- Bens adquiridos para revenda sujeitos à tributação monofásica (STJ, Tema 1.093).
- ICMS da aquisição: fica fora da base do crédito desde maio/2023 (art. 3º, § 2º, III, incluído pela Lei nº 14.592/2023; constitucionalidade discutida).
- Aquisições que passaram a ser tributadas a 10% da alíquota pela LC nº 224/2025: antes de tomar crédito sobre elas, conferir a regra da IN RFB nº 2.305/2025 e da Nota Técnica EFD-Contribuições nº 12/2026 para o CST da entrada, e documentar o fundamento (o tema é discutido e pode ser glosado).

**Compras de fornecedor do Simples Nacional: DÃO crédito** pela alíquota cheia (1,65% e 7,6%), desde que o bem ou serviço seja insumo ou revenda (Ato Declaratório Interpretativo SRF nº 15/2007).

### 5. Exportação e saldo credor
- Receita de exportação é isenta, com **manutenção dos créditos** vinculados (art. 6º da Lei nº 10.833/2003 e art. 5º da Lei nº 10.637/2002).
- Saldo credor vinculado à exportação: compensação com outros tributos ou ressarcimento em dinheiro, pedidos por trimestre via PER/DCOMP. A RFB tem até 360 dias para decidir (art. 24 da Lei nº 11.457/2007).

### 6. Crédito sobre estoque de abertura
Empresa que passa do Presumido para o Real tem crédito presumido sobre o estoque de abertura (bens para revenda e insumos adquiridos de PJ): PIS 0,65% e COFINS 3%, em 12 parcelas mensais iguais (art. 11 da Lei nº 10.637/2002 e art. 12 da Lei nº 10.833/2003). Verificar se houve migração. A lei chama esse crédito de "crédito presumido"; antes de lançar, conferir se ele consta da lista de créditos presumidos de PIS/COFINS reduzidos pelo art. 4º, §2º, II, "d", da LC nº 224/2025 e pela IN RFB nº 2.305/2025 — se constar, o aproveitamento fica limitado a 90%.

### 7. Entregável
**a) Apuração**
```
PIS/COFINS NÃO CUMULATIVO — MM/2026 — EMPRESA EXEMPLO S.A. — CNPJ 00.000.000/0001-00

DÉBITOS
Receita bruta tributável ................ 2.000.000,00
(−) ICMS destacado (Tema 69) ............... 240.000,00
(−) Vendas canceladas / exportação / alíq. zero .. 0,00
(=) Base débito ......................... 1.760.000,00
PIS (1,65%) .................................. 29.040,00
COFINS (7,60%) .............................. 133.760,00
(+ receita financeira: PIS 0,65% / COFINS 4%)

CRÉDITOS (bases sem o ICMS da compra)
Insumos / matéria-prima (CST 50) ............ 800.000,00
Energia elétrica ............................. 30.000,00
Aluguel pago a PJ ............................ 20.000,00
Depreciação do mês (máquinas da produção) .... 50.000,00
Frete na venda ............................... 25.000,00
EPI / treinamento (conceito de insumo) ....... 15.000,00
Base de crédito ............................. 940.000,00
PIS crédito .................................. 15.510,00
COFINS crédito ............................... 71.440,00

PIS a recolher (DARF 6912) ................... 13.530,00
COFINS a recolher (DARF 5856) ................ 62.320,00
Vencimento: 25/MM+1 (antecipar se não for dia útil)
```
**b) Análise de créditos** por categoria, com o fundamento legal ou jurisprudencial e o nível de risco (baixo, médio, alto).
**c) Planilha** de memória (ver "Formato de entrega").
**d) Saldo credor** (se houver), separado por PIS e COFINS, e orientação para PER/DCOMP.
**e) Checklist**
```
[ ] Receitas conferidas com EFD-Contribuições e notas
[ ] ICMS destacado excluído dos débitos (Tema 69) e ICMS da compra fora dos créditos
[ ] Créditos classificados (insumo, energia, aluguel, depreciação, frete) com fundamento
[ ] Créditos pelo conceito de insumo documentados (laudo/parecer)
[ ] LC nº 224/2025 aplicada às receitas que eram isentas/alíquota zero
[ ] Crédito de estoque de abertura (se houve migração)
[ ] Créditos da exportação mantidos
[ ] Saldo credor anterior de PIS e de COFINS usado em separado
[ ] EFD-Contribuições (Bloco M e F600) e DCTFWeb conferidas
```

## Erros comuns / pontos de atenção
- Somar o saldo credor de PIS e COFINS ou usar o mesmo saldo nos dois tributos.
- Deixar de tomar crédito legítimo (energia, aluguel PJ, depreciação, frete na venda).
- Negar crédito de compras de fornecedor do Simples (é permitido).
- Tomar crédito de produto monofásico para revenda.
- Incluir o ICMS da compra na base do crédito (vedado desde maio/2023).
- Achar que a depreciação só pode ser 1/12 ou 1/48: máquinas novas da produção admitem crédito integral no mês.
- Tratar receita financeira como alíquota zero, ou esquecer que variação cambial de exportação continua com alíquota zero.
- Usar os códigos 8109/2172 (cumulativo) no lugar de 6912/5856.
- Receitas do art. 10 da Lei nº 10.833/2003 (hospitais, transporte coletivo, telecomunicações etc.) ficam no cumulativo mesmo no Lucro Real.

### Casos de borda
- **Importador**: PIS/COFINS-Importação na entrada, com crédito.
- **Exportador com saldo credor crônico**: ressarcimento por trimestre; prazo de análise de até 360 dias.
- **Recuperação judicial**: parcelamento especial de débitos federais em até 120 meses (art. 10-A da Lei nº 10.522/2002, redação da Lei nº 14.112/2020).
- **Compras de mercadoria produzida na ZFM** (pessoa jurídica com projeto aprovado pela SUFRAMA): **dão crédito**, mas por alíquotas próprias — PIS 1% (art. 3º, § 12, da Lei nº 10.637/2002) e COFINS 4,6% nos casos gerais (art. 3º, § 17, da Lei nº 10.833/2003); há alíquotas diferentes para hipóteses específicas dos mesmos parágrafos (por exemplo, COFINS 5,6% e 7,6%). Conferir o enquadramento do produto.
- **Software adquirido**: crédito defensável se essencial à produção.

### Quando escalar
- Períodos passados (5 anos) → `recuperacao-creditos-pis-cofins`.
- Cruzamento EFD-Contribuições × DCTFWeb × ECF → `revisao-fiscal-cruzamento-sped`.
- Comparar com o Presumido → `analise-tributaria-regime`.
- Autuação → `resposta-fiscalizacao-intimacao`.

## Perguntas que o usuário costuma fazer
- **"Comprei de empresa do Simples, tenho crédito?"** Sim, pela alíquota cheia, se for insumo ou revenda.
- **"EPI dá crédito?"** Sim, quando exigido por norma (a RFB aceita pelo PN Cosit nº 5/2018). Guarde a comprovação.
- **"Posso tomar crédito da máquina de uma vez?"** Se for máquina nova destinada à produção, sim, no mês da aquisição.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas a fisco): documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei nº 10.637/2002 (PIS) — arts. 1º a 3º (inclusive § 12, ZFM), 5º, 10 (prazo) e 11.
- Lei nº 10.833/2003 (COFINS) — arts. 1º a 3º (créditos, incisos e §§ 2º, 14 e 17), 6º, 10, 11 (prazo) e 12.
- Lei nº 14.592/2023 — ICMS fora da base dos créditos (art. 3º, § 2º, III, das Leis nº 10.637 e nº 10.833).
- Lei nº 11.774/2008, art. 1º (redação da Lei nº 12.546/2011) — crédito imediato de máquinas.
- Lei nº 11.488/2007, art. 6º — edificações em 24 meses.
- Lei nº 10.865/2004, art. 15 — crédito na importação.
- Decreto nº 8.426/2015 — alíquotas sobre receitas financeiras.
- Lei nº 11.457/2007, art. 24 — prazo de 360 dias.
- Lei nº 10.522/2002, art. 10-A — parcelamento na recuperação judicial.
- Lei nº 11.933/2009 — prazo do dia 25; IN RFB nº 2.248/2025 — DCTFWeb; IN RFB nº 2.121/2022 — consolidação.
- STJ, REsp 1.221.170/PR (Temas 779 e 780); STJ, Tema 1.093 (monofásicos); STF, RE 574.706 (Tema 69); STF, RE 592.616 (Tema 118 — ISS).
- Súmulas CARF nº 188 e nº 217 (fretes).
- Parecer Normativo Cosit/RFB nº 5/2018; Ato Declaratório Interpretativo SRF nº 15/2007.
- LC nº 224/2025, art. 4º (§§ 2º, II, "d"; 3º, III; 4º, I e IV), IN RFB nº 2.305/2025 e Nota Técnica EFD-Contribuições nº 12/2026; EC nº 132/2023 e LC nº 214/2025.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
