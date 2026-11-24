---
name: apuracao-mei
description: "Cuida do MEI (Microempreendedor Individual) — DAS-MEI mensal com os valores de 2026, DASN-SIMEI anual, controle do limite de R$ 81.000, tolerância de 20%, desenquadramento e migração para ME no Simples. Use quando o usuário tiver cliente MEI ou disser \"MEI\", \"DAS-MEI\", \"PGMEI\", \"DASN-SIMEI\", \"NFS-e nacional\", \"desenquadramento\", \"estourou o limite do MEI\", \"empregado do MEI\", ou quando o acumulado do ano passar de 70% do limite. Não use para Simples ME/EPP (calcular-das-simples-nacional). MEI Caminhoneiro tem regra própria (R$ 251.600 e INSS de 12%), resumida aqui só como referência. Entrega: tabela de controle anual, DAS do mês, diagnóstico de risco e carta-aviso ao cliente quando o limite estiver perto."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Apuração e controle do MEI

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Calcula o DAS-MEI do mês (valor fixo, ligado ao salário mínimo), mantém o controle do faturamento acumulado no ano, estima quando o cliente vai estourar o limite e diz o que fazer se estourar (dentro ou fora da tolerância de 20%). Também lembra a DASN-SIMEI e as obrigações do MEI que tem empregado.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Emissão ou conferência do DAS-MEI do mês.
- Controle mensal do limite de faturamento da carteira de MEIs.
- MEI que estourou o limite ou mudou para atividade não permitida.
- MEI que vai contratar empregado.
- Entrega da DASN-SIMEI (até 31 de maio).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). O MEI é pessoa física com CNPJ: o CPF do titular e os dados do empregado não vão para a tabela de controle nem para a carta.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite. A carta-aviso é rascunho: o contador revisa antes de mandar.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Tabelas de referência (2026)
```
SALÁRIO MÍNIMO 2026: R$ 1.621,00 (Decreto nº 12.797/2025)

DAS-MEI MENSAL 2026 (valor fixo — art. 18-A, §3º, IV e V, da LC nº 123/2006;
INSS de 5% do salário mínimo — art. 21, §2º, II, "a", da Lei nº 8.212/1991)
INSS (5% do salário mínimo) ......... R$ 81,05
ICMS (comércio/indústria) ........... R$ 1,00
ISS (serviços) ...................... R$ 5,00
Comércio ou indústria ............... R$ 82,05
Serviços ............................ R$ 86,05
Comércio + serviços ................. R$ 87,05
Vencimento: dia 20 do mês seguinte (guia pelo PGMEI)

LIMITES
Anual: R$ 81.000,00 (média de R$ 6.750,00/mês)
Ano de abertura: R$ 6.750,00 × nº de meses entre o início da atividade e
  dezembro (fração de mês conta como mês inteiro — art. 100, §1º, da
  Resolução CGSN nº 140/2018)
Tolerância de 20%: até R$ 97.200,00 no ano (ou limite proporcional × 1,20)
  - até 20% acima: continua MEI no ano; vira ME a partir de 1º de janeiro
    seguinte e paga DAS sobre o excesso
  - mais de 20% acima: desenquadramento RETROATIVO a 1º de janeiro
    (ou ao início da atividade, se for o ano de abertura)
  (art. 18-A, §7º, III e IV, da LC nº 123/2006)

EMPREGADO DO MEI (art. 18-C da LC nº 123/2006)
Máximo 1 empregado, que recebe 1 salário mínimo (lei federal ou estadual)
  ou o piso salarial da categoria
Empresa: CPP de 3% sobre o salário de contribuição (art. 18-C, §1º, III)
  + FGTS 8%
Empregado: INSS descontado pela tabela progressiva 2026
Recolhimento: guia gerada no módulo simplificado do eSocial para o MEI
  (conferir no portal do eSocial se o FGTS sai na mesma guia ou pelo FGTS Digital)
Exemplo com salário mínimo: CPP 3% = 48,63; FGTS 8% = 129,68;
  INSS do empregado 7,5% = 121,58 (descontado do salário)

NFS-e NACIONAL
Destinatário com CNPJ: nota obrigatória, salvo se o destinatário emitir
nota de entrada (art. 106 da Resolução CGSN nº 140/2018). Serviço: emitir
pelo emissor nacional (gov.br/nfse), padrão obrigatório para o MEI
(Resolução CGSN nº 169/2022). Venda ou serviço a pessoa física:
nota dispensada, mas recomendada.

DASN-SIMEI
Prazo: 31 de maio de cada ano (referente ao ano anterior); o prazo não é
prorrogado se cair em fim de semana ou feriado.
Obrigatória mesmo com faturamento zero.
Multa por atraso: 2% ao mês-calendário ou fração sobre os tributos
declarados, limitada a 20%, mínimo R$ 50,00; reduzida à metade se entregue
antes de procedimento de ofício (art. 38 da LC nº 123/2006).

MEI CAMINHONEIRO (só referência — art. 18-F da LC nº 123/2006)
Limite R$ 251.600,00/ano · INSS 12% do mínimo = R$ 194,52
DAS 2026: R$ 195,52 (carga intermunicipal/interestadual) ou
          R$ 199,52 (transporte municipal)
```

### 2. Entrevista mínima
```
P1: "CNPJ + competência + faturamento do mês?"
P2 (primeiro contato): "Qual a atividade? Quando o MEI foi aberto?"
P3: "Tem empregado? Prestou serviço a empresa no mês (NFS-e)?"
P4 (controle): "Qual o faturamento acumulado no ano até agora?"
```
Cliente recorrente: pedir só o que mudou desde o mês passado.

### 3. Cálculo e controle (rodar em Python)
```python
# DAS-MEI 2026 e situação do limite anual.
SALARIO_MINIMO = 1621.00   # Decreto nº 12.797/2025 — revisar todo janeiro

def das_mei(tipo):
    inss = round(SALARIO_MINIMO * 0.05, 2)            # 81,05
    adicional = {"comercio": 1.00, "servico": 5.00, "misto": 6.00}[tipo]
    return inss + adicional

def status_anual(meses_ativos, acumulado):
    limite = min(81_000.00, 6_750.00 * meses_ativos)  # proporcional no ano de abertura
    tolerancia = limite * 1.20
    uso = acumulado / limite * 100
    if acumulado <= limite:
        return f"OK — uso de {uso:.1f}% do limite de R$ {limite:,.2f}"
    if acumulado <= tolerancia:
        return (f"EXCESSO ATÉ 20% — segue MEI no ano; vira ME em 1º de janeiro; "
                f"paga DAS sobre o excesso de R$ {acumulado - limite:,.2f}")
    return "EXCESSO ACIMA DE 20% — desenquadramento RETROATIVO (1º de janeiro ou início da atividade)"

def meses_para_estourar(acumulado, media_mensal, meses_ativos=12):
    limite = min(81_000.00, 6_750.00 * meses_ativos)
    return (limite - acumulado) / media_mensal if media_mensal else None

print(f"DAS serviço: R$ {das_mei('servico'):.2f}")         # 86.05
print(status_anual(meses_ativos=12, acumulado=85_000))
print(status_anual(meses_ativos=7, acumulado=60_000))     # aberto há 7 meses
```

### 4. Diagnóstico de risco (rodar sempre)
`meses para estourar = (limite − acumulado) ÷ faturamento médio mensal`
- Menos de 3 meses: alerta imediato e carta-aviso.
- Menos de 6 meses ou uso acima de 70%: alerta com plano de migração.

### 5. Quando o limite estoura
**Prazo de comunicação** (art. 18-A, §7º, da LC nº 123/2006; art. 115 da Resolução CGSN nº 140/2018): nos dois casos de excesso de receita, comunicar o desenquadramento no Portal do Simples Nacional até o **último dia útil do mês seguinte** àquele em que ocorreu o excesso. Sem a comunicação, há desenquadramento de ofício e multa (art. 18-A, §8º, e art. 36-A da LC nº 123/2006).

**Excesso de até 20%** (art. 18-A, §7º, III): o cliente segue MEI até dezembro; a partir de 1º de janeiro vira ME no Simples. O excesso é tributado no "DAS de excesso de receita", gerado pela DASN-SIMEI e pago no vencimento do Simples relativo a janeiro do ano seguinte, com as alíquotas efetivas dos Anexos (art. 115, §8º, da Resolução CGSN nº 140/2018).

**Excesso acima de 20%**: vira ME retroativo a 1º de janeiro (ou ao início da atividade, no ano de abertura). Refaça a apuração desde então no Simples (`calcular-das-simples-nacional`), abatendo o DAS-MEI pago. DAS em atraso: multa de mora de 0,33% ao dia (máximo 20%) + Selic.

**Atividade que deixou de ser permitida, 2º empregado (ou empregado com salário acima do permitido), filial ou participação em outra empresa**: desenquadramento obrigatório, com comunicação até o último dia útil do mês seguinte ao da situação e efeitos a partir do mês seguinte. Inclusão de atividade não permitida, abertura de filial ou mudança de natureza jurídica no CNPJ desenquadram automaticamente (art. 18-A, §17, da LC nº 123/2006).

### 6. Empregado do MEI
- 1 empregado, com 1 salário mínimo ou o piso da categoria.
- Guia mensal pelo módulo simplificado do eSocial: CPP 3% + FGTS 8% + INSS descontado do empregado (+ IRRF, se houver).
- Admissão e folha pelo eSocial simplificado (usar `folha-pagamento-mensal` e `esocial-admissao`).

### 7. Retenção de 11% pelo tomador
- **O MEI não sofre a retenção de 11%**: entre os optantes do Simples, a retenção do art. 31 da Lei nº 8.212/1991 alcança só ME e EPP tributadas no Anexo IV (art. 166 da IN RFB nº 2.110/2022).
- O MEI não pode exercer suas atividades mediante cessão ou locação de mão de obra (art. 112 da Resolução CGSN nº 140/2018).
- Exceção do art. 18-B da LC nº 123/2006: a empresa que contrata MEI para **hidráulica, eletricidade, pintura, alvenaria, carpintaria ou manutenção/reparo de veículos** paga a CPP de 20% sobre o valor do serviço (art. 22, III, da Lei nº 8.212/1991) e cumpre as obrigações acessórias de contratante de contribuinte individual, **sem reter nada do MEI** (art. 173 da IN RFB nº 2.110/2022).
- Se houver pessoalidade, subordinação e habitualidade com o contratante, vale a relação de emprego (art. 18-B, §2º, da LC nº 123/2006) e o MEI é excluído do Simples.

### 8. Entregável obrigatório
**a) Tabela de controle anual**
```
MEI: CLIENTE EXEMPLO   CNPJ: 00.000.000/0001-00   Atividade: serviços
ANO: 2026
Mês   Faturamento   Acumulado   DAS (R$ 86,05)   NFS-e para PJ
Jan   6.000         6.000       [ ] pago         2
Fev   8.000         14.000      [ ]              3
...
Out   7.500         75.000      [ ]              5
Limite anual: R$ 81.000   Uso: 92,6%   Estouro previsto: novembro
Situação: ATENÇÃO — preparar migração para ME
DASN-SIMEI 2025: entregue em 28/05/2026
```
**b) DAS do mês**: "PGMEI > Emitir guia > competência 01/2026 > R$ 86,05 (serviços) > vencimento 20/02/2026."

**c) Carta-aviso** (quando faltar menos de 3 meses para estourar):
```
Assunto: Atenção — limite do MEI perto de estourar

Olá, [nome do cliente],

Seu faturamento em 2026 chegou a R$ X (X% do limite de R$ 81.000). No ritmo
atual, o limite estoura em [mês].

Há 2 caminhos:
1. Pedir o desenquadramento agora e passar a ME no Simples Nacional.
   - O imposto passa a ser um percentual do faturamento (a partir de 4% no
     comércio e 6% em serviços do Anexo III, conforme a atividade).
   - Muda o custo contábil: R$ X por mês.
2. Continuar MEI até dezembro e passar a ME em 1º de janeiro de 2027.
   - Faturamento até R$ 97.200 é tolerado (excesso de até 20%), pagando
     imposto sobre o excesso.
   - Acima disso, o desenquadramento volta a janeiro de 2026, com imposto
     e multa sobre os meses passados.

Recomendo a opção __ porque __.
Por favor, responda em até 5 dias úteis.

Atenciosamente, [contador responsável]
```
**d) Checklist mensal**
```
[ ] DAS gerado e pago até o dia 20
[ ] NFS-e emitidas para PJ (emissor nacional)
[ ] Acumulado do ano atualizado e risco calculado
[ ] Empregado: eventos do eSocial e DAE pagos
[ ] Comprovante do DAS arquivado
```
**e) Checklist anual (DASN-SIMEI)**
```
[ ] Receita do ano conferida com extratos e notas
[ ] DASN-SIMEI transmitida até 31 de maio (mesmo com faturamento zero)
[ ] Recibo arquivado
[ ] Cliente avisado se estiver perto do limite
```

## Erros comuns / pontos de atenção
- Usar o salário mínimo antigo no DAS (em 2026 é R$ 1.621,00; DAS de R$ 82,05 a R$ 87,05).
- Esquecer o DAS de algum mês: o MEI fica em débito e pode perder a contagem de carência para benefícios do INSS.
- Não acompanhar o acumulado e ser surpreendido em dezembro; alertar todo mês acima de 70%.
- Atividade não permitida ao MEI (ex.: advocacia, medicina, engenharia, contabilidade).
- Confundir o limite proporcional do ano de abertura com o anual.
- Esquecer que valores que não são receita da atividade (empréstimos, aportes do titular, auxílios do governo) não entram no faturamento.
- Usar GFIP/SEFIP para o empregado do MEI: as informações vão pelo eSocial (módulo simplificado).

## Casos de borda
- **Aberto há 7 meses com R$ 60 mil**: limite proporcional = R$ 47.250; tolerância = R$ 56.700. Passou dos 20%: desenquadramento retroativo ao mês de abertura.
- **Aberto em janeiro, mas só faturou a partir de junho**: o limite é o anual (R$ 81.000), porque o proporcional conta meses de atividade desde a abertura.
- **Débitos antigos**: emitir o DAS atual e mostrar a situação fiscal do PGMEI/e-CAC. O parcelamento de débitos do MEI é permitido desde a LC nº 155/2016: o convencional pode ser pedido a qualquer tempo no Portal do Simples Nacional ou no e-CAC ("Parcelamento – Microempreendedor Individual"), em até 60 parcelas de no mínimo R$ 50,00, só para débitos vencidos e já declarados na DASN-SIMEI (Perguntas e Respostas MEI e Simei, capítulo 4) → `parcelamento-receita-federal`.
- **MEI inadimplente por muito tempo**: a inscrição pode ser cancelada de ofício, sem aviso, após 12 meses consecutivos sem pagamentos ou declarações, com publicação no Portal do Empreendedor (art. 18-A, §15-B, da LC nº 123/2006).
- **Reforma Tributária**: em 2026 o MEI não precisa destacar CBS/IBS na nota; a NF-e de MEI (CRT 4) sem esses grupos passa a ser rejeitada a partir de 04/01/2027. O MEI não pode optar pelo regime regular de IBS/CBS.

## Quando escalar
- Vai migrar para ME → `analise-tributaria-regime` (escolha do anexo) + `calcular-das-simples-nacional`.
- Contratou empregado → `folha-pagamento-mensal` + `esocial-admissao`.
- Débitos antigos → `parcelamento-receita-federal`.
- Serviço com cessão de mão de obra → `retencoes-tributarias-tomador`.

## Perguntas que o usuário costuma fazer
- "Quanto é o DAS do MEI em 2026?" R$ 82,05 (comércio/indústria), R$ 86,05 (serviços) ou R$ 87,05 (os dois).
- "Meu cliente faturou R$ 90 mil. Perde o MEI?" Fica MEI até dezembro, paga imposto sobre o excesso e vira ME em janeiro.
- "Abri o MEI em setembro; qual o meu limite?" R$ 6.750 × 4 meses = R$ 27.000.

## Formato de entrega
- Cálculos, apurações e controles: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, relatórios e correspondências (como a carta-aviso): documento DOCX.
- Este padrão prevalece sobre os formatos citados acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- LC nº 123/2006: art. 18-A (MEI, limite, DAS fixo, desenquadramento e cancelamento — §§ 1º, 2º, 3º, 7º, 8º, 15-B e 17), art. 18-B (contratação de MEI por empresa), art. 18-C (empregado do MEI), art. 18-F (MEI transportador autônomo de cargas), arts. 36-A e 38 (multas).
- Lei nº 8.212/1991: art. 21, §2º, II, "a" (INSS de 5% do MEI), art. 22, III (CPP de 20% do art. 18-B), art. 31 (retenção de 11%).
- IN RFB nº 2.110/2022: arts. 166 e 173.
- Resolução CGSN nº 140/2018: art. 100 (requisitos e limite proporcional), art. 106 (nota fiscal), art. 112 (vedação de cessão de mão de obra), art. 115 (desenquadramento), Anexo XI (ocupações permitidas).
- Resolução CGSN nº 169/2022 (NFS-e padrão nacional).
- Decreto nº 12.797/2025 (salário mínimo de 2026).
- Perguntas e Respostas MEI e Simei (CGSN, atualizado em 29/04/2025), capítulos 3, 4 e 6.
- Emenda Constitucional nº 132/2023, LC nº 214/2025 e Ato Conjunto RFB/CGIBS nº 4/2026 (cronograma CBS/IBS).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
