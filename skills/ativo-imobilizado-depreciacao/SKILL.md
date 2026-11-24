---
name: ativo-imobilizado-depreciacao
description: "Cuida do ativo imobilizado (CPC 27) do cadastro à baixa — custo de aquisição (preço + frete + montagem + tributos não recuperáveis), depreciação (linear, soma dos dígitos, unidades produzidas), vida útil contábil × fiscal (Anexo III da IN RFB nº 1.700/2017) com IR diferido, depreciação acelerada por turnos (art. 323 do RIR/2018), valor residual e revisão anual, redução ao valor recuperável (CPC 01), CIAP (ICMS em 48 parcelas), intangível (CPC 04) e arrendamento do locatário (CPC 06 (R2)). Use quando o usuário comprar, vender ou baixar bem do imobilizado, fizer a revisão anual de vida útil e valor residual, suspeitar de perda de valor do bem, assinar arrendamento, ou mencionar \"depreciação\", \"imobilizado\", \"vida útil\", \"impairment\", \"CIAP\", \"direito de uso\", \"baixa de bem\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Ativo Imobilizado e Depreciação

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Monta o cadastro do bem com o custo correto, calcula a depreciação mensal contábil e a fiscal, propõe os lançamentos de aquisição, depreciação, perda de valor e baixa, controla o crédito de ICMS do CIAP e trata arrendamentos. Separa sempre a vida útil real (contábil) da vida útil fiscal, porque a diferença gera ajuste no imposto.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Compra, venda, baixa ou transferência de bem.
- Depreciação mensal (etapa D+3 da skill `fechamento-mensal`).
- Revisão anual de vida útil, valor residual e indícios de perda de valor.
- Contrato de arrendamento novo (locatário).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Veículo em nome de sócio ou empregado: não repetir CPF nem placa sem necessidade.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: Bem novo a cadastrar, revisão anual ou baixa/venda? Posso ler a nota fiscal de aquisição?
Q2: Tipo de bem (edificação, máquina, veículo, computador, móvel)? Local e centro de custo? Uso na produção ou na administração?
Q3: Data em que o bem ficou pronto para uso (não a data da nota)?
Q4: Regime tributário (Simples, Presumido, Real)? Contribuinte do ICMS com direito ao CIAP?
Q5: Norma adotada: CPCs completos, NBC TG 1000 (PME), NBC TG 1001 (pequena empresa) ou NBC TG 1002 (microentidade)? Muda o tratamento do arrendamento.
Q6: Houve fato que indique perda de valor do bem (queda de mercado, dano, obsolescência, bem parado)?
```

### 2. Reconhecimento e custo (CPC 27)
```
Custo = preço de aquisição
      + frete, seguro, instalação e montagem
      + tributos NÃO recuperáveis
      + custos de teste antes do uso
      + encargos financeiros até o bem ficar pronto, quando for ativo qualificável (CPC 20 (R1))
      − descontos comerciais e abatimentos
```
Não entram no custo: tributos recuperáveis (ICMS, PIS e COFINS com direito a crédito), treinamento, despesas gerais e manutenção após o início do uso.

Exemplo: máquina com preço 120.000 + frete 5.000 + montagem 3.000 = custo 128.000. O ICMS de 21.600 destacado na nota é recuperável e não entra no custo.

**Bem de pequeno valor (regra fiscal):** pode ser deduzido direto como despesa o bem de valor unitário de até R$ 1.200,00 ou com vida útil de até um ano, salvo quando a atividade exigir a utilização de um conjunto desses bens (art. 313, § 1º, do RIR/2018 (Decreto nº 9.580/2018)). Na contabilidade, a decisão de não ativar segue a política de materialidade da empresa, documentada.

### 3. Vida útil contábil × fiscal
A vida útil **contábil** é a estimativa real de uso do bem na empresa (CPC 27), apoiada em laudo, histórico ou política documentada. A vida útil **fiscal** é a referência da Receita Federal para dedução no Lucro Real (art. 320 do RIR/2018; Anexo III da IN RFB nº 1.700/2017). A empresa pode usar taxa fiscal diferente se comprovar que é adequada (art. 124 da IN RFB nº 1.700/2017).

Referência fiscal (Anexo III da IN RFB nº 1.700/2017 — o anexo classifica os bens pela NCM; conferir a posição do bem):
```
Bem                                          Vida útil   Taxa anual
Edificações                                  25 anos     4%
Máquinas e equipamentos (maioria das NCM)    10 anos     10%   conferir a NCM do bem
Instalações                                  10 anos     10%
Móveis de escritório (NCM 9403)              10 anos     10%
Automóveis de passageiros (NCM 8703)         5 anos      20%
Veículos para transporte de mercadorias (NCM 8704)  4 anos  25%
Tratores (NCM 8701)                          4 anos      25%
Computadores e unidades (NCM 8471)           5 anos      20%
Ferramentas manuais (NCM 8202 a 8207)        5 anos      20%
Terrenos                                     não depreciam
```
Software é intangível: amortização, não depreciação (CPC 04 (R1)), pela vida útil estimada (prazo de uso ou de licença). O Anexo III não traz linha para programas de computador; não usar a taxa de computadores (NCM 8471) para software.

Quando a depreciação contábil e a fiscal diferem, a diferença é temporária: controlar no e-Lalur (Parte B) e, quando aplicável, reconhecer IR e CSLL diferidos (CPC 32). Exemplo: base 120.000; contábil em 96 meses = 1.250,00 por mês; fiscal em 120 meses = 1.000,00 por mês; diferença de 250,00 por mês.

**Depreciação acelerada por turnos (fiscal, bens móveis):** coeficiente 1,0 para um turno de 8 horas, 1,5 para dois turnos e 2,0 para três turnos (art. 323 do RIR/2018). É benefício fiscal: na contabilidade, o uso mais intenso já deve estar refletido na vida útil estimada.

**Revisão anual obrigatória:** vida útil, valor residual e método são revisados pelo menos no fim de cada exercício; mudança tem efeito prospectivo, como mudança de estimativa (CPC 27, item 51; CPC 23).

### 4. Métodos e cálculo da depreciação
```
LINEAR (mais usado):    (custo − valor residual) ÷ vida útil em meses
SOMA DOS DÍGITOS:       parcelas maiores no início; fator = dígito do período ÷ [n × (n + 1) ÷ 2]
UNIDADES PRODUZIDAS:    (custo − valor residual) ÷ unidades estimadas × unidades do período
```
A depreciação começa quando o bem está disponível para uso (no local e na condição de funcionar), não na data da nota. Bem em construção ou montagem não deprecia.

Cálculo de apoio (só cálculo, sem acesso a arquivos):
```python
# Depreciação linear mensal: contábil (vida útil real) e fiscal (Anexo III, com turnos)
def deprec_mensal(custo, valor_residual, vida_util_meses):
    return (custo - valor_residual) / vida_util_meses

def deprec_fiscal_mensal(custo, valor_residual, vida_fiscal_meses, turnos=1):
    # coeficientes do art. 323 do RIR/2018 (bens móveis): 1 turno 1,0; 2 turnos 1,5; 3 turnos 2,0
    fator = {1: 1.0, 2: 1.5, 3: 2.0}.get(turnos, 1.0)
    return (custo - valor_residual) / vida_fiscal_meses * fator

# Exemplo: custo 128.000, residual 8.000, contábil 96 meses, fiscal 120 meses
print(f"Contábil: R$ {deprec_mensal(128_000, 8_000, 96):,.2f}")        # 1.250,00
print(f"Fiscal 1 turno: R$ {deprec_fiscal_mensal(128_000, 8_000, 120):,.2f}")    # 1.000,00
print(f"Fiscal 2 turnos: R$ {deprec_fiscal_mensal(128_000, 8_000, 120, 2):,.2f}") # 1.500,00
```
Controlar o limite: a depreciação acumulada nunca passa do custo menos o valor residual.

### 5. Lançamentos (contas pelo nome; usar o código do plano do cliente)
```
Aquisição:
  D Imobilizado (conta do bem)         C Banco ou Fornecedores
  D ICMS a recuperar (CIAP), quando houver crédito

Depreciação de bem administrativo:
  D Despesa de depreciação             C (−) Depreciação acumulada
Depreciação de bem da produção:
  D Custo de produção — depreciação    C (−) Depreciação acumulada

Baixa ou venda com ganho:
  D (−) Depreciação acumulada (saldo do bem)   D Banco (valor recebido)
  C Imobilizado (custo histórico)              C Ganho na venda de imobilizado
Baixa ou venda com perda:
  D (−) Depreciação acumulada   D Banco   D Perda na venda de imobilizado
  C Imobilizado (custo histórico)
```
Exemplo de venda: após 30 meses, acumulada 37.500 e valor contábil 90.500; venda por 95.000 gera ganho de 4.500.

### 6. Redução ao valor recuperável (CPC 01 (R1))
- A cada data de balanço, verificar se há **indicação** de perda de valor (queda de preço de mercado, dano físico, obsolescência, bem ocioso, mudança desfavorável no uso). Havendo indicação, calcular o valor recuperável. O teste anual obrigatório, mesmo sem indicação, vale para intangível de vida útil indefinida, intangível ainda não disponível para uso e ágio.
- Valor recuperável = o **maior** entre o valor justo líquido de despesas de venda e o valor em uso (valor presente dos fluxos de caixa esperados).
- Se o valor contábil for maior que o recuperável, reconhecer a perda:
```
D Perda por redução ao valor recuperável (resultado)
C (−) Perdas por redução ao valor recuperável (conta redutora própria do imobilizado)
```
Não usar a conta de depreciação acumulada nem chamar de "provisão". Reversão é permitida se o valor recuperável voltar a subir (exceto ágio).
- No Lucro Real, a perda só é dedutível quando o bem for alienado ou baixado (art. 32 da Lei nº 12.973/2014); até lá, adicionar no e-Lalur.
- PME pela NBC TG 1000: Seção 27 (redução ao valor recuperável), com a mesma lógica de indicação.

### 7. CIAP — crédito de ICMS sobre o imobilizado
```
Crédito mensal = (ICMS da nota ÷ 48) × (saídas tributadas ÷ total de saídas do mês)
```
- Apropriação em 48 parcelas mensais, a partir da entrada do bem, no Bloco G da EFD ICMS/IPI (art. 20, § 5º, da Lei Complementar nº 87/1996 (Lei Kandir)).
- Parcela não escriturada no mês: conferir no regulamento do ICMS da UF do cliente se e como pode ser aproveitada fora do período. O direito de usar o crédito extingue-se depois de cinco anos contados da emissão do documento (art. 23, parágrafo único, da Lei Complementar nº 87/1996).
- Bem alienado antes de decorridos quatro anos da aquisição: a partir da alienação, as parcelas restantes não são aproveitadas (art. 20, § 5º, V, da Lei Complementar nº 87/1996). Em baixa por perda ou transferência, conferir a regra no regulamento do ICMS da UF.
- Optante do Simples Nacional não toma crédito de ICMS pelo CIAP.
- Reforma Tributária: em 2026 o ICMS segue sem mudança no CIAP; a redução gradual do ICMS, com a entrada do IBS, começa em 2029 (Emenda Constitucional nº 132/2023 e Lei Complementar nº 214/2025). Antes de orientar planejamento de saldos de CIAP para os anos de transição, ler as regras de aproveitamento dos saldos credores de ICMS na Lei Complementar nº 214/2025.

### 8. Arrendamento — locatário (CPC 06 (R2))
**Antes de aplicar, conferir a norma da empresa.** Empresa que adota a NBC TG 1000 (R1) (PME) segue a Seção 20, que mantém a separação entre arrendamento financeiro (ativo e passivo) e operacional (despesa ao longo do prazo). O modelo de direito de uso abaixo é do CPC 06 (R2), para quem adota os CPCs completos.
```
Dados: 60 parcelas mensais de 4.448,89; taxa incremental 1% a.m.
Início (valor presente das 60 parcelas a 1% a.m. = 200.000,00):
  D Direito de uso                          200.000,00
  C Passivo de arrendamento (CP e LP)       200.000,00

1º mês (juros = 200.000,00 × 1% = 2.000,00; principal = 4.448,89 − 2.000,00):
  D Passivo de arrendamento                   2.448,89
  D Juros de arrendamento (despesa financeira) 2.000,00
  C Banco                                     4.448,89
(os juros caem mês a mês sobre o saldo do passivo: 2º mês = 197.551,11 × 1% = 1.975,51)

Amortização do direito de uso (200.000 ÷ 60 meses):
  D Amortização do direito de uso (despesa ou custo)  3.333,33
  C (−) Amortização acumulada — direito de uso       3.333,33
```
Isenções opcionais: contratos com prazo de 12 meses ou menos e bens de baixo valor (o IASB citou, nas bases de conclusão, a referência de cerca de US$ 5 mil para o bem novo).

### 9. Entregáveis
**a) Cadastro do bem**
```
Nº patrimônio: __   Descrição: __
Aquisição: __/__/__   Fornecedor: __   NF: __
Disponível para uso em: __/__/__
Custo: R$ __ (preço + frete + montagem + tributos não recuperáveis)
Local: __   Centro de custo: __   Uso: produção | administração
Vida útil contábil: __ anos   Vida útil fiscal (Anexo III): __ anos   Turnos: __
Valor residual: R$ __
Depreciação mensal contábil: R$ __   fiscal: R$ __   diferença: R$ __
Depreciação acumulada: R$ __   Valor contábil líquido: R$ __
CIAP: parcela __/48
```
**b)** Lançamentos do mês (depreciação, CIAP, baixas).
**c)** Memória de cálculo por bem.
**d)** Alerta de perda de valor quando houver indicação.
**e)** Checklist anual:
```
[ ] Revisão de vida útil, valor residual e método (CPC 27, item 51)
[ ] Indícios de perda de valor avaliados (CPC 01 (R1))
[ ] Inventário físico × controle de bens × razão
[ ] CIAP escriturado todo mês
[ ] Diferença contábil × fiscal controlada no e-Lalur e IR diferido revisado
```

## Erros comuns / pontos de atenção
- Depreciar a partir da data da nota em vez da data em que o bem ficou pronto para uso.
- Depreciar bem em construção ou montagem.
- Usar a vida útil fiscal como contábil sem análise (distorce a DRE e esquece o IR diferido).
- Aplicar a aceleração por turnos na contabilidade como se fosse estimativa de vida útil.
- Lançar perda por redução ao valor recuperável na depreciação acumulada.
- Não revisar vida útil e valor residual no fim do exercício.
- Incluir ICMS recuperável no custo do bem.
- Aplicar o modelo de direito de uso (CPC 06 (R2)) a empresa que adota a NBC TG 1000.
- Depreciar terreno junto com a edificação (separar os valores).

## Perguntas que o usuário costuma fazer
- **"Posso lançar direto em despesa um bem de R$ 1.100?"** Pela regra fiscal, sim, se for valor unitário até R$ 1.200,00 e não fizer parte de um conjunto necessário à atividade. Na contabilidade, depende da política de materialidade da empresa.
- **"A empresa trabalha em 3 turnos. Dobro a depreciação no balanço?"** No fiscal, pode usar coeficiente 2,0 (art. 323 do RIR/2018). No contábil, a vida útil estimada já deve refletir o uso intenso.
- **"Presumido precisa controlar depreciação fiscal?"** A depreciação não muda o imposto no Presumido, mas é obrigatória na contabilidade e afeta o ganho de capital na venda do bem.

## Quando escalar
- CIAP e Bloco G em detalhe: skill `efd-icms-ipi`.
- Adições e exclusões no Lucro Real (depreciação, perda de valor): skill `apuracao-lucro-real`.
- Modelos de lançamento: `lancamentos-contabeis-padrao`.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre outro formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- CPC 27 — Ativo Imobilizado (reconhecimento, custo, depreciação; item 51, revisão anual de vida útil e valor residual).
- CPC 01 (R1) — Redução ao Valor Recuperável de Ativos.
- CPC 04 (R1) — Ativo Intangível.
- CPC 06 (R2) — Arrendamentos.
- CPC 20 (R1) — Custos de Empréstimos (capitalização em ativo qualificável).
- CPC 23 — Políticas Contábeis, Mudança de Estimativa e Retificação de Erro.
- CPC 32 — Tributos sobre o Lucro (IR diferido).
- NBC TG 1000 (R1) — PME: Seção 17 (imobilizado), Seção 20 (arrendamentos), Seção 27 (redução ao valor recuperável). Pequena empresa e microentidade: NBC TG 1001 e NBC TG 1002, conforme a norma adotada pelo cliente.
- Art. 313, § 1º, art. 317, art. 320 e art. 323 do RIR/2018 (Decreto nº 9.580/2018): bem de pequeno valor (até R$ 1.200,00), dedutibilidade da depreciação, taxa anual e coeficientes por turnos.
- Anexo III e art. 124 da IN RFB nº 1.700/2017: taxas fiscais de depreciação e uso de taxa diferente comprovada.
- Art. 32 da Lei nº 12.973/2014: dedutibilidade da perda por redução ao valor recuperável só na alienação ou baixa.
- Art. 20, § 5º (crédito de ICMS do ativo imobilizado em 48 parcelas — CIAP; inciso V, alienação antes de quatro anos) e art. 23, parágrafo único (prazo de cinco anos para usar o crédito), da Lei Complementar nº 87/1996 (Lei Kandir).
- Emenda Constitucional nº 132/2023 e Lei Complementar nº 214/2025: transição do ICMS para o IBS.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
