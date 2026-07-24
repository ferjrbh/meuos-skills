# MeuOS — Biblioteca de Skills

> Skills oficiais do **MeuOS** para o seu Claude Code: organize seu OS pessoal, crie conteúdo,
> faça growth, automação e produtividade — cada uma pronta para instalar em segundos.

[![skills](https://img.shields.io/badge/skills-49-D95C1A?style=flat-square)](https://www.meuos.com.br)
[![feito para](https://img.shields.io/badge/feito_para-Claude_Code-1A2B4A?style=flat-square)](https://claude.com/claude-code)
[![MeuOS](https://img.shields.io/badge/MeuOS-meuos.com.br-D95C1A?style=flat-square)](https://www.meuos.com.br)

---

## O que é isto

O **MeuOS** é um sistema operacional pessoal para gestores e empreendedores que trabalham com IA.
Este repositório é a **biblioteca oficial de skills** — habilidades que ensinam o seu agente a
executar tarefas no padrão MeuOS, da organização do seu conhecimento à criação de propostas,
slides, conteúdo e automações.

Cada skill é um único arquivo **`SKILL.md`** (instruções + gatilhos de ativação). É leve,
portátil e funciona com qualquer ferramenta de IA que leia skills.

## Como funciona

Quando você instala uma skill na pasta de skills do seu agente (`~/.claude/skills/` no Claude Code),
o Claude lê a descrição dela e a **ativa sozinho** assim que você pede algo relacionado — você não
precisa "chamar" a skill, só descrever a tarefa em linguagem natural.

## Agentes suportados

As skills são markdown puro — funcionam com os **dois cérebros** que o MeuOS suporta:

| Agente | Onde a skill é instalada | Como ativa |
|---|---|---|
| **Claude** (Claude Code/Desktop, VSCode, Cursor…) | `~/.claude/skills/{slug}/SKILL.md` | automático — o Claude lê a descrição e ativa quando o tema surge |
| **ChatGPT** (app Codex, CLI, OpenClaw) | `.meuos/skills/{slug}/SKILL.md` na pasta do OS + linha de referência na seção "## Skills instaladas" do `AGENTS.md` | o agente lê a skill quando o AGENTS.md aponta pra ela |

A aba **Skills** do MeuOS gera o prompt de instalação certo pros dois — é só copiar e colar no seu agente.

> ⚠️ Exceções: `otimizar-custo` depende da memória do Claude Code (`MEMORY.md`) e **não se aplica ao ChatGPT**.
> Skills que editam o arquivo de entrada do OS (`fim-do-dia`, `otimizar-os`) **espelham a mudança na entrada irmã** (claude.md ↔ AGENTS.md) — regra dual-agent.

## Requisitos

- **Claude Code** (app Desktop) ou **app ChatGPT** (modo Codex) — qualquer um dos dois.
- Funciona também em VSCode, Cursor, OpenClaw e outros agentes que leiam as pastas acima.

## Como instalar

**Pelo app (mais fácil):** na aba **Skills** do [MeuOS](https://www.meuos.com.br), cada skill tem um
botão que copia o prompt de instalação pronto.

**Manual:** cole o prompt abaixo no seu Claude Code, trocando `{NOME}` e `{slug}` pela skill desejada
(o `{slug}` é o nome da pasta em [`skills/`](skills/)):

```
Instale a skill {NOME} do MeuOS. Baixe o conteúdo de
https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/{slug}/SKILL.md
e salve como SKILL.md na pasta de skills do seu agente (você sabe onde elas ficam). Crie a pasta
se não existir e confirme ao terminar.
```

> A versão de cada skill fica no frontmatter do próprio `SKILL.md`. No app, a aba Skills avisa
> quando há atualização.

---

## Catálogo

### 🧩 Core — rode primeiro (6)
Os ritos essenciais do MeuOS. Comece pela **MeuOS do Zero**.

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[MeuOS do Zero](skills/meuos-do-zero/SKILL.md)** | Monta, conserta e organiza seu OS do zero | *"meuos do zero"*, *"configurar meu os"* |
| **[Importar dados do GPT](skills/importar-dados-gpt/SKILL.md)** | Migra o conhecimento das suas conversas do ChatGPT/Gemini pro OS, destilando por contexto | *"importar do chatgpt"*, *"migrar do gpt"* |
| **[Fim do Dia](skills/fim-do-dia/SKILL.md)** | Fecha a sessão: sintetiza, captura aprendizados e atualiza os docs | *"fim do dia"*, *"vamos fechar"* |
| **[Otimizar OS](skills/otimizar-os/SKILL.md)** | Confere seus docs contra a realidade (código/banco/automações) **e** compacta/organiza — num fluxo só | *"otimizar os"*, *"confere mds"*, *"docs batem com a realidade?"*, *"limpar terreno"* |
| **[Otimizar Custo](skills/otimizar-custo/SKILL.md)** | Reduz o custo de tokens higienizando a memória do agente | *"otimizar custo"*, *"otimizar memória"* |
| **[Conferir Entrega](skills/conferir-entrega/SKILL.md)** | Checa tudo antes de declarar uma tarefa concluída | *"conferir entrega"*, *"terminei"* |

### 📊 Apresentações (3)

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Criar Apresentação](skills/criar-apresentacao/SKILL.md)** | Monta um deck completo (HTML ou PPTX) a partir do seu modelo | *"criar apresentação"*, *"montar slides"* |
| **[Criar Modelo de Apresentação](skills/criar-modelo-apresentacao/SKILL.md)** | Cria seu padrão visual de slides (35 layouts) com a sua marca | *"criar template de slides"* |
| **[PowerPoint (.pptx)](skills/pptx/SKILL.md)** | Cria e edita apresentações PPTX reais e editáveis | *"powerpoint"*, *"pptx"* |

### 📄 Office (4)

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Word (.docx)](skills/docx/SKILL.md)** | Cria e edita documentos Word editáveis | *"word"*, *"docx"* |
| **[Excel (.xlsx)](skills/xlsx/SKILL.md)** | Cria, edita e analisa planilhas com fórmulas e abas | *"excel"*, *"planilha"* |
| **[PDF](skills/pdf/SKILL.md)** | Cria, edita e extrai dados de PDFs | *"pdf"*, *"extrair pdf"* |
| **[Gera HTML to PDF](skills/gera-html-to-pdf/SKILL.md)** | Documentos longos em PDF A4 perfeito (propostas, dossiês, lâminas) | *"html para pdf"*, *"criar proposta"* |

### 📈 Growth (18)

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Growth — Product Context](skills/growth-context/SKILL.md)** | Cria o contexto-mestre de marketing (alimenta as demais) | *"contexto de marketing"* |
| **[Redator de Blog SEO](skills/redator-blog-seo/SKILL.md)** | Posts pra rankear no Google e ser citado por IA | *"escrever post de blog"*, *"artigo pra rankear"* |
| **[Growth — SEO Audit](skills/growth-seo-audit/SKILL.md)** | Auditoria de SEO técnico e on-page, com prioridades | *"auditoria de seo"* |
| **[Growth — AI SEO](skills/growth-ai-seo/SKILL.md)** | Otimiza pra aparecer no ChatGPT, Claude e Perplexity | *"ai seo"*, *"aparecer no chatgpt"* |
| **[Growth — Programmatic SEO](skills/growth-programmatic-seo/SKILL.md)** | Páginas em escala pra capturar long-tail | *"programmatic seo"* |
| **[Growth — Schema.org](skills/growth-schema/SKILL.md)** | Schema.org pra rich snippets, com código pronto | *"schema"*, *"rich snippets"* |
| **[Growth — Site Architecture](skills/growth-site-arch/SKILL.md)** | Arquitetura de site pra SEO e conversão | *"arquitetura de site"* |
| **[Growth — Page CRO](skills/growth-page-cro/SKILL.md)** | Plano CRO de página com experimentos A/B priorizados | *"otimizar conversão da página"* |
| **[Growth — Form CRO](skills/growth-form-cro/SKILL.md)** | Otimiza formulários pra converter mais | *"otimizar formulário"* |
| **[Growth — Signup CRO](skills/growth-signup-cro/SKILL.md)** | Maximiza cadastros completos no signup | *"otimizar signup"* |
| **[Growth — Onboarding CRO](skills/growth-onboarding-cro/SKILL.md)** | Reduz time-to-value e abandono no onboarding | *"otimizar onboarding"* |
| **[Growth — Paywall CRO](skills/growth-paywall-cro/SKILL.md)** | Otimiza paywall (copy, timing, pricing display) | *"otimizar paywall"* |
| **[Growth — Popup CRO](skills/growth-popup-cro/SKILL.md)** | Popups que convertem sem irritar | *"popup que converte"* |
| **[Growth — Pricing](skills/growth-pricing/SKILL.md)** | Estratégia de pricing (modelo, ancoragem, página) | *"estratégia de preço"* |
| **[Growth — Churn](skills/growth-churn/SKILL.md)** | Analisa e reduz churn, com fluxos de retenção | *"reduzir churn"* |
| **[Growth — Referral](skills/growth-referral/SKILL.md)** | Programa de indicação (loop viral) | *"programa de indicação"* |
| **[Growth — Lead Magnets](skills/growth-lead-magnets/SKILL.md)** | Iscas de captura (ebook, checklist) + nurturing | *"lead magnet"*, *"isca"* |
| **[Growth — Free Tool](skills/growth-free-tool/SKILL.md)** | Ferramenta grátis como isca de captação | *"ferramenta gratuita isca"* |

### 🎯 Marketing (10)

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Market Suite](skills/market/SKILL.md)** | Suíte completa de marketing com IA | *"marketing completo"* |
| **[Market Brand](skills/market-brand/SKILL.md)** | Identidade da marca: posicionamento, tom, personas | *"brand book"*, *"identidade da marca"* |
| **[Market Copy](skills/market-copy/SKILL.md)** | Copy de conversão pra qualquer página | *"copy"*, *"headline"* |
| **[Market Ads](skills/market-ads/SKILL.md)** | Criativos e copy de ads (Meta, Google, LinkedIn) | *"anúncios"*, *"ads"* |
| **[Market Emails](skills/market-emails/SKILL.md)** | Sequências de email (nurturing, lançamento, venda) | *"sequência de email"* |
| **[Market Social](skills/market-social/SKILL.md)** | Calendário de conteúdo pra redes sociais | *"calendário de conteúdo"* |
| **[Market Funnel](skills/market-funnel/SKILL.md)** | Analisa e otimiza o funil de vendas | *"otimizar funil"* |
| **[Market Landing](skills/market-landing/SKILL.md)** | Análise CRO de landing page | *"analisar landing"* |
| **[Market Launch](skills/market-launch/SKILL.md)** | Playbook completo de lançamento de produto | *"lançamento de produto"* |
| **[Market Competitors](skills/market-competitors/SKILL.md)** | Análise competitiva e identificação de gaps | *"análise de concorrentes"* |

### 🛠️ Lovable (2)

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Lovable Prompt Master](skills/lovable-prompt-master/SKILL.md)** | Prompts prontos pro Lovable construir apps web | *"prompt pro lovable"* |
| **[Design to Prompt](skills/design-to-prompt/SKILL.md)** | Transforma um design (Figma/print) em prompt de tela | *"design to prompt"* |

### 🧠 Produtividade (2)

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Structured Thinking](skills/structured-thinking/SKILL.md)** | Exploração estruturada antes de tarefas complexas | *"pensar estruturado"* |
| **[Systematic Debugging](skills/systematic-debugging/SKILL.md)** | Método sistemático pra debugar problemas | *"debugar"*, *"systematic debugging"* |

### 🔌 n8n (3)

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Conectar n8n](skills/conectar-n8n/SKILL.md)** | Claude cria, edita e debuga workflows n8n via API REST | *"conectar n8n"* |
| **[n8n AI Agents & RAG](skills/n8n-ai-rag/SKILL.md)** | Agentes de IA e workflows RAG no n8n | *"rag no n8n"*, *"agente n8n"* |
| **[n8n Skills (Patterns & Code)](skills/n8n-skills/SKILL.md)** | Patterns canônicos, Code node e expressões do n8n | *"n8n skills"*, *"patterns n8n"* |

### 🚀 Avançado — exclusiva dos tiers Presencial e Corp (1)

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Criar Skill](skills/criar-skill/SKILL.md)** | Transforma uma tarefa sua num procedimento reutilizável do agente — o POP do seu agente, com entrevista, template, teste e instalação dual | *"criar skill"*, *"transformar isso em skill"* |

---

## Como atualizar

As skills evoluem. Para pegar a versão nova, rode o mesmo prompt de instalação — ele sobrescreve com
a última versão do GitHub. No app, a aba **Skills** mostra quando há atualização disponível.

## Crie a sua própria skill

Uma skill é um único `SKILL.md` com frontmatter (metadados) + instruções em markdown:

```markdown
---
name: Minha Skill
description: O que ela faz e quando deve ser ativada — o Claude usa isto para decidir sozinho.
---

# Minha Skill

Passo a passo que o agente deve seguir...
```

Salve em `~/.claude/skills/minha-skill/SKILL.md` e pronto — o Claude já a reconhece.

## Aprenda mais

Para dominar o modelo MeuOS, entrar na comunidade e manter suas skills sempre atualizadas, faça o
curso em **[www.meuos.com.br](https://www.meuos.com.br)**.

## Licença

Conteúdo **proprietário do MeuOS** — uso livre para alunos, proibida a redistribuição ou revenda.
Veja **[LICENSE](LICENSE.md)**. Dúvidas e acesso: [www.meuos.com.br](https://www.meuos.com.br).

---

_Biblioteca oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)_
