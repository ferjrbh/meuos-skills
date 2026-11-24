---
name: fgts-guia-recolhimento
description: "Especialista em FGTS mensal e rescisório pelo FGTS Digital — 8% sobre a remuneração (2% aprendiz; doméstico 8% + 3,2% de antecipação da multa, pelo DAE do eSocial Doméstico), vencimento no dia 20 do mês seguinte (Lei nº 14.438/2022), FGTS do 13º, guia rescisória (mês da rescisão + mês anterior não recolhido + aviso indenizado + 13º + multa de 40% ou 20%) em até 10 dias do término do contrato, pagamento por PIX, encargos por atraso (TR, juros de 0,5% ao mês e multa de 5% ou 10%), parcelamento e Certificado de Regularidade do FGTS (CRF). Use quando o usuário (a) recolhe FGTS do mês, (b) gera guia rescisória, (c) fala em FGTS atrasado, parcelamento, CRF, FGTS Digital, GRRF. Entrega: cálculo + guia mensal ou rescisória + vencimento + orientação da CRF."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# FGTS — Recolhimento Mensal e Rescisório (FGTS Digital)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Calcula o FGTS do mês e o FGTS rescisório, indica a guia certa no FGTS Digital e o vencimento, aponta o que entra e o que não entra na base e orienta sobre atraso, parcelamento e CRF.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Recolhimento mensal do FGTS (inclusive sobre o 13º).
- Rescisão: depósitos rescisórios e multa.
- FGTS em atraso, parcelamento, emissão de CRF para licitação ou financiamento.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e paga. O código abaixo é exemplo de conferência: mostrar ao usuário antes de rodar.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Tabela crítica (2026)
```
ALÍQUOTAS
Empregado em geral: 8% da remuneração (art. 15 da Lei nº 8.036/1990)
Aprendiz: 2% (art. 15, § 7º, da Lei nº 8.036/1990)
Doméstico: 8% + 3,2% de antecipação da indenização rescisória (arts. 21 e 22 da
  LC nº 150/2015), pagos no DAE do eSocial Doméstico (junto vão INSS e o seguro
  contra acidentes de 0,8%, que NÃO é FGTS — art. 34 da LC nº 150/2015)

ENTRA NA BASE: salário, HE, adicionais, comissões, DSR, 13º (1ª e 2ª parcelas),
  férias gozadas + 1/3, aviso prévio trabalhado e indenizado (Súmula 305 do TST),
  salário-maternidade, afastamento por acidente do trabalho e serviço militar
NÃO ENTRA (art. 15, § 6º, da Lei nº 8.036/1990, que remete ao art. 28, § 9º, da
  Lei nº 8.212/1991): vale-transporte, auxílio-alimentação (vedado em dinheiro),
  diárias de viagem, abono pecuniário de férias, férias indenizadas, PLR
  (Lei nº 10.101/2000), indenizações

VENCIMENTO MENSAL: até o dia 20 do mês seguinte; se não for dia útil, ANTECIPA
  (art. 15 da Lei nº 8.036/1990, redação da Lei nº 14.438/2022). O "dia 7" era da GFIP.
13º SALÁRIO: FGTS da 1ª parcela entra na folha do mês do pagamento (paga em novembro →
  vence 20/12); FGTS da folha anual (2ª parcela) vence em 20/01 do ano seguinte.
  Desligamento em dezembro: o FGTS do 13º passa a seguir o prazo rescisório.
  (Nota Orientativa FGTS Digital nº 11/2025)
VENCIMENTO RESCISÓRIO: em até 10 dias contados a partir do término do contrato (art. 18
  da Lei nº 8.036/1990 e art. 477, § 6º, da CLT). A guia inclui o mês da rescisão, o mês
  imediatamente anterior (se ainda não recolhido), o aviso indenizado, o 13º e a multa.
PAGAMENTO: guia do FGTS Digital, por PIX. Não se usa mais a GRRF do Conectividade Social.

MULTA RESCISÓRIA (sobre o saldo para fins rescisórios — art. 18 da Lei nº 8.036/1990)
40% — dispensa sem justa causa; rescisão indireta; encerramento (art. 18, § 1º)
20% — acordo do art. 484-A da CLT; culpa recíproca e força maior reconhecidas pela
      Justiça do Trabalho (art. 18, § 2º)
0%  — justa causa, pedido de demissão, término do contrato a termo, falecimento
(A contribuição adicional de 10% da LC nº 110/2001 foi extinta em 01/01/2020 — Lei nº 13.932/2019.)

ATRASO (art. 22 da Lei nº 8.036/1990)
Atualização pela TR, cobrada por dia de atraso (caput e § 2º)
+ juros de mora de 0,5% ao mês ou fração (§ 1º)
+ multa de 5% no mês do vencimento e de 10% a partir do mês seguinte (§ 2º-A)
O FGTS Digital calcula os encargos automaticamente na emissão da guia.
Débito em atraso deixa o CRF irregular.
```

### 2. Entrevista mínima
```
Q1: Empresa + competência + base do FGTS do mês por categoria (geral, aprendiz, doméstico)?
Q2: Houve 13º, férias, afastamentos ou rescisões no mês?
Q3: Rescisão: motivo + data + saldo para fins rescisórios (extrato do FGTS)? O FGTS do
    mês anterior já foi recolhido?
Q4: Há competências em atraso? Precisa de CRF?
```

### 3. Cálculo (exemplo para conferência)
```python
# Exemplo de conferência do FGTS (valores 2026). Mostrar ao usuário antes de rodar.
def fgts_mensal(base_geral, base_aprendiz=0.0):
    # base_geral: remunerações dos empregados em geral (8%)
    # base_aprendiz: remunerações dos aprendizes (2%)
    return round(base_geral * 0.08 + base_aprendiz * 0.02, 2)

def fgts_domestico(base):
    # Doméstico: 8% FGTS + 3,2% antecipação da multa (LC 150/2015), no DAE do eSocial Doméstico
    return round(base * 0.08, 2), round(base * 0.032, 2)

MULTA = {'sem_justa': 0.40, 'rescisao_indireta': 0.40, 'encerramento': 0.40,
         'acordo_484A': 0.20, 'culpa_reciproca': 0.20, 'forca_maior': 0.20,
         'justa_causa': 0.0, 'pedido': 0.0, 'termino_contrato': 0.0, 'falecimento': 0.0}

def guia_rescisoria(saldo_fins_rescisorios, dep_mes, dep_aviso, dep_13, motivo, dep_mes_anterior=0.0):
    # saldo_fins_rescisorios: extrato do FGTS (todos os depósitos do contrato, corrigidos)
    # dep_*: 8% sobre saldo de salário do mês, aviso indenizado e 13º da rescisão
    # dep_mes_anterior: FGTS do mês anterior ainda não recolhido (entra na guia rescisória)
    depositos = round(dep_mes + dep_aviso + dep_13 + dep_mes_anterior, 2)
    multa = round((saldo_fins_rescisorios + depositos) * MULTA[motivo], 2)
    return depositos, multa, round(depositos + multa, 2)

# Exemplo: sem justa causa; saldo 38.400,00; saldo de salário 2.900,00; aviso 10.440,00; 13º 2.416,67
d, m, t = guia_rescisoria(38400.00, 2900*0.08, 10440*0.08, 2416.67*0.08, 'sem_justa')
print(f'Depósitos rescisórios: {d:,.2f} | Multa: {m:,.2f} | Guia FGTS Digital: {t:,.2f}')
# Resultado esperado: 1.260,53 | 15.864,21 | 17.124,74
```

### 4. Entregável
**a) Cálculo mensal**
```
COMPETÊNCIA __/____ — Base FGTS: R$ __
Geral 8%: R$ __   Aprendizes 2%: R$ __   (Doméstico: DAE do eSocial Doméstico)
TOTAL: R$ __   Vencimento: 20/__/____ (antecipar se não for dia útil)
```
**b) Guia rescisória (FGTS Digital)**
```
Empregado (matrícula): __  Motivo: __  Desligamento: __/__/____
Saldo para fins rescisórios (extrato): R$ __
+ Depósito do mês anterior, se ainda não recolhido (8%): R$ __
+ Depósito do mês da rescisão (8%): R$ __
+ Depósito sobre aviso indenizado (8%): R$ __
+ Depósito sobre 13º da rescisão (8%): R$ __
= Base da multa: R$ __   × __% = Multa: R$ __
GUIA = depósitos rescisórios + multa: R$ __
Vencimento: 10 dias contados do término do contrato
```
**c) CRF:** emitida e consultada no site da CAIXA (consulta de regularidade do empregador). Conferir a data de validade impressa no próprio certificado e a autenticidade no site da CAIXA antes de entregar a licitação ou banco. Só sai regular sem débito em aberto.
**d) Parcelamento de FGTS em atraso:** pedido pelo FGTS Digital, nas condições da resolução do Conselho Curador do FGTS em vigor. Conferir no portal do FGTS Digital (gov.br/trabalho-e-emprego) o número de parcelas e as condições antes de simular para o cliente; não informar número de parcelas sem essa conferência.
**e) Checklist**
```
MENSAL
[ ] Base do FGTS conferida com o S-5003/S-5013
[ ] Aprendizes com 2%
[ ] 13º: FGTS da 1ª parcela na folha do mês do pagamento; da folha anual até 20/01
[ ] Guia paga até o dia 20 (antecipada se não for dia útil)

RESCISÓRIA
[ ] Saldo para fins rescisórios conferido no extrato
[ ] FGTS do mês anterior incluído, se ainda não recolhido
[ ] Multa conforme o motivo (40 / 20 / 0)
[ ] Guia paga em até 10 dias do término do contrato
[ ] S-2299 transmitido
```

## Erros comuns / pontos de atenção
- Usar o vencimento antigo do dia 7 (agora é dia 20).
- Achar que a 1ª parcela do 13º não tem FGTS (tem: entra na folha do mês do pagamento).
- Não recolher FGTS sobre aviso prévio indenizado.
- Aprendiz com 8% (correto: 2%).
- Calcular a multa só sobre os depósitos recentes (é sobre o saldo para fins rescisórios do contrato todo).
- Esquecer o FGTS do mês anterior ainda não recolhido na guia rescisória.
- Recolher FGTS no auxílio por incapacidade temporária comum a partir do 16º dia (não é devido) ou deixar de recolher no afastamento acidentário (é devido — art. 15, § 5º).
- Somar o 0,8% de seguro contra acidentes do doméstico como se fosse FGTS.

## Casos especiais
- **Empresa em recuperação judicial:** o FGTS em atraso continua exigível. Antes de propor parcelamento, conferir no FGTS Digital e na resolução vigente do Conselho Curador se há condição específica para empresas em recuperação judicial e como o plano de recuperação trata os créditos.
- **Simples Nacional (qualquer anexo):** o FGTS é sempre recolhido à parte, nunca no DAS.
- **Afastamentos:** doença comum a partir do 16º dia — sem FGTS; acidente do trabalho e serviço militar — com FGTS (art. 15, § 5º, da Lei nº 8.036/1990); licença-maternidade — com FGTS (art. 28, IV, do Decreto nº 99.684/1990).

## Quando escalar
- Cálculo completo da rescisão → `rescisao-clt-calculo`
- S-2299 → `esocial-rescisao`
- Folha mensal → `folha-pagamento-mensal`
- Débitos federais (não FGTS) → `parcelamento-receita-federal`

## Perguntas que o usuário costuma fazer
- **"O dia 20 caiu no sábado. Pago na segunda?"** Não: antecipa para a sexta (último dia útil antes).
- **"Desliguei dia 5; o FGTS do mês passado vence dia 20?"** Se ainda não foi recolhido, entra na guia rescisória e vence em 10 dias do término do contrato (art. 18 da Lei nº 8.036/1990).

## Base legal usada nesta skill
- Lei nº 8.036/1990 — art. 15 (depósito de 8%, vencimento dia 20; § 5º afastamentos; § 6º parcelas excluídas; § 7º aprendiz), art. 18 (depósitos rescisórios e multa de 40%/20%), art. 22 (encargos por atraso: TR, juros de 0,5% ao mês e multa de 5%/10%).
- Lei nº 14.438/2022 — vencimento no dia 20.
- Lei nº 13.932/2019 — extinção do adicional de 10% da LC nº 110/2001.
- LC nº 150/2015 — arts. 21, 22 e 34 (doméstico).
- Lei nº 8.212/1991 — art. 28, § 9º (parcelas fora da base).
- Decreto nº 99.684/1990 — regulamento do FGTS.
- CLT — art. 477, § 6º (prazo de 10 dias).
- Súmula 305 do TST — FGTS sobre aviso prévio indenizado.
- Nota Orientativa FGTS Digital nº 11/2025 (SIT/MTE, 09/12/2025) — FGTS do 13º e na rescisão.

## Formato de entrega
- Cálculos, apurações e conciliações: entregar SEMPRE planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar SEMPRE documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima neste documento (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
