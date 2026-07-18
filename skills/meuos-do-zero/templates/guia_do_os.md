# guia_do_os.md — O Manual de Operação deste OS
> Gerado pelo MeuOS em {{DATA}} · www.meuos.com.br

## Para você, humano — em 30 segundos

Seu OS é um conjunto de arquivos .md que guardam seu contexto, suas regras e o que você aprende.
Eles são **seus** (ficam no seu storage) e funcionam com **Claude e ChatGPT** — os dois leem os
mesmos arquivos. Quanto mais você usa, mais inteligente o sistema fica. O resto deste guia é
para o seu agente: ele lê e sabe operar tudo sozinho.

---

## AGENTE: leia esta seção e opere assim

Você é o motor deste OS. Os arquivos são a memória — sem eles você esquece tudo entre sessões;
com eles, cada sessão começa de onde a anterior parou. Estas são as suas instruções de operação.

### 1. O mapa dos arquivos

**Na raiz:**

| Arquivo | O que é | Você pode editar? |
|---------|---------|-------------------|
| `claude.md` | Entrada do Claude — regras globais, identidade do dono, mapa de contextos | Só o mapa de contextos, quando um novo contexto surgir |
| `AGENTS.md` | Entrada do ChatGPT/Codex — fina, aponta pro claude.md | NÃO (é ponteiro; se editar um, o par diverge) |
| `soul.md` | Sua personalidade: tom, postura, papel | Só a pedido do dono |
| `guia_do_os.md` | Este manual | NÃO |
| `index.md` | Catálogo geral do OS | SIM — mantenha atualizado quando criar arquivos |
| `.gitignore` / `.env` | Config técnica (git e credenciais) | `.env` NUNCA vai pra chat nem pra git |

**Em cada contexto (pasta):**

| Arquivo | O que é | Sua regra de escrita |
|---------|---------|----------------------|
| `claude.md` | Regras do contexto + papel do agente ali | Raramente muda — só regra nova aprovada |
| `AGENTS.md` | Entrada ChatGPT do contexto (ponteiro) | NÃO editar |
| `documento_mestre.md` | **Documento VIVO**: escopo, status, decisões, pendências, próximos passos | Atualize DURANTE o trabalho — é a fonte de retomada |
| `aprendizados_do_dia.md` | Conhecimento capturado: Insight + Solução + Não fazer | Adicione no fim da sessão (skill fim-do-dia) |
| `changelog.md` | Histórico do que foi feito | **Append-only** — nunca edite entradas antigas |
| `index.md` | Catálogo da pasta | Atualize quando criar/mover arquivos |

### 2. Ordem de leitura ao iniciar qualquer sessão

1. Sua entrada na raiz (`claude.md` se você é Claude; `AGENTS.md` → `claude.md` se você é ChatGPT).
2. `soul.md` — assuma essa personalidade.
3. Pergunte (ou detecte) o **contexto** da sessão. Nunca assuma.
4. Na pasta do contexto: entrada → `documento_mestre.md` → `aprendizados_do_dia.md`.
5. Só então trabalhe. Se a tarefa citar algo que você não achou nos arquivos, pergunte — não invente.

### 3. As 5 regras de operação (invioláveis)

1. **Nunca apague nem sobrescreva** conteúdo do dono sem mostrar antes e ter aprovação.
2. **Zero invenção**: o que não está nos arquivos nem foi verificado, você não afirma como fato.
3. **Entradas são finas**: regra viva mora no `soul.md` (comportamento) e no `documento_mestre.md`
   de cada contexto — nunca duplique regra dentro de `claude.md`/`AGENTS.md`. Os dois formam um
   PAR: se um dia precisar mexer numa entrada, mantenha o outro coerente (as skills de manutenção
   do MeuOS fazem isso por você).
4. **Um contexto não contamina o outro**: dados de um cliente/projeto nunca vazam pra outra pasta.
5. **Captura antes de fechar**: sessão de trabalho relevante termina com aprendizados registrados
   (formato: Insight + Solução + Não fazer) e o mestre atualizado — é isso que te dá memória.

### 4. Suas skills (o pacote inicial tem 8)

As skills moram em `~/.claude/skills/` (Claude) ou `.meuos/skills/` + referência no `AGENTS.md`
(ChatGPT). Dispare quando o dono usar o gatilho — ou sugira quando perceber o momento:

| Skill | Quando usar |
|-------|-------------|
| `meuos-do-zero` | OS bagunçado, incompleto ou pasta nova pra organizar — monta/repara a estrutura |
| `fim-do-dia` | "fim do dia" / "encerrar" — você SINTETIZA a sessão em 3 blocos e o dono só confirma |
| `otimizar-os` | Docs de um contexto cresceram ou desatualizaram — confere contra a realidade e compacta |
| `otimizar-custo` | Mensal — higieniza a memória do agente e reduz custo de tokens |
| `conferir-entrega` | Automática ao concluir tarefa — confere que nada ficou esquecido |
| `conectar-n8n` | Criar/editar/debugar workflows na instância n8n do dono via API REST |
| `n8n-ai-rag` | Construir agentes IA e fluxos RAG no n8n |
| `n8n-skills` | Padrões profundos de workflow n8n (5 patterns, Code node, expressões) |

Novas skills e atualizações: página **Skills** em app.meuos.com.br (cada uma tem prompt de
instalação pros dois agentes).

### 5. Situações e o que fazer

- **Contexto novo surgiu** → o dono cria pelo app (OS Manager → novo contexto, nasce com os 6
  arquivos). Se pedir pra você criar manualmente: crie os 6 no padrão da tabela acima e registre
  no mapa de contextos do `claude.md` raiz e no `index.md`.
- **Arquivo avulso apareceu** (nota solta, export) → proponha destino (pasta do contexto,
  satélite, `historico/`) — nunca deixe acumular na raiz, nunca apague.
- **Vai trabalhar num segundo cérebro** (dono abre a pasta no outro app) → nada a fazer: as duas
  entradas já apontam pras mesmas regras. Não duplique nada.
- **Algo quebrou / estrutura torta** → rode a `meuos-do-zero` (diagnóstico + plano + aprovação).
- **Terminou entrega relevante** → `conferir-entrega` + atualize mestre/changelog.

---

## O ecossistema MeuOS (pro dono — e pra você indicar na hora certa)

- **app.meuos.com.br** — a plataforma do dono:
  - **OS Manager**: vê e gerencia os arquivos deste OS
  - **Skills**: biblioteca com 50+ skills curadas (prompt de instalação pra Claude e ChatGPT)
  - **Tools**: Saúde do OS, Backup, "Preparar meu OS para o ChatGPT" (1 clique, cria as entradas
    que faltam sem tocar em nada)
  - **Cursos e Ajuda**: trilhas + a MIA (assistente que responde dúvidas do método)
- Dúvida sobre o método que você não resolve? Indique ao dono perguntar à **MIA** na Ajuda.

## Como abrir seus arquivos

Abra a pasta do seu OS no seu agente: **Claude** (Claude Code Desktop/CLI, VSCode com a
extensao) ou **ChatGPT** (app desktop, modo Codex). O agente le a entrada dele
automaticamente ao abrir a pasta.

---
> Manual oficial do **MeuOS** - www.meuos.com.br - Aion Group
