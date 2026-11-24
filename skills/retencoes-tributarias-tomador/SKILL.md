---
name: retencoes-tributarias-tomador
description: "Calcula as retenções que a empresa TOMADORA deve fazer ao pagar serviços de pessoa jurídica: IRRF 1,5% ou 1% (código 1708), CSRF 4,65% (PIS+COFINS+CSLL, código 5952, dispensada quando a retenção do pagamento for de até R$ 10,00), INSS 11% em cessão de mão de obra ou empreitada listada na IN RFB nº 2.110/2022, e ISS conforme a lei municipal e a LC nº 116/2003; aplica as dispensas do prestador optante do Simples (com declaração) e indica prazos, valor líquido a pagar e eventos da EFD-Reinf (R-2010 e R-4020). Acionar quando o usuário disser \"retenção na nota\", \"reter impostos do prestador\", \"CSRF\", \"4,65%\", \"R$ 215,05\", \"IRRF 1,5%\", \"INSS 11%\", \"cessão de mão de obra\", \"ISS retido\", \"declaração do Simples\", \"valor líquido a pagar\", \"DARF 1708 ou 5952\", \"R-2010\", \"R-4020\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Retenções tributárias do tomador de serviços

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Para cada nota de serviço recebida, identifica quais tributos o tomador deve reter (IRRF, CSRF, INSS e ISS), calcula os valores, aplica as dispensas (Simples com declaração, valores mínimos, entidades imunes), informa o líquido a pagar ao prestador, os prazos de recolhimento e os eventos da EFD-Reinf.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Nota de serviço de pessoa jurídica a pagar.
- Dúvida sobre dispensa do Simples, limite da CSRF, retenção de 11% ou ISS retido.
- Conferência de EFD-Reinf (R-2010, R-4020) e DCTFWeb.

Pagamento a pessoa física (salário, RPA, aluguel) → `calculo-irrf-folha`. Locação de bens e aluguel não são serviço: não entram nas retenções desta skill (IRRF de serviços, CSRF, INSS de 11%).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
1. Nota recebida: prestador (CNPJ de exemplo), regime (Simples? qual Anexo?), serviço exato, valor bruto, data do pagamento.
2. O prestador do Simples entregou a **declaração de optante**?
3. O serviço é prestado com cessão de mão de obra ou empreitada **e** está listado nos arts. 111 e 112 da IN RFB nº 2.110/2022?
4. Município do prestador, do tomador e do local da execução; a lei municipal exige retenção?
5. O prestador é entidade imune ou isenta (com comprovação)?

### 2. Quadro de retenções
| Retenção | Alíquota | Norma | Quando | Recolhimento |
|---|---|---|---|---|
| IRRF serviços profissionais | 1,5% | art. 714 do Decreto nº 9.580/2018 (RIR/2018) | medicina, engenharia, advocacia, contabilidade, consultoria, auditoria etc. | DARF 1708 |
| IRRF limpeza, conservação, segurança, vigilância, locação de mão de obra | 1,0% | art. 716 do RIR/2018 | — | DARF 1708 |
| CSRF (PIS 0,65% + COFINS 3% + CSLL 1%) | 4,65% | arts. 30 e 31 da Lei nº 10.833/2003 | serviços do art. 30 (limpeza, conservação, manutenção, segurança, vigilância, transporte de valores, locação de mão de obra, assessoria creditícia, serviços profissionais) | DARF 5952 |
| INSS | 11% | art. 31 da Lei nº 8.212/1991; IN RFB nº 2.110/2022, arts. 110 a 112 | cessão de mão de obra ou empreitada de serviço **listado** | DCTFWeb (após R-2010) |
| ISS | 2% a 5% (ou alíquota efetiva do Simples) | art. 6º da LC nº 116/2003 e lei municipal | conforme lei municipal e § 2º do art. 6º | guia municipal |

**Dispensas e limites**
- **CSRF**: dispensada a retenção de valor igual ou inferior a R$ 10,00 em **um pagamento** (pagamento de até R$ 215,05) — art. 31, § 3º, da Lei nº 10.833/2003, redação da Lei nº 13.137/2015. **Não se soma** mais o mês: a mesma lei revogou o § 4º do art. 31. Dois pagamentos de R$ 200,00 ao mesmo prestador no mês → nenhum retém.
- **IRRF de serviços de PJ (1708)**: dispensada a retenção de valor igual ou inferior a R$ 10,00 (art. 67 da Lei nº 9.430/1996). A Receita aplica a dispensa a cada pagamento ou crédito de pessoa jurídica a outra pessoa jurídica, pelo total pago naquela ocasião, ainda que se refira a mais de uma nota (Solução de Consulta Cosit nº 258/2024, vinculante). Imposto retido acima de R$ 10,00 é recolhido normalmente; a regra do art. 68 da Lei nº 9.430/1996 (não emitir DARF abaixo de R$ 10,00 e somar ao período seguinte) vale para o recolhimento, não para a retenção.
- **Prestador do Simples com declaração de optante**: sem IRRF e sem CSRF, em todos os Anexos. CSRF: art. 32, III, da Lei nº 10.833/2003 e art. 3º, II, da IN SRF nº 459/2004 (receitas próprias do optante). IRRF: IN RFB nº 765/2007. A lei não abre exceção para o Anexo IV; o que muda no Anexo IV é o INSS (item abaixo).
- **INSS do prestador do Simples**: só há retenção de 11% se a atividade for do **Anexo IV** (construção civil, vigilância, limpeza, conservação) e o serviço estiver na lista da IN RFB nº 2.110/2022. Anexos I, II, III e V não sofrem a retenção.
- **MEI**: não há retenção de 11%; nos serviços do art. 18-B da LC nº 123/2006 (hidráulica, eletricidade, pintura, alvenaria, carpintaria, manutenção de veículos), a contratante recolhe 20% de contribuição patronal.
- **Entidade imune ou isenta** (art. 150, VI, "c", da Constituição): a dispensa de retenção depende da norma do tributo e de comprovação do prestador (declaração, estatuto, certificação como o CEBAS quando exigida). Conferir a regra do caso e arquivar a prova antes de deixar de reter.

**Prazos**
- IRRF (1708): até o último dia útil do 2º decêndio do mês seguinte ao pagamento — na prática, dia 20, ou o dia útil anterior (art. 70, I, "e", da Lei nº 11.196/2005).
- CSRF (5952): até o **último dia útil do 2º decêndio** do mês seguinte ao pagamento (art. 35 da Lei nº 10.833/2003, redação da Lei nº 13.137/2015). Não é mais "quinzena".
- INSS 11%: R-2010 até o dia 15; recolhimento via DCTFWeb até o dia 20 do mês seguinte ao da emissão da nota (antecipa se não houver expediente bancário).
- ISS retido: conforme lei municipal.
- EFD-Reinf: R-2010 (INSS) e R-4020 (IRRF/CSRF de PJ), fechamento R-2099/R-4099 até o dia 15. DCTFWeb até o último dia útil do mês seguinte (IN RFB nº 2.248/2025).

### 3. Cálculo (Python, para mostrar a memória)
```python
# Retenções do tomador — avaliação POR PAGAMENTO (sem acúmulo mensal da CSRF)
PROF_1_5 = {'consultoria', 'advocacia', 'contabilidade', 'engenharia', 'arquitetura',
            'medicina', 'auditoria', 'propaganda'}
LIMPEZA_1_0 = {'limpeza', 'conservacao', 'seguranca', 'vigilancia', 'locacao_mao_obra'}

def retencoes(valor, servico, prestador_simples=False, declaracao_simples=False,
              anexo_simples=None, servico_listado_in_2110=False,
              lei_municipal_retem_iss=False, aliq_iss=0.05):
    irrf = csrf = inss = iss = 0.0
    dispensa_simples = prestador_simples and declaracao_simples
    # IRRF (código 1708)
    if not dispensa_simples:
        if servico in LIMPEZA_1_0:
            irrf = valor * 0.01
        elif servico in PROF_1_5:
            irrf = valor * 0.015
        if irrf <= 10.00:   # art. 67 da Lei nº 9.430/1996 (SC Cosit nº 258/2024): por pagamento
            irrf = 0.0
    # CSRF (código 5952): dispensa se a retenção DESTE pagamento for <= R$ 10,00
    if not dispensa_simples and (servico in LIMPEZA_1_0 or servico in PROF_1_5):
        csrf = valor * 0.0465
        if csrf <= 10.00:
            csrf = 0.0
    # INSS 11%: serviço listado na IN 2.110; prestador do Simples só se Anexo IV
    if servico_listado_in_2110 and (not prestador_simples or anexo_simples == 'IV'):
        inss = valor * 0.11
    # ISS: só se a lei municipal (ou art. 6º, § 2º, LC 116) mandar o tomador reter
    if lei_municipal_retem_iss:
        iss = valor * aliq_iss          # prestador do Simples: usar a alíquota efetiva da nota
    total = irrf + csrf + inss + iss
    return {k: round(v, 2) for k, v in
            {'IRRF': irrf, 'CSRF': csrf, 'INSS': inss, 'ISS': iss,
             'total_retido': total, 'liquido': valor - total}.items()}

print(retencoes(10_000, 'consultoria', lei_municipal_retem_iss=True))
# IRRF 150 | CSRF 465 | INSS 0 | ISS 500 | total 1.115 | líquido 8.885
print(retencoes(10_000, 'limpeza', servico_listado_in_2110=True, lei_municipal_retem_iss=True))
# IRRF 100 | CSRF 465 | INSS 1.100 | ISS 500 | total 2.165 | líquido 7.835
print(retencoes(200, 'consultoria'))
# CSRF 9,30 <= 10,00 -> dispensada; IRRF 3,00 <= 10,00 -> dispensado (art. 67 da Lei nº 9.430/1996) | líquido 200,00
```

### 4. Declaração do prestador do Simples (modelo)
```
A EMPRESA EXEMPLO SERVIÇOS LTDA, CNPJ 00.000.000/0001-00, declara, para fins de não
incidência na fonte do IRRF e das contribuições PIS, COFINS e CSLL, que é optante pelo
Simples Nacional (LC nº 123/2006), e se compromete a informar qualquer alteração.
Local, data. Assinatura do representante legal.
```
Guardar no dossiê com a nota. A declaração precisa ter CNPJ, razão social, data, a afirmação expressa de que é optante e a assinatura do representante legal; se for falsa, a responsabilidade pelo tributo não retido é do prestador que a assinou.

### 5. Entregável
**a) Cálculo da nota**
```
NF nº 12345 — Prestador: CONSULTORIA EXEMPLO LTDA (Lucro Presumido) — CNPJ 00.000.000/0001-00
Serviço: consultoria — Tomador e prestador no MUNICÍPIO EXEMPLO
Valor bruto: R$ 10.000,00

[X] IRRF 1,5% (1708) ................ 150,00
[X] CSRF 4,65% (5952) ............... 465,00  (PIS 65,00 | COFINS 300,00 | CSLL 100,00)
[ ] INSS 11% ........................   0,00  (não é cessão de mão de obra listada)
[X] ISS retido 5% ................... 500,00  (lei municipal nº ___/____, art. __)
Total retido ...................... 1.115,00
LÍQUIDO A PAGAR ................... 8.885,00

Recolhimentos do tomador:
- DARF 1708: 150,00 — até 20/MM+1 (antecipa se não for dia útil)
- DARF 5952: 465,00 — até o último dia útil do 2º decêndio de MM+1
- Guia de ISS: 500,00 — prazo da lei municipal
```
**b) Comprovante ao prestador** com cada retenção por tributo.
**c) EFD-Reinf**: R-2010 (INSS) e R-4020 (IRRF/CSRF), com competência.
**d) Planilha** de memória (ver "Formato de entrega").
**e) Checklist**
```
[ ] Cada nota analisada (serviço + regime e Anexo do prestador)
[ ] Declaração de optante do Simples arquivada, quando houver dispensa
[ ] CSRF avaliada por pagamento (dispensa só se a retenção for ≤ R$ 10,00)
[ ] INSS 11% só em serviço listado na IN RFB nº 2.110/2022 (Simples: só Anexo IV)
[ ] ISS conforme lei municipal e local de incidência (LC nº 116/2003, art. 3º)
[ ] DARFs com código e vencimento corretos
[ ] EFD-Reinf (R-2010, R-4020) e DCTFWeb transmitidas
```
A DIRF foi extinta para fatos a partir de 2025; as informações vão na EFD-Reinf (série R-4000). DIRF só para retificar anos anteriores.

## Erros comuns / pontos de atenção
- Somar os pagamentos do mês para a CSRF (regra revogada em 2015) ou usar o antigo limite de R$ 5.000,00.
- Recolher a CSRF pela "quinzena" (o prazo é o 2º decêndio).
- Reter 11% de prestador do Simples fora do Anexo IV, ou deixar de reter do Anexo IV.
- Reter INSS só por ser "cessão de mão de obra", sem conferir a lista da IN RFB nº 2.110/2022.
- Aplicar 1,5% em limpeza e vigilância (é 1%).
- Reter ISS cheio (5%) de prestador do Simples (deve ser a alíquota efetiva informada na nota).
- Cooperativa de trabalho: a contribuição de 15% do tomador (art. 22, IV, da Lei nº 8.212/1991) foi declarada inconstitucional pelo STF (RE 595.838) — não recolher.

### Casos de borda
- **Adiantamento**: seguir o momento de cada retenção. IRRF e CSRF são retidos no **pagamento** (art. 30 da Lei nº 10.833/2003 para a CSRF); o INSS de 11% é retido sobre o valor bruto da **nota** e recolhido até o dia 20 do mês seguinte ao da emissão (art. 31 da Lei nº 8.212/1991). Se houver pagamento antecipado de serviço ainda não faturado, analisar o contrato e registrar a decisão na memória.
- **Royalties pagos a PJ**: não são serviço do art. 30 nem dos arts. 714 e 716 do RIR/2018; tratar fora desta skill, conferindo a norma do caso.
- **Vários pagamentos no mês ao mesmo prestador**: avaliar cada um isoladamente para a CSRF.
- **Locação de bens**: não é serviço; não há retenção de serviço.
- **Prestador de outro município**: conferir o local de incidência (skill `calculo-iss`).

### Quando escalar
- EFD-Reinf → `efd-reinf`; DCTFWeb → `dctfweb`.
- Folha e pagamentos a PF → `calculo-irrf-folha`.
- Conferência das notas de empresa do Simples → `conferir-apuracao-simples-nacional`.

## Perguntas que o usuário costuma fazer
- **"Paguei R$ 400 em duas notas de R$ 200 ao mesmo prestador. Retenho CSRF?"** Não. Cada pagamento é avaliado sozinho; nenhum passa de R$ 10,00 de retenção.
- **"Prestador do Simples sempre está livre do INSS 11%?"** Não. Se ele for do Anexo IV (limpeza, vigilância, construção) e o serviço estiver na lista, retém.
- **"Qual o prazo da CSRF?"** Último dia útil do 2º decêndio do mês seguinte ao pagamento (na prática, até o dia 20, antecipando se não for dia útil). O IRRF de serviços (1708) tem o mesmo prazo.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas a fisco): documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Decreto nº 9.580/2018 (RIR/2018), arts. 714 e 716 — IRRF sobre serviços de PJ.
- Lei nº 9.430/1996, arts. 67 (dispensa da retenção de IRRF de até R$ 10,00, por pagamento — Solução de Consulta Cosit nº 258/2024) e 68 (DARF mínimo de R$ 10,00 e acumulação no recolhimento).
- Lei nº 11.196/2005, art. 70, I, "e" — prazo do IRRF.
- Lei nº 10.833/2003, arts. 30, 31 (§ 3º), 32 (III — optante do Simples) e 35 (redação da Lei nº 13.137/2015) — CSRF, dispensa e prazo.
- IN SRF nº 459/2004 — procedimentos da CSRF; art. 3º, II (optante do Simples).
- IN RFB nº 765/2007 — dispensa de IRRF sobre pagamentos a optante do Simples.
- Lei nº 8.212/1991, art. 31 — retenção de 11%; IN RFB nº 2.110/2022, arts. 110 a 112.
- LC nº 116/2003, arts. 3º e 6º — local de incidência e responsabilidade do tomador pelo ISS.
- LC nº 123/2006, arts. 18-B e 21, § 4º — MEI e ISS retido de optante.
- IN RFB nº 2.043/2021 — EFD-Reinf; IN RFB nº 2.248/2025 — DCTFWeb.
- STF, RE 595.838 — contribuição sobre serviços de cooperativas.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
