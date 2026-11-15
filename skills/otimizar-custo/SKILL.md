---
name: otimizar-custo
description: |
  Deixa as suas sessoes com Claude Code mais leves higienizando a memoria do agente.
  O MEMORY.md e carregado em toda conversa — cada linha ocupa espaco de contexto. Uma memoria
  de 263 linhas pode virar 95 (64% mais leve) depois da higiene. Escaneia o MEMORY.md e os
  arquivos de topico, classifica entradas em manter, arquivar, levar para o OS ou credencial,
  alerta se o claude.md tambem esta pesado (ele tambem entra em toda sessao) e propoe UM plano
  numerado — sempre com aprovacao antes de executar. O resultado sai em leve/pesado, com
  previsao de tokens; nunca em dinheiro.
  ESPECIFICA DO CLAUDE CODE: o mecanismo otimizado (MEMORY.md cobrado em toda mensagem) so
  existe la — rodando no ChatGPT/Codex, a skill explica isso e se encerra sem mexer em nada,
  apontando a otimizar-os para a higiene dos arquivos do OS (que vale nos dois agentes).
  Executa quando o usuario diz "otimizar custo", "reduzir custo", "economizar tokens",
  "otimizar memoria", "limpar memoria", "higienizar memoria", "memoria do claude",
  "revisar memoria", "auditar memoria".
context: meuos
user-invocable: true
argument-hint: "(sem argumentos — roda na pasta do seu Claude Code atual)"
version: 2.8
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Otimizar Custo — Reduzir o Custo de Tokens das Sessoes

## O que esta skill faz

Seu agente de IA (Claude Code) guarda uma "memoria" das suas preferencias, contexto e
decisoes — ela vive numa pasta especial do seu computador. Com o tempo essa memoria
cresce e fica com coisas velhas, duplicadas ou que deveriam estar no seu OS, e nao na
memoria do agente. Isso aumenta o custo por conversa (mais tokens carregados) e deixa
o agente mais lento ou confuso. Esta skill foca em **reduzir esse custo** higienizando
a memoria + alertando quando o CLAUDE.md tambem esta crescendo demais.

Esta skill escaneia essa memoria, mostra o que pode ser limpo e executa a higiene
com sua aprovacao. Em memoria com muita coisa antiga, a reducao costuma passar de 60%; em memoria feita quase so de preferencias em uso, o ganho e pequeno e a skill diz isso.

> **Importante:** Esta skill so faz sentido se voce usa **Claude Code**. Se voce usa
> Cursor, Claude CoWork ou outra ferramenta, a "memoria" dela fica em outro lugar
> e funciona diferente — esta skill nao se aplica.

---

## Por que isso deixa a sessao mais leve

Cada conversa com o Claude Code carrega o conteudo do arquivo `MEMORY.md` como
contexto inicial. Se ele tem 300 linhas, essas 300 linhas ocupam espaco **em toda
mensagem**: sobra menos contexto para o trabalho e o limite do seu plano chega mais
cedo. Mantendo enxuto (🟢 leve pela tabela do guia), toda sessao fica mais leve.

Exemplo: um `MEMORY.md` de 263 linhas vira ~95 linhas apos a higiene — **64% mais leve**.

---

## 🖥️ COMO FALAR COM O USUARIO (padrao visual, vale para a execucao inteira)

1. **Duas etapas, cada uma com cabecalho de 1 linha:** `**Otimizar custo · memoria do agente · etapa 1 de 2**`.
2. **Uma frase de resumo em negrito ANTES da tabela**, com o peso e a barra: `**A memoria do seu agente esta pesada: 🔴 ▰▰▰▰▰▰▰▰▰▰ 263 linhas de 150.**` A barra tem 10 blocos e mede o tamanho contra o limite de "pesado" do guia (os numeros dos exemplos desta skill sao ilustrativos; o limite vem sempre do guia).
3. **UMA tabela numerada** para aprovar: `# | O que faco | O que muda para voce`. Sem nome de arquivo nem numero de linha na tabela (mostrar se o usuario pedir).
4. **UMA aprovacao:** se o agente tiver caixa de opcoes clicaveis (no Claude Code, a ferramenta de pergunta ao usuario), abrir com "Aprovar tudo", "Escolher itens", "Nao mexer em nada". Em "Escolher itens", ou sem a caixa, o usuario responde "tudo" ou os numeros. **A caixa precisa se bastar:** quando ela abre, o usuario pode nao ver o texto que veio antes. Por isso os itens vao DENTRO da caixa: o texto da pergunta lista os itens numerados, 1 linha cada (ex.: `1. Proposta revisada → changelog`), ou a opcao "Aprovar tudo" traz a tabela inteira na previa. Nunca perguntar "quais itens eu gravo?" sem mostrar os itens na propria caixa. Mais de 8 itens: NAO abrir a caixa; mostrar a tabela na mensagem e pedir a resposta por texto ("tudo" ou os numeros).
5. **Leve, atencao e pesado** (🟢 🟡 🔴). Tokens so como previsao. **Nunca valor em dinheiro** (nem R$, nem US$).
6. **So os termos do treinamento:** documento mestre, satelite, aprendizados, changelog, index, ponteiro, contexto, memoria do agente. Nao usar com o usuario: auto-memory, custo fixo, encoded, frontmatter.
7. **Fecho fixo:** cartao de 4 linhas: Feito, Peso, Previsao, Proxima (PASSO 5).

## 📏 ONDE ESTAO OS LIMITES DE TAMANHO

Os limites da memoria (`MEMORY.md`, numero de arquivos de topico) e do `claude.md` moram em UM lugar: a secao **"Limites de tamanho"** do `guia_do_os.md` da raiz do OS. Ler a tabela de la ao iniciar. Guia sem essa secao (anterior a versao 4): avisar em 1 linha, sugerir a skill `otimizar-os` (ela atualiza o guia) e, nesta execucao, ler a tabela direto do catalogo (so leitura): `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/meuos-do-zero/templates/guia_do_os.md`. Os limites de IDADE (60 e 90 dias) sao desta skill e estao no PASSO 1.

---

## Quando usar

- Quando o **Otimizar OS** sugerir ao concluir uma execucao — e o canal unico do lembrete
  (no maximo 1x por mes). O Fim do Dia (`fim-do-dia`) apenas observa, nao sugere esta skill.
- Cadencia: lembrete no maximo 1 vez por mes → o PASSO 1.5 decide se ha mesmo trabalho;
  memoria 🟢 leve → a skill encerra sem mexer em nada
- Quando sentir que o Claude Code esta lento ou confuso com coisas antigas
- Quando o usuario disser "otimizar memoria", "limpar memoria do claude", "auditar memoria"

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO -1 — Em qual agente estou? (guard dual-agent)

Esta skill otimiza a **memoria persistente do Claude Code** (`MEMORY.md` + arquivos de topico em
`~/.claude/projects/.../memory/`) — um mecanismo que **so existe no Claude Code**.

- Rodando no **Claude Code** → siga para o PASSO 0.
- Rodando no **ChatGPT/Codex** (ou outro agente) → explique e encerre, sem mexer em nada:

> `"Esta skill higieniza a memoria especifica do Claude Code (MEMORY.md, carregada em toda mensagem
> de la). Aqui no Codex esse mecanismo nao existe — entao nao ha custo desse tipo pra otimizar.
> Se o objetivo e enxugar os ARQUIVOS do seu OS (documento_mestre, aprendizados, claude.md gordos),
> a skill certa e a 'otimizar OS' — ela funciona igual nos dois agentes. Quer que eu rode ela?"`

### PASSO 0 — Confirmar o working directory

Antes de escanear, identificar o diretorio atual. Ele e o do OS aberto na sessao → seguir sem perguntar
(a aprovacao unica e a do plano). SO perguntar se houver duvida real de qual pasta e (ex.: a sessao
foi aberta fora da pasta do OS):

> `"A sessao esta aberta em [pasta]. E a memoria desta pasta que voce quer enxugar?"`

A memoria vive em `~/.claude/projects/{working-dir-encoded}/memory/`, onde
`{working-dir-encoded}` e o caminho do diretorio atual com `/` e `\` trocados
por `-` e `:` removido. Exemplo:
- Diretorio: `C:\Users\fulano\MeuOs`
- Encoded: `C--Users-fulano-MeuOs`
- Path final: `~/.claude/projects/C--Users-fulano-MeuOs/memory/`

Se a pasta `memory/` nao existir: avisar o usuario que **ainda nao ha memoria
para higienizar** nesse diretorio (pode ser que nunca usou Claude Code aqui,
ou e uma pasta nova). Encerrar.

---

### PASSO 1 — Escanear a memoria

Listar `MEMORY.md` + todos os arquivos `.md` na pasta `memory/`.

Para cada arquivo coletar:
- Nome do arquivo
- Numero de linhas
- Tamanho em KB
- Data da ultima modificacao

Este levantamento e do agente (nao mostrar a lista de arquivos ao usuario; ele ve so a frase de
resumo e a tabela do plano). Classificar:

- **Tamanho** do `MEMORY.md` (linhas E KB) e **numero de arquivos de topico**: 🟢 🟡 🔴 pela tabela
  "Limites de tamanho" do guia.
- **Idade** de cada arquivo de topico (regra desta skill; usar a data mais recente entre a do arquivo e a que o proprio topico declara no cabecalho, se houver): 🟢 menos de 60 dias sem modificar ·
  🟡 60 a 90 dias · 🔴 mais de 90 dias.
- **Arquivo de topico bem maior que os outros**: merece olhar (provavel conteudo que pertence ao OS).

> **Medir os DOIS (linhas E chars).** Uma memoria de poucas linhas em que cada linha virou paragrafo passa no teste de linhas e nao passa no de KB — pesa do mesmo jeito. O que ocupa contexto e o texto (4 caracteres ≈ 1 token), nao a linha.

### Verificacao extra: CLAUDE.md tambem entra no custo

Alem do MEMORY.md, **o CLAUDE.md raiz do seu OS e o CLAUDE.md do contexto ativo** tambem sao carregados em toda mensagem (project instructions). Se eles estiverem grandes, somam tokens em toda sessao.

Verificar pela tabela do guia e **alertar** (sem atuar — so apontar). Se algum estiver 🟡 ou 🔴,
incluir 1 linha no fecho:
> `"O claude.md [da raiz / do contexto X] esta 🟡 em atencao — ele tambem entra em toda sessao. Vale rodar o Otimizar OS depois."`

**So alertar — nao enxugar o claude.md aqui.** Esta skill cuida da memoria do agente; enxugar o claude.md e da skill `otimizar-os`. A unica escrita possivel nele e a excecao do PASSO 4b (regra rigida de operacao), como item aprovado do plano.

---

### PASSO 1.5 — Ha mesmo o que otimizar? (rodar ANTES de classificar; repetir a pergunta ao fim do PASSO 2)

**Antes de propor qualquer plano**, verificar se o estado atual realmente justifica higiene:

| Sinal | O que fazer |
|---|---|
| MEMORY.md 🟢 leve (pela tabela do guia) + zero arquivos >90d sem mod + zero duplicatas | **Avisar que nao ha higiene a fazer** e encerrar (sem propor plano vazio) |
| Ultima execucao foi ha menos de 30 dias (linha `ULTIMA_EXECUCAO=` do arquivo `.last-otimizar-custo` da raiz do OS; arquivo antigo com so uma data solta: essa data e a `ULTIMA_EXECUCAO`; na falta das duas, o cabecalho do `MEMORY.md`) E a memoria nao esta 🔴 pesada | Avisar que ainda e cedo (rodar de novo so forca compactacao artificial). A linha `LAST_SUGGESTED=` do mesmo arquivo e so o registro do lembrete: NAO conta como execucao |

**Mensagem padrao quando nao ha nada a otimizar:**

> `"A memoria do seu agente ja esta 🟢 leve: X linhas, Y anotacoes, nenhuma parada ha mais de 90 dias e nada repetido. Nao ha o que enxugar agora. Rodar com frequencia demais tira contexto que o agente precisa. O Otimizar OS lembra de novo daqui a um mes."`

Mesmo sem nada a fazer, gravar `ULTIMA_EXECUCAO=<hoje>` no `.last-otimizar-custo` da raiz do OS (PASSO 5, item final), para o lembrete mensal nao voltar.

**REGRA: nunca forcar plano de higiene quando nao ha ganho real.** Higiene excessiva remove conteudo util — o oposto do que a skill pretende.

---

### PASSO 2 — Classificar cada entrada

Para cada arquivo (e para as linhas do `MEMORY.md` que apontam para topicos),
classificar em 4 categorias:

| Categoria | Criterio | O que fazer |
|-----------|----------|-------------|
| **Manter** | Preferencia pessoal ativa, regra de estilo, convencao do agente. **Todo topico que o `MEMORY.md` (ou um sub-indice ligado a ele) cita como regra em uso e Manter, qualquer que seja a idade** | Deixar como esta |
| **Arquivar** | Mais de 90 dias sem modificacao E nao citado como regra em uso; conteudo sobre projeto/decisao que ja passou | Mover para `memory/historico/` e ajustar o ponteiro no indice (ou sub-indice) que o citava |
| **Promover** | Informacao que deveria estar no seu OS (regra de negocio, decisao de produto, stack ativa) | Copiar para o OS — destino padrao e o SATELITE do tema — e remover daqui |
| **Credencial** | Senha, token, chave de API, CPF ou qualquer segredo | NUNCA copiar para o OS (ele sincroniza na nuvem e entra em todo backup) e NUNCA arquivar (a copia arquivada continuaria com o segredo). A linha do plano propoe **apagar so o segredo de dentro da anotacao**, trocando-o por "guardado no gerenciador de senhas", e manter o resto do texto. E a unica coisa que esta skill apaga, e so com a aprovacao do plano |

**Como identificar:**

**Manter:** "Prefiro respostas curtas", "NUNCA usar DALL-E", "Sempre
perguntar o contexto antes". Sao preferencias pessoais ou de estilo — fazem
sentido so aqui.

**Arquivar:** Menciona projeto concluido, bug corrigido, decisao ja implementada,
ou simplesmente nao foi tocada em 90+ dias.

**Promover:** Regra de negocio do seu cliente/produto, configuracao de stack
(URL de API, modelo usado), decisao estrategica — tudo isso cabe
melhor no seu OS, no SATELITE do tema (`CONTEXTO_tema.md`), que o agente abre so
quando o assunto surge. MESTRE so para decisao vigente que vale em TODA sessao;
`claude.md` so para regra rigida de operacao; aprendizados NUNCA (e caixa de
entrada — promover para la e adiar a arrumacao). Outros agentes que voce usar
no futuro tambem vao precisar dessa info.

**Credencial:** senha, token, chave de API, CPF. Nunca vai para o OS nem para o
plano em texto: a linha do plano diz so quantas anotacoes tem senha (o nome do arquivo e mostrado se o
usuario pedir, nunca o valor). **Segredo e o que da acesso**: senha, token, chave. Telefone, numero de
identificacao de sistema e documento ficticio de teste nao sao segredo e ficam como estao.

---

**Fim do PASSO 2:** classificou tudo e nao sobrou nada a arquivar, levar para o OS, encurtar ou repetido → avisar que a memoria esta saudavel e encerrar (sem tabela vazia).

---

### PASSO 3 — Plano de acao (sempre mostrar antes de executar)

Apresentar no padrao visual: frase de resumo com o peso + UMA tabela numerada. Juntar itens
parecidos numa linha so (ex.: os 2 arquivos a arquivar viram 1 linha). O que fica como esta
nao entra na tabela.

```
**Otimizar custo · memoria do agente · etapa 1 de 2**

**A memoria do seu agente esta pesada: 🔴 ▰▰▰▰▰▰▰▰▰▰ 263 linhas de 150.**

| # | O que faco | O que muda para voce |
|---|---|---|
| 1 | Guardar 2 anotacoes de projetos encerrados | Saem da memoria do dia a dia; ficam arquivadas |
| 2 | Levar "configuracao do sistema" para o seu OS, no satelite do tema | Passa a valer para qualquer agente, nao so este |
| 3 | Tirar 2 linhas repetidas | Nada; a informacao ja esta no seu OS |
| 4 | Apagar a senha de dentro de 1 anotacao (o resto do texto fica) | Guarde a senha num gerenciador de senhas ANTES de aprovar; ela nao vai para o OS |

Depois do plano: 🟢 cerca de 95 linhas (64% mais leve).
```

Aprovacao unica: caixa de opcoes ("Aprovar tudo", "Escolher itens", "Nao mexer em nada") ou, sem
a caixa, `Responda "tudo" ou os numeros que valem.`

**NUNCA executar sem resposta do usuario.** Aceitar respostas como "tudo",
"so 1 e 3", "nao quero levar nada para o OS, so arquivar".

---

### PASSO 4 — Execucao (somente com aprovacao)

Para cada acao aprovada:

**4a. Arquivar arquivo velho**
1. Criar pasta `memory/historico/` se nao existir
2. Mover o arquivo para la
3. Remover a linha correspondente no `MEMORY.md` (se apontava para ele)

**4b. Promover para o OS**
1. Ler o arquivo de topico original
2. Usar o destino que ja foi mostrado na linha do plano (ele e decidido ANTES, ao montar o plano; se nao era obvio, a linha propos um destino e o usuario ajustou na aprovacao — nao perguntar de novo na execucao). Como escolher o destino:
   - Procurar no `index.md` do contexto um satelite do tema: existe → entra nele (a regra em 1 linha em "Regras
     vigentes"; o corpo do topico, sem reescrever, em "Historico" com a data; satelite existente mantem o nome e
     ganha o modelo ao ser tocado — frontmatter com `abrir_quando` + Regras vigentes no topo — sem reorganizar o
     resto; ganha a linha na secao "Satelites deste contexto" do documento mestre so se ela tiver menos de 15 linhas — regra do guia; senao, so no index); nao existe → satelite novo pelo modelo
     `satelite.md` (frontmatter `updated/context/type: satelite/status: vivo/abrir_quando` · `> Documento pai:` ·
     `## Regras vigentes` · `## Detalhe` · `## Historico`), nome `CONTEXTO_tema.md` (prefixo em maiusculas, tema em
     minusculas; ex: `CLIENTEA_honorario.md`), mesmo que os satelites vizinhos usem outro padrao de nome, + linha
     unica no `*MESTRE.md` (secao "Satelites deste contexto", criada no primeiro ponteiro) e no `index.md`:
     `- [CONTEXTO_tema.md](CONTEXTO_tema.md) — abrir quando: tema A, tema B` (o trecho depois de "abrir quando:"
     tem ate 80 caracteres)
   - Excecoes: decisao vigente que vale em TODA sessao → `*MESTRE.md` · regra rigida de operacao → `claude.md`
   - Nunca `aprendizados_do_dia.md`
3. Copiar o conteudo para o destino SEM reescrever (adaptar so o formato); conferir item a item — regra,
   numero, data, nome, link — e mostrar a lista
4. Adicionar uma nota no destino: "Promovido da memoria em DD/MM pelo usuario"
5. So entao mover o arquivo original para `memory/historico/` (nada e apagado)
6. Remover a linha correspondente no `MEMORY.md`

**4c. Limpar e enxugar o MEMORY.md**
1. Ler o `MEMORY.md` inteiro antes de alterar (nao perder nada)
2. Remover as linhas aprovadas, mantendo a estrutura do indice
3. **Encurtar linha longa do indice — so se for item aprovado do plano** ("Encurtar N linhas do indice"). Vale para linha com mais de ~150 caracteres que APONTA para um arquivo de topico: antes de cortar, conferir no topico que o trecho a sair esta la (se nao estiver, copiar para o topico primeiro, sem reescrever). Linha longa SEM topico proprio nao e encurtada: o texto so existe ali. Regra em uso nunca perde conteudo.
4. **Fundir arquivos de topico irmaos** sobre o mesmo assunto, quando for item aprovado do plano: o mais completo fica, o conteudo do outro entra nele sem reescrever, o outro vai para `memory/historico/` e os ponteiros passam a apontar para o que ficou.
5. Atualizar o cabecalho: "> Ultima otimizacao: DD/MM (skill Otimizar Custo)" (e registro da execucao, nao precisa de linha no plano)
6. Salvar

**4d. Credencial (so se for item aprovado do plano)**
Apagar SO o segredo de dentro da anotacao e por no lugar `(removido da memoria em DD/MM)`. O resto do texto fica. Nao criar copia do segredo em lugar nenhum.

**Nada e salvo fora do que foi aprovado na tabela do plano.** O antes/depois de um item e mostrado
quando o usuario pedir ou escolher item a item; nao pedir nova confirmacao durante a execucao.

---

### PASSO 5 — Fecho (leve/pesado e previsao de tokens; nunca em dinheiro)

**Previsao de tokens (unico calculo):** `caracteres reduzidos ÷ 4` = tokens a menos por mensagem
(medir pelo tamanho do texto; contar linhas engana quando a linha e longa). Contar SO o `MEMORY.md`, que e o que carrega em toda mensagem; linha nova criada no documento mestre entra na conta como acrescimo. E previsao, dizer "cerca de". **Nao converter em R$, US$ nem em
economia por mes:** depende do plano e do uso de cada pessoa, e quem tem plano mensal nao paga
por token.

**Cartao fixo:**

```
**Otimizar custo · memoria do agente · etapa 2 de 2**

**Feito**     4 de 4 itens · nada apagado alem da senha aprovada; o resto foi arquivado
**Peso**      🔴 → 🟢 · memoria 64% mais leve (de 263 para 94 linhas)
**Previsao**  cerca de 2.500 tokens a menos por mensagem
**Proxima**   quando o Otimizar OS lembrar (no maximo 1 vez por mes)
```

Se o `claude.md` da raiz ou do contexto estiver 🟡 ou 🔴, acrescentar a linha de alerta do PASSO 1.
Algo foi levado para um arquivo que tambem carrega em toda sessao (documento mestre ou `claude.md`)?
Dizer na linha "Peso": "X linhas so mudaram de lugar, nao contam como reducao".

**Gravar a trava do lembrete mensal:** no arquivo `.last-otimizar-custo` da raiz do OS (criar se nao
existir), gravar ou atualizar a linha `ULTIMA_EXECUCAO=AAAA-MM-DD` com a data de hoje (arquivo antigo com so uma data solta: substituir essa data pela linha `ULTIMA_EXECUCAO=`), sem apagar a
linha `LAST_SUGGESTED=` (ela e do `otimizar-os`). E esse arquivo que o `otimizar-os` le para so
lembrar desta skill 1 vez por mes. Rodar de novo antes disso so faz sentido se a memoria cresceu de
repente; caso contrario, tira contexto que o agente precisa.

Se houver arquivos ou linhas nao aprovados nesta rodada, listar como pendencia:
> `"Ficaram X itens que voce preferiu nao mexer agora. Posso revisar numa proxima vez."`

---

## Regras de seguranca

- **Sempre conferir o diretorio** antes de escanear, e perguntar se houver duvida — evita mexer na memoria errada
- **Nunca executar sem aprovacao explicita** — plano primeiro, acao depois
- **Nunca deletar arquivo sem arquivar antes** (arquivar em `memory/historico/`, nao apagar definitivo)
- **Nunca promover para o OS sem identificar o destino exato** — o destino aparece na linha do plano; na duvida, a linha propoe um e o usuario ajusta na aprovacao
- **Nunca modificar arquivos do OS** sem deixar uma nota de onde veio (rastreabilidade)
- **Nunca rodar em loop** — uma execucao por chamada
- **Se a pasta memory/ nao existir**, nao cria — apenas informa que nao ha o que higienizar
- **Nao auto-dispara** — o usuario precisa pedir explicitamente

---

## Formato de saida

**`MEMORY.md`** — apos a higiene:
- Cabecalho atualizado com data da otimizacao
- Indice limpo, com links apenas para arquivos de topico que existem
- Sem linhas duplicadas ou apontando para arquivos removidos

**Arquivos em `memory/historico/`** — preservados, so movidos de lugar

**Destinos no OS (quando houve promocao)** — cada entrada promovida carrega
uma nota curta indicando a origem: "Promovido da memoria em DD/MM"

---

## Integracao com outras skills (cadeia: fim-do-dia → otimizar-os → esta skill)

- **Fim do Dia (`fim-do-dia`)** — diaria: captura com gate de escrita e higiene leve; apenas
  OBSERVA a memoria (1 linha se estiver pesada), NAO sugere esta skill
- **Otimizar OS** — semanal sob volume: organiza os arquivos do OS; ao concluir, e quem lembra
  desta skill (no maximo 1x por mes)
- **Esta skill (`otimizar-custo`)** — no maximo 1 vez por mes, sob lembrete: exclusivamente
  a memoria do Claude Code

As tres juntas cobrem: encerramento do dia, organizacao dos docs do OS e higiene
da memoria do agente. Rodar cada uma no momento certo mantem seu sistema enxuto
e barato de operar.

---

## Casos de borda (regras que valem sobre os passos acima)

1. **Sub-indices.** Se o `MEMORY.md` aponta para outros indices (ex.: `INDICE-*.md`), eles fazem parte do indice, e ao arquivar um topico o ponteiro e ajustado onde ele estiver (apontando para `historico/`, com a data).
2. **"Regra em uso" (categoria Manter)** = topico citado no `MEMORY.md` ou num sub-indice de leitura obrigatoria. Aparecer so num catalogo geral que lista tudo NAO torna o topico "em uso". Topico que e regra em uso E regra de negocio: Manter vence.
3. **A barra da frase de resumo mede o PIOR** entre linhas e KB (ex.: `17 KB de 10`), com o outro numero entre parenteses. O numero de anotacoes vai na linha abaixo da tabela.
4. **O plano nao alcanca 🟢.** Se, mesmo com tudo aprovado, a memoria continuar 🟡 ou 🔴, dizer isso abaixo da tabela, com o motivo (ex.: "quase tudo que sobra e preferencia sua em uso"). Nunca forcar corte de regra em uso para bater o alvo.
5. **Destino no OS.** Satelite novo DENTRO de um contexto que existe na pasta do OS: pode nascer (PASSO 4b). Contexto que nao existe na pasta, ou satelite que o index lista mas nao esta no disco: nao criar; o topico fica na memoria e entra em "nao feito". Na tabela, o destino e descrito em palavras (contexto e tema); o nome do arquivo aparece no fecho.
6. **Satelite novo:** modelo em `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/meuos-do-zero/templates/satelite.md` (so leitura). O prefixo do nome e o mesmo que os satelites vizinhos e o documento mestre do contexto usam. O corpo do topico vai inteiro em "Historico"; em "Regras vigentes" entram so as frases de regra que ja existem no texto.
7. **Conferencia item a item** do que foi para o OS: mostrar em ate 5 linhas, logo antes do cartao de fecho.
8. **Levou algo para o OS:** 1 linha no changelog do contexto ("trazido da memoria do agente: X, para o satelite Y"), se o contexto tiver changelog.
9. **Item feito em parte ou aprovado e nao executado:** o cartao diz "N de M itens" e lista o que ficou; nao escrever "voce preferiu nao mexer" quando o motivo foi outro.
10. **Idade em pasta copiada, sincronizada ou restaurada** (todos os arquivos com a data de hoje): usar a data que o topico declara; topico sem data declarada conta como recente (Manter).

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)

## Regra dual-agent (obrigatória)
Esta skill é EXCLUSIVA do Claude Code (depende do `MEMORY.md`, que não existe no ChatGPT/Codex) — se o agente atual não for Claude Code, avise e pare. Exceção espelhável: se a skill gravar regra rígida no `claude.md` do OS (PASSO 4b), **espelhe a mesma mudança no `AGENTS.md` da mesma pasta** (se existir).

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] MEMORY.md + arquivos de topico escaneados e cada entrada classificada (Manter / Arquivar / Promover / Credencial)
- [ ] Plano apresentado e SO o aprovado foi aplicado
- [ ] O que pertence ao OS foi MOVIDO pro contexto certo, nao apagado — destino padrao foi o satelite do tema; MESTRE/claude.md so com o teste "vale em TODA sessao?"
- [ ] Conferencia item a item mostrada ANTES de mover o topico para `memory/historico/`
- [ ] Nada removido sem registro do que saiu
- [ ] O "ha o que otimizar?" (PASSO 1.5) rodou ANTES de montar o plano
- [ ] Usuario viu UMA tabela numerada e deu UMA aprovacao; nada de nome de arquivo ou numero de linha na tabela
- [ ] Nada foi levado para o `aprendizados_do_dia.md`
- [ ] Fecho no cartao fixo (Feito, Peso, Previsao, Proxima), em leve/pesado e previsao de tokens — nenhum valor em dinheiro
- [ ] `ULTIMA_EXECUCAO=` com a data de hoje no `.last-otimizar-custo` da raiz do OS (linha `LAST_SUGGESTED=` preservada)

Se algum item falhou: corrigir ANTES de declarar concluido. Nunca reportar "feito" com item pendente.
