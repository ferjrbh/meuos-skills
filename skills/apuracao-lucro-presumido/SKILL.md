---
name: apuracao-lucro-presumido
description: "Apura o IRPJ e a CSLL trimestrais e o PIS/COFINS cumulativos mensais de empresa no Lucro Presumido, já com a majoração da presunção da LC 224/2025 para receita acima de R$ 5 milhões no ano. Use quando o usuário tiver empresa no Presumido (receita do ano anterior até R$ 78 milhões), disser \"lucro presumido\", \"percentual de presunção\", \"8%\", \"32%\", \"adicional de 10%\", \"DARF 2089\", \"DARF 2372\", \"Tema 69\", \"LC 224\", \"migrou do Simples para o Presumido\" ou pedir conferência de DARF do Presumido. Não use para Simples (calcular-das-simples-nacional) nem para Lucro Real (apuracao-lucro-real). Entrega: cálculo passo a passo, DARFs com código e vencimento, comparativo com o Simples quando vier dele, memória de cálculo e checklist."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Apuração do Lucro Presumido (IRPJ, CSLL, PIS e COFINS)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Calcula o IRPJ e a CSLL do trimestre sobre a base presumida (um percentual da receita fixado em lei) e o PIS/COFINS cumulativos de cada mês. Em 2026 aplica a regra nova da LC nº 224/2025, que aumenta em 10% o percentual de presunção sobre a parte da receita anual que passar de R$ 5 milhões. Entrega memória de cálculo, DARFs e checklist de conferência.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Fechamento trimestral de IRPJ/CSLL e mensal de PIS/COFINS de empresa no Presumido.
- Conferência de DARF já gerado pelo sistema.
- Empresa que saiu do Simples e entrou no Presumido.
- Empresa com receita anual perto ou acima de R$ 5 milhões (efeito da LC nº 224/2025).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Antes de aplicar a majoração da LC nº 224/2025, perguntar se o cliente tem liminar ou ação judicial contra ela (há decisões de TRFs suspendendo a exigência para alguns contribuintes).

## Passo a passo (instruções para o agente de IA)

### 1. Tabelas de referência (2026)

```
PERCENTUAIS DE PRESUNÇÃO (arts. 15 e 20 da Lei nº 9.249/1995)
Atividade                                                IRPJ    CSLL
Revenda de combustíveis                                  1,6%    12%
Comércio, indústria, transporte de cargas, atividades    8%      12%
  em geral
Serviços hospitalares e de auxílio diagnóstico e         8%      12%
  terapia (sociedade empresária + normas da Anvisa)
Construção por empreitada com fornecimento de TODO       8%      12%
  o material
Transporte de passageiros                                16%     12%
Serviços em geral de PJ só prestadora de serviços com    16%     32%
  receita anual até R$ 120 mil (exceto profissões
  regulamentadas)
Serviços em geral, profissões regulamentadas             32%     32%
  (advogado, médico, engenheiro, contador),
  intermediação, locação e administração de bens,
  construção só com mão de obra

MAJORAÇÃO 2026 — LC nº 224/2025, art. 4º, §§ 4º, VII, e 5º;
IN RFB nº 2.305/2025, arts. 14 e 15 (redação da IN RFB nº 2.306/2026)
- +10% SOBRE O PRÓPRIO PERCENTUAL (proporcional, não linear):
  8% → 8,8% · 12% → 13,2% · 16% → 17,6% · 32% → 35,2% · 1,6% → 1,76%
- Só sobre a parcela da receita bruta do ano que EXCEDER R$ 5.000.000,00.
- IRPJ: desde 01/01/2026. CSLL: desde 01/04/2026.
- Limite por trimestre: R$ 1.250.000,00. A parte do limite não usada num
  trimestre soma-se ao limite dos trimestres seguintes do mesmo ano.
  No último trimestre, confronta-se a receita do ano com o limite anual e
  acerta-se o que foi pago a mais nos trimestres anteriores.
- Em 2026 a CSLL só é majorada a partir do 2º trimestre: o limite da CSLL
  no ano é de 3 × R$ 1.250.000,00 = R$ 3.750.000,00. A partir de 2027,
  R$ 5 mi para os dois tributos.
- Início ou encerramento de atividade: limite anual = R$ 1.250.000,00 ×
  nº de trimestres em atividade.

ALÍQUOTAS
IRPJ: 15% sobre a base + adicional de 10% sobre o que exceder
      R$ 20.000 × nº de meses do período de apuração (R$ 60.000 no
      trimestre completo; proporcional no trimestre de início ou de
      encerramento de atividade — art. 3º, §1º, da Lei nº 9.249/1995,
      redação do art. 4º da Lei nº 9.430/1996)
CSLL: 9% (sem adicional)
PIS cumulativo: 0,65% (Lei nº 9.718/1998)
COFINS cumulativa: 3,00% (Lei nº 9.718/1998)

CÓDIGOS DE DARF
IRPJ Presumido: 2089 · CSLL Presumido: 2372
PIS cumulativo: 8109 · COFINS cumulativa: 2172

VENCIMENTOS
IRPJ/CSLL: último dia útil do mês seguinte ao fim do trimestre
  (abr, jul, out, jan). Pode pagar em até 3 quotas mensais iguais,
  cada uma de no mínimo R$ 1.000,00; imposto abaixo de R$ 2.000,00 é
  pago em quota única; a 2ª e a 3ª quotas têm juros Selic + 1%
  (art. 5º da Lei nº 9.430/1996).
PIS/COFINS: até o dia 25 do mês seguinte (antecipa se não for dia útil).
```

### 2. Entrevista mínima
```
P1: "CNPJ + trimestre/ano + receita bruta segregada por atividade?"
P2 (se misto): "Quanto de cada atividade? Comércio / serviço / indústria?"
P3: "Receita bruta ACUMULADA no ano até o trimestre anterior?" (para a LC 224)
P4: "O cliente tem liminar contra a LC nº 224/2025?"
P5: "Receita financeira, ganho de capital, IRRF ou CSRF retidos por terceiros?"
P6: "Receita dos 3 meses separada (para PIS/COFINS) e ICMS destacado nas saídas?"
P7 (se houver): "Receita com ST, monofásica, exportação, devoluções, descontos incondicionais?"
```
Se o usuário já mandou tudo, valide e siga. Declare suposições: "Assumindo receita financeira zero. Corrija se errado."

### 3. Base de cálculo — o que entra e o que sai
- Deduzir da receita bruta, antes de aplicar o percentual: devoluções e vendas canceladas, descontos incondicionais, IPI destacado e ICMS-ST retido (art. 12 do Decreto-Lei nº 1.598/1977; art. 208 do RIR/2018).
- Receita financeira, ganho de capital e demais receitas não operacionais entram **pelo valor integral, sem percentual de presunção** (art. 25, II, da Lei nº 9.430/1996).
- O percentual segue a **atividade real**, não só o CNAE. Confira contrato social e notas emitidas.
- 16% para serviços (só IRPJ; a CSLL fica em 32%): só se a PJ prestar **exclusivamente** serviços e a receita anual for de até R$ 120 mil (art. 15, § 1º, III, "a", da Lei nº 9.249/1995; a CSLL segue o art. 20 da mesma lei). Se a receita acumulada no ano passar de R$ 120 mil, paga a diferença do imposto postergado em relação a cada período já transcorrido, recalculado a 32% (art. 40, parágrafo único, da Lei nº 9.250/1995). Profissão regulamentada é sempre 32%.

### 4. Cálculo (rodar em Python, nunca de cabeça)
Salvar como arquivo `.py` e rodar. Os valores abaixo são exemplo.

```python
# Apuração trimestral do Lucro Presumido com a majoração da LC nº 224/2025,
# na mecânica da IN RFB nº 2.305/2025, art. 15 (redação da IN RFB nº 2.306/2026):
# limite de R$ 1.250.000,00 por trimestre; a parte não usada passa para os
# trimestres seguintes do mesmo ano; acerto anual no último trimestre (fora deste código).

LIMITE_TRIMESTRAL = 1_250_000.00   # R$ 5 mi / 4 trimestres

def excesso_do_trimestre(rec_trimestre, saldo_limite_anterior=0.0):
    """Devolve (receita deste trimestre sujeita ao percentual majorado,
    saldo de limite não usado que passa para o próximo trimestre)."""
    limite = LIMITE_TRIMESTRAL + saldo_limite_anterior
    excesso = max(0.0, rec_trimestre - limite)
    novo_saldo = max(0.0, limite - rec_trimestre)
    return excesso, novo_saldo

def presumido_trimestre(rec_trim, perc_irpj, perc_csll, saldo_irpj=0.0, saldo_csll=0.0,
                        csll_majorada=True, outras_receitas=0.0,
                        irrf_retido=0.0, csll_retida=0.0, meses=3):
    # IRPJ: majoração desde 01/01/2026 -> todos os trimestres do ano
    exc_irpj, prox_saldo_irpj = excesso_do_trimestre(rec_trim, saldo_irpj)
    # CSLL: em 2026 só a partir de 01/04 -> no 1º trimestre/2026 usar csll_majorada=False
    # e começar o saldo da CSLL do zero no 2º trimestre (limite do ano = 3,75 mi).
    if csll_majorada:
        exc_csll, prox_saldo_csll = excesso_do_trimestre(rec_trim, saldo_csll)
    else:
        exc_csll, prox_saldo_csll = 0.0, 0.0
    base_irpj = (rec_trim - exc_irpj) * perc_irpj + exc_irpj * perc_irpj * 1.10 + outras_receitas
    base_csll = (rec_trim - exc_csll) * perc_csll + exc_csll * perc_csll * 1.10 + outras_receitas
    irpj = base_irpj * 0.15
    adicional = max(0.0, base_irpj - 20_000 * meses) * 0.10   # só sobre o excesso de R$ 20 mil × meses
    csll = base_csll * 0.09
    return {
        "Receita sujeita à majoração (IRPJ)": exc_irpj,
        "Saldo de limite para o próximo trimestre (IRPJ)": prox_saldo_irpj,
        "Receita sujeita à majoração (CSLL)": exc_csll,
        "Saldo de limite para o próximo trimestre (CSLL)": prox_saldo_csll,
        "Base IRPJ": base_irpj, "IRPJ 15%": irpj, "Adicional 10%": adicional,
        "IRPJ a pagar (DARF 2089)": irpj + adicional - irrf_retido,
        "Base CSLL": base_csll, "CSLL a pagar (DARF 2372)": csll - csll_retida,
    }

def pis_cofins_mes(receita_mes, icms_destacado=0.0, canceladas=0.0, desc_incond=0.0):
    # ICMS destacado sai da base (Tema 69 do STF, RE 574.706)
    base = receita_mes - icms_destacado - canceladas - desc_incond
    return {"PIS 0,65% (DARF 8109)": base * 0.0065, "COFINS 3% (DARF 2172)": base * 0.03}

# Exemplo: serviços, 3º trimestre/2026, receita de 2.000.000 em cada trimestre
# (1º e 2º trimestres já passaram do limite -> saldo de limite zero; ano ~8 mi)
# Resultado esperado: receita majorada IRPJ = 750.000; CSLL = 750.000;
# base 674.000; IRPJ 101.100 + adicional 61.400; CSLL 60.660
for k, v in presumido_trimestre(2_000_000, 0.32, 0.32, saldo_irpj=0.0, saldo_csll=0.0,
                                csll_majorada=True, outras_receitas=10_000).items():
    print(f"{k:48} R$ {v:>14,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
```

Empresa com mais de uma atividade: calcule a base de cada atividade com seu percentual e distribua a receita sujeita à majoração entre as atividades na proporção da receita de cada uma no trimestre (IN RFB nº 2.305/2025, art. 15, §§ 3º e 6º, redação da IN RFB nº 2.306/2026).

**Acerto no último trimestre** (art. 15, § 5º): confrontar a receita acumulada no ano com o limite anual. Se ficou abaixo de R$ 5 mi, não há acréscimo no 4º trimestre e a empresa pode recalcular os trimestres anteriores sem o acréscimo e deduzir a diferença do 4º trimestre; se ficou acima, o excesso tributado no ano fica limitado à receita que passou do limite anual. Pagamento a maior que não couber na dedução vira restituição ou compensação, com Selic (§§ 7º e 8º). Montar o acerto em planilha e conferir com o texto da IN antes de fechar o ano.

### 5. Regras nucleares
- **Adicional de IRPJ**: 10% só sobre o que a base passar de R$ 20.000 × meses do período (R$ 60.000 no trimestre completo). Nunca sobre a base inteira.
- **LC nº 224/2025**: o acréscimo é proporcional (32% × 1,10 = 35,2%), não 32% + 10 pontos = 42%. Só morde a receita acima do limite; o limite da CSLL em 2026 é menor (R$ 3,75 mi). Há questionamento judicial sobre a forma de antecipação trimestral fixada pela IN RFB nº 2.306/2026: verificar a situação processual do cliente.
- **ICMS na base do PIS/COFINS**: excluir o ICMS destacado nas saídas (Tema 69 do STF, RE 574.706, com modulação a partir de 15/03/2017). No Presumido a alíquota somada é 3,65%: o erro faz pagar 3,65% sobre o ICMS, que não é receita da empresa.
- **Retenções sofridas**: IRRF retido abate o IRPJ devido; CSRF (4,65%) retida abate CSLL, PIS e COFINS de cada tributo. O DARF sai pelo líquido, e a DCTFWeb declara o débito e a dedução.
- **Receita monofásica** (combustíveis, medicamentos, autopeças, cosméticos, bebidas frias): na revenda pelo varejista, PIS/COFINS à alíquota zero; segregue. Atenção: a LC nº 224/2025 (art. 4º) reduziu benefícios federais de PIS/COFINS — as alíquotas zero e isenções alcançadas passaram a 10% da alíquota padrão (no cumulativo, 0,065% de PIS e 0,30% de COFINS), com exceções na própria lei (art. 4º, § 8º: por exemplo, cesta básica do Anexo I da LC nº 214/2025 e alíquotas *ad rem*). Antes de aplicar alíquota zero em revenda monofásica, conferir na lei e na IN RFB nº 2.305/2025 se o dispositivo que dá a alíquota zero ao produto está entre os alcançados ou entre os preservados.
- **Atividade certa é a maior parte do trabalho**. Erros frequentes:
  - transporte de cargas (8%) confundido com passageiros (16%);
  - construção só com mão de obra (32%) confundida com empreitada com todo o material (8%);
  - serviço hospitalar e de diagnóstico (8%, se sociedade empresária e cumprir as normas da Anvisa) confundido com consulta médica de clínica (32%);
  - loja que vende produto e cobra frete à parte: separe produto (8%) e serviço (32%).

### 6. Entregável obrigatório
**a) Tabela de apuração**
```
TRIMESTRE: 3º/2026  CNPJ: 00.000.000/0001-00 (EMPRESA EXEMPLO)
Receita acumulada no ano até o tri anterior: 4.000.000
RECEITA POR ATIVIDADE   Bruta       % normal  Sujeita LC 224  % major.  Base
Serviços                2.000.000   32%       750.000*        35,2%     ...
+ Receita financeira    10.000                                          10.000
= Base IRPJ do trimestre                                                ...
(*) conforme cálculo do passo 4
```

**b) Cálculo** do IRPJ (15% + adicional), da CSLL (9%), deduções de retenções e PIS/COFINS de cada mês com ICMS excluído.

**c) Memória de cálculo** com colunas `atividade, receita, perc_normal, receita_majorada, perc_majorado, base, irpj, adicional, csll, pis, cofins`.

**d) DARFs**: IRPJ 2089 (15% + adicional no mesmo DARF), CSLL 2372, PIS 8109 e COFINS 2172 de cada mês, com período de apuração, valor e vencimento. Se optar por quotas, gerar as 3 com juros.

**e) Comparativo rápido com o Simples** (se a empresa veio do Simples): mostre a alíquota **efetiva** do Simples, nunca a nominal. Ex.: Anexo I, 4ª faixa, RBT12 de R$ 1.200.000 → efetiva = (1.200.000 × 10,70% − 22.500) ÷ 1.200.000 = 8,825%. Compare com o total do Presumido no mesmo período.

**f) Checklist (8 itens)**
```
[ ] Percentual bate com a atividade real (não só CNAE)
[ ] Devoluções, descontos incondicionais, IPI e ICMS-ST deduzidos antes da presunção
[ ] Receita financeira e ganho de capital somados pelo valor integral
[ ] Receita anual acumulada conferida para a LC nº 224/2025 (5 mi IRPJ; 3,75 mi CSLL em 2026)
[ ] Situação judicial do cliente sobre a LC nº 224/2025 verificada
[ ] Adicional de 10% só sobre o excesso de R$ 60 mil
[ ] ICMS excluído da base do PIS/COFINS (Tema 69); IRRF e CSRF retidos abatidos
[ ] Débitos lançados na DCTFWeb (entrega até o último dia útil do mês seguinte)
```

### 7. Casos de borda
- **Empresa que vem do Simples**: no Presumido o PIS/COFINS é cumulativo e **não há crédito sobre o estoque de abertura** (esse crédito do art. 11 da Lei nº 10.637/2002 e do art. 12 da Lei nº 10.833/2003 é só para quem entra no regime não cumulativo, como o Lucro Real).
- **Receita do ano anterior acima de R$ 78 milhões** (ou R$ 6,5 milhões × meses de atividade): obrigada ao Lucro Real (art. 14 da Lei nº 9.718/1998).
- **Distribuição de lucros**: isenta até a base presumida menos IRPJ, CSLL, PIS e COFINS do período; acima disso, só com escrituração contábil que comprove lucro maior (art. 10 da Lei nº 9.249/1995; art. 238 da IN RFB nº 1.700/2017). Desde janeiro de 2026, a Lei nº 15.270/2025 criou retenção de IRRF de 10% sobre o total de lucros e dividendos pagos pela mesma pessoa jurídica à mesma pessoa física acima de R$ 50.000,00 no mês, sem deduções (art. 6º-A da Lei nº 9.250/1995), e o imposto mínimo anual (IRPFM) para quem tem rendimentos acima de R$ 600.000,00 no ano, com alíquota de até 10% (art. 16-A da Lei nº 9.250/1995). Transição: ficam fora da retenção os lucros apurados até o ano-calendário de 2025 cuja distribuição foi aprovada até 31/12/2025 e que forem pagos nos termos do ato de aprovação.
- **Aluguel de imóvel próprio**: locação é 32% (IRPJ e CSLL). Venda de imóvel próprio de empresa do ramo imobiliário é 8%/12%.
- **Regime de caixa**: opção anual; IRPJ/CSLL e PIS/COFINS incidem no recebimento (art. 223 da IN RFB nº 1.700/2017). Para PIS/COFINS, só vale se a empresa adotar o mesmo critério no IRPJ e na CSLL (art. 20 da MP nº 2.158-35/2001). Exige controle de recebimentos.
- **Instituições financeiras**: não podem optar pelo Presumido (obrigadas ao Real).

### 8. Quando escalar
- Margem real abaixo da presumida ou prejuízo → `analise-tributaria-regime` (o Real pode ser melhor).
- Receita acima de R$ 78 milhões → `apuracao-lucro-real`.
- Tema 69 retroativo (5 anos) → `recuperacao-creditos-pis-cofins`.
- Cliente em fiscalização → `resposta-fiscalizacao-intimacao`.

## Erros comuns / pontos de atenção
- Calcular o adicional sobre a base inteira, ou usar R$ 60 mil no trimestre de início de atividade com menos de 3 meses.
- Aplicar a LC nº 224/2025 sobre toda a receita (só sobre o excedente) ou somar 10 pontos ao percentual.
- Usar o limite de R$ 5 mi para a CSLL em 2026 (é R$ 3,75 mi) ou aplicar a CSLL majorada no 1º trimestre de 2026.
- Aplicar presunção sobre receita financeira ou ganho de capital.
- Aplicar 32% em transporte de cargas.
- Prometer crédito de PIS/COFINS sobre estoque ao cliente que saiu do Simples para o Presumido.
- Comparar com o Simples usando a alíquota nominal.

## Perguntas que o usuário costuma fazer
- "A LC 224 aumentou o IRPJ do meu cliente que fatura R$ 3 milhões?" Não: abaixo de R$ 5 mi/ano o percentual não muda (para CSLL em 2026, abaixo de R$ 3,75 mi).
- "Posso parcelar o IRPJ do trimestre?" Em até 3 quotas, mínimo R$ 1.000 cada, com Selic + 1% a partir da 2ª.
- "O ICMS sai da base do PIS/COFINS também no Presumido?" Sim, o Tema 69 vale para os dois regimes.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas a fisco): documento DOCX.
- Este padrão prevalece sobre os formatos citados acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei nº 9.249/1995: art. 3º, § 1º (adicional), art. 15 (presunção do IRPJ), art. 20 (presunção da CSLL), art. 10 (isenção de lucros distribuídos).
- Lei nº 9.250/1995: art. 40, parágrafo único (diferença ao estourar R$ 120 mil); arts. 6º-A e 16-A (retenção sobre dividendos e IRPFM, incluídos pela Lei nº 15.270/2025).
- Lei nº 9.430/1996: arts. 1º, 4º e 5º (apuração trimestral, adicional e quotas), art. 25 (base do Presumido), art. 26.
- LC nº 224/2025, art. 4º (majoração da presunção acima de R$ 5 mi; redução de benefícios); IN RFB nº 2.305/2025, arts. 14 e 15, com a redação da IN RFB nº 2.306/2026 (limite trimestral e acerto anual).
- MP nº 2.158-35/2001, art. 20 (regime de caixa no PIS/COFINS).
- Lei nº 9.718/1998: art. 13 (opção e limite de R$ 78 mi), art. 14 (obrigados ao Real); arts. 2º, 3º e 8º (PIS/COFINS cumulativos).
- Decreto-Lei nº 1.598/1977, art. 12, e Decreto nº 9.580/2018 (RIR/2018), art. 208 (receita bruta e deduções).
- IN RFB nº 1.700/2017: arts. 223 (regime de caixa) e 238 (lucros distribuídos).
- STF, RE 574.706 (Tema 69): exclusão do ICMS da base do PIS/COFINS.
- Lei nº 15.270/2025 (tributação de lucros e dividendos a partir de 2026).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
