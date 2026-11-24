---
name: recuperacao-creditos-pis-cofins
description: "Levanta e calcula PIS/COFINS pagos a maior nos últimos 5 anos (retroativo), com atualização pela Selic, e prepara a retificação da EFD-Contribuições e o PER/DCOMP. Teses: exclusão do ICMS da base (Tema 69 do STF), exclusão do ISS da base (Tema 118 do STF, com checagem da publicação do acórdão), conceito de insumo (Tema 779 do STJ), monofásicos tributados na revenda (inclusive no Simples), receita financeira com alíquota errada, manutenção de créditos na exportação e crédito sobre estoque de abertura. NÃO usar para a apuração mensal corrente (usar a skill 'calculo-pis-cofins-nao-cumulativo'). Acionar quando o usuário disser \"recuperar PIS/COFINS\", \"crédito extemporâneo\", \"tese do século\", \"ICMS na base do PIS\", \"monofásico pago a maior\", \"revisão fiscal de PIS/COFINS\", \"PER/DCOMP de PIS/COFINS\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Recuperação retroativa de créditos de PIS/COFINS

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Identifica quais teses se aplicam ao cliente, calcula mês a mês o valor pago a maior nos períodos ainda não prescritos, atualiza pela Selic e organiza o caminho administrativo: retificar a EFD-Contribuições (e a DCTFWeb/DCTF quando necessário) e só então pedir restituição, ressarcimento ou compensação por PER/DCOMP. Aponta riscos e o que exige ação judicial.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.
> Tese que dependa de ação judicial é encaminhada a advogado com OAB.

> **Janela de 5 anos em novembro/2026.** O prazo para pedir de volta é de 5 anos contados de cada pagamento (art. 168, I, do CTN (Lei nº 5.172/1966) e art. 3º da LC nº 118/2005). O prazo corre da **data do pagamento**, não da competência: em novembro/2026, só pagamentos feitos a partir de **novembro/2021** ainda podem ser recuperados (conferir dia a dia pela data do DARF); a cada mês que passa, um mês se perde. Começar pelos pagamentos mais antigos.

## Quando usar
- Cliente do Lucro Real com vários anos de operação.
- Cliente do Lucro Presumido que incluiu o ICMS na base do PIS/COFINS.
- Cliente (inclusive do Simples) que revende produtos monofásicos e tributou essa receita.
- Trabalho de revisão fiscal ou due diligence.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Memórias de cálculo ficam na pasta do cliente, nunca em pasta temporária do sistema.

## Passo a passo (instruções para o agente de IA)

### 1. Teses
```
1. TEMA 69 DO STF — ICMS fora da base do PIS/COFINS
   - RE 574.706, julgado em 15/03/2017; embargos julgados em 2021
   - Exclui-se o ICMS DESTACADO na nota (não o recolhido), como fixado nos embargos de 2021
   - Modulação: efeitos a partir de 15/03/2017, ressalvadas as ações judiciais e os
     processos administrativos protocolados até essa data
   - Hoje a janela de 5 anos (desde 11/2021) já é toda posterior à modulação: a pergunta
     sobre ação antiga só importa para quem já tem processo
   - A Receita aplica a exclusão administrativamente (Parecer SEI nº 7.698/2021/ME)
   - Valor = ICMS destacado nas vendas × 9,25% (Real) ou × 3,65% (Presumido)
   - ATENÇÃO, lado do crédito: desde 01/05/2023 o ICMS também sai da base dos CRÉDITOS
     sobre compras (Lei nº 14.592/2023). Se a empresa tomou crédito cheio depois disso,
     o ajuste reduz o valor a recuperar
   - Não se aplica ao DAS do Simples Nacional (regime unificado da LC nº 123/2006)

2. TEMA 779 DO STJ — conceito de insumo
   - REsp 1.221.170/PR (2018): insumo é o que é essencial ou relevante à atividade
   - Parecer Normativo Cosit nº 5/2018 (como a Receita aplica)
   - Exemplos aceitos com frequência: combustível da frota usada na produção/prestação,
     EPI exigido por norma, manutenção de máquinas, frete na aquisição de insumos
   - Vale-transporte, vale-refeição e uniforme: crédito previsto em lei só para empresas de
     limpeza, conservação e manutenção (art. 3º, X, da Lei nº 10.637/2002 e da Lei nº 10.833/2003);
     fora disso é tese de risco
   - Só para o Lucro Real (não cumulativo)

3. MONOFÁSICOS tributados na revenda
   - Combustíveis (Lei nº 9.718/1998), medicamentos e perfumaria/cosméticos (Lei nº 10.147/2000),
     autopeças (Lei nº 10.485/2002), bebidas frias (Lei nº 13.097/2015)
   - Atacado/varejo: alíquota zero, porque a tributação se concentra no fabricante/importador
   - Quem pagou na revenda recupera os 5 anos
   - Simples Nacional: a receita de revenda de monofásicos deve ser segregada no PGDAS-D sem
     a parcela de PIS/COFINS (art. 18, § 4º-A, da LC nº 123/2006) — recuperável retificando o PGDAS-D
   - Meses a partir de 04/2026: a LC nº 224/2025 passou a tributar a 10% da alíquota padrão as
     operações antes isentas ou à alíquota zero que constam da lista de benefícios reduzidos
     (anexo da IN RFB nº 2.305/2025, substituído pela IN RFB nº 2.307/2026). Antes de calcular,
     conferir nesse anexo se a alíquota zero da revenda do produto do cliente está na lista:
     se estiver, a parcela de 10% é devida e não entra na recuperação; se não estiver, a
     revenda segue à alíquota zero e o pagamento é indevido por inteiro

4. EXPORTAÇÃO — manutenção e uso de créditos
   - Art. 6º da Lei nº 10.833/2003 e art. 5º da Lei nº 10.637/2002: o crédito vinculado à
     exportação pode ser descontado, compensado ou, ao fim de cada trimestre-calendário,
     ressarcido em dinheiro
   - Art. 17 da Lei nº 11.033/2004 e art. 16 da Lei nº 11.116/2005: manutenção e ressarcimento
     de créditos de vendas com suspensão, isenção ou alíquota zero

5. CRÉDITO PRESUMIDO sobre estoque de abertura (migração do Presumido para o Real)
   - Art. 11 da Lei nº 10.637/2002 (PIS 0,65%) e art. 12 da Lei nº 10.833/2003 (COFINS 3%)
     = 3,65% sobre o estoque de abertura, em 12 parcelas mensais
   - Migração com efeitos a partir de 04/2026: a LC nº 224/2025 limita créditos presumidos
     incluídos na lista de benefícios reduzidos a 90% do valor. Conferir no anexo da
     IN RFB nº 2.305/2025 (redação da IN RFB nº 2.307/2026) se este crédito consta da lista;
     se constar, calcular as parcelas a partir de 04/2026 com o limite de 90%

6. RECEITA FINANCEIRA — Decreto nº 8.426/2015
   - Lucro Real: PIS 0,65% e COFINS 4% (não as alíquotas cheias)
   - Quem aplicou 1,65% e 7,6% pagou a maior

7. TEMA 118 DO STF — ISS fora da base do PIS/COFINS
   - RE 592.616, julgado pelo Plenário em 21/10/2026: "o valor correspondente ao ISS não
     integra a base de cálculo" do PIS e da COFINS
   - Situação em 15/11/2026 (andamento do RE 592.616 no portal do STF): ata de julgamento
     publicada em 23/10/2026; o ACÓRDÃO AINDA NÃO FOI PUBLICADO; a modulação de efeitos não
     foi decidida no julgamento e pode vir em embargos de declaração
   - Regra de uso: toda vez que usar esta tese, consultar o andamento do RE 592.616 no portal
     do STF. Se o acórdão não tiver sido publicado, informar ao usuário: "o acórdão do Tema 118
     do STF ainda não foi publicado". Se já tiver sido, conferir a modulação antes de calcular
   - Enquanto não houver acórdão, modulação definida e orientação da Receita, a recuperação
     é de risco pela via administrativa: levar o caso ao advogado com OAB antes de compensar
   - Estimativa = ISS incidente sobre as receitas de serviço × 9,25% (Real) ou × 3,65%
     (Presumido); o critério exato do valor a excluir depende do acórdão
```

### 2. Entrevista mínima
```
P1: Regime atual e dos últimos 5 anos? Receita anual?
P2: Já existe ação judicial ou processo administrativo sobre alguma tese? Situação e data?
P3: Vende produtos monofásicos? Exporta? Tem receita financeira?
P4: Já exclui o ICMS da base hoje? Desde quando?
P5: Posso ler a EFD-Contribuições e a EFD ICMS/IPI dos meses desde 11/2021?
P6: A empresa tem débitos em aberto? (restituição e ressarcimento passam por compensação de ofício)
```

### 3. Cálculo (Python)
Salvar como `.py` e rodar com `python -I -X utf8 arquivo.py`. Selic acumulada real deve vir da tabela oficial da Receita.

```python
# Tema 69 — valor mensal pago a maior. Valores fictícios.
def credito_tema69(icms_destacado_vendas, regime="real", icms_em_creditos_pos_05_2023=0.0):
    aliq = 0.0925 if regime == "real" else 0.0365
    bruto = icms_destacado_vendas * aliq
    # Desde 05/2023, crédito sobre compras sem ICMS (Lei 14.592/2023):
    # se a empresa tomou crédito com ICMS dentro, descontar o excesso.
    ajuste = icms_em_creditos_pos_05_2023 * aliq if regime == "real" else 0.0
    return bruto - ajuste

def atualizar(valor, selic_acumulada):
    # Selic acumulada do mês seguinte ao pagamento até o mês anterior ao pedido,
    # + 1% no mês do pedido/compensação (art. 39, § 4º, da Lei nº 9.250/1995).
    return valor * (1 + selic_acumulada + 0.01)

meses = [("11/2021", 40_000, 0.0, 0.55), ("06/2023", 40_000, 15_000, 0.30)]  # (comp., ICMS vendas, ICMS em créditos, Selic acum.)
total = 0
for comp, icms_v, icms_c, selic in meses:
    c = credito_tema69(icms_v, "real", icms_c)
    total += atualizar(c, selic)
    print(comp, round(c, 2), round(atualizar(c, selic), 2))
print("Total atualizado:", round(total, 2))
```

### 4. Sequência operacional
1. **Análise preliminar**: teses aplicáveis e estimativa do valor.
2. **Levantamento mês a mês** desde 11/2021: EFD-Contribuições + EFD ICMS/IPI + documentos.
3. **Memória de cálculo** mensal com Selic.
4. **Retificar a EFD-Contribuições** (blocos M e F; e, até 12/2024, a DCTF; a partir de 01/2025, a DCTFWeb/MIT — IN RFB nº 2.237/2024). Sem retificação, o crédito não "existe" para a Receita.
5. **PER/DCOMP** no e-CAC: restituição, ressarcimento ou compensação (IN RFB nº 2.055/2021).
6. **Crédito reconhecido em ação judicial**: exige **habilitação prévia** do crédito antes da primeira compensação, qualquer que seja o valor (IN RFB nº 2.055/2021). Acima de R$ 10 milhões, há limite mensal de compensação, nunca menor que 1/60 do crédito, e a 1ª declaração deve ser feita em até 5 anos do trânsito em julgado (art. 74-A da Lei nº 9.430/1996, incluído pela Lei nº 14.873/2024; limites na Portaria Normativa MF nº 14/2024).
7. **Acompanhar** os despachos decisórios.
8. **Despacho desfavorável**: manifestação de inconformidade em 30 dias (art. 74, § 9º, da Lei nº 9.430/1996).

### 5. Entregáveis
**a) Memória mensal** (planilha na pasta do cliente)
```
competencia,icms_destacado,credito_pis,credito_cofins,total,selic_acum,total_atualizado
11/2021,40000,660,3040,3700,0.55,____
...
TOTAL,,,,____,,____
```
**b) Pacote ao cliente**
```
CLIENTE EXEMPLO — período: 11/2021 a ____

TESES IDENTIFICADAS
[ ] Tema 69 do STF — ICMS na base (com ajuste da Lei 14.592/2023 desde 05/2023)
[ ] Tema 118 do STF — ISS na base (conferir publicação do acórdão e modulação; via advogado)
[ ] Tema 779 do STJ — insumos
[ ] Receita financeira (Decreto 8.426/2015)
[ ] Monofásicos tributados na revenda (inclusive PGDAS-D no Simples)
[ ] Manutenção de créditos na exportação
[ ] Crédito sobre estoque de abertura

VALOR ESTIMADO: R$ ____    ATUALIZADO PELA SELIC: R$ ____

PROPOSTA
- Honorários: R$ ____ (fixo) ou ___% do valor efetivamente aproveitado
- Prazo: retificações em 60 a 180 dias; aproveitamento em 6 a 24 meses
- Riscos: glosa; compensação "não declarada" tem multa isolada de 75% (art. 18 da Lei nº 10.833/2003)
```
**c) EFD-Contribuições retificadora** (blocos M e F ajustados).
**d) Orientação do PER/DCOMP** no e-CAC.
**e) Plano de acompanhamento** mensal dos despachos.

## Erros comuns / pontos de atenção
- Compensar antes de retificar a EFD-Contribuições (e a DCTF/DCTFWeb): glosa quase certa.
- Não atualizar pela Selic.
- Calcular o Tema 69 depois de 05/2023 sem ajustar os créditos (Lei nº 14.592/2023).
- Usar tese sem precedente vinculante em compensação administrativa: risco de compensação não homologada e, se for "não declarada" (por exemplo, crédito de decisão judicial não transitada), multa isolada de 75%.
- Compensar com tributo de outro ente (estadual/municipal): vedado.
- Achar que precisa de certidão negativa para compensar: não precisa; mas na restituição e no ressarcimento a Receita faz **compensação de ofício** com débitos em aberto.
- Deixar meses prescreverem enquanto o levantamento não termina.
- **Multa por compensação não homologada**: a multa isolada de 50% (art. 74, § 17, da Lei nº 9.430/1996) foi declarada inconstitucional (STF, Tema 736). Não usar mais como risco.

**Casos de borda**
- **Cliente com ação ajuizada antes de 15/03/2017**: pode ter direito a períodos anteriores à modulação, conforme a decisão transitada; usar o título judicial (habilitação prévia).
- **Cliente do Simples**: Tema 69 não se aplica ao DAS; a tese útil é a dos monofásicos no PGDAS-D.
- **Cliente em recuperação judicial**: créditos reconhecidos podem ajudar no equacionamento de débitos, observadas as regras da transação (Lei nº 10.522/2002).
- **Exportadora com saldo credor crônico**: pedido de ressarcimento trimestral recorrente.
- **Reforma Tributária**: PIS/COFINS deixam de existir em 2027 (CBS). Os créditos de PIS/COFINS, inclusive presumidos, não apropriados ou não utilizados até a extinção continuam válidos e podem compensar débitos da CBS ou ser ressarcidos/compensados com outros tributos federais, cumpridas as condições da legislação na data da extinção e as regras de ressarcimento e compensação na data do pedido (art. 378 da LC nº 214/2025). Segundo a Receita Federal, o PER/DCOMP Web vai recuperar os saldos informados na EFD-Contribuições de dezembro/2026: por isso, as retificações da recuperação devem estar transmitidas e coerentes até essa escrituração.

## Perguntas que o usuário costuma fazer
- **"Ainda dá tempo de recuperar o ICMS da base desde 2017?"** Não pela via administrativa: só os últimos 5 anos (hoje, desde 11/2021).
- **"Preciso entrar na Justiça?"** Para o Tema 69, não (a Receita aplica). Para teses sem precedente vinculante, ou com precedente ainda sem acórdão publicado e sem modulação definida (caso do Tema 118 em 15/11/2026), sim — com advogado.
- **"O cliente do Simples tem algo a recuperar?"** Muitas vezes sim, nos monofásicos segregados de forma errada no PGDAS-D.

## Formato de entrega
- Cálculos, apurações e conciliações: sempre planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): sempre documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei nº 5.172/1966 (CTN) — art. 168, I (prazo de 5 anos); LC nº 118/2005 — art. 3º.
- Lei nº 9.430/1996 — art. 74 (compensação; § 9º manifestação de inconformidade) e art. 74-A (limite para crédito judicial, incluído pela Lei nº 14.873/2024).
- Lei nº 9.250/1995 — art. 39, § 4º (Selic na restituição/compensação).
- Lei nº 10.637/2002 — arts. 3º, 5º e 11; Lei nº 10.833/2003 — arts. 3º, 6º, 12 e 18.
- Lei nº 14.592/2023 — ICMS fora da base dos créditos (desde 01/05/2023).
- Lei nº 11.033/2004 — art. 17; Lei nº 11.116/2005 — art. 16 (manutenção e ressarcimento de créditos).
- Leis nº 9.718/1998, 10.147/2000, 10.485/2002 e 13.097/2015 — regimes monofásicos.
- LC nº 123/2006 — art. 18, § 4º-A (segregação de receitas no Simples).
- Decreto nº 8.426/2015 — alíquotas sobre receitas financeiras.
- STF, RE 574.706 (Tema 69); STF, RE 592.616 (Tema 118 — julgado em 21/10/2026, acórdão não publicado até 15/11/2026); STJ, REsp 1.221.170/PR (Tema 779); STF, RE 796.939 (Tema 736).
- Parecer SEI nº 7.698/2021/ME; Parecer Normativo Cosit nº 5/2018.
- IN RFB nº 2.055/2021 (restituição, ressarcimento, compensação e habilitação de crédito judicial); IN RFB nº 2.121/2022 (PIS/COFINS); IN RFB nº 2.237/2024 (DCTFWeb/MIT).
- Portaria Normativa MF nº 14/2024 — limites mensais de compensação de crédito judicial.
- LC nº 224/2025 e IN RFB nº 2.305/2025 (anexo substituído pela IN RFB nº 2.307/2026) — redução de 10% dos benefícios federais a partir de 04/2026 para PIS/COFINS.
- LC nº 214/2025 — art. 378 (créditos de PIS/COFINS na transição para a CBS).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
