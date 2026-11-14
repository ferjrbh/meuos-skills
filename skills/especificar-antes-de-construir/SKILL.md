---
name: especificar-antes-de-construir
description: "Transforma uma ideia de app, tela ou automação numa especificação completa ANTES de construir no Lovable, Claude Code, Cursor, Bolt, n8n ou similar. Faz uma entrevista guiada, classifica o porte, compara 2-3 caminhos e recomenda o mais simples, escreve a spec num arquivo .md com critérios de aceite testáveis e um prompt pronto para colar na ferramenta, e passa a spec por dois críticos independentes (segurança e experiência do usuário) antes da entrega. Usar quando o usuário disser 'quero construir um app', 'vamos especificar antes de construir', 'monta a spec disso', 'transforma essa ideia em especificação', 'antes de ir pro Lovable', 'escreve o PRD' ou 'planeja essa automação'."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Especificar Antes de Construir

## O que esta skill faz

A maior parte do retrabalho em app feito com IA não vem de código errado: vem de pedido vago. Você pede "um app de agendamento", a ferramenta inventa vinte decisões por você, e metade delas está errada. Esta skill faz o trabalho de um gerente de produto antes da primeira linha de código:

1. Entrevista você até a ideia ficar clara (problema, quem usa, o que entra e o que sai, dados, telas, integrações e, principalmente, o que **não** entra).
2. Classifica o porte do projeto em linguagem simples e ajusta o tamanho do processo a ele.
3. Compara 2 ou 3 caminhos e recomenda o mais simples que resolve.
4. Escreve a especificação completa num arquivo `.md`, com critérios de aceite que dá para testar.
5. Gera o prompt pronto para colar no Lovable, Claude Code, Cursor ou n8n.
6. Passa a spec por **dois críticos independentes**, um de segurança e outro de experiência do usuário, que não viram a conversa. Os achados voltam numa tabela e a spec é corrigida antes da entrega.

> **Princípio:** a solução chata ganha. O melhor caminho costuma ser o mais simples, que usa o que já existe e tem como voltar atrás.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Localizar o projeto no OS

Verificar se o usuário tem um OS organizado (pastas por contexto, documento mestre, `index.md`, `CLAUDE.md` ou `AGENTS.md`).

| # | Situação | O que fazer |
|---|---|---|
| 1 | Tem OS | Confirmar de qual contexto é o projeto (empresa, cliente, produto). Ler o documento mestre e o `CLAUDE.md`/`AGENTS.md` desse contexto: ferramentas já usadas, regras, decisões anteriores, marca. Trabalhar só nessa pasta |
| 2 | Já existe um app ou repositório desse projeto | Ler a estrutura antes de propor (o que já existe, que tabelas, que telas). A spec nova parte do que existe |
| 3 | Sem OS | Seguir com a entrevista; salvar a spec na pasta atual ou onde o usuário indicar |

NUNCA usar informação de outro contexto do OS.

### PASSO 1: Entrevista guiada

Fazer as perguntas em **blocos de no máximo 4**, esperar a resposta e seguir. Pular o que o usuário já respondeu. Se a resposta for vaga, dar um exemplo concreto para ele escolher ("é mais para A ou para B?").

**Bloco A: problema e pessoas**

| # | Pergunta | Por que importa |
|---|---|---|
| 1 | Que problema isso resolve? O que acontece hoje sem o app? | Sem dor clara, a spec vira lista de desejos |
| 2 | Quem usa? Quantos tipos de usuário existem (ex.: cliente, atendente, dono)? | Cada tipo vê e faz coisas diferentes |
| 3 | Quantas pessoas vão usar no primeiro mês? | Muda o caminho (planilha resolve 5, não resolve 5.000) |
| 4 | Como você vai saber que deu certo? | Vira critério de aceite |

**Bloco B: o que entra, o que sai, os dados**

| # | Pergunta | Por que importa |
|---|---|---|
| 5 | O que o usuário informa ao sistema (campos, arquivos, fotos)? | Define formulários e validação |
| 6 | O que o sistema devolve (tela, e-mail, relatório, mensagem)? | Define a saída e o "pronto" |
| 7 | Que informação precisa ficar guardada, e por quanto tempo? | Define as tabelas |
| 8 | Tem dado pessoal ou sensível (CPF, saúde, financeiro, endereço, foto de pessoa, dado de criança)? | Liga o alerta de LGPD e segurança |

**Bloco C: telas, regras e integrações**

| # | Pergunta | Por que importa |
|---|---|---|
| 9 | Quais telas você imagina? Descreva o caminho do usuário do começo ao fim | Vira o fluxo principal |
| 10 | Quem pode ver e quem pode editar cada coisa? | Vira a regra de permissão |
| 11 | Conversa com algum outro sistema (pagamento, WhatsApp, e-mail, planilha, agenda, IA)? | Cada integração é um risco e um custo |
| 12 | Vai usar celular, computador ou os dois? | Muda o desenho das telas |

**Bloco D: limites**

| # | Pergunta | Por que importa |
|---|---|---|
| 13 | O que **não** entra nesta primeira versão? | O "fora de escopo" é o que mais protege o prazo |
| 14 | Tem prazo ou orçamento? | Pode descartar caminhos |
| 15 | Qual ferramenta pretende usar (Lovable, Claude Code, Cursor, Bolt, n8n, planilha)? | O prompt final é escrito para ela |

**Zero invenção:** o que o usuário não respondeu entra na spec como "a definir", nunca como suposição apresentada como fato. Se uma resposta trava o projeto, perguntar de novo; se não trava, registrar e seguir.

### PASSO 2: Classificar o porte (em linguagem simples)

| # | Porte | Como reconhecer | Quanto processo |
|---|---|---|---|
| 1 | Ajuste rápido | Mudar um texto, uma cor, um campo. Cabe numa frase | Sem spec. Gerar só o prompt e um teste de 1 linha |
| 2 | Pequeno | Corrigir um defeito ou melhorar uma tela, sem mexer em dado | Spec curta: objetivo, o que muda, como testar |
| 3 | Médio | Mexe em 3 ou mais telas, cria campo ou tabela nova, ou muda o que outro sistema recebe | Spec completa (as 13 seções do modelo) + críticos |
| 4 | Grande | Produto novo, tabela nova com dado pessoal, integração externa, pagamento, uso de IA com dado do cliente | Spec completa + críticos + **o usuário aprova a spec antes de construir** |

Na dúvida entre dois portes, ficar no menor. Dizer ao usuário em 1 linha: "Classifiquei como **médio** porque cria uma tabela nova de clientes."

### PASSO 3: Comparar 2 ou 3 caminhos

Para porte médio ou grande, montar a tabela e recomendar o caminho mais simples que resolve:

| # | Caminho | O que muda para você | Custo e esforço | Risco | Como voltar atrás |
|---|---|---|---|---|---|
| 1 | Mais simples (ex.: formulário + planilha + automação) | ... | ... | ... | ... |
| 2 | Intermediário (ex.: app no Lovable com banco) | ... | ... | ... | ... |
| 3 | Completo (ex.: app sob medida com área logada e pagamento) | ... | ... | ... | ... |

Antes de recomendar, responder as três perguntas:
1. Qual é a **menor** mudança que resolve o problema do PASSO 1?
2. Usa algo que o usuário **já tem** (ferramenta, planilha, app atual)?
3. Se der errado, como **voltar** em um passo?

Se o caminho recomendado não for o mais simples, explicar por que o simples não serve. O usuário escolhe; registrar a escolha e o motivo na spec.

### PASSO 4: Escrever a spec no arquivo

**Nome:** `spec-{projeto}-v1.md` (minúsculas, sem acento, com hífen). Nova rodada de mudanças vira `v2`, sem apagar a anterior.

**Onde salvar:** na pasta do contexto do projeto (em `docs/` se existir). Sem OS: pasta atual. No ChatGPT sem acesso a arquivos: entregar o `.md` num bloco de código para o usuário salvar.

**Modelo da spec (preencher todas as seções; seção que não se aplica recebe "não se aplica", nunca é apagada):**

```markdown
# Spec: {nome do projeto} · v1

**Data:** DD/MM/AAAA · **Porte:** {ajuste rápido / pequeno / médio / grande}
**Ferramenta de construção:** {Lovable / Claude Code / Cursor / n8n / ...}
**Status:** rascunho | revisada pelos críticos | aprovada pelo dono

## 1. Objetivo
{Uma frase: o problema que resolve e para quem.}
**Como saberemos que deu certo:** {indicador observável}

## 2. Usuários e permissões
| # | Tipo de usuário | O que vê | O que pode criar/editar/apagar |
|---|---|---|---|
| 1 | Visitante (sem login) | ... | nada |
| 2 | Cliente logado | só os próprios dados | ... |
| 3 | Administrador | tudo | ... |

## 3. Fluxos
### Fluxo principal: {nome}
1. O usuário ...
2. O sistema ...
3. ...
**Se der errado:** {o que o usuário vê em cada falha prevista}

### Fluxos secundários
- ...

## 4. Telas
| # | Tela | Quem acessa | O que mostra | Ação principal | Estados (vazio / carregando / erro / sucesso) |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... |

## 5. Dados
| # | Tabela | Campos (tipo, obrigatório?) | Quem lê | Quem escreve | Dado sensível? |
|---|---|---|---|---|---|
| 1 | clientes | nome (texto, sim), telefone (texto, sim), ... | dono do registro e admin | dono do registro | sim (telefone) |

**Quanto tempo o dado fica guardado:** ...
**Como o usuário pede para apagar os próprios dados (LGPD):** ...

## 6. Regras de negócio
| # | Regra | Exemplo |
|---|---|---|
| 1 | Não pode agendar no passado | Data de ontem → mensagem "Escolha uma data a partir de hoje" |

## 7. Integrações
| # | Sistema externo | Para quê | O que envia / recebe | Se cair, o que acontece | Custo |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... |

## 8. Critérios de aceite (testáveis)
| # | Dado que... | Quando... | Então... |
|---|---|---|---|
| 1 | estou logado como cliente | abro "Meus agendamentos" | vejo só os meus, nunca os de outro cliente |
| 2 | deixo o telefone vazio | clico em "Salvar" | vejo "Informe o telefone" ao lado do campo e nada é salvo |
| 3 | estou sem internet | clico em "Salvar" | vejo aviso de falha e meus dados digitados continuam no formulário |

## 9. Riscos e plano de volta
| # | Risco | Chance (baixa/média/alta) | Impacto | Como evitar | Como voltar atrás |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... |

## 10. Fora de escopo (v1)
- ...

## 11. Caminho escolhido e por quê
{Caminho escolhido no PASSO 3, os descartados e o motivo de cada um.}

## 12. Revisão dos críticos
{Preenchido no PASSO 6.}

## 13. Prompt pronto para a ferramenta
{Preenchido no PASSO 5.}
```

Regras de escrita da spec:
- Critério de aceite tem de ser verificável por uma pessoa clicando: "rápido" não vale, "a lista aparece em até 2 segundos" vale.
- Cada tela tem estado vazio, carregando, erro e sucesso descritos.
- Cada tabela com dado pessoal diz quem lê e quem escreve.
- Nenhum número (preço, volume, prazo) que o usuário não deu.

### PASSO 5: Gerar o prompt pronto para colar

Escrever na seção 13 um prompt na ferramenta escolhida, com esta estrutura:

```text
Contexto: {1-2 frases do objetivo e de quem usa}

Construa a primeira versão com:
1. Telas: {lista curta, com a ação principal de cada uma}
2. Dados: {tabelas e campos}
3. Permissões: {quem vê e edita o quê}. Ative a proteção por linha (RLS) em todas as tabelas: cada usuário só acessa os próprios registros, exceto os papéis de administrador definidos na seção de usuários. Em automação (n8n, Make), aplique a mesma ideia às credenciais e a quem dispara o fluxo.
4. Regras: {lista}
5. Estados: toda tela tem estado vazio, carregando e erro com mensagem clara em português.
6. Celular primeiro: tudo funciona em tela de 375 px, botões com pelo menos 44 px de altura.

Não faça agora: {fora de escopo}

Segurança: nenhuma chave ou senha no código do navegador; chaves ficam em variável de ambiente/segredo. Valide todo campo no servidor.

Critérios de aceite (vou testar exatamente isto):
{lista da seção 8}
```

Ajustes por ferramenta:

| # | Ferramenta | Ajuste no prompt |
|---|---|---|
| 1 | Lovable / Bolt | Pedir uma etapa por vez: primeiro telas e dados, depois login, depois integrações. Prompt gigante gera app confuso |
| 2 | Claude Code / Cursor | Pedir para ler a estrutura do projeto antes, propor o plano e só então escrever código; incluir "rode os testes e mostre o resultado" |
| 3 | n8n | Descrever gatilho, cada passo e o que fazer quando um passo falha (aviso por e-mail, nova tentativa) |

### PASSO 6: Disparar os dois críticos independentes

Só para porte médio ou grande. Os críticos recebem **só o texto da spec**, nunca a conversa: quem participou da construção não enxerga os próprios furos.

**No Claude Code:** abrir dois subagentes (ferramenta Agent/Task), em paralelo, cada um com o prompt do crítico abaixo seguido do texto integral da spec. Não passar resumo da conversa.

**No ChatGPT ou em ferramenta sem subagente:** gerar os dois prompts completos (crítico + spec colada no fim) em blocos de código e instruir: "Abra **uma conversa nova** para cada crítico, de preferência uma conversa temporária ou com a memória desligada (assim o crítico não herda o que falamos aqui), cole o bloco inteiro e me traga a resposta." Esperar as duas respostas antes de seguir.

**Prompt do crítico de SEGURANÇA:**

```text
Você é um revisor de segurança independente. Não participou da criação desta especificação e não pode alterá-la. Leia a spec abaixo e aponte os furos de segurança e privacidade ANTES de alguém construir o sistema.

Verifique, um a um:
1. Dados sensíveis e LGPD: há dado pessoal ou sensível (CPF, saúde, financeiro, criança, localização, foto)? Está dito por quanto tempo fica guardado e como o titular pede para apagar? Coleta-se mais do que o necessário?
2. Quem pode ver e editar o quê: a spec define permissões por tipo de usuário? Um usuário consegue ver ou alterar dado de outro trocando um número na URL?
3. Proteção no banco: as tabelas têm proteção por linha (RLS ou equivalente) descrita? Há tabela sem dono definido?
4. Chaves e segredos: alguma chave de API, senha ou token poderia acabar no navegador ou no código público?
5. Entrada do usuário: os campos são validados no servidor? Upload de arquivo tem limite de tipo e tamanho?
6. Pagamentos e webhooks: se houver, o sistema confirma o pagamento pelo servidor e confere a assinatura do webhook, ou confia no que o navegador diz?
7. IA: se houver IA lendo texto de usuário ou de terceiros, há risco de alguém escrever instruções que a IA obedeça (prompt injection)? A IA tem acesso a mais dado do que precisa?
8. Logs: algum registro de erro ou log guarda dado pessoal, senha ou token?
9. Ações destrutivas: apagar, enviar em massa, cobrar. Há confirmação e permissão adequada?
10. Volta atrás: há backup e plano de volta para cada mudança em banco de dados ou integração? Seção de riscos e rollback (plano de volta) vazia = achado de gravidade alta.
11. Login e abuso: as tentativas de senha são limitadas? Há limite de requisições? O custo de chamadas de IA tem teto?

Responda SOMENTE com uma tabela:
| # | Achado | Seção da spec | Gravidade (alta/média/baixa) | Correção sugerida |
Gravidade alta = vaza dado, permite agir em nome de outro, ou perde dinheiro. Não invente: se a spec não dá informação suficiente, escreva "a spec não define X" como achado. Se não houver achado num item, não o liste.

SPEC:
{colar aqui o texto integral da spec}
```

**Prompt do crítico de EXPERIÊNCIA DO USUÁRIO (UX/UI):**

```text
Você é um revisor de experiência do usuário independente. Não participou da criação desta especificação e não pode alterá-la. Leia a spec abaixo pensando numa pessoa comum, com pressa, no celular.

Verifique, um a um:
1. Fluxo mais curto: dá para chegar ao objetivo com menos telas, cliques ou campos? Algum campo pode ser preenchido automaticamente ou removido?
2. Estados: cada tela descreve o que aparece vazia, carregando, com erro e com sucesso? A pessoa sempre sabe o que está acontecendo?
3. Celular: as telas funcionam em 375 px de largura? Botões com pelo menos 44 px? Nada que exija passar o mouse por cima?
4. Acessibilidade: contraste de texto suficiente, campos com rótulo visível (não só placeholder), dá para usar com teclado?
5. Texto claro: botões dizem o que fazem ("Salvar agendamento", não "OK")? Mensagens de erro dizem o que houve e como resolver, na língua de quem usa?
6. Uma ação principal por tela: há telas com várias ações competindo pela atenção?
7. Ações perigosas: apagar ou cancelar pede confirmação ou permite desfazer? Fica longe do botão principal?
8. O que o usuário vê em cada passo: há algum passo em que a pessoa fica sem resposta, sem saber se deu certo, ou termina numa tela em branco?

Responda SOMENTE com uma tabela:
| # | Achado | Tela/fluxo | Gravidade (alta/média/baixa) | Correção sugerida |
Gravidade alta = a pessoa não consegue concluir a tarefa ou desiste. Não invente: se a spec não descreve algo, escreva "a spec não define X". Se não houver achado num item, não o liste.

SPEC:
{colar aqui o texto integral da spec}
```

### PASSO 7: Consolidar os achados e corrigir a spec

1. Juntar as duas respostas numa tabela única, ordenada por gravidade:

| # | Crítico | Achado | Gravidade | O que fiz na spec |
|---|---|---|---|---|
| 1 | Segurança | Cliente pode ver agendamento de outro pela URL | alta | Seção 2 e 8: regra "cada cliente só vê os próprios" + critério de aceite |
| 2 | UX | Erro de pagamento sem mensagem | média | Seção 4: estado de erro descrito |

2. Corrigir a spec em **todos** os achados de gravidade alta. Médios e baixos: corrigir ou registrar por que ficaram de fora.
3. Achado que depende de decisão do usuário (ex.: "guardar ou não o CPF") vira pergunta direta, fechada, com recomendação.
4. Colar a tabela na seção 12 da spec, atualizar o prompt da seção 13 e mudar o status para "revisada pelos críticos".
5. Achado que o crítico inventou (cita algo que não está na spec) é descartado com o motivo na tabela.

### PASSO 8: Entregar

Dizer ao usuário, em poucas linhas:
1. O caminho completo do arquivo da spec.
2. O porte e o caminho escolhido.
3. Quantos achados os críticos trouxeram e quantos foram corrigidos.
4. O que ainda depende dele (itens "a definir").
5. Para porte grande: "Aprove a spec antes de colar o prompt na ferramenta."

Se o OS tiver `index.md` no contexto, oferecer registrar a spec nele.

---

## Regras desta skill

- **Spec antes de código.** Esta skill não constrói o app; ela entrega a spec e o prompt. Construir é o passo seguinte, com aprovação do usuário.
- **Simples primeiro.** Sempre comparar caminhos e recomendar o mais simples que resolve. Complexidade precisa de justificativa escrita.
- **Zero invenção.** O que o usuário não disse vira "a definir" ou pergunta. Nada de preço, volume, regra ou integração suposta.
- **Fora de escopo é obrigatório.** Spec sem a seção 10 preenchida não está pronta.
- **Críticos independentes de verdade.** Recebem só a spec. Nunca o resumo da conversa, nunca a opinião do agente sobre a spec.
- **Achado alto se corrige antes da entrega.** Dado pessoal exposto, permissão furada ou pagamento confiando no navegador não ficam para depois.
- **Um projeto, um contexto.** Não misturar dados ou exemplos de outro contexto do OS.
- **Processo do tamanho do problema.** Ajuste rápido não ganha spec de dez seções.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Contexto do OS lido (documento mestre, CLAUDE.md/AGENTS.md) ou ausência de OS confirmada
- [ ] Entrevista cobriu o necessário para o porte (médio/grande: problema, usuários, entradas, saídas, dados, telas, integrações e fora de escopo; pequeno e ajuste rápido: o que muda e como testar)
- [ ] Porte classificado e explicado em 1 linha
- [ ] 2-3 caminhos comparados (médio/grande), o escolhido registrado com o motivo
- [ ] Porte médio/grande: spec salva com as 13 seções; o que não se aplica marcado, nada apagado
- [ ] Porte pequeno: spec curta salva com objetivo, o que muda e como testar (ajuste rápido: só o prompt e o teste de 1 linha)
- [ ] Porte médio/grande: toda tela com estados vazio, carregando, erro e sucesso
- [ ] Porte médio/grande: todo dado pessoal com quem lê, quem escreve e prazo de guarda
- [ ] Porte médio/grande: critérios de aceite no formato "dado que / quando / então", testáveis por clique (pequeno: 1 a 3 testes simples)
- [ ] Prompt pronto para a ferramenta escolhida, com RLS, segredos fora do navegador e celular primeiro
- [ ] Porte médio/grande: os dois críticos rodaram só com a spec (subagente ou conversa nova, temporária ou sem memória)
- [ ] Porte médio/grande: todos os achados altos corrigidos; tabela de achados na seção 12
- [ ] Nenhum dado, número ou regra inventado
- [ ] Caminho completo do arquivo informado ao usuário

Se algum item falhou: corrigir ANTES de declarar concluído. Nunca reportar "feito" com item pendente.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
