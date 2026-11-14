---
name: cartilha
description: "Tira um processo da cabeça do gestor e transforma em manual (POP, procedimento operacional padrão) que outra pessoa consegue executar sozinha: entrevista sobre gatilho, entradas, passos, decisões, exceções, erros comuns e critério de pronto, gera o POP com passo a passo numerado, checklist, tabela de decisões, exemplos e glossário, e faz o 'teste do novato' antes de fechar. Usar quando o usuário disser 'cria um POP', 'transforma isso em manual', 'quero passar esse processo pra frente', 'escreve o procedimento de', 'só eu sei fazer isso', ou pedir para documentar uma rotina para treinar alguém."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Cartilha

## O que esta skill faz

Transforma o "eu faço de cabeça" em um procedimento escrito que alguém novo consegue seguir sem ligar para o gestor a cada dúvida. O produto final é um POP (procedimento operacional padrão) de uma tarefa só, com versão e data, passo a passo numerado, decisões explícitas no formato "se acontecer X, faça Y", checklist de conferência e exemplos reais.

O diferencial está no fim: antes de entregar, o agente finge ser um funcionário recém-chegado, lê o POP e faz as perguntas que esse novato faria. Cada pergunta sem resposta é um buraco no manual, e é corrigido antes de fechar.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Contexto, tarefa e leitor

Perguntar em 1 mensagem curta (pular o que o usuário já disse):

> "Para montar a cartilha: (1) de qual empresa ou contexto do seu OS é essa tarefa? (2) qual a tarefa, em uma frase (ex.: 'conferir e liberar pedido para entrega')? (3) quem vai executar: cargo e nível de experiência (estagiário, analista experiente, terceirizado)?"

| # | Resposta | O que muda no POP |
|---|---|---|
| 1 | Contexto | Com OS no padrão MeuOS: ler o documento mestre e o `index.md` daquele contexto para usar os nomes certos de sistemas, áreas e siglas; verificar se já existe POP sobre o tema (se existir, a tarefa vira revisão, não criação). Nunca misturar contextos |
| 2 | Tarefa | Uma tarefa por POP. "Todo o financeiro" não é tarefa; "conciliar o extrato do banco com o sistema" é |
| 3 | Executor | Define o nível de detalhe. Para iniciante, explicar onde clicar e o que é cada termo; para experiente, focar decisões e exceções |

Se houver material existente (procedimento antigo, áudio, print de tela, planilha), ler INTEIRO antes de começar a entrevista.

### PASSO 1: Entrevista em 4 blocos

Fazer um bloco por mensagem. Usar as palavras do usuário; não reescrever o jeito dele de fazer.

**Bloco A · Começo e fim**
1. O que dispara a tarefa? (horário, pedido de cliente, chegada de documento, dia do mês)
2. O que precisa estar em mãos antes de começar? (acessos, documentos, informações)
3. Qual o resultado quando está pronto? Como alguém de fora sabe que terminou certo?
4. Quem aprova ou confere o resultado, se alguém?

**Bloco B · O caminho normal**
5. Descreva os passos do começo ao fim, do jeito que você faz num dia comum.
6. Quanto tempo leva, em média? (se o usuário não souber, registrar "não medido")

**Bloco C · Decisões e exceções**
7. Em que pontos você precisa decidir alguma coisa? O que você olha para decidir?
8. O que acontece de diferente de vez em quando? (cliente sem cadastro, valor acima do normal, sistema fora do ar)
9. Em que situação a pessoa deve parar e chamar alguém? Quem?

**Bloco D · Erros**
10. Quais os erros mais comuns de quem faz isso pela primeira vez?
11. Qual erro custa mais caro? O que acontece quando ele acontece?
12. Tem alguma "manha" que só você sabe?

Se uma resposta for vaga ("aí eu vejo se está certo"), perguntar o critério concreto: "certo como? O que você confere?". O POP morre na palavra "verificar" sem dizer o quê.

### PASSO 2: Escrever o POP no template

Regras de redação:
- Um passo = um verbo no imperativo + objeto ("Abra o sistema de pedidos", "Confira se o CNPJ do pedido é igual ao da nota").
- Passo com mais de uma ação vira dois passos.
- Toda decisão vai para a tabela de decisões, no formato **se → então**, com quem chamar quando nada se aplica.
- Exemplo real em todo passo que tem chance de erro. Dado de cliente real vira dado fictício (nome, documento, valor).
- Termo interno ou sigla vai para o glossário na primeira aparição.

### PASSO 3: Teste do novato (obrigatório, antes de entregar)

O agente assume o papel de alguém novo, com o perfil do PASSO 0, e lê o POP do começo ao fim. Para cada passo, perguntar a si mesmo:

| # | Pergunta do novato | Buraco que revela |
|---|---|---|
| 1 | "Onde eu acho isso?" | Falta caminho, link ou local |
| 2 | "Como eu sei que fiz certo?" | Falta critério de conferência |
| 3 | "E se não for nenhum desses casos?" | Falta exceção ou quem chamar |
| 4 | "O que significa essa palavra?" | Falta glossário |
| 5 | "Posso pular isso se estiver com pressa?" | Falta dizer por que o passo existe |
| 6 | "Eu tenho acesso a isso?" | Falta pré-requisito |

Mostrar ao usuário a lista de perguntas sem resposta (normalmente de 5 a 10), pedir as respostas e incorporar no POP. Repetir o teste até sobrarem zero perguntas abertas ou o usuário decidir que alguma fica como "a definir" (visível no POP, nunca escondida).

### PASSO 4: Entregar e guardar

1. Entregar o POP final, com versão 1.0 e a data de hoje no topo.
2. Sugerir o teste real: a pessoa que vai executar faz a tarefa uma vez lendo só o POP, com o gestor do lado sem ajudar, anotando onde travou. Cada trava vira ajuste e a versão sobe (1.1, 1.2).
3. Com OS no padrão MeuOS, oferecer guardar no contexto do PASSO 0 com o nome `AAAA-MM-DD-pop-[tarefa].md` e atualizar o `index.md`. Sem OS, entregar no chat e oferecer o arquivo .md.

---

## Template de saída

```markdown
# POP: [nome da tarefa]

**Versão:** 1.0 · **Data:** DD/MM/AAAA · **Dono do processo:** [cargo] · **Executor:** [cargo]
**Tempo médio:** [X min ou "não medido"] · **Próxima revisão:** [data ou "quando o processo mudar"]

## Para que serve
[1 a 2 frases: o que esta tarefa garante e o que acontece se não for feita.]

## Quando fazer
[Gatilho: horário, evento ou pedido.]

## Antes de começar
- [ ] [acesso, documento ou informação necessária]

## Passo a passo
1. [Verbo + objeto.] *Exemplo:* [...]
2. [...]
   - ⚠️ Atenção: [erro comum neste passo]

## Decisões
| # | Se... | Então... | Se nenhuma se aplica |
|---|---|---|---|
| 1 | valor acima de R$ [limite informado] | pedir aprovação de [cargo] | parar e chamar [cargo] |

## Pronto quando
- [ ] [critério verificável 1]
- [ ] [critério verificável 2]

## Erros comuns
| # | Erro | Como evitar | Como corrigir se acontecer |
|---|---|---|---|

## Glossário
| # | Termo | Significado |
|---|---|---|

## Pendências deste POP
- [itens "a definir" do teste do novato, ou "nenhuma"]

## Histórico de versões
| # | Versão | Data | O que mudou |
|---|---|---|---|
| 1 | 1.0 | DD/MM/AAAA | criação |
```

---

## Regras desta skill

- **O jeito é do usuário.** O agente organiza e esclarece; não troca o método do gestor por um "melhor" sem perguntar. Sugestão de melhoria vai em nota separada no fim.
- **Zero invenção.** Limite de valor, prazo, nome de sistema ou regra que o usuário não disse vira pergunta, nunca preenchimento.
- **Um POP, uma tarefa.** Se a entrevista revelar que são duas tarefas, propor dois POPs.
- **"Verificar" sempre com o quê.** Nenhum passo pode mandar conferir sem dizer o critério.
- **Dado real fica fora.** Exemplos usam dados fictícios; nome de cliente, documento e senha nunca entram no POP.
- **Teste do novato não é opcional.** POP sem teste é rascunho.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Contexto, tarefa e executor definidos no PASSO 0
- [ ] Material existente lido inteiro (ou confirmado que não há)
- [ ] Os 4 blocos da entrevista respondidos ou marcados "não informado"
- [ ] Versão e data no topo do POP
- [ ] Cada passo com um verbo e uma ação; nenhum "verificar" sem critério
- [ ] Decisões em tabela se → então, com quem chamar
- [ ] Critério de pronto verificável
- [ ] Exemplos com dados fictícios
- [ ] Teste do novato feito e perguntas abertas resolvidas ou listadas em "Pendências"
- [ ] Se guardado no OS: nome `AAAA-MM-DD-pop-[tarefa].md` e `index.md` atualizado

Se algum item falhou: corrigir ANTES de declarar concluído. Nunca reportar "feito" com item pendente.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
