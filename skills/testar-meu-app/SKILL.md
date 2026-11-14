---
name: testar-meu-app
description: "Testa o seu app ou site pelo navegador como um usuário de verdade faria: monta com você a lista de cenários (caminho feliz e falhas), roda no celular e no computador, e devolve um relatório em linguagem simples com o que funcionou, o que quebrou, como reproduzir e o prompt de correção pronto para o Lovable ou o Claude Code. Nunca testa com dado real de cliente nem clica em pagar, excluir ou enviar em massa sem a sua confirmação. Usar quando o usuário disser 'testa meu app', 'vê se está funcionando', 'valida essa tela', 'testa o cadastro', 'confere se quebrou alguma coisa' ou 'faz um teste antes de eu publicar'."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Testar Meu App

## O que esta skill faz

Antes de mandar o link para o cliente, alguém precisa clicar em tudo como se fosse ele. Esta skill faz isso: abre o seu app no navegador, segue os caminhos que um usuário seguiria, tenta os erros que um usuário cometeria (campo vazio, dado esquisito, internet caindo no meio) e olha a tela no celular e no computador.

No fim você recebe um relatório simples, com 🟢 funcionou, 🟡 funciona com ressalva e 🔴 quebrou, o passo a passo para reproduzir cada problema e um prompt de correção pronto para colar na ferramenta em que você construiu o app.

> **Princípio:** clicar sem erro não prova nada. O teste só passa quando a tela mostra o resultado **certo** (o texto, o número, a página esperada).

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Travas de segurança (ler antes de tudo, valem o tempo todo)

| # | Trava | O que fazer |
|---|---|---|
| 1 | Nunca testar em produção com dado real de cliente | Usar ambiente de teste ou de pré-visualização. Se só existir produção, usar **conta de teste** criada para isso. Perguntar ao usuário qual endereço usar |
| 2 | Conta de teste, login feito pelo usuário | Pedir ao usuário que use uma conta de teste. **Nunca pedir e-mail nem senha no chat:** o agente abre o navegador na tela de login, o próprio usuário entra com a conta de teste e o agente espera ele dizer "loguei". Nunca usar a conta pessoal dele nem a de um cliente |
| 3 | Senha real nunca na conversa | Se o usuário colar uma senha real, avisar para trocá-la e pedir que ele mesmo faça o login na janela do navegador. No Claude Code, preferir que o usuário digite a senha direto no navegador aberto |
| 4 | Ações irreversíveis | **Nunca** clicar em pagar, comprar, excluir, cancelar assinatura, enviar e-mail/mensagem em massa ou publicar sem o usuário confirmar naquele momento, mesmo que esteja no roteiro |
| 5 | Pagamento | Só testar com o modo de teste do meio de pagamento (cartão de teste do próprio provedor). Se não houver modo de teste, parar antes de pagar e marcar como "não testado" |
| 6 | Dado pessoal no relatório | Relatório e capturas de tela não exibem dado real de pessoa. Se aparecer, recortar ou descrever sem o dado |
| 7 | Salvar pode disparar algo | Antes de qualquer cenário que SALVE algo (cadastro, agendamento, pedido), perguntar ao usuário se salvar dispara e-mail, mensagem, cobrança ou integração com outro sistema. Se o app estiver em produção ou houver dúvida: confirmar com o usuário a cada salvamento, naquele momento |

Se alguma trava impede o teste, dizer isso ao usuário e marcar o cenário como "não testado", nunca contornar.

### PASSO 1: Descobrir o ambiente e o contexto

1. Se o usuário tem OS organizado (pastas por contexto, documento mestre, `CLAUDE.md` ou `AGENTS.md`), confirmar de qual contexto é o app e ler o documento mestre e a spec dele (por exemplo `spec-*.md`, se existir). Os **critérios de aceite** da spec viram o gabarito do teste.
2. Descobrir qual ferramenta o agente tem para abrir o navegador:

| # | Ambiente | Como testar |
|---|---|---|
| 1 | Claude Code com Playwright MCP | O agente abre o navegador, clica, preenche e tira capturas de tela sozinho |
| 2 | Claude Code sem Playwright MCP | Oferecer a instalação (abaixo). Se o usuário não quiser, seguir no modo manual (linha 3) |
| 3 | ChatGPT, Codex sem Playwright ou qualquer agente sem navegador | Modo manual: o agente gera o roteiro numerado, o usuário executa e responde o que viu em cada passo |

**Instalação curta do Playwright MCP no Claude Code** (precisa do Node.js instalado):

```text
claude mcp add playwright npx @playwright/mcp@latest
```

No Codex (app ou CLI do ChatGPT), o equivalente é `codex mcp add playwright npx "@playwright/mcp@latest"`; com ele instalado, o Codex sai do modo manual e testa sozinho, como o Claude Code.

Depois, fechar e abrir o agente e conferir se o "playwright" aparece conectado (no Claude Code, pelo comando `/mcp`). Fonte oficial e outras formas de instalar: github.com/microsoft/playwright-mcp. Se der erro, seguir no modo manual e não insistir na instalação.

### PASSO 2: Montar a lista de cenários com o usuário

Propor a lista e pedir confirmação. Mínimo: **o caminho feliz de cada fluxo principal + pelo menos 2 falhas**.

| # | Tipo | Exemplo (agenda online de uma clínica fictícia) |
|---|---|---|
| 1 | Caminho feliz | Paciente de teste escolhe data, horário e confirma; vê a tela "Agendamento confirmado" com a data certa |
| 2 | Campo vazio | Clicar em "Confirmar" sem escolher horário: deve aparecer mensagem clara e nada ser salvo |
| 3 | Dado inesperado | Telefone com letras, e-mail sem "@", nome com 300 caracteres, data no passado, emoji no nome |
| 4 | Sem internet | No meio do fluxo, o usuário desliga o Wi-Fi (ou o agente usa o modo offline do navegador, quando disponível) e tenta salvar: deve aparecer aviso, e o que foi digitado não pode sumir |
| 5 | Permissão | Logado como paciente A, tentar abrir o agendamento do paciente B trocando o número no endereço: deve ser bloqueado |
| 6 | Voltar e repetir | Clicar em "Confirmar" duas vezes seguidas: não pode criar dois agendamentos |
| 7 | Sair e entrar | Sair da conta e tentar abrir uma página interna pelo endereço: deve pedir login |

Cada cenário precisa de um **resultado esperado** escrito antes de testar ("aparece a mensagem X", "a lista mostra 1 item"). Sem resultado esperado, o teste não tem como passar nem falhar.

Tamanhos de tela: **celular (375 px de largura)** e **computador (1440 px)**. Se o app for muito usado em tablet, incluir 768 px.

### PASSO 3: Executar

**Modo automático (Playwright MCP):**

1. Abrir o endereço de teste e esperar a página carregar por completo.
2. Para cada cenário, nos dois tamanhos de tela:
   - Seguir os passos como um usuário (clicar no que está visível, digitar nos campos).
   - Conferir o **resultado esperado** pelo conteúdo: o texto exato, o número, o endereço da página. "A página não deu erro" não é resultado.
   - Tirar captura de tela no ponto de verificação. Nome: `{tela}-{cenario}-{largura}.png` (ex.: `agendar-campo-vazio-375.png`), salvo em `tmp/` do contexto (ou na pasta atual).
   - Ler as mensagens de erro do console do navegador; erro vermelho no console entra no relatório como 🟡, mesmo se a tela parecer certa.
3. Esperar pela condição (elemento aparecer, endereço mudar), nunca por tempo fixo.
4. Antes de qualquer clique da trava 4 do PASSO 0, e de qualquer salvamento coberto pela trava 7: parar e perguntar.
5. Se um cenário falhar, tentar de novo **uma vez** para descartar instabilidade. Falhou duas vezes, é 🔴.

**Modo manual (ChatGPT ou sem navegador):**

Gerar um roteiro numerado, um cenário por vez, neste formato, e esperar a resposta do usuário antes do próximo:

```text
Cenário 2 de 7: campo vazio (no celular)
1. Abra {endereço} no celular, já logado com a conta de teste.
2. Toque em "Agendar".
3. Sem escolher horário, toque em "Confirmar".
O esperado: aparece a mensagem "Escolha um horário" perto do campo, e você continua na mesma tela.
Me responda: o que apareceu? (se puder, mande um print)
```

Com a resposta, o agente classifica 🟢/🟡/🔴. Nunca marcar 🟢 sem o usuário ter dito o que viu.

### PASSO 4: Checagem visual rápida (em cada tela testada)

| # | Item | Como reprovar |
|---|---|---|
| 1 | Rolagem horizontal no celular | A página "anda para o lado" em 375 px |
| 2 | Botões e links tocáveis | Menores que ~44 px de altura ou colados uns nos outros |
| 3 | Texto legível | Letra muito pequena, texto claro sobre fundo claro |
| 4 | Estados | Lista vazia sem mensagem, carregamento sem indicador, erro genérico ("Erro inesperado") |
| 5 | Campos | Campo sem rótulo visível, ou só com texto de exemplo que some ao digitar |
| 6 | Fim do fluxo | Ação concluída sem confirmação visível (termina em tela em branco) |

### PASSO 5: Relatório em linguagem simples

Salvar como `relatorio-teste-{app}-AAAA-MM-DD.md` na pasta do contexto (em `docs/` se existir) e mostrar o resumo no chat.

```markdown
# Teste: {app} · DD/MM/AAAA

**Endereço testado:** {ambiente de teste}  ·  **Conta:** de teste
**Modo:** automático (navegador) | manual (você executou)
**Resumo:** 🟢 {n} funcionaram · 🟡 {n} com ressalva · 🔴 {n} quebraram · ⚪ {n} não testados

## Resultado por cenário
| # | Cenário | Celular | Computador | O que aconteceu |
|---|---|---|---|---|
| 1 | Agendar (caminho feliz) | 🟢 | 🟢 | Confirmação com a data certa |
| 2 | Confirmar sem horário | 🔴 | 🔴 | Salvou um agendamento sem horário |

## O que quebrou e como reproduzir
### 🔴 2. Confirmar sem horário
1. Entrar com a conta de teste
2. Tocar em "Agendar" e depois em "Confirmar" sem escolher horário
**Esperado:** mensagem "Escolha um horário"
**Aconteceu:** agendamento salvo vazio na lista
**Evidência:** agendar-campo-vazio-375.png

## Prompt de correção (colar na ferramenta)
{bloco abaixo}

## Não testado e por quê
- Pagamento: sem modo de teste disponível (trava de segurança)
```

**Prompt de correção** (um por problema 🔴, ou um único agrupado se forem poucos):

```text
Encontrei um problema no teste. Corrija só isto, sem mudar mais nada:

Tela: {nome da tela}
Passos para reproduzir: {1, 2, 3}
O que acontece hoje: {comportamento}
O que deveria acontecer: {resultado esperado}
Em celular e computador: {sim/só um}

Depois de corrigir, me diga o que mudou e como eu confiro.
```

Para Claude Code ou Cursor, acrescentar: "Encontre a causa antes de mudar o código e mostre o trecho que causava o problema."

### PASSO 6: Novo teste depois da correção

Quando o usuário disser que corrigiu, rodar de novo **só os cenários que falharam** e mais o caminho feliz (para garantir que a correção não quebrou o principal). Limite de 3 rodadas de corrigir e testar no mesmo problema; na terceira falha, parar e sugerir revisar a spec ou a abordagem.

---

## Regras desta skill

- **Ambiente de teste e conta de teste, sempre.** Dado real de cliente fica fora do teste.
- **Ação irreversível só com confirmação na hora.** Pagar, excluir, enviar em massa e publicar nunca são automáticos.
- **Senha não entra na conversa.** O usuário faz o login de teste direto no navegador e avisa "loguei".
- **Salvar com cuidado.** Antes de salvar, saber se isso dispara e-mail, mensagem, cobrança ou integração; em produção ou na dúvida, confirmar cada salvamento.
- **Resultado esperado antes de testar.** E o teste confere o valor certo, não só a ausência de erro.
- **Pelo menos 2 falhas por fluxo.** Testar só o caminho feliz não é teste.
- **Celular e computador.** Uma tela que só funciona num deles está 🔴 no outro.
- **Relatório leigo.** Nada de jargão sem explicação; cada problema tem passos para reproduzir.
- **Não corrigir por conta própria.** A skill testa e entrega o prompt de correção; mudar o app é decisão do usuário.
- **Validação parcial se anuncia parcial.** O que não foi testado aparece como ⚪ com o motivo.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Travas do PASSO 0 respeitadas: ambiente de teste, conta de teste com login feito pelo usuário, nenhum e-mail ou senha pedido no chat
- [ ] Antes de cada cenário que salva, perguntado se salvar dispara e-mail, mensagem, cobrança ou integração (e confirmado a cada salvamento em produção ou na dúvida)
- [ ] Nenhum clique em pagar, excluir, enviar em massa ou publicar sem confirmação do usuário
- [ ] Lista de cenários combinada com o usuário, com resultado esperado em cada um
- [ ] Caminho feliz + pelo menos 2 falhas (vazio, inesperado, sem internet) por fluxo principal
- [ ] Testado em 375 px e 1440 px
- [ ] Cada 🟢 tem evidência (captura de tela ou relato do usuário)
- [ ] Cada 🔴 tem passos para reproduzir, esperado x aconteceu e prompt de correção
- [ ] Não testados listados como ⚪ com o motivo
- [ ] Relatório salvo com nome padronizado e caminho completo informado
- [ ] Nenhum dado pessoal real em relatório ou captura

Se algum item falhou: corrigir ANTES de declarar concluído. Nunca reportar "feito" com item pendente.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
