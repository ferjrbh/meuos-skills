---
name: analisar-relatorio-contabil
description: "Analisa relatórios contábeis com muitos lançamentos (razão, diário, balancete, livro contábil ou planilha de lançamentos) à luz da ITG 2000 (R1) e da NBC TG 1000 (R1) e entrega diagnóstico consolidado — inventário, análise lançamento a lançamento, classificação por gravidade e sugestões de correção. Use quando o usuário enviar razão, diário, balancete, balanço de verificação ou planilha de lançamentos para revisão, ou pedir \"auditoria de escrituração\", \"revisar escrituração do mês\", \"analisar livro razão\", \"diagnóstico contábil\" ou \"revisar fechamento\", mesmo sem citar a norma."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Analisar Relatório Contábil

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Revisa um conjunto de lançamentos (razão, diário ou planilha) e aponta, um a um, o que está certo, o que tem ressalva e o que precisa ser corrigido, com a correção sugerida e a norma. Termina com um resumo para o contador e recomendações de processo.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Revisão da escrituração do mês antes de fechar.
- Cliente novo: diagnóstico da escrituração recebida do escritório anterior.
- Para um único lançamento, usar `analisar-lancamento-contabil`.
- Para a análise de saldos e indicadores do balancete (integridade, natureza, variações), usar `balancete-analise`.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### Passo 1 — Conferir a leitura e fazer o inventário
- Se o relatório veio em PDF, os totais lidos têm de bater com os totais impressos. Divergência é problema de extração do PDF (OCR ou texto duplicado), não de contabilidade.
- Identificar a entidade, o período e o tipo de relatório.
- Contar o total de lançamentos e de contas.
- Conferir o total de débitos igual ao total de créditos do relatório inteiro.

### Passo 2 — Análise de cada lançamento
Para cada lançamento, verificar:
- Elementos obrigatórios do registro (data, conta devedora, conta credora, histórico, valor, número de identificação ligado ao documento) — ITG 2000 (R1).
- Equilíbrio débito × crédito.
- Competência: reconhecido no período em que o fato ocorreu (art. 177 da Lei nº 6.404/1976; Seção 2 da NBC TG 1000 (R1)).
- Mensuração pelo valor da transação (valor do documento).
- Classificação da conta: natureza correta, circulante × não circulante (Seção 4 da NBC TG 1000 (R1)), custo × despesa.
- Qualidade do histórico.

### Passo 3 — Procurar padrões que um lançamento isolado não mostra
- Mesmo documento lançado duas vezes (mesmo valor, data e contraparte).
- Despesa lançada duas vezes: uma pela provisão e outra pelo pagamento.
- Provisões mensais ausentes (férias, 13º, depreciação) ou sem movimento no período.
- Contas "Outros", "Diversos" ou transitórias recebendo valores relevantes.
- Lançamentos de ajuste no último dia sem documento.
- Lançamentos com data de períodos já encerrados.

### Passo 4 — Classificação por gravidade
| Nível | Descrição | Exemplo |
|---|---|---|
| Crítico | Compromete a validade ou distorce resultado, patrimônio ou tributo | Débito diferente do crédito, data ausente, lançamento em duplicidade |
| Moderado | Exige correção, mas não invalida | Histórico vago, classificação incorreta, competência errada |
| Observação | Melhoria recomendada | Conta poderia ser mais específica |

### Passo 5 — Formato de saída
Sempre com estas seções, nesta ordem:
1. **Resumo executivo.** Tabela com totais por status (aprovados, com ressalvas, reprovados) e contagem por gravidade. Efeito estimado das correções no resultado, quando calculável.
2. **Diagnóstico por lançamento.** Para cada lançamento com problema: identificação, problema, correção sugerida (estorno, transferência ou complementação, com o lançamento de correção) e base normativa (norma e item).
3. **Lançamentos aprovados.** Lista (número e breve descrição). Nunca omitir.
4. **Recomendações gerais.** Até 5 recomendações de processo ou padronização.

## Erros comuns / pontos de atenção
- Corrigir apagando o lançamento já registrado: a correção é por novo lançamento, com trilha (ITG 2000 (R1), itens 31 a 36).
- Olhar só o total do razão: erros de sinais contrários se anulam.
- Tratar decisão conhecida do cliente como erro todo mês: registrar como intencional (nível INTENCIONAL da skill `balancete-analise`).

## Perguntas que o usuário costuma fazer
- **"O relatório tem 3 mil lançamentos. Precisa listar todos?"** Os com problema, um a um; os aprovados podem vir agrupados por conta ou lote, com a quantidade, desde que nenhum fique de fora da contagem.
- **"Posso mandar o diagnóstico ao cliente?"** O diagnóstico é para o contador. Ao cliente vai o relatório mensal, depois das correções.

## Restrições
- Não registrar, aprovar definitivamente nem corrigir lançamentos: apenas diagnosticar.
- Citar a norma e o item em caso de dúvida normativa.
- Nunca omitir lançamentos: todos entram na contagem, no mínimo no bloco de aprovados.

## Base legal usada nesta skill
- ITG 2000 (R1) — Escrituração Contábil (CFC): elementos do registro e retificação (itens 31 a 36).
- NBC TG 1000 (R1) — Contabilidade para PMEs: Seção 2 (competência), Seção 4 (balanço patrimonial), Seção 10 (retificação de erro). Pequenas empresas e microentidades podem adotar a NBC TG 1001 ou a NBC TG 1002 (vigentes para exercícios iniciados a partir de 01/01/2023): conferir a norma adotada pelo cliente.
- Art. 177 da Lei nº 6.404/1976 (Lei das S.A.): competência.
- Arts. 1.179 a 1.195 da Lei nº 10.406/2002 (Código Civil): escrituração.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
