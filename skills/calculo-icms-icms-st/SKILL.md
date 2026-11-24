---
name: calculo-icms-icms-st
description: "Calcula o ICMS próprio e o ICMS-ST em operações internas e interestaduais, com MVA ajustada, DIFAL (LC 190/2022) e FCP, alíquota de 4% de importados, antecipação e remetente do Simples. Use quando o usuário emitir ou receber nota interestadual ou disser \"ICMS\", \"ICMS-ST\", \"substituição tributária\", \"MVA\", \"MVA ajustada\", \"DIFAL\", \"diferencial de alíquota\", \"FCP\", \"FECP\", \"GNRE\", \"Convênio 142/2018\", \"Resolução SF 13\", \"4% importado\", \"alíquota interestadual\". Entrega: cálculo passo a passo, memória nota a nota, GNRE a emitir e checklist contra autuação. Em 2026 lembra os grupos de CBS/IBS do ano-teste na NF-e."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Cálculo de ICMS e ICMS-ST

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Calcula, item a item, o ICMS próprio da operação, o ICMS-ST (substituição tributária: o vendedor recolhe antecipadamente o imposto das etapas seguintes), o DIFAL (diferença entre a alíquota interna do estado de destino e a interestadual) e o FCP (adicional de fundo de combate à pobreza). Diz qual guia pagar, para qual estado e quando, e lista o que conferir para evitar autuação.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Venda interestadual com ou sem ST.
- Venda a consumidor final não contribuinte de outro estado (DIFAL).
- Compra interestadual para uso, consumo ou ativo imobilizado (DIFAL do comprador contribuinte).
- Mercadoria importada (4%).
- Conferência de nota emitida ou recebida.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Nota para consumidor pessoa física traz CPF e endereço: não repetir na memória de cálculo.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite. A GNRE é só instrução; quem emite e paga é o contador ou o cliente.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 0. Reforma Tributária — 2026 é ano-teste
Emenda Constitucional nº 132/2023 e LC nº 214/2025: em 2026 a NF-e destaca CBS 0,9% e IBS 0,1%, compensáveis com PIS/COFINS, sem efeito de caixa para quem cumpre as obrigações acessórias. Desde 03/08/2026 a NF-e do regime normal (CRT 3) sem os grupos de CBS/IBS é rejeitada (rejeição 1115); para Simples e MEI, a partir de 04/01/2027 (Ato Conjunto RFB/CGIBS nº 4/2026). O IBS substitui o ICMS aos poucos de 2029 a 2032; o ICMS acaba em 2033. Nesta skill o cálculo do ICMS segue as regras atuais; para CBS/IBS use `reforma-tributaria-transicao` e confira a página "Reforma do Consumo" da Receita Federal.

### 1. Tabelas de referência
```
ALÍQUOTAS INTERESTADUAIS (Resolução do Senado Federal nº 22/1989 e nº 13/2012)
4%  importados (ou com conteúdo de importação acima de 40%, com FCI
    — Ficha de Conteúdo de Importação — atualizada), salvo exceções da
    Resolução SF nº 13/2012
7%  saída de SP, RJ, MG, RS, PR ou SC para estados do Norte, Nordeste,
    Centro-Oeste e Espírito Santo
12% demais combinações (inclusive entre os estados do Sul/Sudeste,
    e de N/NE/CO/ES para qualquer estado)

ALÍQUOTAS INTERNAS — definidas pela lei de cada UF
Não usar tabela "de memória": várias UFs mudaram a alíquota modal desde
2023 e algumas somam adicional de fundo de pobreza (FCP, FECP, FECOP).
Antes de calcular, conferir na lei estadual do ICMS e no RICMS da UF de
destino, na data da operação:
  - a alíquota modal (geral) e a específica do NCM (combustíveis, energia,
    comunicação, cesta básica, medicamentos têm alíquotas próprias);
  - o adicional de FCP do produto, se houver, e se é recolhido em guia
    ou campo separado;
  - eventual redução de base de cálculo ou benefício do produto.
Registrar na memória de cálculo a norma estadual e o artigo usados.

CFOPs MAIS USADOS
5.102/6.102 venda de mercadoria adquirida de terceiros
5.101/6.101 venda de produção do estabelecimento
5.401/6.401 venda de produção própria com ST, como substituto
5.403/6.403 venda de mercadoria de terceiros com ST, como substituto
5.405       venda de mercadoria recebida com ST já retido (substituído)
6.404       venda de mercadoria com ST cujo imposto já foi retido antes
6.107/6.108 venda a não contribuinte (produção própria / de terceiros)
1.411/2.411 devolução de venda de mercadoria com ST
5.411/6.411 devolução de compra para comercialização com ST
```

### 2. Entrevista mínima
```
P1: "UF de origem, UF de destino, NCM, valor da mercadoria, frete, seguro, outras despesas e IPI?"
P2: "Destinatário é contribuinte do ICMS? Vai revender, industrializar ou usar/consumir?"
P3: "Remetente é do regime normal ou do Simples Nacional?"
P4: "O NCM tem ST entre essas UFs (Convênio ou Protocolo)? Qual a MVA original?"
P5 (importado): "Tem FCI? Conteúdo de importação acima de 40%?"
P6: "O remetente tem inscrição estadual de substituto na UF de destino?"
```
Se vier o XML, leia e extraia tudo; não pergunte o que já está na nota.

### 3. Cálculo (rodar em Python)
```python
# ICMS próprio, MVA ajustada, ICMS-ST, DIFAL "por dentro" e FCP.

def base_icms(valor, frete=0.0, seguro=0.0, outras=0.0, ipi=0.0, ipi_integra=False):
    # IPI integra a base, EXCETO entre contribuintes quando o produto vai para
    # industrialização ou comercialização (art. 13, §2º, da LC nº 87/1996)
    return valor + frete + seguro + outras + (ipi if ipi_integra else 0.0)

def mva_ajustada(mva_original, aliq_inter, aliq_interna_destino):
    return ((1 + mva_original) * (1 - aliq_inter) / (1 - aliq_interna_destino)) - 1

def icms_st(base_propria, ipi, mva, aliq_interna_destino, icms_proprio):
    # na base da ST o IPI entra (quando houver)
    base_st = (base_propria + ipi) * (1 + mva)
    return base_st, base_st * aliq_interna_destino - icms_proprio

def difal_nao_contribuinte(valor_operacao, aliq_inter, aliq_interna, fcp=0.0):
    # Base dupla ("por dentro"): tira o ICMS de origem e embute o de destino.
    # Alguns estados usam base única — conferir a lei da UF de destino.
    icms_origem = valor_operacao * aliq_inter
    base_destino = (valor_operacao - icms_origem) / (1 - (aliq_interna + fcp))
    difal = base_destino * aliq_interna - icms_origem
    valor_fcp = base_destino * fcp
    return icms_origem, base_destino, difal, valor_fcp

# Exemplo 1: SP -> BA, contribuinte que vai revender, mercadoria 10.000 + frete 500,
# MVA original 35%, alíquota interna HIPOTÉTICA de 19% (conferir a da BA)
base = base_icms(10_000, frete=500)
icms_p = base * 0.07
mva = mva_ajustada(0.35, 0.07, 0.19)
base_st, st = icms_st(base, 0, mva, 0.19, icms_p)
print(f"Base {base:,.2f} | ICMS próprio {icms_p:,.2f} | MVA aj {mva:.4%} | Base ST {base_st:,.2f} | ICMS-ST {st:,.2f}")
# Esperado: 10.500,00 | 735,00 | 55,0000% | 16.275,00 | 2.357,25

# Exemplo 2: venda de SP a consumidor final não contribuinte em GO,
# valor 1.000, interestadual 7%, interna HIPOTÉTICA 19%, sem FCP
print(difal_nao_contribuinte(1_000, 0.07, 0.19))
```

### 4. Regras críticas
- **MVA ajustada**: em operação interestadual com ST use a MVA ajustada quando o Convênio ou Protocolo mandar (regra geral do Convênio ICMS nº 142/2018 para operação interestadual): `MVA aj = [(1 + MVA orig) × (1 − alíq. inter) ÷ (1 − alíq. interna destino)] − 1`.
- **ICMS-ST = base ST × alíquota interna do destino − ICMS próprio**. Esquecer de subtrair o ICMS próprio dobra o imposto.
- **IPI na base do ICMS próprio**: entra quando o destinatário vai usar, consumir ou imobilizar, ou não é contribuinte; não entra entre contribuintes para revenda ou industrialização (art. 13, §2º, da LC nº 87/1996).
- **DIFAL — venda a não contribuinte de outra UF** (art. 155, §2º, VII e VIII, da Constituição; LC nº 190/2022): o remetente recolhe o ICMS interestadual à origem e o DIFAL ao destino (GNRE por operação, ou apuração mensal se tiver inscrição na UF de destino). O STF validou a cobrança a partir de 05/04/2022, só com a noventena, sem anterioridade anual (ADIs nº 7.066, 7.070 e 7.078). Antes disso, o STF exigiu lei complementar para o DIFAL (Tema 1.093, RE 1.287.019, e ADI nº 5.469, julgados em 24/02/2021).
- **DIFAL — compra por contribuinte para uso, consumo ou ativo**: quem paga o DIFAL é o destinatário, na apuração da UF dele.
- **FCP** (Fundo de Combate à Pobreza, art. 82 do ADCT da Constituição): adicional de até 2 pontos em produtos definidos pela UF. No DIFAL e na ST o FCP do destino vai para o destino e costuma ter guia ou campo próprio. Ex.: RJ (FECP), BA, PE, MG em produtos específicos — conferir a lista da UF.
- **Remetente do Simples Nacional**: o ICMS próprio é pago no DAS. Quando vende a contribuinte para comercialização ou industrialização, a nota pode informar o crédito ao comprador, limitado ao ICMS efetivamente devido no Simples (CSOSN 101; art. 23, §1º, da LC nº 123/2006). O ICMS devido como substituto tributário fica fora do DAS (art. 13, §1º, XIII, "a", da LC nº 123/2006): o optante calcula a ST normalmente; o valor a abater como "ICMS próprio" segue as regras do Convênio ICMS nº 142/2018 e da lei da UF de destino — conferir antes de fechar o cálculo.
- **DIFAL de optante do Simples na venda a não contribuinte de outra UF**: a cláusula nona do Convênio ICMS nº 93/2015, que estendia esse DIFAL ao Simples, foi declarada inconstitucional pelo STF (ADI nº 5.464, com efeitos desde a cautelar de 2016, e Tema 1.093). A LC nº 190/2022 não alterou a LC nº 123/2006 para incluir esse DIFAL no Simples. Antes de exigir o DIFAL de remetente optante, conferir a lei da UF de destino e se há discussão judicial do cliente sobre o tema. Não confundir com o DIFAL de **entrada** do optante que compra para uso, consumo ou ativo, que existe (art. 13, §1º, XIII, "h", da LC nº 123/2006).
- **4% de importados**: só com FCI válida e conteúdo de importação acima de 40% (Resolução SF nº 13/2012). Sem FCI, use a alíquota normal e registre a pendência.
- **Antecipação na entrada**: vários estados (ex.: BA, PE, GO, MG) cobram antecipação parcial do comprador na entrada interestadual, inclusive de optante do Simples (STF, Tema 517). Conferir a UF.

### 5. Entregável obrigatório
**a) Cálculo passo a passo por nota**
```
NF nº 0001 — SP → BA — destinatário contribuinte (revenda)
Item: NCM 0000.00.00 — PRODUTO EXEMPLO
Valor da mercadoria .................. 10.000,00
+ Frete (cobrado na nota) ............ 500,00
+ IPI (não entra: revenda entre contribuintes) 0,00
= BASE DO ICMS PRÓPRIO ............... 10.500,00
ICMS próprio (7%) .................... 735,00
MVA original: 35% (conferir o Convênio/Protocolo do NCM)
MVA ajustada: [(1,35 × 0,93) ÷ 0,81] − 1 = 55,00%
BASE ST: 10.500 × 1,55 = 16.275,00
ICMS-ST: 19% × 16.275 − 735 = 3.092,25 − 735 = 2.357,25
GNRE para a BA antes da saída: 2.357,25 (se o remetente não tiver IE de substituto na BA)
ICMS próprio: entra na apuração mensal de SP: 735,00
Total de ICMS da nota: 3.092,25 (próprio + ST)
(Alíquota interna de 19% é hipotética para o exemplo.)
```
**b) Memória de cálculo** com colunas `nf, uf_orig, uf_dest, ncm, valor, frete, ipi, base_icms, aliq_inter, icms_proprio, mva_orig, mva_aj, base_st, icms_st, difal, fcp, guia`.

**c) GNRE (instrução)**: portal GNRE (www.gnre.pe.gov.br) → UF favorecida → código de receita → valor → pagamento antes da saída. Códigos mais usados por operação: 10009-9 (ICMS substituição tributária por operação), 10010-2 (ICMS consumidor final não contribuinte de outra UF por operação — DIFAL) e 10012-9 (FCP por operação). Cada UF configura no portal quais códigos aceita e quais detalhamentos exige: há UF que cobra o FCP junto com o ICMS no mesmo código (é o caso do RJ com o FECP). Conferir a tela da UF favorecida antes de emitir. Se o remetente tiver inscrição estadual de substituto no destino, o recolhimento é mensal, no prazo da UF de destino, e não por nota.

**d) Checklist (9 itens)**
```
[ ] NCM conferido no Convênio ICMS nº 142/2018 e no Protocolo/Convênio entre as UFs
[ ] MVA ajustada (não a original) na interestadual, quando aplicável
[ ] IPI na base conforme a destinação
[ ] DIFAL e FCP calculados na venda a não contribuinte de outra UF
[ ] GNRE paga antes da saída (ou IE de substituto no destino conferida)
[ ] Antecipação na UF de destino verificada
[ ] CFOP coerente (5.401, 5.403, 5.405, 6.404, 6.108...)
[ ] CST/CSOSN coerente (10 com ST; 60 com ST já recolhido; 101/201/500 no Simples)
[ ] EFD ICMS/IPI: C170, C190, E110, E200/E210 e E300/E310 (DIFAL/FCP) batendo
```

### 6. Casos de borda
- **Devolução de mercadoria com ST**: CFOP 1.411/2.411 (devolução de venda) ou 5.411/6.411 (devolução de compra). O ICMS-ST é estornado ou ressarcido conforme a regra da UF.
- **Zona Franca de Manaus e Áreas de Livre Comércio**: tratamento especial (isenção de ICMS na remessa com abatimento na nota, PIS/COFINS próprios). Use também `efd-icms-ipi`.
- **Venda a construtora como consumidora final**: se a construtora não for contribuinte do ICMS, aplica o DIFAL do remetente.
- **Brinde e bonificação** (CFOP 5.910/6.910): em regra o ICMS incide. Amostra grátis tem isenção condicionada (Convênio ICMS nº 29/1990). Para PIS/COFINS, analisar o caso.
- **Regime especial da UF**: pode haver alíquota reduzida ou crédito presumido; conferir o decreto da UF.
- **NF cancelada depois de pagar a GNRE**: pedir restituição à SEFAZ de destino (processo demorado).

### 7. Quando escalar
- ICMS-ST pago a maior porque o preço final foi menor que a base presumida (STF, Tema 201, RE 593.849) → pedido de restituição na SEFAZ (lógica parecida com recuperação de créditos; usar `recuperacao-creditos-pis-cofins` só como modelo de memória de cálculo).
- Bloco K ou EFD ICMS/IPI → `efd-icms-ipi`.
- Autuação da SEFAZ → `resposta-fiscalizacao-intimacao`.
- Revisão de 5 anos → `revisao-fiscal-cruzamento-sped`.

## Erros comuns / pontos de atenção
- Usar a MVA original em operação interestadual.
- Não subtrair o ICMS próprio do ICMS-ST.
- Pôr ou tirar o IPI da base sem olhar a destinação.
- Esquecer DIFAL e FCP na venda a não contribuinte.
- Aplicar 4% sem FCI.
- Tratar optante do Simples como regime normal (o ICMS próprio está no DAS).
- Pagar GNRE depois da saída (autuação no trânsito).
- Usar alíquota interna "de memória": várias UFs mudaram a alíquota modal nos últimos anos; conferir sempre a lei estadual vigente.

## Perguntas que o usuário costuma fazer
- "Vendo de MG para SP: 7% ou 12%?" 12% (Sul/Sudeste para Sul/Sudeste, exceto ES).
- "Quem paga o DIFAL na venda para pessoa física de outro estado?" O remetente, para o estado de destino.
- "Preciso de GNRE para toda nota com ST?" Não, se tiver inscrição de substituto na UF de destino: aí recolhe por apuração mensal.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas a fisco): documento DOCX.
- Este padrão prevalece sobre os formatos citados acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- Constituição Federal: art. 155, §2º, VII e VIII (DIFAL); ADCT, art. 82 (FCP).
- LC nº 87/1996 (Lei Kandir): art. 13 (base de cálculo; §2º, IPI), arts. 6º a 10 (substituição tributária).
- LC nº 190/2022 (DIFAL para não contribuinte).
- Resolução do Senado Federal nº 22/1989 (7% e 12%) e nº 13/2012 (4% de importados).
- Convênio ICMS nº 142/2018 (regras gerais da ST); Convênio ICMS nº 93/2015 (DIFAL); Convênio ICMS nº 29/1990 (amostra grátis).
- LC nº 123/2006: art. 13, §1º, XIII, "a" (ST fora do DAS) e "h" (DIFAL na entrada), art. 23, §1º (crédito ao comprador).
- STF: Tema 1.093 (RE 1.287.019) e ADI nº 5.469; ADIs nº 7.066, 7.070 e 7.078; ADI nº 5.464; Tema 201 (RE 593.849); Tema 517.
- Emenda Constitucional nº 132/2023, LC nº 214/2025 e Ato Conjunto RFB/CGIBS nº 4/2026 (CBS/IBS em 2026).
- Convênio S/Nº de 1970 (CFOP). Lei estadual do ICMS e RICMS de cada UF (alíquotas internas, FCP e antecipação).
- Portal GNRE (códigos de receita por UF).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
