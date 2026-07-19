---
name: Importar dados do GPT
description: |
  Migra o CONHECIMENTO das suas conversas antigas do ChatGPT (e tambem Gemini e outros) para o
  seu OS no padrao MeuOS — destilando, nao despejando. Orienta a exportacao oficial dos dados
  (Settings → Data controls → Export), inventaria o zip exportado, faz a triagem das conversas
  por contexto do seu OS, e DESTILA o que importa (decisoes, fatos do negocio, processos,
  preferencias) em arquivos organizados por contexto — com sua aprovacao em cada etapa.
  E a skill de quem usava o GPT no navegador, fez o curso no Claude e quer TRAZER a historia
  pra ca (migrar), em vez de usar os dois agentes ao mesmo tempo (coexistir — isso e outra
  aula: o botao "Preparar meu OS para o ChatGPT").
  Nao-destrutiva: nunca copia conversas inteiras pro OS, nunca grava nada sem aprovacao, e o
  arquivo exportado fica FORA da pasta sincronizada do OS.
  Executa quando o usuario diz "importar dados do gpt", "importar do chatgpt", "migrar do gpt",
  "trazer meus dados do gpt", "importar minhas conversas", "migrar do chatgpt pro claude",
  "importar do gemini", "trazer historico do gpt".
version: 1.1
context: meuos
user-invocable: true
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Importar dados do GPT — Migrando seu histórico pro seu OS

## O que esta skill faz

Você usou o ChatGPT (ou Gemini) por meses no navegador: lá ficaram decisões, contexto do seu
negócio, preferências, processos. Agora você tem um OS no padrão MeuOS — e essa história não
pode se perder. Esta skill **traz o conhecimento** dessas conversas pro seu OS, organizado por
contexto.

**O princípio mais importante: destilar, não despejar.** Conversa crua não é conhecimento —
é matéria-prima. Se a gente copiasse suas 500 conversas pro OS, ele viraria um depósito
ilegível (e caro em tokens). O que a skill faz é **extrair o ouro**: decisões tomadas, fatos
do negócio, processos descritos, preferências suas — e gravar isso nos lugares certos do OS,
com a sua aprovação.

> **Migrar ≠ coexistir.** Esta skill é pra quem quer TRAZER os dados do GPT e seguir no Claude.
> Se o que você quer é usar Claude E ChatGPT ao mesmo tempo no mesmo OS, o caminho é outro
> (e mais simples): o botão **Tools → "Preparar meu OS para o ChatGPT"** no MeuOS.

---

## Quando usar

- Você usava o ChatGPT no navegador, fez o curso, montou seu OS no Claude, e quer trazer o histórico
- Você usava o Gemini (ou outra IA) e quer aproveitar o que ficou lá
- Quando o usuario diz "importar dados do gpt", "migrar do chatgpt", "trazer meu historico"

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0 — Confirmar a pasta do OS e a localização do export

1. Confirmar a **pasta do OS** (onde estão claude.md, soul.md e os contextos): mostrar o
   diretório atual e perguntar se é ali.
2. Perguntar **onde está o arquivo exportado** (o .zip do ChatGPT/Gemini, ou a pasta já
   descompactada). Se o usuário ainda não exportou, seguir pro PASSO 1.

**REGRA DE OURO DA LOCALIZAÇÃO**: o zip e os arquivos brutos ficam **FORA da pasta do OS**
(ex.: `Downloads/` ou uma pasta local `importacao-gpt/` fora do Drive). A pasta do OS
sincroniza com a nuvem — conversa bruta com potencial dado sensível NÃO sobe pro storage.

### PASSO 1 — Orientar a exportação (se ainda não foi feita)

**ChatGPT** (fluxo oficial, verificado em 19-JUL-2026):
1. Entre no ChatGPT → menu do perfil → `Settings` → `Data controls`.
2. Em `Export data`, clique `Export` → `Confirm export`.
3. A OpenAI envia **e-mail (ou SMS)** com o link `Download data export`.
   - Pode levar **até 7 dias** (contas pequenas costumam receber em minutos).
   - O link **expira em 24 horas** — baixe assim que chegar, logado na MESMA conta.
4. Salve o .zip fora da pasta do OS (ex.: `Downloads/`).

> ⚠️ **Avisos importantes**:
> - Export via Settings existe pra contas **Free, Plus e Pro** — **NÃO existe pra ChatGPT
>   Business/Enterprise** (conta da empresa). Nesse caso, o caminho é o Privacy Portal da
>   OpenAI (privacy.openai.com) ou falar com o admin do workspace.
> - Se o usuário usa a feature **Memory** do ChatGPT: pedir pra ele conferir se as memórias
>   vieram no export; se não vierem, copiar manualmente da tela
>   `Settings → Personalization → Memory → Manage` (colar aqui no chat).

**Gemini**: exportação via **Google Takeout** (takeout.google.com) — desmarcar tudo e marcar
só os dados do **Gemini** (o nome do produto na lista pode variar; procurar "Gemini").
Baixar o zip do e-mail do Takeout.

**Outros** (Copilot, DeepSeek, etc.): procurar "export data" / "exportar dados" nas
configurações de privacidade. O pipeline daqui pra frente é o mesmo: um arquivo com as
conversas → inventário → triagem → destilação.

### PASSO 2 — Inventário do export

1. Descompactar o zip (fora do OS) e **listar o que veio** — no ChatGPT normalmente:
   `conversations.json` (todo o histórico), `chat.html` (versão navegável), `user.json` e
   outros. Trabalhe com o que EXISTIR — não assuma nomes.
2. Medir: quantas conversas, de quando até quando, tamanho do arquivo.
3. **Arquivo grande** (centenas de conversas / dezenas de MB): NÃO ler inteiro de uma vez.
   Gerar primeiro um **índice enxuto** via script (título + data + tamanho de cada conversa)
   e trabalhar em lotes a partir dele.

### PASSO 3 — Triagem por contexto (o usuário decide o que importa)

1. Ler o **mapa de contextos** do OS (claude.md raiz).
2. A partir do índice de conversas, propor uma **tabela de triagem**:

```
| # | Conversa (título · data) | Contexto proposto | Importar? |
|---|--------------------------|-------------------|-----------|
| 1 | "Plano de marketing Q3" · mai/26 | Empresa X | sim |
| 2 | "Receita de bolo" · fev/26 | — (descartar) | não |
```

3. Regras da triagem:
   - Smalltalk, testes e curiosidades → **descartar** (propor "não" por padrão).
   - **Tema recorrente SEM contexto correspondente → propor ATIVAMENTE criar o contexto novo.**
     Se 3+ conversas orbitam o mesmo assunto (um cliente, um projeto, uma área da vida) e o OS
     não tem pasta pra ele, a proposta padrão é criar — com nome sugerido e os 6 arquivos
     canônicos (claude.md, AGENTS.md, documento_mestre.md, aprendizados_do_dia.md,
     changelog.md, index.md), usando os templates oficiais da skill meuos-do-zero. Incluir a
     sugestão na própria tabela de triagem: `Contexto proposto: "Cliente Y" (NOVO)`.
   - Conversa avulsa que não casa com nada e não justifica contexto → satélite geral ou descarte.
   - O usuário pode aprovar a tabela em bloco ou ajustar linha a linha. **Nada segue sem OK**
     — inclusive a criação de contextos novos.

### PASSO 4 — Destilação (o coração da skill)

Para cada contexto com conversas aprovadas, ler as conversas **em lotes** e extrair SOMENTE:

- **Fatos e decisões**: o que ficou definido, números, nomes, datas que importam
- **Processos**: passo a passo que o usuário construiu nas conversas
- **Preferências e regras pessoais**: "sempre me responda assim", formatos preferidos
- **Pendências vivas**: o que ficou em aberto e ainda é relevante

Gravar num satélite por contexto: **`importado_do_gpt.md`** dentro da pasta do contexto,
com este formato:

```
# Importado do GPT — {Contexto}
> Destilado do histórico do ChatGPT em {DATA} pela skill Importar dados do GPT.
> Fonte: {N} conversas ({período}). O arquivo bruto NÃO está no OS.

## Fatos e decisões
- ...
## Processos
- ...
## Preferências detectadas
- ...
## Pendências que ainda valem
- ...
## Fontes (título · data)
- ...
```

Regras da destilação:
- **NUNCA copiar conversas inteiras** — só o destilado.
- **Dados sensíveis achados nas conversas (senhas, API keys, tokens, CPF) NUNCA entram em
  .md** — alertar o usuário e deixar de fora.
- Preferências que são REGRA de comportamento → propor promover pro `soul.md` (tom) ou pro
  `documento_mestre.md` do contexto — com aprovação, nunca direto.
- Memórias do ChatGPT (se vieram) → tratar como preferências: destilar e propor destino.

### PASSO 5 — Plano, aprovação e gravação

1. Apresentar o **plano numerado**: quais contextos NOVOS serão criados (com os 6 arquivos
   canônicos), quais `importado_do_gpt.md` serão criados, o que será proposto pro soul/mestre,
   o que foi descartado.
2. Com aprovação: gravar os arquivos, **adicionar ponteiro no `index.md`** de cada contexto
   (e no MESTRE quando relevante) e registrar no `changelog.md`:
   `[DATA] Importação do histórico do GPT — {N} conversas destiladas em {contextos}`.

### PASSO 6 — Pós-importação (higiene)

1. Sugerir **apagar ou arquivar o zip** e a pasta descompactada (dados brutos sensíveis não
   precisam mais existir) — decisão do usuário, nunca apagar sozinho.
2. Lembrar: os satélites `importado_do_gpt.md` entram na manutenção normal do OS — a skill
   `otimizar-os` vai revisá-los junto com o resto (promover o que virou permanente, arquivar
   o que envelhecer).
3. Se o usuário pretende PARAR de usar o GPT: lembrar de cancelar a assinatura e, se quiser,
   apagar as conversas/conta lá — o conhecimento agora vive no OS dele.

---

## Regras de seguranca

- **O arquivo bruto NUNCA entra na pasta do OS** (não sobe pro storage sincronizado)
- **Nunca copiar conversas inteiras** — só conhecimento destilado
- **Dados sensíveis (senha, API key, token, documento) NUNCA entram em .md** — alertar e excluir
- **Nada é gravado sem aprovação** — triagem e plano sempre antes
- **Nunca apagar o export sozinho** — sugerir, o usuário decide
- **Nunca inventar contexto** — na dúvida sobre onde algo se encaixa, perguntar

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
