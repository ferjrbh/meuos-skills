---
name: dre-gerencial
description: "Monta a DRE gerencial do cliente separando custos variáveis e fixos, calcula margem de contribuição (MC), ponto de equilíbrio (PE) em reais e em unidades, compara realizado × orçado × ano anterior e analisa por produto, cliente, loja ou centro de custo, com sensibilidade e recomendações. Acionar quando o usuário disser \"DRE gerencial\", \"margem de contribuição\", \"ponto de equilíbrio\", \"custo variável e fixo\", \"quanto preciso vender\", \"vale a pena fechar a loja\", \"análise de mix\", \"realizado contra orçado\" ou pedir indicadores gerenciais para decisão de preço, mix ou corte de custos. Entrega: DRE gerencial amarrada à DRE contábil, cálculo do PE, sensibilidade e recomendações."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# DRE gerencial

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Reorganiza a DRE contábil em visão de gestão: o que varia com a venda (custos variáveis) e o que não varia (custos e despesas fixos). Com isso calcula quanto cada real vendido sobra para pagar a estrutura (margem de contribuição) e quanto a empresa precisa vender para não ter prejuízo (ponto de equilíbrio). Termina com cenários e recomendações concretas.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Decisão de preço, de mix de produtos ou de fechar uma unidade.
- Cliente que pergunta "quanto preciso faturar por mês".
- Comparação realizado × orçado × ano anterior.
- Não usar para a DRE oficial (CPC 26): essa sai do fechamento (`fechamento-mensal`).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Na análise de pessoal, trabalhar com totais por área, não com salário individual.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e entrega.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: Cliente (CNPJ), competência, DRE contábil do período e regime tributário?
Q2: Existe orçamento aprovado para comparar?
Q3: Análise por produto, unidade ou centro de custo?
Q4: Volume vendido por produto (unidades) — para PE em unidades?
Q5: Mix médio (% de cada produto na venda) — para PE consolidado?
```

### 2. Estrutura da DRE gerencial
```
RECEITA BRUTA
(−) Devoluções, abatimentos e descontos incondicionais
(−) Tributos sobre a venda (ICMS, ISS, PIS, COFINS; no Simples, o DAS)
= RECEITA LÍQUIDA

(−) CUSTOS VARIÁVEIS
   CMV / CPV / CSP (parte variável)
   Comissão sobre venda
   Frete sobre venda
   Tarifa de cartão (MDR)
= MARGEM DE CONTRIBUIÇÃO (R$ e % da receita líquida)

(−) CUSTOS E DESPESAS FIXOS (sem depreciação)
   Pessoal indireto, aluguel, energia (parte fixa), marketing, administrativo
= EBITDA (resultado antes de juros, impostos sobre o lucro, depreciação e amortização)
(−) Depreciação e amortização
= EBIT (resultado operacional)
(±) RESULTADO FINANCEIRO
= LAIR
(−) IRPJ + CSLL (Lucro Real ou Presumido; no Simples já estão dentro do DAS)
= LUCRO LÍQUIDO
```
Pontos de atenção da estrutura:
- **IPI não é dedução da receita bruta.** O IPI destacado na nota é cobrado do comprador e fica fora da receita bruta (art. 12, § 4º, do Decreto-Lei nº 1.598/1977, com a redação da Lei nº 12.973/2014). Se o relatório do cliente traz o faturamento "com IPI", tirar o IPI antes de começar.
- **Depreciação aparece uma vez só**, depois do EBITDA. Não incluí-la também na lista de fixos.
- **Simples Nacional:** o DAS entra como tributo sobre a venda; não há linha de IRPJ/CSLL separada.
- **2026, ano-teste da Reforma Tributária:** CBS (0,9%) e IBS (0,1%) aparecem destacados no documento fiscal (Lei Complementar nº 214/2025); quem cumpre as obrigações acessórias fica dispensado do recolhimento no ano-teste (art. 348, § 1º, da Lei Complementar nº 214/2025). Em 15/11/2026 não foi localizada norma ou orientação técnica do CFC ou do CPC que fixe um tratamento contábil único para esses valores. Na DRE gerencial: deixar os valores destacados fora da receita e da margem, dizer isso numa nota do relatório e manter o mesmo critério todos os meses. Se o contador responsável adotar outro critério na contabilidade, a DRE gerencial segue o dele, com a nota.
- EBITDA não é linha da DRE contábil: é indicador gerencial e deve vir com a definição usada.

### 3. Cálculos
```
MC        = Receita líquida − Custos variáveis
MC %      = MC / Receita líquida
PE (R$)   = Custos fixos / MC %
PE (unid) = Custos fixos / MC unitária (do mix médio, quando houver vários produtos)
Receita para lucro-alvo X = (Custos fixos + X) / MC %
Margem de segurança = (Receita realizada − PE) / Receita realizada
```
Exemplo: custos fixos R$ 100.000/mês e MC % de 40% → PE = R$ 250.000/mês.
Se o lucro-alvo é depois do IR, dividir o lucro-alvo por (1 − alíquota efetiva) antes de somar aos fixos.

### 4. Cálculo em Python
No Windows, gravar o código em arquivo `.py` com a ferramenta de escrita e rodar com `python -I -X utf8 arquivo.py` (evita problemas de aspas e acentos do `python -c`). Mostrar o código ao usuário antes de rodar.
```python
# DRE gerencial: recebe a receita JÁ LÍQUIDA dos tributos sobre a venda
def dre_gerencial(receita_liquida, custo_var, custo_fixo_sem_deprec,
                  deprec=0, result_fin=0, ir_csll=0):
    mc = receita_liquida - custo_var                 # margem de contribuição
    mc_pct = mc / receita_liquida                    # margem em % da receita líquida
    ebitda = mc - custo_fixo_sem_deprec              # fixos SEM depreciação
    ebit = ebitda - deprec                           # depreciação entra uma vez só
    lair = ebit + result_fin                         # resultado financeiro com sinal
    ll = lair - ir_csll
    # PE usa os fixos totais (inclui depreciação, que é custo da estrutura)
    fixos_totais = custo_fixo_sem_deprec + deprec
    pe = fixos_totais / mc_pct if mc_pct > 0 else float("inf")
    return {"mc": mc, "mc_pct": mc_pct, "ebitda": ebitda, "ebit": ebit,
            "lair": lair, "lucro_liquido": ll, "pe_mensal": pe}

r = dre_gerencial(1_500_000, 900_000, 400_000, 50_000, -10_000, 32_000)
for k, v in r.items():
    print(f"{k}: {v:.2%}" if k.endswith("pct") else f"{k}: R$ {v:,.2f}")
```
Observação: o PE contábil acima inclui a depreciação nos fixos. Para "PE de caixa", usar só os fixos que saem do caixa e dizer qual dos dois foi usado.

### 5. Entregável
**a) DRE gerencial do mês:**
```
                            REAL %RL    ORÇ %RL   VAR R$  VAR %   ANO ANT.
Receita bruta              ____         ____
(−) Deduções               (___)        (___)
Receita líquida            ____  100,0  ____ 100,0
(−) Custos variáveis       (___)        (___)
   CMV/CPV                 (___)        (___)
   Comissão                (___)        (___)
   Tarifa cartão           (___)        (___)
MARGEM DE CONTRIBUIÇÃO     ____   __%   ____  __%
(−) Fixos (sem depreciação)
   Pessoal indireto        (___)        (___)
   Aluguel                 (___)        (___)
   Energia                 (___)        (___)
   Marketing               (___)        (___)
   Administrativo          (___)        (___)
EBITDA                     ____   __%   ____  __%
(−) Depreciação            (___)        (___)
EBIT                       ____   __%   ____  __%
(±) Resultado financeiro   ____         ____
LAIR                       ____   __%   ____  __%
(−) IRPJ + CSLL            (___)        (___)
LUCRO LÍQUIDO              ____   __%   ____  __%

PONTO DE EQUILÍBRIO MENSAL: R$ __ (fixos / MC %)
MARGEM DE SEGURANÇA: __%
RECEITA PARA LUCRO-ALVO R$ X: R$ __
CONFERÊNCIA: lucro líquido gerencial = lucro líquido contábil do período? [ ]
```
**b) Sensibilidade:**
```
Cenário                  MC R$   Lucro líquido   PE
Realista                 __      __              __
Receita −10%             __      __              __
Custo variável +5%       __      __              __
Fixos reduzidos em __    __      __              __
```
**c) Recomendações** baseadas nos números, por exemplo:
- "A margem de contribuição caiu para __%; investigar o custo do insumo X."
- "PE atual de R$ X contra receita de R$ Y: margem de segurança de __%."
- "Cortar a despesa Z (R$ __/mês) eleva o lucro líquido em __%."

## Erros comuns / pontos de atenção
- Classificar como variável o que é fixo (aluguel da loja não varia com a venda).
- Comissão sobre venda lançada em marketing.
- DRE gerencial que não fecha com a contábil: o cliente perde a confiança.
- Não ratear despesas indiretas quando a análise é por unidade (e não explicar o critério do rateio).
- PE em unidades sem usar a MC unitária do mix médio.
- Comparar bases diferentes (realizado com IPI, orçado sem IPI).
- Contar a depreciação duas vezes (dentro dos fixos e depois do EBITDA).

### Casos de borda
- **Produto sazonal:** MC % oscila muito; analisar a média móvel de 12 meses.
- **Fechar uma loja:** calcular a margem direta da loja (receita − custos variáveis − fixos próprios). Os fixos rateados da matriz continuam existindo depois do fechamento.
- **Devoluções altas:** tratar como redução da receita, não como despesa.
- **Empresa em crescimento:** fixos sobem em degraus (contratação, sede maior); o PE muda a cada degrau.

### Quando escalar
- Fluxo de caixa projetado → `fluxo-caixa-projetado`
- Análise de balancete → `balancete-analise`
- Valuation → `valuation-pme`
- Comparação de regimes tributários → `analise-tributaria-regime`

### Autoavaliação
- [ ] Lucro gerencial = lucro contábil?
- [ ] Custos classificados (variável × fixo) com critério escrito?
- [ ] MC % sobre a receita líquida?
- [ ] PE em R$ e em unidades?
- [ ] Comparativos real, orçado e ano anterior?
- [ ] Sensibilidade?
- [ ] Recomendações concretas?

## Formato de entrega
- Cálculos, apurações e conciliações: entregar sempre planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar sempre documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Perguntas que o usuário costuma fazer
- **"Margem de contribuição é o mesmo que margem bruta?"** Não. Margem bruta tira só o custo da mercadoria; a de contribuição tira tudo o que varia com a venda (comissão, frete, cartão).
- **"Depreciação entra no ponto de equilíbrio?"** No PE contábil, sim. No PE de caixa, não. Dizer sempre qual foi usado.
- **"No Simples, onde entra o imposto?"** O DAS é tributo sobre a venda e entra antes da margem.

## Base legal usada nesta skill
- Art. 187 da Lei nº 6.404/1976 — estrutura da demonstração do resultado.
- Art. 12 do Decreto-Lei nº 1.598/1977 (redação da Lei nº 12.973/2014) — conceito de receita bruta; IPI destacado fora da receita bruta (§ 4º).
- CPC 26 (R1) — apresentação das demonstrações contábeis (referência para amarrar a DRE gerencial à oficial).
- NBC TG 1000 (R1) — contabilidade para pequenas e médias empresas (pequena empresa e microentidade: NBC TG 1001 e NBC TG 1002).
- Lei Complementar nº 214/2025 — CBS e IBS, ano-teste 2026 (art. 348, § 1º: dispensa do recolhimento para quem cumpre as obrigações acessórias).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
