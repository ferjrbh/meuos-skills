---
name: analisar-lancamento-contabil
description: "Analisa um lançamento contábil individual antes do registro definitivo — elementos obrigatórios do registro, equilíbrio débito e crédito, qualidade do histórico, competência, classificação das contas e forma de retificação (estorno, transferência, complementação) — à luz da ITG 2000 (R1) e da NBC TG 1000 (R1). Use quando o usuário mencionar \"lançamento contábil\", \"escrituração\", \"débito e crédito\", \"partida dobrada\", \"histórico contábil\", \"estorno\", \"transferência\", \"complementação\", \"lançamento extemporâneo\", ou pedir para revisar, validar ou corrigir um único lançamento, mesmo sem citar a norma."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Analisar Lançamento Contábil (unitário)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Confere um lançamento contábil por vez: se tem todos os elementos que a norma de escrituração exige, se débitos e créditos fecham, se o histórico explica o fato, se está na competência certa e se as contas fazem sentido. Se houver erro, indica a forma correta de retificar.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Revisão de um lançamento manual antes de gravar no sistema.
- Dúvida sobre como corrigir um lançamento já feito.
- Para muitos lançamentos de uma vez (razão, diário, balancete), usar a skill `analisar-relatorio-contabil`.
- Para modelos de lançamento por operação, usar `lancamentos-contabeis-padrao`.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Histórico de lançamento de folha ou pró-labore com nome e valor de pessoa: analisar sem reproduzir.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Elementos obrigatórios do registro (ITG 2000 (R1))
- Data do registro contábil (a data em que o fato ocorreu).
- Conta devedora.
- Conta credora.
- Histórico que represente a essência econômica da transação, ou código de histórico padronizado que conste de tabela auxiliar.
- Valor do registro.
- Número de identificação do lançamento, em ordem sequencial, ligado ao documento de origem (nota, contrato, extrato, folha).
- Em lançamento com várias contas: informação que permita identificar todas as partidas que formam o mesmo lançamento.

Escrituração em idioma e moeda nacional, em ordem cronológica, sem rasuras, borrões ou espaços em branco (ITG 2000 (R1) e art. 1.183 da Lei nº 10.406/2002 (Código Civil)).

### 2. Equilíbrio débito × crédito
Conferir se o lançamento segue uma das quatro fórmulas:
- 1ª: um débito para um crédito.
- 2ª: um débito para vários créditos.
- 3ª: vários débitos para um crédito.
- 4ª: vários débitos para vários créditos.

O total de débitos é sempre igual ao total de créditos (método das partidas dobradas).

### 3. Natureza e classificação das contas
- Ativo e despesa aumentam com débito; passivo, patrimônio líquido e receita aumentam com crédito.
- A conta escolhida representa o fato? Exemplo: pagamento de salário já provisionado debita "Salários a pagar", não "Despesa com salários".
- Circulante × não circulante (Seção 4 da NBC TG 1000 (R1)): o prazo de realização ou de vencimento cabe em 12 meses?
- Bem de produção: depreciação vai a custo, não a despesa.
- Receita pelo valor bruto, com tributos sobre a venda em conta redutora (art. 187 da Lei nº 6.404/1976).

### 4. Qualidade do histórico
- Expressa o fato de verdade (quem, o quê, documento)? "Pagamento diverso", "Ajuste" e "Transferência" sem mais detalhe são insuficientes.
- Redigido em português.
- Código ou abreviatura: consta de tabela auxiliar?

### 5. Competência
- O lançamento está no período em que o fato ocorreu, e não no período do pagamento? (art. 177 da Lei nº 6.404/1976; regime de competência da Seção 2 da NBC TG 1000 (R1)).
- Despesa paga antecipadamente (seguro, assinatura anual) vai para despesa antecipada e é apropriada mês a mês.

### 6. Retificação, quando houver erro (ITG 2000 (R1), itens 31 a 36)
- **Estorno:** lançamento inverso, que anula por inteiro o lançamento feito com erro.
- **Transferência:** move o valor da conta errada para a conta certa.
- **Complementação:** acrescenta ou diminui o valor registrado a menor ou a maior.
- **Lançamento de retificação e lançamento extemporâneo** (feito depois da data em que deveria): o histórico informa o motivo, a data e a localização (número) do lançamento corrigido.
- Erro que afeta demonstração de exercício já encerrado: avaliar a retificação de erro de período anterior pela Seção 10 da NBC TG 1000 (R1) (políticas contábeis, mudança de estimativa e retificação de erro) ou pelo CPC 23.

### 7. Classificar a gravidade
| Nível | Descrição | Exemplo |
|---|---|---|
| Crítico | Compromete a validade do lançamento | Débito diferente do crédito, data ausente, fato que não ocorreu |
| Moderado | Exige correção, mas não invalida | Histórico vago, conta trocada, competência errada |
| Observação | Melhoria recomendada | Conta poderia ser mais específica |

### 8. Formato de saída
```
ANÁLISE DO LANÇAMENTO nº ____
Status: APROVADO | APROVADO COM RESSALVAS | REPROVADO
Elementos obrigatórios: [OK ou lista do que falta]
Equilíbrio D/C: [OK ou divergência]
Contas e classificação: [OK ou conta sugerida]
Histórico: [OK ou sugestão de redação]
Competência: [OK ou período correto]
Parecer final: [1 parágrafo objetivo; se reprovado, o tipo de retificação e o lançamento de correção sugerido]
```

## Erros comuns / pontos de atenção
- Receita lançada já líquida de impostos.
- Pagamento de passivo provisionado lançado como nova despesa (despesa em dobro).
- Lançamento no mês do pagamento em vez do mês do fato.
- Corrigir erro apagando ou alterando o lançamento já registrado sem deixar trilha: a correção é feita por novo lançamento.
- Histórico genérico que não permite achar o documento.

## Perguntas que o usuário costuma fazer
- **"Posso só editar o lançamento errado no sistema?"** Antes do fechamento do período, o sistema pode permitir; depois, a correção é feita por estorno, transferência ou complementação, com histórico explicando.
- **"Qual a diferença entre estorno e transferência?"** Estorno anula tudo; transferência só muda a conta, mantendo o fato.

## Restrições
- Não registrar nem aprovar lançamentos: apenas analisar.
- Em dúvida normativa, citar a norma e o item.
- Se faltar informação (documento de origem, data do fato), perguntar antes de concluir.

## Base legal usada nesta skill
- ITG 2000 (R1) — Escrituração Contábil (CFC): elementos do registro contábil, identificação do lançamento, retificação (itens 31 a 36) e lançamento extemporâneo.
- NBC TG 1000 (R1) — Contabilidade para PMEs: Seção 2 (conceitos e princípios, competência), Seção 4 (balanço patrimonial, circulante e não circulante), Seção 10 (retificação de erro). Pequenas empresas e microentidades podem adotar a NBC TG 1001 ou a NBC TG 1002 (vigentes para exercícios iniciados a partir de 01/01/2023): conferir a norma adotada pelo cliente.
- Art. 177 e art. 187 da Lei nº 6.404/1976 (Lei das S.A.): competência e estrutura da DRE.
- Arts. 1.179 a 1.195 da Lei nº 10.406/2002 (Código Civil): escrituração; art. 1.183 (forma da escrituração).
- CPC 23: políticas contábeis, mudança de estimativa e retificação de erro.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
