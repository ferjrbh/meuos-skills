---
name: structured-thinking
description: |
  Forca exploracao estruturada antes de executar tarefas complexas.
  Invoque quando voce pedir para criar algo novo (workflow, feature, integracao),
  quando houver decisao arquitetural, ou quando existir mais de um caminho possivel.
  NAO invoque para tarefas simples como consultas, ajustes pontuais ou perguntas diretas.
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Structured Thinking

## Quando ativar
- voce pede para CRIAR algo novo (workflow, feature, integracao, automacao)
- Decisao com mais de um caminho possivel
- Projeto que envolve multiplos sistemas (n8n + Supabase + Lovable)
- Tarefa que pode dar retrabalho se mal planejada

## Quando NAO ativar
- Consultas simples ("me mostra o workflow X")
- Ajustes pontuais ("muda o nome desse campo")
- Perguntas diretas ("como funciona o webhook?")
- Debug de erro especifico (usar systematic-debugging)

## Protocolo — 4 passos antes de executar

### Passo 1 — Entender o problema real
Antes de pensar em solucao, entender:
- O que voce quer que ACONTECA no final? (resultado, nao ferramenta)
- Qual o gatilho? (manual, automatico, webhook, schedule?)
- Quem vai usar? (voce, cliente, sistema?)
- Ja existe algo parecido funcionando? (evitar duplicar)

Fazer NO MAXIMO 3 perguntas de clarificacao. Se o pedido ja estiver claro, pular para o Passo 2.

### Passo 2 — Mapear o que ja existe
Antes de criar do zero, verificar:
- Workflows existentes que fazem algo parecido (n8n MCP -> list_workflows)
- Tabelas no Supabase que ja guardam os dados necessarios
- Componentes no Lovable que podem ser reaproveitados
- Skills que se aplicam (n8n-workflow-patterns, lovable-prompt-master, etc.)

### Passo 3 — Propor abordagem (max. 2 opcoes)
Apresentar para voce:

**Opcao A** (recomendada): [descricao em 2-3 linhas]
- Vantagem: [principal beneficio]
- Risco: [o que pode dar errado]

**Opcao B** (alternativa): [descricao em 2-3 linhas]
- Vantagem: [principal beneficio]
- Risco: [o que pode dar errado]

Se so existir um caminho razoavel, apresentar apenas 1 opcao com a justificativa.

### Passo 4 — Executar apos aprovacao
So iniciar a implementacao depois que voce escolher a abordagem.
Se voce disser "vai com a recomendada" ou "manda ver", executar sem mais perguntas.

## Regra de ouro
> Pensar 2 minutos antes evita refazer 20 minutos depois.
> Mas pensar 10 minutos quando bastava 30 segundos e desperdicio.
> Calibrar pelo tamanho da tarefa.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
