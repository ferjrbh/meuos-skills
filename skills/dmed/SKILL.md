---
name: dmed
description: "Prepara e confere a DMED (Declaração de Serviços Médicos e de Saúde) anual de PJ prestadoras de serviços de saúde (hospitais, clínicas, laboratórios, médicos e dentistas em PJ) e de operadoras de planos privados de assistência à saúde. A DMED é o espelho da dedução de saúde no IRPF do paciente: divergência gera malha. Continua exigida em 2026 (IN RFB nº 2.074/2022); entrega até o último dia útil de fevereiro do ano seguinte. Acionar quando o usuário disser \"fazer a DMED\", \"cliente clínica\", \"hospital\", \"operadora de plano\", \"paciente caiu na malha por despesa médica\", \"recibo médico sem CPF\", \"PGD DMED\". Entrega lista consolidada por responsável pelo pagamento e beneficiário, roteiro do PGD, checklist e alerta ao cliente sobre CPF nos recibos."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# DMED anual

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Levanta os valores recebidos de pessoas físicas por prestador de serviço de saúde (ou, no caso de operadora, os valores pagos pelos titulares e dependentes e os reembolsos) e prepara os dados para o programa gerador da DMED. Confere CPF do responsável pelo pagamento e do beneficiário, porque é por esse cruzamento que a Receita confere a dedução de saúde no IRPF.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Situação em 2026.** A DMED continua obrigatória e é regulada pela **IN RFB nº 2.074/2022**, em vigor
> desde 01/04/2022 (ela revogou a IN RFB nº 985/2009). A DMED 2026 (ano-calendário 2025) foi entregue
> de 02/01 a 27/02/2026, pelo PGD DMED 2026 (ADE Cofis nº 27/2025). A do ano-calendário 2026 vence no
> **último dia útil de fevereiro de 2027**.

## Quando usar
- Cliente PJ (ou PF equiparada a PJ) que presta serviços médicos e de saúde.
- Cliente operadora de plano privado de assistência à saúde.
- Paciente do cliente que caiu na malha por despesa médica.
- Retificação de DMED anterior.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- **Dado de saúde é dado pessoal sensível** (art. 5º, II, da Lei nº 13.709/2018 (LGPD)). Usar só o necessário (art. 6º, III, da LGPD — necessidade): trabalhar com a planilha do cliente, sem copiar nomes, CPFs ou procedimentos para a resposta. Exemplos sempre com dados fictícios.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Quem entrega e o que informa
```
OBRIGADOS (art. 2º)
- PJ ou equiparada prestadora de serviços de saúde
- operadora de plano privado de assistência à saúde autorizada pela ANS
- demais entidades que mantenham programa de assistência à saúde ou operem contrato de
  prestação continuada ou cobertura de custos assistenciais, ainda que fora da ANS

SERVIÇOS DE SAÚDE (art. 1º, parágrafo único): psicólogos, fisioterapeutas, terapeutas
ocupacionais, fonoaudiólogos, dentistas, hospitais, laboratórios, clínicas médicas de
qualquer especialidade, estabelecimento geriátrico classificado como hospital pelo
Ministério da Saúde, entidades de ensino para instrução de deficiente físico ou mental,
serviços radiológicos e de próteses ortopédicas ou dentárias

PRESTADOR informa (art. 4º, I): CPF e nome do responsável pelo pagamento e do
beneficiário do serviço; valores recebidos de PESSOAS FÍSICAS, por responsável pelo
pagamento. Não informa o que foi pago por operadora ou outra PJ.

OPERADORA informa (art. 4º, II): CPF e nome do titular e dos dependentes; valores
recebidos de PF por titular e dependente; reembolsos à PF por beneficiário e por
prestador. Beneficiário sem CPF: informar a data de nascimento (§ 2º). Plano coletivo
empresarial: dispensa de informar os beneficiários enquanto durar o vínculo de emprego
(§ 3º), com as regras próprias dos §§ 4º e 5º para plano coletivo por adesão com
participação da empresa.

DISPENSADOS (art. 3º): PJ inativa; PJ ativa que não prestou serviço de saúde; PJ que
prestou serviço de saúde só mediante pagamento de outra PJ.
NÃO ENTREGA: profissional de saúde pessoa física (não equiparada a PJ).

PRAZO (art. 5º): último dia útil de fevereiro do ano seguinte, até 23h59min59s
(horário de Brasília), pela matriz, com certificado digital (exceto optante do
Simples Nacional)
```
Artigos da IN RFB nº 2.074/2022.

### 2. Entrevista mínima
```
Q1: "Ano-calendário + CNPJ. O cliente é prestador ou operadora?"
Q2 (prestador): "O sistema exporta os recebimentos de PF do ano com CPF de quem pagou e do paciente?"
Q3 (prestador): "Os atendimentos pagos por plano estão separados? (ficam fora)"
Q4 (operadora): "Há relatório de mensalidades por titular/dependente e de reembolsos?"
Q5: "Os recibos trazem o CPF de quem pagou e do paciente?"
```

### 3. Prestador
- Somente valores pagos diretamente por PF (particular).
- Separar responsável pelo pagamento e beneficiário (ex.: mãe paga o tratamento do filho).
- Excluir atendimentos pagos por operadora.

### 4. Operadora
- Valores pagos por titular e por dependente.
- Reembolsos por beneficiário.

### 5. Orientação ao prestador sobre recibos
Para o paciente deduzir no IRPF, o comprovante deve indicar nome, endereço e CPF ou CNPJ de quem recebeu (art. 8º, § 2º, III, da Lei nº 9.250/1995). Na prática, para a DMED e o IRPF baterem, o recibo deve trazer também o CPF de quem pagou e do paciente, o valor, a data, a descrição do serviço e o registro profissional (CRM, CRO etc.).
Profissional de saúde **pessoa física** (médico, dentista, psicólogo, fisioterapeuta, fonoaudiólogo e terapeuta ocupacional) emite o recibo pelo **Receita Saúde**, obrigatório desde 01/01/2025 em substituição ao recibo em papel (Receita Federal, gov.br). O Receita Saúde não se aplica à PJ prestadora, que continua informando pela DMED.

### 6. Entregável obrigatório

**a) Lista consolidada**
```
DMED — ANO __ — CNPJ __ (CLÍNICA EXEMPLO) — Prestador/Operadora

Responsável pelo pagamento   CPF               Beneficiário   CPF               Valor anual
PACIENTE EXEMPLO 1           000.000.000-00    (o mesmo)                        R$ 4.500,00
RESPONSÁVEL EXEMPLO 2        111.111.111-11    DEPENDENTE 2   222.222.222-22    R$ 1.200,00
Total: R$ __
```

**b) Arquivo para o PGD DMED** (importação do sistema do cliente ajustada).

**c) Recibo de entrega** arquivado.

**d) Alerta ao cliente**, se houver recebimentos sem CPF: "Sem o CPF de quem pagou e do paciente, a DMED fica incompleta e o paciente pode cair na malha. Recomendamos exigir CPF em todo recibo."

**e) Checklist**
```
[ ] Recebimentos de PF do ano levantados
[ ] Atendimentos por plano excluídos (prestador)
[ ] Responsável e beneficiário separados, com CPF válido
[ ] Operadora: mensalidades por titular/dependente + reembolsos
[ ] PGD sem erros
[ ] Transmitida até o último dia útil de fevereiro
[ ] Recibo arquivado
[ ] Amostra de recibos com CPF conferida
```

## Erros comuns / pontos de atenção
- Prestador informar atendimento pago pelo plano (deve ir só na DMED da operadora).
- Trocar CPF do responsável pelo do beneficiário: o IRPF de quem pagou não bate.
- Operadora esquecer reembolsos.
- **Multa** (art. 6º da IN RFB nº 2.074/2022, que remete ao art. 57 da MP nº 2.158-35/2001):
  - atraso, por mês-calendário ou fração: R$ 500,00 para PJ em início de atividade, imune, isenta ou que apurou Lucro Presumido ou Simples Nacional na última declaração; R$ 1.500,00 para as demais PJ;
  - não atender intimação da RFB: R$ 500,00 por mês-calendário;
  - informação omitida, inexata ou incompleta: 3% do valor das operações, não inferior a R$ 100,00;
  - multa por atraso cai à metade se a entrega ocorrer antes de procedimento de ofício; para o Simples Nacional, redução de 70% nas multas por intimação e por informação incorreta.
  A DMED não segue a regra de "2% ao mês" de outras declarações. Informação falsa pode configurar crime contra a ordem tributária (art. 2º da Lei nº 8.137/1990), conforme o parágrafo único do art. 6º da IN RFB nº 2.074/2022.

### Casos de borda
- **Clínica que atende particular e plano**: na DMED dela, só os particulares; os do plano são informados pela operadora.
- **Cooperativa médica**: a cooperativa entrega a DMED dela; o cooperado PF não entrega DMED (se tiver PJ própria que atenda particular, a PJ entrega).
- **Serviço estético em estabelecimento de saúde**: entra na DMED só o serviço prestado por quem está na lista do parágrafo único do art. 1º da IN RFB nº 2.074/2022 (ex.: clínica médica, dentista). Serviço que não seja de saúde (ex.: estética feita por salão ou spa) não entra. Na dúvida sobre um procedimento específico, conferir o contrato social/CNAE do prestador e a natureza do serviço no recibo.

### Quando encaminhar para outra skill
- Paciente na malha → `diagnosticar-malha-fina-pf`
- IRPF do paciente → `elaborar-irpf-completa`
- Checar dados sensíveis antes de usar planilha com IA: retirar o que a tarefa não precisa (art. 6º, III, da LGPD)

### Autoavaliação
- [ ] Recebimentos de PF levantados?
- [ ] CPFs validados (responsável e beneficiário)?
- [ ] Atendimentos por plano excluídos (prestador)?
- [ ] Reembolsos incluídos (operadora)?
- [ ] PGD sem erros?
- [ ] Transmitida até o último dia útil de fevereiro?
- [ ] Alerta sobre CPF nos recibos enviado?

## Perguntas que o usuário costuma fazer
- **"Médico autônomo, sem CNPJ, entrega DMED?"** Não. Ele emite recibo pelo Receita Saúde.
- **"A DMED acabou como a DIRF?"** Não. Continua obrigatória em 2026.
- **"Quem pagou foi a empresa do paciente. Entra na DMED?"** Entra o que foi pago por pessoa física; pagamento por PJ não é informado como pagamento de PF.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): documento DOCX.
- Este padrão prevalece sobre outros formatos citados acima, exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- IN RFB nº 2.074/2022 — DMED: art. 1º (serviços de saúde), art. 2º (obrigados), art. 3º (dispensados), art. 4º (o que informar), art. 5º (prazo), art. 6º (multas); revogou a IN RFB nº 985/2009 (art. 7º).
- MP nº 2.158-35/2001, art. 57 — multas.
- ADE Cofis nº 27/2025 — PGD DMED 2026.
- Lei nº 9.250/1995, art. 8º, II, "a", e § 2º — dedução de despesas médicas no IRPF e requisitos do comprovante.
- Decreto nº 9.580/2018 (RIR/2018), art. 73 — dedução de despesas médicas.
- Lei nº 13.709/2018 (LGPD), art. 5º, II, e art. 6º, III — dado sensível e necessidade.
- Página "Declarar serviços médicos e da saúde (DMED)" (gov.br) e notícia "Programa Gerador da Dmed 2026 disponível para download" (gov.br/receitafederal, dez/2025).
- Notícias da Receita Federal sobre o Receita Saúde (gov.br/receitafederal, dez/2024 e fev/2026).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
