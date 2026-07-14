---
name: Confere MDs
description: |
  Audita a documentacao de um contexto do seu OS contra a fonte-da-verdade (codigo, banco,
  automacoes) e corrige o que estiver desatualizado — sempre com sua aprovacao.
  Executa quando o usuario diz "confere mds", "confere docs", "auditar documentacao",
  "docs batem com a realidade?", "verificar documentacao", "docs drift", "audit mds",
  "revisar documentacao", "a doc esta desatualizada?", "tem muita coisa vencida nos mds".
  Detecta contagens erradas, contradicoes entre arquivos, informacao vencida, arquivos
  orfaos e arquivos grandes demais.
version: 1.0
context: meuos
user-invocable: true
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Confere MDs — Auditoria de Documentacao vs Realidade

## O que esta skill faz

Seus documentos (`*MESTRE.md`, `claude.md`, arquivos satelite) descrevem um sistema que muda
todo dia: o codigo ganha rotas novas, o banco ganha tabelas, pendencias sao resolvidas, versoes
de ferramentas mudam. Esta skill compara o que os documentos AFIRMAM com o que EXISTE de
verdade — e propoe as correcoes numa tabela para voce aprovar.

> Analogia: e o **inventario fisico da loja**. De tempos em tempos alguem confere se o que o
> sistema diz que tem na prateleira esta mesmo na prateleira. Se ninguem confere, o estoque
> vira ficcao — e todo mundo para de confiar nele.

O metodo: **extrair afirmacoes verificaveis dos documentos, checar cada uma contra a fonte,
apresentar tabelas de drift para aprovacao, executar somente o que for aprovado**. Nunca
decidir sozinho. Nunca apagar. Sempre deixar ponteiro de volta.

---

## Quando usar

- Apos sessoes intensas de trabalho (sprint fechou, muitas mudancas)
- Quando o `changelog.md` cresceu 5+ entradas desde a ultima conferencia
- Antes de compartilhar documentos com socio, cliente ou parceiro
- Quando alguem aponta inconsistencia ("ue, a tabela X nao existe mais?")
- Ritual mensal ou trimestral de higiene

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 1 — Identificar o contexto

**Esta skill SEMPRE roda em UM contexto por vez.**

- Se o usuario informou na chamada: usar esse
- Se ficou obvio pela conversa: usar esse
- Se houver duvida: **PERGUNTAR** — `"Em qual contexto vou conferir os documentos? (Pessoal / Consultoria/ClienteA / Produtos/MeuApp / ...)"`

NUNCA auditar o OS inteiro de uma vez. Para varios contextos, rodar a skill varias vezes.

### PASSO 2 — Descobrir as fontes-da-verdade disponiveis

Ler o `claude.md` e o `*MESTRE.md` do contexto procurando sinais de onde vive a realidade:

| Sinal encontrado no documento | Fonte-da-verdade | Como checar |
|---|---|---|
| Menciona `github.com/USUARIO/REPO` | Repo GitHub | MCP de GitHub disponivel OU clone local (Grep/ls) |
| Menciona projeto Supabase (ref ou URL) | Supabase | MCP de Supabase que corresponda ao projeto |
| Menciona workflows ou "n8n" | n8n | MCP/API do n8n |
| Existe pasta de repo clonado no contexto | Filesystem local | Grep/Glob direto |
| Menciona lib externa (Next.js, Stripe...) | Documentacao oficial | WebFetch sob demanda |

**Nao assumir ferramenta especifica pelo nome** — detectar qualquer MCP de GitHub, Supabase ou
n8n que estiver configurado e usar o que corresponder ao contexto.

Se uma fonte nao estiver disponivel (MCP nao configurado, repo nao clonado): **sinalizar mas
prosseguir**. Se NENHUMA fonte externa existir (so documentos), rodar em **modo
consistencia-interna**: detectar apenas contradicoes entre documentos, duplicacoes, orfaos e
arquivos grandes — sem validar afirmacoes externamente.

### PASSO 3 — Mapear a arvore de documentos do contexto

Listar TODOS os `.md` da pasta do contexto e subpastas, EXCETO `historico/`, `tmp/`,
`node_modules/`, `.git/`, `.meuos/`, `bkp/`.

Para cada arquivo, extrair: path completo, tamanho em KB, linhas, titulo (primeiro `#`) e
referencias a outros `.md`.

**Varrer subpastas individualmente**: quando o `index.md` lista uma pasta genericamente
(ex: `| docs/ | saidas geradas |`), ler DENTRO dela. Satelites "escondidos" em subpastas sao a
causa mais comum de arquivo orfao.

**Detectar arquivos orfaos**: existem no disco mas nao sao referenciados no `*MESTRE.md` nem no
`index.md`. Proposta padrao: adicionar ponteiro. Arquivar em `historico/` so quando o conteudo
estiver obsoleto.

**Detectar arquivos grandes** (mesmos limites da skill Otimizar OS):

| Arquivo | 🟢 OK | 🟡 Atencao | 🔴 Acao sugerida |
|---|---|---|---|
| `claude.md` | <200 linhas | 200-300 | >300 — sugerir split em satelite |
| `*MESTRE.md` | <300 linhas | 300-500 | >500 — sugerir extracao de secoes densas |
| Satelite tematico | <25KB | 25-40KB | >40KB — sugerir split por tema |
| `changelog.md` | <30KB | 30-50KB | >50KB — sugerir arquivar >6 meses em `historico/` |
| `aprendizados_do_dia.md` | <200 linhas | 200-250 | >250 — sugerir migrar antigos |
| Outros | <20KB | 20-35KB | >35KB — avaliar caso a caso |

> Esta skill so DETECTA e SUGERE split/compactacao — quem executa a reorganizacao e a skill
> **Otimizar OS**. Aqui o foco e corrigir CONTEUDO errado.

### PASSO 4 — Extrair afirmacoes verificaveis

Para cada documento ativo, procurar (regex/heuristica):

1. **Contagens numericas**: `(\d+)\s*(tabelas|edge functions|rotas|policies|prompts|workflows|telas|componentes|funcoes)`
2. **Linhas de arquivo**: "arquivo X com ~N linhas"
3. **Modelos de IA citados**: `GPT-\d`, `Claude (Sonnet|Opus|Haiku)`, `Gemini \d`
4. **Versoes declaradas**: `v\d+\.\d+`, "Documento v2"
5. **Status de pendencias**: `[ ]` e `[x]` em listas
6. **URLs e IDs**: repos, projetos, workflows
7. **Nomes de tabela/funcao/endpoint** em backticks

Guardar cada afirmacao como: `(arquivo, linha, tipo, valor, contexto)`.

### PASSO 5 — Verificar cada afirmacao contra a fonte

| Tipo de afirmacao | Como verificar |
|---|---|
| "N tabelas" | Listar tabelas no Supabase e contar |
| "N edge functions" | Listar functions + conferir pasta no repo |
| "N policies" | SQL: `SELECT count(*) FROM pg_policies WHERE schemaname='public'` |
| "N workflows" | Listar workflows no n8n |
| "N rotas" / "N telas" | Grep no repo (router/pastas) |
| "Arquivo X ~N linhas" | `wc -l` no repo local |
| "IA principal e o modelo Y" | Grep no codigo — qual modelo e chamado de fato |
| "[x] pendencia resolvida" | Cruzar com changelog/codigo — foi mesmo? |

Se a fonte nao estiver disponivel: marcar como **"nao verificavel neste ambiente"** e seguir.

### PASSO 6 — Montar 3 tabelas para aprovacao (SEMPRE apresentar na integra)

**Tabela 1 — Ajustes de conteudo**

```
| # | Arquivo | Trecho atual | Mudanca proposta | Motivo (fonte-da-verdade) |
|---|---------|--------------|------------------|---------------------------|
| A1 | MESTRE.md:L23 | "23 tabelas" | "24 tabelas" | Supabase lista 24 |
| A2 | CLIENTEA_TECH_API.md:L11 | "16 rotas" | "17 rotas (inclui /relatorios)" | grep no router = 17 |
```

**Tabela 2 — Estrutura / metadados**

```
| # | Arquivo | Status sugerido | Motivo |
|---|---------|-----------------|--------|
| S1 | analise_antiga.md | Adicionar ponteiro no index OU arquivar | Arquivo orfao |
| S2 | MESTRE.md (580 linhas) | Sugerir split via Otimizar OS | Acima de 500 linhas (🔴) |
| S3 | changelog.md (62KB) | Sugerir arquivar entradas antigas | Acima de 50KB (🔴) |
| S4 | PLANO_SPRINT.md secao 2 | Remover secao (tudo ja executado) | Informacao vencida |
```

**Tabela 3 — Pendencias soltas para consolidar no MESTRE**

```
| # | Pendencia | Onde estava | Sugestao |
|---|-----------|-------------|----------|
| P1 | Migrar modulo X | CLIENTEA_TECH_NOTAS.md | Promover ao MESTRE secao Backlog |
| P2 | Renovar credencial em OUT | rascunho_solto.md | Promover ao MESTRE secao Pendencias |
```

**Regra de ouro**: apresentar TODAS as linhas, mesmo se a tabela for longa. Nao filtrar por
"importancia" — quem decide o que importa e o usuario.

### PASSO 7 — Aguardar aprovacao

Formatos aceitos:
- **Global**: "pode executar tudo"
- **Item a item**: "A1, A3 sim; S2 nao"
- **Por tabela**: "toda a tabela 1; da 2 so S1 e S3"
- **Rejeicao total**: "nao muda nada" — registrar nos aprendizados e encerrar

Se a resposta for ambigua, pedir confirmacao antes de agir. **NUNCA executar sem resposta.**

### PASSO 8 — Executar os ajustes aprovados

- Edicao cirurgica: alterar somente o trecho aprovado, nada ao redor
- Criacao de satelite novo: criar o arquivo + adicionar ponteiro no MESTRE E no `index.md`
- Arquivamento: mover para `historico/` + remover a entrada do `index.md`
- Se um ajuste falhar: reportar e seguir com os demais — nao abortar o lote

### PASSO 9 — Registrar nos aprendizados

Adicionar entrada no `aprendizados_do_dia.md` do contexto:

```markdown
### DD-MMM-AAAA — confere-mds: N ajustes aplicados, M itens de estrutura
- **Insight:** [drift mais relevante — ex: "doc dizia GPT-4 desde marco, o codigo usa outro modelo desde abril"]
- **Solucao:** N ajustes de conteudo + M de estrutura. Fontes consultadas: [lista].
- **Nao fazer:** [regra que emergir — ex: "nao confiar em contagem numerica com mais de 30 dias"]
```

Registrar MESMO quando o usuario rejeitar tudo — e util saber que a auditoria rodou.

### PASSO 10 — Guardar o carimbo da execucao

Criar/atualizar `{contexto}/historico/.last-confere-mds`:

```
ULTIMA_EXECUCAO=AAAA-MM-DDTHH:MM
AJUSTES_APLICADOS=N
ITENS_ESTRUTURA=M
FONTES_CONSULTADAS=github,supabase,n8n,fs
```

Criar `historico/` se nao existir. A skill **Fim do Dia** pode usar esse carimbo para sugerir
nova auditoria quando o changelog acumular 5+ entradas novas.

---

## Integracao com as outras skills do MeuOS

| Skill | Papel na dupla |
|---|---|
| **Confere MDs** (esta) | Detecta e corrige **drift de conteudo** (doc ≠ realidade) |
| **Otimizar OS** | Executa a **reorganizacao estrutural** (split, compactacao, arquivamento) |
| **Fim do Dia** | Captura **aprendizados novos** e fecha a sessao |

Ordem ideal de higiene completa: primeiro **Confere MDs** (corrige o conteudo), depois
**Otimizar OS** (organiza a estrutura).

---

## Regras de seguranca

- **Nunca executar ajuste sem aprovacao explicita**
- **Nunca apagar conteudo** — apenas mover para `historico/` ou changelog
- **Nunca alterar documentos de contexto diferente do escolhido**
- **Sempre apresentar as 3 tabelas na integra** (mesmo longas)
- **Sempre deixar ponteiro de volta** ao extrair conteudo para arquivo novo
- **Sempre registrar a execucao nos aprendizados** (mesmo rejeitada)
- **Hipotese nao e fato**: afirmacao nao verificada entra como "nao verificavel", nunca como confirmada

## O que esta skill NAO faz

- **NAO compacta nem reorganiza documentos** (isso e da skill Otimizar OS)
- **NAO captura aprendizados de sessao** (isso e da skill Fim do Dia)
- **NAO altera codigo, banco ou automacoes** — so documentacao
- **NAO gera documentacao nova do zero** — so corrige a existente

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
