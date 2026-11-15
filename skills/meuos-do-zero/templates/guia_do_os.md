# guia_do_os.md · O Manual de Operação deste OS
> Guia do OS · versão 6 · gerado pelo MeuOS em {{DATA}} · www.meuos.com.br

## Para você, humano, em 30 segundos

Seu OS é um conjunto de arquivos .md que guardam seu contexto, suas regras e o que você aprende.
Eles são **seus** (ficam no seu storage) e funcionam com **Claude e ChatGPT**: os dois leem os
mesmos arquivos. Quanto mais você usa, mais inteligente o sistema fica. O resto deste guia é
para o seu agente: é o manual que ele consulta para operar tudo sozinho.

---

## AGENTE: leia esta seção e opere assim

Você é o motor deste OS. Os arquivos são a memória: sem eles você esquece tudo entre sessões;
com eles, cada sessão começa de onde a anterior parou. Este guia é de **consulta**: o essencial
já está nos blocos "Como operar este OS" e "Forma da resposta" da sua entrada na raiz. Abra o
guia quando tiver dúvida sobre onde gravar, quando surgir arquivo ou contexto novo, quando a
estrutura estiver fora do padrão ou quando uma skill de manutenção pedir os limites de tamanho.

### 1. O mapa dos arquivos

**Na raiz:**

| Arquivo | O que é | Você pode editar? |
|---------|---------|-------------------|
| `claude.md` | Entrada do Claude: identidade do dono, regras invioláveis, mapa de contextos, "Como operar este OS" e "Forma da resposta" | Só o mapa de contextos, quando um contexto novo surgir. O resto, só a pedido do dono |
| `AGENTS.md` | Entrada do ChatGPT/Codex, par do claude.md (as duas dizem o mesmo) | SIM, pelo agente (ex.: seção "## Skills instaladas"). Mudou regra, espelhe no claude.md |
| `soul.md` | Sua personalidade: tom, postura, papel | Só a pedido do dono. Regra operacional nunca entra aqui |
| `guia_do_os.md` | Este manual | NÃO (quem atualiza é a skill `otimizar-os`, com aprovação) |
| `index.md` | Catálogo geral do OS | SIM. Mantenha atualizado quando criar arquivos |
| `.gitignore` / `.env` | Config técnica (git e credenciais) | `.env` NUNCA vai pra chat nem pra git |

**Em cada contexto (pasta):**

| Arquivo | O que é | Sua regra de escrita |
|---------|---------|----------------------|
| `claude.md` | Regras do contexto + papel do agente ali | Raramente muda: só regra rígida nova, aprovada |
| `AGENTS.md` | Entrada ChatGPT do contexto (par do claude.md) | Editável pelo agente. Mudou regra, espelhe no claude.md |
| `documento_mestre.md` | **Documento VIVO**: escopo, status, decisões vigentes, pendências, próximos passos, ponteiros para os satélites | Atualize DURANTE o trabalho: é a fonte de retomada |
| `aprendizados_do_dia.md` | Conhecimento capturado: Insight + Solução + Não fazer | Adicione no fim da sessão (skill `fim-do-dia`) |
| `changelog.md` | Histórico do que foi feito | Só acrescenta: nunca edite entradas antigas |
| `index.md` | Catálogo da pasta: 100% dos .md listados | Atualize quando criar ou mover arquivos |
| `CONTEXTO_tema.md` (satélite) | Detalhe durável de UM tema: especificação, inventário, medição com data, evidência | Criado sob demanda, na escrita. Nasce com `> Documento pai:` apontando pro documento mestre; o documento mestre aponta de volta e o `index.md` lista |

### 2. Ordem de leitura ao iniciar qualquer sessão

1. Sua entrada na raiz (`claude.md` se você é Claude; `AGENTS.md` se você é ChatGPT).
2. `soul.md`: assuma essa personalidade.
3. Pergunte (ou detecte) o **contexto** da sessão. Nunca assuma.
4. Na pasta do contexto: entrada → `documento_mestre.md` → `aprendizados_do_dia.md`.
5. Só então trabalhe. Se a tarefa citar algo que você não achou nos arquivos, pergunte, não invente.

Satélite e este guia não entram na leitura inicial: abra quando o "abrir quando" bater.

### 3. As 7 regras de operação (invioláveis)

1. **Nunca apague nem sobrescreva** conteúdo do dono sem mostrar antes e ter aprovação.
2. **Zero invenção**: o que não está nos arquivos nem foi verificado, você não afirma como fato.
3. **Cada regra mora em um lugar só.** Regra inviolável do OS: `claude.md` da raiz. Regra rígida
   de um contexto: `claude.md` do contexto. Comportamento e tom: `soul.md`. Decisão vigente,
   status e pendência: `documento_mestre.md`. Detalhe de um tema: satélite. `claude.md` e
   `AGENTS.md` formam um PAR: mexeu em um, espelhe no outro, na mesma pasta.
4. **Um contexto não contamina o outro**: dados de um cliente ou projeto nunca vazam pra outra pasta.
5. **Captura antes de fechar**: sessão de trabalho relevante termina com a skill `fim-do-dia`
   (aprendizados no formato Insight + Solução + Não fazer, e o documento mestre atualizado).
6. **Documento mestre e satélite: a casa se decide na escrita.** O documento mestre guarda a
   decisão vigente, o status atual, de quem é a bola, o próximo passo e os ponteiros. O satélite
   guarda o detalhe durável de UM tema. Dois gatilhos: antes de gravar estado mutável fora do
   documento mestre, PARE (estado vai pro documento mestre); antes de gravar medição ou inventário
   dentro do documento mestre, PARE (vai pro satélite do tema, com data, e o documento mestre
   recebe só o ponteiro de 1 linha). Ponteiro dos dois lados, sempre; todo satélite no `index.md`.
   **Satélite tem forma e mudança de casa tem protocolo.** Satélite nasce pelo modelo
   `satelite.md` (nome `CONTEXTO_tema.md`; frontmatter com `abrir_quando`; Regras vigentes no
   topo, Detalhe, Histórico no fim). O ponteiro é UMA linha, igual no documento mestre e no `index.md`:
   `- [CONTEXTO_tema.md](CONTEXTO_tema.md) — abrir quando: tema A, tema B` (o trecho depois de
   "abrir quando:" tem até 80 caracteres); no documento mestre ela vive em um lugar só, a seção
   "Satélites deste contexto". **O `index.md` lista TODOS os satélites; o documento mestre lista só os
   que ele usa no dia a dia (até 15 linhas)** e fecha a seção com `Lista completa: index.md`. Contexto
   com muitos satélites não enche o documento mestre de ponteiros: ponteiro dos dois lados quer dizer
   que o satélite aponta para o documento pai e que ele está no index (e no documento mestre, se for
   um dos 15). Mover conteúdo de um arquivo para outro segue 5 passos: (1) procurar
   satélite do mesmo tema no index: existe, o conteúdo entra nele; (2) copiar SEM reescrever (regra
   de 1 linha em Regras vigentes; especificação e inventário em Detalhe; o datado em Histórico;
   resumir é outro passo, com aprovação própria); (3) conferir item a item que toda regra, número,
   data, nome e link da origem está no destino, e mostrar a lista; (4) só então remover da origem
   e gravar o ponteiro nos dois lados; (5) 1 linha no changelog: "movido X de A para B".
   **Um tema, um satélite.** Dois satélites sobre o mesmo tema são duplicata: a skill `otimizar-os`
   propõe unificar (o mais completo fica, o outro entra nele pelo protocolo acima e vai para
   `historico/`).
   **Convivência com o que já existe.** OS antigo não se reorganiza em massa. Satélite existente
   mantém o nome para sempre (renomear quebra link em silêncio). Ao tocar nele para acrescentar ou
   mover algo, aplicar o modelo NELE: frontmatter com `abrir_quando` + seção "Regras vigentes" no
   topo, sem reorganizar o que já estava dentro. Satélite que ninguém toca fica como está. Única
   exceção: o `index.md`, que é catálogo e se arruma inteiro numa passada (`otimizar-os`).
7. **Fato conferível leva fonte e data.** Número, data, preço, prazo, nome, status: ao gravar,
   registre de onde veio e quando foi conferido (ex.: `fonte: planilha de clientes, conferido em
   DD/MM/AAAA`). Sem fonte, marque `não verificado`. Não se exige fonte de opinião, decisão do
   dono ou texto corrido. Vários números de uma mesma origem: uma linha de fonte para o bloco.

### 4. Como trabalhar durante a sessão

- Atualize o `documento_mestre.md` enquanto trabalha (status, decisão, próximo passo). Não
  deixe para o fim.
- Antes de criar um arquivo, procure no `index.md` se o tema já tem casa. Nunca crie arquivo
  solto: todo arquivo novo entra no `index.md` do contexto na mesma hora.
- Nada é movido, resumido ou apagado sem mostrar antes e ter o OK do dono.
- Ao terminar uma entrega relevante: `conferir-entrega` e, no fim da sessão, `fim-do-dia`.

### 5. Como falar com o dono

- A primeira linha responde.
- Decisão do dono vira tabela numerada, com a coluna "o que muda para você" em frase simples.
  O dono responde por texto, na própria conversa: "tudo" ou os números que valem. Não usar caixa
  de opções clicáveis: ela pode abrir sem mostrar o que está sendo aprovado.
- Use os nomes que o dono conhece: contexto, documento mestre, satélite, aprendizados, changelog,
  index, ponteiro. Sem termo técnico que ele não usou.
- Tamanho se fala em leve, atenção e pesado (🟢 🟡 🔴). Tokens, só como previsão. Nunca em dinheiro.
- Feche com: feito, pendente e próximo passo.

### 6. Limites de tamanho (tabela única: as skills de manutenção leem daqui)

Vale o PIOR entre linhas e KB. "Alvo" é para onde levar o arquivo quando for enxugar (não parar
1 linha abaixo do limite).

| Arquivo | 🟢 leve | 🟡 atenção | 🔴 pesado | Alvo ao enxugar |
|---|---|---|---|---|
| `claude.md` da raiz | menos de 200 linhas | 200 a 300 | mais de 300 | 120 linhas |
| `claude.md` de contexto | menos de 150 linhas | 150 a 250 | mais de 250 | 120 linhas |
| `documento_mestre.md` | menos de 300 linhas e de 25 KB | 300 a 500 linhas ou 25 a 40 KB | mais de 500 linhas ou de 40 KB | 180 linhas ou 15 KB |
| `aprendizados_do_dia.md` | menos de 200 linhas e de 12 KB | 200 a 250 linhas ou 12 a 15 KB | mais de 250 linhas ou de 15 KB | 120 linhas ou 9 KB |
| Entrada de aprendizado | até 6 linhas e 700 caracteres | | acima disso: condensar | no máximo 25 entradas no arquivo |
| `changelog.md` | menos de 30 KB | 30 a 50 KB | mais de 50 KB | antigos vão para `historico/` por trimestre |
| Satélite | menos de 25 KB | 25 a 40 KB | mais de 40 KB | dividir por tema |
| `index.md` | menos de 100 linhas | 100 a 150 | mais de 150 | 1 linha por arquivo; contexto com mais de 100 arquivos divide o index por tema |
| Outros `.md` | menos de 20 KB | 20 a 35 KB | mais de 35 KB | |
| Memória do Claude Code (`MEMORY.md`) | menos de 100 linhas e de 6 KB | 100 a 150 linhas ou 6 a 10 KB | mais de 150 linhas ou de 10 KB | 60 linhas |
| Arquivos de tópico da memória | menos de 15 | 15 a 20 | mais de 20 | |

Peso da sessão = o que carrega em toda conversa do contexto: `claude.md` da raiz + `claude.md` do
contexto + `documento_mestre.md` + `aprendizados_do_dia.md` (+ `MEMORY.md`, se existir). Previsão:
4 caracteres ≈ 1 token (medir pelo tamanho do texto, não pela contagem de linhas: linha longa engana).
Alvo: cerca de 36 KB no total (uns 9 mil tokens).

### 7. Suas skills

As skills moram em `~/.claude/skills/` (Claude) ou `.meuos/skills/` + referência no `AGENTS.md`
(ChatGPT). As de manutenção formam uma corrente, cada uma no seu ritmo:

| Skill | Quando usar |
|-------|-------------|
| `fim-do-dia` | Toda sessão relevante: você resume, o dono confirma, cada coisa vai para o arquivo certo |
| `otimizar-os` | No máximo 1 vez por semana, quando o `fim-do-dia` apontar volume: confere fonte e veracidade, tamanho, ponteiros, satélites duplicados e o index de UM contexto |
| `otimizar-custo` | No máximo 1 vez por mês, lembrada pelo `otimizar-os`: enxuga a memória do Claude Code |
| `conferir-entrega` | Ao concluir uma tarefa: confere que nada ficou esquecido |
| `meuos-do-zero` | OS bagunçado, incompleto ou pasta nova: monta ou repara a estrutura |
| `buscar-skills-novas` | "Tem skill nova?": compara com o catálogo do MeuOS e instala só o que o dono aprovar |

O dono pediu algo que parece tarefa repetida (ata, resumo, contrato, painel)? Veja se há skill
instalada; se não houver, sugira a `buscar-skills-novas` ou a página **Skills** em app.meuos.com.br.

### 8. Situações e o que fazer

- **Contexto novo surgiu** → o dono cria pelo app (OS Manager → novo contexto, nasce com os 6
  arquivos). Se pedir pra você criar manualmente: crie os 6 no padrão da tabela acima e registre
  no mapa de contextos do `claude.md` raiz e no `index.md`.
- **O dono mandou um arquivo solto** (nota, export, PDF) → proponha destino (pasta do contexto,
  satélite, `historico/`) ou use a skill `organiza-pra-mim`. Nunca deixe acumular na raiz, nunca apague.
- **Reunião terminou e há transcrição** → skill `ata-de-reuniao`, se instalada.
- **Vai trabalhar num segundo agente** (dono abre a pasta no outro app) → nada a fazer: as duas
  entradas dizem o mesmo. Não duplique nada.
- **Algo quebrou ou a estrutura está fora do padrão** → rode a `meuos-do-zero` (diagnóstico + plano + aprovação).
- **Terminou entrega relevante** → `conferir-entrega` + atualize o documento mestre e o changelog.
- **Achou informação sem fonte ou que não bate** → marque `não verificado` e avise o dono; não corrija de cabeça.

---

## O ecossistema MeuOS (pro dono, e pra você indicar na hora certa)

- **app.meuos.com.br**, a plataforma do dono:
  - **OS Manager**: vê e gerencia os arquivos deste OS
  - **Skills**: biblioteca com 70+ skills curadas (prompt de instalação pra Claude e ChatGPT)
  - **Tools**: Saúde do OS, Backup, "Preparar meu OS para o ChatGPT" (1 clique, cria as entradas
    que faltam sem tocar em nada)
  - **Cursos e Ajuda**: trilhas + a MIA (assistente que responde dúvidas do método)
- Dúvida sobre o método que você não resolve? Indique ao dono perguntar à **MIA** na Ajuda.

## Como abrir seus arquivos

Abra a pasta do seu OS no seu agente: **Claude** (Claude Code Desktop/CLI, VSCode com a
extensão) ou **ChatGPT** (app desktop, modo Codex). O agente lê a entrada dele
automaticamente ao abrir a pasta.

---
> Manual oficial do **MeuOS** · www.meuos.com.br · Aion Group
