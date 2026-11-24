---
name: calculo-inss-empresa
description: "Calcula o INSS patronal mensal — CPP de 20%, RAT × FAP e Terceiros (5,8% típico) — e a contribuição das empresas na reoneração gradual da folha (Lei 14.973/2024: em 2026, 60% da alíquota da CPRB + 10% sobre a folha), atividades concomitantes e o Simples Anexo IV (CPP fora do DAS, sem Terceiros). Use quando o usuário tiver folha CLT ou disser \"INSS patronal\", \"CPP\", \"RAT\", \"FAP\", \"GILRAT\", \"Terceiros\", \"Sistema S\", \"CPRB\", \"desoneração da folha\", \"reoneração\", \"Anexo IV\", \"DCTFWeb INSS\", \"pró-labore INSS\". Entrega: cálculo passo a passo, comparativo CPRB × folha, guia com vencimento, memória e checklist."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Cálculo do INSS da empresa (contribuição patronal)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Calcula o que a empresa paga de INSS sobre a folha: a cota patronal (CPP, 20%), o RAT ajustado pelo FAP (seguro de acidente de trabalho conforme o risco da atividade) e as contribuições a Terceiros (Sistema S, salário-educação e INCRA). Para empresas que optaram pela CPRB (contribuição sobre a receita bruta, a "desoneração da folha"), aplica a transição de 2025 a 2027 da Lei nº 14.973/2024. Também trata pró-labore e o Simples Anexo IV.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Apuração ou conferência mensal do INSS patronal.
- Empresa optante pela CPRB na transição (2025 a 2027) ou decidindo a opção de 2027.
- Empresa do Simples no Anexo IV.
- Conferência da DCTFWeb gerada pelo eSocial (S-5011).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Para o INSS patronal bastam os totais da folha por rubrica; não listar salários por pessoa.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Tabelas de referência (2026)
```
INSS PATRONAL — REGRA GERAL (art. 22 da Lei nº 8.212/1991)
CPP (cota patronal) ......... 20% sobre a folha de empregados e avulsos
CPP sobre pró-labore e
  contribuinte individual ... 20% (art. 22, III) — sem RAT e sem Terceiros
RAT ......................... 1%, 2% ou 3% conforme a atividade preponderante
                              (Anexo V do Decreto nº 3.048/1999)
FAP ......................... 0,5000 a 2,0000, divulgado todo ano pelo governo
RAT ajustado (GILRAT) ....... RAT × FAP

TERCEIROS (exemplos de 5,8% — o código FPAS define a composição)
Indústria (FPAS 507): SESI 1,5% + SENAI 1,0% + salário-educação 2,5%
                      + INCRA 0,2% + SEBRAE 0,6% = 5,8%
Comércio (FPAS 515):  SESC 1,5% + SENAC 1,0% + salário-educação 2,5%
                      + INCRA 0,2% + SEBRAE 0,6% = 5,8%
Transporte, rural, cooperativas, ensino etc. têm composições próprias.

Total típico: 20% + 2,4% (RAT 2% × FAP 1,2) + 5,8% = 28,2% sobre a folha

REONERAÇÃO GRADUAL — art. 9º-A da Lei nº 12.546/2011 (incluído pela Lei nº 14.973/2024)
Ano    CPRB (% da alíquota)   Contribuição sobre a folha (art. 22, I e III, da Lei nº 8.212/1991)
2024   100%                   0%
2025   80%                    5%  (25% da alíquota de 20%)
2026   60%                    10% (50% da alíquota de 20%)   <- ano corrente
2027   40%                    15% (75% da alíquota de 20%)
2028   fim da CPRB            20% (regra geral)
- A empresa optante paga as DUAS parcelas no período de transição.
- A parcela sobre a folha alcança os incisos I (empregados e avulsos) e
  III (contribuintes individuais, inclusive pró-labore) do art. 22 da
  Lei nº 8.212/1991.
- A parcela sobre a folha não incide sobre o 13º salário de 2025 a 2027
  (art. 9º-A, §1º, da Lei nº 12.546/2011).
- RAT × FAP e Terceiros continuam sobre a folha normalmente.
- Alíquotas da CPRB vão de 1% a 4,5%, conforme o setor (Lei nº 12.546/2011).
- A opção é feita com o pagamento de janeiro e vale para o ano todo,
  sem volta.
- Contrapartida: a optante firma termo em que se compromete a manter
  quadro médio de empregados igual ou superior a 75% da média do ano
  anterior; se descumprir, perde a CPRB a partir do ano seguinte e volta
  aos 20% (art. 4º da Lei nº 14.973/2024).
- Setores do anexo da Lei nº 12.546/2011 (TI, comunicação, transporte,
  calçados, confecção, construção civil e outros) — conferir CNAE/NCM.

VENCIMENTO E GUIA
CPP, RAT, Terceiros e CPRB: dia 20 do mês seguinte (antecipa se não for
dia útil). Pagamento por DARF emitido pela DCTFWeb (não usa mais GPS para
empresas no eSocial). DCTFWeb: entrega até o último dia útil do mês
seguinte (IN RFB nº 2.248/2025); eSocial S-1299 e EFD-Reinf R-2099 até o dia 15.
CPRB: informada na EFD-Reinf (R-2060) e paga no DARF emitido pela
DCTFWeb, junto com as demais contribuições (não emitir DARF avulso).
```

### 2. Entrevista mínima
```
P1: "CNPJ + competência + folha bruta do mês (salário, adicionais, HE, comissões, férias)?"
P2: "Atividade preponderante (CNAE) por estabelecimento? RAT e FAP de 2026?"
P3: "Código FPAS (define os Terceiros)?"
P4: "Optou pela CPRB em janeiro/2026? Qual a alíquota do setor e a receita bruta do mês?"
P5: "Tem pró-labore ou autônomos? Atividades concomitantes (parte desonerada, parte não)?"
P6: "É do Simples? Qual anexo?"
```

### 3. Cálculo (rodar em Python)
```python
# INSS patronal — regime regular e transição da CPRB (Lei 14.973/2024).
TRANSICAO = {2025: (0.80, 0.05), 2026: (0.60, 0.10), 2027: (0.40, 0.15)}

def inss_regular(folha, rat=0.02, fap=1.0, terceiros=0.058, prolabore=0.0):
    return {
        "CPP 20% folha": folha * 0.20,
        "RAT x FAP": folha * rat * fap,
        "Terceiros": folha * terceiros,
        "CPP 20% pró-labore": prolabore * 0.20,   # sem RAT e sem Terceiros
    }

def inss_desonerada(folha, receita, aliq_cprb, ano=2026, rat=0.02, fap=1.0,
                    terceiros=0.058, folha_13=0.0, prolabore=0.0):
    fator, aliq_folha = TRANSICAO[ano]
    return {
        f"CPRB {int(fator*100)}% de {aliq_cprb:.1%} da receita": receita * aliq_cprb * fator,
        f"CPP {int(aliq_folha*100)}% folha (sem 13º)": (folha - folha_13) * aliq_folha,
        "RAT x FAP": folha * rat * fap,
        "Terceiros": folha * terceiros,
        # pró-labore (art. 22, III) também fica na alíquota reduzida da transição
        f"CPP {int(aliq_folha*100)}% pró-labore": prolabore * aliq_folha,
    }

def mostra(titulo, d):
    print(titulo)
    for k, v in d.items():
        print(f"  {k:38} R$ {v:>12,.2f}")
    print(f"  {'TOTAL':38} R$ {sum(d.values()):>12,.2f}")

mostra("Regime regular", inss_regular(100_000, 0.02, 1.2, 0.058, prolabore=5_000))
mostra("Optante CPRB 2026", inss_desonerada(100_000, 1_000_000, 0.045, 2026, 0.02, 1.2, prolabore=5_000))
mostra("Optante CPRB 2027 (simulação)", inss_desonerada(100_000, 1_000_000, 0.045, 2027, 0.02, 1.2, prolabore=5_000))
# Esperado: regular 29.200; 2026 = 27.000 + 10.000 + 2.400 + 5.800 + 500 = 45.700
```

### 4. Regras críticas
- **Pró-labore e autônomos**: CPP de 20% como contribuinte individual (art. 22, III, da Lei nº 8.212/1991). Não há RAT nem Terceiros sobre pró-labore. Na empresa optante pela CPRB, a CPRB substitui também a contribuição do art. 22, III; na transição, o pró-labore paga a alíquota reduzida do ano (10% em 2026), como a folha de empregados (art. 9º-A da Lei nº 12.546/2011, incluído pela Lei nº 14.973/2024).
- **Atividades concomitantes**: parte desonerada e parte não → proporcionaliza pela receita (art. 9º da Lei nº 12.546/2011).
- **Simples Anexo IV** (construção, limpeza, vigilância, obras, advocacia): CPP de 20% + RAT × FAP fora do DAS, pela DCTFWeb. **Não paga Terceiros**: a optante do Simples está dispensada das contribuições a terceiros (art. 13, §3º, da LC nº 123/2006). Nos demais anexos, a CPP está dentro do DAS.
- **Entram na base**: salário, horas extras, adicionais (periculosidade, insalubridade, noturno), comissões, gratificações habituais, DSR, 13º, férias gozadas e o terço constitucional das férias gozadas (STF, Tema 985).
- **Não entram**: aviso prévio indenizado (STJ, Tema 478; dispensa da PGFN), férias indenizadas e seu terço, vale-transporte, alimentação pelo PAT ou em ticket (não em dinheiro), diárias de viagem e ajuda de custo (art. 457, §2º, da CLT, com a Lei nº 13.467/2017; art. 28, §9º, da Lei nº 8.212/1991), PLR paga conforme a Lei nº 10.101/2000.
- **LC nº 224/2025**: a contribuição previdenciária da empresa está entre os tributos alcançados pela redução de 10% dos benefícios fiscais desde 01/04/2026 (art. 4º, §1º, VI, da LC nº 224/2025). A **CPRB está fora da redução** (art. 4º, §8º, XII, da LC nº 224/2025). Se o cliente usa outro benefício previdenciário (alíquota reduzida, isenção), conferir na IN RFB nº 2.305/2025 se ele está na lista de benefícios reduzidos ou preservados.

### 5. Entregável obrigatório
**a) Apuração mensal**
```
INSS PATRONAL — MM/2026 — EMPRESA EXEMPLO (CNPJ 00.000.000/0001-00) — CNAE ____
Folha total ........................ 100.000,00
  Salários ......................... 80.000
  HE e adicionais .................. 12.000
  Comissões ........................ 8.000
Pró-labore (sócio administrador) .... 5.000,00
CPP 20% × folha .................... 20.000,00
RAT 2% × FAP 1,2 × folha ........... 2.400,00
Terceiros 5,8% × folha ............. 5.800,00
CPP 20% × pró-labore ............... 1.000,00
TOTAL INSS PATRONAL ................ 29.200,00
Vencimento: dia 20 do mês seguinte — DARF da DCTFWeb
```
**b) Comparativo CPRB × folha** (empresa de setor desonerado)
```
Regime regular: R$ 29.200/mês
Optante 2026: CPRB 60% × 4,5% × 1.000.000 = 27.000
              + CPP 10% × 100.000 = 10.000
              + RAT × FAP 2.400 + Terceiros 5.800
              + CPP 10% × pró-labore 5.000 = 500
              = R$ 45.700
Leitura: com folha de 10% da receita, a CPRB já não compensa neste exemplo.
A opção de 2026 foi feita em janeiro e não muda; use o comparativo para
decidir janeiro/2027 (40% da CPRB + 15% da folha).
```
**c) Memória de cálculo** por rubrica e por estabelecimento.
**d) Guia** (DARF da DCTFWeb) com vencimento.
**e) Checklist (7 itens)**
```
[ ] CNAE preponderante e RAT conferidos por estabelecimento
[ ] FAP de 2026 conferido
[ ] FPAS e Terceiros corretos (e Simples sem Terceiros)
[ ] Pró-labore com CPP de 20% (optante da CPRB em 2026: 10%)
[ ] Verbas fora da base excluídas (aviso indenizado, férias indenizadas, PLR, VT)
[ ] Atividades concomitantes proporcionalizadas; CPRB na transição correta (2026: 60% + 10%)
[ ] S-5011 do eSocial = DCTFWeb = cálculo interno
```

## Erros comuns / pontos de atenção
- Tratar a CPRB como se ainda substituísse 100% da CPP (desde 2025 há parcela sobre a folha).
- Usar a tabela de transição errada (2026 é 60% da CPRB + 10% da folha).
- RAT errado para o CNAE ou FAP desatualizado.
- Cobrar Terceiros da optante do Simples Anexo IV.
- Pôr aviso prévio indenizado na base.
- Esquecer o pró-labore, ou aplicar RAT e Terceiros sobre ele.
- Não separar atividade desonerada e não desonerada.

## Casos de borda
- **Empresa com vários CNAEs**: RAT pela atividade preponderante de cada estabelecimento com CNPJ próprio (Súmula 351 do STJ).
- **Aprendiz**: CPP normal de 20% (não há alíquota reduzida de INSS); o que muda é o **FGTS, de 2%** (art. 15, §7º, da Lei nº 8.036/1990).
- **MEI com empregado**: CPP de 3% (art. 18-C da LC nº 123/2006).
- **Estagiário (Lei nº 11.788/2008)**: não há INSS patronal nem FGTS sobre a bolsa.
- **Filial em outro estado**: pode ter RAT e Terceiros diferentes; apurar por estabelecimento.
- **Reclamatória trabalhista**: INSS sobre as verbas salariais reconhecidas (evento próprio no eSocial).

## Quando escalar
- Folha completa → `folha-pagamento-mensal`.
- INSS e FGTS juntos, retenção de 11% → `fgts-guia-recolhimento` e `retencoes-tributarias-tomador`.
- Decisão estratégica CPRB × folha para 2027 → `analise-tributaria-regime`.
- Eventos S-1200, S-1299 → `esocial-eventos-periodicos`.
- DCTFWeb após o eSocial fechado → `dctfweb`.

## Perguntas que o usuário costuma fazer
- "Ainda vale a pena a desoneração em 2027?" Simule 40% da CPRB + 15% da folha contra 20% da folha; quanto maior a folha em relação à receita, menor a vantagem.
- "Optante do Simples no Anexo IV paga Sistema S?" Não; paga CPP de 20% + RAT × FAP fora do DAS.
- "Aviso prévio indenizado tem INSS?" Não (STJ, Tema 478).

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre os formatos citados acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- Lei nº 8.212/1991: art. 22 (CPP, RAT, contribuinte individual), art. 28, §9º (verbas fora da base), art. 30, I, "b" (vencimento).
- Decreto nº 3.048/1999: Anexo V (RAT por CNAE) e art. 202-A (FAP).
- Lei nº 12.546/2011: arts. 7º a 9º (CPRB e atividades concomitantes) e art. 9º-A (transição 2025-2027, incluído pela Lei nº 14.973/2024); Lei nº 14.973/2024, art. 4º (termo de manutenção de empregados).
- LC nº 123/2006: art. 13, §3º (Simples sem Terceiros), art. 18-C (MEI).
- Lei nº 8.036/1990: art. 15, §7º (FGTS de 2% do aprendiz).
- CLT (Decreto-Lei nº 5.452/1943): art. 457, §2º (diárias e ajuda de custo).
- Lei nº 10.101/2000 (PLR). LC nº 224/2025, art. 4º, §1º, VI, e §8º, XII (redução de benefícios; CPRB preservada), e IN RFB nº 2.305/2025.
- STF, Tema 985 (terço de férias gozadas); STJ, Tema 478 (aviso prévio indenizado); Súmula 351 do STJ (RAT por estabelecimento).
- IN RFB nº 2.110/2022 (normas gerais de contribuição previdenciária); IN RFB nº 2.248/2025 (DCTFWeb).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
