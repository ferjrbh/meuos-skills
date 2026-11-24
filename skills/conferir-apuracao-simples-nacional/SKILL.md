---
name: conferir-apuracao-simples-nacional
description: "Confere a apuração mensal do Simples Nacional (PGDAS-D) cruzando com as notas fiscais de saída e de entrada. Verifica a receita bruta do mês e a RBT12, o Anexo correto pela atividade (art. 18 da LC nº 123/2006), o fator r, a alíquota efetiva e o valor do DAS, a segregação de receitas (ICMS-ST, monofásico, exportação, ISS retido), o sublimite de ICMS/ISS e as retenções nas notas de serviços tomados (INSS 11%, ISS, IRRF, CSRF). Acionar quando o usuário disser \"conferir PGDAS\", \"conferir Simples\", \"validar Simples Nacional\", \"alíquota do Simples\", \"DAS\", \"fator r\", \"Anexo III ou V\", \"RBT12\", \"alíquota efetiva\", \"enquadramento\", \"CNAE do Simples\", \"retenção nas notas de entrada\", \"ISS retido no Simples\", ou enviar o PDF do PGDAS-D com as notas. Entrega: relatório de conferência com status por verificação, impacto financeiro e ações."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Conferir apuração do Simples Nacional

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Revisa o PGDAS-D já gerado (ou a gerar) e aponta divergências: receita do mês diferente das notas, Anexo ou faixa errados, fator r mal calculado, alíquota efetiva ou DAS que não batem, receitas que deveriam ter sido segregadas e retenções aplicadas (ou esquecidas) nas notas de serviço tomadas. Produz um relatório com status por item e o impacto em reais.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Reforma Tributária.** Em 2026 o optante do Simples continua pagando tudo pelo DAS. A partir de 2027 ele pode optar por apurar IBS e CBS pelo regime regular, fora do DAS. A opção é semestral (janelas em setembro e em março, com efeito no semestre seguinte); a primeira foi de 01/09 a 30/10/2026, com efeitos de janeiro a junho de 2027, cancelável de 03/11 a 20/12/2026 (Resolução CGSN nº 186/2026, com os prazos alterados pela Resolução CGSN nº 194/2026). NF-e de optante (CRT 1, 2 e 4) sem os grupos de IBS/CBS passa a ser rejeitada a partir de 04/01/2027. Também a partir de 2027: o regime de caixa deixa de existir no Simples (só competência) e a RBT12 e a folha do fator r passam a ser as dos 12 meses antecedentes ao mês anterior ao período de apuração (Perguntas e Respostas do Simples Nacional, perguntas 5.3.2, 5.7 e 5.11). Detalhes na skill `reforma-tributaria-transicao`.

## Quando usar
- Conferência mensal do DAS antes de enviar ao cliente.
- Suspeita de Anexo errado (principalmente III × V pelo fator r).
- Revisão de retenções nas notas de serviços tomados pela empresa do Simples.

MEI → `apuracao-mei`. Cálculo do DAS do zero → `calcular-das-simples-nacional`.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). A folha usada no fator r entra só pelo total.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### Insumos necessários
1. **PGDAS-D** do período (PDF ou dados: RBT12, receita do mês por atividade, alíquotas, valores).
2. **Notas de saída** do período (XML de NF-e e NFS-e).
3. **Notas de entrada / serviços tomados** (para verificar retenções).
4. **Folha dos últimos 12 meses** (total, para o fator r).
Sem o PGDAS-D não há conferência: pedir antes de seguir.

### Etapa 1 — Dados da empresa e do período
- Atividades exercidas (CNAE principal e secundários) e **descrição real do serviço**.
- UF e município (sublimite e ISS).
- Regime de reconhecimento da receita no Simples: competência ou caixa (o regime de caixa só vale até o período de apuração 12/2026).
- RBT12 e receita do mês. Empresa com menos de 13 meses: RBT12 proporcionalizada (média dos meses anteriores × 12; no 1º mês, receita do próprio mês × 12 — regra até 2026, pergunta 5.4 do Perguntas e Respostas do Simples Nacional).
- Consultar o Anexo A no fim deste arquivo.

### Etapa 2 — Receita bruta do mês
```
Receita do mês nas notas = Σ notas de saída do mês − canceladas − devoluções − descontos incondicionais
```
(receita bruta: art. 3º, § 1º, da LC nº 123/2006). Comparar com o PGDAS-D:

| Situação | Status |
|---|---|
| Igual (tolerância ≤ R$ 0,01) | OK |
| Diferença até R$ 5,00 | Atenção — arredondamento ou nota cancelada |
| Diferença > R$ 5,00 | Divergência — nota não lançada ou período errado |

Pontos de atenção:
- Nota cancelada em mês posterior: deduzir no período de apuração em que a venda foi tributada; devolução de mercadoria: deduzir no mês da devolução (arts. 17 e 18 da Resolução CGSN nº 140/2018).
- Nota com ISS retido pelo tomador: a receita entra inteira; a retenção é informada no PGDAS-D (campo de ISS retido), sem reduzir a receita.
- Receitas com ICMS-ST, monofásicas (PIS/COFINS) e de exportação **entram na receita**, mas devem ser **segregadas** para retirar da partilha os tributos já pagos ou não devidos.

### Etapa 3 — Anexo correto e fator r
O Anexo depende da **atividade**, conforme o art. 18 da LC nº 123/2006 e o art. 25 da Resolução CGSN nº 140/2018. O CNAE é só indicativo.
- Anexo I: comércio (inclusive restaurante e bar — fornecimento de alimentação).
- Anexo II: indústria.
- Anexo III: serviços do § 5º-B do art. 18 que não estão sujeitos ao fator r (ex.: escritório de contabilidade, agência de viagem, instalação e manutenção, corretagem de seguros) e locação de bens móveis; comunicação e transporte intermunicipal/interestadual de cargas no Anexo III com ICMS no lugar do ISS (§ 5º-E).
- Anexo IV: construção civil, vigilância, limpeza, conservação (inclusive controle de pragas urbanas) e **advocacia** (§ 5º-C).
- Anexo III ou V conforme o **fator r**: atividades do § 5º-I (medicina veterinária, despachante, tradução, engenharia, consultoria, auditoria, publicidade, representação comercial, perícia etc.), as dos incisos XVI e XVIII a XXI do § 5º-B (fisioterapia, arquitetura, medicina e enfermagem, odontologia, psicologia e demais da lista) e as do § 5º-D (software desenvolvido no estabelecimento, academias, laboratórios, diagnóstico por imagem, prótese, administração e locação de imóveis de terceiros, montagem de estandes), conforme os §§ 5º-J e 5º-M.

**Fator r**
```
Fator r = Folha de salários dos 12 meses anteriores (FS12) ÷ RBT12
≥ 28%  → Anexo III        < 28%  → Anexo V
```
Folha (art. 18, § 24, da LC nº 123/2006; art. 26 da Resolução CGSN nº 140/2018): remunerações pagas a empregados, avulsos e contribuintes individuais (pró-labore e autônomos), 13º salário, **mais** o montante efetivamente recolhido de contribuição patronal previdenciária — **inclusive a CPP recolhida dentro do DAS** — e de FGTS. A folha é somada pelo regime de caixa (valores pagos). **Não** entram distribuição de lucros, aluguéis, bolsa de estagiário nem pagamentos a MEI (pergunta 5.11 do Perguntas e Respostas do Simples Nacional, atualizado em 09/10/2026).

Atenção: escritório de **contabilidade** fica no Anexo III sem fator r (§ 5º-B, XIV) e **advocacia** no Anexo IV (§ 5º-C, VII). Corretagem de seguros (§ 5º-B, XVII) também é Anexo III sem fator r.

Se o PGDAS-D usou o Anexo errado: recalcular e informar a diferença do DAS.

### Etapa 4 — Alíquota efetiva e DAS
```
Alíquota efetiva = (RBT12 × alíquota nominal − parcela a deduzir) ÷ RBT12
DAS da atividade = receita do mês da atividade × alíquota efetiva (com as segregações)
```
Conferir: faixa da RBT12 (total da empresa, todas as atividades), alíquota efetiva (tolerância 0,01 p.p.) e valor do DAS. Atividades em Anexos diferentes: cada receita no seu Anexo, mas a faixa usa a RBT12 total. Tabelas e partilhas: o Anexo B no fim deste arquivo.

### Etapa 5 — ICMS e ISS
- **Dentro do DAS** (regra): quando a receita não passa do sublimite estadual. Em 2026 o sublimite é de R$ 3.600.000,00 em todos os estados e no Distrito Federal (Portaria CGSN nº 54/2025). O CGSN divulga a cada ano se algum estado adotou o sublimite opcional de R$ 1.800.000,00 (art. 19 da LC nº 123/2006): conferir a portaria do ano.
- **Fora do DAS**: se a receita passa do sublimite, ICMS e ISS são recolhidos pelo regime normal (arts. 19 e 20 da LC nº 123/2006), e os federais seguem no DAS. Também fora do DAS o ISS em valor fixo do escritório contábil autorizado pela lei municipal (art. 18, § 22-A) e os valores fixos mensais de ICMS/ISS que o ente adotar para ME com receita de até R$ 360.000,00 (art. 18, § 18; art. 33 da Resolução CGSN nº 140/2018).
- **Não existe "lista de municípios que permitem ISS no Simples"**: o município não escolhe se o ISS fica dentro ou fora do DAS.
- **Teto de 5% de ISS**: nos Anexos III e IV o percentual efetivo de ISS dentro do DAS é limitado a 5%; o excedente vai para os tributos federais (notas dos Anexos). Os Anexos não trazem piso de ISS, mas o município não pode conceder isenção ou redução que resulte em ISS abaixo de 2%, salvo nos subitens 7.02, 7.05 e 16.01 da lista da LC nº 116/2003 (art. 31 da Resolução CGSN nº 140/2018).
- **ISS retido pelo tomador**: a receita é informada como "com retenção" e a parcela de ISS sai do DAS. A retenção deve ter sido feita pela alíquota efetiva de ISS informada na nota (a do mês anterior ao da prestação); no mês de início de atividade, 2%; sem informação na nota, 5% (art. 21, § 4º, I, II e V, da LC nº 123/2006). ISS em valor fixo não sofre retenção (art. 21, § 4º, IV).

### Etapa 6 — Retenções nas notas de serviços tomados
Regras completas no Anexo C, no fim deste arquivo.

| Tributo | Alíquota | Prestador do Simples | Observação |
|---|---|---|---|
| IRRF | 1,5% (profissionais) ou 1% (limpeza, conservação, segurança, vigilância, locação de mão de obra) | Dispensado (art. 1º da IN RFB nº 765/2007), com declaração de optante | Dispensa da retenção de até R$ 10,00 por pagamento (art. 67 da Lei nº 9.430/1996) |
| CSRF (PIS+COFINS+CSLL) | 4,65% | Dispensado (art. 32, III, da Lei nº 10.833/2003), com declaração de optante | Dispensa de retenção ≤ R$ 10,00 por pagamento (não há mais limite mensal de R$ 5.000) |
| INSS | 11% | Só se a atividade for do **Anexo IV** (arts. 166 e 167 da IN RFB nº 2.110/2022) | Serviço precisa estar na lista da IN RFB nº 2.110/2022 |
| ISS | alíquota municipal ou efetiva do Simples | Pode haver retenção | Conforme lei municipal e art. 6º da LC nº 116/2003 |

Verificar em cada nota: (1) prestador é optante e apresentou declaração? (2) serviço sujeito a INSS e prestador no Anexo IV? (3) o município exige retenção de ISS? (4) houve retenção indevida ou faltou retenção?

### Etapa 7 — Relatório
**Cabeçalho**: EMPRESA EXEMPLO LTDA, CNPJ 00.000.000/0001-00, atividade principal, período, Anexo(s).

**Status**: OK · Atenção · Divergência (sem emoji; usar palavra ou símbolo simples).

| Verificação | Resultado | Observação |
|---|---|---|
| Receita do mês | | |
| RBT12 e faixa | | |
| Anexo / fator r | | |
| Alíquota efetiva | | |
| Valor do DAS | | |
| Segregações (ST, monofásico, exportação, ISS retido) | | |
| ICMS/ISS (sublimite) | | |
| Retenções INSS | | |
| Retenções ISS | | |
| Retenções IRRF/CSRF | | |

**Impacto financeiro**: DAS correto × declarado; retenções não feitas (risco do tomador); retenções indevidas (pedido de restituição do prestador).
**Ações**: o que corrigir, quem faz e prazo (retificação do PGDAS-D; DAS vence no dia 20 do mês seguinte).

## Erros comuns / pontos de atenção
- Colocar advocacia no fator r (é Anexo IV) ou contabilidade no fator r (é Anexo III).
- Tirar a CPP paga no DAS da folha do fator r (ela entra).
- Usar 13,20% na 3ª faixa do Anexo III (o correto é 13,50%).
- Usar a partilha da 1ª faixa do Anexo IV para todas as faixas.
- Achar que o município decide se o ISS fica no DAS.
- Esquecer a segregação de ICMS-ST e monofásicos (paga duas vezes).
- Reter INSS de prestador do Simples fora do Anexo IV.
- Usar limite mensal de R$ 5.000 para CSRF (regra revogada em 2015).
- Esquecer o limite de exclusão, medido pela receita bruta acumulada no ano: acima de R$ 4.800.000,00 até R$ 5.760.000,00 → exclusão a partir de 01/01 do ano seguinte; acima de R$ 5.760.000,00 → exclusão a partir do mês seguinte ao do excesso (art. 30 da LC nº 123/2006; pergunta 4.3 do Perguntas e Respostas do Simples Nacional).

## Perguntas que o usuário costuma fazer
- **"Psicóloga sem pró-labore paga mais?"** Sim. Sem folha, o fator r fica abaixo de 28% e a receita vai para o Anexo V (15,5% na 1ª faixa contra 6% no Anexo III).
- **"O ISS do Simples pode ser menor que 2%?"** Pela partilha do Anexo, sim (por exemplo, no início da 2ª faixa do Anexo III). O que a lei proíbe é o município conceder isenção ou redução que leve o ISS abaixo de 2% (art. 31 da Resolução CGSN nº 140/2018). Na retenção do mês de início de atividade a alíquota é 2% (art. 21, § 4º, II, da LC nº 123/2006).
- **"Distribuição de lucros conta no fator r?"** Não.
- **"A CPP que pago no DAS entra na folha do fator r?"** Sim, como encargo efetivamente recolhido (art. 26 da Resolução CGSN nº 140/2018).

## Formato de entrega
- Relatório de conferência e pareceres: documento DOCX.
- Recálculos e memória: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- LC nº 123/2006 — art. 3º, § 1º (receita bruta); art. 13, § 1º (tributos fora do DAS); art. 17, XIV (vedação de loteamento e incorporação); art. 18, §§ 1º, 1º-A (alíquota efetiva), 5º-B a 5º-M (Anexos e fator r), 18 (valores fixos), 22-A (ISS fixo do escritório contábil), 24 (folha do fator r); arts. 19 e 20 (sublimite); art. 21, § 4º (retenção de ISS); art. 30 (exclusão); Anexos I a V (redação da LC nº 155/2016).
- Resolução CGSN nº 140/2018 — arts. 17 e 18 (devolução e cancelamento), art. 25 (Anexos), art. 26 (folha do fator r), art. 31 (piso municipal de 2% do ISS), art. 33 (valores fixos).
- Portaria CGSN nº 54/2025 — sublimite de R$ 3.600.000,00 para 2026.
- Resolução CGSN nº 186/2026, alterada pela Resolução CGSN nº 194/2026 — opção pelo regime regular de IBS/CBS e prazos para 2027.
- Perguntas e Respostas do Simples Nacional (CGSN, atualizado em 09/10/2026) — perguntas 4.3, 5.2, 5.3, 5.4, 5.7, 5.11, 5.14, 5.18 e 8.1.
- LC nº 116/2003, art. 6º — responsabilidade pelo ISS.
- Lei nº 8.212/1991, art. 31, e IN RFB nº 2.110/2022, arts. 111, 112, 166 e 167 — retenção de 11%.
- Lei nº 10.833/2003, arts. 30 a 32 (redação da Lei nº 13.137/2015) — CSRF.
- IN RFB nº 765/2007, art. 1º — dispensa de IRRF para optante do Simples.
- Lei nº 9.430/1996, art. 67 — dispensa da retenção de IRRF de até R$ 10,00.
- Decreto nº 9.580/2018 (RIR/2018), arts. 714 e 716 — IRRF sobre serviços.
- EC nº 132/2023 e LC nº 214/2025 — Reforma Tributária.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

## Anexo A · Atividade (CNAE) → Anexo do Simples Nacional

> Base legal: LC nº 123/2006, art. 18, §§ 5º-B a 5º-M (redação da LC nº 155/2016), conferidos no Planalto em 15/11/2026; Resolução CGSN nº 140/2018, art. 25 (inclusive o anexo com CNAEs impeditivos e ambíguos); Perguntas e Respostas do Simples Nacional (CGSN, atualizado em 09/10/2026), pergunta 5.2.

---

## Como usar este arquivo
1. O Anexo é definido pela **atividade efetivamente exercida** (descrição do serviço ou da venda), conforme o art. 18 da LC nº 123/2006. O CNAE é **indicativo**.
2. Localize a atividade nas seções abaixo (organizadas pelo dispositivo da lei).
3. Para atividades sujeitas ao **fator r** (Seção 5), calcule o fator r antes de definir Anexo III ou V.
4. Os códigos CNAE citados são exemplos. Antes de usar no cliente, confira a subclasse e a descrição exatas na tabela CNAE oficial (IBGE/CONCLA) e se o CNAE é **impeditivo** ou **ambíguo** no anexo da Resolução CGSN nº 140/2018.

---

## Seção 1 — Comércio → ANEXO I
Revenda de mercadorias, no varejo ou no atacado.

| CNAE (divisão/classe) | Atividade |
|---|---|
| 45 | Comércio de veículos, peças e acessórios (a parte de **manutenção e reparação** é serviço: ver Seção 3) |
| 46 | Comércio por atacado |
| 47 | Comércio varejista |
| 5611-2 | Restaurantes, bares e lanchonetes (fornecimento de alimentação é operação com ICMS) |
| 5620-1 | Serviços de alimentação para eventos e fornecimento de refeições: o **fornecimento de alimentação e bebidas** vai para o Anexo I (ICMS); a organização de festas e recepções e o bufê, sem o fornecimento de alimentos, é serviço do subitem 17.11 da lista da LC nº 116/2003 (ISS, Anexo III). Separar as receitas no PGDAS-D. |

Quem fabrica e vende o que produz → Anexo II na receita de produção própria. Farmácia de manipulação: Anexo III quando o produto é manipulado sob encomenda no próprio estabelecimento; nos demais casos, Anexo I (art. 18, § 4º, VII, da LC nº 123/2006).

---

## Seção 2 — Indústria → ANEXO II
Fabricação, transformação, beneficiamento ou montagem de produtos (divisões 10 a 33 da CNAE), por exemplo: 10–12 alimentos e bebidas; 13–15 têxtil, vestuário e calçados; 16–18 madeira, papel e **gráfica** (inclusive impressão de material publicitário, 1813-0/01); 20 química; 22 borracha e plástico; 23 minerais não metálicos; 24–25 metalurgia; 26–27 eletrônicos e equipamentos elétricos; 28–30 máquinas e veículos; 31–32 móveis e outros.

Atenção: a divisão 33 (manutenção e reparação de máquinas) é **serviço** de instalação, reparo e manutenção → Anexo III (§ 5º-B, IX).
Atividades vedadas no Simples (ex.: fabricação de bebidas alcoólicas, exceto as do art. 17, § 1º; cigarros; armas) → conferir o art. 17 da LC nº 123/2006.

---

## Seção 3 — Serviços sem fator r → ANEXO III
**§ 5º-B (exceto os incisos sujeitos ao fator r) e § 5º-F**, por exemplo:
- Creche, pré-escola, ensino fundamental, ensino técnico, idiomas, artes, cursos preparatórios (§ 5º-B, I).
- Agência terceirizada de correios (II); agência de viagem e turismo (III); autoescola (IV); agência lotérica (V).
- Instalação, reparos e manutenção em geral; usinagem, solda e tratamento de metais (IX) — ex.: 3311 a 3329, 4520-0 (manutenção de veículos), 9511-8 (manutenção de computadores).
- Transporte municipal de passageiros e de cargas (XIII) — ex.: 4921-3.
- Coleta de resíduos não perigosos.
- **Escritório de serviços contábeis (XIV)** — 6920-6/01. **Sem fator r.** Se a lei municipal autorizar o ISS em valor fixo, ele é pago em guia do município e o PGDAS-D desconsidera a parcela de ISS (art. 18, § 22-A; pergunta 5.14 do Perguntas e Respostas do Simples Nacional). O escritório precisa cumprir as obrigações do § 22-B, sob pena de exclusão (§ 22-C).
- Produções cinematográficas, audiovisuais, artísticas e culturais (XV) — ex.: 5911-1, 5912-0, 9001-9.
- Corretagem de seguros (XVII) — 6622-3.
- Corretagem de imóveis de terceiros e serviços vinculados à locação de imóveis (assessoria locatícia e avaliação para locação).
- Locação de bens móveis — ex.: 7711-0, 7719-5, 7721-7, 7723-3, 7729-2, 7731-4, 7732-2, 7733-1, 7739-0 (Anexo III sem a parcela de ISS, pois locação de bem móvel não é serviço — Súmula Vinculante 31 do STF).
- Hotelaria e alojamento — 5510-8, 5590-6.
- Lavanderia (9601-7), cabeleireiro e estética (9602-5), serviços funerários (9603-3), outros serviços pessoais (9609-2).
- Organização de feiras e eventos (8230-0), cobrança (8291-1), envasamento e empacotamento por conta de terceiros (8292-0), call center (8220-2).

**§ 5º-E — Anexo III com ICMS no lugar do ISS**: serviços de **comunicação** (inclusive telecomunicações, 61xx) e **transporte intermunicipal e interestadual de cargas e de passageiros** permitidos (ex.: 4930-2, 4929-9 quando intermunicipal). O ISS é retirado da partilha e entra o percentual de ICMS do Anexo I.

---

## Seção 4 — ANEXO IV (§ 5º-C) — sem CPP no DAS
- **Construção de imóveis e obras de engenharia em geral**, inclusive subempreitada, execução de projetos, paisagismo e decoração de interiores (I) — ex.: 4120-4, 4211-1, 4212-0, 4213-8, 4221-9, 4222-7, 4223-5, 4291-0, 4299-5, 4311-8, 4312-6, 4313-4, 4319-3, 4391-6, 4399-1.
- **Vigilância, limpeza ou conservação** (VI) — ex.: 8011-1/01 (vigilância e segurança privada), 8121-4 (limpeza em prédios e domicílios), 8129-0 (outras limpezas). Inclui dedetização, desratização e demais serviços de controle de pragas urbanas (8122-2), considerados limpeza e conservação (pergunta 5.18 do Perguntas e Respostas do Simples Nacional).
- **Serviços advocatícios** (VII) — 6911-7/01.

Como decidir nos casos de fronteira:
- Instalações elétricas e hidráulicas, montagem industrial e obras de acabamento (4321-5, 4322-3, 4329-1, 4330-4, 4292-8): os subitens 7.02 e 7.05 da lista da LC nº 116/2003 têm item próprio no PGDAS-D e vão para o Anexo III ou IV conforme a atividade. Se for execução de obra, Anexo IV; se for só instalação, reparo ou manutenção, Anexo III (§ 5º-B, IX). Decidir pelo contrato e pela descrição da NFS-e.
- Incorporação imobiliária (4110-7) e loteamento: **vedados** ao Simples (art. 17, XIV, da LC nº 123/2006). Construção por empreitada para terceiros é Anexo IV.
- Transporte de valores (8012-9), monitoramento de sistemas de segurança (8020-0) e serviços combinados para apoio a edifícios (8111-7, 8112-5): verificar, pelo contrato, se o serviço prestado é vigilância, limpeza ou conservação (Anexo IV) ou outro serviço (Anexo III), e se o CNAE consta como ambíguo no anexo da Resolução CGSN nº 140/2018.

Lembrete: no Anexo IV a CPP sobre a folha é paga à parte (eSocial/DCTFWeb).

---

## Seção 5 — Atividades sujeitas ao FATOR R → ANEXO III (r ≥ 28%) ou ANEXO V (r < 28%)

### Fórmula
```
Fator r = Folha de salários dos 12 meses anteriores ÷ RBT12
Folha (art. 18, § 24, da LC nº 123/2006; art. 26 da Resolução CGSN nº 140/2018):
  + remunerações de empregados e avulsos, com 13º salário
  + pró-labore dos sócios e pagamentos a autônomos
  + encargos efetivamente recolhidos: contribuição patronal previdenciária
    (inclusive a CPP recolhida dentro do DAS) e FGTS
  − NÃO entram distribuição de lucros, aluguéis, bolsa de estagiário e pagamentos a MEI
  (folha pelo regime de caixa: valores pagos)
```

| Fator r | Anexo |
|---|---|
| ≥ 28% | **Anexo III** (6% a 33%) |
| < 28% | **Anexo V** (15,5% a 30,5%) |

### Grupo A — § 5º-B com § 5º-M (saúde e arquitetura)
| Atividade | CNAE (exemplos) |
|---|---|
| Fisioterapia (XVI) | 8650-0/04 |
| Arquitetura e urbanismo (XVIII) | 7111-1/00 |
| Medicina, inclusive laboratorial, e enfermagem (XIX) | classe 8630-5 (atividade médica ambulatorial), 8650-0/01 (enfermagem) |
| Odontologia e prótese dentária (XX) | 8630-5/04 (atividade odontológica) |
| Psicologia, psicanálise, terapia ocupacional, acupuntura, podologia, fonoaudiologia, clínicas de nutrição e de vacinação e bancos de leite (XXI) | 8650-0/03 (psicologia e psicanálise), 8650-0/05, 8650-0/06, 8650-0/02, 8690-9/03, 8690-9/04 |

### Grupo B — § 5º-D com § 5º-M
| Atividade | CNAE (exemplos) |
|---|---|
| Administração e locação de imóveis de terceiros (I) | 6821-8, 6822-6 |
| Academias de dança, capoeira, ioga, artes marciais, atividades físicas, natação e escolas de esportes (II e III) | 8591-1, 8592-9, 9313-1 |
| Programas de computador, licenciamento de software e páginas eletrônicas, desde que desenvolvidos no estabelecimento do optante (IV a VI) | 6201-5/01, 6201-5/02, 6202-3/00, 6203-1/00, 6204-0/00, 6209-1/00 |
| Montagem de estandes para feiras (IX) | conferir a subclasse no CONCLA |
| Laboratórios de análises clínicas ou de patologia clínica (XII) | 8640-2/01, 8640-2/02 |
| Tomografia, diagnóstico por imagem, registros gráficos e métodos ópticos, ressonância magnética (XIII) | subclasses de diagnóstico da classe 8640-2 |
| Prótese em geral (XIV) | 3250-7/06 (serviços de prótese dentária) |

### Grupo C — § 5º-I com § 5º-J (atividades intelectuais)
| Atividade | CNAE (exemplos) |
|---|---|
| Medicina veterinária (II) | 7500-1 |
| Comissaria, despachantes, tradução e interpretação (V) | 7490-1/01 (tradução e interpretação) |
| Engenharia, medição, cartografia, topografia, geologia, geodésia, testes, suporte e análises técnicas, pesquisa, design, desenho e agronomia (VI) | 7112-0/00, 7119-7/01, 7119-7/03, 7119-7/99, 7120-1, 7210-0, 7220-7, 7410-2, 7490-1/03 |
| Representação comercial e demais intermediações de negócios e serviços de terceiros (VII) | 4611-7 a 4619-2 (representantes comerciais), 7490-1/04 |
| Perícia, leilão e avaliação (VIII) | conferir a subclasse no CONCLA conforme o serviço |
| Auditoria, economia, consultoria, gestão, organização, controle e administração (IX) | 6920-6/02 (consultoria e auditoria contábil e tributária), 7020-4/00 |
| Jornalismo e publicidade (X) | 7311-4, 7312-2, 7319-0, 7320-3 |
| Agenciamento, exceto de mão de obra (XI) | 7490-1/04, 7490-1/05 |
| Outras atividades intelectuais, técnicas, científicas, desportivas, artísticas ou culturais não sujeitas aos Anexos III ou IV (XII) | conferir a subclasse no CONCLA conforme o serviço |

### Itens que não pertencem a esta seção
- **Advocacia (6911-7/01)** → Anexo IV (§ 5º-C, VII). Não tem fator r.
- **Contabilidade (6920-6/01)** → Anexo III (§ 5º-B, XIV). Não tem fator r.
- **Corretagem de seguros** → Anexo III (§ 5º-B, XVII). Não tem fator r.
- A classe 6920-6 tem só as subclasses /01 e /02.
- **Bancos, financeiras, crédito, capitalização, fundos e holdings** (6411 a 6499) → atividades vedadas ou incompatíveis com o Simples (art. 3º, § 4º, VIII, e art. 17, I, da LC nº 123/2006; anexo de CNAEs impeditivos da Resolução CGSN nº 140/2018).
- **Cartórios (6912-5)** → serviço notarial delegado à pessoa física do titular; não é empresa do Simples.
- **Telecomunicações (61xx)** → § 5º-E (Anexo III com ICMS), não fator r.
- **Impressão de material publicitário (1813-0/01)** → indústria gráfica (Anexo II).
- **8630-5/04** é atividade odontológica; psicologia é 8650-0/03.
- Atividade hospitalar é a classe 8610-1 (não 8630-5/01).
- 7490-1/02 é escafandria e mergulho e 8011-1/02 é adestramento de cães de guarda: não usar esses códigos para secretariado ou investigação.

---

## Alerta crítico: fator r baixo
Empresas de serviços do fator r em que os sócios **não retiram pró-labore** (ou retiram pouco) ficam com fator r perto de zero e caem no Anexo V.

**Exemplo (psicologia, CNAE 8650-0/03 — EMPRESA EXEMPLO SERVIÇOS LTDA)**

| Situação | Fator r | Anexo | Alíquota 1ª faixa |
|---|---|---|---|
| Sócia retira R$ 4.000/mês de pró-labore (folha 12 meses ≈ R$ 48.000 + encargos), RBT12 = R$ 120.000 | ≥ 40% | III | 6,00% |
| Sócia não retira pró-labore, RBT12 = R$ 120.000 | 0% | V | 15,50% |
| Diferença no DAS mensal (receita R$ 10.000) | | | R$ 950,00/mês |

Isso equivale a R$ 11.400/ano de diferença no DAS. Na decisão, considerar também o custo do pró-labore (INSS de 11% do sócio e IRRF) — o ganho líquido é menor que a diferença do DAS.

---

## Resumo visual
```
Atividade da empresa
  ├─ Comércio (inclui restaurante) ───────────────────► ANEXO I
  ├─ Indústria (inclui gráfica) ──────────────────────► ANEXO II
  ├─ Construção / vigilância / limpeza / advocacia ──► ANEXO IV (CPP fora do DAS)
  ├─ Comunicação / transporte intermunicipal ────────► ANEXO III com ICMS (§ 5º-E)
  ├─ Serviço do § 5º-B sem fator r (ex.: contabilidade) ► ANEXO III
  └─ Serviço com fator r (§§ 5º-I, 5º-D e 5º-B XVI, XVIII–XXI)
        ├─ r ≥ 28% ──► ANEXO III
        └─ r < 28% ──► ANEXO V
```

---
> Material de apoio criado por Marcia — contadora. Validado em 15/11/2026.

## Anexo B · Tabelas do Simples Nacional — Anexos I a V

> Base legal: Anexos I a V da LC nº 123/2006, na redação da LC nº 155/2016 (vigência desde 01/01/2018), conferidos no Planalto em 15/11/2026; Resolução CGSN nº 140/2018.
> Limite anual: R$ 4.800.000,00. Sublimite de ICMS/ISS em 2026: R$ 3.600.000,00 em todos os estados e no Distrito Federal (Portaria CGSN nº 54/2025). O sublimite opcional de R$ 1.800.000,00 (art. 19 da LC nº 123/2006) só vale no estado que o adotar na portaria anual do CGSN.

---

## Fórmula geral
```
Alíquota efetiva = (RBT12 × alíquota nominal − parcela a deduzir) ÷ RBT12
DAS da atividade = receita do mês × alíquota efetiva
Valor de cada tributo = alíquota efetiva × percentual de repartição da faixa
```

---

## ANEXO I — Comércio

| Faixa | RBT12 (R$) | Alíquota nominal | Parcela a deduzir (R$) |
|---|---|---|---|
| 1ª | até 180.000,00 | 4,00% | — |
| 2ª | 180.000,01 a 360.000,00 | 7,30% | 5.940,00 |
| 3ª | 360.000,01 a 720.000,00 | 9,50% | 13.860,00 |
| 4ª | 720.000,01 a 1.800.000,00 | 10,70% | 22.500,00 |
| 5ª | 1.800.000,01 a 3.600.000,00 | 14,30% | 87.300,00 |
| 6ª | 3.600.000,01 a 4.800.000,00 | 19,00% | 378.000,00 |

### Repartição Anexo I (%)
| Faixa | IRPJ | CSLL | COFINS | PIS | CPP | ICMS |
|---|---|---|---|---|---|---|
| 1ª e 2ª | 5,50 | 3,50 | 12,74 | 2,76 | 41,50 | 34,00 |
| 3ª a 5ª | 5,50 | 3,50 | 12,74 | 2,76 | 42,00 | 33,50 |
| 6ª | 13,50 | 10,00 | 28,27 | 6,13 | 42,10 | — |

> Na 6ª faixa o ICMS é recolhido fora do DAS (acima do sublimite).

---

## ANEXO II — Indústria

| Faixa | RBT12 (R$) | Alíquota nominal | Parcela a deduzir (R$) |
|---|---|---|---|
| 1ª | até 180.000,00 | 4,50% | — |
| 2ª | 180.000,01 a 360.000,00 | 7,80% | 5.940,00 |
| 3ª | 360.000,01 a 720.000,00 | 10,00% | 13.860,00 |
| 4ª | 720.000,01 a 1.800.000,00 | 11,20% | 22.500,00 |
| 5ª | 1.800.000,01 a 3.600.000,00 | 14,70% | 85.500,00 |
| 6ª | 3.600.000,01 a 4.800.000,00 | 30,00% | 720.000,00 |

### Repartição Anexo II (%) — o IPI representa 7,5% da alíquota efetiva nas faixas 1 a 5
| Faixa | IRPJ | CSLL | COFINS | PIS | CPP | IPI | ICMS |
|---|---|---|---|---|---|---|---|
| 1ª a 5ª | 5,50 | 3,50 | 11,51 | 2,49 | 37,50 | 7,50 | 32,00 |
| 6ª | 8,50 | 7,50 | 20,96 | 4,54 | 23,50 | 35,00 | — |

---

## ANEXO III — Serviços (art. 18, §§ 5º-B, 5º-D, 5º-E e 5º-F; e os do fator r ≥ 28%)

| Faixa | RBT12 (R$) | Alíquota nominal | Parcela a deduzir (R$) |
|---|---|---|---|
| 1ª | até 180.000,00 | 6,00% | — |
| 2ª | 180.000,01 a 360.000,00 | 11,20% | 9.360,00 |
| 3ª | 360.000,01 a 720.000,00 | **13,50%** | 17.640,00 |
| 4ª | 720.000,01 a 1.800.000,00 | 16,00% | 35.640,00 |
| 5ª | 1.800.000,01 a 3.600.000,00 | 21,00% | 125.640,00 |
| 6ª | 3.600.000,01 a 4.800.000,00 | 33,00% | 648.000,00 |

### Repartição Anexo III (%)
| Faixa | IRPJ | CSLL | COFINS | PIS | CPP | ISS |
|---|---|---|---|---|---|---|
| 1ª | 4,00 | 3,50 | 12,82 | 2,78 | 43,40 | 33,50 |
| 2ª | 4,00 | 3,50 | 14,05 | 3,05 | 43,40 | 32,00 |
| 3ª | 4,00 | 3,50 | 13,64 | 2,96 | 43,40 | 32,50 |
| 4ª | 4,00 | 3,50 | 13,64 | 2,96 | 43,40 | 32,50 |
| 5ª | 4,00 | 3,50 | 12,82 | 2,78 | 43,40 | 33,50 (*) |
| 6ª | 35,00 | 15,00 | 16,03 | 3,47 | 30,50 | — |

(*) O percentual efetivo máximo de ISS é 5%. Na 5ª faixa, quando a alíquota efetiva passar de 14,92537%, o ISS fica fixo em 5% e o restante (alíquota efetiva − 5%) é repartido: IRPJ 6,02%; CSLL 5,26%; COFINS 19,28%; PIS 4,18%; CPP 65,26%.

> Na 6ª faixa o ISS é recolhido fora do DAS (acima do sublimite).

### ISS: teto de 5% nos Anexos; piso de 2% só para benefícios municipais
Os Anexos da LC nº 123/2006 limitam o ISS a 5% e transferem o excedente para os tributos federais. Os Anexos **não** trazem piso: o percentual de ISS resulta da partilha da faixa. O limite de 2% vale em duas situações diferentes:
- o município não pode conceder isenção ou redução que resulte em ISS abaixo de 2%, salvo nos subitens 7.02, 7.05 e 16.01 da lista da LC nº 116/2003 (art. 31 da Resolução CGSN nº 140/2018);
- na retenção do ISS no mês de início de atividade, o tomador aplica a alíquota efetiva de 2% (art. 21, § 4º, II, da LC nº 123/2006).

---

## ANEXO IV — Construção civil, vigilância, limpeza, conservação e advocacia (art. 18, § 5º-C)

| Faixa | RBT12 (R$) | Alíquota nominal | Parcela a deduzir (R$) |
|---|---|---|---|
| 1ª | até 180.000,00 | 4,50% | — |
| 2ª | 180.000,01 a 360.000,00 | 9,00% | 8.100,00 |
| 3ª | 360.000,01 a 720.000,00 | 10,20% | 12.420,00 |
| 4ª | 720.000,01 a 1.800.000,00 | 14,00% | 39.780,00 |
| 5ª | 1.800.000,01 a 3.600.000,00 | 22,00% | 183.780,00 |
| 6ª | 3.600.000,01 a 4.800.000,00 | 33,00% | 828.000,00 |

### Repartição Anexo IV (%) — cada faixa tem a sua
| Faixa | IRPJ | CSLL | COFINS | PIS | ISS |
|---|---|---|---|---|---|
| 1ª | 18,80 | 15,20 | 17,67 | 3,83 | 44,50 |
| 2ª | 19,80 | 15,20 | 20,55 | 4,45 | 40,00 |
| 3ª | 20,80 | 15,20 | 19,73 | 4,27 | 40,00 |
| 4ª | 17,80 | 19,20 | 18,90 | 4,10 | 40,00 |
| 5ª | 18,80 | 19,20 | 18,08 | 3,92 | 40,00 (*) |
| 6ª | 53,50 | 21,50 | 20,55 | 4,45 | — |

(*) ISS limitado a 5%. Na 5ª faixa, quando a alíquota efetiva passar de 12,5%, o ISS fica em 5% e o restante é repartido: IRPJ 31,33%; CSLL 32,00%; COFINS 30,13%; PIS 6,54%.

> **Atenção**: o Anexo IV **não inclui a CPP** (contribuição previdenciária patronal) no DAS. A empresa recolhe a CPP sobre a folha segundo a legislação dos demais contribuintes (art. 13, VI, e art. 18, § 5º-C, da LC nº 123/2006; arts. 168 a 171 da IN RFB nº 2.110/2022): 20% sobre a remuneração mais a contribuição para riscos ambientais do trabalho (RAT), declarada no eSocial e paga via DCTFWeb. O percentual de RAT e o FAP variam conforme a atividade preponderante e o estabelecimento: conferir no caso concreto. As contribuições a terceiros (Sistema S) continuam dispensadas para o optante (art. 13, § 3º, da LC nº 123/2006).

---

## ANEXO V — Serviços do fator r < 28% (art. 18, §§ 5º-I, 5º-J e 5º-M)

Atividades típicas: engenharia, consultoria, auditoria, publicidade, representação comercial, perícia, medicina veterinária, despachante, tradução, medicina, odontologia, psicologia, fisioterapia, arquitetura, software desenvolvido no estabelecimento — quando o fator r for menor que 28%. **Não** inclui advocacia (Anexo IV) nem escritório de contabilidade (Anexo III).

| Faixa | RBT12 (R$) | Alíquota nominal | Parcela a deduzir (R$) |
|---|---|---|---|
| 1ª | até 180.000,00 | 15,50% | — |
| 2ª | 180.000,01 a 360.000,00 | 18,00% | 4.500,00 |
| 3ª | 360.000,01 a 720.000,00 | 19,50% | 9.900,00 |
| 4ª | 720.000,01 a 1.800.000,00 | 20,50% | 17.100,00 |
| 5ª | 1.800.000,01 a 3.600.000,00 | 23,00% | 62.100,00 |
| 6ª | 3.600.000,01 a 4.800.000,00 | 30,50% | 540.000,00 |

### Repartição Anexo V (%)
| Faixa | IRPJ | CSLL | COFINS | PIS | CPP | ISS |
|---|---|---|---|---|---|---|
| 1ª | 25,00 | 15,00 | 14,10 | 3,05 | 28,85 | 14,00 |
| 2ª | 23,00 | 15,00 | 14,10 | 3,05 | 27,85 | 17,00 |
| 3ª | 24,00 | 15,00 | 14,92 | 3,23 | 23,85 | 19,00 |
| 4ª | 21,00 | 15,00 | 15,74 | 3,41 | 23,85 | 21,00 |
| 5ª | 23,00 | 12,50 | 14,10 | 3,05 | 23,85 | 23,50 |
| 6ª | 35,00 | 15,50 | 16,44 | 3,56 | 29,50 | — |

---

## Exemplos de cálculo

### Exemplo 1 — Psicologia no Anexo V, 1ª faixa
- RBT12: R$ 120.000,00 · receita do mês: R$ 10.000,00
- Alíquota efetiva: (120.000 × 15,5% − 0) ÷ 120.000 = **15,50%**
- DAS: 10.000 × 15,50% = **R$ 1.550,00**

### Exemplo 2 — A mesma empresa no Anexo III (fator r ≥ 28%), 1ª faixa
- Alíquota efetiva: **6,00%** · DAS: **R$ 600,00**
- Diferença de R$ 950,00 por mês só pelo Anexo.

### Exemplo 3 — Serviço, 3ª faixa, Anexo III
- RBT12: R$ 500.000,00 · receita do mês: R$ 42.000,00
- Alíquota efetiva: (500.000 × 13,50% − 17.640) ÷ 500.000 = (67.500 − 17.640) ÷ 500.000 = **9,972%**
- DAS: 42.000 × 9,972% = **R$ 4.188,24**

### Exemplo 4 — Comércio, Anexo I, 4ª faixa
- RBT12: R$ 900.000,00 · receita do mês: R$ 80.000,00
- Efetiva = (900.000 × 10,70% − 22.500) ÷ 900.000 = **8,20%** · DAS = **R$ 6.560,00**

---

## Atividades mistas (mais de um Anexo)
Cada receita é tributada no Anexo da sua atividade, com a alíquota efetiva calculada pela **RBT12 total** da empresa (soma de todas as atividades). No PGDAS-D, informar a receita de cada atividade separadamente e marcar as segregações (ICMS-ST, monofásico, exportação, ISS retido).

---
> Material de apoio criado por Marcia — contadora. Validado em 15/11/2026.

## Anexo C · Retenções na fonte sobre serviços — prestador ou tomador do Simples Nacional

> Base legal: Decreto nº 9.580/2018 (RIR/2018), arts. 714, 716 e 718; Lei nº 9.430/1996, arts. 67 e 68; Lei nº 10.833/2003, arts. 30 a 36 (redação da Lei nº 13.137/2015); IN RFB nº 765/2007; IN SRF nº 459/2004; Lei nº 8.212/1991, art. 31; IN RFB nº 2.110/2022; LC nº 116/2003, art. 6º; LC nº 123/2006, arts. 18-B e 21, § 4º.

---

## Princípio: o que o optante do Simples dispensa e o que não dispensa
O prestador **optante do Simples** que entrega a **declaração de optante** ao tomador fica dispensado das retenções de:
- **IRRF** sobre serviços (art. 1º da IN RFB nº 765/2007);
- **CSRF** (PIS + COFINS + CSLL, 4,65%) — art. 32, III, da Lei nº 10.833/2003 e art. 3º, II, da IN SRF nº 459/2004 (redação da IN RFB nº 765/2007).

Guardar a declaração no dossiê. Declaração falsa transfere a responsabilidade ao prestador.

O Simples **não** dispensa automaticamente:
- **INSS 11%**: só se aplica ao prestador do Simples cuja atividade é tributada no **Anexo IV** (construção, vigilância, limpeza, conservação) — arts. 166 e 167 da IN RFB nº 2.110/2022. Prestador dos Anexos I, II, III e V não sofre retenção de 11%.
- **ISS**: segue a lei municipal e o art. 6º da LC nº 116/2003.

---

## 1. IRRF sobre serviços prestados por PJ

### Alíquotas
| Serviço | Alíquota | Código | Base |
|---|---|---|---|
| Serviços profissionais (medicina, engenharia, arquitetura, advocacia, contabilidade, auditoria, consultoria, análise técnica, programação, publicidade, entre outros da lista legal) | 1,5% | 1708 | art. 714 do RIR/2018 |
| Limpeza, conservação, segurança, vigilância e locação de mão de obra | 1,0% | 1708 | art. 716 do RIR/2018 |
| Comissões, corretagens e outras remunerações por representação comercial ou mediação de negócios | 1,5% | 8045 | art. 718 do RIR/2018 |

Transporte de cargas e de passageiros não constam da lista de retenção de IRRF entre pessoas jurídicas. Construção civil só entra quando o serviço for profissional de engenharia listado no art. 714 do RIR/2018 (projeto, fiscalização, consultoria), não a empreitada de obra: conferir a descrição do serviço na nota.

### Valor mínimo
Fica dispensada a retenção de IRRF de valor igual ou inferior a R$ 10,00 (art. 67 da Lei nº 9.430/1996). A Receita aplica a dispensa a cada pagamento entre pessoas jurídicas, considerando o total pago naquela ocasião, ainda que se refira a mais de uma nota (Solução de Consulta Cosit nº 258/2024). A 1,5%, isso corresponde a pagamento de até R$ 666,66. Se o IRRF retido de um mesmo código no período ficar abaixo de R$ 10,00, ele é somado ao dos períodos seguintes até atingir esse valor, porque não se emite DARF abaixo de R$ 10,00 (art. 68 da Lei nº 9.430/1996).

### Prestador do Simples
Sem retenção de IRRF, com a declaração de optante. Se o tomador reteve indevidamente, o prestador **não** pode abater o valor no DAS: deve pedir restituição (PER/DCOMP) ou acertar com o tomador.

### Tomador do Simples
- **CSRF**: a pessoa jurídica optante pelo Simples **não** está obrigada a reter PIS, COFINS e CSLL quando contrata serviços (art. 30, § 2º, da Lei nº 10.833/2003).
- **IRRF**: os arts. 714 e 716 do RIR/2018 alcançam os pagamentos feitos por pessoas jurídicas em geral e não trazem dispensa para a fonte pagadora optante. Tratar o optante tomador como obrigado à retenção do IRRF, salvo dispensa do caso (prestador optante com declaração, valor de até R$ 10,00).

---

## 2. CSRF — PIS/COFINS/CSLL retidos (código 5952)

| Tributo | Alíquota |
|---|---|
| PIS | 0,65% |
| COFINS | 3,00% |
| CSLL | 1,00% |
| **Total** | **4,65%** |

### Dispensa
- Dispensa quando a retenção de **um pagamento** for igual ou inferior a **R$ 10,00** — isto é, pagamento de até **R$ 215,05** (art. 31, § 3º, da Lei nº 10.833/2003).
- **Não existe soma mensal**: a Lei nº 13.137/2015 revogou o § 4º do art. 31 da Lei nº 10.833/2003. Cada pagamento é avaliado isoladamente.
- **Não existe limite de R$ 5.000,00 por mês** (regra anterior a 2015).

### Prazo
Recolher até o **último dia útil do 2º decêndio do mês seguinte** ao do pagamento (art. 35 da Lei nº 10.833/2003, redação da Lei nº 13.137/2015).

### Prestador do Simples
Sem retenção, mediante declaração de optante.

---

## 3. INSS — retenção de 11%

### Quem retém
A empresa contratante de serviços prestados mediante **cessão de mão de obra ou empreitada**, quando o serviço está **listado nos arts. 111 e 112 da IN RFB nº 2.110/2022** (art. 31 da Lei nº 8.212/1991). Não basta ser "cessão de mão de obra" em abstrato. As hipóteses de dispensa foram consolidadas pela IN RFB nº 2.289/2025: conferir a redação vigente da IN RFB nº 2.110/2022 no caso concreto.

### Base e alíquota
11% sobre o valor bruto da nota, podendo deduzir materiais e equipamentos quando discriminados no contrato e na nota, nos limites da IN RFB nº 2.110/2022. Declarado no evento R-2010 da EFD-Reinf (até o dia 15) e recolhido via DCTFWeb até o dia 20 do mês seguinte à emissão da nota.

### Prestador do Simples
- **Anexo IV** (construção civil, vigilância, limpeza, conservação): **sofre** a retenção de 11% (art. 166 da IN RFB nº 2.110/2022).
- **Anexos I, II, III e V**: **não** sofre a retenção (art. 167 da IN RFB nº 2.110/2022), porque a CPP já está no DAS.

### Serviços que costumam estar na lista (conferir sempre os arts. 111 e 112)
Limpeza, conservação e zeladoria; vigilância e segurança; construção civil (obras, reformas, demolição, instalação); serviços de manutenção de máquinas e equipamentos com cessão; digitação e preparação de dados; serviços de saúde e de TI **somente quando** prestados mediante cessão de mão de obra e listados. Não presumir: conferir o item na IN.

### MEI e autônomo
- **MEI**: não há retenção de 11%. Quando o MEI presta serviços de hidráulica, eletricidade, pintura, alvenaria, carpintaria ou manutenção/reparo de veículos, a **contratante** recolhe a contribuição patronal de 20% sobre o valor pago, sem reter nada do MEI (art. 18-B da LC nº 123/2006; art. 22, III, da Lei nº 8.212/1991; art. 173 da IN RFB nº 2.110/2022).
- **Autônomo (pessoa física)**: a empresa desconta 11% do contribuinte individual (até o teto de R$ 8.475,55 em 2026) e recolhe a sua contribuição de 20%.

---

## 4. ISS — retenção municipal

### Quem retém
O tomador, quando a **lei municipal** o torna responsável, e nos casos do **art. 6º, § 2º, da LC nº 116/2003** (ex.: serviços 3.05, 7.02, 7.04, 7.05, 7.09, 7.10, 7.12, 7.16, 7.17, 7.19, 11.02, 17.05 e 17.10).

### Alíquota
- Prestador fora do Simples: alíquota municipal, entre 2% e 5% (arts. 8º e 8º-A da LC nº 116/2003).
- **Prestador do Simples** (art. 21, § 4º, da LC nº 123/2006): alíquota efetiva de ISS informada na nota, a que o prestador estava sujeito no mês anterior ao da prestação (inciso I); 2% no mês de início de atividade (inciso II); 5% se a nota não informar a alíquota (inciso V). Se o ISS do prestador é recolhido em valor fixo mensal, não cabe retenção (inciso IV).

### Prestador do Simples e ISS retido
- O Simples **não** impede a retenção do ISS. Se o município exige, o tomador retém.
- O ISS **está no DAS por regra** (até o sublimite de R$ 3.600.000,00). Quando há retenção, o prestador informa no PGDAS-D a receita "com retenção de ISS" e a parcela do ISS sai do DAS — por isso **não há pagamento em dobro**.
- O município não escolhe deixar o ISS fora do DAS. O ISS só sai do DAS quando a receita passa do sublimite, no ISS em valor fixo previsto em lei (ex.: escritórios contábeis autorizados pela lei municipal) ou quando há retenção.

### Local de incidência
Regra geral: município do estabelecimento prestador. Exceções: art. 3º da LC nº 116/2003 (obra, limpeza de imóveis, vigilância, fornecimento de mão de obra etc.). Ver skill `calculo-iss`.

---

## 5. Checklist — notas de serviço tomadas

| Item | Verificação |
|---|---|
| Prestador é optante do Simples? | Consultar o CNPJ no portal do Simples e pedir a declaração de optante |
| Anexo do prestador | Se Anexo IV e serviço listado na IN RFB nº 2.110/2022 → reter 11% |
| IRRF | Prestador do Simples com declaração: não reter. Outros: 1,5% ou 1% conforme o serviço, salvo retenção de até R$ 10,00 |
| CSRF | Tomador do Simples: não retém. Prestador do Simples com declaração: não reter. Demais: 4,65%, salvo retenção ≤ R$ 10,00 no pagamento |
| INSS | 11% sobre o bruto, menos materiais/equipamentos discriminados |
| ISS | Lei municipal ou art. 6º, § 2º, da LC nº 116/2003; alíquota efetiva se o prestador for do Simples |
| EFD-Reinf | R-2010 (INSS) e R-4020 (IRRF/CSRF) transmitidos |

---

## 6. Exemplos práticos

### Exemplo A — Empresa do Simples contrata limpeza de outra empresa do Simples
- Prestador: limpeza → Anexo IV.
- **IRRF e CSRF**: prestador do Simples com declaração → não reter. (Além disso, o tomador optante não é obrigado a reter a CSRF.)
- **INSS 11%**: **sim**, se o serviço estiver listado na IN RFB nº 2.110/2022 (limpeza costuma estar).
- **ISS**: conforme lei municipal; se reter, usar a alíquota efetiva informada na nota.

### Exemplo B — Lucro Presumido contrata psicóloga do Simples
- **IRRF e CSRF**: não reter (declaração de optante).
- **INSS**: não (psicologia não é Anexo IV; e atendimento em consultório próprio não é cessão de mão de obra).
- **ISS**: conforme lei municipal.

### Exemplo C — Lucro Real contrata empresa de TI do Simples
- **IRRF e CSRF**: não reter (declaração de optante).
- **INSS**: **não** — TI é Anexo III ou V, e o prestador do Simples fora do Anexo IV não sofre a retenção de 11%.
- **ISS**: conforme lei municipal.

---

## 7. Retenção indevida ou falta de retenção
**Retenção indevida** (o tomador reteve sem dever):
- Federal (IRRF, CSRF, INSS): o prestador pede restituição ou compensação (PER/DCOMP) ou acerta com o tomador. **Não** abate no DAS.
- ISS: pedido de restituição ao município.

**Falta de retenção** (o tomador deveria reter e não reteve):
- INSS 11%: o tomador responde pelo valor não retido, com multa e juros (art. 31 da Lei nº 8.212/1991).
- IRRF e CSRF: o tomador fica sujeito à exigência do valor que deixou de reter, com os acréscimos legais. Avaliar o caso concreto (tributo, data do pagamento e se o prazo de entrega da declaração do prestador já passou) antes de definir quem paga e como regularizar.

Recomendação: exigir a declaração de optante e manter controle das retenções para comprovar em fiscalização.

---
> Material de apoio criado por Marcia — contadora. Validado em 15/11/2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
