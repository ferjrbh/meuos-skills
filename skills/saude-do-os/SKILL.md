---
name: saude-do-os
description: |
  Avalia a saude do seu OS direto no seu computador: le os arquivos .md da pasta do OS,
  pontua de 0 a 100 pela rubrica oficial do MeuOS (Estrutura, Volume, Frescor, Completude),
  mostra semaforo e lista de problemas com o caminho de cada arquivo. Roda 100% local —
  enxerga TODOS os arquivos da pasta, inclusive os criados por outras ferramentas.
  Executa quando o usuario diz "saude do os", "avaliar meu os", "nota do os", "health check
  do os", "como esta meu os", "diagnostico do os".
version: 1.0
context: meuos
user-invocable: true
argument-hint: "(sem args — roda na pasta do OS aberta no agente)"
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Saúde do OS — avaliação local (0 a 100)

> **Read-only.** Esta skill NUNCA cria, edita ou apaga arquivo. Ela só lê e reporta.
> A rubrica abaixo é a MESMA do app MeuOS (paridade 1:1) — não invente critérios novos,
> não arredonde diferente, não pule penalidade.

## Passo 0 — Localize a raiz do OS (obrigatório)

1. A raiz do OS é a pasta que contém `claude.md` E `soul.md` (nomes em minúsculas).
2. Se a pasta atual não for a raiz, procure 1 nível acima e 1 abaixo.
3. **Se não encontrar, PARE** e diga: "Não encontrei a raiz do seu OS (pasta com claude.md
   e soul.md). Abra o agente na pasta do OS e rode a skill de novo." Não avalie outra pasta.

## Passo 1 — Inventário

1. Liste todos os `.md` da raiz até 3 níveis (raiz = nível 0, contexto = 1, subpasta = 2).
2. **Contextos** = pastas do nível 1, EXCETO: pastas ocultas (começando com `.`), `bkp/`
   e `.meuos/`. Pastas ocultas não são contexto e NÃO pontuam.
3. Para cada arquivo, colete: tamanho em KB e data de modificação (mtime do arquivo).
4. Idade do OS = dias desde o mtime MAIS ANTIGO entre `claude.md` e `soul.md` da raiz.
   Se idade < 7 dias, o OS é NOVO → a categoria C (Frescor) não desconta nada.

## Passo 2 — Rubrica (some os descontos por categoria; piso 0 em cada uma)

### Categoria A — Estrutura (começa com 30)
| Verificação | Desconto | Severidade |
|---|---|---|
| `claude.md` da raiz ausente | −10 | crítico |
| `soul.md` da raiz ausente | −5 | alto |
| `index.md` da raiz ausente | −2 | baixo |
| Arquivos obrigatórios por contexto (`claude.md`, `documento_mestre.md`, `aprendizados_do_dia.md`, `changelog.md`): conte os ausentes | −round(ausentes ÷ total_obrigatórios × 10) | alto (1 problema por arquivo ausente) |
| Arquivo do OS com nome fora do padrão `^[a-z0-9_]+\.md$` | −3 (uma vez) | baixo |

### Categoria B — Volume (começa com 30)
| Verificação | Desconto | Severidade |
|---|---|---|
| `claude.md` raiz < 0.5 KB (possivelmente vazio) | −8 | alto |
| `claude.md` raiz > 15 KB (compactar) | −4 | médio |
| `soul.md` raiz < 0.3 KB (template vazio) | −5 | alto |
| Mestres problemáticos (< 0.5 KB nunca preenchido OU > 50 KB): conte-os | −round(problemáticos ÷ nº_contextos × 8) | alto / médio |
| ALGUM `aprendizados_do_dia.md` > 100 KB | −5 (uma vez) | alto |
| ALGUM `changelog.md` > 200 KB | −4 (uma vez) | médio |

### Categoria C — Frescor (começa com 25; OS NOVO = pula inteira)
| Verificação | Desconto | Severidade |
|---|---|---|
| Mestres sem atualização há > 30 dias: conte-os | −round(desatualizados ÷ nº_contextos × 10) | médio (cite os dias) |
| `aprendizados_do_dia.md` sem atualização há > 14 dias: TODOS desatualizados → −10; alguns → −round(desatualizados ÷ total × 5) | ver regra | médio |
| NENHUM `changelog.md` com modificação nos últimos 30 dias | −5 | baixo |

### Categoria D — Completude (começa com 15)
| Verificação | Desconto | Severidade |
|---|---|---|
| `claude.md` raiz com < 3 seções (`## `) | −5 | alto |
| `soul.md` raiz com < 2 seções (`## `) | −3 | médio |
| `index.md` raiz com < 5 linhas de conteúdo real (ignora vazias e `<!--`) | −2 | baixo |
| Mestres com < 3 seções: conte-os | −round(incompletos ÷ nº_contextos × 4) | médio |
| TODOS os `aprendizados_do_dia.md` com < 5 linhas de conteúdo real | −3 | baixo |

### Penalidades extras (aplicar SOBRE o total; piso final 10)
| Verificação | Desconto |
|---|---|
| `"a definir"` em arquivo com conteúdo (ISENTOS: `aprendizados_do_dia.md` e `changelog.md` — são logs) | −5 por ocorrência |
| "Mestre pobre": < 800 bytes, OU sem seção de decisões, OU pendências sem mexer há 30+ dias | −5 por sinal |

## Passo 3 — Resultado (formato fixo)

```
SAÚDE DO OS — {score}/100 {🟢|🟡|🔴}

Estrutura   {sA}/30
Volume      {sB}/30
Frescor     {sC}/25   (ou "isento — OS novo")
Completude  {sD}/15

Problemas ({n}):
{tabela: severidade | arquivo | problema — ordenada crítico→alto→médio→baixo}

Top 3 ações recomendadas:
1. ...
```

Semáforo: 80-100 🟢 "OS saudável — estrutura completa e ativo" · 50-79 🟡 "OS com melhorias
necessárias" · 0-49 🔴 "OS com problemas estruturais".

## Regras finais

- Ao terminar, ofereça: "Quer que eu corrija algum desses pontos? A skill **otimizar-os**
  faz a manutenção completa." NÃO corrija nada sem o usuário pedir.
- Não mostre o passo a passo do cálculo — só o resultado no formato acima.
