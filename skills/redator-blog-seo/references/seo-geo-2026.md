# Por que estas regras — SEO e busca por IA em 2026 (com fontes oficiais)

> Referência da skill **redator-blog-seo**. O SKILL.md diz *o que fazer*; aqui está *por que*,
> ancorado em documentação oficial. Regra de ouro: **nomes de modelo, recursos e regras de
> rich result mudam** — confirme na fonte oficial antes de cravar. Tudo abaixo foi verificado
> em 2026; relê a fonte se for usar daqui a alguns meses.

A virada de chave de 2026: o Google **dissolveu o "Helpful Content System" dentro do núcleo do
ranking** (mar/2024) e passou a avaliar utilidade continuamente, site a site. O eixo é E-E-A-T
com **Trust (confiança) como o vértice mais importante**, e os core updates de dez/2025 a 2026
elevaram o piso de qualidade. Tradução para o gestor: não existe mais um "truque de SEO" a
perseguir — existe **ser, de fato, a melhor resposta**, e provar isso.
Fonte: https://developers.google.com/search/docs/appearance/ranking-systems-guide

---

## Dois mitos que o nosso instinto ainda repete — e que morreram

### 1. "Tem uma densidade/contagem de palavra-chave ideal" — não tem
O Google **nega explicitamente** ter densidade ideal ou contagem de palavras preferida. Os
sistemas de ranking entendem **significado** (BERT, neural matching), então repetir a frase
exata não ajuda e pode atrapalhar. Analogia: é como um candidato numa entrevista que repete o
nome da vaga 9 vezes — não convence ninguém; o que convence é demonstrar que domina o assunto.
- Não há densidade ideal: https://developers.google.com/search/docs/appearance/ranking-systems-guide
- "Você está escrevendo para um número de palavras porque ouviu que o Google prefere? (Não, não
  preferimos)": https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- **O que fazer:** mire **cobertura semântica** (entidade-alvo + subtópicos + termos
  relacionados). Comprimento = o que a intenção exige, e para. Enchimento dilui e é punido.

### 2. "FAQ/HowTo em schema rende rich result" — não rende mais
O **FAQ rich result foi removido por completo** do Google Search em **07-mai-2026**, para todos
os sites; o **HowTo rich result está morto desde set/2023**. O JSON-LD continua sendo Schema.org
válido (não penaliza), mas **não gera mais nenhum destaque no SERP** — então tratá-lo como item
obrigatório de qualidade é mirar um alvo que sumiu.
- FAQPage (doc oficial, mudança): https://developers.google.com/search/docs/appearance/structured-data/faqpage
- Cobertura: https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/
- HowTo/FAQ (anúncio 2023): https://developers.google.com/search/blog/2023/08/howto-faq-changes
- **O que fazer:** mantenha o **bloco de FAQ visível** (ele é útil e citável pela IA); trate o
  schema FAQPage como opcional sem ganho de SERP; nunca bloqueie publicação por ele.

---

## O que move o ponteiro hoje (os ganhos reais)

### A. Autor é Pessoa, não Organização — sameAs + knowsAbout
O sinal que a IA **não consegue fabricar** é Experiência (o "E" extra do E-E-A-T). Modelar o
autor como `Person` real, com `sameAs` (perfis que provam a identidade — LinkedIn, Wikidata) e
`knowsAbout` (áreas de expertise), é o maior ganho de Trust disponível, e custa quase nada
(mudar o bloco de schema + puxar 2-3 campos do contexto). O byline real é recomendação oficial.
Analogia: é a diferença entre um artigo "assinado pela redação" e um assinado por um especialista
com currículo público — o segundo é citável por humano e por IA.
- Article / author Person: https://developers.google.com/search/docs/appearance/structured-data/article
- sameAs (identidade) vs knowsAbout (autoridade tópica): https://willscott.me/2025/07/30/sameas-versus-knowsabout-in-schema/
- **Regra dura:** o autor tem de ser **pessoa real** do contexto. Inventar autor para encher
  schema é mentira que corrói Trust (e fere a regra anti-invenção).

### B. Information gain — dado próprio + estatística com fonte nomeada
Pesquisa peer-reviewed (Princeton, GEO, KDD 2024) mostra que **adicionar estatísticas, citar
fontes e inserir aspas** eleva a probabilidade de citação por IA em ~30-40% — enquanto "fluência"
e enchimento têm efeito desprezível. E o Google rebaixa como qualidade mais baixa o conteúdo que
"um chatbot escreveria em 10 segundos". Junte os dois: **cada artigo precisa de ≥1 estatística
com fonte nomeada e linkada no corpo + ≥1 ângulo/dado próprio** que o SERP ainda não tem.
- Princeton GEO (paper): https://arxiv.org/abs/2311.09735
- "Information gain" em SEO: https://searchengineland.com/what-information-gain-seo-means-440326
- Conteúdo IA sem valor é spam (scaled content abuse): https://developers.google.com/search/docs/essentials/spam-policies
- Analogia: numa reunião, quem traz **um número novo e uma história de bastidor** é citado; quem
  repete o consenso, não.

### C. Answer-first e leitura por passagem
A IA cita **passagens**, não páginas — e a maior parte das citações sai dos primeiros ~30% do
conteúdo. Por isso: a primeira frase de cada seção responde a pergunta do H2, **autossuficiente**
(sem "isso/ele" solto — comece pela entidade), e há um **bloco TL;DR** logo após a intro. O
próprio Google posiciona "responder primeiro" e headings descritivos como **boa comunicação**
(não truque) — o que é ótimo, porque significa que vale tanto para humano quanto para máquina.
- AI features / como aparecer: https://developers.google.com/search/docs/appearance/ai-features
- **Calibragem honesta:** "multiplicadores por formato" que circulam (tabela 4x, etc.) são
  heurística de fornecedor, não promessa. Trate como boa formatação de baixo risco, não como hack.

### D. Links internos semânticos de cluster
Num estudo de 2,5 milhões de links, **81% das âncoras eram ricas em keyword, mas só 8% tinham
alinhamento semântico forte** com a página-destino — é o erro nº1 e a maior oportunidade. O
Google pede âncora **descritiva, concisa e relevante**, condena "clique aqui"/"leia mais", exige
`<a href>` real, e diz que **toda página relevante precisa de ≥1 link de entrada** (sem órfãos).
Links **dentro da prosa** carregam mais sinal que caixas de "leia também".
- Links rastreáveis (doc oficial): https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- **O que fazer:** âncora de 2-5 palavras que descreve o tópico do destino e casa com o título
  dele; linkar de/para a página-pilar do tema; variar a âncora ao repetir o mesmo destino.

### E. Schema honesto (e o que ele faz e não faz)
Article (ou BlogPosting) + BreadcrumbList **continuam ativos e recomendados** — valem pelo rich
result tradicional e pela desambiguação de entidades. O que **não** é verdade é que schema seja
alavanca de citação por IA: evidência rigorosa (Ahrefs, 2026) achou efeito nulo, e os LLMs leem
o **HTML visível** e ignoram JSON-LD oculto. Conclusão prática: faça o schema certo pelo rich
result do Google, mas o ganho de IA vem do **conteúdo visível bem estruturado**.
- Article: https://developers.google.com/search/docs/appearance/structured-data/article
- Breadcrumb: https://developers.google.com/search/docs/appearance/structured-data/breadcrumb
- Schema ≠ citação por IA: https://www.stanventures.com/news/schema-markup-has-no-meaningful-impact-on-ai-citations-7231/

### F. Elegibilidade técnica — e o que NÃO fazer
O **único requisito oficial** para ser citado em AI Overviews é estar **indexado e elegível a
snippet**. Logo: não aplique `noindex`/`nosnippet` onde quer citação, e libere os crawlers de IA
no `robots.txt` (GPTBot, PerplexityBot, Google-Extended, CCBot) se a marca quer aparecer. E
**não** invista em `llms.txt` (nenhum grande motor usa para citação; o Google confirmou que não
usa) nem em "versão para IA" do texto — o próprio Google (2026) diz que otimizar para IA
generativa **ainda é SEO**.
- AI features / requisito de citação: https://developers.google.com/search/docs/appearance/ai-features
- Google não endossa llms.txt: https://www.seroundtable.com/google-does-not-endorse-llms-txt-40789.html

---

## Transparência, frescor e supervisão (sinais de Trust)
- **IA não é proibida**, mas usar automação para manipular ranking, sim. O Google sugere
  transparência quando razoável e **exige supervisão/valor humano**. Uma linha "redigido com
  apoio de IA e revisado por [pessoa]" + revisão humana real protege o Trust.
  https://developers.google.com/search/docs/essentials/spam-policies
- **`dateModified` honesto**: só atualize a data quando o conteúdo muda. Data falsa corrói
  E-E-A-T. Refresh programado importa especialmente se o alvo inclui Perplexity (pune conteúdo
  velho); menos para o AI Overviews do Google.

---

## Fontes oficiais (confirme aqui antes de cravar — isto muda)
- Google — guia de sistemas de ranking: https://developers.google.com/search/docs/appearance/ranking-systems-guide
- Google — criar conteúdo útil (E-E-A-T, word count, autoavaliação): https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google — políticas de spam (scaled content abuse, IA): https://developers.google.com/search/docs/essentials/spam-policies
- Google — recursos de IA / como aparecer: https://developers.google.com/search/docs/appearance/ai-features
- Google — Article structured data: https://developers.google.com/search/docs/appearance/structured-data/article
- Google — Breadcrumb structured data: https://developers.google.com/search/docs/appearance/structured-data/breadcrumb
- Google — FAQPage (mudança de mai/2026): https://developers.google.com/search/docs/appearance/structured-data/faqpage
- Google — links rastreáveis: https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- Schema.org (referência de vocabulário): https://schema.org/
- Princeton GEO (peer-reviewed): https://arxiv.org/abs/2311.09735
