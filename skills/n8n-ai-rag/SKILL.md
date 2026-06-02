---
name: n8n AI Agents & RAG
description: Skill especializada pra construir agentes IA e workflows RAG no n8n.
version: 1.1
context: meuos
category: n8n
user-invocable: true
triggers:
  - agente IA n8n
  - chatbot no n8n
  - RAG no n8n
  - vector store n8n
  - embeddings n8n
  - AI agent com tools
  - memory multi-turno
  - output parser n8n
  - mcp client n8n
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# n8n AI Agents & RAG

Pacote pra construir e debugar agentes IA + RAG no n8n. Complementa `Conectar n8n` (REST) e `n8n-skills` (design geral). Aqui sao os tipos de conexao especificos do n8n langchain, topologias canonicas e gotchas exclusivos do mundo AI.

## Os 11 connection types `ai_*`

n8n langchain usa conexoes "tipadas" entre nodes AI — diferente do `main` dos nodes regulares. Cada `ai_*` plugga em uma "porta" especifica do node-pai (geralmente um Agent ou Chain).

| Connection | Frequencia* | O que e | Quando usar |
|---|---|---|---|
| `ai_languageModel` | 601 | LLM que pensa | OBRIGATORIO em agent/chain. Modelos: `lmChatOpenAi`, `lmChatGoogleGemini`, `lmChatAnthropic`, `lmChatGroq`, `lmChatOllama` |
| `ai_tool` | 344 | Capacidade que o agente invoca | Agent com multi-step. Tools: `toolHttpRequest`, `toolWorkflow`, `toolCalculator`, `toolWikipedia`, `toolSerpApi` |
| `ai_outputParser` | 148 | Forca output estruturado | Agent que precisa retornar JSON valido. Use `outputParserStructured` (com schema) ou `outputParserAutofixing` |
| `ai_memory` | 135 | Historico multi-turno | Chatbot. Use `memoryBufferWindow` (sessionIdType: fromInput pra capturar por usuario) |
| `ai_embedding` | 127 | Vetoriza texto | Insercao em vector store + retriever. Modelos: `embeddingsOpenAi`, `embeddingsMistralCloud`, `embeddingsCohere` |
| `ai_textSplitter` | 78 | Quebra docs longos | Antes de vetorizar. `textSplitterRecursiveCharacterTextSplitter` e o default — recomendado |
| `ai_document` | 74 | Loader entrega doc pronto | Plugado em vector store insertion. `documentDefaultDataLoader` aceita binarios + text + URL |
| `ai_vectorStore` | 34 | Plugar vector store em retriever ou tool | Cluster: `vectorStoreQdrant`, `vectorStorePinecone`, `vectorStoreInMemory`, `vectorStoreSupabase` |
| `ai_retriever` | 18 | Busca docs similares | Em chains RAG nao-agente. `retrieverVectorStore` |
| `ai_chain` | raro | Sub-chain | Avancado, doc-only |
| `ai_reranker` | raro | Reordena retriever | `rerankerCohere` — melhora qualidade RAG |

*Frequencia em 299 templates publicos.

## Topologia canonica RAG

Esta estrutura aparece replicada nos templates oficiais. Memorize:

### Pipeline 1 — Insercao (rodar quando dado novo entra)
```
[Trigger] (webhook/cron/manual)
    |
[Get Source]                      <-- HTTP, Drive, Notion, etc
    |
[Vector Store (Insert mode)]      <-- vectorStoreQdrant, vectorStorePinecone, vectorStoreInMemory
    |
    +-> [embedding model]         (ai_embedding) -- embeddingsOpenAi
    |
    +-> [data loader]             (ai_document)  -- documentDefaultDataLoader
            |
            +-> [text splitter]   (ai_textSplitter) -- textSplitterRecursiveCharacterTextSplitter
```

### Pipeline 2 — Query (rodar a cada pergunta)
```
[chatTrigger] ou [webhook]
    |
[AI Agent]
    |
    +-> [language model]          (ai_languageModel) -- lmChatOpenAi
    |
    +-> [memory]                  (ai_memory) -- memoryBufferWindow (sessionIdType: fromInput)
    |
    +-> [output parser]           (ai_outputParser) -- outputParserStructured
    |
    +-> [vector store as tool]    (ai_tool) -- toolVectorStore
            |
            +-> [vector store]    (ai_vectorStore) -- vectorStoreQdrant (mesmo do Pipeline 1)
            |
            +-> [embedding]       (ai_embedding) -- embeddingsOpenAi (MESMO modelo do Pipeline 1!)
```

**REGRA CRITICA**: o embedding model usado pra inserir tem que ser o MESMO usado pra consultar. Se inserir com `text-embedding-ada-002` e consultar com `text-embedding-3-large`, vetores nao sao comparaveis e RAG retorna lixo.

## Memory com sessionId

Sem memory, agente nao tem contexto multi-turno. Setup `memoryBufferWindow`:

```json
{
  "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
  "parameters": {
    "sessionIdType": "fromInput",
    "sessionKey": "={{ $json.body.userId }}",
    "contextWindowLength": 10
  }
}
```

`sessionIdType: fromInput` + `sessionKey` = expressao que gera o ID por usuario/canal. Sem isso, todos os usuarios compartilham historico (problema!). Common patterns:
- Webhook chat: `={{ $json.body.userId }}` ou `={{ $json.body.from.id }}` (Telegram)
- Form: `={{ $json.email }}`
- Chat trigger: usa o sessionId padrao do node

## Tool Workflow — agente com capacidades complexas

Quando o agente precisa de uma capacidade que envolve varios passos (consultar API, transformar, salvar), embrulhe em sub-workflow e exponha como tool:

```
Workflow A (agente):
  [chatTrigger] -> [Agent] <- [toolWorkflow "Buscar pedidos do cliente"]
                                              |
                                              v
Workflow B (sub-workflow disparado pelo agente):
  [executeWorkflowTrigger] -> [HTTP Request shop API] -> [Set] -> retorna pro agente
```

Setup do `toolWorkflow`:
```json
{
  "type": "@n8n/n8n-nodes-langchain.toolWorkflow",
  "parameters": {
    "name": "buscar_pedidos",
    "description": "Busca os pedidos de um cliente por CPF. Argumento: cpf (string)",
    "workflowId": "ID_DO_WORKFLOW_B",
    "fields": {
      "values": [
        { "name": "cpf", "type": "stringValue", "stringValue": "={{ $fromAI('cpf') }}" }
      ]
    }
  }
}
```

`$fromAI('campo')` extrai o argumento que o LLM gerou pra chamar a tool. Pattern usado em 49/299 templates.

## Output Parser Structured — JSON valido obrigatorio

Sem output parser, o agente retorna texto livre. Pra ter JSON valido:

```json
{
  "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
  "parameters": {
    "schema": "={\n  \"type\": \"object\",\n  \"properties\": {\n    \"intent\": { \"type\": \"string\", \"enum\": [\"pedido\", \"cancelamento\", \"duvida\"] },\n    \"sentiment\": { \"type\": \"number\" }\n  },\n  \"required\": [\"intent\"]\n}"
  }
}
```

Conecte como `ai_outputParser` no Agent. Se o LLM retornar JSON malformado (acontece), use `outputParserAutofixing` em cima — ele tenta corrigir antes de cair.

## MCP Client / Trigger nativos do n8n

n8n tem 2 nodes MCP nativos:

- **`mcpClient`**: workflow n8n CONSOME um MCP server externo. Util pra integrar tools de outros provedores (OpenAI MCP, Anthropic, etc) sem reimplementar.
- **`mcpTrigger`**: workflow n8n VIRA um MCP server consumido por agentes externos (Claude, ChatGPT). Util pra expor seus workflows como ferramentas pra outros agentes.

```json
// mcpClient — agente n8n usa MCP de fora
{
  "type": "@n8n/n8n-nodes-langchain.mcpClient",
  "parameters": {
    "endpoint": "https://mcp.fornecedor.com",
    "authentication": { "type": "headerAuth", "headerName": "Authorization", "headerValue": "Bearer ..." }
  }
}
```

```json
// mcpTrigger — workflow n8n e exposto via MCP
{
  "type": "@n8n/n8n-nodes-langchain.mcpTrigger",
  "parameters": {
    "path": "/mcp",
    "authentication": "none"  // ou apiKey
  }
}
```

**Nao confunda com nosso aprendizado anterior** (a skill `Conectar n8n` substitui o n8n-mcp do czlonkowski por REST). MCP nativos do n8n sao DIFERENTES — sao nodes dentro de workflows pra integracao MCP-MCP, nao a forma do agente Claude controlar o n8n.

## Padrao "Agente + multi-tool + memory + parser" (canonical)

Estrutura mais usada pra chatbot util em prod:

```
[chatTrigger sessionIdType=fromInput]
    -> [AI Agent]
         <- [lmChatOpenAi]                    (ai_languageModel)
         <- [memoryBufferWindow]              (ai_memory)         sessionKey: $json.sessionId
         <- [outputParserStructured]          (ai_outputParser)   schema com intent + dados
         <- [toolWorkflow "consulta_pedido"]  (ai_tool)           sub-workflow com HTTP
         <- [toolWorkflow "abrir_chamado"]    (ai_tool)           sub-workflow com webhook
         <- [toolHttpRequest "wikipedia"]     (ai_tool)           HTTP direto
```

System message do Agent:
```
Voce e um assistente da Empresa X. Use as tools disponiveis pra:
- consultar pedidos do cliente (tool consulta_pedido)
- abrir chamados (tool abrir_chamado)
- buscar info publica (tool wikipedia)
Sempre retorne JSON com schema definido. Em duvida, peca esclarecimento.
```

## Gotchas exclusivos AI

- **Embedding model TEM que ser o mesmo entre insercao e query** (regra critica acima)
- **Tool descriptions sao prompts**: o agente decide qual tool usar baseado em descricao. Vaga = agente nao usa. Especifica demais = agente nao reusa em casos parecidos
- **Memory consome contexto rapido**: `contextWindowLength: 10` significa as 10 ultimas trocas. Reduzir se LLM tem context window pequeno
- **Output parser strict** com schema rigido: se o JSON do LLM nao bater 100%, tudo falha. Sempre adicionar `outputParserAutofixing` em prod
- **`$fromAI('campo')`** so funciona dentro de tools (toolWorkflow, toolHttpRequest com `useCustomTool: true`). Em outros lugares retorna vazio
- **chatTrigger vs webhook**: chatTrigger oferece UI de chat embutida na n8n (boa pra dev). Webhook oferece controle total da request (use em prod com Telegram/Discord/web custom)
- **Erro 503 "modelo sobrecarregado"**: qualquer provedor de LLM (Google, OpenAI) devolve 503 sob pico de demanda — atinge modelos estaveis, nao e bug do seu fluxo. Em producao: (1) ligue **Retry On Fail** nas Settings do node do LLM (3 tries, ~1800ms); (2) configure **fallback de outro provedor** (ex: Gemini -> GPT) via Error workflow pattern; (3) nunca trave o fluxo — devolva mensagem amigavel se ambos falharem. Nao adianta so trocar de modelo no mesmo provedor: a sobrecarga costuma ser ampla

## Templates de referencia

Todos no repo `enescingoz/awesome-n8n-templates` (CC-BY 4.0):

- `AI_Research_RAG_and_Data_Analysis/Build a Tax Code Assistant with Qdrant, Mistral.ai and OpenAI.json` — agente RAG completo com multi-tool
- `OpenAI_and_LLMs/` — varios chatbots simples (otimo pra comecar)
- `WordPress/` (categorias diversas) — RAG com Qdrant e arquivos de blog

## Doc oficial

- RAG no n8n: https://docs.n8n.io/advanced-ai/rag-in-n8n/
- Agent: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/
- Vector stores: https://docs.n8n.io/advanced-ai/vector-stores/
- Tool Workflow: https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolworkflow/

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
