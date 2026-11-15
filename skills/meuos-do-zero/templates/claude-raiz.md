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

## Como operar este OS
- O documento mestre de cada contexto guarda a decisão vigente, o status e o próximo passo. Detalhe de um assunto (medição, lista, especificação) vai para um satélite: um arquivo CONTEXTO_tema.md, com ponteiro no documento mestre e no index.md.
- Decida a casa da informação na hora de escrever, não na faxina.
- Atualize o documento mestre durante o trabalho: ele é a fonte de retomada.
- Nunca crie arquivo solto: todo arquivo novo entra no index.md do contexto.
- Sessão de trabalho relevante termina com a skill fim-do-dia.
- Nada é movido, resumido ou apagado sem mostrar antes e ter o OK do dono.
- Todo número, data ou fato que dá para conferir leva a fonte e a data da conferência. Sem fonte, marque "não verificado".
- Manual completo: [guia_do_os.md](guia_do_os.md). Abrir quando: dúvida sobre onde gravar, arquivo novo, contexto novo, estrutura fora do padrão, limites de tamanho.

## Forma da resposta
- A primeira linha responde.
- Decisão do dono vira tabela numerada, com "o que muda para você" em frase simples. O dono aprova pela caixa de opções, quando houver, ou pelos números.
- Linguagem de gestor, sem termo técnico que o dono não usou.
- Feche com: feito, pendente e próximo passo.
