---
name: calculo-irrf-folha
description: "Cálculo do IRRF sobre salário CLT, pró-labore, 13º salário, RPA de autônomo e outros rendimentos pagos por empresa a pessoa física (aluguel, juros, royalties), com a tabela mensal vigente desde maio/2025, desconto simplificado de R$ 607,20, dependente de R$ 189,59, pensão judicial, INSS deduzido e o REDUTOR da Lei nº 15.270/2025 (IR zero até R$ 5.000,00 de rendimento). Acionar quando o usuário disser \"calcular IRRF\", \"imposto de renda na folha\", \"tabela do IR 2026\", \"redutor dos 5 mil\", \"isenção até 5 mil\", \"desconto simplificado\", \"dependente de IR\", \"IR do 13º\", \"IR do pró-labore\", \"RPA\", \"DARF 0561/0588/3208\", ou perguntar se aviso prévio indenizado, férias indenizadas ou multa do FGTS têm IR. Entrega: memória de cálculo (tabela, redutor e IRRF devido em linhas separadas), código da receita, análise de não incidência e checklist."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Cálculo do IRRF na folha e em pagamentos a pessoa física

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Calcula o imposto de renda que a empresa deve reter de pessoas físicas: empregado CLT, sócio (pró-labore), autônomo (RPA) e outros rendimentos. Aplica a tabela progressiva mensal, compara deduções legais com o desconto simplificado, aplica o redutor da Lei nº 15.270/2025 e indica o código da receita e o prazo. Também aponta as verbas em que não há IR.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Cálculo ou conferência do IRRF da folha mensal, do 13º, do pró-labore ou de RPA.
- Dúvida sobre o redutor de 2026, dependentes, pensão judicial ou desconto simplificado.
- Verbas rescisórias: saber o que tem e o que não tem IR.
- Pagamento de aluguel, juros ou royalties de PJ a PF.

Folha completa → `folha-pagamento-mensal`; rescisão → `rescisao-clt-calculo`; carnê-leão → skill de IRPF.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
1. Tipo de rendimento (salário CLT, pró-labore, RPA, aluguel, 13º) e valor bruto do mês.
2. Dependentes (quantos) e pensão alimentícia judicial (valor).
3. CLT/pró-labore: INSS do mês já calculado? Há previdência complementar?
4. Autônomo: o tomador é PJ? (a PJ retém; não é carnê-leão).
5. É 13º? (tributação exclusiva, separada do mês).

### 2. Tabelas de 2026

**Tabela progressiva mensal** (vigente desde maio/2025 — Lei nº 15.191/2025; **não** foi alterada pela Lei nº 15.270/2025)

| Base mensal (R$) | Alíquota | Parcela a deduzir |
|---|---|---|
| até 2.428,80 | isento | 0,00 |
| 2.428,81 a 2.826,65 | 7,5% | 182,16 |
| 2.826,66 a 3.751,05 | 15% | 394,16 |
| 3.751,06 a 4.664,68 | 22,5% | 675,49 |
| acima de 4.664,68 | 27,5% | 908,73 |

- Dependente: R$ 189,59 por mês.
- **Desconto simplificado mensal: R$ 607,20** (25% de 2.428,80). Ele **substitui** todas as deduções legais (INSS, dependentes, pensão, previdência complementar). Usar o que der menor imposto. (Era R$ 564,80 até abril/2025.)

**Redutor da Lei nº 15.270/2025** (art. 3º-A da Lei nº 9.250/1995) — aplicado **depois** da tabela, desde 01/01/2026, aos rendimentos tributáveis sujeitos à incidência mensal, calculado sobre o **rendimento tributável bruto** do mês (não sobre a base):

| Rendimento tributável bruto mensal | Redução do imposto |
|---|---|
| até 5.000,00 | até R$ 312,89, limitada ao imposto apurado (IRRF = zero) |
| 5.000,01 a 7.350,00 | 978,62 − (0,133145 × rendimento), limitada ao imposto apurado |
| acima de 7.350,00 | sem redução |

O redutor nunca gera imposto negativo (art. 3º-A, §1º, da Lei nº 9.250/1995). São duas referências diferentes no mesmo cálculo: a tabela usa a **base** (bruto − deduções); o redutor usa o **bruto**.

Ajuste anual (declaração de 2027, ano-calendário 2026 — art. 11-A da Lei nº 9.250/1995, incluído pela Lei nº 15.270/2025): imposto zerado para rendimentos tributáveis até R$ 60.000,00 e redução parcial até R$ 88.200,00 (R$ 8.429,73 − 0,095575 × rendimento anual). Quem tem mais de uma fonte pagadora acerta na declaração anual.

**INSS do segurado em 2026** (Portaria Interministerial MPS/MF nº 13/2026), progressivo faixa a faixa: até 1.621,00 = 7,5%; até 2.902,84 = 9%; até 4.354,27 = 12%; até 8.475,55 = 14%. Teto R$ 8.475,55; desconto máximo R$ 988,09. Contribuinte individual (pró-labore e autônomo pago por PJ): 11% até o teto (máximo R$ 932,31).

**Códigos de receita (DARF) por natureza**
- 0561 — rendimento do trabalho assalariado, inclusive 13º, e pró-labore.
- 0588 — rendimento do trabalho sem vínculo (autônomo, RPA).
- 3208 — aluguéis e royalties pagos a pessoa física.
- 1708 — serviços profissionais prestados por PJ (ver `retencoes-tributarias-tomador`).
- 3562 — participação nos lucros ou resultados (PLR).
- 5706 — juros sobre capital próprio (art. 9º da Lei nº 9.249/1995). Alíquota de 17,5% desde 01/01/2026 (art. 9º, §2º, da Lei nº 9.249/1995, com redação da LC nº 224/2025). Prazo próprio: até o 3º dia útil seguinte ao decêndio do pagamento (art. 70, I, "b", da Lei nº 11.196/2005).
- Desde a inclusão do IRRF na DCTFWeb, o DARF é emitido pela própria DCTFWeb a partir do eSocial (S-1210) e da EFD-Reinf, já agrupando os débitos por código: conferir no DARF gerado se cada natureza saiu no código certo, sem montar DARF avulso.

**Prazo de pagamento**: até o **último dia útil do 2º decêndio** do mês seguinte ao do pagamento do rendimento (fato gerador do IRRF é o pagamento) — na prática, dia 20, ou o dia útil anterior se o dia 20 não for útil (art. 70, I, "e", da Lei nº 11.196/2005). A DCTFWeb vence no último dia útil do mês seguinte (IN RFB nº 2.248/2025), mas isso não adia o pagamento do IRRF.

### 3. Cálculo (Python, para mostrar a memória)

```python
# IRRF mensal 2026: tabela (sobre a base) + redutor da Lei nº 15.270/2025 (sobre o bruto)
def faixa(base):
    if base <= 2428.80: return 0.0
    if base <= 2826.65: return base * 0.075 - 182.16
    if base <= 3751.05: return base * 0.15 - 394.16
    if base <= 4664.68: return base * 0.225 - 675.49
    return base * 0.275 - 908.73

def irrf_mensal(bruto, inss=0, dependentes=0, pensao=0, simplificado=False):
    # Deduções legais OU desconto simplificado (um substitui o outro)
    deducoes = 607.20 if simplificado else inss + dependentes * 189.59 + pensao
    base = bruto - deducoes
    imposto = max(faixa(base), 0)
    # Redutor: usa o rendimento BRUTO tributável
    if bruto <= 5000:
        reducao = min(imposto, 312.89)   # até R$ 312,89, limitada ao imposto
    elif bruto <= 7350:
        reducao = min(max(978.62 - 0.133145 * bruto, 0), imposto)
    else:
        reducao = 0
    return round(base, 2), round(imposto, 2), round(reducao, 2), round(imposto - reducao, 2)

# Exemplo: bruto 6.272,73; INSS 2026 = 679,70; 2 dependentes
print(irrf_mensal(6272.73, 679.70, 2))                  # base 5.213,85 | tabela 525,08 | redutor 143,44 | IRRF 381,64
print(irrf_mensal(6272.73, simplificado=True))          # IRRF 505,85 -> deduções legais são melhores
```

### 4. Regras críticas
- **13º salário**: tributação exclusiva na fonte, separada do salário do mês, sobre o valor **total** do 13º, no mês da quitação (2ª parcela). Base = 13º bruto − INSS do 13º − dependentes − pensão. A 1ª parcela (até 30/11) não tem desconto de INSS nem de IR. **Redutor no 13º**: a redução também se aplica ao imposto cobrado exclusivamente na fonte sobre o 13º (art. 3º-A, §3º, da Lei nº 9.250/1995, incluído pela Lei nº 15.270/2025): calcular o IR do 13º pela tabela e aplicar o redutor separadamente, com o valor do 13º como rendimento, sem somar ao salário do mês.
- **Pró-labore**: INSS de 11% até o teto + IRRF pela tabela e redutor. A empresa recolhe a contribuição patronal de 20% sobre o pró-labore (fora do Simples dos Anexos I a III e V).
- **Autônomo (RPA) pago por PJ**: retém INSS de 11% (até o teto), IRRF pela tabela (código 0588) e ISS se a lei municipal exigir. A empresa recolhe 20% de contribuição patronal.
- **Aluguel pago por PJ a PF**: IRRF pela tabela mensal (código 3208). Não entram no rendimento bruto os impostos, taxas e emolumentos sobre o imóvel, o aluguel pago pela locação de imóvel sublocado, as despesas de cobrança ou recebimento (comissão da administradora) e as despesas de condomínio, quando pagos pelo locador (art. 42 do Decreto nº 9.580/2018 — RIR/2018). Como o aluguel é rendimento tributável sujeito à incidência mensal, entra no cálculo do redutor da Lei nº 15.270/2025 pela redação do art. 3º-A da Lei nº 9.250/1995.
- **Pensão alimentícia judicial**: deduz integralmente da base (art. 4º, II, da Lei nº 9.250/1995).

**Verbas sem IR (não reter)**
- Aviso prévio indenizado e indenização por despedida, até o limite legal, e FGTS (inclusive a multa de 40%): art. 6º, V, da Lei nº 7.713/1988.
- Férias não gozadas indenizadas (vencidas e proporcionais) e o terço: Súmulas 125 e 386 do STJ.
- **Atenção**: indenização por horas extras **tem** IR, mesmo prevista em acordo coletivo (Súmula 463 do STJ).

### 5. Entregável
**a) Memória de cálculo**
```
COLABORADOR: EMPREGADO EXEMPLO — CPF 000.000.000-00 — Competência MM/2026

Salário bruto.......................... 6.000,00
Hora extra 50% (10h × 27,27)........... 272,73
BRUTO TRIBUTÁVEL..................... 6.272,73

(−) INSS 2026 (progressivo).............. 679,70
    121,58 + 115,37 + 174,17 + 268,58
(−) Dependentes (2 × 189,59)............. 379,18
(−) Pensão alimentícia.................... 0,00
BASE IRRF............................ 5.213,85

IR pela tabela: 5.213,85 × 27,5% − 908,73 = 525,08
Redutor (bruto 6.272,73 entre 5.000,01 e 7.350,00):
  978,62 − 0,133145 × 6.272,73 = 143,44
IRRF DEVIDO = 525,08 − 143,44 = 381,64
Comparativo simplificado: (6.272,73 − 607,20) → IR 649,29 − 143,44 = 505,85 → usar deduções legais

Recolhimento: código 0561 — até 20/MM+1 (antecipar se não for dia útil)
```
**b) Planilha** com a memória (ver "Formato de entrega").
**c) Comparativo** deduções legais × simplificado, sempre com tabela, redutor e IRRF devido em linhas separadas.
**d) Aviso de não incidência** quando houver aviso prévio indenizado, férias indenizadas ou multa do FGTS.
**e) Checklist**
```
[ ] Tabela, desconto simplificado (607,20) e redutor de 2026 aplicados
[ ] Redutor calculado sobre o rendimento BRUTO (não sobre a base)
[ ] Dependentes com declaração assinada do empregado
[ ] Pensão judicial com decisão ou acordo homologado
[ ] Natureza do rendimento correta (salário, autônomo, aluguel, 13º, PLR)
[ ] eSocial S-1210 / EFD-Reinf série R-4000 e DCTFWeb batendo
[ ] Comprovante de rendimentos entregue até o último dia útil de fevereiro
```
A DIRF foi extinta para fatos a partir de 2025: as informações vão para o eSocial e a EFD-Reinf. DIRF só para retificar anos anteriores.

## Erros comuns / pontos de atenção
- Usar o desconto simplificado antigo (564,80) ou somá-lo às deduções legais (ele substitui todas).
- Esquecer o redutor de 2026 ou aplicá-lo sobre a base em vez do bruto.
- Calcular INSS com alíquota cheia sobre o total (é progressivo, faixa a faixa).
- Tributar o 13º junto com o salário do mês.
- Esquecer dependentes declarados pelo empregado.
- Não reter IR de autônomo ("ele acerta na declaração").
- Esquecer a retenção sobre aluguel pago a PF.
- Reter IR sobre aviso prévio indenizado, férias indenizadas ou multa do FGTS.

### Casos de borda
- **Duas fontes pagadoras**: cada uma calcula o seu IRRF; o acerto é na declaração anual.
- **Pensão alimentícia recebida**: o STF afastou o IR sobre pensão alimentícia decorrente do direito de família (ADI 5.422, 2022). Não é caso de carnê-leão.
- **Pró-labore acima do teto do INSS**: INSS para no teto; o IR segue a tabela; acima de R$ 7.350,00 não há redutor.
- **PLR** (Lei nº 10.101/2000): tabela exclusiva anual, tributação separada (código 3562).
- **Stock options**: o STJ fixou (Tema 1.226, 2024) que os planos têm natureza mercantil; o IR incide só como **ganho de capital** na venda das ações, não no exercício da opção. A RFB e o CARF ainda divergem em alguns casos — avaliar o risco.

### Quando escalar
- Folha completa → `folha-pagamento-mensal`; rescisão → `rescisao-clt-calculo`.
- DCTFWeb → `dctfweb`; cruzamentos → `revisao-fiscal-cruzamento-sped`.

## Perguntas que o usuário costuma fazer
- **"Quem ganha R$ 5.000,00 não paga mais IR?"** Na fonte, em 2026, quem tem rendimento tributável mensal de até R$ 5.000,00 fica com IRRF zero por causa do redutor. A tabela continua a mesma.
- **"O redutor é sobre o salário líquido?"** Não. É sobre o rendimento tributável bruto do mês.
- **"Vale a pena o desconto simplificado?"** Calcule os dois; normalmente compensa para quem tem poucas deduções.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei nº 7.713/1988, arts. 6º, V (isenções na rescisão e FGTS) e 7º (retenção na fonte).
- Lei nº 9.250/1995, art. 4º (deduções: dependentes, pensão, previdência), art. 3º-A (redutor mensal, inclusive no 13º — §3º) e art. 11-A (redução anual), incluídos pela Lei nº 15.270/2025.
- Lei nº 15.191/2025 — tabela mensal vigente desde maio/2025 e desconto simplificado.
- Lei nº 15.270/2025 — redutor do IRRF a partir de 2026 e regras anuais.
- Lei nº 11.196/2005, art. 70, I, "b" (JCP) e "e" (demais rendimentos) — prazo de recolhimento do IRRF.
- Decreto nº 9.580/2018 (RIR/2018) — regulamento do imposto de renda; art. 42 (exclusões do rendimento de aluguel).
- Lei nº 9.249/1995, art. 9º, §2º (JCP a 17,5%, redação da LC nº 224/2025).
- Lei nº 10.101/2000 — PLR.
- Portaria Interministerial MPS/MF nº 13/2026 — tabela do INSS 2026.
- IN RFB nº 2.248/2025 — prazo da DCTFWeb.
- STJ, Súmulas 125, 386 e 463; STJ, Tema 1.226 (stock options); STF, ADI 5.422 (pensão alimentícia).
- Receita Federal, página "Tributação de 2026" (tabelas mensais e de redução).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
