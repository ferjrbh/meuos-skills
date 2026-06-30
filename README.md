# MeuOS - Biblioteca de Skills

Skills oficiais do MeuOS para alunos. Cada skill e um `SKILL.md` pronto pro **Claude Code**.

## Como instalar

Copie o **prompt** da skill que quer (abaixo) e cole no seu Claude Code. Ele baixa do GitHub e instala em `~/.claude/skills/`.

**Total: 47 skills.**

---

## Core (obrigatorias) (5)

### MeuOS do Zero  `v1.0`
Monta, conserta e organiza seu OS do ZERO — pra quem esta chegando ao modelo MeuOS ou instalou algo errado. Roda na pasta atual (confirma se e a certa), escaneia o que existe, infere seus contextos e confirma com voce, e cria/repara a estrutura canonica (claude.md, soul.md, guia_do_os.md + contextos com documento_mestre/aprendizados/changelog/index) com os templates oficiais. Nao-destrutiva. E a primeira skill a rodar.

*Gatilhos:* meuos do zero, configurar meu os, comecar meu os, montar meu os, instalei errado, meu os ta baguncado, nao tenho os ainda, organizar meu os do zero, consertar minha instalacao, setup do os, arrumar meu os

[Ver SKILL.md](skills/meuos-do-zero/SKILL.md)

```
Instale a skill **MeuOS do Zero** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/meuos-do-zero/SKILL.md` e salve em `~/.claude/skills/meuos-do-zero/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Conferir Entrega  `v1.0`
Verificacao rapida antes de declarar qualquer tarefa concluida. O agente ativa automaticamente ao perceber que algo foi concluido. Garante que nada foi esquecido, o OS esta atualizado e dados sensiveis estao protegidos.

*Gatilhos:* conferir entrega, verificar entrega, pronto, terminei, conclui, feito, pode fechar, entregue, finalizado

[Ver SKILL.md](skills/conferir-entrega/SKILL.md)

```
Instale a skill **Conferir Entrega** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/conferir-entrega/SKILL.md` e salve em `~/.claude/skills/conferir-entrega/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Fim do Dia  `v4.1`
Rotina de encerramento do dia em menos de 10 minutos. NOVO: o agente agora SINTETIZA a sessao em 3 blocos (o que fizemos / o que aprendemos / o que fica pra amanha) e voce so CONFIRMA ou ajusta — sem responder 3 perguntas abertas. Prevê sessoes vazias (sem aprendizado novo, sem pendencias) e nao forca registro artificial.

*Gatilhos:* fim do dia, encerrar, fechar o dia, fim de sessao, fim de trabalho, vamos fechar, pode fechar, encerra ai, wrap-up, encerrar sessao, revisao diaria, sintese do dia, sintese da sessao

[Ver SKILL.md](skills/fim-do-dia/SKILL.md)

```
Instale a skill **Fim do Dia** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/fim-do-dia/SKILL.md` e salve em `~/.claude/skills/fim-do-dia/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Otimizar Custo  `v2.1`
Reduz o custo de tokens das suas sessoes com Claude Code higienizando a memoria do agente. Voce paga tokens do MEMORY.md em toda conversa — cada linha e cobrada em TODA mensagem. Esta skill identifica o que pode ser limpo, calcula a economia em R$/mes e executa apenas com sua aprovacao. Tipico: reducao de 60-65% no MEMORY.md, com economia mensal real (ate ~R$ 285/mes em uso intenso).

*Gatilhos:* otimizar custo, reduzir custo, economizar tokens, otimizar memoria, limpar memoria, higienizar memoria, memoria do claude, revisar memoria, memoria do agente, auditar memoria, reduzir tokens, memoria gorda, claude esta caro

[Ver SKILL.md](skills/otimizar-custo/SKILL.md)

```
Instale a skill **Otimizar Custo** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/otimizar-custo/SKILL.md` e salve em `~/.claude/skills/otimizar-custo/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Otimizar OS  `v4.1`
Organiza e compacta os arquivos de UM contexto escolhido (nao mais o OS inteiro de uma vez). NOVO: (1) faz BACKUP da memoria do Claude Code antes de qualquer scan — protege contra perda de maquina; (2) CACA MDs ORFAOS (arquivos sem ponteiro no INDEX/MESTRE) e propoe vinculacao; (3) escopo por contexto pergunta antes de rodar. Continua executando so com sua aprovacao.

*Gatilhos:* otimizar os, organizar arquivos, arquivos grandes, compactar docs, higienizar, limpar documentos, doc-compactor, reduzir arquivos, arquivos crescendo, limpar terreno, organizar contexto, mds orfaos, backup memoria

[Ver SKILL.md](skills/otimizar-os/SKILL.md)

```
Instale a skill **Otimizar OS** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/otimizar-os/SKILL.md` e salve em `~/.claude/skills/otimizar-os/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

---

## Biblioteca (39)

### Criar Apresentacao  `v1.2` - `apresentacoes`
Monta uma apresentacao completa (HTML navegavel ou arquivo PPTX) a partir de um modelo visual previamente criado + o conteudo que voce informar. Entrevista, sugere estrutura narrativa, gera e valida.

*Gatilhos:* criar apresentacao, montar slides, fazer uma apresentacao, criar slides, novo deck, montar deck, montar ppt, criar ppt, precisa de slides, apresentacao sobre, slides sobre

[Ver SKILL.md](skills/criar-apresentacao/SKILL.md)

```
Instale a skill **Criar Apresentacao** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/criar-apresentacao/SKILL.md` e salve em `~/.claude/skills/criar-apresentacao/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Criar Modelo de Apresentacao  `v1.4` - `apresentacoes`
Cria o padrao visual de apresentacao do usuario — pacote com 35 layouts prontos (capa, indice, conteudo, fotos, graficos, timeline, comparacao, pricing, CTA, encerramento) usando as cores, fonte e logo do usuario. O modelo gerado vira fonte de verdade da skill Criar Apresentacao.

*Gatilhos:* criar modelo de apresentacao, criar padrao de slides, criar template de slides, meu modelo visual, padrao visual para apresentacoes, template de apresentacao, design system de slides, modelo de ppt, modelo para slides

[Ver SKILL.md](skills/criar-modelo-apresentacao/SKILL.md)

```
Instale a skill **Criar Modelo de Apresentacao** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/criar-modelo-apresentacao/SKILL.md` e salve em `~/.claude/skills/criar-modelo-apresentacao/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Design to Prompt  `v1.0` - `lovable`
Transforma um design (Figma, screenshot) em prompt preciso para IA construir a tela. Extrai layout, cores e componentes.

[Ver SKILL.md](skills/design-to-prompt/SKILL.md)

```
Instale a skill **Design to Prompt** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/design-to-prompt/SKILL.md` e salve em `~/.claude/skills/design-to-prompt/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Excel (.xlsx)  `v1.2` - `office`
Cria, edita e analisa planilhas Excel. Fórmulas, formatação e múltiplas abas — pronto para enviar a cliente.

[Ver SKILL.md](skills/xlsx/SKILL.md)

```
Instale a skill **Excel (.xlsx)** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/xlsx/SKILL.md` e salve em `~/.claude/skills/xlsx/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Gera HTML to PDF  `v1.0` - `office`
Cria documentos longos em HTML que viram PDFs A4 perfeitos — propostas, lâminas, dossiês, relatórios. Resolve o problema clássico do PDF estourando (título numa página e texto na seguinte, tabela cortada no meio, foto cortando rosto, signature jogada em página vazia). A regra central: cada <div class="page"> é UMA página A4 inteira pré-calibrada pelo agente. Navegador não decide — só renderiza.

*Gatilhos:* gera html to pdf, gerar html to pdf, criar proposta, documento html para pdf, lamina do produto, white paper, dossie, curriculo bonito, relatorio em pdf, criar template de doc longo, minha proposta ta saindo torta no pdf, pdf ta quebrando, como fazer pdf que nao estoura, html para pdf, documento longo

[Ver SKILL.md](skills/gera-html-to-pdf/SKILL.md)

```
Instale a skill **Gera HTML to PDF** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/gera-html-to-pdf/SKILL.md` e salve em `~/.claude/skills/gera-html-to-pdf/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — AI SEO  `v1.0` - `growth`
Otimiza seu site para aparecer no ChatGPT, Claude e Perplexity. Ajusta estrutura, conteúdo e citação para LLMs te referenciarem.

[Ver SKILL.md](skills/growth-ai-seo/SKILL.md)

```
Instale a skill **Growth — AI SEO** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-ai-seo/SKILL.md` e salve em `~/.claude/skills/growth-ai-seo/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Churn  `v1.0` - `growth`
Analisa e reduz churn. Identifica momentos críticos de perda, sugere intervenções e cria fluxos de retenção.

[Ver SKILL.md](skills/growth-churn/SKILL.md)

```
Instale a skill **Growth — Churn** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-churn/SKILL.md` e salve em `~/.claude/skills/growth-churn/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Form CRO  `v1.0` - `growth`
Otimiza formulários para aumentar conversão. Reduz fricção, melhora copy dos campos e sugere ordem e obrigatoriedade.

[Ver SKILL.md](skills/growth-form-cro/SKILL.md)

```
Instale a skill **Growth — Form CRO** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-form-cro/SKILL.md` e salve em `~/.claude/skills/growth-form-cro/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Free Tool  `v1.0` - `growth`
Desenha ferramenta gratuita como isca. Escopo, UX, captura de lead e fluxo pós-uso para converter em cliente pagante.

[Ver SKILL.md](skills/growth-free-tool/SKILL.md)

```
Instale a skill **Growth — Free Tool** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-free-tool/SKILL.md` e salve em `~/.claude/skills/growth-free-tool/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Lead Magnets  `v1.0` - `growth`
Gera iscas de captura (ebook, checklist, template). Tema, formato, landing page e sequência de nurturing pós-download.

[Ver SKILL.md](skills/growth-lead-magnets/SKILL.md)

```
Instale a skill **Growth — Lead Magnets** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-lead-magnets/SKILL.md` e salve em `~/.claude/skills/growth-lead-magnets/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Onboarding CRO  `v1.0` - `growth`
Otimiza onboarding de produto. Reduz time-to-value, identifica pontos de abandono e desenha o aha moment.

[Ver SKILL.md](skills/growth-onboarding-cro/SKILL.md)

```
Instale a skill **Growth — Onboarding CRO** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-onboarding-cro/SKILL.md` e salve em `~/.claude/skills/growth-onboarding-cro/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Page CRO  `v1.0` - `growth`
Plano CRO completo para uma página com experimentos A/B priorizados por impacto/esforço. Vai além de análise rápida.

[Ver SKILL.md](skills/growth-page-cro/SKILL.md)

```
Instale a skill **Growth — Page CRO** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-page-cro/SKILL.md` e salve em `~/.claude/skills/growth-page-cro/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Paywall CRO  `v1.0` - `growth`
Otimiza paywall de SaaS, conteúdo ou app. Copy, posicionamento, timing e pricing display para maximizar conversão.

[Ver SKILL.md](skills/growth-paywall-cro/SKILL.md)

```
Instale a skill **Growth — Paywall CRO** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-paywall-cro/SKILL.md` e salve em `~/.claude/skills/growth-paywall-cro/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Popup CRO  `v1.0` - `growth`
Desenha popups que convertem sem irritar. Trigger, copy, timing e segmentação — de exit-intent a captura contextual.

[Ver SKILL.md](skills/growth-popup-cro/SKILL.md)

```
Instale a skill **Growth — Popup CRO** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-popup-cro/SKILL.md` e salve em `~/.claude/skills/growth-popup-cro/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Pricing  `v1.0` - `growth`
Estratégia de pricing. Modelo (freemium, tiers, usage), ancoragem, página de preços e teste sem quebrar a base atual.

[Ver SKILL.md](skills/growth-pricing/SKILL.md)

```
Instale a skill **Growth — Pricing** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-pricing/SKILL.md` e salve em `~/.claude/skills/growth-pricing/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Product Context  `v1.0` - `growth`
Cria o contexto mestre de marketing do produto (personas, posicionamento, ICPs). Documento que alimenta todas as outras skills growth.

[Ver SKILL.md](skills/growth-context/SKILL.md)

```
Instale a skill **Growth — Product Context** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-context/SKILL.md` e salve em `~/.claude/skills/growth-context/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Programmatic SEO  `v1.0` - `growth`
Cria páginas em escala para capturar long-tail SEO. Estrutura template, fontes de dados e publicação automática.

[Ver SKILL.md](skills/growth-programmatic-seo/SKILL.md)

```
Instale a skill **Growth — Programmatic SEO** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-programmatic-seo/SKILL.md` e salve em `~/.claude/skills/growth-programmatic-seo/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Referral  `v1.0` - `growth`
Programa de indicação (referral). Incentivos, mecânica, fluxo e integração com onboarding para gerar loop viral.

[Ver SKILL.md](skills/growth-referral/SKILL.md)

```
Instale a skill **Growth — Referral** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-referral/SKILL.md` e salve em `~/.claude/skills/growth-referral/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — SEO Audit  `v1.0` - `growth`
Auditoria completa de SEO técnico e on-page. Indexação, core web vitals, meta tags — e prioriza as correções.

[Ver SKILL.md](skills/growth-seo-audit/SKILL.md)

```
Instale a skill **Growth — SEO Audit** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-seo-audit/SKILL.md` e salve em `~/.claude/skills/growth-seo-audit/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Schema.org  `v1.0` - `growth`
Adiciona schema.org no seu site para rich snippets no Google. FAQ, Product, Article, Organization — com código pronto.

[Ver SKILL.md](skills/growth-schema/SKILL.md)

```
Instale a skill **Growth — Schema.org** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-schema/SKILL.md` e salve em `~/.claude/skills/growth-schema/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Signup CRO  `v1.0` - `growth`
Otimiza fluxo de signup para maximizar cadastros completos. Campos, clareza de valor, social auth e recuperação de abandono.

[Ver SKILL.md](skills/growth-signup-cro/SKILL.md)

```
Instale a skill **Growth — Signup CRO** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-signup-cro/SKILL.md` e salve em `~/.claude/skills/growth-signup-cro/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Growth — Site Architecture  `v1.0` - `growth`
Arquitetura de site/SaaS pensada para SEO e conversão. Hierarquia, silos de conteúdo, internal linking e navegação.

[Ver SKILL.md](skills/growth-site-arch/SKILL.md)

```
Instale a skill **Growth — Site Architecture** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/growth-site-arch/SKILL.md` e salve em `~/.claude/skills/growth-site-arch/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Redator de Blog SEO  `v1.0` - `growth`
Escreve posts de blog otimizados para o Google E para citacao por IA (ChatGPT, Perplexity, AI Overviews): estrutura answer-first, autor com sinais reais de E-E-A-T, dado proprio com fonte nomeada, FAQ util, schema honesto e links internos semanticos. Le o contexto da marca pelo ponteiro no claude.md/index.md do OS (`{contexto}/marketing.md`; fallback `.agents/`) e orquestra growth-seo-audit, growth-site-arch, growth-schema, growth-ai-seo e market-brand.

*Gatilhos:* escrever post de blog, redigir artigo pro site, post de SEO, artigo pra rankear, escrever pra aparecer no ChatGPT/Google, pauta do blog, blog post, conteudo de blog

[Ver SKILL.md](skills/redator-blog-seo/SKILL.md)

```
Instale a skill **Redator de Blog SEO** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/redator-blog-seo/SKILL.md` e salve em `~/.claude/skills/redator-blog-seo/SKILL.md`; baixe tambem `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/redator-blog-seo/references/seo-geo-2026.md` e salve em `~/.claude/skills/redator-blog-seo/references/seo-geo-2026.md` (crie as pastas se nao existirem). Confirme a instalacao ao terminar.
```

### Lovable Prompt Master  `v1.0` - `lovable`
Gera prompts prontos para o Lovable construir apps web. Estrutura stack, features, auth e banco — cola no Lovable e ele constrói.

[Ver SKILL.md](skills/lovable-prompt-master/SKILL.md)

```
Instale a skill **Lovable Prompt Master** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/lovable-prompt-master/SKILL.md` e salve em `~/.claude/skills/lovable-prompt-master/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Market Ads  `v1.0` - `marketing`
Gera criativos e copy para ads (Meta, Google, LinkedIn). Headline, descrição, CTA e variantes A/B prontos para subir.

[Ver SKILL.md](skills/market-ads/SKILL.md)

```
Instale a skill **Market Ads** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/market-ads/SKILL.md` e salve em `~/.claude/skills/market-ads/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Market Brand  `v1.0` - `marketing`
Define identidade da marca: posicionamento, tom de voz, personas e mensagens-chave. Gera brand book em markdown.

[Ver SKILL.md](skills/market-brand/SKILL.md)

```
Instale a skill **Market Brand** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/market-brand/SKILL.md` e salve em `~/.claude/skills/market-brand/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Market Competitors  `v1.0` - `marketing`
Análise competitiva automática. Lista concorrentes, compara copy/pricing/features e identifica gaps para você se diferenciar.

[Ver SKILL.md](skills/market-competitors/SKILL.md)

```
Instale a skill **Market Competitors** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/market-competitors/SKILL.md` e salve em `~/.claude/skills/market-competitors/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Market Copy  `v1.0` - `marketing`
Gera copy otimizada para qualquer página. Headline, CTA, bullet e social proof — seguindo frameworks validados de conversão.

[Ver SKILL.md](skills/market-copy/SKILL.md)

```
Instale a skill **Market Copy** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/market-copy/SKILL.md` e salve em `~/.claude/skills/market-copy/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Market Emails  `v1.0` - `marketing`
Gera sequência de emails (nurturing, lançamento, venda). Assunto, preview e corpo com frameworks de copywriting validados.

[Ver SKILL.md](skills/market-emails/SKILL.md)

```
Instale a skill **Market Emails** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/market-emails/SKILL.md` e salve em `~/.claude/skills/market-emails/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Market Funnel  `v1.0` - `marketing`
Analisa e otimiza funil de vendas. Mapeia estágios, identifica onde perde cliente e sugere correções por etapa.

[Ver SKILL.md](skills/market-funnel/SKILL.md)

```
Instale a skill **Market Funnel** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/market-funnel/SKILL.md` e salve em `~/.claude/skills/market-funnel/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Market Landing  `v1.0` - `marketing`
Análise CRO de landing page. Identifica gargalos de conversão e sugere melhorias em copy, layout e prova social.

[Ver SKILL.md](skills/market-landing/SKILL.md)

```
Instale a skill **Market Landing** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/market-landing/SKILL.md` e salve em `~/.claude/skills/market-landing/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Market Launch  `v1.0` - `marketing`
Gera playbook completo de lançamento de produto. Timeline, canais, copy e métricas — do pre-launch ao pós-lançamento.

[Ver SKILL.md](skills/market-launch/SKILL.md)

```
Instale a skill **Market Launch** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/market-launch/SKILL.md` e salve em `~/.claude/skills/market-launch/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Market Social  `v1.0` - `marketing`
Gera calendário completo de conteúdo para redes sociais. Posts, carrosséis e reels formatados por plataforma.

[Ver SKILL.md](skills/market-social/SKILL.md)

```
Instale a skill **Market Social** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/market-social/SKILL.md` e salve em `~/.claude/skills/market-social/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Market Suite  `v1.2` - `marketing`
Suite completa de marketing com IA. Auditoria de site, geração de copy, emails, social, ads e proposta comercial — tudo em markdown.

[Ver SKILL.md](skills/market/SKILL.md)

```
Instale a skill **Market Suite** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/market/SKILL.md` e salve em `~/.claude/skills/market/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### PDF  `v1.2` - `office`
Cria, edita e extrai dados de PDFs. Gera relatório formatado, preenche formulário, extrai texto de contrato — sem conversão manual.

[Ver SKILL.md](skills/pdf/SKILL.md)

```
Instale a skill **PDF** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/pdf/SKILL.md` e salve em `~/.claude/skills/pdf/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### PowerPoint (.pptx)  `v1.2` - `apresentacoes`
Cria, edita e analisa apresentações PowerPoint. Gera slides reais editáveis, não só HTML para imprimir.

[Ver SKILL.md](skills/pptx/SKILL.md)

```
Instale a skill **PowerPoint (.pptx)** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/pptx/SKILL.md` e salve em `~/.claude/skills/pptx/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Structured Thinking  `v1.0`
Força exploração estruturada antes de executar tarefas complexas. Evita retrabalho em decisões com mais de um caminho possível.

[Ver SKILL.md](skills/structured-thinking/SKILL.md)

```
Instale a skill **Structured Thinking** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/structured-thinking/SKILL.md` e salve em `~/.claude/skills/structured-thinking/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Systematic Debugging  `v1.0`
Método sistemático para debugar problemas complexos. Reproduz o bug, isola a variável, testa hipótese — em vez de tentativa e erro.

[Ver SKILL.md](skills/systematic-debugging/SKILL.md)

```
Instale a skill **Systematic Debugging** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/systematic-debugging/SKILL.md` e salve em `~/.claude/skills/systematic-debugging/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### Word (.docx)  `v1.1` - `office`
Cria, edita e analisa documentos Word. Use para gerar proposta, contrato ou qualquer entregável em formato Word editável.

[Ver SKILL.md](skills/docx/SKILL.md)

```
Instale a skill **Word (.docx)** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/docx/SKILL.md` e salve em `~/.claude/skills/docx/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

---

## n8n (3)

### Conectar n8n  `v2.0`
Permite ao seu Claude criar, editar, ativar e debugar workflows direto na sua instancia n8n via API REST. Sem MCP, sem npx — so curl. Funciona em qualquer Claude (CLI, VSCode extension, Cursor, Desktop).

*Gatilhos:* n8n mcp, instalar n8n mcp, conectar n8n

[Ver SKILL.md](skills/conectar-n8n/SKILL.md)

```
Instale a skill **Conectar n8n** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/conectar-n8n/SKILL.md` e salve em `~/.claude/skills/conectar-n8n/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### n8n AI Agents & RAG  `v1.1`
Skill especializada pra construir agentes IA e workflows RAG no n8n: 11 connection types ai_*, topologia canonica RAG, multi-tool, memory com sessionIdType, output parsers structured/autofixing, MCP nativo do n8n.

*Gatilhos:* agente IA n8n, chatbot no n8n, RAG no n8n, vector store n8n, embeddings n8n

[Ver SKILL.md](skills/n8n-ai-rag/SKILL.md)

```
Instale a skill **n8n AI Agents & RAG** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/n8n-ai-rag/SKILL.md` e salve em `~/.claude/skills/n8n-ai-rag/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

### n8n Skills (Patterns, Code, Expressões)  `v3.0`
Compendio profundo pra desenhar workflows n8n: 5 patterns canonicos, configuracao operation-aware de nodes, Code node JavaScript e Python, sintaxe de expressoes. Complementa a skill "Conectar n8n". Sem dependencia de MCP.

*Gatilhos:* n8n skills, instalar n8n skills, skills n8n

[Ver SKILL.md](skills/n8n-skills/SKILL.md)

```
Instale a skill **n8n Skills (Patterns, Code, Expressões)** do MeuOS. Baixe `https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/n8n-skills/SKILL.md` e salve em `~/.claude/skills/n8n-skills/SKILL.md` (crie a pasta se nao existir). Confirme a instalacao ao terminar.
```

---


_Biblioteca oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)_
