---
name: buscar-skills-novas
description: "Consulta o catalogo publico de skills do MeuOS no GitHub, compara com as skills instaladas localmente, mostra as novidades em tabela numerada e instala apenas o que o usuario aprovar. Usar quando o usuario disser 'busca skills novas', 'tem skill nova?', 'atualiza minhas skills', 'o que saiu de novo no MeuOS', 'instala a skill X do catalogo'. Funciona no Claude local e em agente OpenClaw na VPS."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Buscar Skills Novas

## O que esta skill faz

O catalogo oficial de skills do MeuOS e um repositorio publico no GitHub. Esta skill olha o catalogo, compara com o que o usuario ja tem instalado, apresenta o que ha de novo (ou atualizado) numa tabela numerada e instala SOMENTE o que o usuario aprovar. Instalar = copiar 1 arquivo `SKILL.md` para a pasta local de skills. Nada e executado, nada e sobrescrito sem aprovacao.

**Catalogo oficial:**

| # | Recurso | URL |
|---|---|---|
| 1 | Listar as skills do catalogo | `https://api.github.com/repos/ferjrbh/meuos-skills/contents/skills` |
| 2 | Baixar uma skill especifica | `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/{slug}/SKILL.md` |

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 1: Descobrir onde as skills moram NESTA maquina

A skill funciona em dois ambientes. Detectar qual existe:

| # | Ambiente | Diretorio de skills |
|---|---|---|
| 1 | Claude local (computador do usuario) | `~/.claude/skills/{slug}/SKILL.md` |
| 2 | Agente OpenClaw na VPS | `~/.openclaw/skills/{slug}/SKILL.md` (e onde o Curso OpenClaw MeuOS instala, P9; se o `openclaw skills list` mostrar outro diretorio, confirmar o caminho real na instalacao) |

Se nenhum dos dois existir, perguntar ao usuario onde as skills dele ficam. NUNCA chutar um caminho e criar pasta em lugar errado.

### PASSO 2: Levantar as skills instaladas

Listar as subpastas do diretorio local que contem `SKILL.md`. Para cada uma, ler do frontmatter o `name` e a `version`. Esse e o inventario local.

### PASSO 3: Consultar o catalogo (1 chamada so)

Fazer GET em `https://api.github.com/repos/ferjrbh/meuos-skills/contents/skills`. A resposta e um JSON: cada item com `"type": "dir"` e uma skill do catalogo, e o campo `"name"` e o slug.

Cuidados:

- E um repositorio publico: NAO precisa de token nem de credencial nenhuma.
- A API do GitHub sem autenticacao tem limite de requisicoes por hora. Por isso: **1 chamada para listar** e depois baixar via `raw.githubusercontent.com` (que nao consome esse limite) apenas o que interessar.
- Sem internet ou API fora do ar: avisar o usuario e parar. Nao inventar lista de skills de memoria.

### PASSO 4: Comparar e apresentar em tabela numerada

Para cada slug do catalogo que NAO esta instalado, baixar o `SKILL.md` correspondente (URL de raw acima) e extrair `name`, `version` e a primeira frase util da `description`. Para os que JA estao instalados, comparar a `version` do catalogo com a local.

Apresentar ao usuario:

```
| # | Skill | O que faz (1 linha) | Status |
|---|---|---|---|
| 1 | ata-de-reuniao | Transforma transcricao de reuniao em ata pronta | NOVA |
| 2 | resumo-executivo | Resume documento longo no formato de decisao | NOVA |
| 3 | pdf | Manipular arquivos PDF | atualizacao (1.2 instalada, 1.3 no catalogo) |
| 4 | fim-do-dia | Rotina de encerramento do dia | em dia |
```

> "Quais voce quer instalar/atualizar? Responda pelos numeros (ex: 1 e 3), 'todas' ou 'nenhuma'."

Se nao houver nada novo nem atualizado: dizer "tudo em dia" e parar. Nao instalar nada "por garantia".

### PASSO 5: Instalar SO o que foi aprovado

Para cada skill aprovada:

1. `mkdir -p {diretorio_de_skills}/{slug}`
2. Baixar `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/{slug}/SKILL.md` para `{diretorio_de_skills}/{slug}/SKILL.md`
3. Conferir que o arquivo baixado nao esta vazio e tem frontmatter valido (comeca com `---` e tem `name:`)

**Atualizacao de skill ja instalada e substituicao de arquivo: so com aprovacao explicita daquele item.** Se o usuario personalizou a skill local (conteudo diverge do catalogo alem da versao), avisar antes: atualizar vai sobrescrever a personalizacao. Nesse caso, oferecer guardar uma copia da versao local antes (ex: `SKILL.md.bak-local`).

### PASSO 6: Reportar

Uma mensagem curta: o que foi instalado/atualizado, com caminho, e o que ficou de fora por decisao do usuario.

> "Instaladas: ata-de-reuniao e resumo-executivo em `~/.claude/skills/`. A atualizacao do pdf ficou de fora, como voce pediu. Skills novas ficam disponiveis na proxima sessao do agente."

---

## Regras desta skill

- **Instalar e copiar arquivo, nunca executar.** O conteudo de uma skill so passa a valer quando o agente a carrega; a instalacao em si nao roda nada.
- **Nada entra sem aprovacao.** A tabela numerada e o pedido de aprovacao sao obrigatorios, mesmo que haja 1 skill nova so.
- **Nada e sobrescrito em silencio.** Atualizacao avisa a versao antiga e a nova; personalizacao local detectada gera backup antes.
- **Zero invencao.** A lista de skills vem da API na hora. Sem acesso, sem lista.
- **So o catalogo oficial.** Esta skill instala apenas do repositorio `ferjrbh/meuos-skills`. Skill de outra origem e decisao manual do usuario, fora daqui.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Diretorio local de skills identificado corretamente (ou perguntado ao usuario)
- [ ] Catalogo consultado ao vivo (1 chamada de listagem; nada de lista de memoria)
- [ ] Comparacao instaladas × catalogo apresentada em tabela numerada
- [ ] Usuario aprovou explicitamente CADA item instalado/atualizado
- [ ] Nenhuma skill sobrescrita sem aviso (backup da personalizacao local, se havia)
- [ ] Arquivos baixados conferidos (nao vazios, frontmatter valido)
- [ ] Reporte final com caminhos e o que ficou de fora

Se algum item falhou: corrigir ANTES de declarar concluido. Nunca reportar "feito" com item pendente.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
