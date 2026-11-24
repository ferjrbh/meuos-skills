---
name: reforma-tributaria-transicao
description: "Orienta a transição da Reforma Tributária do Consumo (Emenda Constitucional nº 132/2023, LC nº 214/2025 e LC nº 227/2026, que instituiu o Comitê Gestor do IBS): ano-teste 2026 (CBS 0,9% + IBS 0,1% destacados), cronograma de 2026 a 2033, fases de obrigatoriedade dos campos de IBS/CBS nos documentos fiscais, opção do Simples pelo regime regular de IBS/CBS (Resolução CGSN nº 186/2026), Imposto Seletivo, reduções de alíquota, cashback, split payment e créditos. Acionar quando o usuário disser \"reforma tributária\", \"IBS\", \"CBS\", \"Imposto Seletivo\", \"LC 214\", \"LC 227\", \"EC 132\", \"Comitê Gestor\", \"ano-teste\", \"destaque na nota\", \"rejeição 1115\", \"CRT 3\", \"regime regular do Simples\", \"split payment\", \"alíquota de referência\", \"cashback\", \"crédito de IBS/CBS\", \"período de transição\" ou perguntar como a reforma afeta a nota fiscal, a apuração ou o regime do cliente."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Reforma Tributária do Consumo — transição 2026–2033

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Traduz o cronograma e as regras de transição da Reforma em ações práticas para o escritório e para o cliente: o que fazer na nota fiscal em 2026, quando cada documento passa a exigir IBS/CBS, o que muda em 2027 (CBS, Imposto Seletivo, IPI zero), como fica o Simples e como simular o impacto. Sempre confere a orientação oficial vigente antes de responder.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Regra de ouro.** A regulamentação muda com frequência (atos conjuntos RFB/CGIBS, notas técnicas de documentos fiscais, resoluções do CGSN). Antes de responder sobre prazo, alíquota ou obrigação, consultar a página "Reforma Tributária do Consumo" da Receita Federal (gov.br/receitafederal), o Portal da NF-e e o Perguntas e Respostas do Simples Nacional (para optantes).

## Quando usar
- Dúvidas sobre IBS, CBS, Imposto Seletivo e o cronograma.
- Adequação de ERP e emissor de notas (novos grupos de campos).
- Decisão do optante do Simples sobre o regime regular de IBS/CBS.
- Simulação de impacto por cliente.

Apuração atual de PIS/COFINS, ICMS, ISS, IPI ou Simples → skills específicas.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite. Nenhuma opção de regime (por exemplo, a do Simples) é feita pela skill.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Cronograma da transição
| Ano | O que acontece |
|---|---|
| 2026 | Ano-teste: CBS 0,9% e IBS 0,1% destacados nos documentos fiscais, compensáveis com PIS/COFINS; dispensa de recolhimento para quem cumpre as obrigações acessórias. ICMS, ISS, PIS, COFINS e IPI continuam normais. |
| 2027 | CBS em vigor; **PIS e COFINS extintos**; Imposto Seletivo em vigor; **IPI com alíquota zero**, exceto produtos com industrialização incentivada na ZFM. IBS a 0,1% (0,05% estadual + 0,05% municipal), com a alíquota da CBS reduzida em 0,1 ponto percentual. |
| 2028 | Igual a 2027 (IBS ainda a 0,1% e CBS reduzida em 0,1 ponto percentual). |
| 2029 | ICMS e ISS a 90% das alíquotas; IBS sobe proporcionalmente. |
| 2030 | ICMS e ISS a 80%. |
| 2031 | ICMS e ISS a 70%. |
| 2032 | ICMS e ISS a 60%. |
| 2033 | ICMS e ISS extintos; IBS e CBS plenos. |

Base: arts. 125 a 133 do ADCT (incluídos pela EC nº 132/2023) e LC nº 214/2025; material oficial de capacitação CFC/RFB sobre a Reforma (Receita Federal, maio/2026). As alíquotas de referência da CBS e do IBS são fixadas por resolução do Senado Federal: nas simulações, usar só a alíquota divulgada oficialmente na data e identificar qualquer outro número como estimativa.

### 2. Normas que regulamentam (situação em 15/11/2026)
- **LC nº 214/2025**: institui IBS, CBS e Imposto Seletivo (1ª etapa da regulamentação).
- **LC nº 227/2026** (sancionada em 13/01/2026, publicada em 14/01/2026, originada do PLP nº 108/2024): institui o **Comitê Gestor do IBS (CGIBS)**, o processo administrativo do IBS, a distribuição da receita entre estados e municípios e regras de transição (inclusive aproveitamento de saldos de ICMS); altera a LC nº 214/2025 e trata do ITCMD.
- **Resolução CGSN nº 186/2026** (09/04/2026), com os prazos alterados pela **Resolução CGSN nº 194/2026**: opção pelo Simples para 2027 (até 15/10/2026) e opção pelo regime regular de IBS/CBS (até 30/10/2026).
- **Ato Conjunto RFB/CGIBS nº 4/2026** (30/07/2026): cronograma em 4 fases de obrigatoriedade dos campos de IBS/CBS.
- **LC nº 224/2025**: não é da Reforma do Consumo, mas reduz benefícios federais e majora a presunção do Lucro Presumido acima de R$ 5 milhões em 2026 (skill `apuracao-lucro-presumido`).

### 3. O que fazer em 2026 (ano-teste)
1. **Documentos fiscais**: destacar CBS (0,9%) e IBS (0,1%) por item. Grupos novos criados pela NT 2025.002 da NF-e (grupos UB e W03). Conferir na nota técnica vigente do Portal da NF-e se, em 2026, os valores de IBS/CBS entram ou não no total do documento antes de orientar o ERP.
2. **Fases de obrigatoriedade** (Ato Conjunto RFB/CGIBS nº 4/2026):

| Fase | Data | Escopo |
|---|---|---|
| 1 | 03/08/2026 | NF-e, NFC-e, CT-e, CT-e OS, MDF-e, GTV-e, NF3e, DC-e, NFS-e Via, BP-e |
| 2 | 01/10/2026 | NFS-e de serviços gerais (ISS) |
| 3 | 15/11/2026 | Eventos periódicos da DeRE (balancete, aplicações, deduções, títulos) |
| 4 | 01/12/2026 | Plataformas digitais, subitens 1.03/1.05/1.09/16.01, bens imateriais, condomínios, locações |

   Exceções da fase 1: monofásicos e importação de bens materiais → 01/01/2027. **Simples e MEI ficam fora das 4 fases → 04/01/2027.**
3. **Rejeição 1115** (NF-e sem IBS/CBS): regime normal (CRT 3) desde 03/08/2026; Simples e MEI (CRT 1, 2 e 4) a partir de 04/01/2027.
4. **Dispensa de recolhimento**: quem emite os documentos corretamente e cumpre as obrigações acessórias não recolhe a CBS e o IBS de teste; os valores são compensáveis com PIS/COFINS. Confirmar o tratamento das penalidades no período de adaptação antes de orientar o cliente.
5. **Diagnóstico por cliente**: (a) o ERP/emissor já gera os grupos novos? (b) cadastro de produtos e serviços com NCM/NBS e classificação tributária (cClassTrib) corretos; (c) clientes B2B que vão exigir crédito; (d) impacto no preço e nos contratos.

### 4. Simples Nacional
- O Simples continua. A partir de 2027 o optante pode escolher apurar **IBS e CBS pelo regime regular** (fora do DAS, com crédito pleno para o comprador), mantendo IRPJ, CSLL, CPP e demais tributos no DAS.
- **Opção semestral**: a opção fica disponível em setembro (efeito no 1º semestre do ano seguinte) e em março (efeito no 2º semestre do mesmo ano). A primeira janela, prorrogada pela Resolução CGSN nº 194/2026, foi de 01/09 a 30/10/2026 (efeitos de janeiro a junho de 2027); o cancelamento, irretratável, é possível de 03/11 a 20/12/2026. Quem não optou recolhe IBS/CBS pelo DAS de janeiro a junho de 2027 e pode optar em março de 2027 para o 2º semestre. Quem já optou não precisa repetir a opção a cada semestre, salvo para mudar (pergunta 2.27 do Perguntas e Respostas do Simples Nacional, atualizado em 09/10/2026; Manual da Opção pelo Regime Regular do IBS e da CBS no Portal do Simples).
- Não se aplica ao MEI (SIMEI). Empresa em início de atividade tem prazos de opção próprios: conferir no Manual da Opção pelo Regime Regular do IBS e da CBS, no Portal do Simples Nacional.
- **Crédito do comprador**: fornecedor no DAS → crédito limitado ao valor efetivamente recolhido no DAS; fornecedor no regime regular → crédito pleno.
- **Quando tende a compensar**: carteira majoritariamente B2B (clientes no Lucro Real/Presumido), indústria ou atacado vendendo para redes, muitos insumos creditáveis. **Quando não**: carteira B2C, serviços com poucos insumos, prioridade em simplicidade. Decidir com simulação.

### 5. Conceitos-chave
- **IBS** (estados e municípios) e **CBS** (União): IVA dual, base ampla, cobrança "por fora", princípio do destino, não cumulatividade ampla com crédito financeiro.
- **Imposto Seletivo** (a partir de 2027): bens e serviços prejudiciais à saúde ou ao meio ambiente (ex.: fumo, bebidas alcoólicas e açucaradas, veículos, extração mineral). Conferir a lista da LC nº 214/2025.
- **Reduções de alíquota**: 60% (por exemplo, saúde, educação, dispositivos médicos, medicamentos, transporte coletivo, insumos agropecuários, produções artísticas), 30% (profissões intelectuais regulamentadas, como advocacia, contabilidade, engenharia), 100% (cesta básica nacional e outros casos listados). Sempre conferir a lista e os anexos da LC nº 214/2025 pelo NCM/NBS.
- **Cashback**: devolução de parte do tributo a famílias de baixa renda inscritas no CadÚnico.
- **Split payment**: recolhimento no momento da liquidação financeira, com implantação gradual.
- **Regimes específicos**: combustíveis, serviços financeiros, operações com imóveis, planos de saúde, cooperativas, entre outros.
- **Saldos credores** de ICMS, PIS e COFINS: há regras próprias de aproveitamento na transição (ADCT, na redação da EC nº 132/2023, LC nº 214/2025 e LC nº 227/2026). Antes de informar prazo ou forma de uso ao cliente, localizar o dispositivo aplicável ao tributo e citar o artigo.

### 6. Como responder
1. Identificar regime e atividade do cliente (CNAE, NCM/NBS, B2B × B2C, UF/município).
2. Consultar a orientação vigente (RFB, Portal da NF-e, CGIBS e, para optantes, Portal do Simples Nacional).
3. Responder com: regra atual + o que muda e quando + ação prática + fonte (norma e artigo).
4. Simulação de impacto: carga atual × carga projetada com a alíquota de referência **divulgada oficialmente** na data; se ainda não houver alíquota oficial, usar a estimativa marcada como estimativa e mostrar sensibilidade.

## Erros comuns / pontos de atenção
- Dizer que o IBS "entra em 2027 em vigor pleno" ou que o ICMS acaba em 2032 (acaba em 2033).
- Tratar a alíquota de referência estimada como definitiva.
- Achar que o Simples acaba, ou que o município ou o cliente decide o tratamento sem a opção formal.
- Esquecer que Simples e MEI só passam a ter rejeição por falta de IBS/CBS em 04/01/2027.
- Responder com material anterior à Resolução CGSN nº 186/2026, à LC nº 227/2026 ou ao Ato Conjunto RFB/CGIBS nº 4/2026 sem conferir a norma atual.
- Confundir a LC nº 224/2025 (ajuste fiscal) com a Reforma do Consumo.
- Informar prazo de uso de saldo credor de ICMS/PIS/COFINS sem citar o dispositivo.

## Perguntas que o usuário costuma fazer
- **"Preciso pagar CBS/IBS em 2026?"** Em regra não: quem destaca corretamente e cumpre as obrigações acessórias fica dispensado; os valores são compensáveis.
- **"Meu cliente do Simples precisa destacar IBS/CBS?"** A obrigação com rejeição começa em 04/01/2027 para CRT 1, 2 e 4.
- **"Perdi a janela de setembro/outubro de 2026, e agora?"** De janeiro a junho de 2027 o IBS/CBS segue pelo DAS; a próxima janela é março de 2027, com efeito no 2º semestre de 2027.

## Formato de entrega
- Cálculos e simulações de impacto: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres e comunicados a clientes: documento DOCX.

## Base legal usada nesta skill
- Emenda Constitucional nº 132/2023 — arts. 156-A e 195, V, da Constituição e arts. 125 a 133 do ADCT (transição).
- LC nº 214/2025 — institui IBS, CBS e Imposto Seletivo; regimes diferenciados, cashback, split payment.
- LC nº 227/2026 — Comitê Gestor do IBS, processo administrativo do IBS, transição e alterações na LC nº 214/2025.
- Resolução CGSN nº 186/2026, alterada pela Resolução CGSN nº 194/2026 — opção pelo Simples para 2027 e pelo regime regular de IBS/CBS.
- Ato Conjunto RFB/CGIBS nº 4/2026 — fases de obrigatoriedade nos documentos fiscais.
- NT 2025.002 da NF-e — grupos de IBS/CBS e rejeição 1115.
- LC nº 224/2025 — ajuste fiscal de 2026.
- Perguntas e Respostas do Simples Nacional (CGSN, atualizado em 09/10/2026), pergunta 2.27.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
