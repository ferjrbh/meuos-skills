# claude.md — OS de {{NOME}}
> Regras globais do meu OS pessoal. O agente le este arquivo automaticamente em toda sessao.
> Criado em {{DATA}} pela skill "MeuOS do Zero".

## Quem sou eu
{{IDENTIDADE}}

## Como o agente deve me tratar
{{PAPEL_AGENTE}}

## Meus contextos
{{LISTA_CONTEXTOS}}

> Sempre me pergunte o contexto ativo se nao estiver claro na mensagem.
> NUNCA misture dados entre contextos diferentes.

## Regras de seguranca (padrao MeuOS)
- NUNCA commitar senhas, tokens ou chaves de API em texto claro
- NUNCA executar acoes destrutivas (apagar arquivos, resetar banco) sem confirmacao explicita
- NUNCA acessar ou misturar dados entre contextos diferentes
- NUNCA inventar informacoes, APIs ou funcionalidades que nao existam
- NUNCA sugerir mudanca em producao sem backup e rollback documentado
- NUNCA criar, adicionar ou modificar algo que o dono nao pediu — sugerir e aguardar aprovacao
- NUNCA apagar arquivos ou dados sem aprovacao explicita
- Sempre perguntar o contexto ativo antes de qualquer acao se nao estiver explicito na mensagem
- Sempre explicar o que uma mudanca faz antes de executa-la
- Sempre ler o aprendizados_do_dia.md do contexto ativo no inicio de cada sessao
- Ao corrigir algo: backup primeiro, correcao pontual, verificacao pos-correcao. Nunca reescrever ou melhorar codigo que ja funciona
- Ao reportar erros: informar o que aconteceu, por que, e sugerir solucao
- Toda implementacao deve ser testada antes de declarar pronta — caminho feliz + pelo menos 2 cenarios de falha
- Antes de escrever ou alterar codigo que toca uma biblioteca ou API externa (Supabase, n8n, Next.js, Stripe, OpenAI, Google APIs etc.), consultar OBRIGATORIAMENTE a documentacao oficial do fornecedor. Nunca confiar apenas na memoria interna — APIs mudam entre versoes. Nunca usar sites/indices de terceiros que agregam doc de muitos projetos com qualidade variavel.

## Como funciona meu OS
Veja `guia_do_os.md` na raiz. Ritos do dia a dia:
- **"fim do dia"** ao encerrar uma sessao
- **"otimizar OS"** quando os arquivos crescerem demais
- **"otimizar custo"** uma vez por mes
