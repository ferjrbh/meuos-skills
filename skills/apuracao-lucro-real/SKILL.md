---
name: apuracao-lucro-real
description: "Apura IRPJ e CSLL no Lucro Real, trimestral ou anual com estimativa mensal, partindo do lucro contábil antes dos tributos (LAIR), fazendo adições e exclusões na Parte A do LALUR/LACS, compensando prejuízo fiscal e base negativa com a trava de 30% e gerando os DARFs. Use quando a empresa for obrigada ao Real (receita acima de R$ 78 mi, instituição financeira, factoring, lucros do exterior, benefício fiscal) ou optante, ou quando o usuário disser \"lucro real\", \"LALUR\", \"LACS\", \"prejuízo fiscal\", \"Parte B\", \"balancete de suspensão\", \"estimativa mensal\", \"JCP\", \"equivalência patrimonial\". Não use para Presumido nem Simples, nem para preencher ou transmitir a ECF (use 'ecf-escrituracao-contabil-fiscal'): esta skill apura o tributo."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Apuração do Lucro Real (IRPJ e CSLL)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Parte do lucro contábil antes do IRPJ e da CSLL (LAIR), soma as despesas que a lei não aceita (adições), tira as receitas que a lei não tributa (exclusões), compensa prejuízos de anos anteriores até o limite de 30% e calcula IRPJ (15% + adicional de 10%) e CSLL (9%). Entrega a Parte A do LALUR (livro de apuração do IRPJ) e do LACS (livro da CSLL), a Parte B atualizada, os DARFs e um checklist.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Fechamento trimestral do Lucro Real ou estimativa mensal do Real anual.
- Balancete de suspensão ou redução da estimativa.
- Controle de prejuízo fiscal e base negativa da CSLL.
- Cálculo de JCP (juros sobre capital próprio) dedutível.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Isso vale para remuneração de sócios e diretores que aparecer no razão.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Sem balancete fechado não há Lucro Real: se faltar, peça o fechamento primeiro (`fechamento-mensal`).

## Passo a passo (instruções para o agente de IA)

### 1. Tabelas de referência (2026)
```
ALÍQUOTAS
IRPJ: 15% sobre o lucro real
Adicional: 10% sobre o que exceder R$ 20.000 × meses do período
           (R$ 60.000 no trimestre; R$ 240.000 no ano)
CSLL: 9% para empresas em geral.
      Instituições financeiras, seguradoras e equiparadas têm alíquotas
      próprias no art. 3º da Lei nº 7.689/1988, alterado pelo art. 7º da
      LC nº 224/2025 com efeitos desde 01/04/2026: por exemplo,
      instituições de pagamento e entidades do inciso II-B, 12% até
      31/12/2027 e 15% a partir de 01/01/2028; entidades do inciso II-C e
      empresas de capitalização, 17,5% até 31/12/2027 e 20% a partir de
      01/01/2028. Conferir o inciso aplicável ao tipo de entidade.

FORMAS DE APURAÇÃO
Trimestral: definitiva a cada trimestre (31/03, 30/06, 30/09, 31/12).
Anual: estimativa mensal (receita × percentual do Presumido) com
       balancete de suspensão/redução e ajuste em 31/12. A opção pelo
       anual se faz com o pagamento da estimativa de janeiro e vale
       para o ano todo (art. 3º da Lei nº 9.430/1996).

CÓDIGOS DE DARF
IRPJ (PJ obrigada ao Lucro Real): estimativa mensal 2362 · trimestral 0220 · ajuste anual 2430
IRPJ (PJ optante, não obrigada): estimativa mensal 5993 · trimestral 3373 · ajuste anual 2456
CSLL: estimativa mensal 2484 · trimestral 6012 · ajuste anual 6773
NÃO usar 2469 para CSLL de empresa comum (é de entidade financeira).
NÃO usar 2089/2372 (são do Lucro Presumido).

PRAZOS
Trimestral: último dia útil do mês seguinte ao trimestre (até 3 quotas,
            mínimo R$ 1.000 cada; Selic + 1% a partir da 2ª).
Estimativa mensal: último dia útil do mês seguinte.
Ajuste anual: último dia útil de março do ano seguinte.
ECF: último dia útil de julho do ano seguinte.
DCTFWeb: último dia útil do mês seguinte (IN RFB nº 2.248/2025).
```

### 2. Entrevista mínima
```
P1: "CNPJ + período + forma (Real trimestral ou anual com estimativa)?"
P2: "Balancete fechado do período? Qual o LAIR (lucro antes de IRPJ/CSLL)?"
P3: "Saldo de prejuízo fiscal (IRPJ) e de base negativa (CSLL) na Parte B, por ano de origem?"
P4: "ECD do ano anterior e plano de contas referencial?"
P5: "Houve multas, provisões, brindes, doações, JCP, equivalência patrimonial, dividendos recebidos, subvenções, operações com o exterior?"
P6: "A empresa tem benefício fiscal (SUDAM, SUDENE, PAT, Lei do Bem etc.)?" (corte de 10% da LC nº 224/2025)
```

### 3. Cálculo (rodar em Python, nunca de cabeça)
```python
# Lucro Real — IRPJ e CSLL com trava de 30% separada para cada tributo.
def lucro_real(lair, adicoes_irpj, exclusoes_irpj, prejuizo_fiscal,
               adicoes_csll, exclusoes_csll, base_negativa_csll,
               periodicidade="trimestral"):
    # IRPJ (LALUR)
    ajustado_irpj = lair + adicoes_irpj - exclusoes_irpj
    comp_pf = min(prejuizo_fiscal, max(0.0, ajustado_irpj) * 0.30)   # trava de 30%
    lucro_real = ajustado_irpj - comp_pf
    teto = 60_000 if periodicidade == "trimestral" else 240_000
    irpj = max(0.0, lucro_real) * 0.15
    adicional = max(0.0, lucro_real - teto) * 0.10
    # CSLL (LACS) — livro e saldo próprios, não se misturam com o IRPJ
    ajustado_csll = lair + adicoes_csll - exclusoes_csll
    comp_bn = min(base_negativa_csll, max(0.0, ajustado_csll) * 0.30)
    base_csll = ajustado_csll - comp_bn
    csll = max(0.0, base_csll) * 0.09
    return {
        "Lucro ajustado IRPJ": ajustado_irpj, "Prejuízo compensado": comp_pf,
        "Prejuízo remanescente (Parte B)": prejuizo_fiscal - comp_pf,
        "Lucro real": lucro_real, "IRPJ 15%": irpj, "Adicional 10%": adicional,
        "IRPJ total": irpj + adicional,
        "Base CSLL ajustada": ajustado_csll, "Base negativa compensada": comp_bn,
        "Base negativa remanescente (Parte B)": base_negativa_csll - comp_bn,
        "CSLL 9%": csll,
    }

# Exemplo: LAIR 500.000; adições 50.000; exclusões 40.000;
# prejuízo fiscal 300.000; mesmos ajustes e saldo para a CSLL
r = lucro_real(500_000, 50_000, 40_000, 300_000, 50_000, 40_000, 300_000)
for k, v in r.items():
    print(f"{k:40} R$ {v:>14,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
# Esperado: lucro real 357.000; IRPJ total 83.250 (DARF 0220); CSLL 32.130 (DARF 6012)
```

### 4. Adições — Parte A (despesas contabilizadas que a lei não aceita)
```
- IRPJ e CSLL provisionados .......................... art. 1º da Lei nº 9.316/1996
- Provisões não dedutíveis (exceto férias, 13º e as
  autorizadas em lei) ................................ art. 13, I, da Lei nº 9.249/1995
- Multas por infração fiscal punitivas (as
  compensatórias/de mora são dedutíveis) ............. art. 41, §5º, da Lei nº 8.981/1995
- Brindes ............................................ art. 13, VII, da Lei nº 9.249/1995
- Doações fora das hipóteses e limites legais ........ art. 13, VI e §2º, da Lei nº 9.249/1995
- Tributos com exigibilidade suspensa (não pagos) .... art. 41, §1º, da Lei nº 8.981/1995
- Resultado NEGATIVO de equivalência patrimonial ..... art. 23 do Decreto-Lei nº 1.598/1977
- JCP acima do limite legal .......................... art. 9º da Lei nº 9.249/1995
- Ajustes de preço de transferência .................. Lei nº 14.596/2023
- Despesas não necessárias à atividade ou sem
  comprovação ........................................ art. 311 do RIR/2018 (Decreto nº 9.580/2018)
- PLR paga em desacordo com a Lei nº 10.101/2000 .... art. 3º, § 1º, da Lei nº 10.101/2000
```
Cada adição está ligada à lei de origem. Se o cliente ou o fisco pedir o artigo do RIR/2018, localizar o dispositivo correspondente no Decreto nº 9.580/2018 antes de citá-lo.

### 5. Exclusões — Parte A (receitas contabilizadas que a lei não tributa)
```
- Reversão de provisões que foram adicionadas
- Resultado POSITIVO de equivalência patrimonial ..... art. 23 do Decreto-Lei nº 1.598/1977
- Dividendos recebidos de PJ no Brasil ............... art. 10 da Lei nº 9.249/1995
- Variação cambial ativa, se optou pelo regime de
  caixa (opção anual) ................................ art. 30 da MP nº 2.158-35/2001
- Amortização de ágio controlada na Parte B .......... Lei nº 12.973/2014
```
Atenção:
- **Lucros de controlada no exterior**: o resultado de equivalência é excluído, mas os lucros da controlada são tributados no Brasil no fim do ano (arts. 76 a 78 da Lei nº 12.973/2014). Não basta excluir.
- **Subvenção para investimento**: desde 01/01/2024 não pode mais ser excluída. A Lei nº 14.789/2023 criou um crédito fiscal (25% sobre a receita de subvenção ligada a implantação ou expansão, com habilitação prévia na Receita).
- Tributos recuperáveis na compra de imobilizado **não** são exclusão do LALUR: só não entram no custo do bem (NBC TG 27).

### 6. Prejuízo fiscal e base negativa — trava de 30%
- A compensação é limitada a 30% do lucro ajustado do período em que se compensa (art. 42 da Lei nº 8.981/1995; art. 15 da Lei nº 9.065/1995). A trava vale na **utilização**, não na geração.
- O que sobra fica na Parte B, sem prazo de validade (salvo mudança de controle e de ramo, e regras de cisão/fusão).
- Prejuízo fiscal (IRPJ, LALUR) e base negativa (CSLL, LACS) são saldos separados.

Exemplo: prejuízo acumulado de R$ 1 milhão e lucro ajustado de R$ 100 mil no trimestre → compensa R$ 30 mil; sobram R$ 970 mil.

### 7. JCP — juros sobre capital próprio
```
JCP máximo = TJLP pro rata × contas do PL permitidas
  (desde 2024: capital social, reservas de capital, reservas de lucros,
   ações em tesouraria e prejuízos acumulados — art. 9º, §8º, da
   Lei nº 9.249/1995, com a redação da Lei nº 14.789/2023)
Limite: o MAIOR entre 50% do lucro líquido do período (antes do JCP e
        do IRPJ, após a CSLL) e 50% dos lucros acumulados + reservas de lucros
```
- É despesa dedutível no IRPJ e na CSLL: economia de até 34% (15% + 10% + 9%) quando há adicional.
- IRRF na fonte sobre o JCP pago ou creditado ao sócio: 17,5% desde 01/01/2026 (art. 9º, §2º, da Lei nº 9.249/1995, com a redação do art. 8º da LC nº 224/2025; até 2025 era 15%).
- Exige ata de deliberação e TJLP do período.

### 8. Estimativa mensal (Real anual)
```
Estimativa do mês = (receita do mês × percentual do Presumido) × 15%
                    + adicional (sobre o excesso de R$ 20.000 no mês)
CSLL estimada = (receita × 12% ou 32%) × 9%
```
- Os percentuais são os dos arts. 15 e 20 da Lei nº 9.249/1995. O acréscimo de 10% da LC nº 224/2025 está dirigido ao lucro presumido (art. 4º, § 5º, da LC nº 224/2025; arts. 14 e 15 da IN RFB nº 2.305/2025, com a redação da IN RFB nº 2.306/2026); esses textos não trazem regra expressa para a base estimada do Real anual. Usar os percentuais normais na estimativa e acompanhar eventual ato da Receita Federal sobre o tema.
- Suspensão ou redução: balancete acumulado do ano, encerrado no último dia do mês e assinado por contador, mostrando que o imposto devido até ali é menor que o já pago (art. 35 da Lei nº 8.981/1995; art. 47 da IN RFB nº 1.700/2017). Estimativa paga a mais vira saldo negativo para compensação, não devolução imediata.

### 9. LC nº 224/2025 no Lucro Real
- Não há presunção no Real trimestral, então a majoração do Presumido não se aplica.
- O impacto vem pela redução de 10% dos benefícios fiscais federais (art. 4º da LC nº 224/2025 — ex.: incentivos regionais de redução do IRPJ) e pelas limitações de crédito de PIS/COFINS; e, para quem paga JCP, pelo IRRF de 17,5%. Pergunte se o cliente usa benefício, confira se ele está na lista dos alcançados ou dos preservados (art. 4º, §§ 2º e 8º) e recalcule o valor do incentivo.

### 10. Entregável obrigatório
**a) LALUR/LACS Parte A**
```
LALUR PARTE A — 1º TRIMESTRE/2026 — EMPRESA EXEMPLO (CNPJ 00.000.000/0001-00)
LAIR contábil ................................. 500.000
(+) ADIÇÕES
   Multa fiscal punitiva ...................... 5.000
   Provisão não dedutível ..................... 18.000
   Doações sem incentivo ...................... 12.000
   JCP acima do limite ........................ 8.000
   Brindes .................................... 2.000
   Total adições .............................. 45.000
(−) EXCLUSÕES
   Dividendos recebidos ....................... 15.000
   Equivalência positiva (controlada no Brasil) 20.000
   Reversão de provisão adicionada ............ 5.000
   Total exclusões ............................ 40.000
LUCRO LÍQUIDO AJUSTADO ........................ 505.000
(−) Prejuízo fiscal compensado (30%) .......... 151.500
LUCRO REAL .................................... 353.500
IRPJ 15% ...................................... 53.025
Adicional 10% × (353.500 − 60.000) ............ 29.350
IRPJ TOTAL — DARF 0220 ........................ 82.375
CSLL 9% (LACS, se os ajustes e a base negativa forem iguais) — DARF 6012 ... 31.815
TOTAL ......................................... 114.190
Vencimento: 30/04/2026 (último dia útil de abril) ou 1ª quota
```
**b) Memória de cálculo** com LALUR, LACS e Parte B.
**c) Parte B atualizada**: prejuízo fiscal e base negativa por ano de origem.
**d) DARFs**: IRPJ 0220 e CSLL 6012 (trimestral) ou 2362/2484 (estimativa) ou 2430/6773 (ajuste); no IRPJ da PJ optante, 3373, 5993 e 2456, com valor, período e vencimento.
**e) Comparativo rápido com o Presumido** (com a LC nº 224/2025 se a receita passar de R$ 5 mi).
**f) Checklist (9 itens)**
```
[ ] LAIR conferido com a DRE do balancete
[ ] Cada adição com documento (NF, comprovante, ata)
[ ] Cada exclusão com fundamento legal (lei + artigo)
[ ] Prejuízo e base negativa compensados com a trava de 30%, em livros separados
[ ] Parte B atualizada por ano de origem
[ ] Adicional só sobre o excesso (R$ 60 mil tri / R$ 240 mil ano)
[ ] Benefícios fiscais recalculados com o corte de 10% da LC nº 224/2025
[ ] Débitos na DCTFWeb e códigos de DARF corretos (0220/6012 ou 2362/2484; IRPJ da optante 3373/5993/2456)
[ ] ECF (anual) coerente com ECD e EFD-Contribuições
```

## Erros comuns / pontos de atenção
- Usar os DARFs do Presumido (2089/2372) no Real.
- Compensar prejuízo acima de 30% ou misturar prejuízo fiscal com base negativa.
- Excluir lucros de controlada no exterior como se fossem dividendos do Brasil.
- Excluir subvenção para investimento pelo regime antigo (acabou em 2024).
- Calcular JCP com contas do PL que a Lei nº 14.789/2023 retirou, ou sem ata.
- Variação cambial pelo caixa sem opção formalizada.
- Calcular o adicional sobre o lucro inteiro.

## Casos de borda
- **Real maior que o Presumido figurado**: avaliar mudança no ano seguinte (`analise-tributaria-regime`).
- **Recuperação judicial**: parcelamento especial (Lei nº 14.112/2020, até 120 meses) → `parcelamento-receita-federal`.
- **Partes relacionadas no exterior**: preço de transferência pela Lei nº 14.596/2023. Grupo multinacional com receita consolidada de 750 milhões de euros ou mais: adicional da CSLL da tributação mínima global (Pilar 2) da Lei nº 15.079/2024.
- **PJ que entra no não cumulativo** (por exemplo, vinda do Presumido): crédito de PIS/COFINS sobre o estoque de abertura, 0,65% + 3% = 3,65%, em 12 parcelas mensais (art. 11 da Lei nº 10.637/2002; art. 12 da Lei nº 10.833/2003). Para empresa vinda do Simples, conferir no texto desses artigos se a hipótese está alcançada antes de lançar o crédito.
- **Dividendos pagos aos sócios a partir de 2026**: IRRF de 10% sobre o total pago no mês pela mesma PJ à mesma pessoa física acima de R$ 50.000,00, e IRPFM anual acima de R$ 600.000,00 de rendimentos (arts. 6º-A e 16-A da Lei nº 9.250/1995, incluídos pela Lei nº 15.270/2025).

## Quando escalar
- Margem alta e receita modesta → `analise-tributaria-regime`.
- Tema 69 retroativo → `recuperacao-creditos-pis-cofins`.
- Recuperação judicial → advogado parceiro (atividade privativa de advogado).
- ECF anual → `ecf-escrituracao-contabil-fiscal`.
- Cruzamento ECF × ECD × DCTFWeb → `revisao-fiscal-cruzamento-sped`.

## Perguntas que o usuário costuma fazer
- "O prejuízo fiscal prescreve?" Não, mas só compensa 30% do lucro ajustado por período.
- "A LC 224 aumentou o IRPJ do Lucro Real?" Não pela base; o efeito vem do corte de 10% dos benefícios.
- "Posso suspender a estimativa de um mês?" Sim, com balancete acumulado que mostre imposto devido menor que o pago.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas a fisco): documento DOCX.
- Este padrão prevalece sobre os formatos citados acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- Lei nº 9.430/1996: arts. 1º a 3º (períodos e opção pelo anual), art. 5º (quotas).
- Lei nº 9.718/1998: art. 14 (obrigados ao Lucro Real).
- Lei nº 8.981/1995: art. 35 (suspensão/redução), art. 41 (tributos e multas), art. 42 (trava de 30%); Lei nº 9.065/1995, art. 15.
- Lei nº 9.249/1995: art. 9º (JCP), art. 10 (dividendos), art. 13 (indedutíveis).
- Lei nº 9.316/1996: art. 1º (IRPJ/CSLL não dedutíveis).
- Decreto-Lei nº 1.598/1977: art. 23 (equivalência patrimonial).
- Lei nº 12.973/2014: arts. 76 a 78 (lucros no exterior).
- Lei nº 14.789/2023 (subvenções e JCP); Lei nº 14.596/2023 (preço de transferência); Lei nº 15.079/2024 (Pilar 2).
- Lei nº 7.689/1988: art. 3º (alíquotas da CSLL).
- LC nº 224/2025: art. 4º (corte de 10% de benefícios), art. 7º (CSLL de financeiras), art. 8º (IRRF de 17,5% sobre JCP), art. 14 (vigência).
- Lei nº 15.270/2025 (dividendos e IRPFM).
- Lei nº 10.101/2000, art. 3º, § 1º (PLR dedutível).
- Decreto nº 9.580/2018 (RIR/2018), art. 311; IN RFB nº 1.700/2017, art. 47; IN RFB nº 2.248/2025 (DCTFWeb).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
