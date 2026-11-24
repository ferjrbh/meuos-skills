# MeuOS — Biblioteca de Skills

> Skills oficiais do **MeuOS** para o seu Claude Code: organize seu OS pessoal, crie conteúdo,
> faça growth, automação e produtividade — cada uma pronta para instalar em segundos.

[![skills](https://img.shields.io/badge/skills-153-D95C1A?style=flat-square)](https://www.meuos.com.br)
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

### 🥾 Método TRILHA: tarefas longas com IA (3)
Para o trabalho que não cabe num prompt só. A primeira serve para qualquer projeto; as duas seguintes usam o método para criar e publicar um site.

| Skill | O que faz | Gatilhos |
|---|---|---|
| **[MeuOS TRILHA](skills/meuos-trilha/SKILL.md)** | Conduz qualquer tarefa longa pelos 6 marcos: critérios de pronto, regras, etapas, livro de bordo, prova e aprovação nos pontos de risco | *"método trilha"*, *"me guia nesse projeto"*, *"retomar de onde paramos"* |
| **[Site TRILHA: preparar](skills/trilha-site-preparar/SKILL.md)** | Entrevista uma pergunta por vez, pede o material e cataloga tudo até o briefing aprovado | *"quero criar meu site pelo Método TRILHA"*, *"me entrevista para o site"* |
| **[Site TRILHA: construir e publicar](skills/trilha-site-publicar/SKILL.md)** | Constrói por blocos testados e guia pelo GitHub (privado) e pela Vercel até o site no ar | *"constrói o site"*, *"publica o site"* |

### 🧮 Contábil: o escritório de contabilidade (63)
Para o contador e o escritório contábil, criadas pela contadora **Márcia Almeida** com a lei citada e parâmetros de 2026. A skill prepara; o contador revisa e assina.

#### Tributos e Apuração (15)

| Skill | O que faz |
|---|---|
| **[Analisar Notas Fiscais (Área Fiscal)](skills/analisar-notas-fiscais/SKILL.md)** | Lê XMLs de NF-e (entrada e saída) e NFS-e, confere o lançamento contábil esperado por CFOP e aponta inconsistências fiscais, com foco em empresas do Simples Nacional |
| **[Apuração do Lucro Presumido (IRPJ, CSLL, PIS e COFINS)](skills/apuracao-lucro-presumido/SKILL.md)** | Apura o IRPJ e a CSLL trimestrais e o PIS/COFINS cumulativos mensais de empresa no Lucro Presumido, já com a majoração da presunção da LC 224/2025 para receita acima… |
| **[Apuração do Lucro Real (IRPJ e CSLL)](skills/apuracao-lucro-real/SKILL.md)** | Apura IRPJ e CSLL no Lucro Real, trimestral ou anual com estimativa mensal, partindo do lucro contábil antes dos tributos (LAIR), fazendo adições e exclusões na Parte… |
| **[Apuração e controle do MEI](skills/apuracao-mei/SKILL.md)** | Cuida do MEI (Microempreendedor Individual) |
| **[Calcular o DAS do Simples Nacional](skills/calcular-das-simples-nacional/SKILL.md)** | Calcula o DAS mensal do Simples Nacional a partir do faturamento |
| **[Cálculo de ICMS e ICMS-ST](skills/calculo-icms-icms-st/SKILL.md)** | Calcula o ICMS próprio e o ICMS-ST em operações internas e interestaduais, com MVA ajustada, DIFAL (LC 190/2022) e FCP, alíquota de 4% de importados, antecipação e… |
| **[Cálculo do INSS da empresa (contribuição patronal)](skills/calculo-inss-empresa/SKILL.md)** | Calcula o INSS patronal mensal |
| **[Cálculo e apuração mensal de IPI](skills/calculo-ipi/SKILL.md)** | Apuração mensal de IPI para indústria e estabelecimentos equiparados a industrial (importador, filial atacadista de indústria), com TIPI vigente (Decreto nº… |
| **[Cálculo do IRRF na folha e em pagamentos a pessoa física](skills/calculo-irrf-folha/SKILL.md)** | Cálculo do IRRF sobre salário CLT, pró-labore, 13º salário, RPA de autônomo e outros rendimentos pagos por empresa a pessoa física (aluguel, juros, royalties), com a… |
| **[Cálculo e apuração mensal de ISS](skills/calculo-iss/SKILL.md)** | Apuração mensal de ISS (ISSQN): enquadramento do serviço na lista da LC nº 116/2003, definição do município competente (regra do estabelecimento prestador × exceções… |
| **[Apuração de PIS/COFINS cumulativo](skills/calculo-pis-cofins-cumulativo/SKILL.md)** | Apuração mensal de PIS (0,65%) e COFINS (3%) no regime cumulativo (Lucro Presumido e atividades do art. 10 da Lei nº 10.833/2003 no Lucro Real), com exclusão do ICMS… |
| **[Apuração de PIS/COFINS não cumulativo](skills/calculo-pis-cofins-nao-cumulativo/SKILL.md)** | Apuração mensal de PIS (1,65%) e COFINS (7,6%) no regime não cumulativo (Lucro Real), com débitos × créditos, conceito de insumo do STJ (REsp 1.221.170, Temas 779 e… |
| **[Conferir apuração do Simples Nacional](skills/conferir-apuracao-simples-nacional/SKILL.md)** | Confere a apuração mensal do Simples Nacional (PGDAS-D) cruzando com as notas fiscais de saída e de entrada. Verifica a receita bruta do mês e a RBT12, o Anexo… |
| **[Reforma Tributária do Consumo — transição 2026–2033](skills/reforma-tributaria-transicao/SKILL.md)** | Orienta a transição da Reforma Tributária do Consumo (Emenda Constitucional nº 132/2023, LC nº 214/2025 e LC nº 227/2026, que instituiu o Comitê Gestor do IBS):… |
| **[Retenções tributárias do tomador de serviços](skills/retencoes-tributarias-tomador/SKILL.md)** | Calcula as retenções que a empresa TOMADORA deve fazer ao pagar serviços de pessoa jurídica: IRRF 1,5% ou 1% (código 1708), CSRF 4,65% (PIS+COFINS+CSLL, código 5952,… |

#### Obrigações Acessórias (8)

| Skill | O que faz |
|---|---|
| **[DCTFWeb mensal e anual](skills/dctfweb/SKILL.md)** | Prepara e confere a DCTFWeb mensal (e a anual de 13º salário): débitos federais que vêm do eSocial e da EFD-Reinf (INSS patronal CPP, RAT×FAP, Terceiros, INSS retido,… |
| **[DIMOB anual](skills/dimob/SKILL.md)** | Prepara e confere a DIMOB (Declaração de Informações sobre Atividades Imobiliárias) anual de construtoras, incorporadoras, loteadoras, imobiliárias e administradoras… |
| **[DMED anual](skills/dmed/SKILL.md)** | Prepara e confere a DMED (Declaração de Serviços Médicos e de Saúde) anual de PJ prestadoras de serviços de saúde (hospitais, clínicas, laboratórios, médicos e… |
| **[ECD — Escrituração Contábil Digital](skills/ecd-escrituracao-contabil-digital/SKILL.md)** | Prepara, diagnostica e valida a ECD anual (SPED Contábil |
| **[ECF — Escrituração Contábil Fiscal](skills/ecf-escrituracao-contabil-fiscal/SKILL.md)** | Prepara e confere a ECF anual (IN RFB nº 2.004/2021): recuperação da ECD, mapeamento referencial, e-Lalur/e-Lacs (Parte A com adições, exclusões e compensações; Parte… |
| **[EFD-Contribuições mensal](skills/efd-contribuicoes/SKILL.md)** | Prepara e confere a EFD-Contribuições mensal (PIS/COFINS e CPRB): escrituração por CST, créditos do não cumulativo, Bloco M (apuração), F500/F550 (regime de caixa ou… |
| **[EFD ICMS/IPI mensal](skills/efd-icms-ipi/SKILL.md)** | Prepara e confere a EFD ICMS/IPI mensal (SPED Fiscal |
| **[EFD-Reinf mensal](skills/efd-reinf/SKILL.md)** | Organiza a EFD-Reinf mensal: R-1000 (cadastro), R-1070 (processos), R-2010/R-2020 (retenção de 11% de INSS na cessão de mão de obra, tomador e prestador),… |

#### DP e eSocial (9)

| Skill | O que faz |
|---|---|
| **[Analisar Folha de Pagamento e Pró-labore](skills/analisar-folha-pagamento/SKILL.md)** | Lê PDFs de folha de pagamento e pró-labore, confere retenções (INSS, IRRF, vale-transporte), encargos (INSS patronal, RAT, Terceiros, FGTS), lançamentos contábeis… |
| **[eSocial — Admissão (S-2190 / S-2200)](skills/esocial-admissao/SKILL.md)** | Especialista em admissão no eSocial |
| **[eSocial — Afastamentos (S-2230) e CAT (S-2210)](skills/esocial-afastamentos/SKILL.md)** | Especialista em afastamentos no eSocial |
| **[eSocial — Eventos Periódicos e Fechamento](skills/esocial-eventos-periodicos/SKILL.md)** | Especialista em eventos periódicos do eSocial |
| **[eSocial — Desligamento (S-2299)](skills/esocial-rescisao/SKILL.md)** | Especialista no desligamento CLT no eSocial |
| **[Férias e 13º Salário](skills/ferias-13-salario/SKILL.md)** | Especialista em férias e 13º salário com os parâmetros de 2026 |
| **[FGTS — Recolhimento Mensal e Rescisório (FGTS Digital)](skills/fgts-guia-recolhimento/SKILL.md)** | Especialista em FGTS mensal e rescisório pelo FGTS Digital |
| **[Folha de Pagamento Mensal (CLT)](skills/folha-pagamento-mensal/SKILL.md)** | Especialista em folha CLT mensal com parâmetros de 2026 |
| **[Rescisão CLT — Cálculo das Verbas](skills/rescisao-clt-calculo/SKILL.md)** | Especialista no cálculo financeiro da rescisão CLT |

#### Fechamento Contábil (14)

| Skill | O que faz |
|---|---|
| **[Analisar Extrato Bancário e de Caixa](skills/analisar-extrato-bancario/SKILL.md)** | Lê extratos bancários (PDF ou OFX) e relatórios de caixa, classifica cada transação contabilmente, concilia o saldo do extrato com o saldo do razão item a item e… |
| **[Analisar Lançamento Contábil (unitário)](skills/analisar-lancamento-contabil/SKILL.md)** | Analisa um lançamento contábil individual antes do registro definitivo |
| **[Analisar Relatório Contábil](skills/analisar-relatorio-contabil/SKILL.md)** | Analisa relatórios contábeis com muitos lançamentos (razão, diário, balancete, livro contábil ou planilha de lançamentos) à luz da ITG 2000 (R1) e da NBC TG 1000 (R1)… |
| **[Ativo Imobilizado e Depreciação](skills/ativo-imobilizado-depreciacao/SKILL.md)** | Cuida do ativo imobilizado (CPC 27) do cadastro à baixa |
| **[Análise de Balancete](skills/balancete-analise/SKILL.md)** | Lê e analisa o balancete mensal antes da entrega ao cliente |
| **[Conciliação de Cartões e Credenciadoras](skills/conciliacao-cartoes-credenciadora/SKILL.md)** | Concilia as vendas no cartão e no PIX por maquininha (Cielo, Stone, Rede, GetNet, PagSeguro, SafraPay, Mercado Pago e outras) com os repasses da credenciadora |
| **[Conciliação de Clientes (Contas a Receber)](skills/conciliacao-clientes/SKILL.md)** | Concilia o razão de clientes (contas a receber) título a título |
| **[Conciliação de Fornecedores (Contas a Pagar)](skills/conciliacao-fornecedores/SKILL.md)** | Concilia o razão de fornecedores (contas a pagar) nota a nota |
| **[Conciliar extrato bancário × razão contábil](skills/conciliar-extrato-razao/SKILL.md)** | Faz o casamento item a item entre o extrato bancário (OFX, CSV ou PDF) e o razão contábil da conta banco. Aponta lançamentos sem par, tarifas, IOF, juros e… |
| **[DRE gerencial](skills/dre-gerencial/SKILL.md)** | Monta a DRE gerencial do cliente separando custos variáveis e fixos, calcula margem de contribuição (MC), ponto de equilíbrio (PE) em reais e em unidades, compara… |
| **[Fechamento contábil mensal](skills/fechamento-mensal/SKILL.md)** | Roteiro completo do fechamento contábil mensal em até 5 dias úteis (D+1 a D+5) |
| **[Fluxo de caixa projetado](skills/fluxo-caixa-projetado/SKILL.md)** | Monta o fluxo de caixa pelo método direto, realizado e projetado |
| **[Lançamentos contábeis padrão](skills/lancamentos-contabeis-padrao/SKILL.md)** | Catálogo de lançamentos contábeis (débito e crédito) para as operações do dia a dia |
| **[Plano de contas aderente aos CPCs](skills/plano-contas-cpc/SKILL.md)** | Estrutura o plano de contas do cliente com todas as contas analíticas mapeadas para o plano referencial da ECD, aderente aos CPCs (26 apresentação, 27 imobilizado, 04… |

#### IRPF e Societário (10)

| Skill | O que faz |
|---|---|
| **[Abertura de empresa (CNPJ) pela REDESIM](skills/abertura-empresa-cnpj/SKILL.md)** | Conduz a abertura de empresa pela REDESIM (Lei nº 11.598/2007, com as simplificações da Lei nº 14.195/2021) |
| **[Alteração contratual](skills/alteracao-contratual/SKILL.md)** | Prepara alterações contratuais pela REDESIM |
| **[Análise de IRPF (revisão da pré-preenchida)](skills/analisar-irpf/SKILL.md)** | Analisa a declaração de IRPF pré-preenchida (Receita Federal) cruzando com os documentos do cliente |
| **[Elaboração da declaração de IRPF (completa × simplificada)](skills/elaborar-irpf-completa/SKILL.md)** | ELABORA a declaração de IRPF do zero para contribuintes com várias fontes |
| **[Encerramento de empresa (baixa)](skills/encerramento-empresa-baixa/SKILL.md)** | Conduz a baixa de empresa pela REDESIM |
| **[Carnê-leão (aluguel e demais rendimentos de PF e do exterior)](skills/irpf-aluguel-carne-leao/SKILL.md)** | Calcula o carnê-leão (recolhimento mensal obrigatório |
| **[Ganho de capital da pessoa física](skills/irpf-ganho-capital/SKILL.md)** | Apura o ganho de capital de pessoa física na venda de imóveis, participações societárias fora da bolsa, criptoativos e outros bens |
| **[IR sobre investimentos em bolsa (renda variável)](skills/irpf-investimentos-bolsa/SKILL.md)** | Apura o IR mensal da pessoa física em renda variável na B3 |
| **[Parcelamento e transação de débitos federais](skills/parcelamento-receita-federal/SKILL.md)** | Compara as saídas para débitos federais |
| **[Resposta a fiscalização e intimação](skills/resposta-fiscalizacao-intimacao/SKILL.md)** | Prepara a resposta a fiscalizações e cobranças federais (e, no que couber, estaduais e municipais) |

#### Consultoria Avançada (7)

| Skill | O que faz |
|---|---|
| **[Análise comparativa de regime tributário](skills/analise-tributaria-regime/SKILL.md)** | Compara Simples Nacional, Lucro Presumido e Lucro Real para um cliente, com projeção de 12 meses e todos os tributos (IRPJ, CSLL, PIS/COFINS ou CBS, ICMS, ISS, INSS… |
| **[Diagnóstico de malha fina do IRPF](skills/diagnosticar-malha-fina-pf/SKILL.md)** | Diagnostica declaração de IRPF JÁ ENTREGUE que caiu na malha fina. Lê o extrato do processamento no e-CAC (Meu Imposto de Renda), identifica a causa da retenção… |
| **[Due diligence contábil, fiscal e trabalhista](skills/due-diligence-contabil/SKILL.md)** | Conduz due diligence (auditoria de compra) contábil, fiscal, trabalhista e societária antes de compra, venda, fusão ou aporte de investidor. Identifica passivos… |
| **[Diagnóstico de malha e intimações de pessoa jurídica](skills/malha-fina-pj-diagnostico/SKILL.md)** | Diagnostica comunicações do fisco a empresas |
| **[Recuperação retroativa de créditos de PIS/COFINS](skills/recuperacao-creditos-pis-cofins/SKILL.md)** | Levanta e calcula PIS/COFINS pagos a maior nos últimos 5 anos (retroativo), com atualização pela Selic, e prepara a retificação da EFD-Contribuições e o PER/DCOMP.… |
| **[Revisão fiscal por cruzamento de SPEDs](skills/revisao-fiscal-cruzamento-sped/SKILL.md)** | Cruza as escriturações e declarações da empresa |
| **[Valuation de PME](skills/valuation-pme/SKILL.md)** | Estima o valor de uma pequena ou média empresa por fluxo de caixa descontado (DCF |

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
