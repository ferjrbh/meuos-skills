---
name: Otimizar OS
description: |
  Organiza e compacta os arquivos do contexto ativo quando estao crescendo demais.
  Executa quando o usuario diz "otimizar os", "organizar arquivos", "arquivos grandes",
  "compactar docs", "higienizar", "limpar documentos", "doc-compactor", "reduzir arquivos",
  "arquivos crescendo", "limpar terreno", "organizar contexto".
  Analisa, propoe um plano e executa somente com aprovacao do usuario.
version: 3.3
context: meuos
user-invocable: true
---

# Otimizar OS — Organizacao e Compactacao de Documentos

## O que esta skill faz

Esta skill analisa todos os arquivos de documentacao do seu OS (raiz + todas as pastas + todas as subpastas), identifica quais estao crescendo demais e propoe um plano de organizacao. Ela pode resumir secoes antigas, mover conteudo concluido para o historico e sugerir a criacao de arquivos secundarios quando o documento principal estiver sobrecarregado. Tudo com sua aprovacao antes de qualquer mudanca.

---

## Quando usar

- Quando o agente alertar que arquivos estao com semaforo 🔴 na Revisao Diaria
- Antes de uma sessao longa em um contexto (para "limpar o terreno")
- Quando sentir que os arquivos estao pesados e dificeis de navegar
- Uma vez por mes como higiene preventiva
- Quando o usuario diz "otimizar os", "organizar arquivos", "arquivos grandes"

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0 — Backup da Memoria do Claude Code (sempre primeiro)

**Antes de qualquer scan/edicao**, copiar a memoria do Claude Code para uma pasta versionada dentro do OS do usuario. Isso protege contra perda de maquina, renomeacao da pasta de trabalho ou troca de equipamento — a memoria do Claude vive em `~/.claude/` (fora do Drive/OneDrive).

**Origem:** `~/.claude/projects/{working-dir-encoded}/memory/`
**Destino:** `meuos/auto-memory-backup/{YYYY-MM-DD}/`

```bash
DATA=$(date +%Y-%m-%d)
WORKING_DIR_ENCODED=$(pwd | sed 's|:||;s|/|-|g;s|\\|-|g')
ORIGEM=~/.claude/projects/${WORKING_DIR_ENCODED}/memory
DESTINO="meuos/auto-memory-backup/${DATA}"

# Se a memoria existe, copiar
if [ -d "$ORIGEM" ]; then
  mkdir -p "$DESTINO"
  cp -r "$ORIGEM"/* "$DESTINO/" 2>/dev/null
  echo "OK — memoria copiada para $DESTINO"
else
  echo "Sem memoria do Claude Code para este diretorio (pular)"
fi
```

**Rotacao automatica — manter os 10 backups mais recentes:**

```bash
cd meuos/auto-memory-backup 2>/dev/null && \
  ls -t | tail -n +11 | xargs -I {} rm -rf "{}" 2>/dev/null
```

**Se a pasta `meuos/auto-memory-backup/` nao existir**: criar automaticamente. **Se a pasta `~/.claude/projects/.../memory/` nao existir**: pular silenciosamente (o usuario pode nao usar Claude Code, ou e diretorio novo).

**Reportar ao usuario:** `"Backup da memoria do Claude: [N arquivos copiados para auto-memory-backup/{data}/] (10 mais recentes mantidos)"` ou `"Sem memoria pra fazer backup neste diretorio."`

---

### PASSO 0.5 — Identificar o contexto a otimizar (escopo obrigatorio)

**Esta skill SEMPRE roda em UM contexto por vez.** Antes de qualquer scan ou edicao, identificar exatamente qual pasta sera otimizada:

- Se o usuario informou na chamada: usar esse
- Se ficou obvio pela conversa: usar esse
- Se houver duvida ou nao foi informado: **PERGUNTAR**:

```
"Em qual contexto vou rodar a organizacao? Exemplos:
- Pessoal
- Consultoria/ClienteA
- Consultoria/ClienteB
- Produtos/MeuApp
- Raiz (apenas arquivos da raiz, sem entrar em pastas)

Qual?"
```

**NUNCA escanear o OS inteiro de uma vez.** Esta skill organiza UM contexto. Se o usuario quiser organizar varios, rodar a skill multiplas vezes (uma por contexto).

---

Antes de qualquer acao, confirmar o contexto:
- Se o usuario informou: usar esse
- Se ficou obvio: usar esse
- Se houver duvida: perguntar `"Em qual contexto rodar a organizacao? (Pessoal / [Nome da Empresa]?)"`

**Nota sobre profundidade do OS:** O usuario pode ter um OS em qualquer uma destas configuracoes — adaptar ao que existir:
- **Flat (1 nivel):** arquivos diretamente na raiz do OS
- **Com pastas (2 niveis):** raiz + pastas de contexto (ex: `Consultoria/`)
- **Com subpastas (3 niveis):** raiz + pastas + subpastas (ex: `Consultoria/ClienteA/`)

O scan de diagnostico (Passo 1) cobre todos os niveis existentes. Pastas excluidas automaticamente: `.meuos/` e `bkp/`.

---

### PASSO 1 — Scan e relatorio de saude (APENAS DO CONTEXTO ESCOLHIDO)

**Importante:** esta skill roda em **UM contexto por vez**. Se o usuario nao informou qual, **perguntar no PASSO 0** antes de prosseguir. Nunca escanear o OS inteiro de uma vez — isso vira plano impossivel de aprovar item-a-item.

Escolha valida do contexto:
- "Pessoal" → escaneia raiz + apenas a pasta `Pessoal/` e suas subpastas
- "Consultoria/ClienteA" → escaneia apenas `Consultoria/ClienteA/` (e subpastas dela, se houver)
- "Raiz" → escaneia apenas os arquivos diretamente na raiz (sem entrar em pastas)

Para cada nivel **dentro do contexto escolhido**:
- Listar todos os arquivos `.md`
- Coletar: nome, numero de linhas, tamanho em KB
- Identificar o `*MESTRE.md` de cada contexto (qualquer arquivo terminando em `MESTRE.md`)

Apresentar uma tabela com semaforo de saude, agrupada por contexto com path completo:

```
Relatorio de Saude — MeuOS
Data: [DATA]

RAIZ
| Arquivo | Linhas | Tamanho | Status |
|---------|--------|---------|--------|
| claude.md | 95 | 6KB | 🟢 ok |
| soul.md | 42 | 3KB | 🟢 ok |
| aprendizados_do_dia.md | 180 | 11KB | 🟢 ok |
| changelog.md | 210 | 18KB | 🟡 atencao |

CONSULTORIA/CLIENTEA
| Arquivo | Linhas | Tamanho | Status |
|---------|--------|---------|--------|
| CLIENTEA_DOCUMENTO_MESTRE.md | 487 | 28KB | 🔴 muito grande |
| aprendizados_do_dia.md | 220 | 14KB | 🟡 atencao |
| changelog.md | 150 | 10KB | 🟢 ok |

CONSULTORIA/CLIENTEB
| Arquivo | Linhas | Tamanho | Status |
|---------|--------|---------|--------|
| CLIENTEB_DOCUMENTO_MESTRE.md | 180 | 12KB | 🟢 ok |
| aprendizados_do_dia.md | 95 | 6KB | 🟢 ok |
```

**Regras de semaforo:**

| Arquivo | 🟢 OK | 🟡 Atencao | 🔴 Precisa de acao |
|---------|-------|-----------|-------------------|
| `*MESTRE.md` (qualquer nivel) | menos de 300 linhas | 300 a 500 | mais de 500 |
| `claude.md` | menos de 200 linhas | 200 a 300 | mais de 300 |
| Arquivos secundarios (ex: `empresa_detalhes.md`) | menos de 25KB | 25 a 40KB | mais de 40KB |
| `changelog.md` | menos de 30KB | 30 a 50KB | mais de 50KB |
| `aprendizados_do_dia.md` | menos de 200 linhas | 200 a 250 | mais de 250 |
| `index.md` | menos de 100 linhas | 100 a 150 | mais de 150 |
| Outros arquivos `.md` | menos de 20KB | 20 a 35KB | mais de 35KB |

---

### PASSO 2 — Analise profunda

Para cada arquivo com status 🔴 ou 🟡 (em qualquer nivel), analisar o conteudo e identificar:

**2a. Separar o que e permanente do que e temporario (criterio primario)**

Antes de olhar a idade do conteudo, o agente classifica cada bloco pelo seu TIPO:

| Tipo | Exemplos | O que acontece |
|------|----------|----------------|
| **Permanente** | Regras do seu negocio, padroes de trabalho, convencoes, "nunca fazer X", configuracoes ativas | **Fica onde esta** — nao importa a idade |
| **Promovivel** | Regra que voce usa em toda sessao e deveria estar no documento mestre | **Sobe para o documento_mestre.md** — fica mais visivel e permanente (ver 2d) |
| **Temporario** | Entregas concluidas, bugs corrigidos, decisoes pontuais, status updates datados | Compacta conforme a idade (ver abaixo) |
| **Ultrapassado** | Status que nao vale mais, pesquisa ja usada, decisao substituida por outra mais recente | **Vai para o historico** ou changelog |

**Como o agente identifica o tipo:**
- Contem "nunca", "sempre", "regra", "padrao", "obrigatorio" → provavelmente **permanente**
- Contem data especifica + resultado pontual ("Bug X corrigido em DD/MM") → **temporario**
- Referencia a estado passado ("aguardando X" quando X ja aconteceu) → **ultrapassado**
- Usado em toda sessao do contexto (o agente consulta frequentemente) → **promovivel**

**2a.1 Para conteudo temporario, aplicar criterio de idade:**

| Idade | O que fazer |
|-------|-------------|
| Menos de 30 dias | Nao mexer — conteudo ativo |
| 30 a 60 dias | Propor condensacao (3 paragrafos viram 3 linhas) |
| 60 a 90 dias | Condensar obrigatoriamente + mover detalhes para o changelog |
| Mais de 90 dias | Manter apenas 1 linha resumo + referencia ao changelog |

**2b. Secoes densas que podem virar arquivos separados**

Quando um `*MESTRE.md` (em qualquer nivel do OS) tiver uma secao com mais de 50 linhas sobre um unico tema, ela e candidata a virar um arquivo separado referenciado no mestre. Criar o arquivo separado na mesma pasta do mestre.

Exemplos de bons candidatos para arquivo separado:
- Historico de decisoes tecnicas de um sistema especifico
- Especificacoes detalhadas de um modulo ou produto
- Mapeamentos de APIs e integracoes
- Documentacao de fluxos comerciais detalhados

**2c. Conteudo obsoleto**

Identificar:
- Arquivos de pesquisa ou analise pontuais que ja cumpriram seu papel
- Secoes sobre decisoes que foram substituidas por decisoes mais recentes
- Status desatualizados (ex: "aguardando X" sendo que X ja aconteceu)

**2d. Regras que merecem subir para o documento mestre**

Algumas regras nos seus aprendizados sao tao importantes que deveriam estar no documento mestre (o documento vivo que o agente le antes de trabalhar). Exemplos:
- "Nunca compartilhar dados deste cliente com outros contextos"
- "Sempre pedir aprovacao antes de alterar o produto"
- "Brevo so para campanhas, nunca para alertas internos"

O agente identifica essas regras e pergunta:
> `"Encontrei X regras nos aprendizados que parecem permanentes. Quer que eu promova para o documento mestre?"`

Se voce aprovar, a regra:
1. E adicionada no documento_mestre.md do contexto (na secao de regras)
2. E removida dos aprendizados (para nao ficar duplicada)
3. E registrada no changelog (historico da mudanca)

> Por que o mestre e nao o claude.md? Porque o claude.md tem regras que quase nunca mudam (instrucoes basicas do agente). O mestre e o documento vivo que o agente le antes de trabalhar — regras operacionais ficam melhor la.

---

### PASSO 3 — Plano de acao (sempre mostrar antes de executar)

Apresentar ao usuario uma lista numerada das acoes propostas, agrupadas por tipo e indicando o path completo de cada arquivo:

```
Plano de Organizacao — MeuOS

RESUMIR CONTEUDO ANTIGO (X acoes)
1. [Consultoria/ClienteA/CLIENTEA_DOCUMENTO_MESTRE.md] Secao "Decisoes de Marco" (mais de 60 dias): condensar de 45 → ~8 linhas
2. [changelog.md] Entradas antes de Janeiro/2026: arquivar em historico/

CRIAR ARQUIVO SEPARADO (X acoes)
3. [Consultoria/ClienteA/CLIENTEA_DOCUMENTO_MESTRE.md] Secao "Integracao com API X" (55 linhas): criar Consultoria/ClienteA/CLIENTEA_TECH_API_X.md
4. [Consultoria/ClienteA/CLIENTEA_DOCUMENTO_MESTRE.md] Secao "Historico de Contratos" (70 linhas): criar Consultoria/ClienteA/CLIENTEA_COMERCIAL_CONTRATOS.md

ARQUIVAR OBSOLETOS (X acoes)
5. [Consultoria/ClienteB/pesquisa_plataformas_2025.md] Analise pontual ja concluida → mover para Consultoria/ClienteB/historico/

MANTER (sem acao)
- [claude.md] Conteudo evergreen — nao alterar
- [Consultoria/ClienteB/CLIENTEB_DOCUMENTO_MESTRE.md] Tamanho adequado — nao alterar
```

Perguntar ao usuario:
> `"Posso executar o plano completo? Ou prefere aprovar item por item?"`

**NUNCA executar sem resposta do usuario.**

---

### PASSO 4 — Execucao (somente com aprovacao)

Executar apenas os itens aprovados, nesta ordem:

**4a. Resumir conteudo antigo**
1. Ler a secao original antes de alterar (nao perder nada)
2. Reescrever em formato compacto:
   - Decisoes: `**[DATA] Decisao:** [resultado em 1 frase]. Detalhes no changelog [DATA].`
   - Processos concluidos: `**[TEMA]:** [resultado final]. Ver changelog para detalhes.`
   - Status desatualizados: remover (ja estao no changelog)
3. Verificar que nenhuma referencia a outros arquivos quebrou

**4b. Criar arquivo separado (split)**
1. Criar novo arquivo com nome descritivo na mesma pasta do mestre: `[CONTEXTO]_[AREA]_[TEMA].md`
2. Adicionar no topo do novo arquivo uma linha apontando de onde veio:
   ```
   > Documento pai: [path/NOME_DOCUMENTO_MESTRE.md]
   ```
3. Mover o conteudo (cortar do mestre, colar no novo arquivo)
4. No `*MESTRE.md`, substituir o conteudo removido por um ponteiro (gancho inline):
   ```
   > **[TEMA]:** [resumo de 1 a 2 linhas]. Documento completo: `[path/nome_do_arquivo.md]`
   ```
5. Atualizar a tabela de arquivos do contexto no documento mestre (se houver)

**Atualizar index.md apos cada criacao:**
- Se `index.md` existir na pasta do contexto: adicionar entrada para o novo arquivo com link e descricao
- Se o arquivo original foi arquivado: remover a entrada do index.md do contexto
- Se houve mudanca na raiz: atualizar tambem o index.md da raiz
- Atualizar data e contadores no cabecalho de cada index tocado
- O index.md e atualizado JUNTO com cada acao — nao esperar o final

> Cada contexto tem seu proprio index.md. A raiz tem o index geral que aponta para os contextos.

**Limite:** no maximo 3 arquivos novos por execucao para nao fragmentar demais.

**Como a arvore de arquivos fica organizada depois da execucao:**

```
MESTRE (documento principal — ponteiros para tudo, max 300 linhas)
|
+-- Arquivo separado N1 (tema principal, ex: CLIENTEA_TECH_DECISOES.md)
|   |
|   +-- Arquivo separado N2 (sub-tema, se o N1 crescer muito)
|
+-- Arquivo separado N1 (outro tema)
|
+-- changelog.md (historico de entregas e decisoes)
    |
    +-- historico/CHANGELOG_2026_Q1.md (arquivado quando o changelog passa de 50KB)
```

**Regra do ponteiro dos dois lados:**
- Arquivo pai (mestre) aponta para baixo: `ver ARQUIVO_SEPARADO.md`
- Arquivo filho (separado) tem cabecalho apontando para cima: `> Documento pai: NOME_MESTRE.md`

Isso mantem a navegacao clara nos dois sentidos.

**4c. Arquivar conteudo obsoleto**
1. Criar pasta `historico/` dentro do mesmo contexto se nao existir
2. Mover arquivo para `[path]/historico/nome_original.md`
3. Se for o changelog, mover apenas as entradas antigas — manter o arquivo com as entradas recentes e o cabecalho

**4d. Caca de MDs orfaos (SEMPRE executar)**

**O que e um MD orfao:** arquivo `.md` que existe fisicamente em alguma subpasta do contexto mas **nao tem ponteiro** no `index.md` daquela pasta nem e mencionado no `*MESTRE.md` do contexto. Sem ponteiro, o agente futuro nao sabe que aquele arquivo existe — conhecimento se perde silenciosamente.

**Procedimento:**

1. Listar TODOS os `.md` do contexto escolhido (recursivo, ignorando `historico/`, `tmp/`, `node_modules/`, `.git/`)

2. Para cada arquivo, verificar se ha referencia a ele em:
   - `index.md` da propria pasta
   - `index.md` de pastas-pai dentro do contexto
   - `*MESTRE.md` do contexto
   - `claude.md` do contexto (se houver)

3. Para arquivos **sem nenhuma referencia** (orfaos), apresentar tabela ao usuario:

```
| # | Arquivo orfao | Localizacao | Sugestao |
|---|---------------|-------------|----------|
| O1 | analise_concorrentes.md | Consultoria/ClienteA/docs/ | Adicionar ponteiro no index.md (categoria Analises) |
| O2 | tech_integracao_nova.md | Consultoria/ClienteA/tech/ | Mencionar no MESTRE secao Integracoes + ponteiro no index |
| O3 | rascunho_velho.md | Consultoria/ClienteA/tmp_old/ | Mover para historico/ (arquivo antigo) |
```

4. Aguardar aprovacao do usuario item-a-item ou em lote ("todos os ponteiros sim, O3 arquivar").

5. Executar aprovados:
   - **Adicionar entrada no index.md** da pasta correspondente: `- [NOME](caminho) — descricao one-liner`
   - **Mencionar inline no MESTRE** com ponteiro (se for satelite relevante para o contexto)
   - **Mover para historico/** (se for obsoleto)

**REGRA — nunca decidir sozinho:** o agente nunca decide se um orfao e relevante ou obsoleto. Sempre apresentar a tabela e aguardar a resposta do usuario.

---

**4e. Confirmar cada alteracao**
Antes de salvar qualquer mudanca em arquivo existente, mostrar o antes e depois:
```
ANTES:
[trecho original — primeiras linhas]

DEPOIS:
[trecho resumido — como ficara]

Confirmar? (sim / nao / ajustar)
```

---

### PASSO 5 — Relatorio final

Apresentar o resultado da organizacao com paths completos:

```
Organizacao concluida ✓

| Arquivo | Antes | Depois | Reducao |
|---------|-------|--------|---------|
| Consultoria/ClienteA/CLIENTEA_DOCUMENTO_MESTRE.md | 487 linhas | 220 linhas | -55% |
| changelog.md | 210 linhas | 140 linhas | -33% |

Novos arquivos criados:
- Consultoria/ClienteA/CLIENTEA_TECH_API_X.md (detalhes da integracao)
- Consultoria/ClienteA/CLIENTEA_COMERCIAL_CONTRATOS.md (historico de contratos)

Arquivados:
- Consultoria/ClienteB/historico/pesquisa_plataformas_2025.md

Status atual:
- Consultoria/ClienteA/CLIENTEA_DOCUMENTO_MESTRE.md: 🟢 ok
- changelog.md: 🟢 ok
- aprendizados_do_dia.md: 🟢 ok
```

Se ainda houver arquivos 🟡 ou 🔴 restantes (itens nao aprovados), indicar claramente:
> `"Ainda ha X arquivos acima do limite ideal. Posso organiza-los numa proxima execucao quando quiser."`

---

## Formato de saida

**`*MESTRE.md`** — apos a organizacao:
- Deve ser legivel em menos de 5 minutos
- Contem: escopo do contexto, status atual, pendencias abertas, ponteiros para arquivos de detalhe
- NAO contem: historico detalhado, logs de decisoes antigas, especificacoes extensas

**Arquivo separado criado:**
```markdown
> Documento pai: [path/NOME_DOCUMENTO_MESTRE.md]

# [Titulo do Tema]
> Criado em: [DATA] | Extraido de: [NOME_DOCUMENTO_MESTRE.md]

[Conteudo completo do tema]
```

**changelog.md** — estrutura mantida, apenas entradas antigas arquivadas se aprovado

---

## Regras de seguranca

- **Nunca executar sem aprovacao** — sempre mostrar o plano primeiro
- **Nunca apagar conteudo** — apenas mover (changelog, historico/ ou arquivo separado)
- **Nunca resumir regras de negocio fundamentais** — independente da idade
- **Nunca criar mais de 3 arquivos novos por execucao** — evita fragmentacao excessiva
- **Nunca quebrar links entre arquivos** — todo arquivo separado tem ponteiro bidirecional
- **Nunca modificar arquivos de outro contexto** (quando o scope for um subcontexto especifico)
- **Sempre ler o arquivo antes de alterar** — nada de editar sem entender o conteudo primeiro
- **Sempre mostrar antes/depois** para alteracoes em arquivos existentes
- **Nunca assumir que o OS e flat** — sempre escanear raiz + pastas + subpastas antes de declarar o relatorio completo

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
