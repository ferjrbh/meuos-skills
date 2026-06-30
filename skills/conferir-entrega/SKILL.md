---
name: Conferir Entrega
description: |
  Verificacao rapida antes de declarar qualquer tarefa concluida. O agente ativa automaticamente
  ao perceber que algo foi concluido. Tambem roda quando o usuario diz "conferir entrega",
  "verificar entrega", "pronto", "terminei", "conclui", "feito", "pode fechar", "entregue", "finalizado".
  Garante que nada foi esquecido, o OS esta atualizado e dados sensiveis estao protegidos.
version: 1.0
context: meuos
user-invocable: true
argument-hint: "[tipo da entrega] (opcional)"
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Conferir Entrega

## O que esta skill faz

Esta skill e uma verificacao rapida que roda quando voce termina qualquer entrega — uma decisao, um workflow, um documento, um projeto. Ela garante que nada foi esquecido: o OS esta atualizado, os arquivos estao organizados e nenhuma informacao sensivel ficou exposta. Leva menos de 2 minutos.

## Regra de ouro

> So declare "pronto" quando tiver EVIDENCIA de que esta pronto. "Acho que ficou bom" nao e evidencia. "Verifiquei X e o resultado foi Y" e evidencia.

---

## Quando usar

- Ao terminar qualquer entrega (documento, decisao, automacao, projeto)
- Quando o agente sugerir proativamente ao perceber que algo foi concluido
- Quando quiser ter certeza de que nada ficou para tras

---

## Checklists por tipo de entrega

### Decisao tomada ou documentada

- \[ \] A decisao esta registrada no documento_mestre.md? (Data + Decisao + Motivo)
- \[ \] Pendencias relacionadas foram atualizadas? (marcou \[x\] ou adicionou novas)
- \[ \] Se envolve parceiro: ele foi alinhado?

### Workflow ou automacao criada

- \[ \] Esta funcionando? (testou com dados reais, nao so imaginou)
- \[ \] Se der erro, o que acontece? (tem tratamento ou alerta?)
- \[ \] Nome e descricao estao claros para voce entender daqui a 30 dias?
- \[ \] Credenciais estao seguras? (nao hardcoded em texto visivel)

### Documento ou arquivo criado

- \[ \] Segue a convencao de nomes do OS? (contexto no nome, extensao correta)
- \[ \] index.md foi atualizado com o novo arquivo?
- \[ \] Se foi extraido do documento_mestre: tem ponteiro de volta?
- \[ \] Descricao no index.md reflete o conteudo real?

### Projeto ou fase concluida

- \[ \] documento_mestre.md foi atualizado? (status, pendencias, decisoes)
- \[ \] Itens concluidos estao marcados \[x\] ou migrados para changelog?
- \[ \] Aprendizados capturados? (o que funcionou, o que nao fazer)

### Seguranca (aplicar em TODA entrega)

- \[ \] Nenhuma senha, token ou chave exposta em texto visivel?
- \[ \] Nenhum dado pessoal (CPF, email privado) hardcoded em arquivos?
- \[ \] Credenciais de servicos estao em local seguro (variaveis de ambiente, cofre)?
- \[ \] Se compartilhou arquivo: removeu informacoes sensiveis antes?

---

## Como apresentar a conclusao

Ao finalizar, use este formato:

```
Concluido: [o que foi feito em 1 linha]

Verificacoes:
- [x] [item verificado] — [evidencia breve]
- [x] [item verificado] — [evidencia breve]
- [ ] [item nao aplicavel] — pulado porque [motivo]

Proximo passo sugerido: [se houver]
```

---

## Quando NAO usar

- Respostas a perguntas (nao e entrega)
- Pesquisas e consultas (nao e implementacao)
- Quando o usuario disser "nao precisa verificar"

---

## Regras de seguranca

- **Nunca pular o check de seguranca** — ele se aplica a TODA entrega, sem excecao
- **Nunca declarar pronto sem evidencia** — mostrar o que foi verificado
- **Nunca inventar verificacoes** — se nao verificou, nao marcar \[x\]
- **Adaptar ao tipo de entrega** — nao aplicar checks de automacao numa decisao simples

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
