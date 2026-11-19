# MeuOS — Biblioteca de Skills

> Skills oficiais do **MeuOS** para o seu Claude Code: organize seu OS pessoal, crie conteúdo,
> faça growth, automação e produtividade — cada uma pronta para instalar em segundos.

[![skills](https://img.shields.io/badge/skills-87-D95C1A?style=flat-square)](https://www.meuos.com.br)
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
> `copiloto` roda isolado no Claude Code (sem ver a conversa de quem fez a conta); no ChatGPT ele roda na mesma conversa e pede para você abrir uma conversa nova.
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

### 🧩 Core — rode primeiro (9)
Os ritos essenciais do MeuOS. Comece pela **MeuOS do Zero**.

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[MeuOS do Zero](skills/meuos-do-zero/SKILL.md)** | Monta, conserta e organiza seu OS do zero | *"meuos do zero"*, *"configurar meu os"* |
| **[Importar dados do GPT](skills/importar-dados-gpt/SKILL.md)** | Migra o conhecimento das suas conversas do ChatGPT/Gemini pro OS, destilando por contexto | *"importar do chatgpt"*, *"migrar do gpt"* |
| **[Fim do Dia](skills/fim-do-dia/SKILL.md)** | Fecha a sessão: sintetiza, captura aprendizados e atualiza os docs | *"fim do dia"*, *"vamos fechar"* |
| **[Otimizar OS](skills/otimizar-os/SKILL.md)** | Confere seus docs contra a realidade (código/banco/automações) **e** compacta/organiza — num fluxo só | *"otimizar os"*, *"confere mds"*, *"docs batem com a realidade?"*, *"limpar terreno"* |
| **[Otimizar Custo](skills/otimizar-custo/SKILL.md)** | Reduz o custo de tokens higienizando a memória do agente | *"otimizar custo"*, *"otimizar memória"* |
| **[Conferir Entrega](skills/conferir-entrega/SKILL.md)** | Checa tudo antes de declarar uma tarefa concluída | *"conferir entrega"*, *"terminei"* |
| **[Criar Skill](skills/criar-skill/SKILL.md)** | Transforma uma tarefa sua num procedimento reutilizável do agente: entrevista, template, teste e instalação | *"criar skill"*, *"transformar isso em skill"* |
| **[Avaliar Skill](skills/avaliar-skill/SKILL.md)** | Audita a qualidade e os riscos de uma skill (sua ou de terceiro) antes de instalar ou publicar: veredito APROVADA / USAR COM ATENÇÃO / REPROVADA, com os consertos priorizados | *"avalia essa skill"*, *"essa skill é segura?"*, *"posso instalar essa skill?"* |
| **[Buscar Skills Novas](skills/buscar-skills-novas/SKILL.md)** | Compara o catálogo do MeuOS com o que você tem instalado, confere a segurança de cada skill e instala só o que você aprovar | *"busca skills novas"*, *"tem skill nova?"*, *"atualiza minhas skills"* |

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

### 🎯 Marketing (14)

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
| **[Market Audit](skills/market-audit/SKILL.md)** | Auditoria completa do marketing a partir da URL, com nota e plano priorizado | *"auditoria de marketing"*, *"analisar meu site"* |
| **[Market Report](skills/market-report/SKILL.md)** | Compila as análises num relatório único, apresentável ao cliente ou à diretoria | *"relatório de marketing"*, *"compilar relatório"* |
| **[Market Proposal](skills/market-proposal/SKILL.md)** | Proposta comercial de marketing com escopo, preço em três níveis e projeção de retorno | *"proposta de marketing"*, *"proposta pro cliente"* |
| **[Multiplicador de Conteúdo](skills/multiplicador-de-conteudo/SKILL.md)** | Uma ideia vira post, carrossel, LinkedIn, blog, e-mail, roteiro de Reels e WhatsApp, entregues numa página HTML pronta pra copiar | *"multiplica esse conteúdo"*, *"transforma em vários formatos"* |

### 🛠️ Lovable e construção de apps (5)

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Lovable Prompt Master](skills/lovable-prompt-master/SKILL.md)** | Prompts prontos pro Lovable construir apps web | *"prompt pro lovable"* |
| **[Design to Prompt](skills/design-to-prompt/SKILL.md)** | Transforma um design (Figma/print) em prompt de tela | *"design to prompt"* |
| **[Especificar Antes de Construir](skills/especificar-antes-de-construir/SKILL.md)** | Ideia vira especificação completa antes de construir, com caminho mais simples, riscos e prompt pronto; fecha com crítico de segurança e crítico de UX | *"especificar antes de construir"*, *"montar a spec"* |
| **[Testar Meu App](skills/testar-meu-app/SKILL.md)** | Testa o seu app pelo navegador como um usuário faria e devolve o que quebrou, com prompt de correção | *"testa meu app"*, *"valida esse fluxo"* |
| **[Criador de Wireframe](skills/criador-wireframe/SKILL.md)** | Esboço de tela em HTML (computador e celular) antes de construir, com a sua marca | *"cria um wireframe"*, *"esboço da tela"* |

### 🧠 Produtividade e gestão (7)

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Structured Thinking](skills/structured-thinking/SKILL.md)** | Exploração estruturada antes de tarefas complexas | *"pensar estruturado"* |
| **[Systematic Debugging](skills/systematic-debugging/SKILL.md)** | Método sistemático pra debugar problemas | *"debugar"*, *"systematic debugging"* |
| **[Ata de Reunião](skills/ata-de-reuniao/SKILL.md)** | Transcrição ou anotação vira ata: decisões, ações com dono e prazo, pendências | *"faz a ata"*, *"ata da reunião"* |
| **[Resumo Executivo](skills/resumo-executivo/SKILL.md)** | Documento longo vira uma página de decisão: contexto, opções, recomendação e próximos passos | *"resumo executivo"*, *"resume pra decisão"* |
| **[Organiza Pra Mim](skills/organiza-pra-mim/SKILL.md)** | Arquivo ou anotação solta vai para a pasta certa do OS, com nome padrão e índice | *"organiza pra mim"*, *"guarda isso"* |
| **[Cartilha](skills/cartilha/SKILL.md)** | Tira o processo da sua cabeça e vira manual passo a passo que a equipe segue | *"cria uma cartilha"*, *"transforma em manual"* |
| **[Conversa Difícil](skills/conversa-dificil/SKILL.md)** | Roteiro para feedback, cobrança ou negociação, com ensaio | *"conversa difícil"*, *"como falo isso"* |

### 🔎 Análise e decisão (6)

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Comandante](skills/comandante/SKILL.md)** | Rotina de análise com evidência: contexto da empresa, plano de voo, base contada, conta por código, referência pública e cada número com endereço | *"comandante"*, *"plano de voo"* |
| **[Copiloto](skills/copiloto/SKILL.md)** | Confere um número do zero, sem ver a conta anterior, e revisa a peça inteira antes de ela sair: não sai, sai com correção ou pode sair | *"copiloto"*, *"confere esse número"*, *"posso mandar isso?"* |
| **[Raio-X de Processo](skills/raio-x-de-processo/SKILL.md)** | Mapeia um processo, conta as horas gastas por mês e mostra por onde começar a automatizar | *"raio-x do processo"*, *"o que automatizar primeiro"* |
| **[Ler Contrato](skills/ler-contrato/SKILL.md)** | Lê o contrato antes de assinar: prazos, multas e cláusulas de risco com o trecho exato (não substitui advogado) | *"lê esse contrato"*, *"posso assinar?"* |
| **[Decisão Difícil](skills/decisao-dificil/SKILL.md)** | Organiza opções, números e riscos de uma decisão e fecha com recomendação em 1 página | *"decisão difícil"*, *"me ajuda a decidir"* |
| **[Painel de Indicadores](skills/painel-de-indicadores/SKILL.md)** | Planilha vira painel visual com a sua marca, cada número com a conta mostrada | *"monta um painel"*, *"dashboard da planilha"* |

> O **Copiloto** tem 6 arquivos (instruções, catálogo, modelo de laudo e 3 scripts). Se você instalar só o `SKILL.md`, ele baixa o resto sozinho na primeira vez que rodar. Funciona sem Python: no Windows, faz as contas no PowerShell.

### 🧹 AI Slop: sobreviver à porcaria bem escrita (3)

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Filtro AI Slop](skills/filtro-ai-slop/SKILL.md)** | Antes de enviar: 7 perguntas e 4 testes, frases que você não sustentaria e semáforo verde, amarelo ou vermelho | *"passa no filtro"*, *"isso está pronto para mandar?"* |
| **[Triagem do que Chega](skills/triagem-do-que-chega/SKILL.md)** | Para quem recebe: o que pedem de você, fatos com fonte, o que falta e a devolução educada ao autor, sem reescrever o documento dele | *"triagem disso"*, *"o que esse documento quer de mim?"* |
| **[Política de Escrita com IA](skills/politica-de-escrita-com-ia/SKILL.md)** | Entrevista de 6 perguntas que monta a política da sua empresa em 1 página, com mensagem de lançamento e plano de 30 dias | *"criar política de IA da empresa"*, *"como evitar workslop no meu time"* |

### 🧭 Consultivo: do operacional ao consultivo (12)
Para o negócio que quer deixar de vender só execução e passar a vender orientação. As 3 marcadas com 🧾 deixam a decisão final com o contador ou o advogado.

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Diagnóstico e Proposta Consultiva](skills/diagnostico-e-proposta-consultiva/SKILL.md)** | Lê os números do cliente, aponta as 3 oportunidades que mais pesam e monta a proposta de assessoria | *"faz o diagnóstico desse cliente"*, *"monta uma proposta consultiva"* |
| **[Precificação e Reajuste](skills/precificacao-e-reajuste/SKILL.md)** | Margem por cliente, quem dá prejuízo, preço sugerido e a carta de reajuste | *"quais clientes dão prejuízo"*, *"escreve a carta de reajuste"* |
| **[Roteiro da Reunião com o Cliente](skills/roteiro-da-reuniao-com-o-cliente/SKILL.md)** | Pauta, os 5 números do período, 3 perguntas e o resumo com combinados | *"prepara a reunião com o cliente"*, *"pauta da reunião mensal"* |
| **[Conteúdo de Autoridade](skills/conteudo-de-autoridade/SKILL.md)** | Uma mudança do mercado vira artigo, post e comunicado à carteira, com fonte oficial | *"transforma isso em conteúdo"*, *"comunicado para os clientes"* |
| **[Onboarding do Cliente Premium](skills/onboarding-do-cliente-premium/SKILL.md)** | Checklist de entrada, diagnóstico inicial, plano de 90 dias e boas-vindas | *"fechei um cliente novo"*, *"plano dos primeiros 90 dias"* |
| **[Relatório Gerencial Comentado](skills/relatorio-gerencial-comentado/SKILL.md)** | Dois períodos de resultado viram uma página em linguagem de dono | *"me explica esse DRE"*, *"relatório do mês para o dono"* |
| **[Relatório de Achados](skills/relatorio-de-achados/SKILL.md)** | Achados de qualquer revisão com evidência, risco, recomendação e plano de ação | *"organiza esses achados"*, *"relatório da auditoria"* |
| **[Proposta de Projeto](skills/proposta-de-projeto/SKILL.md)** | Escopo com o que fica de fora, cronograma e preço pelas horas, com a conta aberta | *"monta uma proposta de projeto"*, *"quanto cobro por esse projeto"* |
| **[Due Diligence Simplificada](skills/due-diligence-simplificada/SKILL.md)** 🧾 | Checagem antes de comprar, vender ou receber sócio: documentos, semáforo por área e o que negociar | *"vou comprar uma empresa"*, *"vai entrar um sócio"* |
| **[Impacto da Reforma Tributária](skills/impacto-da-reforma-tributaria/SKILL.md)** 🧾 | Ficha do impacto do IBS e da CBS na empresa, com fonte oficial e perguntas para o contador | *"como a reforma afeta minha empresa"* |
| **[Planejamento Tributário Comparativo](skills/planejamento-tributario-comparativo/SKILL.md)** 🧾 | Quadro dos regimes possíveis com os números da empresa, para a decisão com o contador | *"qual o melhor regime para minha empresa"* |
| **[Proposta de BPO Financeiro](skills/proposta-de-bpo-financeiro/SKILL.md)** | Para escritório contábil: pacote, horas, preço e responsabilidades do BPO financeiro | *"proposta de BPO financeiro"* |

### 🔌 n8n (3)

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[Conectar n8n](skills/conectar-n8n/SKILL.md)** | Claude cria, edita e debuga workflows n8n via API REST | *"conectar n8n"* |
| **[n8n AI Agents & RAG](skills/n8n-ai-rag/SKILL.md)** | Agentes de IA e workflows RAG no n8n | *"rag no n8n"*, *"agente n8n"* |
| **[n8n Skills (Patterns & Code)](skills/n8n-skills/SKILL.md)** | Patterns canônicos, Code node e expressões do n8n | *"n8n skills"*, *"patterns n8n"* |

---

## Como atualizar

As skills evoluem. Para pegar a versão nova de UMA skill, rode o mesmo prompt de instalação — ele sobrescreve com
a última versão do GitHub. No app, a aba **Skills** mostra quando há atualização disponível.

**Para atualizar todas de uma vez**, cole este prompt no seu Claude Code (ou Codex) aberto na pasta do seu OS.
O endereço traz `fim-do-dia` só como exemplo: o agente troca pelo nome de cada pasta. Skill que você mesmo
criou (não existe no GitHub) e skill que já está na versão atual ficam como estão.

```
Atualize todas as minhas skills do MeuOS. Faça assim: 1) liste as pastas da minha pasta de skills (você sabe onde elas ficam) que têm um arquivo SKILL.md e leia a linha "version" do frontmatter de cada uma; 2) para cada pasta, baixe o SKILL.md da pasta de mesmo nome no GitHub do MeuOS, que fica em https://raw.githubusercontent.com/ferjrbh/meuos-skills/main/skills/fim-do-dia/SKILL.md trocando "fim-do-dia" pelo nome de cada pasta; se a versão baixada for maior que a local, substitua o SKILL.md local pelo baixado; se a versão for igual ou o arquivo não existir no GitHub (erro 404), não mexa; 3) não altere nenhum outro arquivo do meu OS; 4) ao final, mostre uma tabela com skill, versão antes e versão depois. Não me pergunte nada no meio, só mostre a tabela.
```

## Crie a sua própria skill

Uma skill é um único `SKILL.md` com frontmatter (metadados) + instruções em markdown:

```markdown
---
name: minha-skill
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
