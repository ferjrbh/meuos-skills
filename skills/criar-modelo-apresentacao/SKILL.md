---
name: Criar Modelo de Apresentacao
description: |
  Cria o modelo visual de apresentacao do usuario — um pacote completo com 35 layouts
  de slide (capa, indice, conteudo, fotos, graficos, chat, timeline, comparacao, pricing,
  CTA e encerramento) usando as cores, fonte e logo do usuario.
  Executa quando o usuario diz "criar modelo de apresentacao", "criar padrao de slides",
  "criar template de slides", "meu modelo visual", "padrao visual para apresentacoes",
  "template de apresentacao", "design system de slides", "modelo de ppt", "modelo para slides".
  O modelo gerado vira fonte-de-verdade da skill "Criar Apresentacao".
version: 1.1
context: meuos
user-invocable: true
argument-hint: "(sem argumentos — a skill faz entrevista completa)"
---

---

## 🥇 REGRA DE OURO — HTML que vira PDF certo (novidade · 13-MAI-2026)

Se você (ou o agente) está gerando HTML que será impresso em PDF (Ctrl+P → Salvar como PDF), a regra abaixo é INQUEBRÁVEL:

> **Cada `<div class="page">` (ou `<div class="slide">`) é UMA página A4 / UM slide 16:9 inteiro pré-calibrado pelo designer. O navegador não decide nada — só renderiza.**

NUNCA empilhar múltiplas seções dentro de uma `.page`/`.slide` confiando em `page-break-inside: avoid`. A heurística do Chrome falha. SEMPRE quebrar manualmente em divs separados, 1 por página/slide.

**CSS canônico:**
```css
.page, .slide {
  width: 210mm;           /* A4 portrait; ou 338mm pra 16:9 paisagem */
  min-height: 297mm;      /* A4; ou 190mm pra 16:9 */
  page-break-after: always;
  display: flex;
  flex-direction: column;
  padding: 16mm 18mm;
}
@page { size: A4; margin: 0; }
@media print {
  body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
}
```

**Detalhamento completo:** veja a skill **`Gera HTML to PDF`** (subcategory `office`) — fonte-única dessa regra, com checklist, anti-patterns, e prompt-template pra você pedir certo ao agente.

---


# Criar Modelo de Apresentacao — Seu Padrao Visual de Slides

## O que esta skill faz

Esta skill cria o SEU padrao visual de apresentacoes — um pacote com 35 layouts prontos
(capa, indice, conteudo, fotos, graficos, comparacao, timeline, pricing, CTA, encerramento)
pintado com as SUAS cores, SUA fonte e SUA logo. Depois, quando voce quiser montar
qualquer apresentacao, a skill "Criar Apresentacao" usa este modelo como base — voce nao
precisa pensar em design, so no conteudo.

Pense assim: este modelo e a "identidade visual da sua apresentacao". Define uma vez,
usa para sempre. Pode criar varios modelos (um para cada marca, cliente ou tema).

> **Importante para o agente de IA:** esta skill ja contem o CSS+HTML CANONICO completo
> embutido na secao "BLUEPRINT CANONICO" no final do arquivo. Voce NAO precisa buscar
> gabarito externo — o codigo de referencia dos 35 slides esta pronto, basta copiar,
> substituir os placeholders pelos tokens do aluno e trocar os textos-demo pelo conteudo
> real descrito no catalogo.

---

## Quando usar

- Antes da primeira vez que voce for criar slides no OS
- Quando quiser uma nova identidade visual (novo cliente, novo produto, nova marca)
- Quando quiser atualizar o modelo atual (trocar cor, fonte, logo)
- Quando o usuario diz "criar modelo", "padrao de slides", "template de apresentacao"

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0 — Apresentar a skill e pedir o nome do modelo

Apresentar em 3-4 linhas o que vai acontecer:

> Vamos criar o SEU padrao visual de apresentacoes. Vou te fazer algumas perguntas
> rapidas (cores, fonte, logo, fotos) e entregar um pacote com 35 layouts prontos que
> voce pode usar em qualquer apresentacao. Se nao souber alguma resposta, deixo uma
> sugestao padrao. Podemos comecar?

Apos confirmacao, pedir o NOME do modelo:

> Como voce quer chamar este modelo? (exemplos: "padrao-pessoal", "modelo-empresa-x",
> "minha-marca") Use letras minusculas e tracos — sem espacos nem acentos.

Validar: apenas `[a-z0-9\-]+`, sem espaco. Se vier com espaco, converter para traco e
mostrar ao usuario. Se vier com acento, remover os acentos. Confirmar antes de prosseguir.

---

### PASSO 1 — Entrevista de identidade visual (10 perguntas)

Fazer uma pergunta por vez, SEMPRE com sugestao padrao entre parenteses para o usuario
poder responder so "ok" ou "padrao" se nao souber.

**1. Cor principal**
> Qual e a cor principal do seu modelo? Pode dar em hexadecimal (`#c8a97e`) ou nome
> (`dourado`, `azul`, `verde`). (Sugestao padrao: `#1e3a8a` — azul marinho)

Validar: se for nome, converter para hex. Aceitar nomes comuns em portugues e ingles.

**2. Cor secundaria**
> E a cor secundaria? (Sugestao padrao: uma versao mais clara da principal)

Se usuario nao tem opiniao: GERAR uma versao 20% mais clara da cor principal.

**3. Cor de fundo dos slides**
> Qual o fundo dos slides? (Sugestao padrao: `#fafaf9` off-white. Outras opcoes: `#ffffff`
> branco, `#0a0e27` azul escuro, `#1d1d1f` preto premium)

**4. Tom geral**
> O fundo que voce escolheu e claro ou escuro? Isso define se o texto vai ser claro
> ou escuro.

Armazenar como `tom = "escuro" | "claro"`.

**5. Fonte principal**
> Que fonte voce quer usar? (Sugestao padrao: `Poppins`. Outras: `Inter`, `Roboto`,
> `Open Sans`, `Montserrat`, `Lato`, `Nunito`, `Raleway`)

Qualquer fonte do Google Fonts e valida. Se o usuario der uma fonte rara, pedir confirmacao.

**6. Rounded corners**
> Os cantos dos cards e caixas vao ser arredondados? Quanto?
> 1) Sem (`0px`) — brutalista
> 2) Leve (`6px`)
> 3) Padrao (`12px`)
> 4) Bem arredondado (`20px`) **[sugestao padrao]**
> 5) Ultra arredondado (`32px`)

Armazenar `radius` e `radius_small = radius / 2` (min 4px).

**7. Densidade**
> 1) Minimalista (1 ideia por slide, tipografia gigante)
> 2) Balanceado (2-3 bullets) **[sugestao padrao]**
> 3) Denso (ate 5 bullets)

**8. Estilo tipografico**
> 1) Serif (formal)
> 2) Sans-serif (moderna) **[sugestao padrao]**
> 3) Mista (titulos serif + corpo sans)

Se mista, pedir a fonte serif (sugerir `Playfair Display`).

**9. Rodape dos slides**
> 1) Com logo + nome + site
> 2) So nome + numero do slide **[sugestao padrao]**
> 3) So numero
> 4) Sem rodape

Se 1 ou 2: pedir o texto exato.

**10. Transicao entre secoes**
> 1) Sem divisoria
> 2) Divisoria colorida com numero grande **[sugestao padrao]**
> 3) Foto full-bleed com titulo

Salvar tudo em `tokens` (ver estrutura em "TOKENS JSON" no final).

---

### PASSO 2 — Logo e fotos (paths locais obrigatorios)

**2a. Logo**

Perguntar:
> Agora preciso da sua LOGOMARCA. Ela precisa estar **salva no seu computador** —
> nao pode ser URL da internet. Me passa o caminho completo do arquivo.

Se o usuario informar URL web (`http://` ou `https://`):
> Percebi que voce me passou um link da internet. Posso:
> A) Baixar automaticamente para `meus-modelos/{nome_modelo}/assets/logo.{ext}`
> B) Te ensinar como baixar manualmente
>
> Qual voce prefere?

Se A: criar a pasta assets/, baixar via HTTP GET, salvar com extensao baseada no Content-Type.
Se B: ensinar passo a passo (salvar imagem como... → salvar em pasta especifica).

Validar path final:
- Arquivo existe? Senao: avisar e pedir de novo.
- Extensao .png, .jpg, .jpeg, .svg, .webp? Senao: avisar.
- Copiar arquivo para `meus-modelos/{nome_modelo}/assets/logo.{ext}` (self-contained).

**2b. Fotos (3 fotos)**

> Preciso de 3 fotos para montar os layouts com imagem. Podem ser qualquer coisa —
> foto de ambiente, produto, natureza. Sao so exemplos para o modelo mostrar como
> slides com foto ficam — voce troca depois nas apresentacoes reais.

Repetir mesmo fluxo da logo. Salvar como `foto1.{ext}`, `foto2.{ext}`, `foto3.{ext}`.

Se usuario nao tem:
> Posso usar 3 placeholders coloridos (retangulos SVG com gradiente nas suas cores)
> — voce troca depois. Prefere assim?

Se sim, gerar 3 SVGs com gradientes nas cores primaria + secundaria.

---

### PASSO 3 — Gerar o template HTML a partir do BLUEPRINT CANONICO

**IMPORTANTE:** o blueprint completo (CSS + 35 slides) esta embutido nesta skill na secao
"BLUEPRINT CANONICO" no final do arquivo. Voce NAO precisa inventar nada — apenas:

1. **Copiar TODO o bloco** entre os marcadores `<!-- === INICIO BLUEPRINT === -->` e
   `<!-- === FIM BLUEPRINT === -->`.

2. **Substituir os placeholders** pelos valores do objeto `tokens`:

| Placeholder | Substituir por |
|-------------|----------------|
| `{{COR_PRIMARIA}}` | `tokens.cor_primaria` |
| `{{COR_PRIMARIA_LIGHT}}` | versao 15% mais clara da primaria |
| `{{COR_PRIMARIA_SOFT}}` | versao 90% mais clara da primaria (alpha) |
| `{{COR_SECUNDARIA}}` | `tokens.cor_secundaria` |
| `{{COR_SECUNDARIA_LIGHT}}` | versao 15% mais clara da secundaria |
| `{{COR_SECUNDARIA_SOFT}}` | versao 90% mais clara da secundaria |
| `{{COR_FUNDO}}` | `tokens.cor_fundo` |
| `{{COR_TEXTO}}` | `#1a1a1a` se tom=claro, `#f5f5f7` se tom=escuro |
| `{{COR_TEXTO_MUTED}}` | `#64748b` (claro) / `#94a3b8` (escuro) |
| `{{COR_TEXTO_SOFT}}` | `#94a3b8` (claro) / `#64748b` (escuro) |
| `{{COR_BORDA}}` | `#e2e8f0` (claro) / `#2a2a2a` (escuro) |
| `{{COR_BORDA_STRONG}}` | `#cbd5e1` (claro) / `#3a3a3a` (escuro) |
| `{{SHADOW_RGBA_SM}}` | RGBA da primaria com alpha 0.08 |
| `{{SHADOW_RGBA}}` | RGBA da primaria com alpha 0.10 |
| `{{OVERLAY_RGBA_STRONG}}` | RGBA da primaria com alpha 0.85 |
| `{{OVERLAY_RGBA_MED}}` | RGBA da primaria com alpha 0.65 |
| `{{OVERLAY_ACCENT_STRONG}}` | RGBA da secundaria com alpha 0.90 |
| `{{FONTE}}` | `tokens.fonte_principal` (sem aspas extras) |
| `{{RADIUS}}` | `tokens.radius` (ex: `20px`) |
| `{{RADIUS_SMALL}}` | metade do radius, minimo 4px |
| `{{RODAPE_TEXTO}}` | conteudo do rodape baseado em `tokens.rodape_tipo` e `rodape_texto` |

3. **Substituir os textos-demo dos 35 slides** pelo conteudo descrito no "CATALOGO DE
   LAYOUTS" abaixo. Os textos demo do blueprint sao de uma consultoria ficticia — voce
   NUNCA deve deixar esses textos no HTML final. Use-os apenas como guia de estrutura,
   espacamento e hierarquia tipografica. Substitua TODOS pelo conteudo real apropriado
   ao contexto do aluno.

4. **Substituir paths de assets** no blueprint:
   - `assets/logo.svg` → `assets/logo.{ext}` (usar extensao real do arquivo do aluno)
   - `assets/foto1.svg` → `assets/foto1.{ext}`
   - `assets/foto2.svg` → `assets/foto2.{ext}`
   - `assets/foto3.svg` → `assets/foto3.{ext}`

5. **Ajustar tipografia por densidade** (apos substituir placeholders):
   - Se `tokens.densidade = "minimalista"`: aumentar todos os font-sizes em 25%
   - Se `tokens.densidade = "denso"`: reduzir todos os font-sizes em 15%
   - Se `tokens.densidade = "balanceado"`: manter (default)

6. **Salvar** em `meus-modelos/{nome_modelo}/template.html`.

---

### CATALOGO DE LAYOUTS (os 35 blueprints obrigatorios)

O blueprint contem TODOS os 35 ja implementados. Conteudo resumido de cada:

| # | Tipo | Demo no blueprint |
|---|------|-------------------|
| 1 | Portada completa | "Transformacao em 5 passos" |
| 2 | Cover centralizada | Nome da empresa grande |
| 3 | Indice/TOC | 4 secoes numeradas |
| 4 | Divisoria de secao c/ numero | "PARTE 1" + numero 01 |
| 5 | Conteudo 3 bullets | "3 sintomas recorrentes" |
| 6 | Highlight box | "O custo da inacao" |
| 7 | 2 cards | "Quem avanca x Quem trava" |
| 8 | Rule-list | "4 principios inegociaveis" |
| 9 | 3 cards | "Tres pilares" |
| 10 | 6 cards (3x2) | "Seis dominios" |
| 11 | Divisoria colorida | "PARTE 2" com fundo secundaria |
| 12 | Flow diagram | "Metodo em 5 passos" |
| 13 | Stats/ROI | "Resultados medios" |
| 14 | Tabela | "Comparativo de abordagens" |
| 15 | Comparacao 2 colunas | "Antes vs Depois" |
| 16 | Timeline horizontal | "Cronograma 90 dias" |
| 17 | Chat/dialogo | Conversa CEO + IA |
| 18 | Steps numerados | "Como comecamos" |
| 19 | Divisoria minimalista | "PARTE 3" |
| 20 | Foto+texto split | "Caso 1" |
| 21 | Texto+foto split (invertido) | "Caso 2" |
| 22 | Foto full + overlay | "Caso 3" com overlay primaria |
| 23 | Split c/ foto inset | Quote de cliente |
| 24 | Foto terco superior | "Dashboard em producao" |
| 25 | Grid 3 fotos | "Entregaveis" |
| 26 | Divisoria com foto | "PARTE 4" com overlay secundaria |
| 27 | Barras verticais | "Evolucao da eficiencia" |
| 28 | Donuts | "Distribuicao de impacto" |
| 29 | Progress bars | "Adocao por area" |
| 30 | Multi-chart 2x2 | "KPIs do trimestre" |
| 31 | BIG NUMBER | "+347%" com gradiente |
| 32 | Quote | Depoimento de diretor |
| 33 | Pricing 3 planos | "Diagnostico / Transformacao / Ongoing" |
| 34 | CTA forte | "Vamos conversar em 45 minutos?" |
| 35 | Encerramento | "Obrigado" + contato |

**REGRA OBRIGATORIA:** troque TODOS os textos demo pelo conteudo real do aluno. Se o
aluno nao forneceu conteudo para todos os 35 slides (comum — o modelo tem mais slides
que o briefing de uma apresentacao tipica), inventar conteudo coerente com o contexto
do aluno (nome da empresa, area de atuacao). Os 35 layouts sao o CATALOGO VISUAL, nao
obrigatoriamente uma apresentacao completa. O aluno depois usa a skill "Criar
Apresentacao" para montar decks reais com este modelo como base.

---

### PASSO 4 — Gerar tokens.json e README.md

**`meus-modelos/{nome_modelo}/tokens.json`**:

```json
{
  "nome_modelo": "{nome}",
  "cor_primaria": "{hex}",
  "cor_secundaria": "{hex}",
  "cor_fundo": "{hex}",
  "tom": "{escuro|claro}",
  "fonte_principal": "{nome}",
  "fonte_serif": "{nome|null}",
  "fonte_url": "{url|null}",
  "radius": "{px}",
  "densidade": "{minimalista|balanceado|denso}",
  "rodape_tipo": "{1-4}",
  "rodape_texto": "{texto|null}",
  "transicao": "{1-3}",
  "logo_path": "assets/logo.{ext}",
  "fotos": ["assets/foto1.{ext}", "assets/foto2.{ext}", "assets/foto3.{ext}"],
  "criado_em": "{ISO date}",
  "layouts": 35
}
```

**`meus-modelos/{nome_modelo}/README.md`** — instrucoes para o usuario sobre como
usar, quais tokens foram aplicados, como exportar PDF (Ctrl+P, paisagem, margens zero).

---

### PASSO 5 — Auto-conferencia

**5a. Detectar se Playwright esta disponivel**

> Voce tem a skill `playwright` (validacao visual) instalada? (sim/nao/nao sei)

Se `sim`: abrir template.html headless, capturar screenshots dos slides 1, 11, 20, 35,
salvar em `validacao/`, confirmar OK.

Se `nao`: recomendar instalar (marketplace MeuOs) e oferecer duas opcoes:
- Seguir com checagem estatica apenas
- Pausar, instalar, voltar depois

**5b. Checagem estatica obrigatoria (sempre roda)**

| Verificacao | Erro se falhar |
|-------------|----------------|
| 35 slides no template.html? | "Esperava 35, encontrou X" |
| Cor primaria no CSS? | "Cor primaria nao aplicada" |
| Cor secundaria no CSS? | "Cor secundaria nao aplicada" |
| Fonte aplicada? | "Fonte nao aplicada" |
| Radius aplicado? | "Radius nao aplicado" |
| Nenhum `{{placeholder}}` restante? | "Placeholder nao substituido" |
| Logo referenciada? | "Logo ausente" |
| 3 fotos referenciadas? | "Fotos ausentes" |
| Navegacao JS? | "JS de navegacao ausente" |
| Primeiro slide com `active`? | "Sem slide ativo" |
| Arquivos em assets/? | "Assets nao copiadas" |
| `@page` com `size: 33.867cm 19.05cm` no CSS? | "Bloco @page de impressao ausente — PDF vai sair errado" |
| `@media print` no CSS? | "Bloco @media print ausente — slides vao quebrar no PDF" |
| `print-color-adjust: exact` no CSS? | "Backgrounds vao sumir ao imprimir" |

Se qualquer falha: reportar, pedir ajuste, NAO declarar concluido.

**5c. Se nao tem Playwright, pedir render manual**

> Abra `template.html` no navegador e confirme:
> 1. Capa mostra o titulo?
> 2. Setas do teclado mudam slide?
> 3. Cores estao como queria?
> 4. Logo aparece?
>
> Tudo OK? (sim / algo errado)

---

### PASSO 6 — Relatorio final

```
✓ Modelo de apresentacao criado

Nome: {nome_modelo}
Local: meus-modelos/{nome_modelo}/
Layouts: 35
Cores: {primaria} + {secundaria} em fundo {fundo}
Fonte: {fonte}
Arquivos:
  - template.html ({X} KB)
  - tokens.json
  - README.md
  - assets/logo.{ext} + foto1/2/3

Como usar agora:
1. Abra `meus-modelos/{nome_modelo}/template.html` no navegador
2. Quando quiser criar apresentacao real, rode a skill "Criar Apresentacao"

Quer que eu abra a proxima skill agora? (sim/nao)
```

---

## Se o usuario perguntar "como salvo em PDF?"

> Abra `template.html` no navegador, Ctrl+P (Cmd+P no Mac), "Salvar como PDF",
> orientacao HORIZONTAL, margens ZERO. Em "Mais configuracoes": desmarque "Cabecalho
> e rodape" + marque "Graficos de fundo".

---

## Regras de seguranca

- **Nunca assumir resposta** — sempre perguntar com sugestao padrao
- **Nunca usar URLs web** — exigir paths locais (download automatico OK)
- **Sempre copiar assets para pasta do modelo** — self-contained
- **Nunca gerar sem auto-conferencia** — se falhar, nao declarar pronto
- **Nunca sobrescrever modelo existente sem avisar**
- **Nunca declarar concluido sem os 35 slides**
- **Se o usuario desistir no meio**, salvar progresso parcial em `tmp/`

---

## Integracao com outras skills

- **Criar Apresentacao** — le este modelo e gera apresentacoes reais
- **Fim do Dia** — registra criacao de novo modelo
- **Playwright** — usado para validacao visual (opcional)

---

## BLUEPRINT CANONICO

Este e o gabarito completo que voce deve copiar e adaptar aos tokens do aluno. Ja contem
os 35 slides funcionais com CSS modular, JS de navegacao (setas, espaco, Home/End,
numeros 1-9) e footer dinamico. Os textos sao de uma consultoria ficticia "EMPRESA TESTE
LTDA" — voce NUNCA deve deixar esses textos no HTML final.

<!-- === INICIO BLUEPRINT === -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Modelo de Slides — EMPRESA TESTE LTDA</title>
<link href="https://fonts.googleapis.com/css2?family={{FONTE}}:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --primary: {{COR_PRIMARIA}};
    --primary-light: {{COR_PRIMARIA_LIGHT}};
    --primary-soft: {{COR_PRIMARIA_SOFT}};
    --secondary: {{COR_SECUNDARIA}};
    --secondary-light: {{COR_SECUNDARIA_LIGHT}};
    --secondary-soft: {{COR_SECUNDARIA_SOFT}};
    --bg: {{COR_FUNDO}};
    --card: #ffffff;
    --text: {{COR_TEXTO}};
    --text-muted: {{COR_TEXTO_MUTED}};
    --text-soft: {{COR_TEXTO_SOFT}};
    --border: {{COR_BORDA}};
    --border-strong: {{COR_BORDA_STRONG}};
    --success: #10b981;
    --danger: #ef4444;
    --radius: {{RADIUS}};
    --radius-sm: {{RADIUS_SMALL}};
    --shadow-sm: 0 1px 3px {{SHADOW_RGBA_SM}};
    --shadow: 0 8px 24px {{SHADOW_RGBA}};
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: '{{FONTE}}', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: var(--bg);
    color: var(--text);
    overflow: hidden;
    height: 100vh;
  }

  /* PRINT: cada slide = 1 pagina PDF horizontal exata (16:9 PowerPoint) */
  @page {
    size: 33.867cm 19.05cm;
    margin: 0;
  }
  @media print {
    html, body {
      overflow: visible !important;
      height: auto !important;
      background: var(--bg) !important;
    }
    .slide {
      display: flex !important;
      width: 33.867cm !important;
      height: 19.05cm !important;
      page-break-after: always;
      page-break-inside: avoid;
      break-after: page;
      break-inside: avoid;
      position: relative !important;
    }
    .slide:last-child { page-break-after: auto; break-after: auto; }
    .slide-nav, .slide-num, .slide-footer { display: none !important; }
    * {
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      color-adjust: exact !important;
    }
  }

  /* NAVEGACAO */
  .slide-nav {
    position: fixed; top: 16px; right: 24px; z-index: 1000;
    display: flex; align-items: center; gap: 10px;
    background: var(--card); border: 1px solid var(--border);
    border-radius: 999px; padding: 6px 10px;
    box-shadow: var(--shadow-sm);
    font-size: 14px; color: var(--text-muted);
  }
  .slide-nav button {
    width: 28px; height: 28px; border: none; background: transparent;
    border-radius: 999px; cursor: pointer; font-size: 18px;
    color: var(--primary); font-weight: 700;
  }
  .slide-nav button:hover { background: var(--primary-soft); }
  .slide-nav #counter { font-variant-numeric: tabular-nums; min-width: 44px; text-align: center; }

  .slide-num {
    position: absolute; top: 18px; left: 24px; z-index: 10;
    background: var(--primary); color: #fff;
    width: 36px; height: 36px; border-radius: 999px;
    display: flex; align-items: center; justify-content: center;
    font-weight: 700; font-size: 13px; letter-spacing: 0.5px;
  }

  /* FOOTER */
  .slide-footer {
    position: fixed; bottom: 14px; left: 0; right: 0; z-index: 5;
    text-align: center; font-size: 12px; color: var(--text-soft);
    letter-spacing: 1px; text-transform: uppercase; font-weight: 500;
    pointer-events: none;
  }
  .slide-footer img { height: 18px; vertical-align: middle; margin-right: 10px; opacity: 0.7; }

  /* SLIDE */
  .slide {
    display: none; width: 100vw; height: 100vh;
    padding: 56px 88px 72px; position: relative;
    flex-direction: column; justify-content: center; overflow: hidden;
  }
  .slide.active { display: flex; }

  /* TIPOS DE SLIDE */
  .slide-cover {
    background: var(--card);
    justify-content: center; align-items: center; text-align: center;
  }
  .slide-section {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
    color: #fff;
  }
  .slide-section-accent {
    background: linear-gradient(135deg, var(--secondary) 0%, var(--secondary-light) 100%);
    color: #fff;
  }
  .slide-content { background: var(--bg); }
  .slide-content-alt { background: var(--card); }
  .slide-chat { background: #f1f5f9; }
  .slide-split { flex-direction: row; gap: 56px; align-items: stretch; padding: 56px 88px 72px; }
  .slide-photo-split { padding: 0; flex-direction: row; }
  .slide-photo-full { padding: 0; }

  /* BARRAS LATERAIS */
  .primary-bar {
    position: absolute; left: 0; top: 0; bottom: 0; width: 8px;
    background: linear-gradient(180deg, var(--primary) 0%, var(--primary-light) 100%);
  }
  .secondary-bar {
    position: absolute; left: 0; top: 0; bottom: 0; width: 8px;
    background: linear-gradient(180deg, var(--secondary) 0%, var(--secondary-light) 100%);
  }

  /* DECORACAO */
  .primary-line {
    width: 80px; height: 4px; background: linear-gradient(90deg, var(--primary), var(--secondary));
    border-radius: 2px; margin: 24px 0 0;
  }
  .primary-line-center { margin: 24px auto 0; }

  /* TIPOGRAFIA */
  .label {
    font-size: 13px; letter-spacing: 3px; text-transform: uppercase;
    color: var(--secondary); font-weight: 600; margin-bottom: 14px;
  }
  .label-primary { color: var(--primary); }
  .label-white { color: #fff; opacity: 0.9; }

  .title-hero { font-size: 96px; font-weight: 800; line-height: 0.95; color: var(--primary); letter-spacing: -2px; }
  .title-xl { font-size: 64px; font-weight: 700; line-height: 1.08; color: var(--text); letter-spacing: -1px; }
  .title-lg { font-size: 52px; font-weight: 700; line-height: 1.1; color: var(--text); }
  .title-md { font-size: 40px; font-weight: 700; line-height: 1.2; color: var(--text); }
  .title-sm { font-size: 30px; font-weight: 700; line-height: 1.3; color: var(--text); }
  .title-on-dark { color: #fff; }
  .title-primary { color: var(--primary); }
  .title-secondary { color: var(--secondary); }

  .subtitle { font-size: 24px; color: var(--text-muted); line-height: 1.5; margin-top: 20px; font-weight: 400; }
  .subtitle-on-dark { color: rgba(255,255,255,0.85); }
  .body-xl { font-size: 26px; line-height: 1.6; color: var(--text); font-weight: 400; }
  .body-lg { font-size: 22px; line-height: 1.6; color: var(--text); }
  .body-md { font-size: 20px; line-height: 1.6; color: var(--text); }
  .body-muted { color: var(--text-muted); }

  /* BULLETS */
  .bullet-list { list-style: none; padding: 0; margin-top: 30px; }
  .bullet-list li {
    font-size: 24px; color: var(--text); padding: 14px 0 14px 40px;
    position: relative; line-height: 1.4; border-bottom: 1px solid var(--border);
  }
  .bullet-list li:last-child { border-bottom: none; }
  .bullet-list li::before {
    content: ''; position: absolute; left: 0; top: 50%;
    transform: translateY(-50%); width: 10px; height: 10px;
    background: var(--secondary); border-radius: 999px;
  }
  .bullet-list li strong { color: var(--primary); font-weight: 700; }

  /* HIGHLIGHT BOX */
  .highlight-box {
    background: var(--primary-soft);
    border-left: 6px solid var(--primary);
    border-radius: var(--radius-sm);
    padding: 28px 36px;
    margin-top: 32px;
  }
  .highlight-box p { font-size: 24px; color: var(--primary); line-height: 1.5; font-weight: 500; }
  .highlight-box.accent { background: var(--secondary-soft); border-left-color: var(--secondary); }
  .highlight-box.accent p { color: var(--secondary); }

  /* CARDS */
  .cards-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 32px; }
  .cards-grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-top: 28px; }
  .cards-grid-6 { display: grid; grid-template-columns: 1fr 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 18px; margin-top: 24px; }

  .card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 28px 32px;
    position: relative; overflow: hidden;
    box-shadow: var(--shadow-sm);
  }
  .card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
  }
  .card-sm { padding: 20px 24px; }
  .card-icon {
    width: 48px; height: 48px; border-radius: var(--radius-sm);
    background: var(--primary-soft); color: var(--primary);
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 16px; font-weight: 800; font-size: 20px;
  }
  .card-icon.accent { background: var(--secondary-soft); color: var(--secondary); }
  .card-title { font-size: 22px; font-weight: 700; color: var(--text); margin-bottom: 8px; }
  .card-body { font-size: 17px; color: var(--text-muted); line-height: 1.5; }
  .card-body-sm { font-size: 15px; color: var(--text-muted); line-height: 1.4; }

  /* RULE LIST */
  .rule-list { display: flex; flex-direction: column; gap: 18px; margin-top: 32px; }
  .rule-item {
    background: var(--card); border-left: 5px solid var(--secondary);
    border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    padding: 20px 28px;
    box-shadow: var(--shadow-sm);
  }
  .rule-title { font-size: 22px; font-weight: 700; color: var(--primary); margin-bottom: 4px; }
  .rule-body { font-size: 18px; color: var(--text-muted); line-height: 1.4; }

  /* CHECK LIST */
  .check-list { list-style: none; margin-top: 28px; }
  .check-list li {
    font-size: 22px; padding: 14px 0 14px 44px; position: relative;
    border-bottom: 1px solid var(--border); color: var(--text); line-height: 1.4;
  }
  .check-list li:last-child { border-bottom: none; }
  .check-list li::before {
    content: '\2713'; position: absolute; left: 0; top: 50%;
    transform: translateY(-50%); color: var(--success);
    font-weight: 900; font-size: 22px;
  }

  /* CHAT */
  .chat-container {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 28px 32px; margin-top: 24px;
    box-shadow: var(--shadow-sm);
  }
  .chat-msg { margin-bottom: 20px; display: flex; align-items: flex-start; gap: 14px; }
  .chat-msg:last-child { margin-bottom: 0; }
  .chat-avatar {
    width: 40px; height: 40px; border-radius: 999px;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px; flex-shrink: 0; font-weight: 700;
  }
  .av-user { background: var(--primary-soft); color: var(--primary); }
  .av-ai { background: var(--secondary-soft); color: var(--secondary); }
  .chat-right { flex: 1; }
  .chat-name {
    font-size: 12px; color: var(--text-muted); margin-bottom: 6px;
    font-weight: 700; letter-spacing: 1px; text-transform: uppercase;
  }
  .chat-bubble {
    border-radius: var(--radius-sm); padding: 16px 20px;
    font-size: 18px; line-height: 1.55; color: var(--text);
  }
  .bubble-user { background: var(--primary-soft); }
  .bubble-ai { background: var(--secondary-soft); }
  .bubble-ai strong { color: var(--secondary); }

  /* COMPARACAO */
  .compare-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 30px; }
  .compare-col {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 28px 32px;
    box-shadow: var(--shadow-sm);
  }
  .compare-title {
    font-size: 15px; font-weight: 700; letter-spacing: 2px;
    text-transform: uppercase; margin-bottom: 18px;
    padding-bottom: 12px; border-bottom: 1px solid var(--border);
  }
  .compare-bad { color: var(--danger); }
  .compare-good { color: var(--success); }
  .compare-item {
    display: flex; align-items: flex-start; gap: 12px;
    margin-bottom: 14px; font-size: 18px; color: var(--text); line-height: 1.4;
  }
  .compare-item .dot-bad { color: var(--danger); font-size: 22px; flex-shrink: 0; font-weight: 800; }
  .compare-item .dot-good { color: var(--success); font-size: 22px; flex-shrink: 0; font-weight: 800; }

  /* ROI / STATS */
  .roi-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 30px; }
  .roi-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 28px 32px; position: relative;
    box-shadow: var(--shadow-sm);
  }
  .roi-card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
    background: var(--secondary);
  }
  .roi-label {
    font-size: 13px; color: var(--text-muted);
    letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px;
  }
  .roi-value { font-size: 44px; font-weight: 800; color: var(--primary); line-height: 1; }
  .roi-value.accent { color: var(--secondary); }
  .roi-desc { font-size: 16px; color: var(--text-muted); margin-top: 8px; line-height: 1.4; }

  .stat-row { display: flex; gap: 28px; margin-top: 36px; }
  .stat-box {
    flex: 1; background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 26px; text-align: center;
    box-shadow: var(--shadow-sm);
  }
  .stat-value { font-size: 48px; font-weight: 800; color: var(--primary); line-height: 1; }
  .stat-value.accent { color: var(--secondary); }
  .stat-label { font-size: 15px; color: var(--text-muted); margin-top: 10px; line-height: 1.3; }

  /* TABELA */
  .table-wrap {
    margin-top: 28px; overflow: hidden;
    border-radius: var(--radius); border: 1px solid var(--border);
    box-shadow: var(--shadow-sm); background: var(--card);
  }
  table { width: 100%; border-collapse: collapse; }
  th {
    background: var(--primary); padding: 16px 22px; text-align: left;
    font-size: 14px; letter-spacing: 1.5px; text-transform: uppercase;
    color: #fff; font-weight: 600;
  }
  td { padding: 16px 22px; font-size: 18px; color: var(--text); border-bottom: 1px solid var(--border); }
  tr:last-child td { border-bottom: none; }
  tr:nth-child(even) td { background: #f8fafc; }

  /* TIMELINE */
  .timeline-horizontal {
    display: flex; align-items: flex-start; gap: 8px; margin-top: 32px;
    position: relative;
  }
  .timeline-horizontal::before {
    content: ''; position: absolute; top: 22px; left: 24px; right: 24px;
    height: 3px; background: linear-gradient(90deg, var(--primary), var(--secondary));
    border-radius: 2px; z-index: 0;
  }
  .timeline-step {
    flex: 1; display: flex; flex-direction: column; align-items: center;
    text-align: center; position: relative; z-index: 1;
  }
  .timeline-dot {
    width: 46px; height: 46px; border-radius: 999px; background: var(--card);
    border: 4px solid var(--primary); display: flex; align-items: center;
    justify-content: center; font-weight: 800; color: var(--primary);
    font-size: 18px; margin-bottom: 12px;
    box-shadow: var(--shadow-sm);
  }
  .timeline-dot.accent { border-color: var(--secondary); color: var(--secondary); }
  .timeline-title { font-size: 17px; font-weight: 700; color: var(--text); margin-bottom: 4px; }
  .timeline-desc { font-size: 14px; color: var(--text-muted); line-height: 1.4; }

  /* STEPS */
  .steps-h { display: flex; gap: 20px; margin-top: 32px; }
  .step { flex: 1; text-align: center; position: relative; }
  .step-num {
    width: 58px; height: 58px; border-radius: 999px;
    background: linear-gradient(135deg, var(--primary), var(--primary-light));
    color: #fff; display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 22px; margin: 0 auto 14px;
    box-shadow: var(--shadow);
  }
  .step-num.accent { background: linear-gradient(135deg, var(--secondary), var(--secondary-light)); }
  .step-title { font-size: 18px; font-weight: 700; color: var(--text); margin-bottom: 6px; }
  .step-desc { font-size: 14px; color: var(--text-muted); line-height: 1.4; }

  /* FLOW */
  .flow { display: flex; align-items: center; gap: 0; margin-top: 36px; flex-wrap: nowrap; justify-content: center; }
  .flow-box {
    background: var(--card); border: 2px solid var(--primary);
    border-radius: var(--radius-sm); padding: 18px 24px;
    text-align: center; min-width: 150px;
    box-shadow: var(--shadow-sm);
  }
  .flow-box.accent { border-color: var(--secondary); }
  .flow-box.success { border-color: var(--success); }
  .flow-box-title { font-size: 16px; font-weight: 700; color: var(--text); }
  .flow-box-sub { font-size: 12px; color: var(--text-muted); margin-top: 4px; }
  .flow-arrow { font-size: 28px; color: var(--secondary); padding: 0 10px; font-weight: 700; }

  /* TOC */
  .toc { margin-top: 34px; }
  .toc-item {
    display: flex; align-items: baseline; gap: 18px;
    padding: 18px 0; border-bottom: 1px solid var(--border);
  }
  .toc-num { font-size: 32px; font-weight: 800; color: var(--secondary); min-width: 58px; font-variant-numeric: tabular-nums; }
  .toc-content { flex: 1; }
  .toc-title { font-size: 24px; font-weight: 700; color: var(--text); }
  .toc-desc { font-size: 15px; color: var(--text-muted); margin-top: 4px; }

  /* SECTION NUMBER */
  .section-number {
    font-size: 200px; font-weight: 800; color: rgba(255,255,255,0.12);
    position: absolute; right: 80px; bottom: 40px; line-height: 1;
    letter-spacing: -6px;
  }
  .section-content { position: relative; z-index: 2; }

  /* PHOTO */
  .photo-half {
    flex: 1; height: 100%;
    background-size: cover; background-position: center;
  }
  .text-half {
    flex: 1; padding: 64px 72px;
    display: flex; flex-direction: column; justify-content: center;
    background: var(--card);
  }
  .photo-full-bg {
    position: absolute; inset: 0; background-size: cover; background-position: center;
  }
  .photo-overlay {
    position: absolute; inset: 0;
    background: linear-gradient(135deg, {{OVERLAY_RGBA_STRONG}}, {{OVERLAY_RGBA_MED}});
    display: flex; flex-direction: column; justify-content: center;
    padding: 56px 88px; color: #fff;
  }
  .photo-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); overflow: hidden;
    box-shadow: var(--shadow-sm);
  }
  .photo-card img { width: 100%; height: 180px; object-fit: cover; display: block; }
  .photo-card-body { padding: 18px 22px; }
  .photo-inset {
    border-radius: var(--radius); overflow: hidden;
    box-shadow: var(--shadow); flex-shrink: 0;
  }
  .photo-top {
    position: absolute; top: 0; left: 0; right: 0; height: 40vh;
    background-size: cover; background-position: center;
  }
  .photo-top::after {
    content: ''; position: absolute; left: 0; right: 0; bottom: 0; height: 40%;
    background: linear-gradient(180deg, transparent, var(--bg));
  }
  .photo-top-content { position: absolute; top: 42vh; left: 88px; right: 88px; bottom: 72px; }

  /* CHARTS */
  .chart-bars {
    display: flex; align-items: flex-end; gap: 28px;
    height: 240px; margin-top: 32px; padding: 0 20px;
  }
  .chart-bar-col {
    flex: 1; display: flex; flex-direction: column;
    align-items: center; gap: 10px;
  }
  .chart-bar {
    width: 100%; border-radius: var(--radius-sm) var(--radius-sm) 0 0;
    background: linear-gradient(180deg, var(--primary), var(--primary-light));
    position: relative;
  }
  .chart-bar.accent { background: linear-gradient(180deg, var(--secondary), var(--secondary-light)); }
  .chart-bar-label { font-size: 14px; color: var(--text-muted); text-align: center; }
  .chart-bar-value { font-size: 16px; font-weight: 700; color: var(--text); }

  .chart-donuts { display: flex; gap: 60px; justify-content: center; margin-top: 40px; align-items: center; }
  .chart-donut-wrap { text-align: center; }
  .chart-donut {
    width: 170px; height: 170px; border-radius: 999px;
    position: relative; display: flex; align-items: center; justify-content: center;
  }
  .chart-donut-inner {
    width: 110px; height: 110px; border-radius: 999px;
    background: var(--bg);
    display: flex; align-items: center; justify-content: center;
    font-size: 30px; font-weight: 800; color: var(--primary);
  }
  .chart-donut-label { font-size: 15px; color: var(--text-muted); margin-top: 14px; font-weight: 500; }

  .progress-wrap { margin-top: 30px; }
  .progress-item { margin-bottom: 22px; }
  .progress-header { display: flex; justify-content: space-between; margin-bottom: 8px; }
  .progress-name { font-size: 18px; color: var(--text); font-weight: 600; }
  .progress-pct { font-size: 18px; color: var(--primary); font-weight: 800; }
  .progress-track { height: 14px; background: var(--border); border-radius: 999px; overflow: hidden; }
  .progress-fill { height: 100%; border-radius: 999px; }

  .multi-chart {
    display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 28px;
  }
  .chart-box {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 22px;
    box-shadow: var(--shadow-sm);
  }
  .chart-box-title {
    font-size: 14px; color: var(--text-muted);
    letter-spacing: 1.5px; text-transform: uppercase;
    margin-bottom: 14px; font-weight: 600;
  }
  .chart-box-value { font-size: 36px; font-weight: 800; color: var(--primary); margin-bottom: 6px; }
  .chart-mini-bars { display: flex; align-items: flex-end; gap: 6px; height: 56px; }
  .chart-mini-bar { flex: 1; background: var(--primary-light); border-radius: 4px 4px 0 0; }

  /* BIG NUMBER */
  .big-number {
    font-size: 200px; font-weight: 800; color: var(--primary);
    line-height: 1; letter-spacing: -6px; text-align: center;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .big-number-label {
    font-size: 24px; color: var(--text-muted); text-align: center;
    margin-top: 16px; max-width: 700px; line-height: 1.4;
  }

  /* QUOTE */
  .quote-slide { text-align: center; }
  .quote-mark {
    font-size: 120px; color: var(--secondary); line-height: 0.5;
    font-family: Georgia, serif; font-weight: 800;
  }
  .quote-text {
    font-size: 42px; font-weight: 500; line-height: 1.35;
    color: var(--text); max-width: 1000px; margin: 0 auto; font-style: italic;
  }
  .quote-author {
    font-size: 20px; color: var(--text-muted); margin-top: 28px;
    letter-spacing: 1px;
  }
  .quote-author strong { color: var(--primary); font-weight: 700; }

  /* PRICING */
  .pricing-grid {
    display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px;
    margin-top: 36px; align-items: stretch;
  }
  .pricing-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 32px 28px;
    display: flex; flex-direction: column;
    box-shadow: var(--shadow-sm);
  }
  .pricing-card.featured {
    border-color: var(--primary); border-width: 2px;
    transform: scale(1.05);
    box-shadow: var(--shadow);
  }
  .pricing-badge {
    display: inline-block; background: var(--secondary); color: #fff;
    font-size: 11px; letter-spacing: 2px; text-transform: uppercase;
    font-weight: 700; padding: 4px 14px; border-radius: 999px;
    margin-bottom: 14px; align-self: flex-start;
  }
  .pricing-name { font-size: 20px; font-weight: 700; color: var(--primary); margin-bottom: 8px; }
  .pricing-price { font-size: 44px; font-weight: 800; color: var(--text); line-height: 1; }
  .pricing-price .small { font-size: 18px; color: var(--text-muted); font-weight: 500; }
  .pricing-desc { font-size: 14px; color: var(--text-muted); margin-top: 8px; }
  .pricing-features { list-style: none; padding: 0; margin: 20px 0; flex: 1; }
  .pricing-features li {
    font-size: 15px; color: var(--text); padding: 8px 0 8px 28px;
    position: relative; line-height: 1.4;
  }
  .pricing-features li::before {
    content: '\2713'; position: absolute; left: 0; top: 8px;
    color: var(--success); font-weight: 900;
  }
  .pricing-cta {
    display: block; text-align: center; padding: 14px;
    background: var(--primary); color: #fff; border-radius: var(--radius-sm);
    text-decoration: none; font-weight: 700; font-size: 15px;
  }
  .pricing-card.featured .pricing-cta { background: var(--secondary); }

  /* CTA */
  .cta-slide {
    text-align: center;
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 50%, var(--secondary) 100%);
    color: #fff; justify-content: center; align-items: center;
  }
  .cta-title { font-size: 72px; font-weight: 800; line-height: 1.05; color: #fff; letter-spacing: -1px; max-width: 1000px; }
  .cta-sub { font-size: 24px; color: rgba(255,255,255,0.9); margin-top: 20px; max-width: 800px; line-height: 1.5; }
  .cta-button {
    display: inline-block; margin-top: 40px; padding: 20px 48px;
    background: #fff; color: var(--primary); border-radius: 999px;
    font-weight: 800; font-size: 20px; text-decoration: none;
    letter-spacing: 0.5px; box-shadow: 0 16px 40px rgba(0,0,0,0.25);
  }

  /* LOGO IN COVER */
  .cover-logo { width: 280px; height: auto; margin-bottom: 40px; }
  .cover-logo-small { width: 160px; height: auto; margin-bottom: 24px; }

  /* UTILS */
  .spacer-sm { height: 16px; }
  .spacer { height: 32px; }
  .flex-between { display: flex; justify-content: space-between; align-items: center; }
</style>
</head>
<body>

<nav class="slide-nav">
  <button id="prev" aria-label="Anterior">&#8249;</button>
  <span id="counter">1 / 35</span>
  <button id="next" aria-label="Proximo">&#8250;</button>
</nav>

<!-- =================================================================== -->
<!-- SLIDE 1 — Portada completa -->
<div class="slide slide-cover active">
  <div class="slide-num">1</div>
  <img src="assets/logo.svg" class="cover-logo" alt="Logo">
  <div class="label label-primary">APRESENTACAO CORPORATIVA 2026</div>
  <h1 class="title-hero">Transformacao<br>em <span style="color:var(--secondary);">5 passos</span></h1>
  <div class="subtitle" style="max-width:700px; text-align:center;">Como a EMPRESA TESTE LTDA acelera resultados de gestao com dados, processos e IA aplicada.</div>
  <div class="primary-line primary-line-center"></div>
</div>

<!-- SLIDE 2 — Cover centralizada minimalista -->
<div class="slide slide-cover" style="background: linear-gradient(135deg, var(--primary), var(--primary-light)); color:#fff;">
  <div class="slide-num">2</div>
  <img src="assets/logo.svg" class="cover-logo-small" alt="Logo" style="filter:brightness(0) invert(1);">
  <h1 class="title-hero title-on-dark" style="color:#fff; text-align:center;">EMPRESA TESTE<br><span style="color:var(--secondary-light);">LTDA</span></h1>
  <div class="subtitle subtitle-on-dark" style="text-align:center; margin-top:28px;">Consultoria em gestao, dados e inteligencia artificial</div>
</div>

<!-- SLIDE 3 — Indice / TOC -->
<div class="slide slide-content">
  <div class="slide-num">3</div>
  <div class="primary-bar"></div>
  <div class="label label-primary">O QUE VOCE VAI VER</div>
  <h2 class="title-lg">Indice</h2>
  <div class="toc">
    <div class="toc-item">
      <div class="toc-num">01</div>
      <div class="toc-content">
        <div class="toc-title">Diagnostico do cenario</div>
        <div class="toc-desc">Onde estao as perdas hoje e o que os dados mostram</div>
      </div>
    </div>
    <div class="toc-item">
      <div class="toc-num">02</div>
      <div class="toc-content">
        <div class="toc-title">Proposta e metodo</div>
        <div class="toc-desc">Abordagem em 5 passos aplicada ao seu contexto</div>
      </div>
    </div>
    <div class="toc-item">
      <div class="toc-num">03</div>
      <div class="toc-content">
        <div class="toc-title">Resultados e evidencias</div>
        <div class="toc-desc">Numeros de casos anteriores e projecao para voce</div>
      </div>
    </div>
    <div class="toc-item">
      <div class="toc-num">04</div>
      <div class="toc-content">
        <div class="toc-title">Investimento e proximos passos</div>
        <div class="toc-desc">Como comecamos, quanto custa, quando voce ve retorno</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 4 — Divisoria de secao com numero grande -->
<div class="slide slide-section">
  <div class="slide-num">4</div>
  <div class="section-content">
    <div class="label label-white">PARTE 1</div>
    <h2 class="title-xl title-on-dark">Diagnostico<br>do cenario</h2>
    <div style="font-size:22px; color:rgba(255,255,255,0.85); margin-top:20px; max-width:600px;">
      Onde estao as perdas, o que os dados mostram e por que o processo atual trava.
    </div>
  </div>
  <div class="section-number">01</div>
</div>

<!-- SLIDE 5 — Conteudo com 3 bullets -->
<div class="slide slide-content">
  <div class="slide-num">5</div>
  <div class="primary-bar"></div>
  <div class="label">3 SINTOMAS RECORRENTES</div>
  <h2 class="title-md">Os tres pontos de dor que aparecem em 9 de cada 10 diagnosticos</h2>
  <ul class="bullet-list">
    <li><strong>Dados dispersos</strong> em 4 a 6 sistemas diferentes, sem fonte unica de verdade</li>
    <li><strong>Decisoes no escuro</strong> — diretoria gasta tempo validando numero ao inves de decidir</li>
    <li><strong>Processos manuais</strong> consomem 30 a 40% do tempo do time operacional</li>
  </ul>
</div>

<!-- SLIDE 6 — Highlight box -->
<div class="slide slide-content-alt">
  <div class="slide-num">6</div>
  <div class="secondary-bar"></div>
  <div class="label">O CUSTO DA INACAO</div>
  <h2 class="title-md">Cada mes sem dados confiaveis custa decisoes</h2>
  <div class="highlight-box accent">
    <p>"Empresas que operam no escuro tomam 3x mais decisoes ruins — e o impacto compound ao longo do ano equivale a perder um trimestre inteiro de receita."</p>
  </div>
  <div class="spacer"></div>
  <div class="body-muted" style="font-size:17px;">Fonte: levantamento interno com 47 empresas medias, 2023-2025 (dados ficticios).</div>
</div>

<!-- SLIDE 7 — 2 cards -->
<div class="slide slide-content">
  <div class="slide-num">7</div>
  <div class="primary-bar"></div>
  <div class="label">DOIS CAMINHOS</div>
  <h2 class="title-md">O que separa empresas que avancam das que travam</h2>
  <div class="cards-grid">
    <div class="card">
      <div class="card-icon">A</div>
      <div class="card-title">Quem avanca</div>
      <div class="card-body">Padroniza dados, automatiza o operacional e libera o time para decisao. Foco em insight acionavel, nao relatorio bonito.</div>
    </div>
    <div class="card">
      <div class="card-icon accent">B</div>
      <div class="card-title">Quem trava</div>
      <div class="card-body">Continua colando planilha em planilha, tratando sintoma em vez de causa. Discute dado em vez de estrategia.</div>
    </div>
  </div>
</div>

<!-- SLIDE 8 — Rule list -->
<div class="slide slide-content-alt">
  <div class="slide-num">8</div>
  <div class="primary-bar"></div>
  <div class="label">4 PRINCIPIOS INEGOCIAVEIS</div>
  <h2 class="title-md">Como trabalhamos</h2>
  <div class="rule-list">
    <div class="rule-item">
      <div class="rule-title">1. Fonte unica de verdade</div>
      <div class="rule-body">Toda area da empresa olhando para o mesmo numero, atualizado automaticamente.</div>
    </div>
    <div class="rule-item">
      <div class="rule-title">2. Automacao antes de ferramenta nova</div>
      <div class="rule-body">Resolver o processo primeiro, depois escolher o software certo — nunca o contrario.</div>
    </div>
    <div class="rule-item">
      <div class="rule-title">3. Time treinado, nao dependente</div>
      <div class="rule-body">Voce sai do projeto com autonomia. Nao vendemos dependencia.</div>
    </div>
    <div class="rule-item">
      <div class="rule-title">4. ROI mensuravel em 90 dias</div>
      <div class="rule-body">Se nao conseguirmos provar retorno em 3 meses, voce nao paga o saldo final.</div>
    </div>
  </div>
</div>

<!-- SLIDE 9 — 3 cards -->
<div class="slide slide-content">
  <div class="slide-num">9</div>
  <div class="primary-bar"></div>
  <div class="label">TRES PILARES</div>
  <h2 class="title-md">O metodo em tres frentes simultaneas</h2>
  <div class="cards-grid-3">
    <div class="card">
      <div class="card-icon">D</div>
      <div class="card-title">Dados</div>
      <div class="card-body">Centralizar, limpar e versionar. Do operacional ate a camada executiva.</div>
    </div>
    <div class="card">
      <div class="card-icon accent">P</div>
      <div class="card-title">Processos</div>
      <div class="card-body">Automatizar o repetitivo. Documentar o critico. Treinar o time.</div>
    </div>
    <div class="card">
      <div class="card-icon">IA</div>
      <div class="card-title">Inteligencia</div>
      <div class="card-body">IA aplicada em pontos de alavancagem real — nao em demo de laboratorio.</div>
    </div>
  </div>
</div>

<!-- SLIDE 10 — 6 cards grid 3x2 -->
<div class="slide slide-content-alt">
  <div class="slide-num">10</div>
  <div class="primary-bar"></div>
  <div class="label">AREAS DE ATUACAO</div>
  <h2 class="title-md">Seis dominios onde entregamos resultado</h2>
  <div class="cards-grid-6">
    <div class="card card-sm">
      <div class="card-icon">F</div>
      <div class="card-title" style="font-size:18px;">Financeiro</div>
      <div class="card-body-sm">DRE automatizado, fluxo de caixa ao vivo, cenarios.</div>
    </div>
    <div class="card card-sm">
      <div class="card-icon accent">C</div>
      <div class="card-title" style="font-size:18px;">Comercial</div>
      <div class="card-body-sm">Pipeline, forecast, atribuicao de receita.</div>
    </div>
    <div class="card card-sm">
      <div class="card-icon">M</div>
      <div class="card-title" style="font-size:18px;">Marketing</div>
      <div class="card-body-sm">CAC, LTV, funil integrado, ROI por canal.</div>
    </div>
    <div class="card card-sm">
      <div class="card-icon accent">O</div>
      <div class="card-title" style="font-size:18px;">Operacoes</div>
      <div class="card-body-sm">Produtividade, SLA, custo por unidade.</div>
    </div>
    <div class="card card-sm">
      <div class="card-icon">P</div>
      <div class="card-title" style="font-size:18px;">Pessoas</div>
      <div class="card-body-sm">Headcount, turnover, engajamento.</div>
    </div>
    <div class="card card-sm">
      <div class="card-icon accent">E</div>
      <div class="card-title" style="font-size:18px;">Executivo</div>
      <div class="card-body-sm">Paineis de diretoria, comite mensal, OKRs.</div>
    </div>
  </div>
</div>

<!-- SLIDE 11 — Divisoria colorida -->
<div class="slide slide-section-accent">
  <div class="slide-num">11</div>
  <div class="section-content">
    <div class="label label-white">PARTE 2</div>
    <h2 class="title-xl title-on-dark">Proposta<br>e metodo</h2>
    <div style="font-size:22px; color:rgba(255,255,255,0.9); margin-top:20px; max-width:600px;">
      Como aplicamos o metodo de 5 passos no seu contexto, em 90 dias.
    </div>
  </div>
  <div class="section-number">02</div>
</div>

<!-- SLIDE 12 — Flow diagram -->
<div class="slide slide-content">
  <div class="slide-num">12</div>
  <div class="primary-bar"></div>
  <div class="label">METODO EM 5 PASSOS</div>
  <h2 class="title-md">Como a transformacao acontece</h2>
  <div class="flow">
    <div class="flow-box">
      <div class="flow-box-title">Diagnostico</div>
      <div class="flow-box-sub">Semana 1-2</div>
    </div>
    <div class="flow-arrow">&#8250;</div>
    <div class="flow-box accent">
      <div class="flow-box-title">Arquitetura</div>
      <div class="flow-box-sub">Semana 3-4</div>
    </div>
    <div class="flow-arrow">&#8250;</div>
    <div class="flow-box">
      <div class="flow-box-title">Implementacao</div>
      <div class="flow-box-sub">Semana 5-10</div>
    </div>
    <div class="flow-arrow">&#8250;</div>
    <div class="flow-box accent">
      <div class="flow-box-title">Validacao</div>
      <div class="flow-box-sub">Semana 11-12</div>
    </div>
    <div class="flow-arrow">&#8250;</div>
    <div class="flow-box success">
      <div class="flow-box-title">Autonomia</div>
      <div class="flow-box-sub">Ongoing</div>
    </div>
  </div>
  <div class="highlight-box" style="margin-top:48px;">
    <p>90 dias para sair de "onde estamos travados" para "o time conduz sozinho".</p>
  </div>
</div>

<!-- SLIDE 13 — Stats / ROI -->
<div class="slide slide-content-alt">
  <div class="slide-num">13</div>
  <div class="primary-bar"></div>
  <div class="label">NUMEROS DE CASOS ANTERIORES</div>
  <h2 class="title-md">Resultados medios apos 90 dias</h2>
  <div class="roi-grid">
    <div class="roi-card">
      <div class="roi-label">Reducao de tempo operacional</div>
      <div class="roi-value">-38%</div>
      <div class="roi-desc">Automacao de processos repetitivos libera o time</div>
    </div>
    <div class="roi-card">
      <div class="roi-label">Aumento em decisoes baseadas em dado</div>
      <div class="roi-value accent">+3.2x</div>
      <div class="roi-desc">Diretoria passa a decidir com numero, nao com sensacao</div>
    </div>
    <div class="roi-card">
      <div class="roi-label">ROI medio no primeiro ano</div>
      <div class="roi-value">4.7x</div>
      <div class="roi-desc">Investimento pago em ate 4 meses na maioria dos casos</div>
    </div>
    <div class="roi-card">
      <div class="roi-label">Satisfacao do time</div>
      <div class="roi-value accent">92%</div>
      <div class="roi-desc">Menos retrabalho, mais foco em atividades de alto valor</div>
    </div>
  </div>
</div>

<!-- SLIDE 14 — Tabela -->
<div class="slide slide-content">
  <div class="slide-num">14</div>
  <div class="primary-bar"></div>
  <div class="label">COMPARATIVO DE ABORDAGENS</div>
  <h2 class="title-md">O que diferencia o metodo EMPRESA TESTE</h2>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Criterio</th>
          <th>Consultoria tradicional</th>
          <th>Metodo EMPRESA TESTE</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Prazo ate primeiro resultado</td><td>6-12 meses</td><td>30-60 dias</td></tr>
        <tr><td>Dependencia pos-projeto</td><td>Alta (retencao continua)</td><td>Zero (time autonomo)</td></tr>
        <tr><td>Modelo de cobranca</td><td>Hora tecnica</td><td>Resultado + sucesso</td></tr>
        <tr><td>Uso de IA</td><td>Discurso</td><td>Implementacao real</td></tr>
        <tr><td>Garantia de ROI</td><td>Nenhuma</td><td>90 dias ou saldo nao e cobrado</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- SLIDE 15 — Comparacao 2 colunas -->
<div class="slide slide-content-alt">
  <div class="slide-num">15</div>
  <div class="primary-bar"></div>
  <div class="label">ANTES VS DEPOIS</div>
  <h2 class="title-md">O que muda para a diretoria em 90 dias</h2>
  <div class="compare-grid">
    <div class="compare-col">
      <div class="compare-title compare-bad">ANTES</div>
      <div class="compare-item"><span class="dot-bad">&#10005;</span><span>Reuniao de comite gasta 70% do tempo validando numero</span></div>
      <div class="compare-item"><span class="dot-bad">&#10005;</span><span>Cada area com sua versao da verdade</span></div>
      <div class="compare-item"><span class="dot-bad">&#10005;</span><span>Decisao urgente espera 2 dias de consolidacao manual</span></div>
      <div class="compare-item"><span class="dot-bad">&#10005;</span><span>IA e tema de palestra, nao de operacao</span></div>
    </div>
    <div class="compare-col">
      <div class="compare-title compare-good">DEPOIS</div>
      <div class="compare-item"><span class="dot-good">&#10003;</span><span>Comite foca em estrategia — numero ja chega validado</span></div>
      <div class="compare-item"><span class="dot-good">&#10003;</span><span>Fonte unica consultada por todos em tempo real</span></div>
      <div class="compare-item"><span class="dot-good">&#10003;</span><span>Decisao com dado fresco em minutos, nao dias</span></div>
      <div class="compare-item"><span class="dot-good">&#10003;</span><span>IA rodando em producao, reduzindo custos mensurados</span></div>
    </div>
  </div>
</div>

<!-- SLIDE 16 — Timeline horizontal -->
<div class="slide slide-content">
  <div class="slide-num">16</div>
  <div class="primary-bar"></div>
  <div class="label">CRONOGRAMA DE 90 DIAS</div>
  <h2 class="title-md">Como se distribui ao longo do projeto</h2>
  <div class="timeline-horizontal">
    <div class="timeline-step">
      <div class="timeline-dot">1</div>
      <div class="timeline-title">Dias 1-14</div>
      <div class="timeline-desc">Diagnostico profundo + entrevistas com lideres</div>
    </div>
    <div class="timeline-step">
      <div class="timeline-dot accent">2</div>
      <div class="timeline-title">Dias 15-30</div>
      <div class="timeline-desc">Arquitetura de dados e priorizacao de fluxos</div>
    </div>
    <div class="timeline-step">
      <div class="timeline-dot">3</div>
      <div class="timeline-title">Dias 31-60</div>
      <div class="timeline-desc">Implementacao e integracao dos sistemas</div>
    </div>
    <div class="timeline-step">
      <div class="timeline-dot accent">4</div>
      <div class="timeline-title">Dias 61-80</div>
      <div class="timeline-desc">Validacao, ajustes e treinamento do time</div>
    </div>
    <div class="timeline-step">
      <div class="timeline-dot">5</div>
      <div class="timeline-title">Dias 81-90</div>
      <div class="timeline-desc">Handoff, documentacao e autonomia total</div>
    </div>
  </div>
</div>

<!-- SLIDE 17 — Chat/Dialogo -->
<div class="slide slide-chat">
  <div class="slide-num">17</div>
  <div class="primary-bar"></div>
  <div class="label">COMO USAMOS IA NO DIA A DIA</div>
  <h2 class="title-md">Exemplo real: consulta de diretoria em 30 segundos</h2>
  <div class="chat-container">
    <div class="chat-msg">
      <div class="chat-avatar av-user">CEO</div>
      <div class="chat-right">
        <div class="chat-name">Diretor Geral</div>
        <div class="chat-bubble bubble-user">Por que a margem caiu 4 pontos no mes passado?</div>
      </div>
    </div>
    <div class="chat-msg">
      <div class="chat-avatar av-ai">AI</div>
      <div class="chat-right">
        <div class="chat-name">Assistente de Dados</div>
        <div class="chat-bubble bubble-ai">A queda e explicada por <strong>3 fatores</strong>: aumento de 7% no custo de frete (fornecedor X), mix de vendas deslocado para produtos de menor margem (-2.1 pp) e campanha promocional abaixo do forecast (-1.2 pp). Quer ver o detalhamento por SKU?</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 18 — Steps numerados -->
<div class="slide slide-content-alt">
  <div class="slide-num">18</div>
  <div class="primary-bar"></div>
  <div class="label">COMO COMECAMOS JUNTOS</div>
  <h2 class="title-md">4 passos para iniciar</h2>
  <div class="steps-h">
    <div class="step">
      <div class="step-num">1</div>
      <div class="step-title">Call de 45 min</div>
      <div class="step-desc">Entendemos seu cenario e desafios principais</div>
    </div>
    <div class="step">
      <div class="step-num accent">2</div>
      <div class="step-title">Diagnostico gratuito</div>
      <div class="step-desc">Proposta personalizada com escopo e investimento</div>
    </div>
    <div class="step">
      <div class="step-num">3</div>
      <div class="step-title">Aprovacao e kickoff</div>
      <div class="step-desc">Inicio em ate 7 dias da assinatura do contrato</div>
    </div>
    <div class="step">
      <div class="step-num accent">4</div>
      <div class="step-title">Execucao em 90 dias</div>
      <div class="step-desc">Voce ve resultado em 30, autonomia total em 90</div>
    </div>
  </div>
</div>

<!-- SLIDE 19 — Divisoria minimalista -->
<div class="slide slide-section">
  <div class="slide-num">19</div>
  <div class="section-content" style="max-width:1000px;">
    <div class="label label-white">PARTE 3</div>
    <h2 class="title-xl title-on-dark">Resultados<br>e evidencias</h2>
  </div>
</div>

<!-- SLIDE 20 — Foto + texto split -->
<div class="slide slide-photo-split">
  <div class="slide-num">20</div>
  <div class="text-half">
    <div class="label">CASO 1</div>
    <h2 class="title-md">Varejo multi-canal com 12 lojas em 4 estados</h2>
    <div class="body-md" style="margin-top:20px; color:var(--text-muted);">
      Empresa familiar na segunda geracao, crescendo 18% ao ano, mas com decisoes travadas por relatorios semanais do financeiro.
    </div>
    <div class="highlight-box accent" style="margin-top:28px;">
      <p>De 5 dias para 5 minutos no fechamento gerencial.</p>
    </div>
  </div>
  <div class="photo-half" style="background-image: url('assets/foto1.svg');"></div>
</div>

<!-- SLIDE 21 — Texto + foto split invertido -->
<div class="slide slide-photo-split">
  <div class="slide-num">21</div>
  <div class="photo-half" style="background-image: url('assets/foto2.svg');"></div>
  <div class="text-half">
    <div class="label">CASO 2</div>
    <h2 class="title-md">SaaS B2B com 2.400 clientes ativos</h2>
    <div class="body-md" style="margin-top:20px; color:var(--text-muted);">
      Crescimento rapido, mas churn subindo sem explicacao clara. Diretoria perdida sobre onde intervir primeiro.
    </div>
    <div class="highlight-box" style="margin-top:28px;">
      <p>Churn reduzido de 4.1% para 2.3% em 60 dias apos identificar padroes de uso.</p>
    </div>
  </div>
</div>

<!-- SLIDE 22 — Foto full + overlay -->
<div class="slide slide-photo-full">
  <div class="slide-num">22</div>
  <div class="photo-full-bg" style="background-image: url('assets/foto1.svg');"></div>
  <div class="photo-overlay">
    <div class="label label-white">CASO 3</div>
    <h2 class="title-xl title-on-dark" style="max-width:900px;">Industria com 320 funcionarios e 3 plantas</h2>
    <div class="body-lg" style="color:rgba(255,255,255,0.9); margin-top:20px; max-width:800px;">
      Reducao de 22% no custo de producao em 8 meses por meio de planejamento baseado em demanda real, nao em projecao manual.
    </div>
  </div>
</div>

<!-- SLIDE 23 — Split com foto inset -->
<div class="slide slide-split">
  <div class="slide-num">23</div>
  <div class="primary-bar"></div>
  <div style="flex:1;">
    <div class="label">O QUE OS CLIENTES DIZEM</div>
    <h2 class="title-md">"Nao vendem software — vendem clareza"</h2>
    <div class="body-lg" style="margin-top:24px; color:var(--text-muted);">
      A maior diferenca esta na metodologia. O time da EMPRESA TESTE nao aparece com uma ferramenta pronta. Aparece com perguntas, escuta o operacional e so depois propoe. E quando propoe, e cirurgico.
    </div>
    <div class="spacer"></div>
    <div class="body-md" style="font-weight:600; color:var(--primary);">Maria Silva, CEO de empresa parceira</div>
  </div>
  <div class="photo-inset" style="flex:1; max-height:480px;">
    <img src="assets/foto3.svg" style="width:100%; height:100%; object-fit:cover;" alt="">
  </div>
</div>

<!-- SLIDE 24 — Foto terco superior -->
<div class="slide slide-content-alt">
  <div class="slide-num">24</div>
  <div class="photo-top" style="background-image: url('assets/foto3.svg');"></div>
  <div class="photo-top-content">
    <div class="label">DASHBOARD EM PRODUCAO</div>
    <h2 class="title-md">O que sua diretoria vai olhar todo dia</h2>
    <div class="body-md" style="margin-top:20px; color:var(--text-muted); max-width:800px;">
      Paineis desenhados com o time, nao para o time. Cada diretor tem a visao dele, atualizada em tempo real, sem precisar pedir relatorio para ninguem.
    </div>
  </div>
</div>

<!-- SLIDE 25 — Grid 3 fotos -->
<div class="slide slide-content">
  <div class="slide-num">25</div>
  <div class="primary-bar"></div>
  <div class="label">ENTREGAVEIS</div>
  <h2 class="title-md">O que voce recebe ao final dos 90 dias</h2>
  <div class="cards-grid-3" style="margin-top:28px;">
    <div class="photo-card">
      <img src="assets/foto1.svg" alt="">
      <div class="photo-card-body">
        <div class="card-title" style="font-size:19px;">Arquitetura documentada</div>
        <div class="card-body-sm">Diagramas, fluxos e decisoes registradas em Notion.</div>
      </div>
    </div>
    <div class="photo-card">
      <img src="assets/foto2.svg" alt="">
      <div class="photo-card-body">
        <div class="card-title" style="font-size:19px;">Dashboards vivos</div>
        <div class="card-body-sm">Paineis por diretor, com drill-down por area.</div>
      </div>
    </div>
    <div class="photo-card">
      <img src="assets/foto3.svg" alt="">
      <div class="photo-card-body">
        <div class="card-title" style="font-size:19px;">Time treinado</div>
        <div class="card-body-sm">Handoff completo + 60 dias de suporte ongoing.</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 26 — Divisoria com foto -->
<div class="slide slide-photo-full">
  <div class="slide-num">26</div>
  <div class="photo-full-bg" style="background-image: url('assets/foto2.svg');"></div>
  <div class="photo-overlay" style="background: linear-gradient(135deg, {{OVERLAY_ACCENT_STRONG}}, {{OVERLAY_RGBA_STRONG}});">
    <div class="label label-white">PARTE 4</div>
    <h2 class="title-xl title-on-dark">Numeros<br>que importam</h2>
  </div>
</div>

<!-- SLIDE 27 — Barras verticais -->
<div class="slide slide-content">
  <div class="slide-num">27</div>
  <div class="primary-bar"></div>
  <div class="label">EVOLUCAO DA EFICIENCIA OPERACIONAL</div>
  <h2 class="title-md">Reducao de horas gastas em tarefas repetitivas</h2>
  <div class="chart-bars">
    <div class="chart-bar-col">
      <div class="chart-bar-value">180h</div>
      <div class="chart-bar" style="height:90%;"></div>
      <div class="chart-bar-label">Mes 1<br>(baseline)</div>
    </div>
    <div class="chart-bar-col">
      <div class="chart-bar-value">152h</div>
      <div class="chart-bar" style="height:76%;"></div>
      <div class="chart-bar-label">Mes 2</div>
    </div>
    <div class="chart-bar-col">
      <div class="chart-bar-value">124h</div>
      <div class="chart-bar accent" style="height:62%;"></div>
      <div class="chart-bar-label">Mes 3</div>
    </div>
    <div class="chart-bar-col">
      <div class="chart-bar-value">92h</div>
      <div class="chart-bar accent" style="height:46%;"></div>
      <div class="chart-bar-label">Mes 4</div>
    </div>
    <div class="chart-bar-col">
      <div class="chart-bar-value">72h</div>
      <div class="chart-bar accent" style="height:36%;"></div>
      <div class="chart-bar-label">Mes 5</div>
    </div>
  </div>
  <div class="highlight-box accent" style="margin-top:32px;">
    <p>60% de reducao em 5 meses — equivalente a 3 pessoas alocadas em atividades de maior valor.</p>
  </div>
</div>

<!-- SLIDE 28 — Donuts -->
<div class="slide slide-content-alt">
  <div class="slide-num">28</div>
  <div class="primary-bar"></div>
  <div class="label">DISTRIBUICAO DE IMPACTO</div>
  <h2 class="title-md">Onde o valor e gerado ao longo do projeto</h2>
  <div class="chart-donuts">
    <div class="chart-donut-wrap">
      <div class="chart-donut" style="background: conic-gradient(var(--primary) 0% 68%, var(--border) 68% 100%);">
        <div class="chart-donut-inner">68%</div>
      </div>
      <div class="chart-donut-label">Reducao de<br>custo operacional</div>
    </div>
    <div class="chart-donut-wrap">
      <div class="chart-donut" style="background: conic-gradient(var(--secondary) 0% 42%, var(--border) 42% 100%);">
        <div class="chart-donut-inner" style="color:var(--secondary);">42%</div>
      </div>
      <div class="chart-donut-label">Aumento em<br>receita recorrente</div>
    </div>
    <div class="chart-donut-wrap">
      <div class="chart-donut" style="background: conic-gradient(var(--success) 0% 92%, var(--border) 92% 100%);">
        <div class="chart-donut-inner" style="color:var(--success);">92%</div>
      </div>
      <div class="chart-donut-label">Satisfacao<br>dos lideres</div>
    </div>
  </div>
</div>

<!-- SLIDE 29 — Progress bars -->
<div class="slide slide-content">
  <div class="slide-num">29</div>
  <div class="primary-bar"></div>
  <div class="label">ADOCAO POR AREA</div>
  <h2 class="title-md">Ritmo de adesao ao novo metodo</h2>
  <div class="progress-wrap">
    <div class="progress-item">
      <div class="progress-header">
        <div class="progress-name">Financeiro</div>
        <div class="progress-pct">98%</div>
      </div>
      <div class="progress-track"><div class="progress-fill" style="width:98%; background:var(--primary);"></div></div>
    </div>
    <div class="progress-item">
      <div class="progress-header">
        <div class="progress-name">Comercial</div>
        <div class="progress-pct">86%</div>
      </div>
      <div class="progress-track"><div class="progress-fill" style="width:86%; background:var(--secondary);"></div></div>
    </div>
    <div class="progress-item">
      <div class="progress-header">
        <div class="progress-name">Operacoes</div>
        <div class="progress-pct">74%</div>
      </div>
      <div class="progress-track"><div class="progress-fill" style="width:74%; background:var(--primary);"></div></div>
    </div>
    <div class="progress-item">
      <div class="progress-header">
        <div class="progress-name">Marketing</div>
        <div class="progress-pct">62%</div>
      </div>
      <div class="progress-track"><div class="progress-fill" style="width:62%; background:var(--secondary);"></div></div>
    </div>
  </div>
</div>

<!-- SLIDE 30 — Multi-chart 2x2 -->
<div class="slide slide-content-alt">
  <div class="slide-num">30</div>
  <div class="primary-bar"></div>
  <div class="label">VISAO CONSOLIDADA</div>
  <h2 class="title-md">KPIs do trimestre</h2>
  <div class="multi-chart">
    <div class="chart-box">
      <div class="chart-box-title">Receita recorrente</div>
      <div class="chart-box-value">R$ 2.8M</div>
      <div class="chart-mini-bars">
        <div class="chart-mini-bar" style="height:40%;"></div>
        <div class="chart-mini-bar" style="height:55%;"></div>
        <div class="chart-mini-bar" style="height:70%;"></div>
        <div class="chart-mini-bar" style="height:82%;"></div>
        <div class="chart-mini-bar" style="height:95%;"></div>
      </div>
    </div>
    <div class="chart-box">
      <div class="chart-box-title">Clientes ativos</div>
      <div class="chart-box-value" style="color:var(--secondary);">+2.400</div>
      <div class="chart-mini-bars">
        <div class="chart-mini-bar" style="height:50%; background:var(--secondary-light);"></div>
        <div class="chart-mini-bar" style="height:62%; background:var(--secondary-light);"></div>
        <div class="chart-mini-bar" style="height:71%; background:var(--secondary-light);"></div>
        <div class="chart-mini-bar" style="height:85%; background:var(--secondary-light);"></div>
        <div class="chart-mini-bar" style="height:92%; background:var(--secondary-light);"></div>
      </div>
    </div>
    <div class="chart-box">
      <div class="chart-box-title">NPS</div>
      <div class="chart-box-value">72</div>
      <div class="chart-mini-bars">
        <div class="chart-mini-bar" style="height:60%;"></div>
        <div class="chart-mini-bar" style="height:65%;"></div>
        <div class="chart-mini-bar" style="height:70%;"></div>
        <div class="chart-mini-bar" style="height:72%;"></div>
        <div class="chart-mini-bar" style="height:78%;"></div>
      </div>
    </div>
    <div class="chart-box">
      <div class="chart-box-title">Tempo medio de resposta</div>
      <div class="chart-box-value" style="color:var(--secondary);">&lt; 4h</div>
      <div class="chart-mini-bars">
        <div class="chart-mini-bar" style="height:95%; background:var(--secondary-light);"></div>
        <div class="chart-mini-bar" style="height:78%; background:var(--secondary-light);"></div>
        <div class="chart-mini-bar" style="height:62%; background:var(--secondary-light);"></div>
        <div class="chart-mini-bar" style="height:48%; background:var(--secondary-light);"></div>
        <div class="chart-mini-bar" style="height:35%; background:var(--secondary-light);"></div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 31 — BIG NUMBER -->
<div class="slide slide-content" style="justify-content:center; align-items:center; text-align:center;">
  <div class="slide-num">31</div>
  <div class="label label-primary" style="text-align:center;">O NUMERO QUE CONTA A HISTORIA</div>
  <div class="big-number">+347%</div>
  <div class="big-number-label">
    foi o retorno medio sobre o investimento dos clientes no primeiro ano apos a implementacao do metodo EMPRESA TESTE.
  </div>
  <div class="primary-line primary-line-center" style="margin-top:40px;"></div>
</div>

<!-- SLIDE 32 — Quote -->
<div class="slide slide-content-alt quote-slide" style="justify-content:center;">
  <div class="slide-num">32</div>
  <div class="quote-mark">&ldquo;</div>
  <div class="quote-text">
    Antes da EMPRESA TESTE, eu tomava decisao no olhometro. Hoje tomo com dado. E o mais importante: meu time toma decisao sem precisar de mim.
  </div>
  <div class="quote-author">
    <strong>Carlos Mendes</strong> — Diretor Financeiro, empresa parceira
  </div>
</div>

<!-- SLIDE 33 — Pricing -->
<div class="slide slide-content">
  <div class="slide-num">33</div>
  <div class="primary-bar"></div>
  <div class="label">TRES MODELOS DE ENGAJAMENTO</div>
  <h2 class="title-md">Investimento</h2>
  <div class="pricing-grid">
    <div class="pricing-card">
      <div class="pricing-name">Diagnostico</div>
      <div class="pricing-price">R$ 18k<span class="small">/ unico</span></div>
      <div class="pricing-desc">Avaliacao em 2 semanas com relatorio executivo e roadmap.</div>
      <ul class="pricing-features">
        <li>2 entrevistas com cada diretor</li>
        <li>Analise dos 5 sistemas principais</li>
        <li>Relatorio de 30 paginas</li>
        <li>1 sessao de apresentacao</li>
      </ul>
      <a href="#" class="pricing-cta">Comecar</a>
    </div>
    <div class="pricing-card featured">
      <div class="pricing-badge">Mais escolhido</div>
      <div class="pricing-name">Transformacao 90d</div>
      <div class="pricing-price">R$ 120k<span class="small">/ 3 meses</span></div>
      <div class="pricing-desc">Metodo completo com implementacao, handoff e garantia de ROI.</div>
      <ul class="pricing-features">
        <li>Diagnostico + arquitetura + execucao</li>
        <li>Integracao dos sistemas principais</li>
        <li>Dashboards personalizados</li>
        <li>Treinamento do time + documentacao</li>
        <li>Garantia de ROI em 90 dias</li>
      </ul>
      <a href="#" class="pricing-cta">Comecar</a>
    </div>
    <div class="pricing-card">
      <div class="pricing-name">Ongoing</div>
      <div class="pricing-price">R$ 12k<span class="small">/ mes</span></div>
      <div class="pricing-desc">Apos o projeto base, acompanhamento continuo com squad dedicado.</div>
      <ul class="pricing-features">
        <li>1 reuniao de diretoria mensal</li>
        <li>Ajustes e novos dashboards</li>
        <li>Suporte prioritario</li>
        <li>Evolucao do metodo</li>
      </ul>
      <a href="#" class="pricing-cta">Comecar</a>
    </div>
  </div>
</div>

<!-- SLIDE 34 — CTA forte -->
<div class="slide cta-slide">
  <div class="slide-num">34</div>
  <h1 class="cta-title">Vamos conversar<br>em 45 minutos?</h1>
  <div class="cta-sub">
    Te mostramos como aplicariamos o metodo no seu contexto especifico, sem compromisso e sem cobranca.
  </div>
  <a href="#" class="cta-button">AGENDAR DIAGNOSTICO GRATUITO</a>
</div>

<!-- SLIDE 35 — Encerramento -->
<div class="slide slide-cover">
  <div class="slide-num">35</div>
  <img src="assets/logo.svg" class="cover-logo" alt="Logo">
  <h1 class="title-hero" style="font-size:72px; text-align:center;">Obrigado</h1>
  <div class="subtitle" style="text-align:center; margin-top:24px;">Ana Souza (ficticio) — CEO EMPRESA TESTE LTDA</div>
  <div class="primary-line primary-line-center"></div>
  <div style="margin-top:32px; font-size:18px; color:var(--text-muted); text-align:center;">
    contato@empresateste.com.br &nbsp;&middot;&nbsp; www.empresateste.com.br &nbsp;&middot;&nbsp; (11) 9999-9999
  </div>
</div>
<!-- =================================================================== -->

<div class="slide-footer" id="footer"></div>

<script>
  const slides = document.querySelectorAll('.slide');
  const counter = document.getElementById('counter');
  let current = 0;

  function go(to) {
    slides[current].classList.remove('active');
    current = (to + slides.length) % slides.length;
    slides[current].classList.add('active');
    counter.textContent = `${current + 1} / ${slides.length}`;
  }

  document.addEventListener('keydown', (e) => {
    if (['ArrowRight', ' ', 'PageDown'].includes(e.key)) { e.preventDefault(); go(current + 1); }
    else if (['ArrowLeft', 'PageUp'].includes(e.key)) { e.preventDefault(); go(current - 1); }
    else if (e.key === 'Home') { go(0); }
    else if (e.key === 'End') { go(slides.length - 1); }
    else if (/^[1-9]$/.test(e.key)) { go(parseInt(e.key) - 1); }
  });

  document.getElementById('next').onclick = () => go(current + 1);
  document.getElementById('prev').onclick = () => go(current - 1);

  document.getElementById('footer').innerHTML =
    '<img src="assets/logo.svg" alt=""> {{RODAPE_TEXTO}}';
</script>

</body>
</html>

<!-- === FIM BLUEPRINT === -->

## Notas finais

- O blueprint acima esta em portugues brasileiro, tipografia Poppins por padrao e paleta
  azul+laranja. Substitua TUDO pelos tokens do aluno.
- Se o aluno pedir densidade `minimalista` ou `denso`, ajuste os font-sizes nas regras
  `.title-*`, `.body-*` e `.bullet-list li` conforme PASSO 3 item 5.
- Se o aluno pediu tipografia `mista` (serif+sans), troque a variavel `--font-serif`
  dentro do `:root` e aplique nos titulos (`.title-*`) deixando `--font` (sans) no body.
- Se o aluno escolheu fundo escuro (`tom=escuro`), alem de inverter cores de texto,
  ajuste os gradientes das divisorias de secao para ficarem legiveis.
- Fotos placeholder SVG: se o aluno nao forneceu fotos, gere 3 SVGs com gradiente
  primaria->secundaria e salve em `assets/foto{1,2,3}.svg`. Veja exemplo em
  `examples/modelo-empresa-teste/assets/` do bundle.

---

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio — Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
