---
name: preparar-os-para-chatgpt
description: |
  Prepara o seu OS para o ChatGPT/Codex: cria o arquivo AGENTS.md (a "porta de entrada"
  que o Codex le) na raiz e em cada contexto que ainda nao tem. Roda 100% local — enxerga
  TODOS os contextos, inclusive os que o seu proprio agente criou fora do app. So CRIA
  arquivos que faltam: nunca edita, nunca apaga, e rodar duas vezes nao muda nada.
  Executa quando o usuario diz "preparar meu os para o chatgpt", "preparar os para gpt",
  "criar agents.md", "meu os no codex", "deixar meu os pronto pro chatgpt".
version: 1.0
context: meuos
user-invocable: true
argument-hint: "(sem args — roda na pasta do OS aberta no agente)"
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Preparar meu OS para o ChatGPT — criar os AGENTS.md que faltam

> **Só cria.** Esta skill NUNCA edita nem apaga arquivo nenhum. Se o `AGENTS.md` já
> existe numa pasta, ela **não toca nele** (o conteúdo pode ter sido customizado).
> Rodar de novo é seguro: o que já está pronto é pulado.

## Passo 0 — Localize a raiz do OS (obrigatório)

1. A raiz do OS é a pasta que contém `claude.md` E `soul.md` (nomes em minúsculas).
2. Se a pasta atual não for a raiz, procure 1 nível acima e 1 abaixo.
3. **Se não encontrar, PARE** e diga: "Não encontrei a raiz do seu OS (pasta com claude.md
   e soul.md). Abra o agente na pasta do OS e rode a skill de novo."

## Passo 1 — Monte o plano (mostre ANTES de criar)

1. **Raiz**: se tem `claude.md` e **não** tem `AGENTS.md` → entra no plano.
2. **Contextos**: para cada pasta do nível 1 que **não** começa com `.` — se ela tem
   `claude.md` e **não** tem `AGENTS.md` → entra no plano.
   - Pasta sem `claude.md` **não é contexto**: ignore (não crie nada nela).
   - Pastas ocultas (`.claude/`, `.meuos/`), `bkp/`: ignore sempre.
3. Nome do OS: leia a 1ª linha do `claude.md` da raiz — se casar com
   `# {Nome} — claude.md`, use `{Nome}`; senão use "Meu OS".
4. Mostre o plano ao usuário (lista de arquivos a criar) e **peça confirmação**.
   Plano vazio → responda "Seu OS já está pronto para o ChatGPT — todos os contextos já
   têm AGENTS.md" e encerre.

## Passo 2 — Crie os arquivos (só após o "pode criar")

### `AGENTS.md` da RAIZ (substitua `{NOME}` pelo nome do OS)

```markdown
# {NOME} — AGENTS.md
> Entrada do Codex/ChatGPT deste OS (gerada pelo MeuOS · "Preparar meu OS para o ChatGPT").
> Este arquivo é seu: seu agente pode editá-lo (ex.: a seção "## Skills instaladas").
> Regras vivas preferem o [soul.md](soul.md) e os documentos de cada contexto.

## Leia antes de qualquer coisa, nesta ordem
1. [claude.md](claude.md) — as regras globais deste OS. Elas valem INTEGRALMENTE para você.
2. [soul.md](soul.md) — personalidade e tom do agente.

## Regra de navegação
Toda pasta de contexto tem um claude.md (e pode ter um AGENTS.md como este). Ao trabalhar
numa pasta, leia PRIMEIRO o arquivo de entrada dela; depois o documento_mestre.md e o
aprendizados_do_dia.md. Trate o claude.md de cada pasta como o arquivo de instruções do contexto.

## Skills instaladas
<!-- A instalação de skills pelo caminho ChatGPT/Codex adiciona referências aqui
     (arquivos em .meuos/skills/{slug}/SKILL.md). Não remova esta seção. -->
```

### `AGENTS.md` de cada CONTEXTO (substitua `{CONTEXTO}` pelo nome da pasta)

```markdown
# {CONTEXTO} — AGENTS.md
> Entrada do Codex/ChatGPT deste contexto (gerada pelo MeuOS).
> O [claude.md](claude.md) ao lado contém as regras — leia-o como se fosse este arquivo,
> junto do [documento_mestre.md](documento_mestre.md). Seu agente pode editar as entradas —
> mantenha as duas espelhadas; regras vivas preferem o documento_mestre.md.
```

> **Por que ponteiro e não cópia:** o `claude.md` de um OS que já viveu foi customizado por
> você e pelo seu agente. Copiar o conteúdo criaria duas fontes que divergem com o tempo.
> O ponteiro manda o Codex ler o `claude.md` como se fosse a entrada dele — zero duplicação.

## Passo 3 — Resultado (formato fixo)

```
OS PREPARADO PARA O CHATGPT
Criados: {n} arquivo(s)
{lista: AGENTS.md · Contexto/AGENTS.md · ...}
Já existiam (não tocados): {n}
```

Se algum arquivo falhar na criação, diga quais foram criados e quais faltaram — e que
rodar de novo continua de onde parou (os já criados são pulados).
