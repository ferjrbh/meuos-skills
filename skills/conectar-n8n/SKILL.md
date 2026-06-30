---
name: Conectar n8n
description: |
  Permite ao seu Claude criar, editar, ativar e debugar workflows direto na sua instancia n8n via
  API REST. Sem MCP, sem npx — so curl. Funciona em qualquer Claude (CLI, VSCode, Cursor, Desktop).
  Ativa quando o usuario diz "conectar n8n", "liste meus workflows n8n", "crie um workflow no n8n",
  "ative o workflow X", "leia os logs do workflow X", "debug do meu workflow", "paginar execucoes n8n".
version: 2.1
context: meuos
user-invocable: true
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Conectar n8n

Esta skill ensina o agente a usar a API REST do seu n8n self-hospedado direto, sem precisar de MCP. Funciona em qualquer ambiente que tenha curl/fetch (CLI, VSCode extension, Cursor, Claude Desktop).

## Quando ativar

Toda vez que o usuario falar "n8n", "workflow", "automacao", "trigger", ou pedir para listar/criar/ativar/debugar/paginar/handlear erro de algo no n8n. Para tarefas de DESIGN profundo (escolher pattern, configurar nodes complexos), trigger tambem a skill `n8n-skills`. Para AI Agents/RAG, trigger `n8n-ai-rag`.

## Pre-requisitos

1. N8N_API_URL — URL publica da instancia n8n (ex: https://n8n.minhaempresa.com.br)
2. N8N_API_KEY — token gerado em Settings -&gt; API -&gt; Create API Key

Onde estao as credenciais:

- Cadastradas no MeuOs (dashboard -&gt; area do agente). Pode pedir pra ele copiar e colar.
- Ou em .env na pasta do OS.
- Ou colar direto no chat.

Nao invente. Se nao tiver as 2, peca antes de fazer qualquer coisa.

## Cookbook curl

```bash
URL="https://n8n.minha.com.br"
KEY="eyJ..."
```

### Listar workflows (com paginacao cursor)

```bash
curl -s "$URL/api/v1/workflows?limit=50" -H "X-N8N-API-KEY: $KEY"
# resposta: { data: [...], nextCursor: "abc..." }

# proxima pagina:
curl -s "$URL/api/v1/workflows?limit=50&cursor=abc..." -H "X-N8N-API-KEY: $KEY"
```

### Pegar workflow especifico (definicao completa)

```bash
curl -s "$URL/api/v1/workflows/$WF_ID" -H "X-N8N-API-KEY: $KEY"
```

### Criar workflow

```bash
curl -s -X POST "$URL/api/v1/workflows" \
  -H "X-N8N-API-KEY: $KEY" \
  -H "content-type: application/json" \
  -d '{
    "name": "Nome",
    "nodes": [...],
    "connections": {...},
    "settings": { "executionOrder": "v1" }
  }'
```

### Atualizar workflow (PUT, nao PATCH)

```bash
curl -s -X PUT "$URL/api/v1/workflows/$WF_ID" \
  -H "X-N8N-API-KEY: $KEY" \
  -H "content-type: application/json" \
  -d '{ "name": "...", "nodes": [...], "connections": {...}, "settings": {...} }'
```

**GOTCHA CRITICO**: o endpoint `PUT /workflows/{id}` aceita `settings` mas faz **whitelist** dos campos. Para ATIVAR o workflow, NUNCA tente passar `active: true` no body — isso e ignorado silenciosamente. Use o endpoint dedicado abaixo.

### Ativar / desativar (endpoints dedicados — UNICA forma correta)

```bash
curl -s -X POST "$URL/api/v1/workflows/$WF_ID/activate"   -H "X-N8N-API-KEY: $KEY"
curl -s -X POST "$URL/api/v1/workflows/$WF_ID/deactivate" -H "X-N8N-API-KEY: $KEY"
```

### Listar execucoes (com paginacao cursor)

```bash
curl -s "$URL/api/v1/executions?workflowId=$WF_ID&limit=20" -H "X-N8N-API-KEY: $KEY"
# resposta inclui nextCursor pra proxima pagina

# Filtros uteis:
# &status=success | error | running | waiting
# &startedAfter=2026-05-07T00:00:00Z
```

### Ler dados de uma execucao com payloads

```bash
curl -s "$URL/api/v1/executions/$EXEC_ID?includeData=true" -H "X-N8N-API-KEY: $KEY"
```

Resposta inclui `data.resultData.runData["NomeDoNode"]` com input/output de cada execucao do node — essencial pra debugar workflow que falhou.

### Listar credenciais (so metadata, nao le secrets)

```bash
curl -s "$URL/api/v1/credentials" -H "X-N8N-API-KEY: $KEY"
```

### Descobrir schema de um tipo de credencial (PRA criar credenciais via API)

```bash
curl -s "$URL/api/v1/credentials/schema/postgres" -H "X-N8N-API-KEY: $KEY"
# substitua "postgres" por: telegramApi, openAiApi, googleSheetsOAuth2Api, etc
```

Retorna o JSON Schema com os campos esperados (host, database, user, password etc). Essencial pra criar credentials novas via API ou validar config.

### Criar credencial via API

```bash
curl -s -X POST "$URL/api/v1/credentials" \
  -H "X-N8N-API-KEY: $KEY" \
  -H "content-type: application/json" \
  -d '{
    "name": "Postgres prod",
    "type": "postgres",
    "data": {
      "host": "db.empresa.com.br",
      "database": "app",
      "user": "n8n",
      "password": "secret"
    }
  }'
```

### Anexar error workflow a um workflow alvo

Para um workflow X chamar um workflow Y quando erra:

1. Crie o workflow Y comecando com node `n8n-nodes-base.errorTrigger`
2. Pegue o ID do workflow Y (resposta do POST /workflows)
3. PUT no workflow X passando `settings.errorWorkflow = ID_DO_Y`:

```bash
curl -s -X PUT "$URL/api/v1/workflows/$WORKFLOW_X_ID" \
  -H "X-N8N-API-KEY: $KEY" \
  -H "content-type: application/json" \
  -d '{
    "name": "...",
    "nodes": [...],
    "connections": {...},
    "settings": {
      "executionOrder": "v1",
      "errorWorkflow": "ID_DO_Y"
    }
  }'
```

Depois disso, qualquer falha no workflow X dispara o Y, que recebe os dados via Error Trigger node ($json contem: workflow, execution.error, execution.lastNodeExecuted).

## Estrutura de um workflow (referencia rapida)

JSON minimo valido:

```json
{
  "name": "Hello world",
  "nodes": [
    {
      "id": "trigger",
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [240, 300],
      "parameters": {}
    },
    {
      "id": "set",
      "name": "Set",
      "type": "n8n-nodes-base.set",
      "typeVersion": 3,
      "position": [460, 300],
      "parameters": {
        "assignments": {
          "assignments": [
            { "id": "1", "name": "msg", "value": "Hello", "type": "string" }
          ]
        }
      }
    }
  ],
  "connections": {
    "Manual Trigger": {
      "main": [[{ "node": "Set", "type": "main", "index": 0 }]]
    }
  },
  "settings": { "executionOrder": "v1" }
}
```

Para detalhes profundos de patterns, configuracao de nodes, code nodes JS/Python e expressoes, abrir a skill `n8n-skills`. Para AI Agents/RAG, abrir `n8n-ai-rag`.

## Troubleshooting

**401 Unauthorized**

- API key errada/expirada -&gt; regerar em Settings -&gt; API
- URL com /api/v1 ou barra final extra -&gt; use so o dominio raiz

**404 Not Found em endpoint que existe**

- Public API desabilitada. Garanta N8N_PUBLIC_API_DISABLED=false. Reinicie.

**SSL self-signed / cert error**

- curl -k temporariamente. Solucao: cert valido (Lets Encrypt).

**Workflow nao executa apos PUT**

- Voce passou `active: true` no body do PUT? Whitelist do settings ignora isso. Use POST /activate.

**Body \[Object\] em log**

- Use JSON.stringify($json) no Code node pra inspecionar.

**Nao acha o erro de uma execucao**

- GET /executions/$EXEC_ID?includeData=true -&gt; data.resultData.runData\[NodeName\] tem o stack completo.

## Doc oficial

- API OpenAPI: {N8N_URL}/api/v1/docs
- Catalogo de nodes: https://n8n.io/integrations
- Error handling: https://docs.n8n.io/flow-logic/error-handling/
- Sub-workflows: https://docs.n8n.io/flow-logic/subworkflows/

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
