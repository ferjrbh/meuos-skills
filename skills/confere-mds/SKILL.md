---
name: confere-mds
description: |
  [APOSENTADA] Esta skill foi fundida na skill `otimizar-os`. Nao use esta. Se voce disser
  "confere mds", "confere docs", "auditar documentacao", "docs batem com a realidade?" ou
  "docs drift", o agente deve invocar a skill `otimizar-os` (que agora faz Conferir + Otimizar
  num fluxo so). Mantida apenas como redirecionamento.
version: 2.0
context: meuos
user-invocable: false
author: Fernando Lúcio — Aion Group
homepage: https://www.meuos.com.br
---

# Confere MDs — APOSENTADA (fundida em `otimizar-os`)

A conferencia de documentos contra a realidade (código, banco, automações) agora faz parte da skill
**`otimizar-os`**, na **FASE A (Conferir)**.

**O que fazer:** invoque a skill **`otimizar-os`**. Se quiser SO conferir (sem compactar/organizar), use a
flag `--so-confere`. Os gatilhos antigos ("confere mds", "confere docs", "auditar documentacao", "docs batem
com a realidade?", "verificar documentacao", "docs drift") agora pertencem ao `otimizar-os`.

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group
