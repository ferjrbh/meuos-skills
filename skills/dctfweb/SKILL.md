---
name: dctfweb
description: "Prepara e confere a DCTFWeb mensal (e a anual de 13º salário): débitos federais que vêm do eSocial e da EFD-Reinf (INSS patronal CPP, RAT×FAP, Terceiros, INSS retido, IRRF, CSRF) e os informados no MIT (IRPJ, CSLL, PIS/COFINS, IPI e demais). Vincula DARFs pagos, PER/DCOMP e suspensões judiciais, e orienta a retificação na ordem certa. Prazo de entrega em 2026 é o último dia útil do mês seguinte (IN RFB nº 2.248/2025). Acionar quando o usuário disser \"fazer a DCTFWeb\", \"fechei o eSocial e a Reinf\", \"conferir débitos da DCTFWeb\", \"MIT\", \"DCTFWeb de 13º\", \"aferição de obra\", \"reclamatória trabalhista\", \"retificar DCTFWeb\", \"DCTFWeb não bate com o eSocial\". Entrega tabela débitos esperados × confessados, plano de retificação se houver divergência, lista de DARFs por código e checklist de recibo."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# DCTFWeb mensal e anual

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Organiza a confissão mensal dos débitos federais na DCTFWeb (Declaração de Débitos e Créditos Tributários Federais Previdenciários e de Outras Entidades e Fundos). Confere se tudo que veio do eSocial e da EFD-Reinf está correto, se os tributos que não vêm desses sistemas foram informados no MIT (Módulo de Inclusão de Tributos) e se pagamentos, compensações e suspensões estão vinculados. Termina com a tabela de conferência e a lista de DARFs.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Mudanças que valem em 2026**
> - Desde os fatos geradores de **janeiro/2025**, a DCTF antiga (PGD) deixou de existir. A DCTFWeb passou a receber **todos** os débitos federais: os do eSocial e da EFD-Reinf e, pelo **MIT**, IRPJ, CSLL, PIS/COFINS, IPI e demais. Norma vigente: **IN RFB nº 2.237/2024**, que substituiu a IN RFB nº 2.005/2021 para esses fatos geradores.
> - **Prazo de entrega:** último dia útil do mês seguinte ao dos fatos geradores (IN RFB nº 2.248/2025, que alterou a IN RFB nº 2.237/2024). Não é mais o dia 25. Exemplo: DCTFWeb de setembro/2026 venceu em 30/10/2026.
> - O prazo de **entrega** não muda o prazo de **pagamento** de cada tributo (INSS e IRRF da folha continuam no dia 20).

## Quando usar
- Depois de fechar o eSocial (S-1299) e a EFD-Reinf (R-2099 e R-4099) da competência.
- Para informar no MIT os tributos apurados fora do eSocial e da Reinf.
- Na DCTFWeb anual de 13º salário, na de aferição de obra (CNO) e na de reclamatória trabalhista.
- Para retificar débitos depois de ajuste no eSocial, na Reinf ou no MIT.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Categorias da DCTFWeb
```
Geral mensal         todos os débitos federais da competência (eSocial + Reinf + MIT);
                     prazo: último dia útil do mês seguinte (art. 6º)
Anual (13º salário)  só o 13º; entrega até 20 de dezembro; se não for dia útil,
                     antecipa para o dia útil imediatamente anterior (art. 7º, I)
Diária               espetáculo desportivo; até o 2º dia útil após o evento (art. 7º, II)
Aferição de obra     construção civil por CNO, aferição pelo Sero (art. 7º, III)
Reclamatória (RT)    contribuições decorrentes de processo trabalhista; prazo do
                     art. 6º (art. 7º, IV)
```
Artigos da IN RFB nº 2.237/2024. As declarações do art. 7º só são exigidas quando houver valores a declarar (§ 2º do art. 7º da IN RFB nº 2.237/2024).

### 2. Pré-requisitos
- eSocial S-1299 da competência fechado e aceito.
- EFD-Reinf R-2099 e R-4099 fechados e aceitos (ou "sem movimento", se for o caso).
- Apurações de IRPJ, CSLL, PIS/COFINS e IPI prontas para lançar no MIT.
- DARFs já pagos identificados (tributos com vencimento antes da entrega, como CSRF e IRRF decendial/quinzenal).
- PER/DCOMP em uso e processos com suspensão judicial mapeados.

### 3. Entrevista mínima
```
Q1: "CNPJ (matriz) + competência. S-1299 fechado? R-2099 e R-4099 fechados?"
Q2: "Apurações de IRPJ/CSLL/PIS/COFINS/IPI prontas para o MIT?"
Q3: "Há DARFs já pagos nesta competência? PER/DCOMP em uso?"
Q4: "Algum débito com exigibilidade suspensa (liminar, depósito judicial)?"
Q5: "A empresa está na CPRB em transição (Lei nº 14.973/2024)? Isso muda os totalizadores."
```

### 4. Fluxo
1. Acessar e-CAC > DCTFWeb.
2. Conferir os débitos que vieram automaticamente:
   - do eSocial: CPP, RAT × FAP, Terceiros, IRRF sobre rendimentos do trabalho;
   - da EFD-Reinf: INSS retido de cessão de mão de obra (R-2010/R-2020), IRRF e CSRF sobre pagamentos a PF e PJ (R-4010/R-4020), CPRB (R-2060).
3. Informar no **MIT** os débitos que não vêm de eventos: IRPJ, CSLL, PIS/COFINS, IPI e outros. Códigos usuais:
   - IRPJ Lucro Presumido: 2089 · Lucro Arbitrado: 5625
   - IRPJ Lucro Real — PJ **obrigada** ao Lucro Real: estimativa mensal 2362 · trimestral 0220 · ajuste anual 2430
   - IRPJ Lucro Real — PJ **optante** (não obrigada): estimativa mensal 5993 · trimestral 3373 · ajuste anual 2456
   - IRPJ instituições financeiras: estimativa 2319 · trimestral 1599 · ajuste anual 2390
   - CSLL Lucro Presumido ou Arbitrado: 2372
   - CSLL Lucro Real (PJ não financeira): estimativa mensal 2484 · trimestral 6012 · ajuste anual 6773
   - CSLL entidades financeiras: estimativa 2469 · trimestral 2030 · ajuste anual 6758
   - PIS cumulativo 8109 · PIS não cumulativo 6912
   - COFINS cumulativa 2172 · COFINS não cumulativa 5856
   - IPI: 5123
   Fonte dos códigos de IRPJ e CSLL: Perguntas e Respostas Pessoa Jurídica da RFB (capítulos de pagamento do IRPJ e da CSLL). Antes de lançar, conferir o código na tabela do próprio MIT.
4. Vincular DARFs pagos (número, data e valor).
5. Vincular PER/DCOMP (número e data).
6. Informar suspensões de exigibilidade (número do processo).
7. Transmitir **até o último dia útil do mês seguinte**.
8. Emitir os DARFs e conferir os vencimentos de cada tributo.

O valor de um débito só muda pela escrituração de origem (eSocial, EFD-Reinf ou MIT). Para corrigir, retificar a origem e encerrar de novo; a DCTFWeb é atualizada depois.

### 5. Vencimentos de pagamento (diferentes do prazo de entrega)
```
INSS empresa, INSS retido, IRRF da folha:   dia 20 do mês seguinte (antecipa se não for dia útil)
CSRF (5952) e IRRF serviços PJ (1708):      até o último dia útil do 2º decêndio do mês
                                             seguinte ao do pagamento (na prática, dia 20)
PIS / COFINS:                                dia 25 do mês seguinte (antecipa se não for dia útil)
IPI:                                         dia 25 do mês seguinte (antecipa se não for dia útil)
IRPJ/CSLL Presumido (trimestral):            último dia útil do mês seguinte ao trimestre
IRPJ/CSLL Real estimativa:                   último dia útil do mês seguinte
```
Antes de afirmar uma data, conferir a Agenda Tributária oficial (gov.br/receitafederal > Agenda Tributária).

### 6. Entregável obrigatório

**a) Tabela débitos esperados × confessados**
```
COMPETÊNCIA __/____ — CNPJ (matriz) __

[ ] eSocial S-1299 OK em __/__/__
[ ] R-2099 OK em __/__/__
[ ] R-4099 OK em __/__/__
[ ] MIT encerrado em __/__/__ (se houver tributo a informar)

DÉBITOS VINDOS DO eSocial / EFD-Reinf:
  CPP empresa.................. R$ __
  RAT × FAP.................... R$ __
  Terceiros.................... R$ __
  INSS retido cessão MO........ R$ __
  IRRF trabalho (0561)......... R$ __
  IRRF PF/PJ (0588, 1708, 3208) R$ __
  CSRF (5952).................. R$ __

DÉBITOS INFORMADOS NO MIT:
  IRPJ......................... R$ __ (cód __)
  CSLL......................... R$ __ (cód __)
  PIS / COFINS................. R$ __ (cód __)
  IPI.......................... R$ __

VINCULAÇÕES:
  DARFs pagos.................. R$ __
  PER/DCOMP.................... R$ __
  Suspensões................... R$ __ (proc. __)

SALDO A PAGAR................. R$ __
```

**b) Plano de retificação, se houver divergência**
1. Retificar primeiro o evento de origem (eSocial, EFD-Reinf ou MIT).
2. Encerrar de novo (S-1299, R-2099/R-4099 ou encerramento do MIT).
3. Conferir a DCTFWeb retificadora gerada e transmitir.
4. Pagar a diferença com acréscimos legais ou pedir restituição/compensação do valor pago a maior (PER/DCOMP Web).

**c) DARFs por código** (lista para o cliente pagar).

**d) Recibo** arquivado na pasta do cliente.

## Erros comuns / pontos de atenção
- Transmitir antes de fechar eSocial e Reinf: débitos ficam faltando.
- Esquecer o MIT (IRPJ, CSLL, PIS/COFINS, IPI): desde 2025 esses débitos não vão mais para a DCTF antiga.
- Vincular DARF de outra competência.
- Retificar a Reinf ou o eSocial e não conferir a DCTFWeb retificadora.
- **Multa** (art. 11 da IN RFB nº 2.237/2024):
  - atraso ou falta de entrega: 2% ao mês-calendário ou fração sobre os tributos informados, ainda que pagos, limitada a 20%;
  - informação incorreta ou omitida: R$ 20,00 para cada grupo de 10 informações;
  - mínimos: R$ 200,00 (declaração sem movimento) e R$ 500,00 (demais casos);
  - reduções da multa por atraso: 50% se entregar antes de procedimento de ofício; 25% se entregar no prazo da intimação;
  - redução dos valores mínimos: 90% para o MEI e 50% para ME/EPP optante do Simples Nacional (não vale em caso de fraude, resistência ou embaraço à fiscalização, nem se a multa não for paga em 30 dias da notificação).

### Casos de borda
- **Empresa em recuperação judicial** (Lei nº 11.101/2005, alterada pela Lei nº 14.112/2020): débitos anteriores seguem o tratamento da RJ/transação; os correntes vão na DCTFWeb normal.
- **Parcelamento** (Lei nº 10.522/2002): o débito original continua confessado; as parcelas são pagas à parte.
- **Liminar ou depósito judicial**: informar o processo; a suspensão vale enquanto a decisão estiver vigente.
- **Filiais**: DCTFWeb e DARF são gerados por empresa (matriz), reunindo todos os estabelecimentos.
- **Reclamatória trabalhista**: categoria própria; recolhimento conforme orientação do Manual da DCTFWeb.

### Quando encaminhar para outra skill
- Cruzamento entre SPEDs → `revisao-fiscal-cruzamento-sped`
- Débitos atrasados → `parcelamento-receita-federal`
- Auto de infração → `resposta-fiscalizacao-intimacao`
- eSocial pendente → `esocial-eventos-periodicos`; Reinf pendente → `efd-reinf`

### Autoavaliação
- [ ] eSocial e Reinf fechados antes da DCTFWeb?
- [ ] MIT preenchido e encerrado quando havia tributo a informar?
- [ ] Cada débito esperado presente?
- [ ] Pagamentos e compensações vinculados?
- [ ] Suspensões com processo informado?
- [ ] Transmitida até o último dia útil do mês seguinte?
- [ ] Recibo arquivado?

## Perguntas que o usuário costuma fazer
- **"O prazo ainda é dia 25?"** Não. Desde as competências de 2025 é o último dia útil do mês seguinte (IN RFB nº 2.248/2025).
- **"O valor do eSocial veio diferente na DCTFWeb. Corrijo na DCTFWeb?"** Não dá. A DCTFWeb não calcula nada: corrija o evento no eSocial e feche de novo.
- **"Empresa do Presumido sem folha precisa de DCTFWeb?"** Se houver tributo a informar no MIT, sim. Sem nenhum fato gerador, entrega a DCTFWeb do primeiro mês sem movimento e fica dispensada nos meses seguintes, até voltar a ter fato gerador (art. 6º, § 2º, II, da IN RFB nº 2.237/2024).

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): documento DOCX.
- Este padrão prevalece sobre outros formatos citados acima, exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- IN RFB nº 2.237/2024 — DCTFWeb para fatos geradores a partir de 01/01/2025: art. 6º (prazo mensal e sem movimento), art. 7º (13º, diária, aferição, reclamatória), art. 11 (multas).
- IN RFB nº 2.248/2025 — deu nova redação ao art. 6º da IN RFB nº 2.237/2024: último dia útil do mês seguinte.
- IN RFB nº 2.005/2021 — regra anterior (fatos geradores até 12/2024).
- Lei nº 10.833/2003, art. 35 — prazo de recolhimento da CSRF.
- Lei nº 14.973/2024 — reoneração gradual da folha (CPRB em transição).
- Lei nº 10.522/2002 — parcelamento de débitos federais.
- Decreto nº 70.235/1972 — processo administrativo fiscal.
- Manual da DCTFWeb e Perguntas e Respostas da DCTFWeb (gov.br/receitafederal).
- Perguntas e Respostas Pessoa Jurídica da RFB — códigos de receita do IRPJ e da CSLL.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
