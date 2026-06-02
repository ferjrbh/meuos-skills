---
name: n8n Skills (Patterns, Code, Expressões)
description: Compendio profundo pra desenhar workflows n8n. 8 patterns canonicos (incluindo sub-workflow, error workflow, batch+retry), node configuration, Code JS/Python, expressoes, respondToWebhook 3 modos.
version: 3.0
context: meuos
category: n8n
user-invocable: true
---

# n8n Skills

Compendio profundo de design pra n8n. Use junto com `Conectar n8n` (operacional REST) e `n8n-ai-rag` (especifico de agentes IA). 6 areas:

1. Workflow patterns (8 arquiteturas)
2. Node configuration
3. Code node — JavaScript
4. Code node — Python
5. Expression syntax `{{ }}`
6. Webhook response modes

---

## 1) Workflow patterns — 8 arquiteturas canonicas

### A. Webhook processing
Trigger: webhook recebe HTTP. Fluxo: Webhook -> Validate -> Transform -> Respond ou Notify async.
**Gotcha critico**: dados em `$json.body`, nao no root.

### B. HTTP API integration
Trigger: schedule ou manual. Fluxo: HTTP Request -> Transform -> Action -> Error Handler. Auth SEMPRE em "Credentials". Paginacao precisa de plano (cursor ou pagination automatica).

### C. Database operations
Trigger: schedule (cron) com SELECT. Fluxo: Query -> Transform -> Write -> Verify. Cuidado: type mismatch causa falha silenciosa em alguns conectores.

### D. AI Agent workflow
Trigger: webhook ou input manual. Fluxo: AI Agent (Model + Tools + Memory) -> Output. Para profundidade total ver skill `n8n-ai-rag`.

### E. Scheduled tasks
Trigger: cron. Gotchas: timezone (TZ do server) e retry (sempre precisa de error handler).

### F. Sub-workflow pattern (NOVO v3.0)
Workflow grande quebra em sub-workflows. **Parent**: usa node `n8n-nodes-base.executeWorkflow` (operation = "Execute Workflow", workflowId = id-do-sub). **Child**: comeca com `n8n-nodes-base.executeWorkflowTrigger` (recebe input do parent em `$json`).

```json
// Parent: Execute Workflow node
{
  "type": "n8n-nodes-base.executeWorkflow",
  "parameters": {
    "workflowId": { "value": "abc123", "mode": "list" },
    "mode": "each"
  }
}
// Child: comeca com
{
  "type": "n8n-nodes-base.executeWorkflowTrigger",
  "typeVersion": 1
}
```

Por que: modulariza, permite reuso, sub-workflows nao contam pra limite mensal de execucoes em alguns planos n8n. Pattern usado em 47/299 templates publicos.

### G. Error Workflow pattern (NOVO v3.0)
Workflow X falha -> dispara workflow Y de tratamento. **Setup**:

1. Crie workflow Y comecando com node `n8n-nodes-base.errorTrigger`
2. errorTrigger recebe `$json` com:
   - `workflow.id` / `workflow.name` (qual workflow quebrou)
   - `execution.id` / `execution.error.message` / `execution.error.stack`
   - `execution.lastNodeExecuted` (qual node quebrou)
3. Em Y, ramifique: enviar Slack/email/Telegram alertando + log no DB
4. No workflow X (alvo), `settings.errorWorkflow = ID_DO_Y` via API ou na UI Workflow Settings

```json
// Settings do workflow X
"settings": {
  "executionOrder": "v1",
  "errorWorkflow": "ID_DO_WORKFLOW_Y"
}
```

CRITICO em prod: workflow scheduled/webhook que falha sem error workflow = problema invisivel.

### H. Batch processing com `splitInBatches` + retry (NOVO v3.0)
Quando precisar processar N items em lotes de M (ex: API com rate limit, processamento pesado por item):

```
[Trigger] -> [Get Items (200)] -> [Loop Over Items (batch=20)]
                                       |
                                       +-> [HTTP Request com retry]
                                       |     (Settings -> Retry On Fail = true,
                                       |      Max Tries = 3, Wait = 1000ms)
                                       |
                                       +-> [done? loop volta] -> [Final processing]
```

`splitInBatches` (chamado "Loop Over Items" no UI) roda multiplas vezes. **Gotcha**: dentro do loop, `$input.all()` so retorna o batch atual. Pra acumular dados entre iteracoes, use `$getWorkflowStaticData('node')` ou node Aggregate ao final.

```javascript
// Code node dentro do loop, acumulando
const state = $getWorkflowStaticData('node')
state.processed = state.processed || []
state.processed.push(...$input.all().map(i => i.json.id))
return $input.all()  // segue o loop
```

`retryOnFail` (per-node setting): SEMPRE marcar em chamada externa critica (HTTP Request, Postgres, Telegram). 21/299 templates fazem isso.

### Gotchas gerais
- `settings.executionOrder: "v1"` (default novo) — workflows antigos (v0) podem ter ordem diferente
- Multiplos items processam individualmente, exceto com SplitInBatches ou Code node `$input.all()`
- Expressoes precisam `{{ }}` ou viram literal

---

## 2) Node configuration — regras de dependencia

n8n esconde/mostra campos baseado em outros. 3 padroes:

**A. Boolean toggles**: campo aparece quando outro vira true. Ex: HTTP `sendBody: true` mostra `body`.
**B. Operation switches**: cada operation exige campos diferentes. Slack `post` precisa `channel`+`text`; `update` precisa `messageId`+`text`.
**C. Type/value selection**: HTTP `GET` esconde body; `POST/PUT/PATCH` mostra.

### Regras criticas
- HTTP POST/PUT/PATCH: `sendBody: true` torna `body` obrigatorio
- IF unario (`isEmpty`): `singleValue: true` — nao passe `value2`
- IF binario: precisa `value1` E `value2`
- Database INSERT/UPDATE/SELECT: cada um quer campos diferentes — nao reuse config

### Estrategia
Comece minimo, valide, deixe o erro guiar o que adicionar. Nao adivinhe — campos aparecem condicionalmente.

---

## 3) Code node — JavaScript

### Modos
- **Run Once for All Items** (default, 95%): roda 1 vez, `$input.all()` traz todos
- **Run Once for Each Item**: roda N vezes, `$input.item` traz item atual

### Acesso a dados
```javascript
$input.all()                       // todos os items
$input.first()                     // primeiro
$input.item                        // item atual (Each Item)
$node["NodeName"].first().json     // output de outro node
$json.body.email                   // webhook: dados em .body
```

### Formato de retorno (CRITICO)
```javascript
return [{ json: { field: value } }]   // array de objetos com wrapper json
return []                              // vazio e ok
```

### Built-in disponiveis
- `$helpers.httpRequest({...})` — fetch sem auth
- `DateTime` (Luxon) — `.now()`, `.plus({days: 1})`, `.toFormat('yyyy-MM-dd')`
- `$jmespath('expr', obj)` — query JSON

### Indisponiveis
- `$helpers.httpRequestWithAuthentication`
- `require('lib')` — bloqueado a menos que admin libere
- `$env` — pode estar bloqueado por `N8N_BLOCK_ENV_ACCESS_IN_NODE=true`

### Padroes uteis
```javascript
// Filter + map
return $input.all()
  .filter(i => i.json.status === 'ativo')
  .map(i => ({ json: { id: i.json.id, nome: i.json.nome.toUpperCase() } }))

// Aggregation
const total = $input.all().reduce((acc, i) => acc + i.json.valor, 0)
return [{ json: { total } }]

// State entre execucoes
const state = $getWorkflowStaticData('node')
state.lastRun = state.lastRun || new Date().toISOString()
return [{ json: state }]
```

### Gotchas
- **Webhook nesting**: `$json.body.email` (nao `$json.email`)
- **SplitInBatches perde dados**: depois do loop, use `$getWorkflowStaticData()` pra acumular
- **pairedItem**: novos items precisam `{ pairedItem: { item: idx } }` se Set downstream usar
- **Float currency**: `Math.round(v * 100) / 100`

---

## 4) Code node — Python

### Sintaxe (prefixo `_` em vez de `$`)
```python
_input.all()                          # todos
_input.first()                        # primeiro
_input.item                           # Each Item mode
_node["NodeName"].first()["json"]     # outro node
_json.get("body", {})                 # webhook
```

### Standard library disponivel
`json`, `datetime`, `re`, `base64`, `hashlib`, `urllib.parse`, `math`, `random`, `statistics`. Helpers: `_now`, `_today`, `_jmespath()`.

### NAO disponivel
- Pacotes externos (requests, pandas, numpy, bs4)
- `_helpers.httpRequest()` — use HTTP Request node
- Luxon — use datetime standard

### Formato de retorno
```python
return [{"json": {"field": value}}]   # list de dicts com wrapper json
```

### Quando usar Python
Regex/string/matematica simples — Python e tao bom. HTTP request / lib externa / integracao mais profunda — JavaScript e melhor.

### Gotcha critico
```python
# seguro
email = _json.get("body", {}).get("email", "")
# quebra se faltar
email = _json["body"]["email"]
```

---

## 5) Expression syntax `{{ }}`

Em campos string (exceto Code node), use `{{ expressao }}`.

| Variavel | Uso |
|---|---|
| `{{ $json.campo }}` | Campo do item atual |
| `{{ $json.body.campo }}` | **Webhook** — sempre via .body |
| `{{ $node["Set"].json.campo }}` | Output de outro node |
| `{{ $now }}` | DateTime atual (Luxon) |
| `{{ $now.toFormat('yyyy-MM-dd') }}` | Formatacao |
| `{{ $env.VAR }}` | Env var (pode estar bloqueada) |
| `{{ $('NodeName').first().json.x }}` | Sintaxe alternativa |

### Bracket notation (espacos / nomes especiais)
```
{{ $json['nome do campo'] }}
{{ $node["HTTP Request"].json }}
```

### NAO usar
- Code nodes: JS/Python direto, sem `{{ }}`
- Webhook paths: estaticos
- Credentials: usar sistema do n8n

### Erros comuns
| Erro | Correcao |
|---|---|
| `$json.field` literal | Faltou `{{ }}` |
| `{{ $json.nome do campo }}` falha | Use bracket: `{{ $json['nome do campo'] }}` |
| Webhook sem dados | Use `{{ $json.body.* }}` |
| Code node com `{{ }}` | Remova braces |

---

## 6) Respond to Webhook — 3 modos (NOVO v3.0)

Quando o webhook node tem `responseMode: 'responseNode'`, voce pode escolher COMO responder no node `respondToWebhook`. **8 modos disponiveis** — os 3 mais usados:

### A. `firstIncomingItem` (default mais comum)
Responde com o JSON do PRIMEIRO item que chega no node. Ideal pra webhooks que retornam 1 resultado.

```json
{
  "type": "n8n-nodes-base.respondToWebhook",
  "parameters": {
    "respondWith": "firstIncomingItem"
  }
}
```

### B. `allIncomingItems`
Responde com o ARRAY de todos os items. Ideal pra webhooks que retornam lista.

```json
{
  "parameters": {
    "respondWith": "allIncomingItems"
  }
}
```

### C. `json`
Responde com JSON literal customizado (use expressoes pra montar).

```json
{
  "parameters": {
    "respondWith": "json",
    "responseBody": "={ \"status\": \"ok\", \"id\": \"{{ $json.id }}\" }"
  }
}
```

### Outros modos (mencao rapida)
- `text`: HTML/texto cru. Por seguranca, n8n agora **wrapa HTML em iframe sandbox** desde 1.103.0 — JS no HTML nao acessa parent window/local storage.
- `binary`: arquivo binario
- `redirect`: HTTP 302 com Location
- `noData`: 200 sem body
- `jwt`: assina JWT no servidor

### Gotchas
- O node roda **uma vez** com o primeiro item, mesmo se voce conectar varios items via Loop. Pra agrupar primeiro: use Aggregate node antes.
- Se o workflow termina sem o respondToWebhook executar -> 200 generico
- Se erro antes do respondToWebhook -> 500 generico
- Se 2 respondToWebhook executarem -> o segundo e ignorado

---

## Como aprender mais

1. Use `Conectar n8n` pra listar workflows existentes e estudar JSON deles
2. Crie 1 workflow simples de cada pattern A-H — veja como n8n monta
3. No erro: leia mensagem do n8n — quase sempre aponta o campo
4. Doc oficial: https://docs.n8n.io

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
