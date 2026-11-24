---
name: calculo-pis-cofins-cumulativo
description: "Apuração mensal de PIS (0,65%) e COFINS (3%) no regime cumulativo (Lucro Presumido e atividades do art. 10 da Lei nº 10.833/2003 no Lucro Real), com exclusão do ICMS destacado (Tema 69 do STF), demais exclusões da receita bruta, segregação de receitas monofásicas (alíquota zero na revenda), efeitos da LC nº 224/2025 desde 01/04/2026, dedução da CSRF retida e DARFs 8109 e 2172. Acionar quando o usuário disser \"PIS e COFINS do Presumido\", \"regime cumulativo\", \"0,65% e 3%\", \"excluir ICMS da base\", \"Tema 69\", \"monofásico\", \"revenda de cosmético/autopeça/combustível/bebida fria\", \"CSRF retida\", \"DARF 8109 ou 2172\", \"receita financeira no Presumido\" ou \"LC 224 no PIS/COFINS\". Entrega: apuração mensal em planilha, DARFs com vencimento e checklist."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Apuração de PIS/COFINS cumulativo

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Calcula o PIS e a COFINS do mês no regime cumulativo: parte da receita bruta, faz as exclusões permitidas (ICMS destacado, vendas canceladas, descontos incondicionais, IPI, ICMS-ST, receitas monofásicas e de exportação), aplica as alíquotas, desconta as retenções sofridas e indica os DARFs. Neste regime **não há crédito** sobre compras.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Reforma Tributária.** 2026 é ano-teste: CBS 0,9% e IBS 0,1% destacados na nota e compensáveis integralmente com o PIS/COFINS devido; quem cumpre as obrigações acessórias fica dispensado do recolhimento (Emenda Constitucional nº 132/2023; Lei Complementar nº 214/2025). **A partir de 2027 o PIS e a COFINS são extintos e substituídos pela CBS.** Use a skill `reforma-tributaria-transicao`.

> **LC nº 224/2025.** Desde 01/04/2026 operações antes isentas ou com alíquota zero passaram a ser tributadas a 10% da alíquota do sistema padrão (art. 4º, §4º, I, da LC nº 224/2025). No cumulativo, o sistema padrão é 0,65% e 3% (art. 4º, §3º, III), logo: **PIS 0,065% + COFINS 0,30%**. Ficam fora da redução, entre outras, as alíquotas zero da Cesta Básica Nacional e dos produtos do Anexo XV da LC nº 214/2025 (art. 4º, §8º, III). Para o Lucro Presumido, a majoração de 10% da presunção do IRPJ/CSLL acima de R$ 5 milhões não muda a alíquota do PIS/COFINS. Conferir sempre a IN RFB nº 2.305/2025 e a Nota Técnica EFD-Contribuições nº 12/2026.

## Quando usar
- Empresa no Lucro Presumido (ou Arbitrado).
- Lucro Real com receitas que a lei mantém no cumulativo (art. 10 da Lei nº 10.833/2003).
- Conferência de EFD-Contribuições e DARFs de PIS/COFINS cumulativo.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
1. CNPJ (pode ser de exemplo), competência e receita bruta do mês segregada (vendas, serviços, outras).
2. ICMS destacado nas notas de saída do mês (Tema 69).
3. Há receita monofásica (combustível, medicamento, perfumaria/higiene, autopeça, bebida fria), exportação, IPI ou ICMS-ST destacados?
4. Há operações que antes eram isentas ou de alíquota zero (atingidas pela LC nº 224/2025)?
5. Houve CSRF (4,65%) retida por clientes no mês?
6. Lucro Real: a receita é de atividade do art. 10 da Lei nº 10.833/2003?

### 2. Parâmetros
```
ALÍQUOTAS (cumulativo)
PIS 0,65%  |  COFINS 3,00%  (bancos e assemelhados: COFINS 4% — art. 18 da Lei nº 10.684/2003)
Operações antes isentas/alíquota zero, desde 01/04/2026 (LC nº 224/2025): PIS 0,065% + COFINS 0,30%

BASE = receita bruta (art. 12 do Decreto-Lei nº 1.598/1977, redação da Lei nº 12.973/2014)
(−) ICMS destacado nas saídas (STF, RE 574.706 — Tema 69)
(−) vendas canceladas e devoluções; descontos incondicionais (Lei nº 9.718/1998, art. 3º, § 2º, I)
(−) IPI e ICMS cobrado como substituto tributário, destacados na nota: não
    compõem a receita bruta (Decreto-Lei nº 1.598/1977, art. 12, § 4º,
    redação da Lei nº 12.973/2014)
(−) ISS: STF, Tema 118 (RE 592.616), julgado em 21/10/2026 — ver regra de uso no passo 4
(−) receitas de exportação (isentas; imunidade do art. 149, § 2º, I, da Constituição)
(−) receitas de revenda de produtos monofásicos (alíquota zero na revenda)

DARF E PRAZO
PIS cumulativo: 8109  |  COFINS cumulativo: 2172
Vencimento: até o dia 25 do mês seguinte; se não for dia útil, ANTECIPA
(art. 18, II e parágrafo único, da Medida Provisória nº 2.158-35/2001,
redação da Lei nº 11.933/2009). Bancos e demais pessoas jurídicas do
art. 22, § 1º, da Lei nº 8.212/1991: até o dia 20 (art. 18, I).
Declaração: DCTFWeb (MIT) até o último dia útil do mês seguinte (IN RFB nº 2.248/2025)
EFD-Contribuições: até o 10º dia útil do 2º mês seguinte

CSRF RETIDA PELO CLIENTE (4,65% = PIS 0,65% + COFINS 3% + CSLL 1%)
Deduz do PIS e da COFINS devidos, cada parcela no seu tributo (a CSLL retida vai para a CSLL).
```

### 3. Cálculo (Python, para mostrar a memória)
```python
# PIS/COFINS cumulativo — base = receita bruta - exclusões
def pis_cofins_cumulativo(receita_bruta, icms_destacado=0, vendas_canc=0, descontos_incond=0,
                          ipi=0, icms_st=0, rec_exportacao=0, rec_monofasica=0,
                          rec_lc224=0, pis_retido=0, cofins_retida=0):
    # Se a receita bruta informada já vier sem IPI e ICMS-ST, passar ipi=0 e icms_st=0
    base = (receita_bruta - icms_destacado - vendas_canc - descontos_incond - ipi - icms_st
            - rec_exportacao - rec_monofasica - rec_lc224)
    pis = base * 0.0065 + rec_lc224 * 0.00065      # LC 224/2025: 10% da alíquota cheia
    cofins = base * 0.03 + rec_lc224 * 0.0030
    return {
        'base': round(base, 2),
        'pis_devido': round(pis, 2), 'cofins_devida': round(cofins, 2),
        'pis_a_recolher_8109': round(max(0, pis - pis_retido), 2),
        'cofins_a_recolher_2172': round(max(0, cofins - cofins_retida), 2),
    }

print(pis_cofins_cumulativo(800_000, icms_destacado=96_000, vendas_canc=5_000))
# base 699.000,00 | PIS 4.543,50 | COFINS 20.970,00
```

### 4. Tema 69 — como aplicar
- STF, RE 574.706 (Tema 69), julgado em 15/03/2017: o ICMS não compõe a base do PIS e da COFINS. Nos embargos (2021) o STF definiu que se exclui o **ICMS destacado** na nota (não o recolhido) e modulou os efeitos a partir de 15/03/2017, ressalvadas as ações ajuizadas até essa data.
- No cumulativo, a exclusão é feita na apuração mensal: base = receita bruta − ICMS destacado − demais exclusões. Para uma alíquota de ICMS de 18%, a base cai para cerca de 82% da receita.
- A Lei nº 14.592/2023 **não** "consolidou o Tema 69" nas saídas: ela tratou dos **créditos** do regime não cumulativo (excluiu o ICMS da base do crédito, a partir de maio/2023). Não tem efeito no cumulativo, que não tem crédito.
- Recuperação dos 5 anos anteriores → `recuperacao-creditos-pis-cofins`.

**Exclusão do ISS — Tema 118 do STF (RE 592.616).** Em 21/10/2026 o STF decidiu que o valor do ISS não integra a base do PIS e da COFINS. Regra de uso: toda vez que aplicar essa exclusão, verificar no portal do STF se o acórdão do RE 592.616 já foi publicado e se houve modulação de efeitos (o colegiado não analisou modulação no julgamento; o tema pode voltar em embargos). Se o acórdão ainda não tiver sido publicado, informar ao usuário: "o acórdão do Tema 118 do STF ainda não foi publicado". Se já foi, seguir normalmente, conferindo a modulação.

### 5. Receita financeira e outras receitas
- O STF declarou inconstitucional o alargamento da base do art. 3º, § 1º, da Lei nº 9.718/1998 (RE 585.235, Tema 110). Depois da Lei nº 12.973/2014, a base do cumulativo é a **receita bruta** do art. 12 do Decreto-Lei nº 1.598/1977 (atividade principal). Para empresa não financeira, receita financeira não entra na base do PIS/COFINS cumulativo. Instituições financeiras têm regra própria (STF, Tema 372).
- Indenização que não é receita não entra na base.

### 6. Monofásicos — alíquota zero na revenda
A tributação é concentrada no fabricante ou importador; o atacadista e o varejista revendem com alíquota zero:
- Combustíveis: Lei nº 9.718/1998, arts. 4º a 6º; Lei nº 10.865/2004.
- Medicamentos e perfumaria/higiene pessoal: Lei nº 10.147/2000.
- Autopeças: Lei nº 10.485/2002 (NCMs dos anexos).
- Bebidas frias: Lei nº 13.097/2015.
Erro frequente: varejista pagando 3,65% sobre a revenda de cosmético ou autopeça.
**LC nº 224/2025 na revenda monofásica**: o texto da lei não trata expressamente da revenda de produto monofásico (CST 04). Antes de tributar ou de manter a alíquota zero na revenda a partir de 04/2026, conferir a IN RFB nº 2.305/2025 e a Nota Técnica EFD-Contribuições nº 12/2026 para o NCM e o regime do cliente, e registrar a decisão e o fundamento na memória de cálculo.

### 7. Entregável
**a) Apuração mensal**
```
PIS/COFINS CUMULATIVO — MM/2026 — EMPRESA EXEMPLO LTDA — CNPJ 00.000.000/0001-00

Receita bruta total ...................... 800.000,00
(−) Vendas canceladas ...................... 5.000,00
(−) IPI / ICMS-ST destacados ....................0,00
(−) ICMS destacado (Tema 69) .............. 96.000,00
(−) Exportação / monofásicos .................. 0,00
(=) BASE ................................. 699.000,00
PIS (0,65%) ................................ 4.543,50
COFINS (3,00%) ............................ 20.970,00
(−) PIS / COFINS retidos por clientes ......... 0,00
DARF 8109 (PIS) ............................ 4.543,50
DARF 2172 (COFINS) ........................ 20.970,00
Vencimento: 25/MM+1 (antecipar se não for dia útil)
```
**b) Planilha** de memória (ver "Formato de entrega").
**c) DARFs** com código, valor e vencimento.
**d) Oportunidade**: se o ICMS não vinha sendo excluído, estimar a recuperação dos últimos 5 anos e encaminhar a `recuperacao-creditos-pis-cofins`.
**e) Checklist**
```
[ ] Receita conferida com as notas e com a EFD-Contribuições
[ ] ICMS destacado excluído (Tema 69); ISS (Tema 118) só com a regra de uso aplicada
[ ] Monofásicos e exportação segregados
[ ] Operações atingidas pela LC nº 224/2025 tributadas a 0,065% + 0,30% desde 04/2026
[ ] PIS e COFINS retidos (CSRF) deduzidos cada um no seu tributo
[ ] DARFs 8109 e 2172 com vencimento no dia 25 (antecipado se preciso)
[ ] DCTFWeb (MIT) e EFD-Contribuições transmitidas no prazo
```

## Erros comuns / pontos de atenção
- Não excluir o ICMS destacado.
- Tributar receita de revenda monofásica.
- Esquecer de abater o PIS e a COFINS retidos pelos clientes.
- Aplicar o não cumulativo (1,65% + 7,6%) em empresa do Presumido.
- Incluir receita financeira de empresa não financeira na base.
- Esquecer a LC nº 224/2025 em operações que eram isentas ou de alíquota zero.

### Casos de borda
- **Migração do Simples para o Presumido**: PIS/COFINS cumulativo a partir do mês em que começa o novo regime.
- **Lucro Real com atividade do art. 10 da Lei nº 10.833/2003** (por exemplo, serviços hospitalares, transporte coletivo de passageiros, telecomunicações, empresas jornalísticas e de radiodifusão): essas receitas ficam no cumulativo; separar das demais.
- **Incorporação imobiliária no RET**: pagamento unificado de 4% (IRPJ, CSLL, PIS e COFINS) sobre a receita da incorporação afetada (Lei nº 10.931/2004, art. 4º).
- **Exportação**: isenta; no cumulativo não há saldo credor a recuperar (não existe crédito).

### Quando escalar
- Recuperação do Tema 69 (5 anos) → `recuperacao-creditos-pis-cofins`.
- Comparar com Lucro Real → `calculo-pis-cofins-nao-cumulativo` e `analise-tributaria-regime`.
- Cruzamento EFD-Contribuições × DCTFWeb → `revisao-fiscal-cruzamento-sped`.
- Autuação → `resposta-fiscalizacao-intimacao`.

## Perguntas que o usuário costuma fazer
- **"Excluo o ICMS que paguei ou o que está na nota?"** O destacado na nota de saída.
- **"Empresa do Presumido tem crédito de PIS/COFINS?"** Não. No cumulativo não há crédito.
- **"Em 2027 ainda existe PIS/COFINS?"** Não. A CBS substitui os dois a partir de 2027.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas a fisco): documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei nº 9.715/1998 (PIS) e LC nº 70/1991 (COFINS).
- Lei nº 9.718/1998, arts. 2º, 3º, § 2º (base e exclusões), 4º a 6º (combustíveis) e 8º (alíquota COFINS); Lei nº 10.684/2003, art. 18 (COFINS de 4% de bancos).
- Decreto-Lei nº 1.598/1977, art. 12, caput e § 4º (receita bruta; tributos destacados fora dela, redação da Lei nº 12.973/2014).
- Medida Provisória nº 2.158-35/2001, art. 18 (prazo, redação da Lei nº 11.933/2009).
- Lei nº 10.833/2003, art. 10 (receitas que permanecem no cumulativo) e arts. 30 a 36 (CSRF).
- Lei nº 10.147/2000, Lei nº 10.485/2002, Lei nº 13.097/2015 (monofásicos).
- Lei nº 10.931/2004, art. 4º (RET).
- STF, RE 574.706 (Tema 69); STF, RE 585.235 (Tema 110); STF, RE 592.616 (Tema 118 — ISS); STF, Tema 372.
- Lei nº 14.592/2023 (ICMS fora da base dos créditos no não cumulativo).
- LC nº 224/2025, art. 4º, §§ 3º, III, 4º, I, e 8º, III, e IN RFB nº 2.305/2025 (tributação de 10% da alíquota do sistema padrão desde 01/04/2026); Nota Técnica EFD-Contribuições nº 12/2026.
- IN RFB nº 2.121/2022 (consolidação das normas de PIS/COFINS); IN RFB nº 2.248/2025 (DCTFWeb).
- EC nº 132/2023 e LC nº 214/2025 (CBS a partir de 2027).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
