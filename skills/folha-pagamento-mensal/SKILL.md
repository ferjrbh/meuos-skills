---
name: folha-pagamento-mensal
description: "Especialista em folha CLT mensal com parâmetros de 2026 — salário-base, horas extras, DSR sobre variáveis, adicional noturno com hora reduzida, periculosidade ou insalubridade (não cumulam), faltas e reflexo no DSR; descontos de INSS progressivo (teto 8.475,55; máximo 988,09), IRRF com desconto simplificado de 607,20 ou deduções e redutor da Lei nº 15.270/2025, vale-transporte até 6%, plano de saúde; FGTS 8% (aprendiz 2%) com vencimento no dia 20; CCT/ACT e banco de horas. Use quando o usuário fecha a folha do mês ou fala em holerite, INSS, IRRF, dissídio, periculosidade, insalubridade, hora noturna, banco de horas. Entrega: holerite por empregado + tabela consolidada + memória de cálculo + checklist."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Folha de Pagamento Mensal (CLT)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Calcula a folha mensal de cada empregado (proventos, descontos e líquido), com as tabelas de 2026, e entrega o holerite, a tabela consolidada do mês, a memória de cálculo e o checklist de fechamento.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Fechamento da folha do mês.
- Conferência de holerite gerado pelo sistema.
- Para apenas conferir uma folha pronta (sem recalcular), use `analisar-folha-pagamento`.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Arquivos de memória de cálculo ficam na pasta do cliente, nunca em pasta temporária compartilhada.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite. O código abaixo é exemplo de conferência: mostrar ao usuário antes de rodar.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Tabelas 2026
```
INSS DO EMPREGADO (Portaria Interministerial MPS/MF nº 13/2026) — progressivo
Faixa                      Alíquota   Parcela a deduzir (atalho)
até 1.621,00                 7,5%         0,00
1.621,01 a 2.902,84          9,0%        24,32
2.902,85 a 4.354,27         12,0%       111,40
4.354,28 a 8.475,55         14,0%       198,49
Teto: 8.475,55 | desconto máximo: 988,09
Atalho: salário de contribuição × alíquota da faixa − parcela a deduzir (dá o mesmo
resultado do cálculo faixa a faixa).

IRRF MENSAL (tabela inalterada desde maio/2025)
até 2.428,80 isento | até 2.826,65 7,5% (−182,16) | até 3.751,05 15% (−394,16)
| até 4.664,68 22,5% (−675,49) | acima 27,5% (−908,73)
Base: rendimento − INSS − 189,59 por dependente − pensão judicial
   OU rendimento − desconto simplificado de 607,20 → usar a que der MENOR imposto.
REDUTOR (Lei nº 15.270/2025), depois da tabela, pelo rendimento BRUTO tributável:
até 5.000,00 → imposto zero | 5.000,01 a 7.350,00 → reduz 978,62 − 0,133145 × rendimento
| acima de 7.350,00 → sem redução (nunca gera imposto negativo)

SALÁRIO MÍNIMO 2026: R$ 1.621,00 (Decreto nº 12.797/2025) — base da insalubridade
```

### 2. Entrevista mínima
```
Q1: Empresa + competência + cadastro (salários, jornadas, dependentes, CCT/ACT)?
Q2: Frequência: dias trabalhados, faltas, atestados, HE 50%/100%, horas noturnas?
Q3: Variáveis: comissões, prêmios, gratificações, PLR?
Q4: Adiantamento pago no mês? Pensão judicial? Plano de saúde/coparticipação?
Q5: Reajuste da CCT aplicado? Banco de horas com saldo?
Q6: Calendário do mês: dias úteis e domingos/feriados (para o DSR)?
```

### 3. Cálculo (exemplo para conferência)
```python
# Exemplo de conferência — parâmetros 2026. Mostrar ao usuário antes de rodar.
def inss_2026(b):
    if b <= 1621.00: v = b * 0.075
    elif b <= 2902.84: v = b * 0.09 - 24.32
    elif b <= 4354.27: v = b * 0.12 - 111.40
    elif b <= 8475.55: v = b * 0.14 - 198.49
    else: v = 988.09                                   # teto 2026
    return round(v, 2)

def irrf_tabela(base):
    if base <= 2428.80: return 0.0
    if base <= 2826.65: return round(base * 0.075 - 182.16, 2)
    if base <= 3751.05: return round(base * 0.15 - 394.16, 2)
    if base <= 4664.68: return round(base * 0.225 - 675.49, 2)
    return round(base * 0.275 - 908.73, 2)

def folha(salario, he50_h=0, he100_h=0, divisor=220, dias_uteis=25, dias_dsr=5,
          adic_noturno=0.0, peric=False, insal_pct=0.0, dependentes=0, pensao=0.0,
          custo_vt=None, outros_descontos=0.0):
    hora = salario / divisor
    he = round(he50_h * hora * 1.5 + he100_h * hora * 2.0, 2)
    dsr = round((he + adic_noturno) / dias_uteis * dias_dsr, 2)   # DSR sobre variáveis (Súmula 172 TST)
    peric_v = round(salario * 0.30, 2) if peric else 0.0          # art. 193, § 1º, CLT
    insal_v = round(1621.00 * insal_pct, 2)                       # 10/20/40% do salário mínimo (art. 192)
    adicional = max(peric_v, insal_v)                             # não cumulam (art. 193, § 2º)
    bruto = round(salario + he + dsr + adic_noturno + adicional, 2)
    inss = inss_2026(bruto)
    base = min(round(bruto - inss - dependentes * 189.59 - pensao, 2), round(bruto - 607.20, 2))
    ir = irrf_tabela(base)
    if bruto <= 5000: red = ir                                    # redutor Lei 15.270/2025
    elif bruto <= 7350: red = min(max(978.62 - 0.133145 * bruto, 0), ir)
    else: red = 0.0
    irrf = round(ir - red, 2)
    vt = round(salario * 0.06, 2) if custo_vt is None else round(min(salario * 0.06, custo_vt), 2)
    descontos = round(inss + irrf + vt + pensao + outros_descontos, 2)
    return dict(he=he, dsr=dsr, bruto=bruto, inss=inss, base_ir=base, ir_tabela=ir,
                redutor=round(red, 2), irrf=irrf, vt=vt, descontos=descontos,
                liquido=round(bruto - descontos, 2), fgts=round(bruto * 0.08, 2))

# Exemplo: salário 5.000; 10 h extras a 50%; mês com 25 dias úteis e 5 domingos/feriados;
# sem dependentes; VT 6% (custo real maior); plano de saúde 80,00
print(folha(5000, he50_h=10, outros_descontos=80.00))
```

### 4. Regras críticas
- **Hora noturna (art. 73 da CLT):** das 22h às 5h no urbano; hora reduzida de 52min30s; adicional mínimo de 20% (CCT pode ser maior).
- **DSR sobre variáveis:** HE e adicional noturno habituais refletem no DSR (Súmula 172 do TST; Lei nº 605/1949); adicional noturno habitual integra o salário (Súmula 60 do TST).
- **Faltas injustificadas:** descontam o dia e, se houver falta na semana, também o DSR (art. 6º da Lei nº 605/1949).
- **Vale-transporte (Lei nº 7.418/1985):** desconto de até 6% do salário-base, limitado ao custo real; nunca sobre HE ou adicionais.
- **Periculosidade × insalubridade:** não cumulam; o empregado escolhe a mais vantajosa (art. 193, § 2º, da CLT). Insalubridade sobre o salário mínimo, salvo base maior na CCT.
- **Aprendiz:** FGTS de 2% (art. 15, § 7º, da Lei nº 8.036/1990).
- **Doméstico:** FGTS 8% + 3,2% (LC nº 150/2015), pelo eSocial Doméstico.
- **Banco de horas (art. 59 da CLT):** por acordo individual escrito, compensação em até 6 meses (§ 5º); por acordo ou convenção coletiva, até 1 ano (§ 2º). Não compensado no prazo: pagar como HE.
- **Pensão alimentícia judicial:** desconta do líquido e deduz integralmente da base do IRRF (art. 4º, II, da Lei nº 9.250/1995).

### 5. Entregável
**a) Holerite por empregado** (resultado do exemplo acima)
```
EMPRESA EXEMPLO LTDA — CNPJ 00.000.000/0001-00 — Competência __/____
EMPREGADO (matrícula) __ Cargo __ Salário R$ 5.000,00

PROVENTOS                              DESCONTOS
Salário base ............ 5.000,00     INSS ..................... 558,78
HE 50% (10 h) ...........   340,91     IRRF .....................  153,36
DSR sobre HE ............    68,18     Vale-transporte (6%) .....  300,00
                                       Plano de saúde ...........   80,00
                         ─────────                               ─────────
TOTAL PROVENTOS ......... 5.409,09     TOTAL DESCONTOS ......... 1.092,14

LÍQUIDO A RECEBER: R$ 4.316,95
Base INSS 5.409,09 | Base IRRF 4.801,89 (simplificado) | IR tabela 411,79 − redutor 258,43
Base FGTS 5.409,09 | FGTS do mês (empregador) 432,73
```
**b) Tabela consolidada do mês**
```
Empregado | Bruto | INSS | IRRF | VT | Outros | Líquido | FGTS
TOTAIS    |  __   |  __  |  __  | __ |   __   |   __    |  __
```
**c) Memória de cálculo** em planilha na pasta do cliente.
**d) Guias:** INSS (DARF da DCTFWeb, dia 20), IRRF código 0561 (DARF da DCTFWeb, dia 20 do mês seguinte), FGTS (FGTS Digital, dia 20). DCTFWeb transmitida até o último dia útil do mês seguinte.
**e) Checklist (8 itens)**
```
[ ] Frequência conferida (ponto, atestados, banco de horas)
[ ] CCT/ACT aplicada (piso, reajuste, adicionais)
[ ] HE, DSR sobre variáveis e hora noturna reduzida corretos
[ ] INSS progressivo 2026
[ ] IRRF: simplificado × deduções + redutor Lei nº 15.270/2025
[ ] FGTS recolhido até o dia 20 (FGTS Digital)
[ ] Holerite entregue
[ ] eSocial S-1200/S-1210 transmitidos (skill esocial-eventos-periodicos)
```

## Erros comuns / pontos de atenção
- INSS com alíquota única sobre o total (é progressivo).
- IRRF sem comparar o desconto simplificado ou sem o redutor (em 2026, quem ganha até 5.000,00 não tem IRRF).
- DSR sobre HE esquecido ou calculado com divisor fixo (usar os dias úteis e de descanso do mês).
- CCT/reajuste não aplicado.
- VT de 6% "cego" quando o custo real é menor, ou sobre HE.
- Hora noturna sem a redução de 52min30s.
- Somar periculosidade com insalubridade.
- FGTS com vencimento no dia 7 (era da GFIP; agora é dia 20).

## Casos especiais
- **PLR (Lei nº 10.101/2000):** sem INSS e sem FGTS; IRRF por tabela exclusiva, separado da folha.
- **Empregado em férias no mês:** férias pagas 2 dias antes; a folha considera só os dias trabalhados.
- **13º:** 1ª parcela sem INSS e IRRF (com FGTS na folha do mês do pagamento); 2ª parcela com INSS e IRRF sobre o total, em separado, na folha anual (skill `ferias-13-salario`).
- **Vale-transporte custeado integralmente pela empresa:** verificar cláusula da CCT ou política interna.

## Quando escalar
- IRRF detalhado → `calculo-irrf-folha`
- INSS da empresa → `calculo-inss-empresa`
- eSocial → `esocial-eventos-periodicos`
- FGTS → `fgts-guia-recolhimento`
- Férias e 13º → `ferias-13-salario`
- Rescisão → `esocial-rescisao` + `rescisao-clt-calculo`
- Importação de variáveis no sistema de folha → seguir o leiaute de importação do próprio sistema (conferir a documentação do fornecedor antes de gerar o arquivo).

## Perguntas que o usuário costuma fazer
- **"Quem ganha 5.000,00 paga IR em 2026?"** Não: o redutor zera o imposto até 5.000,00 de rendimento.
- **"Posso descontar 6% de VT de todo mundo?"** Só até o custo real do transporte.

## Base legal usada nesta skill
- CLT (Decreto-Lei nº 5.452/1943) — art. 59 (HE e banco de horas), art. 73 (trabalho noturno), art. 192 (insalubridade), art. 193 (periculosidade).
- Lei nº 605/1949 — repouso semanal remunerado (art. 6º: faltas).
- Súmulas 60 e 172 do TST — adicional noturno e reflexo das HE no DSR.
- Portaria Interministerial MPS/MF nº 13/2026 — tabela do INSS 2026.
- Lei nº 15.270/2025 — redutor do IRRF.
- Lei nº 9.250/1995 — art. 4º (deduções da base do IRRF).
- Lei nº 8.036/1990 — art. 15 (FGTS 8%, aprendiz 2%, vencimento dia 20).
- Lei nº 7.418/1985 — vale-transporte.
- Lei nº 10.101/2000 — PLR.
- LC nº 150/2015 — doméstico.
- Decreto nº 12.797/2025 — salário mínimo 2026.
- IN RFB nº 2.248/2025 — prazo da DCTFWeb.

## Formato de entrega
- Cálculos, apurações e conciliações: entregar SEMPRE planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar SEMPRE documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima neste documento (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
