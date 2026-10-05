# Catálogo de checagens do copiloto

Quatro famílias: A mecânica, B dado, C raciocínio, D verificação. Cada checagem diz o que testar, o sintoma típico e de onde vem. Origem "casa" quer dizer lição tirada de análises reais de empresas, só a regra.

Base que justifica o rigor: em auditorias de campo, pelo menos 86% das planilhas tinham erro; uma pessoa sozinha acha cerca de 63% dos erros, e três pessoas, cerca de 83%; o erro de omissão é o que menos se acha (Panko; Panko e Halverson). Os casos Reinhart-Rogoff e London Whale foram descobertos por recálculo independente.

## A · Mecânica da conta

| Código | Checagem | Como testar | Sintoma | Origem |
|---|---|---|---|---|
| A1 | Totais cruzados | Soma das linhas = soma das colunas = total geral; saldo inicial + entradas − saídas = saldo final | Total diferente da soma das partes | ICAEW |
| A2 | A soma pega todas as linhas | Conte os itens dentro de cada soma ou filtro e compare com a origem | Linhas somem sem aviso: no caso Reinhart-Rogoff, a média parou na linha 44 e deixou de fora as linhas 45 a 49 | Herndon, Ash e Pollin |
| A3 | Número digitado no meio da conta | Procure valor fixo dentro de fórmula ou de código | Premissa congelada que quebra na atualização | Panko; FAST |
| A4 | Sinal e unidade | Custo e retorno com o sinal certo; R$ ou R$ mil; % ou ponto percentual; moeda | Erro de mil vezes ou de sinal trocado | EuSpRIG |
| A5 | A conta faz o que a definição diz | Refaça uma linha à mão pela definição declarada | No London Whale, a medida de risco dividia pela soma, e a definição pedia a média | relatório JPMorgan |
| A6 | Ordem e circularidade | Um passo que lê o resultado de um passo posterior; referência circular | O valor muda quando a conta roda de novo | ICAEW |
| A7 | Caça à omissão | Liste o que deveria estar (linhas de custo, segmentos, meses, canais) e marque cada um | Resultado plausível e incompleto | Panko e Halverson |
| A8 | Tabela fecha na conta do leitor | Some as parcelas como estão impressas e compare com o total impresso (`confere_somas.py`); a regra é arredondar cada parcela e somar as parcelas | O leitor soma e não bate | casa |
| A9 | O mesmo número igual em todo lugar | Compare o valor da mesma métrica em todas as telas, tabelas, texto e notas (`extrai_numeros.py`) | Duas verdades na mesma peça | Anthropic ib-check-deck; casa |
| A10 | Lista cortada pela ponta errada | Lista ordenada do maior para o menor cortada pelo fim perde o topo; confira a soma contra um total de controle | Os maiores itens somem do ranking | casa |
| A11 | Datas no calendário | "Mesmo dia" e "mesma semana" se conferem no calendário, dia a dia | Comparação entre semanas que não são equivalentes | casa |

## B · O dado

| Código | Checagem | Como testar | Sintoma | Origem |
|---|---|---|---|---|
| B1 | Completude | Linhas que entram e que saem em cada junção ou filtro; total contra o sistema oficial | Total abaixo do publicado | DAMA |
| B2 | Chave única na granularidade declarada | Multiplicidade da chave completa (`perfil_base.py --chave`); linhas antes e depois de cada junção | Junção que multiplica linhas e infla a soma; bloco anual anexado duas vezes | DAMA; dbt; casa |
| B3 | Integridade entre arquivos | Identificadores órfãos, conferidos nos dois sentidos | Junção interna derruba linhas calada | dbt |
| B4 | Período coberto | Data mínima e máxima contra o período pedido; buracos por dia ou mês; mês incompleto; meses imaturos para o desfecho | Mês parcial lido como queda | DAMA; casa |
| B5 | Validade | Vazios, valores fora de faixa, negativos, valores muito acima do resto, registros de teste | Vazio gravado como zero | DAMA; dbt |
| B6 | Consistência entre fontes | A mesma métrica, de duas fontes, bate dentro da tolerância | Dois números para a mesma coisa | DAMA |
| B7 | Corte silencioso | Base com 1.048.575 ou 1.048.576 linhas passou pelo Excel e foi cortada; a ordenação decide qual ponta some | Série que termina antes da hora | casa |
| B8 | Data guardada como texto | Data em DD-MM-AAAA ou DD/MM/AAAA guardada como texto: mínimo, máximo e filtro mentem | Período errado sem erro na tela | casa |
| B9 | Escala da coluna | A unidade declarada na coluna pode mentir; confira a escala por uma identidade independente | Valores mil vezes maiores ou menores | casa |
| B10 | Entidade casada pelo fato | Case empresas e pessoas por identificador (CNPJ, matrícula) ou pelo que fazem; nome parecido erra sem aviso | Duas empresas viram uma, ou uma vira duas | casa |
| B11 | Export repartido repete a chave | Export quebrado por canal ou período repete a mesma chave em várias linhas; carregar num dicionário sobrescreve; o certo é somar | Denominador encolhe sem aviso | casa |
| B12 | Situação pela lista oficial | Status ativo, cancelado e encerrado vêm da lista do dono do dado | Carteira viva contada pelo comportamento do sistema | casa |

## C · O raciocínio

| Código | Checagem | Como testar | Sintoma | Origem |
|---|---|---|---|---|
| C1 | O que conta como um | Cliente por nome, CNPJ ou grupo econômico (raiz do CNPJ); pessoa; campanha; loja. Recalcule nas unidades possíveis | Concentração escondida: três nomes, um grupo só | casa |
| C2 | Denominador | Quem está na base; a mesma definição dos dois lados da comparação | A taxa "melhora" porque a base mudou | Aqua Book; casa |
| C3 | Razão dos totais ou média das razões | Recalcule ponderado e diga qual foi usado | Unidade pequena pesa como grande (Reinhart-Rogoff ponderou cada país igual) | Herndon, Ash e Pollin |
| C4 | Mediana de medianas | Mediana de um agregado geográfico pondera por tamanho; mediana de medianas engana | Ranking regional invertido | casa |
| C5 | Mistura de grupos | Recalcule dentro de cada grupo; separe a mudança em efeito de mistura e efeito de taxa | O total sobe e todos os grupos caem (paradoxo de Simpson) | Stanford Encyclopedia; casa |
| C6 | Célula pequena | Tamanho de cada célula; os extremos são todos pequenos? | O melhor e o pior da lista são as menores unidades | Wainer |
| C7 | Volta à média, sobrevivente, taxa de base | A seleção foi feita pelos extremos? Só ficaram os que sobreviveram? A prevalência foi dita? | "Virada" das piores lojas | Kahneman e Tversky; Wald |
| C8 | Causa sem grupo de controle | Contrafactual, grupo de controle, período anterior, outras causas | Ganho atribuído a uma ação só com antes e depois | Aqua Book; casa |
| C9 | Efeito de mídia | A janela começa no último período sem investimento; a fatia atribuída sai do total; conversão declarada pela plataforma se confere na ferramenta de análise do site | Campanha leva crédito do que já acontecia | casa |
| C10 | Alavancas que se sobrepõem | Aplique cada alavanca sobre a base já mudada pela anterior; publique a sobreposição; entregue faixa | Ganhos somados passam do total possível | casa |
| C11 | Base de tempo e de moeda | Mês sazonal multiplicado por 12; período parcial; crescimento composto ou simples; valor nominal ou real | Um mês de pico vira o ano | casa |
| C12 | Perímetro igual dos dois lados | Mesma régua, mesmas unidades (mesmas lojas), mesma janela; a meta que vai à mesa é a da rede inteira, a do piloto é mecanismo | Comparação entre bases diferentes | casa |
| C13 | Percentual com a base dita | Fatia do total ou aumento? Porcentagem ou ponto percentual? A frase diz qual | "Subiu 3%" que era 3 pontos | casa |
| C14 | Fechar unidade só tira o custo direto | O rateio da sede fica e se redistribui; a retenção se mede nos fechamentos já feitos | Fechar a pior unidade piora o resultado | casa |
| C15 | Custo de capital | Taxa de custo de capital é depois de imposto e se compara com lucro operacional depois de imposto; a DRE já deprecia o ativo, então somar a posse cheia cobra duas vezes | Operação "destrói valor" por erro de régua | casa |
| C16 | Benchmark com fonte | "Margem do setor" só vale com empresa, balanço e ano; sem isso, é achismo bem escrito | Número de mercado sem endereço | casa |
| C17 | A variável pedida | Meça na variável da pergunta; um substituto (busca no lugar de venda) responde outra pergunta | Conclusão certa para a pergunta errada | casa |
| C18 | Desconto de fornecedor | Recalcule a proposta na nossa unidade (custo por mil, valor mensal); o desconto declarado é ficção até a conta mostrar | Proposta cara que parece barata | casa |
| C19 | Pergunta, população e métrica certas | A conta pode estar certa e responder outra coisa | Aritmética correta, resposta errada | Aqua Book |

## D · A verificação

| Código | Checagem | Como testar | Sintoma | Origem |
|---|---|---|---|---|
| D1 | Recálculo independente | Refaça os números principais a partir do dado bruto, por outro caminho | Única forma de pegar erro do tipo A5 | Aqua Book; Panko |
| D2 | Ponte | Reproduza o número divergente mudando uma escolha de cada vez | Divergência sem explicação | casa |
| D3 | Triangulação | Compare com uma âncora de fora (balanço, dado público); aplique o número à realidade e veja se é absurdo | Coerente por dentro, impossível por fora | Aqua Book; casa |
| D4 | Pré-mortem | "A decisão deu errado em seis meses. Por quê?" | Premissa que ninguém examinou | Klein |
| D5 | Conclusão oposta | Defenda a conclusão contrária mais forte com os mesmos dados | Viés de confirmação | Manual de red team do Ministério da Defesa britânico |
| D6 | Desafio e resposta | Todo desvio é dito em voz alta; achado grave sem resposta depois de dois avisos segura a entrega | Dúvida levantada baixinho e esquecida | FAA, AC 120-71B |
| D7 | Conferir a própria crítica | A refutação passa pelo mesmo rigor do achado; convergência que dependeu de um parâmetro escolhido depois é fabricada | Alarme falso que derruba peça certa | casa |

## Régua de gravidade

Adaptada das normas de materialidade de auditoria (ISA 320 e SAB 99).

- 🔴 **Segura a peça.** O erro pode mudar a decisão: vira um sinal, inverte uma ordem, cruza uma meta ou uma linha de corte, transforma lucro em prejuízo, esconde uma tendência, ou passa de 5% do número principal. Qualquer gatilho qualitativo desses faz o erro ser 🔴, seja qual for o tamanho.
- 🟡 **Corrige e sai.** O tamanho de um número muda, a recomendação continua de pé, e o erro não é trivial. A correção vai junto com o número certo.
- 🔵 **Registra.** Forma: rótulo, arredondamento de exibição, documentação, número digitado que hoje não muda nada.

Na dúvida, suba a gravidade até o número ser recalculado.

## Fontes

Panko, "What we know about spreadsheet errors" (panko.shidler.hawaii.edu) · Panko e Halverson (arxiv.org/pdf/0809.3613) · EuSpRIG, casos públicos (eusprig.org) · ICAEW Financial Modelling Code · FAST Standard (fast-standard.org) · DAMA UK, dimensões de qualidade de dado · dbt, testes de dado · Herndon, Ash e Pollin, PERI WP322 · relatório da força-tarefa do JPMorgan, via AccountingWEB · Stanford Encyclopedia of Philosophy, "Simpson's paradox" · Wainer, "The most dangerous equation" · Aqua Book do governo britânico · FAA AC 120-71B · Klein, "Performing a project premortem", HBR · Red Teaming Handbook, Ministério da Defesa britânico · ISA 320 (ICAEW) · SEC SAB 99. Inspiração de desenho, sem código copiado: Anthropic `knowledge-work-plugins/data/validate-data` e `financial-services/ib-check-deck` (Apache-2.0), `pedrohcgs/claude-code-my-workflow` (MIT), `petehottelet/spreadsheet-auditor` (MIT).
