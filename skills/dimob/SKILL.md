---
name: dimob
description: "Prepara e confere a DIMOB (Declaração de Informações sobre Atividades Imobiliárias) anual de construtoras, incorporadoras, loteadoras, imobiliárias e administradoras de imóveis — vendas, locações, sublocações e intermediações. Continua exigida em 2026 (IN RFB nº 1.115/2010), com entrega até o último dia útil de fevereiro do ano seguinte; multa pelo art. 57 da MP nº 2.158-35/2001. Acionar quando o usuário disser \"fazer a DIMOB\", \"cliente imobiliária\", \"aluguéis administrados\", \"vendas de unidades\", \"intermediação de imóvel\", \"PGD DIMOB\", \"multa DIMOB\". Entrega tabela de operações por tipo, roteiro de importação no PGD, checklist de conferência e lista de pendências de cadastro (CPF/CNPJ e endereços)."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# DIMOB anual

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Levanta e confere as operações imobiliárias do ano (venda de unidades construídas, loteadas ou incorporadas, locação e sublocação administradas, intermediação) e prepara os dados para o programa gerador da DIMOB. Confere CPF/CNPJ das partes, valores contratados, valores pagos no ano, comissões e endereços dos imóveis.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Situação em 2026.** A DIMOB continua obrigatória. A DIMOB do ano-calendário 2025 venceu em
> 27/02/2026; a do ano-calendário 2026 vence no **último dia útil de fevereiro de 2027**.
> Não confundir com a extinção da DIRF: a IN RFB nº 2.181/2024 tratou da DIRF, não da DIMOB.

## Quando usar
- Cliente construtora, incorporadora, loteadora, imobiliária ou administradora de imóveis.
- Empresa constituída para construir, administrar, locar ou vender patrimônio próprio, de condôminos ou de sócios.
- Pessoa física equiparada a PJ por incorporação ou loteamento.
- Retificação de DIMOB anterior.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). A DIMOB envolve CPF de compradores, locadores e locatários: trabalhar com a planilha do cliente, sem copiar os dados para a conversa.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Quem entrega e o que entra
```
OBRIGADOS (IN RFB nº 1.115/2010, art. 1º)
- PJ e equiparadas que comercializem imóveis que construírem, lotearem ou incorporarem
- que intermediem aquisição, alienação ou aluguel de imóveis
- que realizem sublocação
- constituídas para construção, administração, locação ou alienação de patrimônio
  próprio, de condôminos ou de sócios
- quem comercializa imóveis que construiu, loteou ou incorporou informa TODOS os imóveis
  comercializados, ainda que a venda tenha sido intermediada por terceiro (art. 1º, § 1º);
  a informação da imobiliária não dispensa a construtora/incorporadora

DISPENSADOS (art. 1º, § 3º)
- PJ e equiparadas que não tiveram operação imobiliária no ano-calendário

O QUE ENTRA (art. 2º)
- operações de construção, incorporação, loteamento e intermediação de aquisição e
  alienação, NO ANO EM QUE FORAM CONTRATADAS (inciso I)
- pagamentos feitos no ano, mês a mês, de locação, sublocação e intermediação de locação,
  qualquer que seja o ano do contrato (inciso II)
- casos particulares (parceria, cessão de direitos, permuta, distrato): seguir as
  instruções de preenchimento do PGD DIMOB do ano

PRAZO: último dia útil de fevereiro do ano seguinte (art. 3º), pela matriz, reunindo
todos os estabelecimentos; assinatura com certificado digital, exceto optante do
Simples Nacional (art. 3º, § 1º)
SITUAÇÃO ESPECIAL (extinção, fusão, incorporação, cisão total): último dia útil do
mês seguinte ao do evento (art. 1º, § 2º)
```
Artigos da IN RFB nº 1.115/2010. Registros e campos do arquivo: seguir o leiaute e as instruções do PGD DIMOB do ano-calendário declarado.

### 2. Entrevista mínima
```
Q1: "Ano-calendário + CNPJ + tipo (construtora/incorporadora, imobiliária, administradora)?"
Q2: "Quantas vendas, contratos de locação e intermediações no ano?"
Q3: "O sistema imobiliário exporta planilha das operações (contrato, partes, valores)?"
Q4: "Houve IR retido sobre aluguel pago a PF (locatário PJ)?"
Q5: "Os endereços dos imóveis estão completos (CEP, número, complemento)?"
```

### 3. Validação técnica
- CPF/CNPJ de todas as partes válidos (não domiciliado sem CPF: seguir a orientação do PGD).
- Percentual de participação de cada comprador/vendedor quando houver mais de um.
- Valor da operação (contratado) e demais valores exigidos pelos campos do PGD.
- Comissão: valor total auferido na operação.
- Locação: meses de vigência do contrato no ano (início/fim).
- Endereços completos.

### 4. Entregável obrigatório

**a) Tabela consolidada por tipo**
```
DIMOB — ANO __ — CNPJ __ (EMPRESA EXEMPLO)

VENDAS              N operações | Valor contratado R$ __ | Pago no ano R$ __
LOCAÇÕES            M contratos | Aluguéis no ano R$ __  | Comissões R$ __ | IR retido R$ __
INTERMEDIAÇÕES      P operações | Valor R$ __            | Comissões R$ __
ESPECIAIS           cessões / permutas / distratos: Q
```

**b) Arquivo para o PGD DIMOB** (importação a partir do sistema do cliente, ajustada ao leiaute vigente).

**c) Checklist**
```
[ ] Vendas do ano conferidas com contratos
[ ] Locações administradas informadas (todos os meses de vigência)
[ ] Intermediações informadas, mesmo sem comissão
[ ] CPF/CNPJ válidos
[ ] Endereços completos
[ ] PGD sem erros
[ ] Transmitida até o último dia útil de fevereiro
[ ] Recibo arquivado
```

## Erros comuns / pontos de atenção
- Administradora deixar de informar aluguéis que administra em nome do proprietário.
- CPF trocado entre comprador e vendedor ou entre locador e locatário.
- Imóvel financiado: informar o valor da operação e o valor pago no ano conforme as regras do PGD.
- Locação de curta temporada (plataformas): antes de informar, avaliar no contrato se a operação é locação ou hospedagem; só a locação, a sublocação e a intermediação de locação entram no inciso II do art. 2º da IN RFB nº 1.115/2010.
- **Multa** (art. 57 da MP nº 2.158-35/2001; art. 4º da IN RFB nº 1.115/2010, com redação da IN RFB nº 2.218/2024):
  - atraso, por mês-calendário ou fração: R$ 500,00 para PJ em início de atividade, imune, isenta ou que apurou Lucro Presumido ou Simples Nacional na última declaração; R$ 1.500,00 para as demais PJ; R$ 100,00 para PF;
  - não atender intimação da RFB: R$ 500,00 por mês-calendário;
  - informação omitida, inexata ou incompleta: 3% do valor das operações, não inferior a R$ 100,00 (PJ); 1,5%, não inferior a R$ 50,00 (PF);
  - a multa por atraso cai à metade se a declaração for entregue antes de procedimento de ofício (§ 3º do art. 57);
  - optante do Simples Nacional: redução de 70% só nas multas por intimação e por informação incorreta (§ 1º do art. 57), não na multa por atraso.
  A DIMOB não segue a regra de "2% ao mês" de outras declarações.

### Casos de borda
- **Venda na planta com parcelas em vários anos**: a venda é informada na DIMOB do ano em que foi contratada (art. 2º, I, da IN RFB nº 1.115/2010), com os valores pedidos nos campos do PGD daquele ano. Parcelas recebidas nos anos seguintes não geram nova informação de venda (a regra de "todo ano" vale só para locação, sublocação e intermediação de locação — art. 2º, II).
- **Distrato**: informar como devolução/cancelamento conforme o PGD.
- **Permuta**: informar como operação especial; tributação da permuta segue regra própria do IRPJ.
- **Aluguel pago a PF por locatário PJ**: o IRRF (código 3208) é retido pelo locatário PJ e, desde 2025, informado por ele na EFD-Reinf (R-4010). A administradora informa o rendimento e o IR retido na DIMOB quando tiver o dado.

### Quando encaminhar para outra skill
- Locador PF na malha → `diagnosticar-malha-fina-pf`
- Ganho de capital na venda por PF → `irpf-ganho-capital`
- Aluguel recebido por PF (carnê-leão) → `irpf-aluguel-carne-leao`
- Retenção no pagamento de aluguel → `efd-reinf`

### Autoavaliação
- [ ] Vendas, locações e intermediações separadas?
- [ ] CPF/CNPJ validados?
- [ ] Endereços completos?
- [ ] PGD sem erros?
- [ ] Transmitida no prazo?

## Perguntas que o usuário costuma fazer
- **"A DIMOB acabou junto com a DIRF?"** Não. Continua obrigatória em 2026.
- **"A imobiliária já informou. A construtora também precisa?"** Sim, a informação da imobiliária não dispensa a construtora/incorporadora.
- **"Empresa sem operação no ano entrega DIMOB?"** Não; está dispensada.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): documento DOCX.
- Este padrão prevalece sobre outros formatos citados acima, exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- IN RFB nº 1.115/2010 — DIMOB: art. 1º (obrigados, dispensa, situação especial), art. 2º (o que informar), art. 3º (prazo e assinatura), art. 4º (multas).
- IN RFB nº 2.218/2024 — nova redação do art. 4º da IN RFB nº 1.115/2010 (multas).
- MP nº 2.158-35/2001, art. 57 — multas por atraso, intimação, omissão ou inexatidão.
- Decreto-Lei nº 1.381/1974 e Decreto-Lei nº 1.510/1976 — equiparação da PF a PJ (incorporação e loteamento).
- Decreto nº 9.580/2018 (RIR/2018) — IRRF e ganho de capital.
- Página "Declarar atividades imobiliárias (DIMOB)" (gov.br) e instruções do PGD DIMOB.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
