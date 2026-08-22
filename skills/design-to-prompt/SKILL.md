---
name: design-to-prompt
description: |
  Converte referencias visuais (screenshots, descricoes, URLs) em prompts precisos para o Lovable
  ou em especificacoes de componente. Invoque quando voce mostrar uma imagem de design,
  um site de referencia, ou pedir para "replicar esse visual", "fazer parecido com X", "criar esse componente".
  DESAMBIGUACAO: Se voce disser apenas "design" sem contexto, PERGUNTAR:
  "Qual tipo de design? 1) Converter referencia visual em prompt Lovable (design-to-prompt) 2) Interface/tela (interface-design) 3) Visual estatico/poster/certificado (canvas-design)"
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Design to Prompt

## Processo de análise visual

Quando recebo uma referência visual, analiso e extraio:
1. **Layout**: grid, flexbox, número de colunas, alinhamentos
2. **Cores**: identifico o hex de cada cor principal
3. **Tipografia**: família, tamanho, peso, line-height
4. **Espaçamento**: padding e margin de cada elemento
5. **Componentes**: identifico quais são reutilizáveis
6. **Interações**: hover states, transições, animações visíveis
7. **Responsividade**: como se comporta em mobile

## Output padrão
Gero DOIS entregáveis:
1. **Prompt Lovable**: pronto para colar e executar
2. **Spec técnica**: para documentar no normas.md do produto

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)

---

## Checklist final: a execucao foi bem feita? (conferir ANTES de declarar concluido)

- [ ] Referencia visual analisada de verdade (imagem ou URL lida), nunca descrita de memoria
- [ ] Prompt segue o Output padrao da skill, completo
- [ ] Prompt instrui preservar o que ja existe no projeto alvo
- [ ] Cores, tipografia e espacamento extraidos da referencia com valores concretos
- [ ] Entregue pronto pra colar, autocontido (nao depende desta conversa)

Se algum item falhou: corrigir ANTES de declarar concluido. Nunca reportar "feito" com item pendente.
