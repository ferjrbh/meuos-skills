---
name: backup-do-os
description: |
  Faz backup completo do seu OS direto no seu computador: copia todos os arquivos da pasta
  do OS para bkp/AAAA-MM-DD_HH-MM/ (mesma convencao do app MeuOS), confere a copia arquivo
  por arquivo e mostra o resumo. Roda 100% local — copia TUDO, inclusive arquivos criados
  por outras ferramentas, em segundos. Se a pasta e sincronizada (Drive/OneDrive), o backup
  sobe para a nuvem automaticamente.
  Executa quando o usuario diz "backup do os", "fazer backup", "copia de seguranca do os",
  "backup dos meus arquivos".
version: 1.1
context: meuos
user-invocable: true
argument-hint: "(sem args — roda na pasta do OS aberta no agente)"
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Backup do OS — cópia de segurança local

> **Só cria, nunca apaga.** Esta skill NUNCA remove, sobrescreve ou edita arquivo do OS —
> nem backups antigos (o histórico em `bkp/` é permanente). Se algo já existir no destino,
> pare e avise.

## Passo 0 — Localize a raiz do OS (obrigatório)

1. A raiz do OS é a pasta que contém `claude.md` E `soul.md` (nomes em minúsculas).
2. Se a pasta atual não for a raiz, procure 1 nível acima e 1 abaixo.
3. **Se não encontrar, PARE** e diga: "Não encontrei a raiz do seu OS (pasta com claude.md
   e soul.md). Abra o agente na pasta do OS e rode a skill de novo." Não copie outra pasta.

## Passo 1 — Crie a pasta do backup

1. Na raiz do OS, garanta a pasta `bkp/` (crie se não existir).
2. Crie `bkp/AAAA-MM-DD_HH-MM/` com a data e hora locais de AGORA (ex.: `bkp/2026-07-30_15-40/`).
3. Se essa pasta já existir (dois backups no mesmo minuto), acrescente `-2`.

## Passo 2 — Copie

1. Copie TODA a árvore da raiz do OS para a pasta do backup, preservando a estrutura de
   pastas, com estas regras:
   - **EXCLUIR**: `bkp/` (nunca backup-dentro-de-backup) e `.meuos/`.
   - **INCLUIR**: todo o resto — todos os arquivos (não só `.md`) e também pastas ocultas
     como `.claude/`.
2. Use cópia nativa do sistema (ex.: `robocopy` no Windows, `rsync`/`cp -R` no Mac/Linux)
  com as exclusões acima — é instantâneo comparado ao backup antigo pelo app.

## Passo 3 — Confira (obrigatório)

1. Conte arquivos na origem (com as mesmas exclusões) e no destino.
2. **Iguais** → backup íntegro. **Diferentes** → liste exatamente quais arquivos faltaram
   e avise que o backup ficou INCOMPLETO — não declare sucesso.

## Passo 4 — Resumo (formato fixo)

```
BACKUP DO OS ✅
Pasta: bkp/{AAAA-MM-DD_HH-MM}/
Arquivos copiados: {n} de {n}
Contextos incluídos: {lista}
```

## Passo 5 — Reporte pro painel do MeuOS (opcional, best-effort)

Se existir o arquivo `.meuos/agent-key` na raiz do OS, registre o backup (senão, pule
este passo em silêncio):

```
curl -s -X POST https://app.meuos.com.br/api/agentes/tools/backup \
  -H "Authorization: Bearer {conteudo de .meuos/agent-key}" \
  -H "Content-Type: application/json" \
  -d '{"status":"success","files_count":{n},"failed_count":{faltantes},"total_count":{total},"folder_path":"bkp/{AAAA-MM-DD_HH-MM}"}'
```

(Backup incompleto → `"status":"error"` + os números reais.) Deu certo → acrescente:
"Backup registrado no seu painel do MeuOS." Falhou → não trave; acrescente: "Não consegui
registrar no painel — gere uma chave nova no app (Tools → Backup do OS)."

## Avisos finais

- Se a pasta do OS estiver dentro de uma pasta sincronizada (Google Drive/OneDrive), diga:
  "A sincronização vai subir o backup pra nuvem automaticamente."
- Se NÃO estiver numa pasta sincronizada, avise: "Este backup é só local — considere manter
  a pasta do OS dentro do Drive/OneDrive pra ter cópia na nuvem."
- Nunca proponha apagar backups antigos. Se o usuário pedir pra apagar, confirme antes e
  apague SOMENTE a pasta de backup que ele nomear.
