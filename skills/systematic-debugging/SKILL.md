---
name: systematic-debugging
description: |
  Debugging metodico para a stack voce-OS (n8n, Supabase, Lovable).
  Invoque quando houver erro, falha, comportamento inesperado, ou quando
  voce disser "nao ta funcionando", "deu erro", "quebrou", "parou de funcionar".
  Tambem ativar quando uma correcao falhar — nunca tentar a mesma coisa duas vezes.
---

# Systematic Debugging

## Filosofia
> Nunca chutar. Sempre investigar.
> Se a 3a tentativa de fix falhou, PARAR e repensar a abordagem inteira.

## Fase 1 — Coletar evidencias (antes de tocar em qualquer coisa)

### Para erros em N8N:
- Ler o log de execucao completo (n8n MCP -> n8n_executions)
- Identificar QUAL no falhou e a mensagem exata de erro
- Verificar se o workflow funcionava antes (quando parou?)
- Checar se o input do no esta no formato esperado

### Para erros em Supabase:
- Ler o erro exato (execute_sql ou get_logs)
- Verificar se a tabela/coluna existe (list_tables)
- Checar RLS policies se for erro de permissao
- Verificar se a migration mais recente rodou (list_migrations)

### Para erros em Lovable:
- Abrir a URL via Playwright e tirar screenshot
- Verificar console do browser (browser_console_messages)
- Identificar se e erro visual, funcional ou de dados

## Fase 2 — Diagnosticar (entender ANTES de consertar)

### Perguntas obrigatorias:
1. **O que mudou?** — O que foi alterado desde a ultima vez que funcionou?
2. **E isolado?** — So essa parte falha, ou outras tambem?
3. **E reproduzivel?** — Acontece sempre ou intermitente?
4. **Onde esta o problema?** — Frontend, backend, integracao, ou dados?

### Padrao de diagnostico:
```
SINTOMA: [o que voce ve]
EVIDENCIA: [log/erro/screenshot que confirma]
HIPOTESE: [causa provavel baseada na evidencia]
TESTE: [como validar a hipotese sem alterar nada]
```

## Fase 3 — Corrigir (uma coisa por vez)

### Regras inviolaveis:
1. **Uma mudanca por vez** — nunca alterar 2 coisas simultaneamente
2. **Testar apos cada mudanca** — verificar se resolveu antes de mudar mais
3. **Documentar o que tentou** — se falhar, voce sabe o que ja foi feito
4. **Rollback pronto** — saber como desfazer antes de aplicar

### Se a correcao falhar:
- 1a falha: tentar abordagem diferente (nao repetir a mesma)
- 2a falha: voltar a Fase 2, questionar a hipotese
- 3a falha: PARAR. Apresentar para voce:
  > "Ja tentei 3 abordagens e nenhuma resolveu. O problema pode ser mais profundo.
  > Veja o que ja tentei: [lista]. Quer que eu investigue [direcao alternativa]?"

## Fase 4 — Confirmar e prevenir

1. **Confirmar**: Executar/testar para provar que funciona (nao assumir)
2. **Explicar**: Dizer para voce O QUE causou e POR QUE a correcao funciona
3. **Prevenir**: Se aplicavel, sugerir como evitar que aconteca de novo

## Anti-padroes (NUNCA fazer)
- NAO "Deve estar funcionando agora" — sem testar
- NAO Mudar 5 coisas de uma vez e dizer "tentei resolver"
- NAO Deletar e recriar do zero como primeiro recurso
- NAO Ignorar warnings achando que "nao sao importantes"
- NAO Chutar a causa sem ler o log/erro primeiro
