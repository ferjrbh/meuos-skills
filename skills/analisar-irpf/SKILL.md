---
name: analisar-irpf
description: "Analisa a declaração de IRPF pré-preenchida (Receita Federal) cruzando com os documentos do cliente — informes de rendimentos, recibos médicos, notas de corretagem, extratos de previdência, comprovantes de educação — para achar divergências, deduções não aproveitadas e riscos de malha. Usa os parâmetros do IRPF 2026 (ano-calendário 2025) e alerta o que muda no IRPF 2027 pela Lei nº 15.270/2025 (redução anual, IRPFM, dividendos). Gera planilha Excel com achados, riscos e ações. Acionar quando o usuário disser \"imposto de renda\", \"IRPF\", \"declaração IR\", \"pré-preenchida\", \"informe de rendimentos\", \"dedução IR\", \"restituição\", \"malha fina\", \"carnê-leão\", \"ganho de capital\", \"renda variável IR\", ou pedir para \"conferir\", \"revisar\", \"organizar\" a declaração. Para MONTAR a declaração do zero, usar `elaborar-irpf-completa`."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Análise de IRPF (revisão da pré-preenchida)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Revisa a declaração pré-preenchida do cliente contra os documentos que ele enviou. Aponta rendimento omitido, dedução indevida ou não aproveitada, bens com saldo divergente e DARFs de renda variável ou ganho de capital faltantes. Entrega uma planilha de diagnóstico e um resumo claro para o contador agir.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Cliente enviou a pré-preenchida e documentos e quer conferência.
- Verificação preventiva antes de transmitir ou depois de transmitir (para retificar).
- Não usar para montar a declaração do zero (`elaborar-irpf-completa`) nem para responder intimação de malha (`diagnosticar-malha-fina-pf`).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Despesas médicas revelam dado de saúde (dado sensível — art. 5º, II, da LGPD): na resposta do chat, citar só totais e o tipo de problema, nunca o diagnóstico ou o procedimento.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Nome do arquivo de saída sem CPF: `Diagnostico_IRPF_<CLIENTE>_<AnoCalendario>.xlsx`.

## Passo a passo (instruções para o agente de IA)

### Passo 0 — Confirmar o exercício
Perguntar qual declaração está sendo analisada. Esta skill está parametrizada para o **IRPF 2026 (exercício 2026, ano-calendário 2025)**. Se for outro ano, pesquisar os limites no Perguntas e Respostas do ano em gov.br/receitafederal antes de prosseguir.

### Passo 1 — Coletar e classificar os documentos
| Tipo | Exemplos |
|------|---------|
| Declaração pré-preenchida | PDF exportado do e-CAC / Meu Imposto de Renda |
| Informe de rendimentos | Empregador, banco, previdência privada, corretora, INSS |
| Recibo / nota de saúde | Consultas, exames, internações, plano de saúde, Receita Saúde |
| Comprovante de educação | Escola, faculdade, pós-graduação |
| Nota de corretagem / informe B3 | Ações, FII, BDR, ETF, day trade |
| Extrato de previdência | PGBL, VGBL |
| Escritura / ITBI / contrato | Imóveis comprados ou vendidos |
| Outro | Descrever |

Se faltar a pré-preenchida, avisar: "Para a análise completa, preciso da declaração pré-preenchida exportada do e-CAC em PDF. Você tem esse arquivo?"

### Passo 2 — Extrair os dados da declaração
**2.1 Rendimentos tributáveis** — de PJ (CNPJ da fonte, valor, IRRF); de PF e do exterior (aluguel, autônomo, carnê-leão).
**2.2 Rendimentos sujeitos à tributação exclusiva/definitiva** — 13º, aplicações financeiras, JCP, PLR (ficha própria, não somar aos tributáveis).
**2.3 Rendimentos isentos e não tributáveis** — lucros e dividendos (isentos para resultados até 2025), indenizações rescisórias, poupança, LCI, LCA, CRI, CRA, ganho isento na venda de imóvel único até R$ 440.000,00, vendas de ações até R$ 20.000,00 no mês.
**2.4 Deduções** — previdência oficial, PGBL, dependentes (nome, CPF, parentesco), instrução, saúde, pensão alimentícia judicial ou por escritura.
**2.5 Bens e direitos** — imóveis, veículos, contas e aplicações (saldo em 31/12/2024 e 31/12/2025), participações, criptoativos, bens no exterior.
**2.6 Renda variável** — resultado mensal (operações comuns e day trade separados), DARFs pagos (código **6015** para ambos), prejuízos a compensar.
**2.7 Dívidas e ônus** — financiamentos e empréstimos.

### Passo 3 — Cruzar com os documentos
**3.1 Rendimentos × informes**
- Somar os informes de rendimentos tributáveis e comparar com a ficha "Rendimentos Tributáveis Recebidos de PJ".
- Alerta: diferença acima de R$ 50,00 ou CNPJ do informe ausente na declaração (a fonte informou à Receita pela EFD-Reinf/eSocial — a DIRF foi extinta para fatos a partir de 2025).

**3.2 Saúde × recibos**
- Cada recibo precisa de nome, CPF ou CNPJ do prestador, beneficiário (titular, dependente ou alimentando) e valor.
- Não dedutíveis: medicamentos, inclusive vacinas, salvo quando integram a conta emitida pelo estabelecimento hospitalar (pergunta 392 do Perguntas e Respostas IRPF 2026); óculos e lentes (não são aparelho ortopédico nem prótese — art. 73 do Decreto nº 9.580/2018 (RIR/2018)); academia.
- Sem limite de valor, mas valores altos geram alerta na pré-preenchida e risco de malha.
- Conferir com a DMED do prestador e com recibos emitidos pelo Receita Saúde.

**3.3 Instrução × comprovantes**
- Limite de **R$ 3.561,50 por pessoa** no ano-calendário 2025 (art. 8º, II, "b", da Lei nº 9.250/1995).
- Não dedutíveis: cursos livres, idiomas, material escolar, uniforme.

**3.4 PGBL × extrato**
- Dedutível até **12% dos rendimentos tributáveis** da declaração, desde que o contribuinte contribua para a previdência oficial (ou seja aposentado pelo regime oficial).
- VGBL não é dedutível — alertar se aparecer como dedução.

**3.5 Bens × evolução patrimonial**
- Imóvel adquirido no ano com escritura/ITBI.
- Saldos de aplicações batem com os informes em 31/12.
- Conta corrente e poupança com saldo acima de R$ 140,00 em 31/12 devem ser declaradas.
- Variação patrimonial maior que a renda disponível = risco (o desconto simplificado não justifica acréscimo patrimonial).

**3.6 Renda variável × notas de corretagem**
- Resultado mensal = vendas − custo médio − corretagem e emolumentos.
- Ações no mercado à vista: isenção se o total de VENDAS do mês for até R$ 20.000,00; acima, 15% sobre o lucro. Day trade: 20%, sem isenção. Ambos em DARF **6015**, até o último dia útil do mês seguinte.
- FII: rendimento distribuído isento para PF só se o fundo tiver **no mínimo 100 cotistas**, cotas negociadas exclusivamente em bolsa ou balcão organizado, o cotista tiver menos de 10% das cotas/rendimentos e as cotas de pessoas físicas ligadas não somarem 30% ou mais (art. 3º, parágrafo único, da Lei nº 11.033/2004, com redação da Lei nº 14.754/2023). Venda de cota de FII: 20%, sem isenção.
- Obrigatoriedade: alienações em bolsa acima de R$ 40.000,00 no ano ou com ganho tributável obrigam a declarar.

**3.7 Lucros e pró-labore**
- Cliente sócio ou MEI: conferir pró-labore (tributável) e lucros distribuídos (isentos, resultados até 2025).

### Passo 4 — Planilha de diagnóstico (skill `xlsx`)
Abas:
1. **Resumo Executivo** — total de pontos (críticos, alertas, oportunidades) e status geral: SEM DIVERGÊNCIA CRÍTICA / ATENÇÃO NECESSÁRIA / RISCO DE MALHA.
2. **Divergências** — `Categoria | Item | Valor na declaração | Valor nos documentos | Diferença | Risco | Ação recomendada | Base legal`. Risco: **CRÍTICO** (pode gerar malha ou autuação — ex.: rendimento omitido), **ALERTA** (inconsistência a investigar — ex.: recibo sem CPF/CNPJ), **OPORTUNIDADE** (dedução legal não aproveitada).
3. **Rendimentos** — informe × declarado, por fonte.
4. **Despesas de saúde** — prestador, CPF/CNPJ, beneficiário, valor, status (OK / sem identificação / não dedutível). Sem descrever procedimento.
5. **Bens e Direitos** — declarado × documento; variação justificada?
6. **Renda Variável** — mês a mês: resultado, imposto, DARF pago, diferença.
7. **Checklist de Documentos** — esperados × recebidos, com instrução de onde obter cada ausente.
8. **Simplificada × Completa** — comparar o desconto simplificado (20% dos rendimentos tributáveis, limitado a **R$ 16.754,34**) com as deduções legais.

### Passo 5 — Apresentar os achados no chat
1. Problemas críticos (até 3 itens).
2. Alertas a verificar.
3. Oportunidades (economia estimada em R$).
4. Próximos passos (retificar? juntar documento? pagar DARF de renda variável em atraso com multa de mora de 0,33% ao dia, limitada a 20%, mais Selic — art. 61 da Lei nº 9.430/1996?).
5. Aviso para o IRPF 2027 (ano-calendário 2026), se o perfil do cliente for afetado (ver referência abaixo).

### Referência rápida — IRPF 2026 (exercício 2026, ano-calendário 2025)
| Item | Valor |
|------|-------|
| Prazo de entrega | 23/03/2026 a 29/05/2026 (Instrução Normativa RFB nº 2.312/2026) |
| Obrigatoriedade — rendimentos tributáveis | acima de R$ 35.584,00 |
| Obrigatoriedade — isentos/exclusivos | acima de R$ 200.000,00 |
| Obrigatoriedade — bens em 31/12/2025 | acima de R$ 800.000,00 |
| Obrigatoriedade — atividade rural | receita bruta acima de R$ 177.920,00 |
| Obrigatoriedade — bolsa | alienações acima de R$ 40.000,00 ou ganho tributável |
| Tabela anual — faixa isenta | até R$ 28.467,20 |
| Desconto simplificado | 20% dos rendimentos tributáveis, limitado a R$ 16.754,34 |
| Dedução por dependente | R$ 2.275,08/ano |
| Instrução | R$ 3.561,50/pessoa/ano |
| Pais/avós como dependentes | rendimentos (tributáveis ou não) até R$ 28.467,20 em 2025 |
| PGBL | até 12% dos rendimentos tributáveis |
| Imóvel único isento | venda até R$ 440.000,00, sem outra alienação de imóvel nos últimos 5 anos |
| Ações (mercado à vista) | vendas até R$ 20.000,00/mês isentas |
| Bens de pequeno valor | alienações até R$ 35.000,00/mês isentas (R$ 20.000,00 para ações em balcão) |
| Quotas do saldo a pagar | até 8; mínimo R$ 50,00; abaixo de R$ 100,00, quota única; 1ª em 29/05/2026 |
| Multa por atraso na entrega | 1% ao mês sobre o imposto devido, mínimo R$ 165,74, máximo 20% |

Fonte: Perguntas e Respostas IRPF 2026 (Receita Federal, versão 1.00 de 23/04/2026) e notícia do Ministério da Fazenda de 16/03/2026.

### O que muda no IRPF 2027 (ano-calendário 2026) — Lei nº 15.270/2025
- **Redução anual do imposto** (art. 11-A da Lei nº 9.250/1995): rendimentos tributáveis até R$ 60.000,00 → imposto zerado (redução de até R$ 2.694,15); de R$ 60.000,01 a R$ 88.200,00 → redução = R$ 8.429,73 − 0,095575 × rendimentos; acima de R$ 88.200,00 → sem redução.
- **Lucros e dividendos**: retenção de 10% quando uma mesma PJ paga a uma mesma PF mais de R$ 50.000,00 no mês (art. 6º-A da Lei nº 9.250/1995). Lucros de resultados até 2025, com distribuição aprovada até 31/12/2025, ficam fora.
- **IRPFM (imposto mínimo)**: renda total acima de R$ 600.000,00 no ano; alíquota cresce de 0% a 10% (fórmula: renda ÷ 60.000 − 10), chegando a 10% a partir de R$ 1.200.000,00; abate o IR já pago e há redutor quando a soma com a tributação efetiva da empresa supera a alíquota nominal de IRPJ + CSLL da PJ (34%, 40% ou 45%, conforme o tipo de empresa) (arts. 16-A e 16-B da Lei nº 9.250/1995).
- Já no IRPF 2026, avisar o cliente de alta renda para guardar informes de dividendos de 2026 e as atas de aprovação de lucros até 2025.

## Erros comuns / pontos de atenção
- Usar limites de outro ano-calendário.
- Somar rendimentos de tributação exclusiva (13º, aplicações) aos tributáveis.
- Usar código 6010 para day trade: o código de renda variável da PF é 6015.
- Aplicar a isenção de FII com o critério antigo de 50 cotistas (hoje são 100).
- Deduzir VGBL.
- Confiar na pré-preenchida sem conferir: ela traz o que as fontes informaram, inclusive erros.

## Perguntas que o usuário costuma fazer
- **"A pré-preenchida está certa?"** Ela parte do que as fontes informaram; a análise verifica se falta ou sobra algo.
- **"Vale a pena a completa?"** Compare as deduções legais com o desconto simplificado de até R$ 16.754,34.
- **"Recebi dividendos em 2026. Muda algo nesta declaração?"** Não para o IRPF 2026 (ano 2025). Os dividendos de 2026 entram no IRPF 2027, com as novas regras.

## Base legal usada nesta skill
- Lei nº 9.250/1995 — art. 4º (deduções mensais), art. 8º (deduções anuais: saúde, instrução, dependentes, PGBL), art. 10 (desconto simplificado), arts. 6º-A, 11-A, 16-A e 16-B (incluídos pela Lei nº 15.270/2025), art. 22 (bens de pequeno valor), art. 23 (imóvel único).
- Lei nº 7.713/1988 — art. 6º (rendimentos isentos).
- Lei nº 9.249/1995 — art. 10 (lucros e dividendos).
- Lei nº 11.033/2004 — art. 3º (isenções, FII), com redação da Lei nº 14.754/2023.
- Lei nº 11.482/2007 — tabela progressiva anual.
- Lei nº 13.259/2016 — alíquotas do ganho de capital (15% a 22,5%).
- Lei nº 9.430/1996 — art. 61 (multa e juros de mora).
- Lei nº 15.270/2025 — redução do IR, tributação de dividendos e IRPFM.
- Decreto nº 9.580/2018 (RIR/2018) — regulamento do imposto de renda.
- Instrução Normativa RFB nº 1.500/2014 — normas gerais do IRPF.
- Instrução Normativa RFB nº 2.312/2026 — regras e prazo do IRPF 2026.
- Lei nº 13.709/2018 (LGPD) — arts. 5º, II, e 6º, III (dado sensível e necessidade).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
