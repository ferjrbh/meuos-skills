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
| `AGENTS.md` | Entrada do ChatGPT/Codex — fina, aponta pro claude.md | SIM, pelo agente (ex.: seção "## Skills instaladas") — mudou regra, espelhe no claude.md pro par não divergir |
| `soul.md` | Sua personalidade: tom, postura, papel | Só a pedido do dono |
| `guia_do_os.md` | Este manual | NÃO |
| `index.md` | Catálogo geral do OS | SIM — mantenha atualizado quando criar arquivos |
| `.gitignore` / `.env` | Config técnica (git e credenciais) | `.env` NUNCA vai pra chat nem pra git |

**Em cada contexto (pasta):**

| Arquivo | O que é | Sua regra de escrita |
|---------|---------|----------------------|
| `claude.md` | Regras do contexto + papel do agente ali | Raramente muda — só regra nova aprovada |
| `AGENTS.md` | Entrada ChatGPT do contexto (ponteiro) | Editável pelo agente — mudou regra, espelhe no claude.md |
| `documento_mestre.md` | **Documento VIVO**: escopo, status, decisões, pendências, próximos passos | Atualize DURANTE o trabalho — é a fonte de retomada |
| `aprendizados_do_dia.md` | Conhecimento capturado: Insight + Solução + Não fazer | Adicione no fim da sessão (skill fim-do-dia) |
| `changelog.md` | Histórico do que foi feito | **Append-only** — nunca edite entradas antigas |
| `index.md` | Catálogo da pasta | Atualize quando criar/mover arquivos |
| `CONTEXTO_TEMA.md` (satélite) | Detalhe durável de UM tema: spec, inventário, medição com data, evidência | Criado sob demanda, na escrita. Nasce com `> Documento pai:` apontando pro mestre; o mestre aponta de volta e o `index.md` lista |

### 2. Ordem de leitura ao iniciar qualquer sessão

1. Sua entrada na raiz (`claude.md` se você é Claude; `AGENTS.md` → `claude.md` se você é ChatGPT).
2. `soul.md` — assuma essa personalidade.
3. Pergunte (ou detecte) o **contexto** da sessão. Nunca assuma.
4. Na pasta do contexto: entrada → `documento_mestre.md` → `aprendizados_do_dia.md`.
5. Só então trabalhe. Se a tarefa citar algo que você não achou nos arquivos, pergunte — não invente.

### 3. As 6 regras de operação (invioláveis)

1. **Nunca apague nem sobrescreva** conteúdo do dono sem mostrar antes e ter aprovação.
2. **Zero invenção**: o que não está nos arquivos nem foi verificado, você não afirma como fato.
3. **Entradas são finas**: regra viva mora no `soul.md` (comportamento) e no `documento_mestre.md`
   de cada contexto — nunca duplique regra dentro de `claude.md`/`AGENTS.md`. Os dois formam um
   PAR: se um dia precisar mexer numa entrada, mantenha o outro coerente (as skills de manutenção
   do MeuOS fazem isso por você).
4. **Um contexto não contamina o outro**: dados de um cliente/projeto nunca vazam pra outra pasta.
5. **Captura antes de fechar**: sessão de trabalho relevante termina com aprendizados registrados
   (formato: Insight + Solução + Não fazer) e o mestre atualizado — é isso que te dá memória.
6. **Mesa e gaveta (mestre ↔ satélite)**: o mestre é a mesa (decisão vigente, status atual, de quem
   é a bola, próximo passo, ponteiros); o satélite é a gaveta (detalhe durável de UM tema). A casa
   se decide na ESCRITA, pela natureza do fato, nunca na faxina pelo tamanho do arquivo. Dois
   gatilhos: antes de gravar estado mutável fora do mestre, PARE (estado vai pro mestre); antes de
   gravar medição/inventário dentro do mestre, PARE (vai pro satélite do tema, com data, e o mestre
   recebe só o ponteiro de 1 linha). Ponteiro dos dois lados, sempre; todo satélite no `index.md`.
   **Satélite tem forma e mudança de casa tem protocolo.** Satélite nasce pelo modelo
   `satelite.md` (nome `CONTEXTO_tema.md`; frontmatter com `abrir_quando`; Regras vigentes no
   topo, Detalhe, Histórico no fim). O ponteiro é UMA linha, igual no mestre e no `index.md`:
   `- [CONTEXTO_tema.md](CONTEXTO_tema.md) — abrir quando: tema A, tema B` (o trecho depois de
   "abrir quando:" tem até 80 caracteres); no mestre ela vive em um lugar só, a seção "Satélites deste
   contexto". Mover conteúdo de um arquivo para outro segue 5 passos: (1) procurar satélite do mesmo
   tema no index, existe → entra nele; (2) copiar SEM reescrever (regra de 1 linha em Regras vigentes;
   spec e inventário em Detalhe; o datado em Histórico; resumir é outro passo, com aprovação própria);
   (3) conferir item a item que toda regra, número, data, nome e link da origem está no destino, e
   mostrar a lista; (4) só então remover da origem e gravar o ponteiro nos dois lados; (5) 1 linha no
   changelog: "movido X de A para B".
   **Convivência com o que já existe (regra do escoteiro).** OS antigo não se reorganiza em massa.
   Satélite existente mantém o nome para sempre (renomear quebra link em silêncio). Ao tocar nele para
   acrescentar ou mover algo, aplicar o modelo NELE: frontmatter com `abrir_quando` + seção "Regras
   vigentes" no topo, sem reorganizar o que já estava dentro. Mestre sem a seção "Satélites deste
   contexto" ganha a seção no primeiro ponteiro, com aprovação. Satélite que ninguém toca fica como
   está. Única exceção: o `index.md`, que é catálogo e se arruma inteiro numa passada (otimizar-os).

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
