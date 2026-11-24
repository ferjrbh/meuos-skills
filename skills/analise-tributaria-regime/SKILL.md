---
name: analise-tributaria-regime
description: "Compara Simples Nacional, Lucro Presumido e Lucro Real para um cliente, com projeção de 12 meses e todos os tributos (IRPJ, CSLL, PIS/COFINS ou CBS, ICMS, ISS, INSS sobre a folha ou CPRB em transição). Considera a LC nº 224/2025 (presunção maior acima de R$ 5 milhões), a Lei nº 15.270/2025 (dividendos e IRPFM) e a Reforma Tributária (CBS a partir de 2027). Entrega comparativo em 3 cenários, sensibilidade de ±20% e recomendação para assinatura do contador (CRC). Acionar quando o usuário disser \"qual o melhor regime\", \"comparar Simples, Presumido e Real\", \"planejamento tributário do ano\", \"vale a pena sair do Simples\", \"empresa vai estourar o Simples\", \"margem caiu, compensa o Real?\", ou na virada do ano-calendário."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Análise comparativa de regime tributário

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Compara a carga tributária total de um cliente nos três regimes (Simples Nacional, Lucro Presumido e Lucro Real), com projeção de 12 meses e análise de sensibilidade. Aponta o ponto de virada (break-even) entre os regimes, os riscos (limites, atividades vedadas, ST, DIFAL, CPRB) e o prazo de opção. O resultado é uma recomendação fundamentada que o contador responsável revisa e assina.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Três mudanças de 2026 que entram em toda comparação**
> 1. **LC nº 224/2025** (regulamentada pela IN RFB nº 2.305/2025): no Lucro Presumido, os percentuais de presunção sobem 10% (proporcional: 8% vira 8,8%; 32% vira 35,2%) **só sobre a parcela da receita bruta anual que passar de R$ 5.000.000**. IRPJ desde 01/01/2026; CSLL desde 01/04/2026, com limite de R$ 3.750.000 só em 2026. Há liminares de TRFs suspendendo a regra para alguns contribuintes: conferir a situação do cliente.
> 2. **Lei nº 15.270/2025**: dividendos acima de R$ 50 mil por mês, pagos pela mesma empresa à mesma pessoa física, sofrem retenção de 10%, e há o imposto mínimo da alta renda (IRPFM) acima de R$ 600 mil por ano. Isso muda a conta "pró-labore × distribuição de lucros" e precisa entrar na comparação.
> 3. **Reforma Tributária** (Emenda Constitucional nº 132/2023 e Lei Complementar nº 214/2025): 2026 é ano-teste (CBS 0,9% e IBS 0,1% destacados, compensáveis, sem efeito de caixa para quem cumpre as obrigações acessórias). **A partir de 2027 a CBS substitui o PIS/COFINS e o IPI fica zerado (exceto Zona Franca de Manaus).** Projeção que alcance 2027 deve usar CBS no lugar de PIS/COFINS no Presumido e no Real. No Simples, há a opção pelo regime regular de IBS/CBS (Resolução CGSN nº 186/2026).

## Quando usar
- Virada do ano-calendário, antes do prazo de opção.
- Mudança relevante: entrada ou saída de sócio, nova atividade, expansão, queda de margem.
- Empresa perto de estourar o limite do Simples (R$ 4,8 milhões) ou o sublimite estadual de ICMS/ISS (R$ 3,6 milhões — art. 19 da LC nº 123/2006).
- Margem real menor que o percentual presumido (o Lucro Real pode sair mais barato).
- Empresa do Presumido que vai passar de R$ 5 milhões de receita anual (efeito da LC nº 224/2025).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- A opção de regime é decisão do cliente com o contador responsável. A skill recomenda, não opta.

## Passo a passo (instruções para o agente de IA)

### 1. Heurísticas de partida (só para orientar; o cálculo decide)
```
Receita / margem / folha                        Regime que costuma ser vantajoso
Até R$ 4,8 mi, serviço com folha alta           Simples Anexo III (Fator R ≥ 28%)
Até R$ 4,8 mi, comércio com margem média        Simples Anexo I
Até R$ 78 mi, margem real acima da presumida    Lucro Presumido
  (serviço > 32%; comércio/indústria > 8%)      (atenção: acima de R$ 5 mi a presunção sobe — LC 224/2025)
Até R$ 78 mi, margem baixa ou prejuízo          Lucro Real
Indústria com muito insumo                      Lucro Real (créditos de PIS/COFINS — conceito de insumo do STJ, REsp 1.221.170)
Exportadora                                     Lucro Real (manutenção de créditos)
Receita acima de R$ 78 mi, factoring,           Lucro Real OBRIGATÓRIO (art. 14 da Lei nº 9.718/1998)
  instituição financeira, securitizadora,
  lucros do exterior, benefício de isenção/redução
Atividade vedada ao Simples                      Sai do Simples, mas não vai obrigatoriamente para o Real:
                                                 conferir o art. 14 da Lei nº 9.718/1998
Receita até R$ 81 mil/ano                       MEI, se a atividade e as demais condições permitirem
  (art. 18-A, § 1º, da LC nº 123/2006)
```

### 2. Entrevista mínima
```
P1: CNPJ (de exemplo, se for simulação) e atividades principal e secundárias (CNAE)?
P2: Receita dos últimos 12 meses e projeção dos próximos 12? Passa de R$ 5 mi no ano?
P3: Folha dos últimos 12 meses (com pró-labore, 13º e férias) — para o Fator R?
P4: Custos diretos (CMV/CPV/CSP) e despesas operacionais?
P5: Compras e despesas que geram crédito de PIS/COFINS (ou de CBS, a partir de 2027) no Real?
P6: Receita de exportação? Investimentos (CAPEX)? Setor desonerado (CPRB — Lei nº 14.973/2024)?
P7: Como os sócios são remunerados (pró-labore × dividendos)? Algum sócio passa de R$ 50 mil/mês
    de dividendos ou de R$ 600 mil/ano de renda total (Lei nº 15.270/2025)?
P8: Há decisão judicial do cliente sobre a LC nº 224/2025?
```

### 3. Cálculo de apoio (Python)
O código abaixo é um **esqueleto simplificado** para a primeira visão. Ele não substitui a apuração detalhada de cada regime. Para rodar no Windows, salvar como arquivo `.py` e executar com `python -I -X utf8 arquivo.py`.

```python
# Esqueleto de comparação anual — valores do exemplo são fictícios.
# Limitações conhecidas: não calcula ICMS/ISS, Fator R, sublimite nem CPRB;
# usa uma única faixa do Simples; trata o ano inteiro de uma vez.

def simples_anexo_iii_faixa4(receita_anual):
    # Anexo III da LC nº 123/2006, 4ª faixa (RBT12 de 720.000,01 a 1.800.000):
    # 16% e parcela a deduzir 35.640. Para outra faixa ou anexo, trocar pelos valores
    # dos Anexos I a V da LC nº 123/2006.
    aliq_ef = (receita_anual * 0.16 - 35_640) / receita_anual
    return receita_anual * aliq_ef

def base_presumida(receita, perc, limite=5_000_000):
    # LC 224/2025: +10% proporcional no percentual só sobre o que passa do limite.
    ate = min(receita, limite)
    excedente = max(0, receita - limite)
    return ate * perc + excedente * perc * 1.10

def presumido(receita_anual, perc_irpj=0.08, perc_csll=0.12, ano=2026):
    base_irpj = base_presumida(receita_anual, perc_irpj)
    irpj = base_irpj * 0.15 + max(0, base_irpj - 240_000) * 0.10  # adicional: R$ 60 mil/trimestre
    limite_csll = 3_750_000 if ano == 2026 else 5_000_000            # só em 2026 o limite da CSLL é 3/4
    csll = base_presumida(receita_anual, perc_csll, limite_csll) * 0.09
    pis_cofins = receita_anual * (0.0065 + 0.03)                      # cumulativo; em 2027 trocar por CBS
    return irpj + csll + pis_cofins

def real(receita_anual, icms_destacado, custo_direto, despesa, compras_com_credito):
    lair = receita_anual - custo_direto - despesa
    irpj = max(0, lair) * 0.15 + max(0, lair - 240_000) * 0.10
    csll = max(0, lair) * 0.09
    # PIS/COFINS não cumulativo: débito sobre a receita SEM o ICMS destacado (Tema 69 do STF)
    # MENOS os créditos (compras de insumos sem ICMS — Lei nº 14.592/2023). Em 2027, trocar por CBS.
    debito = (receita_anual - icms_destacado) * 0.0925
    credito = compras_com_credito * 0.0925
    return irpj + csll + max(0, debito - credito)

receita = 1_800_000
print("Simples:  ", round(simples_anexo_iii_faixa4(receita), 2))
print("Presumido:", round(presumido(receita, 0.32, 0.32), 2))
print("Real:     ", round(real(receita, 0, 1_200_000, 320_000, 300_000), 2))
# Depois somar, em cada cenário: INSS patronal (CPP 20% + RAT + Terceiros, fora do Simples
# no Anexo IV), ICMS e ISS. Sem isso a comparação fica incompleta.
```

### 4. Cenários
- **Simples**: usar as skills `calcular-das-simples-nacional` e `conferir-apuracao-simples-nacional` (anexos, Fator R, sublimite).
- **Presumido**: usar as skills `apuracao-lucro-presumido` e `calculo-pis-cofins-cumulativo` (com a LC nº 224/2025 acima de R$ 5 milhões).
- **Real**: usar as skills `apuracao-lucro-real` e `calculo-pis-cofins-nao-cumulativo` (créditos de PIS/COFINS sobre insumos).
- Em cada um: carga total anual + percentual sobre a receita + efeito na distribuição aos sócios (Lei nº 15.270/2025).
- Se a projeção alcançar 2027: modelar CBS no lugar de PIS/COFINS, com a alíquota de referência da CBS para 2027 fixada por resolução do Senado Federal nos termos da LC nº 214/2025. Antes de calcular, conferir se a resolução já foi publicada; se ainda não foi, apresentar o cenário de 2027 como estimativa e dizer isso no relatório.

### 5. Sensibilidade
Recalcular com:
- receita ±20%;
- margem (lucro/receita) ±5 pontos percentuais;
- folha como % da receita ±5 pontos percentuais (mexe no Fator R e no INSS).

Identificar o **break-even** (ponto em que um regime passa a ser melhor que outro).

### 6. Entregável
**a) Pacote de análise**
```
CLIENTE EXEMPLO — CNPJ 00.000.000/0001-00 — Análise do ano-calendário ____

PROJEÇÃO DE RECEITA
Mês       Realizado 12m    Projetado
Jan       ____             ____
...
Total     ____             ____

CENÁRIOS                Simples     Presumido    Real
Carga total             R$ ____     R$ ____      R$ ____
% da receita            ___%        ___%         ___%
Sobra para o caixa      R$ ____     R$ ____      R$ ____
Efeito nos sócios       R$ ____     R$ ____      R$ ____   (dividendos/IRPFM — Lei 15.270/2025)

SENSIBILIDADE — Receita ±20%
                        −20%        Base         +20%
Simples                 R$ ____     R$ ____      R$ ____
Presumido               R$ ____     R$ ____      R$ ____
Real                    R$ ____     R$ ____      R$ ____

RISCOS / ATENÇÃO
[ ] Limite do Simples (R$ 4,8 mi) e sublimite estadual (R$ 3,6 mi — conferir no Portal do
    Simples Nacional o sublimite adotado pela UF no ano)
[ ] Atividades vedadas ao Simples
[ ] Presumido acima de R$ 5 mi (LC 224/2025) e situação judicial do cliente
[ ] ST / DIFAL
[ ] CPRB em transição (Lei nº 14.973/2024)
[ ] Reforma Tributária: CBS em 2027; opção do Simples pelo regime regular de IBS/CBS

RECOMENDAÇÃO: ____
JUSTIFICATIVA: 1. ____  2. ____  3. ____

PRAZO PARA OPÇÃO
- Simples: regra geral, até o último dia útil de janeiro, com efeito desde 1º de janeiro
  (art. 16 da LC nº 123/2006). ATENÇÃO: para o ano-calendário 2027 a opção foi antecipada
  pela Resolução CGSN nº 186/2026, com prazos alterados pela Resolução CGSN nº 194/2026:
  opção pelo Simples de 01/09 a 15/10/2026; opção pelo regime regular de IBS/CBS até
  30/10/2026; cancelamento das opções de 03/11 a 20/12/2026. A antecipação foi fixada só
  para 2027: para 2028 em diante, conferir a resolução do CGSN vigente antes da janela.
  Empresa em início de atividade tem prazo próprio.
- Lucro Real anual: pagamento do DARF da estimativa de janeiro (5993 para PJ optante; 2362 para PJ obrigada ao Lucro Real) — irretratável no ano
  (art. 3º da Lei nº 9.430/1996).
- Lucro Real trimestral: pagamento do DARF do 1º trimestre (3373 para PJ optante; 0220 para PJ obrigada).
- Lucro Presumido: pagamento da 1ª quota ou quota única do IRPJ do 1º trimestre, DARF 2089
  (art. 26 da Lei nº 9.430/1996).
- CPRB: opção anual pelo pagamento da contribuição de janeiro, ou da primeira competência
  com receita bruta (art. 9º, § 13, da Lei nº 12.546/2011).

[Local, data]
Responsável técnico: ____ CRC ____
```
**b) Memória de cálculo** com os cenários.
**c) Alerta de prazo** quando a análise for feita perto da janela de opção.

## Erros comuns / pontos de atenção
- Olhar só IRPJ/CSLL e ignorar ICMS/ISS (no comércio, o ICMS costuma ser o maior tributo).
- Esquecer o INSS sobre a folha: no Presumido e no Real, com folha alta, pode pesar mais que tudo.
- Calcular o Real sem os créditos de PIS/COFINS, ou com o ICMS dentro da base do débito (Tema 69 do STF) e dentro da base do crédito (desde maio/2023 o ICMS sai também da base do crédito — Lei nº 14.592/2023).
- Calcular o Presumido acima de R$ 5 milhões sem a majoração da LC nº 224/2025, ou aplicá-la de forma linear (32% + 10 = 42% está errado; o certo é 35,2%).
- Esquecer receitas financeiras e ganhos de capital, que no Presumido entram pelo valor integral (art. 25, II, da Lei nº 9.430/1996).
- Migrar do Presumido para o Real sem aproveitar o crédito presumido sobre o estoque de abertura (art. 11 da Lei nº 10.637/2002 e art. 12 da Lei nº 10.833/2003).
- Análise estática, sem cenário de crescimento: a empresa estoura o Simples no meio do ano.
- Ignorar o efeito da Lei nº 15.270/2025 na retirada dos sócios.
- Usar PIS/COFINS em projeção de 2027 (já será CBS).

**Casos de borda**
- **CPRB em transição** (Lei nº 14.973/2024): 2025 = 80% da alíquota da CPRB + 5% sobre a folha; 2026 = 60% + 10%; 2027 = 40% + 15%; 2028 = fim da CPRB, 20% sobre a folha. Simular cada ano.
- **Filiais em UFs diferentes**: o ICMS varia por UF; calcular por estabelecimento.
- **Receita sazonal** (turismo, agro): usar média móvel de 12 meses.
- **Início de atividade no Simples**: RBT12 proporcional (art. 18, § 2º, da LC nº 123/2006).

## Perguntas que o usuário costuma fazer
- **"Posso trocar de regime no meio do ano?"** Em regra não: a opção vale para o ano todo. Exceção: exclusão do Simples (por exemplo, excesso de receita) e a obrigatoriedade do Lucro Real.
- **"Acima de R$ 5 milhões o Presumido deixa de valer a pena?"** Depende da margem: a presunção sobe só sobre o excedente. Rodar os dois cenários.
- **"A Reforma muda a escolha para 2027?"** Sim, no PIS/COFINS (vira CBS) e no Simples (opção pelo regime regular de IBS/CBS, que dá crédito pleno ao cliente comprador).

## Formato de entrega
- Cálculos, apurações e conciliações: sempre planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): sempre documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei Complementar nº 123/2006 — Simples Nacional (art. 3º limites; art. 16 opção; art. 17 vedações; art. 18 alíquotas e § 2º início de atividade; art. 18-A MEI; art. 19 sublimite).
- Resolução CGSN nº 140/2018 — regulamento do Simples; Resolução CGSN nº 186/2026, alterada pela Resolução CGSN nº 194/2026 — prazos de opção para 2027 e regime regular de IBS/CBS.
- Lei nº 9.249/1995 — arts. 15 e 20 (percentuais de presunção do IRPJ e da CSLL).
- Lei nº 9.430/1996 — arts. 1º a 3º (períodos de apuração e opção pelo Real anual), 25 e 26 (Presumido).
- Lei nº 9.718/1998 — art. 14 (obrigatoriedade do Lucro Real).
- Lei Complementar nº 224/2025 e IN RFB nº 2.305/2025 — majoração da presunção acima de R$ 5 milhões.
- Lei nº 10.637/2002 e Lei nº 10.833/2003 — PIS/COFINS não cumulativo; art. 11 e art. 12 (crédito sobre estoque de abertura).
- Lei nº 14.592/2023 — exclusão do ICMS da base dos créditos de PIS/COFINS.
- STF, RE 574.706 (Tema 69) — ICMS fora da base do PIS/COFINS.
- Lei nº 12.546/2011 (art. 9º, § 13 — opção anual) e Lei nº 14.973/2024 — CPRB e reoneração gradual da folha.
- Lei nº 15.270/2025 — tributação de dividendos e IRPFM.
- Emenda Constitucional nº 132/2023 e Lei Complementar nº 214/2025 — CBS/IBS.
- IN RFB nº 1.700/2017 — regras gerais de IRPJ/CSLL.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
