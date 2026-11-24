---
name: analisar-folha-pagamento
description: "Lê PDFs de folha de pagamento e pró-labore, confere retenções (INSS, IRRF, vale-transporte), encargos (INSS patronal, RAT, Terceiros, FGTS), lançamentos contábeis esperados e provisões mensais de férias e 13º, e entrega diagnóstico por colaborador. Use sempre que o usuário enviar folha de pagamento, holerite, contracheque, recibo de pró-labore, ou mencionar \"folha\", \"pró-labore\", \"INSS\", \"FGTS\", \"IRRF\", \"férias\", \"13º salário\", \"provisão de férias\", \"encargos sociais\", \"departamento pessoal\" ou \"DP\". Acione também para revisão de encargos, retenção de sócio, vale-transporte ou conferência de holerites, mesmo sem citar a norma (NBC TG 33, CLT, Lei 8.212/1991, LC 123/2006)."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Analisar Folha de Pagamento e Pró-labore

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Lê a folha de pagamento e os recibos de pró-labore já calculados, confere se INSS, IRRF, FGTS, vale-transporte e encargos patronais batem com as regras de 2026 e indica os lançamentos contábeis e as provisões esperadas. Não refaz a folha: aponta o que está certo, o que tem ressalva e o que está errado, colaborador por colaborador.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Conferência mensal da folha e do pró-labore antes de contabilizar ou fechar o mês.
- Revisão de encargos sociais (INSS patronal, RAT, Terceiros, FGTS) e de retenções.
- Conferência das provisões mensais de férias e 13º e seus encargos.
- Para CALCULAR a folha, use `folha-pagamento-mensal`; para férias e 13º, `ferias-13-salario`.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). No relatório, identificar o colaborador por matrícula ou iniciais.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Perguntas iniciais
1. Qual empresa, competência e regime tributário (Simples — qual anexo —, Lucro Presumido ou Real)?
2. A empresa está na desoneração da folha (CPRB) em transição pela Lei nº 14.973/2024?
3. Qual o RAT/FAP e o percentual de Terceiros do FPAS da empresa?
4. Há aprendizes, domésticos, afastados ou rescisões no mês?

### 2. Eventos cobertos
Folha de salários; pró-labore de sócios; férias (pagamento e provisão); 13º salário (pagamento e provisão).

### 3. Validações obrigatórias (parâmetros 2026)
- **INSS do empregado** — progressivo por faixas (Portaria Interministerial MPS/MF nº 13/2026): até 1.621,00 = 7,5%; até 2.902,84 = 9%; até 4.354,27 = 12%; até 8.475,55 = 14%. Teto 8.475,55; desconto máximo R$ 988,09. Atalho: salário × alíquota da faixa − parcela a deduzir (0 / 24,32 / 111,40 / 198,49).
- **INSS do sócio (pró-labore)** — 11% retido pela empresa, limitado ao teto (desconto máximo 11% × 8.475,55 = R$ 932,31), conforme art. 4º da Lei nº 10.666/2003 e art. 30, § 4º, da Lei nº 8.212/1991. Pró-labore não tem FGTS.
- **INSS patronal** — 20% sobre a folha de empregados (art. 22, I, da Lei nº 8.212/1991) + RAT ajustado pelo FAP (art. 22, II) + Terceiros conforme FPAS. Sobre pró-labore e autônomos: 20% (art. 22, III), sem RAT e sem Terceiros.
  - **Simples Nacional:** a contribuição patronal (CPP) já está no DAS, exceto no Anexo IV, que recolhe a CPP à parte (art. 13, VI, e art. 18, § 5º-C, da LC nº 123/2006).
  - **Desoneração em transição (Lei nº 14.973/2024):** em 2026, CPRB com 60% da alíquota + 10% sobre a folha; a parcela sobre a folha não incide sobre o 13º.
- **FGTS** — 8% da remuneração (art. 15 da Lei nº 8.036/1990); aprendiz 2% (art. 15, § 7º). Na dispensa sem justa causa há multa de 40% sobre o saldo para fins rescisórios (art. 18, § 1º), recolhida na guia rescisória do FGTS Digital. A contribuição adicional de 10% da LC nº 110/2001 foi extinta a partir de 01/01/2020 (Lei nº 13.932/2019). Vencimento: dia 20 do mês seguinte.
- **IRRF** — base = rendimento tributável − INSS − R$ 189,59 por dependente − pensão judicial, OU rendimento − desconto simplificado de R$ 607,20 (usar o que der menor imposto). Aplicar a tabela mensal e, depois, o **redutor da Lei nº 15.270/2025** calculado sobre o rendimento bruto: até 5.000,00 zera; de 5.000,01 a 7.350,00 reduz 978,62 − 0,133145 × rendimento; acima de 7.350,00 não reduz. Detalhe em `calculo-irrf-folha`.
- **Vale-transporte** — desconto de até 6% do salário-base, limitado ao custo real do transporte (Lei nº 7.418/1985). Nunca sobre HE ou adicionais.

### 4. Lançamentos contábeis esperados

**Folha de salários**
| Evento | Débito | Crédito |
|---|---|---|
| Salário bruto | Salários e Ordenados (Despesa/Custo) | Salários a Pagar |
| INSS patronal + RAT + Terceiros | INSS Patronal (Despesa/Custo) | INSS a Recolher |
| FGTS | FGTS (Despesa/Custo) | FGTS a Recolher |
| INSS do empregado retido | Salários a Pagar | INSS a Recolher |
| IRRF retido | Salários a Pagar | IRRF a Recolher |
| Pagamento líquido | Salários a Pagar | Banco/Caixa |

**Pró-labore**
| Evento | Débito | Crédito |
|---|---|---|
| Pró-labore bruto | Pró-labore (Despesa) | Pró-labore a Pagar |
| INSS patronal 20% (fora do Simples, ou Simples Anexo IV) | INSS sobre Pró-labore (Despesa) | INSS a Recolher |
| INSS do sócio retido (11%) | Pró-labore a Pagar | INSS a Recolher |
| IRRF retido | Pró-labore a Pagar | IRRF a Recolher |
| Pagamento líquido | Pró-labore a Pagar | Banco/Caixa |

**Férias e 13º — apropriação mensal (NBC TG 33 (R2) — Benefícios a Empregados, benefícios de curto prazo)**
O benefício é reconhecido no mês em que o empregado o adquire, não só no pagamento:
- D: Despesa com Férias / 13º — C: Férias a Pagar / 13º a Pagar (passivo)
- Encargos (INSS patronal + RAT + Terceiros + FGTS) apropriados no mesmo mês.
- Referência de cálculo: férias = 1/12 da remuneração + 1/3 por mês; 13º = 1/12 por mês.
- No pagamento, baixar a apropriação (não lançar de novo como despesa).

### 5. Formato de saída
Para cada colaborador ou sócio (por matrícula/iniciais): eventos do mês, lançamentos esperados (D/C/valor), retenções conferidas (valor da folha × valor recalculado), provisões esperadas e status (Aprovado / Com ressalvas / Reprovado) com justificativa. No fim, resumo com totais por evento e os principais alertas.

## Erros comuns / pontos de atenção
- INSS do empregado com alíquota única sobre o total (o correto é progressivo por faixa).
- IRRF sem comparar desconto simplificado × deduções legais, ou sem o redutor da Lei nº 15.270/2025.
- Tratar o FGTS da rescisão como "10%": o depósito é 8% e a multa é 40% (ou 20% no acordo do art. 484-A da CLT).
- Esquecer RAT/FAP e Terceiros no patronal, ou cobrar CPP fora do DAS de empresa do Simples que não é do Anexo IV.
- FGTS sobre pró-labore (não existe).
- Provisão de férias/13º só no mês do pagamento.
- Se a tabela de INSS/IRRF do arquivo não for a de 2026, sinalizar e pedir confirmação. Nunca omitir colaborador: todos aparecem no relatório.

## Perguntas que o usuário costuma fazer
- **"O sócio do Simples paga INSS patronal sobre o pró-labore?"** Só se a empresa for do Anexo IV; nos demais anexos a CPP está no DAS. Os 11% do sócio são retidos em qualquer caso.
- **"O desconto de VT pode ser 6% cheio?"** Só se o custo real do transporte for igual ou maior que 6% do salário-base.

## Base legal usada nesta skill
- NBC TG 33 (R2) — Benefícios a Empregados (benefícios de curto prazo: férias e 13º).
- Lei nº 8.212/1991 — art. 22, I a III (contribuição patronal e RAT); art. 28 (salário de contribuição); art. 30, § 4º (dedução que resulta nos 11% do contribuinte individual).
- Lei nº 10.666/2003 — art. 4º (retenção da contribuição do contribuinte individual pela empresa).
- Portaria Interministerial MPS/MF nº 13/2026 — tabela do INSS 2026.
- Lei nº 8.036/1990 — art. 15 (depósito de 8%; § 7º aprendiz 2%) e art. 18, § 1º (multa de 40%).
- Lei nº 13.932/2019 — extinção da contribuição de 10% da LC nº 110/2001 a partir de 2020.
- Lei nº 15.270/2025 — redutor do IRRF a partir de 2026.
- LC nº 123/2006 — art. 13, VI, e art. 18, § 5º-C (CPP do Anexo IV fora do DAS).
- Lei nº 14.973/2024 — transição da desoneração da folha.
- Lei nº 7.418/1985 — vale-transporte.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
