---
name: Lovable Prompt Master
description: Cria prompts otimizados para o Lovable baseados nas melhores práticas oficiais. Invoque ela sempre que eu pedir para "criar prompt pro Lovable", "como pedir pro Lovable fazer X", ou quando for construir/modificar qualquer feature nos projetos via lovable
---

# Lovable Prompt Master

## Como estruturo um prompt perfeito para o Lovable

### Regra #1 — Uma coisa por vez
Cada prompt deve pedir UMA mudança. Nunca combine "crie o componente + estilize + adicione animação" em um prompt. Podemos ter mais uma desde que sejam nas mesmas telas ou componentes ou logica de fluxo coerente e único.

### Regra #2 — Contexto antes da instrução
Formato obrigatório:
"No [nome do componente/página], [descreva o estado atual]. Quero que [instrução específica]. O resultado deve [critério de aceite]."

### Regra #3 — Referência visual quando possível
Se tiver screenshot ou design, descreva os elementos visuais com precisão:
cores em hex, espaçamentos em px, fontes por nome.

### Regra #4 — Preservar o que existe
Sempre inclua: "Mantenha todo o restante da página exatamente como está."

### Regra #5 — Para bugs
"Na [página/componente], quando [ação do usuário], ocorre [comportamento atual]. O comportamento esperado é [o que deveria acontecer]. Não altere nenhuma outra funcionalidade."

## Template de prompt para nova feature
"Estou construindo [nome do produto]. Na página [nome], preciso adicionar [feature específica].
Ela deve: [lista de comportamentos].
Design: [descrição visual ou referência ao Figma].
Restrições: não altere [o que não pode mudar].
Critério de pronto: [como saber que funcionou]."

## Template de prompt para correção de bug
"Na página [nome], o componente [nome] apresenta o seguinte problema: [descrição exata].
Passos para reproduzir: [1, 2, 3].
Comportamento esperado: [descrição].
Não modifique nenhuma outra parte do código."

## Template de prompt para design/UI
"Crie um componente [nome] com as seguintes especificações:
- Layout: [descrição]
- Cores: background [hex], texto [hex], botão primário [hex]
- Tipografia: [fonte], tamanho [px], peso [valor]
- Espaçamento: padding [px], margin [px]
- Estados: hover [descrição], active [descrição], disabled [descrição]
- Mobile: [comportamento responsivo]
Use Tailwind CSS. Exporte como componente React reutilizável."

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
