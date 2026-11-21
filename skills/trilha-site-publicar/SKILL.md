---
name: trilha-site-publicar
description: "Segunda metade do exercicio do site pelo Metodo TRILHA: com o briefing e o catalogo aprovados, propoe a estrutura, escreve os textos so com fatos aprovados, propoe o visual, constroi o site em HTML, CSS e JavaScript por blocos testados, procura senha e dado pessoal nos arquivos e guia o usuario, clique a clique, pelo GitHub (repositorio privado) e pela Vercel ate o site no ar, conferido no celular e no computador. Nunca pede credencial no chat e nunca publica sem autorizacao. Usar quando o usuario disser 'constroi o site', 'monta o site aprovado', 'publica o site', 'subir o site no GitHub', 'colocar o site na Vercel', 'meu site no ar'."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Site TRILHA: construir e publicar

## O que esta skill faz

Pega o que a skill `trilha-site-preparar` entregou (briefing e catalogo aprovados), constroi o site por blocos, prova que funciona e guia o usuario ate o site publicado. Segue o Metodo TRILHA (skill `meuos-trilha`): cada bloco tem evidencia e cada passo externo tem aprovacao.

---

## Passo a passo (instrucoes para o agente de IA)

### PASSO 0: Conferir a largada

Ler `PROGRESSO.md`, `BRIEFING_SITE.md` e `CATALOGO_SITE.md`. Se o briefing nao estiver APROVADO ou houver lacuna bloqueante, parar e sugerir a skill `trilha-site-preparar`. Se o `PROGRESSO.md` mostrar que a construcao ja comecou, retomar do proximo passo registrado.

### PASSO 1: Estrutura

Propor a menor estrutura que cumpre o objetivo (para o primeiro site, uma pagina costuma bastar: abertura, problema, solucao, beneficios, prova, sobre, chamada para acao). Para cada secao: funcao, mensagem principal, material de apoio e acao esperada. Esperar aprovacao.

### PASSO 2: Textos

Escrever secao por secao usando so fatos do briefing e do catalogo. Cortar frase que serviria para qualquer empresa ("transformamos desafios em resultados"). Afirmacao que exige prova sem prova: marcar e pedir decisao. Esperar aprovacao dos textos.

### PASSO 3: Visual

Propor DUAS direcoes visuais (cores, tipografia, uso de imagens, densidade), nunca dez. Referencia inspira, nao se copia. Esperar a escolha.

### PASSO 4: Construcao por blocos

Construir em HTML, CSS e JavaScript simples, sem login, banco, pagamento, formulario que coleta dado pessoal ou segredo no codigo. Arquivo principal `index.html` na raiz da pasta; criar `README.md` explicando como abrir e testar. Uma secao por vez: construir, abrir no navegador, conferir, registrar no `PROGRESSO.md`. Se pensar em outra tecnologia, explicar ganho e custo e so usar com aprovacao.

### PASSO 5: Homologacao local

Conferir e separar em APROVADO, FALHOU e NAO TESTADO: abre sem erro; texto igual ao aprovado; nada inventado; botoes e links levam ao lugar certo; telefone, e-mail e redes corretos; funciona em tela de celular e de computador; nada cortado ou sobreposto; imagens autorizadas carregando; titulo e descricao da pagina preenchidos. Corrigir as falhas e repetir.

### PASSO 6: Varredura antes de sair da mesa

Procurar nos arquivos senha, token, chave, codigo de verificacao, arquivo `.env`, dado pessoal e base de clientes. Mostrar o que achou sem repetir o segredo. Parar ate o usuario remover. So seguir com a varredura limpa.

### PASSO 7: GitHub (guardar os arquivos em privado)

Explicar em 1 linha: o GitHub guarda os arquivos e o historico de versoes; o repositorio fica privado, o site continua publico. Guiar, um passo por vez, esperando o usuario confirmar cada um:

1. Criar a conta em https://github.com/signup (gratuita) e confirmar o e-mail. Recomendar ativar a verificacao em duas etapas.
2. No canto superior direito, clicar no sinal de mais (+) e em "New repository".
3. Nome simples (ex.: `meu-site`), visibilidade "Private", sem marcar README, licenca ou `.gitignore`. Clicar em "Create repository".
4. Enviar os arquivos, por um dos dois caminhos:
   - Sem terminal (Claude no navegador ou no app): na pagina do repositorio vazio, usar o link "uploading an existing file", arrastar os arquivos da pasta do site (nao a pasta inteira de projeto com briefing e catalogo, so o que vai ao ar) e clicar em "Commit changes".
   - Com terminal (Claude Code): o Claude mostra os comandos de git que pretende usar, o usuario autentica pelo `gh auth login` concluindo a autorizacao no navegador, e o envio so acontece depois da autorizacao explicita.
5. Conferir no GitHub que os arquivos chegaram e que o repositorio aparece como Private.

O plano gratuito do GitHub permite repositorios privados ilimitados, com recursos limitados (fonte: https://docs.github.com/en/get-started/learning-about-github/githubs-plans).

### PASSO 8: Plano e privacidade da Vercel (decisao do usuario)

Antes de criar a conta, explicar e registrar a decisao no `PROGRESSO.md`:
- O plano gratuito (Hobby) e para uso pessoal ou nao comercial (termos da Vercel, secao 4: https://vercel.com/legal/terms). Site que promove empresa ou vende servico deve ir para um plano pago antes de ficar em producao; para aprender e para portfolio pessoal, o Hobby serve.
- No Hobby, o conteudo enviado pode ser usado para treinar a IA da Vercel (termos, secao 3), com opcao de desligar nas configuracoes da conta (Team Settings). Recomendar desligar.
- Nao divulgar preco de plano de memoria: mandar o usuario conferir https://vercel.com/pricing.

### PASSO 9: Vercel (colocar no ar)

Guiar, um passo por vez:

1. Criar a conta em https://vercel.com/signup entrando com a conta do GitHub.
2. No painel, criar um novo projeto ("Add New" > "Project", ou "New Project").
3. Quando a Vercel pedir acesso ao GitHub, escolher "Only select repositories" e marcar so o `meu-site` (fonte: https://vercel.com/docs/git/vercel-for-github).
4. Localizar o `meu-site` e clicar em "Import".
5. Em "Framework Preset", deixar "Other"; site em HTML, CSS e JavaScript sai como esta, sem comando de construcao (fonte: https://vercel.com/docs/builds/configure-a-build).
6. Mostrar ao usuario o que vai ao ar e pedir a autorizacao explicita. Com o OK, o usuario clica em "Deploy".
7. Abrir o endereco terminado em `.vercel.app`.

Explicar: a partir de agora, cada nova versao enviada ao GitHub gera uma nova publicacao automaticamente. Toda mudanca futura passa pela mesma regra: mostrar, autorizar, enviar.

### PASSO 10: Homologacao no ar e entrega

Repetir a homologacao do PASSO 5 no endereco publicado, mais: HTTPS ativo e site aberto no celular do usuario. "Apareceu a animacao de comemoracao" nao e teste. Registrar no `PROGRESSO.md` o endereco, a data, a versao, o plano usado, o resultado dos testes e as pendencias. Entregar ao usuario: endereco do site, repositorio privado, briefing, catalogo, checklist preenchido e a lista dos momentos em que o Claude parou para pedir decisao.

---

## Regras

- A entrada nas contas e sempre do usuario, na tela oficial. Nunca pedir, receber, guardar ou repetir senha, token ou codigo.
- Nunca enviar ao GitHub nem publicar sem autorizacao explicita naquele momento.
- Nunca dizer que o plano gratuito da Vercel serve para uso comercial.
- Tela diferente do descrito (botao mudou de nome ou lugar): descrever o que o usuario esta vendo, procurar a pagina oficial citada e seguir por ela; nunca chutar.

## Checklist antes de entregar

- [ ] Estrutura, textos e visual aprovados
- [ ] Homologacao local e no ar separadas em aprovado, falhou e nao testado
- [ ] Varredura de segredos limpa antes do GitHub
- [ ] Repositorio privado conferido
- [ ] Decisao de plano da Vercel registrada
- [ ] Publicacao autorizada pelo usuario
- [ ] `PROGRESSO.md` com endereco, data e versao

Se algum item falhou: corrigir ANTES de declarar concluido.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
