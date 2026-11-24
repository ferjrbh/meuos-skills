---
name: abertura-empresa-cnpj
description: "Conduz a abertura de empresa pela REDESIM (Lei nº 11.598/2007, com as simplificações da Lei nº 14.195/2021) — consulta de viabilidade (nome e endereço × CNAE), DBE, contrato social com as cláusulas do art. 997 do Código Civil, registro na Junta Comercial ou no Cartório, inscrições estadual e municipal, licenças e opção de regime tributário (Simples Nacional na abertura: pedido feito junto com a inscrição no CNPJ, pelo Portal Redesim, com efeito desde a inscrição — Resolução CGSN nº 183/2025; Presumido ou Real com o primeiro pagamento). Acionar quando o usuário disser \"abrir empresa\", \"abrir CNPJ\", \"nova empresa\", \"segunda empresa\", \"REDESIM\", \"NIRE\", \"DBE\", \"contrato social\", \"SLU\", \"LTDA\", \"MEI, ME ou EPP\". Entrega: checklist completo, cronograma de 5 a 15 dias, roteiro da minuta de contrato social e encaminhamento do plano de contas."
version: 1.1
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Abertura de empresa (CNPJ) pela REDESIM

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Organiza a abertura de uma empresa do zero: escolhe o tipo societário, confere CNAE e endereço, roteiriza a REDESIM (Rede Nacional para a Simplificação do Registro e da Legalização de Empresas e Negócios), lista as cláusulas obrigatórias do contrato social e controla os prazos da opção tributária. O resultado é um checklist com cronograma e os encaminhamentos para contrato social e plano de contas.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Abertura de empresa nova ou de segunda empresa de um cliente.
- Dúvida sobre tipo societário (MEI, empresário individual, LTDA, SLU, S.A., sociedade simples).
- Dúvida sobre prazo de opção pelo Simples Nacional na abertura.
- Não usar para mudança de contrato (use `alteracao-contratual`) nem para baixa (use `encerramento-empresa-baixa`).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Documentos dos sócios (RG, CPF, comprovante de endereço) ficam só na pasta do cliente; nos exemplos usar nomes genéricos (SÓCIO A, EMPRESA EXEMPLO LTDA).

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: Sócios: quantos, qualificação, e-CPF/conta gov.br nível prata ou ouro de cada um?
Q2: Atividade(s): CNAE principal e secundários (descrever a atividade REAL)?
Q3: Capital social e participação de cada sócio? Integralização em dinheiro ou bens?
Q4: Endereço da empresa: próprio, alugado, residencial, virtual/coworking?
Q5: Tipo pretendido: MEI, empresário individual, LTDA (uma ou mais pessoas), S.A., sociedade simples?
Q6: Regime tributário pretendido (acionar `analise-tributaria-regime` se houver dúvida)?
Q7: Atividade regulamentada (CRC, CREA, CRM, OAB etc.) ou com licença sanitária/ambiental?
Q8: Algum sócio é servidor público, militar, estrangeiro ou menor de idade?
```

### 2. Tipos societários
```
Tipo                         Sócios        Responsabilidade do titular/sócio
MEI                          1             ILIMITADA: é empresário individual; o patrimônio
                                           pessoal responde (conferir o limite de receita vigente
                                           no art. 18-A, § 1º, da LC nº 123/2006)
Empresário individual        1             Ilimitada
LTDA                         1 ou mais     Limitada ao valor das quotas, mas TODOS respondem
                                           solidariamente pela integralização (art. 1.052 do CC)
SLU (LTDA de uma pessoa)     1             Igual à LTDA (art. 1.052, §§ 1º e 2º, do CC)
S.A.                         2 ou mais     Limitada ao preço de emissão das ações
                                           (art. 1º da Lei nº 6.404/1976; mínimo de 2 subscritores
                                           no art. 80, I; exceção: subsidiária integral, art. 251)
Sociedade simples            2 ou mais     Conforme o contrato: subsidiária ou não (art. 997, VIII, do CC)

EIRELI: deixou de existir. A SLU foi criada pela Lei nº 13.874/2019 (Liberdade Econômica),
que incluiu os §§ 1º e 2º no art. 1.052 do CC; a Lei nº 14.195/2021 (art. 41) transformou
as EIRELIs existentes em sociedades limitadas unipessoais.
```

### 3. Fluxo REDESIM (5 a 15 dias, conforme o município)
```
1. Consulta de viabilidade: nome empresarial e endereço × CNAE (zoneamento municipal).
   Desde a Lei nº 14.195/2021 é possível usar o próprio número do CNPJ como nome empresarial.
2. DBE (Documento Básico de Entrada) no Coletor Nacional da RFB. No mesmo pedido de inscrição
   no CNPJ, pelo módulo de enquadramento tributário acessado no Acompanhamento do Protocolo
   Redesim, a empresa já declara a opção pelo Simples Nacional e, desde 19/10/2026, escolhe
   entre Simples "puro", Simples "híbrido" (IBS/CBS por fora do DAS) ou regime regular (ver passo 6).
3. Contrato social com as cláusulas do art. 997 do CC (ver passo 5).
4. Registro: Junta Comercial (sociedade empresária) OU Cartório de Registro Civil de Pessoas
   Jurídicas (sociedade simples — ex.: algumas sociedades de profissão regulamentada).
5. CNPJ deferido pela integração REDESIM.
6. Inscrição estadual (se houver ICMS) e inscrição municipal + alvará; licenças sanitária,
   ambiental e do Corpo de Bombeiros quando a atividade exigir (atividade de baixo risco
   pode ser dispensada de alvará — conferir a classificação de risco do município).
7. Procuração eletrônica no e-CAC para o contador.
8. Opção tributária (passo 6).
9. Cadastros: e-CNPJ (A1/A3), eSocial (S-1000 se houver empregado), FGTS Digital,
   emissão de NF-e/NFC-e/NFS-e (NFS-e padrão nacional), conta bancária PJ.
10. Setup contábil: plano de contas (`plano-contas-cpc`), ERP, rotina mensal.
```
**CNPJ alfanumérico:** desde julho de 2026 a Receita Federal pode atribuir, às novas inscrições, CNPJ com letras e números nas 12 primeiras posições (Instrução Normativa RFB nº 2.229/2024). Os CNPJs numéricos continuam válidos. Conferir se o ERP, o banco e os sistemas do cliente aceitam o novo formato.

### 4. CNAE — definição crítica
O CNAE principal afeta anexo do Simples, ICMS-ST, RAT, licenças e retenções. Conferir:
- a atividade real do cliente (não a "desejada");
- a tabela CNAE vigente (IBGE/Concla);
- as atividades impeditivas e as ambíguas do Simples (art. 17 da LC nº 123/2006 e anexos da Resolução CGSN nº 140/2018);
- o RAT pelo CNAE (Anexo V do Decreto nº 3.048/1999).

### 5. Cláusulas obrigatórias (art. 997 do CC, aplicado à LTDA pelo art. 1.054 do CC)
```
I    Nome, nacionalidade, estado civil, profissão e residência dos sócios (PF) ou
     firma/denominação, nacionalidade e sede (PJ)
II   Denominação, objeto, sede e prazo da sociedade
III  Capital social, em moeda corrente, podendo abranger bens avaliáveis em dinheiro
IV   Quota de cada sócio e o modo de realizá-la (integralização)
V    Prestações de sócio que contribui com serviços (não cabe na LTDA — art. 1.055, § 2º, do CC)
VI   Administradores e seus poderes
VII  Participação de cada sócio nos lucros e nas perdas
VIII Se os sócios respondem, ou não, subsidiariamente pelas obrigações sociais
```
Na LTDA, incluir também: cláusula de administração (sócio ou não sócio), regras de cessão de quotas (art. 1.057 do CC), deliberações e quórum (arts. 1.071 a 1.076 do CC) e, se houver, regência supletiva pela Lei nº 6.404/1976 (art. 1.053, parágrafo único, do CC).

**Visto de advogado:** exigido nos atos constitutivos de pessoas jurídicas em geral (art. 1º, § 2º, da Lei nº 8.906/1994 — Estatuto da OAB), mas **dispensado para ME e EPP**: o art. 9º, § 2º, da Lei Complementar nº 123/2006 afasta expressamente o § 2º do art. 1º da Lei nº 8.906/1994 para essas empresas. **Regra de uso:** antes de montar o checklist, PERGUNTAR ao contador "A empresa será ME ou EPP e posso dispensar o visto de advogado? (sim/não)"; sem a confirmação, manter o visto no checklist. Quando o visto for exigido, encaminhar a um advogado.

### 6. Opção tributária — prazos
```
Simples Nacional — empresa EM INÍCIO DE ATIVIDADE (regra vigente desde 13/10/2025):
   o pedido de opção é feito JUNTO com a inscrição no CNPJ, pelo Portal Redesim
   (art. 16, § 3º, da LC nº 123/2006; § 5º do art. 6º da Resolução CGSN nº 140/2018,
   com a redação da Resolução CGSN nº 183/2025):
   - no pedido, declarar expressamente que a empresa não se enquadra nas vedações (art. 6º,
     § 4º); a RFB passa a relação aos Estados, ao DF e aos Municípios para verificarem a
     regularidade (art. 6º, § 6º);
   - a opção produz efeitos a partir da data de inscrição no CNPJ;
   - se indeferida por pendência impeditiva, a empresa pode regularizá-la em até 30 dias
     contados da inscrição no CNPJ.
   Atenção: a regra antiga ("30 dias do último deferimento, limitado a 60 dias da abertura")
   NÃO se aplica mais às novas inscrições. Se a opção não for marcada na inscrição, a empresa
   já constituída só opta na janela ordinária do Portal do Simples Nacional.
   CNPJ inscrito entre 01/10/2026 e 31/12/2026: a opção feita na inscrição vale desde a
   inscrição e para todo o ano-calendário de 2027; a opção pelo IBS/CBS no regime regular
   ("Simples híbrido") vale de janeiro a junho de 2027 (art. 3º da Resolução CGSN nº 186/2026,
   com a redação da Resolução CGSN nº 194/2026).
   A Resolução CGSN nº 190/2026 altera a Resolução CGSN nº 140/2018 a partir de 01/01/2027:
   para pedidos de 2027 em diante, conferir a redação vigente no Portal do Simples Nacional.
Simples Nacional — empresa JÁ EXISTENTE: regra geral, até o último dia útil de janeiro, com
   efeito a partir de 1º de janeiro (art. 16, § 2º, da LC nº 123/2006). Para 2027 a janela foi
   antecipada: de 01/09 a 15/10/2026 (Resolução CGSN nº 186/2026, com o prazo prorrogado pela
   Resolução CGSN nº 194/2026). Antes de orientar, conferir
   no Portal do Simples Nacional a janela vigente para o ano seguinte.
MEI: na própria formalização, pelo Portal do Empreendedor.
Lucro Presumido: com o pagamento da 1ª quota ou quota única do imposto do 1º período de
   apuração (art. 13, § 1º, da Lei nº 9.718/1998); DARF IRPJ trimestral código 2089.
Lucro Real: com o primeiro pagamento do período (estimativa mensal ou apuração trimestral —
   art. 3º da Lei nº 9.430/1996). Código da estimativa mensal do IRPJ: 2362 para PJ OBRIGADA
   ao Lucro Real e 5993 para PJ OPTANTE (não obrigada); apuração trimestral da PJ obrigada: 0220
   (Perguntas e Respostas IRPJ da Receita, capítulo de pagamento). Conferir no Sicalc antes
   de emitir o DARF.
```
Antes de recomendar o regime, considerar a Reforma Tributária: 2026 é ano-teste (CBS 0,9% e IBS 0,1% destacados no documento — Emenda Constitucional nº 132/2023 e Lei Complementar nº 214/2025). No Simples, avaliar a opção pelo IBS/CBS no regime regular ("Simples híbrido" — art. 41, § 3º, da LC nº 214/2025), que permite aos clientes contribuintes do IBS/CBS, quando cabível, aproveitar o crédito desses tributos; ponderar o custo de apuração separada do DAS.

### 7. Entregável obrigatório

**a) Checklist completo**
```
CLIENTE: EMPRESA EXEMPLO LTDA   Início: __/__/__   Conclusão: __/__/__

PRÉ-ABERTURA
[ ] Conta gov.br (prata/ouro) ou e-CPF de todos os sócios
[ ] Comprovante de endereço dos sócios
[ ] Atividade definida (CNAE principal + secundários)
[ ] Capital social e forma de integralização acordados
[ ] Tipo societário: __
[ ] Endereço da empresa (próprio/alugado/virtual) e permissão de uso
[ ] Impedimentos: servidor público (não pode ser administrador — art. 117, X, da Lei nº 8.112/1990,
    no caso federal), militar da ativa, menor, estrangeiro
[ ] CPF dos sócios regular (CPF suspenso ou pendente bloqueia o DBE)

REDESIM
[ ] Viabilidade de nome — protocolo: __
[ ] Viabilidade de endereço × CNAE — protocolo: __
[ ] DBE — protocolo: __

CONTRATO SOCIAL
[ ] Minuta com as cláusulas do art. 997 do CC
[ ] Visto de advogado (se não for ME/EPP) — PERGUNTAR ao contador se a empresa é ME/EPP e se o visto pode ser dispensado; sem confirmação, manter o visto
[ ] Assinaturas digitais coletadas
[ ] Protocolo na Junta Comercial / Cartório em __/__/__
[ ] NIRE / registro: __

INSCRIÇÕES E LICENÇAS
[ ] CNPJ nº __ em __/__/__ (numérico ou alfanumérico — conferir sistemas)
[ ] Inscrição estadual nº __ (se aplicável)
[ ] Inscrição municipal nº __
[ ] Alvará de funcionamento (ou dispensa por baixo risco)
[ ] Licença sanitária / ambiental / Bombeiros (se aplicável)
[ ] Registro no conselho profissional (se atividade regulamentada)

OPÇÃO TRIBUTÁRIA
[ ] Simples Nacional: opção marcada NO PEDIDO DE INSCRIÇÃO do CNPJ (puro ou híbrido) — data __/__/__
[ ] Se indeferida por pendência: regularizar até __/__/__ (30 dias da inscrição no CNPJ)
[ ] Presumido/Real: 1º pagamento em __/__/__

CONTÁBIL E DIGITAL
[ ] e-CNPJ emitido (validade __/__/__)
[ ] Procuração eletrônica e-CAC para o contador
[ ] eSocial S-1000 e FGTS Digital (se houver empregados ou pró-labore)
[ ] Plano de contas implantado (`plano-contas-cpc`)
[ ] ERP configurado
[ ] Conta bancária PJ aberta

NOTAS FISCAIS
[ ] Credenciamento NF-e/NFC-e na SEFAZ (comércio/indústria)
[ ] NFS-e padrão nacional (serviços)
[ ] Destaque de CBS/IBS no documento fiscal (ano-teste 2026)
```

**b) Minuta de contrato social** — roteiro das cláusulas do passo 5. Contrato com acordo de investimento, S.A. ou cláusulas sofisticadas: encaminhar a advogado parceiro.

**c) Cronograma de 5 a 15 dias**, com data por etapa.

**d) Plano de contas inicial** (`plano-contas-cpc`).

**e) Encaminhamento para o setup contábil** (honorários, primeira folha/pró-labore, primeiras notas).

## Erros comuns / pontos de atenção
- CNAE principal diferente da atividade real.
- Não marcar a opção pelo Simples no pedido de inscrição do CNPJ: depois de emitido o CNPJ, a empresa é "já constituída" e só poderá optar na janela ordinária do ano seguinte.
- Usar a regra antiga de "30 dias do último deferimento / 60 dias da abertura" para inscrição nova.
- Deixar passar os 30 dias da inscrição sem regularizar a pendência que indeferiu a opção.
- Tratar MEI como responsabilidade limitada: o MEI é empresário individual e responde com o patrimônio pessoal.
- Endereço residencial ou virtual em município que não permite a atividade: alvará negado.
- Capital social irrisório para a operação real (dificulta crédito e pode sinalizar subcapitalização).
- Atividade regulamentada sem registro no conselho antes de operar.
- Sócio menor de idade: pode ser sócio de LTDA sem autorização judicial se o capital estiver totalmente integralizado, sem poderes de administração e devidamente representado ou assistido (art. 974, § 3º, do CC).
- Sócio estrangeiro: CPF brasileiro e, se residente no exterior, procurador no Brasil (normas do DREI).
- Holding patrimonial: não precisa ser sociedade simples; o mais comum é LTDA. Avaliar caso a caso (tributação, ITBI, ITCMD).
- Startup: pode começar como LTDA/SLU e depois transformar em S.A. (Lei Complementar nº 182/2021 — Marco Legal das Startups).

## Perguntas que o usuário costuma fazer
- **"Abri o CNPJ e não marquei o Simples. Ainda posso entrar este ano?"** Não pela via do início de atividade: a opção do início de atividade é feita junto com a inscrição no CNPJ. Se a opção foi pedida e indeferida por pendência, há 30 dias da inscrição para regularizar. Fora disso, só na janela ordinária de opção (conferir no Portal do Simples Nacional).
- **"MEI protege meu patrimônio?"** Não. O MEI é empresário individual; para separar patrimônio, o caminho é LTDA/SLU.
- **"Preciso de advogado para assinar o contrato?"** Para ME e EPP, não. Para as demais, sim (visto de advogado).

## Quando escalar
- Escolha de regime → `analise-tributaria-regime`
- Plano de contas → `plano-contas-cpc`
- Alteração posterior → `alteracao-contratual`
- Encerramento → `encerramento-empresa-baixa`
- Contrato social complexo (investidor, S.A., acordo de sócios) → advogado parceiro com OAB

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei nº 10.406/2002 (Código Civil) — arts. 966 e 974 (empresário e incapaz), 997 (cláusulas do contrato), 1.052 a 1.057 (LTDA, SLU, quotas), 1.071 a 1.076 (deliberações).
- Lei nº 13.874/2019 (Liberdade Econômica) — criação da sociedade limitada unipessoal.
- Lei nº 14.195/2021 (Ambiente de Negócios) — art. 41 (EIRELI transformada em LTDA); simplificação do registro e do nome empresarial.
- Lei nº 11.598/2007 — REDESIM.
- Lei nº 6.404/1976 — art. 1º (responsabilidade do acionista), art. 80 (requisitos de constituição), art. 251 (subsidiária integral).
- Boletim informativo da Receita Federal sobre o MAT v2.0 (outubro de 2026) — opção de regime no pedido de inscrição do CNPJ.
- Lei Complementar nº 123/2006 — art. 9º, § 2º (dispensa do visto de advogado para ME/EPP); art. 16, §§ 2º e 3º (opção pelo Simples); art. 17 (vedações); art. 18-A (MEI).
- Resolução CGSN nº 140/2018 — art. 2º, IV (empresa em início de atividade), art. 6º, §§ 4º a 6º (opção no início de atividade, com a redação da Resolução CGSN nº 183/2025) e atividades impeditivas; alterações a partir de 01/01/2027 pela Resolução CGSN nº 190/2026.
- Resolução CGSN nº 186/2026 (com a redação da Resolução CGSN nº 194/2026) — opção pelo IBS/CBS no regime regular e regras de 2027 para empresas inscritas de 01/10 a 31/12/2026.
- Lei Complementar nº 214/2025 — art. 41, § 3º (optante do Simples apurando IBS/CBS pelo regime regular).
- Lei nº 9.718/1998 — art. 13, § 1º (opção pelo Lucro Presumido).
- Lei nº 9.430/1996 — art. 3º (opção pela estimativa/Lucro Real).
- Lei nº 8.906/1994 (Estatuto da OAB) — art. 1º, § 2º (visto de advogado).
- Lei nº 8.112/1990 — art. 117, X (servidor federal como administrador).
- Lei Complementar nº 182/2021 — Marco Legal das Startups.
- Instrução Normativa RFB nº 2.229/2024 — CNPJ alfanumérico.
- Decreto nº 3.048/1999 — Anexo V (RAT por CNAE).
- Emenda Constitucional nº 132/2023 e Lei Complementar nº 214/2025 — Reforma Tributária (ano-teste 2026).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
