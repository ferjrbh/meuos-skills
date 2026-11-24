---
name: ferias-13-salario
description: "Especialista em férias e 13º salário com os parâmetros de 2026 — período aquisitivo e concessivo, dias de direito por faltas (art. 130 da CLT), fracionamento em até 3 períodos, abono pecuniário (venda de 1/3, isento de INSS, IRRF e FGTS; com abono o empregado goza 20 dias), 1/3 constitucional, médias de variáveis, pagamento 2 dias antes, férias em dobro; 13º com 1ª parcela até 30/11 (sem INSS e IRRF, com FGTS) e 2ª até 20/12 (INSS e IRRF sobre o total, IRRF exclusivo com redutor da Lei nº 15.270/2025). Use quando o usuário calcula férias ou 13º, ou fala em aviso de férias, abono pecuniário, médias, 13º proporcional, provisão. Entrega: cálculo passo a passo + recibo de férias ou holerite do 13º + guias."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Férias e 13º Salário

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Calcula férias (com ou sem abono) e 13º salário com as tabelas de 2026, mostra o que tem e o que não tem INSS, IRRF e FGTS, monta o recibo de férias e o holerite do 13º e lista prazos e eventos do eSocial.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Férias individuais ou coletivas, abono pecuniário, férias vencendo em dobro.
- 1ª e 2ª parcelas do 13º, 13º proporcional.
- Férias e 13º na rescisão: use `rescisao-clt-calculo` (lá são indenizados, com outra incidência).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite. O código abaixo é exemplo de conferência: mostrar ao usuário antes de rodar.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Parâmetros 2026
```
INSS (Portaria Interministerial MPS/MF nº 13/2026), progressivo:
  até 1.621,00 = 7,5% | até 2.902,84 = 9% (−24,32) | até 4.354,27 = 12% (−111,40)
  | até 8.475,55 = 14% (−198,49) | desconto máximo 988,09
IRRF: tabela mensal inalterada (isento até 2.428,80; 7,5% −182,16; 15% −394,16;
  22,5% −675,49; 27,5% −908,73); dependente 189,59; desconto simplificado 607,20
  (usar o que der menor imposto)
REDUTOR (Lei nº 15.270/2025), pelo rendimento bruto: até 5.000,00 zera;
  5.000,01 a 7.350,00 reduz 978,62 − 0,133145 × rendimento; acima de 7.350,00 não reduz
  · 13º: o redutor se aplica ao IRRF exclusivo do 13º, calculado à parte
  · Férias pagas em recibo separado: a aplicação do redutor é decisão do contador
    responsável. Mostrar SEMPRE o cálculo com e sem redutor.
  · REGRA DE USO: toda vez que calcular férias, PERGUNTAR ao contador "Aplico o redutor
    da Lei nº 15.270/2025 sobre estas férias? (sim/não)" ANTES de fechar o IRRF e o recibo.
    Não decidir sozinho; registrar no memorial a resposta e quem confirmou.
```

### 2. Férias — regras
```
DIAS DE DIREITO POR FALTAS INJUSTIFICADAS NO AQUISITIVO (art. 130 da CLT)
até 5 = 30 dias | 6 a 14 = 24 | 15 a 23 = 18 | 24 a 32 = 12 | mais de 32 = perde

PRAZOS
Aviso de férias: 30 dias antes, por escrito (art. 135 da CLT)
Pagamento: até 2 dias antes do início (art. 145 da CLT)
Concessão: nos 12 meses seguintes ao aquisitivo; fora disso, pagar em dobro (art. 137)
Fracionamento: até 3 períodos, um com no mínimo 14 dias e os outros com no mínimo
  5 dias cada (art. 134, § 1º); início não pode cair nos 2 dias antes de feriado ou DSR (§ 3º)

VALOR
Férias = (salário + média das variáveis habituais) × dias GOZADOS / 30
+ 1/3 constitucional (art. 7º, XVII, da Constituição)
Abono pecuniário (art. 143 da CLT): venda de 1/3 dos dias de direito (10 se o
  direito é 30) + 1/3 sobre o abono; pedido até 15 dias antes do fim do aquisitivo.
  COM ABONO, OS DIAS GOZADOS CAEM: 30 de direito = 20 gozados + 10 vendidos.

INCIDÊNCIAS
Férias gozadas + 1/3 ......... INSS sim | IRRF sim | FGTS sim
  (INSS sobre o 1/3: legítimo — Tema 985 do STF, RE 1.072.485, efeitos desde 15/09/2020)
Abono pecuniário + 1/3 ....... INSS não | IRRF não | FGTS não
  (INSS e FGTS: art. 28, § 9º, "e", 6, da Lei nº 8.212/1991; IRRF do abono:
  IN RFB nº 936/2009. O 1/3 sobre o abono é tratado como isento por critério adotado —
  ver o risco no recibo de exemplo, item 6.)
IRRF das férias: apurado no próprio recibo, em separado do salário do mês
```

### 3. 13º salário — regras
```
1ª parcela: até 30/11 — metade da remuneração do mês anterior; SEM INSS e SEM IRRF;
  COM FGTS (entra na folha do mês do pagamento: paga em novembro, FGTS até 20/12).
  Pode ser paga com as
  férias, se o empregado pedir em janeiro (art. 2º, § 2º, da Lei nº 4.749/1965).
2ª parcela: até 20/12 — total do 13º menos a 1ª parcela, menos INSS e IRRF calculados
  sobre o TOTAL.
Avos: 1/12 por mês com 15 dias ou mais trabalhados (Lei nº 4.090/1962).
Médias: variáveis habituais integram (art. 2º do Decreto nº 57.155/1965).
INSS do 13º: em separado do salário de dezembro, com teto próprio; recolhimento até 20/12
  (antecipa se não houver expediente bancário — art. 216, § 1º, do Decreto nº 3.048/1999);
  folha anual no eSocial (S-1200 e S-1299 anuais) e DCTFWeb anual até 20/12.
FGTS da folha anual (2ª parcela): vence em 20/01 do ano seguinte; desligamento em
  dezembro antecipa para o prazo rescisório (Nota Orientativa FGTS Digital nº 11/2025).
IRRF do 13º: tributação exclusiva na fonte, em separado, com redutor da Lei nº 15.270/2025;
  código 0561, declarado no eSocial (S-1210) e na DCTFWeb; vencimento dia 20 do mês
  seguinte ao pagamento.
Desoneração em transição (2026): a parcela de 10% sobre a folha não incide sobre o 13º.
```

### 4. Entrevista mínima
```
Q1: Empregado (matrícula) + período aquisitivo + faltas injustificadas?
Q2: Salário do mês + média das variáveis (HE, comissões, adicionais) dos últimos 12 meses?
Q3: Quantos dias de direito? Pediu abono? Vai fracionar?
Q4: Houve afastamento no aquisitivo (art. 133 da CLT)?
Q5 (13º): quantos avos? Já pagou a 1ª parcela? Dependentes para IRRF?
```

### 5. Cálculo (exemplo para conferência)
```python
# Exemplo de conferência — parâmetros 2026. Mostrar ao usuário antes de rodar.
def inss_2026(b):
    if b <= 1621.00: v = b * 0.075
    elif b <= 2902.84: v = b * 0.09 - 24.32
    elif b <= 4354.27: v = b * 0.12 - 111.40
    elif b <= 8475.55: v = b * 0.14 - 198.49
    else: v = 988.09
    return round(v, 2)

def irrf_tabela(base):
    if base <= 2428.80: return 0.0
    if base <= 2826.65: return round(base * 0.075 - 182.16, 2)
    if base <= 3751.05: return round(base * 0.15 - 394.16, 2)
    if base <= 4664.68: return round(base * 0.225 - 675.49, 2)
    return round(base * 0.275 - 908.73, 2)

def irrf_2026(bruto, inss, dependentes=0):
    # base: o MENOR entre deduções legais e desconto simplificado (607,20)
    base = min(round(bruto - inss - dependentes * 189.59, 2), round(bruto - 607.20, 2))
    ir = irrf_tabela(base)
    if bruto <= 5000: red = ir                                   # redutor Lei 15.270/2025
    elif bruto <= 7350: red = min(max(978.62 - 0.133145 * bruto, 0), ir)
    else: red = 0.0
    return ir, round(ir - red, 2)                                # (sem redutor, com redutor)

def ferias(salario, media=0, dias_direito=30, abono=False, dependentes=0):
    base_mes = salario + media
    dias_abono = dias_direito / 3 if abono else 0                # art. 143 da CLT
    dias_gozo = dias_direito - dias_abono                        # com abono goza menos
    valor = round(base_mes * dias_gozo / 30, 2); terco = round(valor / 3, 2)
    abono_v = round(base_mes * dias_abono / 30, 2); terco_ab = round(abono_v / 3, 2)
    tributavel = valor + terco                                   # abono e seu 1/3: isentos
    inss = inss_2026(tributavel)
    ir_sem, ir_com = irrf_2026(tributavel, inss, dependentes)
    bruto = round(valor + terco + abono_v + terco_ab, 2)
    return dict(dias_gozo=dias_gozo, valor=valor, terco=terco, abono=abono_v,
                terco_abono=terco_ab, bruto=bruto, inss=inss, irrf_sem_redutor=ir_sem,
                irrf_com_redutor=ir_com, liquido_com_redutor=round(bruto - inss - ir_com, 2),
                fgts=round(tributavel * 0.08, 2))

def decimo_terceiro(salario, media, avos, parcela1, dependentes=0):
    total = round((salario + media) * avos / 12, 2)
    inss = inss_2026(total)                                      # sobre o TOTAL
    ir_sem, ir_com = irrf_2026(total, inss, dependentes)         # redutor também no 13º
    return dict(total=total, inss=inss, irrf=ir_com,
                liquido_2a=round(total - parcela1 - inss - ir_com, 2))

print(ferias(5000, 800, 30, True))
print(decimo_terceiro(5000, 800, 12, 2900))
```

### 6. Entregável
**a) Recibo de férias** (exemplo: salário 5.000,00 + média de HE 800,00; 30 dias de direito; vende 10)
```
FÉRIAS — Empregado (matrícula) __  Aquisitivo __  Gozo __/__ a __/__
Direito: 30 dias  Gozo: 20 dias  Abono: 10 dias   Base: 5.800,00

Férias (20 dias gozados) .............. 3.866,67
+ 1/3 constitucional .................. 1.288,89
+ Abono pecuniário (10 dias) .......... 1.933,33
+ 1/3 sobre o abono ...................   644,44
                                       ─────────
BRUTO ................................. 7.733,33

(−) INSS sobre férias + 1/3 (5.155,56) .........   523,29
(−) IRRF sobre férias + 1/3 (base simplificada 4.548,36):
      tabela .................................   347,89
      com redutor Lei nº 15.270/2025 (−292,18) ..    55,71   (só se o contador confirmar)
(−) Abono e 1/3 do abono: tratados como isentos (critério adotado nesta skill).
    Risco conhecido: a Receita Federal, na Solução de Consulta Cosit nº 209/2021, entende
    que o 1/3 sobre o abono pago no curso do contrato é tributável pelo IRRF. Informar o
    contador desse risco antes de fechar o recibo.

LÍQUIDO com redutor ................... 7.154,33
LÍQUIDO sem redutor ................... 6.862,15
FGTS (8% × 5.155,56) ..................   412,44
Pagamento: até 2 dias antes do início (art. 145 da CLT)
```
**b) Holerite do 13º — 2ª parcela** (salário 5.000,00 + média 800,00; 12/12; sem dependentes)
```
Total do 13º: 5.800,00   1ª parcela paga em novembro: 2.900,00
INSS sobre o total (5.800 × 14% − 198,49) .......... 613,51
IRRF: base 5.186,49 (deduções legais < simplificado) → tabela 517,55
      − redutor 206,38 = 311,17
Líquido da 2ª parcela: 2.900,00 − 613,51 − 311,17 = 1.975,32
FGTS: 232,00 (1ª parcela, na folha de novembro, até 20/12) + 232,00 (folha anual, até 20/01) = 464,00
```
**c) eSocial:** férias no S-2230 com motivo 15 (gozo de férias) — envio obrigatório para empregados (categorias 1XX), até o dia 15 do mês seguinte; pode ser enviado com até 60 dias de antecedência do início (MOS S-1.3); pagamento das férias no S-1200/S-1210 da competência; 13º na folha anual (S-1200 com apuração anual + S-1299 anual).
**d) Checklist**
```
FÉRIAS
[ ] Aviso entregue 30 dias antes
[ ] Dias de direito conferidos (faltas e art. 133)
[ ] Médias de variáveis calculadas
[ ] Abono: pedido no prazo; dias gozados reduzidos
[ ] Pagamento 2 dias antes do início
[ ] Concessivo vencendo? (risco de dobra)
[ ] FGTS sobre férias gozadas + 1/3

13º
[ ] 1ª parcela até 30/11 + FGTS no mês seguinte
[ ] 2ª parcela até 20/12, INSS e IRRF sobre o total, com redutor
[ ] FGTS da 2ª parcela
[ ] Folha anual no eSocial fechada
```

## Erros comuns / pontos de atenção
- Pagar 30 dias de férias e mais 10 de abono (com abono, goza 20).
- INSS ou IRRF sobre o abono pecuniário (isento).
- Não comparar desconto simplificado com deduções legais no IRRF.
- Recolher o FGTS da 1ª parcela do 13º só junto com a 2ª.
- Tirar o 1/3 de férias gozadas da base do INSS (Tema 985 do STF: incide).
- Esquecer as médias de HE e comissões.
- Pagar as férias junto com a folha (o prazo é 2 dias antes do início).

## Casos especiais
- **Afastamento (art. 133 da CLT):** perde o direito ao período quem, no aquisitivo, recebeu do INSS auxílio-doença OU benefício de acidente do trabalho por mais de 6 meses, mesmo descontínuos (inciso IV), ou teve licença remunerada ou paralisação da empresa por mais de 30 dias (incisos II e III). Novo aquisitivo começa no retorno (§ 2º). Afastamento por acidente do trabalho ou por doença atestada pelo INSS, quando não passar dos 6 meses do art. 133, IV, não conta como falta (art. 131, III).
- **Estudante menor de 18 anos:** pode fazer coincidir as férias com as férias escolares (art. 136, § 2º, da CLT).
- **Férias coletivas (arts. 139 a 141 da CLT):** até 2 períodos por ano, nenhum menor que 10 dias; comunicação ao órgão local do MTE e ao sindicato com 15 dias de antecedência (art. 139, §§ 2º e 3º) — ME e EPP estão dispensadas só da comunicação ao MTE (art. 51, V, da LC nº 123/2006); a comunicação ao sindicato continua.
- **Contratado no meio do ano:** 13º proporcional aos avos.

## Quando escalar
- Folha mensal com férias ou 13º → `folha-pagamento-mensal`
- IRRF detalhado → `calculo-irrf-folha`
- Rescisão com férias e 13º → `rescisao-clt-calculo`
- eSocial → `esocial-afastamentos` / `esocial-eventos-periodicos`

## Perguntas que o usuário costuma fazer
- **"A 1ª parcela do 13º tem FGTS?"** Sim: entra na folha do mês do pagamento e vence no dia 20 do mês seguinte.
- **"O redutor de R$ 5 mil vale para o 13º?"** Sim, aplicado ao 13º separadamente. Para férias pagas em recibo separado, perguntar ao contador se aplica, mostrando o cálculo com e sem redutor.

## Base legal usada nesta skill
- Constituição Federal — art. 7º, VIII (13º) e XVII (1/3 de férias).
- CLT (Decreto-Lei nº 5.452/1943) — arts. 129 a 145 (férias), em especial 130, 131, 133, 134, 135, 136, 137, 139, 143 e 145.
- Lei nº 4.090/1962 e Lei nº 4.749/1965 — 13º salário.
- Decreto nº 57.155/1965 — regulamento do 13º (médias).
- Lei nº 8.212/1991 — art. 28, § 9º, "e", 6 (abono fora da base do INSS).
- IN RFB nº 936/2009 — IRRF sobre abono pecuniário; Solução de Consulta Cosit nº 209/2021 — entendimento da Receita sobre o 1/3 do abono (risco).
- Decreto nº 3.048/1999 — art. 216, § 1º (INSS do 13º até 20/12); IN RFB nº 2.237/2024 — DCTFWeb anual do 13º.
- Nota Orientativa FGTS Digital nº 11/2025 (SIT/MTE) — FGTS do 13º.
- Manual de Orientação do eSocial (MOS) S-1.3 — S-2230 (férias, motivo 15) e folha anual.
- STF, Tema 985 (RE 1.072.485) — INSS sobre o 1/3 de férias gozadas.
- Lei nº 15.270/2025 — redutor do IRRF.
- Portaria Interministerial MPS/MF nº 13/2026 — tabela do INSS.
- LC nº 123/2006 — art. 51, V (férias coletivas ME/EPP).
- Lei nº 14.973/2024 — desoneração em transição (13º fora da parcela sobre a folha).

## Formato de entrega
- Cálculos, apurações e conciliações: entregar SEMPRE planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar SEMPRE documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima neste documento (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
