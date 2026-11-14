---
name: ler-contrato
description: "Lê contrato, proposta comercial ou termo antes de assinar e devolve em linguagem simples: partes, objeto, valores e reajuste, prazos e renovação automática, multas e rescisão, exclusividade, confidencialidade e dados pessoais, foro, cláusulas incomuns ou desequilibradas e o que está faltando, com semáforo por cláusula e citação exata do trecho, perguntas para negociar e sugestão de redação alternativa. Não substitui advogado. Usar quando o usuário disser 'lê esse contrato pra mim', 'posso assinar isso?', 'tem alguma pegadinha nesse contrato', 'revisa essa proposta do fornecedor', 'o que eu devo negociar nesse contrato', ou enviar um contrato pedindo análise."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Ler Contrato

> ⚖️ **AVISO FIXO: esta skill não substitui advogado.** Ela ajuda o gestor a entender o que está assinando e a chegar preparado na negociação. Se houver qualquer cláusula 🔴, valor alto para o porte da sua empresa, prazo longo, garantia pessoal (aval, fiança) ou assunto trabalhista, societário ou tributário: **leve a um advogado antes de assinar.** O agente repete este aviso no topo de todo relatório.

## O que esta skill faz

Lê o documento inteiro e devolve o que importa para quem vai assinar: quanto custa, por quanto tempo prende, como sai, quanto paga se sair, o que fica proibido de fazer e o que está estranho. Cada ponto vem com o número da cláusula e o trecho copiado exatamente como está no documento, para o gestor conferir com os próprios olhos. No fim, a lista do que perguntar e do que pedir para mudar, com sugestão de texto.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Contexto e posição do usuário

Perguntar em 1 mensagem curta (pular o que o usuário já disse):

> "Antes de ler: (1) de qual empresa ou contexto do seu OS é esse contrato? (2) você é quem contrata (cliente) ou quem é contratado (fornecedor)? (3) o que é mais importante para você neste acordo: preço, prazo, poder sair fácil, exclusividade, outra coisa? (4) tem prazo para assinar?"

| # | Resposta | O que muda |
|---|---|---|
| 1 | Contexto | Com OS no padrão MeuOS: ler o documento mestre daquele contexto (porte, faturamento, fornecedores atuais) para avaliar o peso dos valores; checar se há contrato anterior com a mesma parte. Nunca usar dados de outro contexto |
| 2 | Posição | Define o que é risco. Multa alta por rescisão é ruim para quem pode querer sair e boa para quem quer garantir receita |
| 3 | Prioridade | Ordena o relatório e as perguntas de negociação |
| 4 | Prazo | Se for curto, entregar primeiro o resumo e os 🔴, depois o resto |

### PASSO 1: Ler o documento INTEIRO

- Ler todas as páginas, incluindo anexos, tabelas de preço, termos referenciados ("conforme Política de Uso disponível em...") e letras pequenas.
- Se o documento citar anexo ou política que não foi enviado, registrar em "O que está faltando" e pedir ao usuário. Não supor o conteúdo.
- Se o arquivo vier ilegível (imagem ruim, página cortada), avisar quais trechos não foram lidos. Relatório de documento lido pela metade não sai como completo.
- Anotar a numeração exata das cláusulas como está no documento.

### PASSO 2: Extrair os 12 pontos

| # | Ponto | O que procurar |
|---|---|---|
| 1 | Partes | Quem assina, com que qualificação; se quem assina tem poder para isso |
| 2 | Objeto | O que exatamente é entregue; o que fica de fora |
| 3 | Valores | Preço, forma e data de pagamento, impostos inclusos ou não, cobranças extras |
| 4 | Reajuste | Índice, periodicidade, se há teto |
| 5 | Prazo e renovação | Duração, renovação automática, prazo de aviso para não renovar |
| 6 | Rescisão e multas | Como sai cada parte, aviso prévio, multa, juros de atraso |
| 7 | Exclusividade e não concorrência | O que fica proibido, por quanto tempo, onde |
| 8 | Confidencialidade e dados pessoais (LGPD) | O que é sigiloso, por quanto tempo; quem trata dados pessoais, para quê e com qual responsabilidade; se o contrato fala do tema ou é omisso |
| 9 | Responsabilidade e garantias | Limite de indenização, quem responde por falha, garantias pessoais |
| 10 | Propriedade intelectual | De quem é o que for produzido |
| 11 | Foro e solução de conflitos | Cidade do foro, arbitragem, mediação |
| 12 | Cláusulas incomuns | Qualquer coisa fora do padrão do restante do contrato ou que só obriga um lado |

### PASSO 3: Semáforo por cláusula

| # | Cor | Critério |
|---|---|---|
| 1 | 🟢 | Claro, equilibrado entre as partes, sem surpresa para a posição do usuário |
| 2 | 🟡 | Ambíguo, ou desfavorável mas comum e negociável; vale perguntar |
| 3 | 🔴 | Obriga só um lado, prende sem saída razoável, multa desproporcional ao valor do contrato, responsabilidade ilimitada, renúncia de direito, garantia pessoal, ou texto que contradiz outra cláusula |

Cada item sai com: número da cláusula, trecho copiado entre aspas **exatamente** como está, explicação em linguagem simples e por que recebeu aquela cor.

**Sobre lei:** o agente NÃO cita artigo de lei, número de lei ou jurisprudência de memória. Se um ponto parece depender de lei (ex.: limite de multa, regra de dados pessoais, direito do consumidor), escrever "pode haver regra legal específica sobre isso: confirmar com advogado". Só citar lei se o próprio contrato citar, ou se a fonte oficial for consultada na hora e o link for informado.

### PASSO 4: O que está faltando

Listar o que um contrato desse tipo normalmente deveria ter e não tem (ex.: prazo de entrega, nível de serviço, critério de aceite, como devolver dados no fim, quem paga impostos). Formular como pergunta, não como afirmação de ilegalidade.

### PASSO 5: Negociação

Para cada 🔴 e cada 🟡 relevante para a prioridade do usuário:
- **Pergunta para a outra parte**, em tom profissional.
- **Sugestão de redação alternativa**, marcada como "sugestão para discutir com seu advogado".

### PASSO 6: Entregar e guardar

1. Entregar o relatório no template abaixo, com o aviso fixo no topo.
2. Com OS no padrão MeuOS, oferecer guardar no contexto do PASSO 0 como `AAAA-MM-DD-contrato-[parte]-[tema].md` e atualizar o `index.md`. Não copiar o contrato inteiro para o OS sem o usuário pedir; o relatório basta.

---

## Template de saída

```markdown
# Leitura de contrato: [tipo] com [outra parte]

> ⚖️ Esta leitura não substitui advogado. Há [N] pontos 🔴: [levar a um advogado antes de assinar / nenhum ponto 🔴, mas valide com advogado se o valor for relevante].

**Documento:** [nome do arquivo, nº de páginas, data do documento] · **Lido em:** DD/MM/AAAA
**Sua posição:** [contratante/contratado] · **Sua prioridade:** [...]
**Trechos não lidos ou anexos ausentes:** [lista ou "nenhum"]

## Em 5 linhas
- O que é: ...
- Quanto custa: ...
- Quanto tempo prende: ...
- Como sair e quanto custa sair: ...
- Maior risco: ...

## Partes e quem assina (poderes)
| # | Parte | Quem assina pela parte | Com que poder (cargo, procuração, contrato social) | Conferido? |
|---|---|---|---|---|
| 1 | ... | ... | ... | [sim / não consta no documento: pedir] |

## Semáforo
| # | Cláusula | Tema | Cor | Trecho exato | O que significa |
|---|---|---|---|---|---|
| 1 | 5.2 | Renovação | 🔴 | "..." | ... |

## Não se aplica
| # | Ponto dos 12 | Por que não se aplica a este contrato |
|---|---|---|
| 1 | ... | ... |

## O que está faltando
| # | Ponto ausente | Pergunta a fazer |
|---|---|---|

## Para negociar
| # | Cláusula | Pergunta | Sugestão de redação (validar com advogado) |
|---|---|---|---|

## Próximo passo
[Assinar como está / negociar os itens X e Y / levar a advogado antes, por causa de Z]
```

---

## Regras desta skill

- **Aviso fixo sempre visível.** Nenhum relatório sai sem o aviso de que não substitui advogado.
- **Documento inteiro, sempre.** Anexo ausente ou página ilegível é declarado; nunca presumido.
- **Citação exata.** Todo ponto tem número da cláusula e trecho copiado sem paráfrase. Se não achou o trecho, não afirma.
- **Lei não se inventa.** Nada de artigo de lei de memória. Na dúvida: "confirmar com advogado".
- **Sem veredito de legalidade.** O agente aponta risco e desequilíbrio; não declara cláusula "ilegal" ou "nula".
- **Contrato é sigiloso.** Não reproduzir trechos fora do relatório nem misturar com outro contexto.

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Aviso "não substitui advogado" no topo do relatório
- [ ] Contexto, posição, prioridade e prazo perguntados no PASSO 0
- [ ] Documento lido inteiro, com anexos ausentes e trechos ilegíveis declarados
- [ ] Os 12 pontos verificados (presentes, ausentes ou não se aplica)
- [ ] Cada item do semáforo com número da cláusula e trecho exato entre aspas
- [ ] Nenhum artigo de lei citado de memória
- [ ] "O que está faltando" preenchido
- [ ] Perguntas e redação alternativa para cada 🔴
- [ ] Recomendação de advogado explícita quando há 🔴, valor alto ou garantia pessoal
- [ ] Se guardado no OS: nome `AAAA-MM-DD-contrato-[parte]-[tema].md` e `index.md` atualizado

Se algum item falhou: corrigir ANTES de declarar concluído. Nunca reportar "feito" com item pendente.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
