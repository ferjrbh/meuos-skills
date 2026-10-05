# Modelo de laudo do copiloto

## Modo número

```
COPILOTO · CROSS-CHECK
Pergunta: ...
Número do copiloto: ...   (endereço: arquivo, coluna, filtro, conta)
Definição usada: o que conta como um · numerador · denominador · período · perímetro
Contexto lido: (arquivo e definições usadas, ou "sem contexto na pasta")

Mapa das variantes (no máximo 8 linhas)
| variante | numerador | denominador | resultado |

Qual responde à pergunta, e por quê: ...
Armadilhas conferidas: unidade · denominador · perímetro · período · agregação · repetição
Para o comandante: compare com o seu número. Se for outro, ache-o no mapa:
a linha em que ele aparece mostra o que mudou.
```

## Modo revisar

```
COPILOTO · LAUDO DE REVISÃO
Peça: (arquivo) · bases usadas: (pasta) · data da revisão
Decisão que a peça sustenta: ...
Número principal: ... · régua: 🔴 acima de (5% do principal) ou se virar a decisão

VEREDITO: 🔴 NÃO SAI | 🟡 SAI COM CORREÇÃO | 🟢 PODE SAIR
Em uma frase: ...

ACHADOS, do mais grave ao mais leve
| # | gravidade | onde | o que a peça diz | o que o dado diz | prova (a conta que gera os dois números) | correção | código do catálogo |

CONTRADITÓRIO
Pré-mortem: ...
Conclusão oposta mais forte: ...
O que falta na peça: ...

COBERTURA
Números recalculados: N de M (quais)
Checagens do catálogo: conferidas e limpas · não se aplicam · não feitas, e por quê
Fonte de fora usada: ... (ou "nenhuma disponível")
Não medido: ...

DÚVIDAS (achados que não consegui reproduzir)
...

Arquivos lidos: ...   Cálculos em: ...
```

Regras do laudo: achado sem prova reproduzível vai para DÚVIDAS; achado 🔴 sem resposta depois de dois avisos segura a peça; a correção sugerida diz o número certo e de onde ele vem.
