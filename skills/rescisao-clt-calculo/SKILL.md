---
name: rescisao-clt-calculo
description: "Especialista no cálculo financeiro da rescisão CLT — verbas por modalidade (sem justa causa, justa causa, pedido, acordo do art. 484-A com multa de 20%, término de contrato a termo, culpa recíproca, rescisão indireta, falecimento), aviso prévio proporcional da Lei nº 12.506/2011 (30 dias + 3 por ano completo, até 90), projeção do aviso indenizado nos avos (Súmula 305 do TST), INSS e IRRF com as não incidências corretas (aviso indenizado — Tema 478 do STJ; férias indenizadas — Súmula 386 do STJ; multa do FGTS — art. 6º, V, da Lei nº 7.713/1988) e FGTS rescisório pelo FGTS Digital. Use quando precisar calcular TRCT ou conferir verbas rescisórias. NÃO transmite o evento ao eSocial (use `esocial-rescisao`)."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Rescisão CLT — Cálculo das Verbas

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Calcula as verbas rescisórias conforme a modalidade de desligamento, projeta o aviso prévio indenizado nos avos de 13º e férias, aplica INSS e IRRF só onde incidem e calcula a guia rescisória do FGTS Digital. Entrega o TRCT detalhado com memória de cálculo.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Cálculo ou conferência de TRCT.
- Simulação do custo de um desligamento.
- Para o evento S-2299 e o roteiro do desligamento, use `esocial-rescisao`.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite. O código abaixo é exemplo de conferência: mostrar ao usuário antes de rodar.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Justa causa, rescisão indireta e culpa recíproca dependem de avaliação jurídica (advogado com OAB); a skill só calcula o cenário informado.

## Passo a passo (instruções para o agente de IA)

### 1. Modalidade × verbas
```
Verba               SemJusta  Justa  Pedido  Acordo484A  TérminoTermo  CulpaRecíp  Falecim.
Saldo de salário      sim      sim    sim      sim          sim           sim        sim
Aviso prévio          sim      não    deve*    metade**     não           metade     não
Férias vencidas+1/3   sim      sim    sim      sim          sim           sim        sim
Férias prop.+1/3      sim      não    sim      sim          sim           metade     sim
13º proporcional      sim      não    sim      sim          sim           metade     sim
Multa FGTS            40%      0      0        20%          0             20%        0
Saque FGTS            sim      não    não      até 80%      sim           sim        dependentes
Seguro-desemprego     sim      não    não      não          não           não        não
*  No pedido, o aviso é obrigação do empregado (cumprir ou ter descontados 30 dias).
** No acordo, metade do aviso se indenizado (art. 484-A, I, "a", da CLT).
Rescisão indireta (art. 483) = mesmas verbas da sem justa causa (exige reconhecimento judicial).
Culpa recíproca: Súmula 14 do TST (exige reconhecimento judicial).
Justa causa: férias proporcionais indevidas (Súmula 171 do TST); vencidas sempre devidas.
Pedido de demissão: férias proporcionais devidas mesmo com menos de 1 ano (Súmula 261 do TST).
Contrato a termo encerrado antes do prazo: indenização dos arts. 479/480 da CLT, salvo cláusula
assecuratória (art. 481), quando valem as regras do prazo indeterminado.
```

### 2. Mapa de incidência
```
Verba                        INSS   IRRF   FGTS   Fundamento
Saldo de salário              sim    sim    sim   verba salarial
Aviso prévio indenizado       não    não    sim   INSS: Tema 478 do STJ (REsp 1.230.957/RS);
                                                  IRRF: art. 6º, V, da Lei nº 7.713/1988;
                                                  FGTS: Súmula 305 do TST
Férias indenizadas + 1/3      não    não    não   IRRF: Súmula 386 do STJ; INSS: art. 28,
                                                  § 9º, "d", da Lei nº 8.212/1991
13º proporcional              sim    sim    sim   INSS e IRRF apurados em separado do saldo
Multa de 40%/20% do FGTS      não    não    —     IRRF: art. 6º, V, da Lei nº 7.713/1988
Indenização art. 479          não    não    não   natureza indenizatória (posição conservadora no IRRF)
```
Ao fundamentar: a não incidência de IRRF sobre férias indenizadas é a Súmula 386 do STJ; a da multa do FGTS é o art. 6º, V, da Lei nº 7.713/1988.

### 3. Aviso prévio proporcional e projeção
- Lei nº 12.506/2011: 30 dias + 3 dias por ano completo de serviço, acréscimo máximo de 60 (total 90).
- O acréscimo beneficia só o empregado; no pedido de demissão, o empregado deve 30 dias.
- O aviso indenizado integra o tempo de serviço (art. 487, § 1º, da CLT; Súmula 305 do TST): projeta a data de saída e pode acrescentar avos de 13º e de férias.
- Exemplo: desligado em 30/04 com 60 dias de aviso indenizado → data projetada 29/06. O 13º vai a 6/12 (janeiro a junho; junho tem 29 dias, ≥ 15), não 4/12.
- Avo de 13º: mês civil com 15 dias ou mais. Avo de férias: cada fração de 15 dias ou mais contada a partir do aniversário do período aquisitivo (não do mês civil).

### 4. Entrevista mínima
```
Q1: Data de admissão + data do desligamento + modalidade?
Q2: Salário + média das variáveis habituais dos últimos 12 meses?
Q3: Aviso prévio trabalhado, indenizado ou dispensado?
Q4: Períodos de férias vencidas não gozadas?
Q5: Saldo do FGTS para fins rescisórios (extrato)?
Q6: Já pagou 1ª parcela do 13º no ano? Dependentes para IRRF? Estabilidade?
```

### 5. Cálculo (exemplo para conferência)
```python
# Exemplo de conferência — parâmetros 2026. Mostrar ao usuário antes de rodar.
from datetime import date, timedelta

def inss_2026(b):
    if b <= 1621.00: v = b * 0.075
    elif b <= 2902.84: v = b * 0.09 - 24.32
    elif b <= 4354.27: v = b * 0.12 - 111.40
    elif b <= 8475.55: v = b * 0.14 - 198.49
    else: v = 988.09
    return round(v, 2)

def irrf_2026(bruto, inss, dependentes=0):
    base = min(bruto - inss - dependentes * 189.59, bruto - 607.20)
    faixas = [(2428.80, 0, 0), (2826.65, .075, 182.16), (3751.05, .15, 394.16),
              (4664.68, .225, 675.49), (float('inf'), .275, 908.73)]
    for teto, aliq, ded in faixas:
        if base <= teto: ir = max(round(base * aliq - ded, 2), 0); break
    if bruto <= 5000: return 0.0                                  # redutor Lei 15.270/2025
    if bruto <= 7350: return round(max(ir - max(978.62 - 0.133145 * bruto, 0), 0), 2)
    return ir

def anos_completos(adm, dem):
    return dem.year - adm.year - ((dem.month, dem.day) < (adm.month, adm.day))

def avos_13(dem_projetada):
    # meses do ano com 15 dias ou mais (contrato iniciado antes de 1º/jan)
    return dem_projetada.month - 1 + (1 if dem_projetada.day >= 15 else 0)

def avos_ferias(inicio_aquisitivo, dem_projetada):
    avos, ini = 0, inicio_aquisitivo
    while True:
        m, a = (ini.month % 12) + 1, ini.year + (ini.month // 12)
        fim = date(a, m, min(ini.day, 28)) - timedelta(days=1)    # simplificação do dia
        if fim <= dem_projetada: avos, ini = avos + 1, fim + timedelta(days=1)
        else:
            if (dem_projetada - ini).days + 1 >= 15: avos += 1
            return min(avos, 12)

def rescisao_sem_justa(adm, dem, salario, media=0.0, saldo_fgts=0.0,
                       ferias_vencidas=1, inicio_aquisitivo=None):
    base = salario + media
    dias_aviso = 30 + min(anos_completos(adm, dem) * 3, 60)        # Lei 12.506/2011
    projetada = dem + timedelta(days=dias_aviso)                   # Súmula 305 TST
    saldo = round(base * dem.day / 30, 2)
    aviso = round(base * dias_aviso / 30, 2)
    fv = round(base * 4 / 3 * ferias_vencidas, 2)
    fp = round(base * avos_ferias(inicio_aquisitivo, projetada) / 12 * 4 / 3, 2)
    d13 = round(base * avos_13(projetada) / 12, 2)
    inss_s, inss_13 = inss_2026(saldo), inss_2026(d13)            # 13º em separado
    ir = irrf_2026(saldo, inss_s) + irrf_2026(d13, inss_13)
    bruto = round(saldo + aviso + fv + fp + d13, 2)
    dep = round((saldo + aviso + d13) * 0.08, 2)                   # FGTS rescisório
    multa = round((saldo_fgts + dep) * 0.40, 2)
    return dict(dias_aviso=dias_aviso, projetada=str(projetada), saldo=saldo, aviso=aviso,
                ferias_vencidas=fv, ferias_prop=fp, decimo=d13, bruto=bruto,
                inss=round(inss_s + inss_13, 2), irrf=round(ir, 2),
                liquido=round(bruto - inss_s - inss_13 - ir, 2),
                fgts_depositos=dep, multa_40=multa, guia_fgts=round(dep + multa, 2))

print(rescisao_sem_justa(date(2018, 3, 15), date(2026, 4, 15), 5000, 800, 38400,
                         ferias_vencidas=1, inicio_aquisitivo=date(2026, 3, 15)))
```

### 6. Entregável
**a) TRCT detalhado** (exemplo: admissão 15/03/2018, dispensa sem justa causa com aviso indenizado em 15/04/2026, salário 5.000,00 + média 800,00, 8 anos completos, 1 período de férias vencido, saldo do FGTS 38.400,00, sem 1ª parcela do 13º paga)
```
TRABALHADOR (matrícula) __  Adm 15/03/2018  Desligamento 15/04/2026  Motivo S-2299: 02
Aviso: 30 + 8 × 3 = 54 dias → data projetada 08/06/2026

VERBAS RESCISÓRIAS
Saldo de salário (15 dias) .................... 2.900,00
Aviso prévio indenizado (54 dias) ............ 10.440,00
Férias vencidas + 1/3 ......................... 7.733,33
Férias proporcionais 3/12 + 1/3 (aquisitivo
  a partir de 15/03/2026, com projeção) ....... 1.933,33
13º proporcional 5/12 (jan–mai, com projeção).. 2.416,67
                                              ──────────
BRUTO ........................................ 25.423,33

DESCONTOS
INSS sobre saldo (2.900,00) ...................   236,68
INSS sobre 13º, em separado (2.416,67) ........   193,18
IRRF (saldo e 13º até 5.000,00: redutor zera) .     0,00
(aviso, férias indenizadas e multa: sem INSS e sem IRRF)
                                              ──────────
LÍQUIDO DO TRCT .............................. 24.993,47

FGTS — GUIA RESCISÓRIA DO FGTS DIGITAL (fora do TRCT)
Depósito sobre saldo de salário (8%) ..........   232,00
Depósito sobre aviso indenizado (8%) ..........   835,20
Depósito sobre 13º (8%) .......................   193,33
Saldo para fins rescisórios (extrato) ........ 38.400,00
Base da multa (saldo + depósitos) ............ 39.660,53
Multa 40% .................................... 15.864,21
GUIA = 1.260,53 + 15.864,21 ................. 17.124,74
Prazo: pagamento do TRCT e da guia em até 10 dias do término (art. 477, § 6º, da CLT):
25/04/2026 cai em sábado — por segurança, pagar até sexta-feira, 24/04/2026
```
**b) Guias:** INSS e IRRF pela DCTFWeb (DARF, dia 20 do mês seguinte); FGTS pela guia rescisória do FGTS Digital (10 dias), que inclui também o FGTS do mês anterior se ainda não recolhido (art. 18 da Lei nº 8.036/1990).
**c) Comprovação do tempo de serviço** com a data projetada.
**d) Checklist**
```
[ ] Modalidade confirmada e documentada
[ ] Médias de variáveis dos últimos 12 meses
[ ] Aviso pela Lei nº 12.506/2011 e data projetada (Súmula 305)
[ ] Avos de 13º (mês civil) e de férias (aquisitivo) com projeção
[ ] Férias vencidas incluídas (todas as modalidades)
[ ] INSS e IRRF só sobre saldo e 13º (em separado); redutor da Lei nº 15.270/2025
[ ] Multa correta (40 / 20 / 0) sobre o saldo para fins rescisórios
[ ] Pagamento e guia FGTS em até 10 dias corridos
[ ] S-2299 (skill esocial-rescisao)
```

## Erros comuns / pontos de atenção
- Contar avos de férias pelo mês civil (o correto é pelo período aquisitivo).
- Não projetar o aviso indenizado nos avos.
- INSS ou IRRF sobre aviso indenizado, férias indenizadas ou multa do FGTS.
- Somar o 13º ao saldo de salário para calcular INSS/IRRF (são separados).
- Multa de 40% no acordo do art. 484-A (é 20%).
- Pagar a multa do FGTS no TRCT: ela vai na guia do FGTS Digital.
- Atraso no pagamento: multa de 1 salário (art. 477, § 8º, da CLT).
- Exigir homologação no sindicato: não é mais obrigatória (o § 1º do art. 477 foi revogado pela Lei nº 13.467/2017), salvo regra da CCT/ACT.

## Casos especiais
- **Estabilidade** (gestante, CIPA, acidentado, dirigente sindical): não dispensar sem justa causa; ver `esocial-rescisao`.
- **Reclamação trabalhista em curso:** pagar as verbas incontroversas e avaliar provisão da contingência (NBC TG 25).
- **Aposentadoria espontânea seguida de dispensa sem justa causa:** a aposentadoria não extingue o contrato; a multa de 40% incide sobre todos os depósitos do contrato (OJ 361 da SDI-1 do TST).
- **Férias vencidas em dobro:** se o período concessivo já venceu, as férias vencidas são pagas em dobro (art. 137 da CLT).

## Quando escalar
- S-2299 e roteiro → `esocial-rescisao`
- FGTS Digital → `fgts-guia-recolhimento`
- Discussão judicial → parceiro advogado com OAB (atividade privativa).

## Perguntas que o usuário costuma fazer
- **"Aviso indenizado tem INSS?"** Não (Tema 478 do STJ), mas tem FGTS (Súmula 305 do TST).
- **"No acordo, as férias também caem pela metade?"** Não: só o aviso indenizado e a multa do FGTS são pela metade.

## Base legal usada nesta skill
- CLT (Decreto-Lei nº 5.452/1943) — art. 137 (dobra), art. 477, §§ 6º e 8º (prazo e multa), arts. 479 a 481 (contrato a termo), art. 483 (rescisão indireta), art. 484 (culpa recíproca), art. 484-A (acordo), art. 487, § 1º (aviso integra o tempo de serviço).
- Lei nº 12.506/2011 — aviso prévio proporcional.
- Lei nº 8.036/1990 — art. 18 (depósitos rescisórios e multa).
- Lei nº 7.713/1988 — art. 6º, V (isenção de IR sobre aviso e indenizações rescisórias, inclusive a multa do FGTS).
- Lei nº 8.212/1991 — art. 28, § 9º, "d" (férias indenizadas fora do salário de contribuição).
- STJ — Tema 478 (REsp 1.230.957/RS) e Súmula 386.
- TST — Súmulas 14, 171, 261 e 305; OJ 361 da SDI-1.
- Lei nº 15.270/2025 — redutor do IRRF; Portaria Interministerial MPS/MF nº 13/2026 — INSS.

## Formato de entrega
- Cálculos, apurações e conciliações: entregar SEMPRE planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar SEMPRE documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima neste documento (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
