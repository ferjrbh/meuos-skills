---
name: calculo-ipi
description: "Apuração mensal de IPI para indústria e estabelecimentos equiparados a industrial (importador, filial atacadista de indústria), com TIPI vigente (Decreto nº 11.158/2022 e alterações), CST de IPI, suspensão (drawback, RECOF, industrialização por encomenda), imunidade na exportação, crédito presumido da Lei nº 9.363/1996, saldo credor e DARF 5123. Acionar quando o usuário disser \"apurar IPI\", \"TIPI\", \"alíquota de IPI do NCM\", \"crédito de IPI\", \"saldo credor de IPI\", \"drawback\", \"RECOF\", \"industrialização por encomenda\", \"crédito presumido de exportação\", \"E520/E530\", \"DARF 5123\", \"Zona Franca de Manaus\" ou \"IPI zero em 2027\". Entrega: apuração débitos × créditos em planilha, DARF com vencimento e checklist."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Cálculo e apuração mensal de IPI

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Apura o IPI do mês: soma os débitos das saídas tributadas, soma os créditos das entradas que dão direito a crédito, considera o saldo credor anterior e chega ao IPI a recolher (DARF 5123) ou ao saldo credor que passa para o mês seguinte. Confere NCM, alíquota da TIPI, CST e o fundamento de cada suspensão, isenção ou imunidade.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Reforma Tributária.** 2026 é ano-teste da CBS (0,9%) e do IBS (0,1%) (Emenda Constitucional nº 132/2023 e Lei Complementar nº 214/2025). **A partir de 2027 as alíquotas do IPI ficam reduzidas a zero, exceto para produtos que tenham industrialização incentivada na Zona Franca de Manaus** (art. 126, III, "a", do ADCT, incluído pela EC nº 132/2023), e entra o Imposto Seletivo. Para o cronograma completo use a skill `reforma-tributaria-transicao`.

> **LC nº 224/2025.** Desde 01/04/2026 os benefícios fiscais de IPI foram reduzidos em 10% (redução linear de benefícios federais — art. 4º, §1º, V, da LC nº 224/2025). O sistema padrão de referência é a alíquota da TIPI sem as reduções das Notas Complementares (art. 4º, §3º, II), e os créditos presumidos de IPI das Leis nº 9.363/1996, nº 10.276/2001 e nº 9.440/1997 estão na lista de benefícios reduzidos (art. 4º, §2º, II, "c"), com aproveitamento limitado a 90% (art. 4º, §4º, IV). Antes de aplicar isenção, redução de alíquota ou crédito presumido, conferir a IN RFB nº 2.305/2025.

## Quando usar
- Indústria ou equiparado a industrial com saídas tributadas pelo IPI.
- Conferência de E520/E530 (apuração do IPI na EFD ICMS/IPI).
- Operações com suspensão (drawback, RECOF, remessa para industrialização), exportação, ZFM/ALC.
- Dúvida sobre crédito de entrada, estorno de crédito ou saldo credor.

Não usar para: empresa do Simples Nacional (o IPI vai no DAS, Anexo II — usar skill do Simples), ICMS/ICMS-ST (`calculo-icms-icms-st`), PIS/COFINS.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
1. CNPJ (pode ser de exemplo), competência e tipo de estabelecimento: industrial, equiparado (importador, filial atacadista, etc.) ou atacadista comum (que não é contribuinte do IPI na revenda).
2. Notas de entrada com IPI destacado (matéria-prima, produto intermediário, embalagem) e notas de saída tributadas.
3. Há suspensão (drawback, RECOF, remessa para industrialização), exportação, venda para ZFM/ALC?
4. Saldo credor do mês anterior? Crédito presumido em aproveitamento?

Se o cliente enviar XMLs, ler e separar o IPI por CST e por CFOP.

### 2. Tabelas de referência

**TIPI**: Decreto nº 11.158/2022, com as alterações posteriores. Cada NCM (8 dígitos) tem alíquota própria; há produtos com alíquota zero e produtos com alíquotas altas (fumo, bebidas). Sempre consultar a TIPI atualizada no site da Receita Federal na data da operação.

**CST do IPI** (tabela oficial — entradas 00 a 49; saídas 50 a 99):

| CST | Entrada | CST | Saída |
|---|---|---|---|
| 00 | Entrada com recuperação de crédito | 50 | Saída tributada |
| 01 | Entrada tributada com alíquota zero | 51 | Saída tributada com alíquota zero |
| 02 | Entrada isenta | 52 | Saída isenta |
| 03 | Entrada não tributada | 53 | Saída não tributada |
| 04 | Entrada imune | 54 | Saída imune |
| 05 | Entrada com suspensão | 55 | Saída com suspensão |
| 49 | Outras entradas | 99 | Outras saídas |

**CFOP mais comuns**
- 5.101/6.101: venda de produção do estabelecimento.
- 5.901/6.901: remessa para industrialização por encomenda (encomendante envia insumos).
- 5.902/6.902: retorno dos insumos usados na industrialização (industrializador devolve).
- 5.124/6.124: industrialização efetuada para outra empresa (cobrança do serviço e dos materiais próprios do industrializador).
- 5.501/6.501: remessa de produção do estabelecimento com fim específico de exportação (não é drawback).
- 3.127: compra para industrialização sob o regime de drawback; 7.127: venda de produção do estabelecimento sob o regime de drawback.
- 7.101: venda de produção do estabelecimento para o exterior.
- 1.201/2.201: devolução de venda de produção do estabelecimento (entrada).
- 5.910/6.910: remessa em bonificação, doação ou brinde.

**DARF e prazo**
- Código 5123 (IPI — demais produtos). Fumo, bebidas e outros produtos têm códigos próprios: conferir na tabela de códigos de receita da RFB.
- Vencimento: até o 25º dia do mês seguinte ao fato gerador; se o dia 25 não for dia útil, **antecipa** para o dia útil anterior (art. 52, I, "c", e §4º, da Lei nº 8.383/1991, com redação da Lei nº 11.933/2009). Cigarros do código NCM 2402.20.00 vencem no 10º dia do mês seguinte (art. 52, I, "a").
- Declaração: desde 2025 o IPI é declarado na DCTFWeb (módulo MIT), que vence no último dia útil do mês seguinte (IN RFB nº 2.248/2025). O prazo de **pagamento** continua sendo o dia 25.

### 3. Cálculo (Python, para mostrar a memória)

```python
# Apuração do IPI: saldo anterior + créditos - débitos
def ipi_apuracao(creditos, debitos, saldo_anterior=0):
    saldo = saldo_anterior + creditos - debitos
    if saldo >= 0:
        return saldo, 0            # sobra saldo credor: passa para o mês seguinte
    return 0, abs(saldo)           # falta crédito: IPI a recolher

creditos_mes = 12_500
debitos_mes = 18_000
saldo_anterior = 1_500
saldo_credor, ipi_recolher = ipi_apuracao(creditos_mes, debitos_mes, saldo_anterior)
print(f'IPI a recolher (DARF 5123): R$ {ipi_recolher:,.2f}')   # 4.000,00
print(f'Saldo credor a transportar: R$ {saldo_credor:,.2f}')   # 0,00

# Crédito presumido de IPI para ressarcimento de PIS/COFINS na exportação
# (Lei nº 9.363/1996): 5,37% sobre a base = insumos x (receita de exportação / receita operacional bruta)
def credito_presumido_9363(insumos, rec_exportacao, rec_operacional_bruta):
    return insumos * (rec_exportacao / rec_operacional_bruta) * 0.0537

cp = credito_presumido_9363(insumos=500_000, rec_exportacao=2_000_000, rec_operacional_bruta=10_000_000)
print(f'Crédito presumido (5,37%): R$ {cp:,.2f}')   # 5.370,00
# Atenção: desde 01/04/2026 o aproveitamento do crédito presumido fica limitado a 90%
# (art. 4º, §4º, IV, da LC nº 224/2025): cp_aproveitavel = cp * 0.90.
# Conferir também a regra alternativa da Lei nº 10.276/2001 antes de usar o valor.
print(f'Aproveitável desde 04/2026 (90%): R$ {cp * 0.90:,.2f}')   # 4.833,00
```

### 4. Regras críticas
- **IPI "por fora"**: não integra a própria base de cálculo. Integra a base do ICMS quando a operação é para uso/consumo ou destinatário não contribuinte (art. 13, § 2º, da LC nº 87/1996).
- **Crédito na entrada**: dá crédito o IPI destacado na aquisição de matéria-prima, produto intermediário e material de embalagem usados na industrialização (art. 226, I, do Decreto nº 7.212/2010 — RIPI). **Não** é "toda entrada tributada": bens do ativo imobilizado e material de uso e consumo não geram crédito.
- **Estorno**: o crédito de insumos usados em produtos isentos ou com alíquota zero pode ser mantido (art. 11 da Lei nº 9.779/1999). Para saídas **não tributadas (NT)** o crédito deve ser estornado (art. 254 do RIPI). Em saídas **com suspensão**, a manutenção do crédito depende do regime específico (drawback, RECOF, encomenda, exportação): ler a norma do regime e o ato concessório antes de manter o crédito e registrar o fundamento na memória.
- **Suspensão × isenção**: suspensão é condicional (exige um evento posterior, por exemplo exportar no prazo do drawback); isenção é dispensa definitiva. Se a condição da suspensão não for cumprida, o IPI fica devido com juros e multa.
- **Industrialização por encomenda**: o encomendante remete os insumos (CFOP 5.901, com suspensão). O industrializador devolve os insumos (5.902) e cobra a industrialização e os materiais que empregou (5.124). A suspensão no retorno vale quando o produto ainda será industrializado ou comercializado pelo encomendante nos termos do art. 43 do RIPI. Se o retorno for tributado, a base de cálculo segue o valor tributável do art. 190 do RIPI; montar a base com o valor da industrialização e dos materiais do industrializador conforme o enquadramento do caso concreto e registrar o inciso usado.
- **Exportação**: imune (art. 153, § 3º, III, da Constituição), com manutenção dos créditos das entradas. Pode gerar crédito presumido da Lei nº 9.363/1996 (ou da Lei nº 10.276/2001), **mas só para empresa cujo PIS/COFINS é cumulativo**: as Leis nº 9.363/1996 e nº 10.276/2001 não se aplicam à pessoa jurídica submetida à apuração não cumulativa (art. 14 da Lei nº 10.833/2003). Empresa do Lucro Real no não cumulativo não calcula esse crédito presumido; ela mantém os créditos de PIS/COFINS vinculados à exportação.
- **ZFM e ALC**: regime próprio (Decreto-Lei nº 288/1967). Conferir NCM, destinatário e benefício aplicável na NF.
- **Devolução de venda** (CFOP 1.201/2.201): o estabelecimento que recebe a devolução **credita-se** do IPI destacado na nota de venda original (art. 229 do RIPI), anulando o débito da venda.
- **Bonificação, doação e brinde** (CFOP 5.910): é saída, e em regra há incidência de IPI. Não confundir com "reposição".
- **Simples Nacional**: o IPI está dentro do DAS (Anexo II). O IPI na importação é cobrado à parte (art. 13, § 1º, XII, da LC nº 123/2006).

### 5. Entregável
**a) Apuração mensal**
```
APURAÇÃO IPI — MM/AAAA — EMPRESA EXEMPLO INDÚSTRIA LTDA — CNPJ 00.000.000/0001-00

ENTRADAS COM CRÉDITO (CST 00)
NF nº  Fornecedor      NCM        Base       IPI %    IPI
1234   FORNECEDOR A    0000.00.00 50.000     10%      5.000
5678   FORNECEDOR B    0000.00.00 20.000      5%      1.000
TOTAL CRÉDITOS DO MÊS                                  6.000

SAÍDAS TRIBUTADAS (CST 50)
9999   CLIENTE EXEMPLO 0000.00.00 80.000     10%      8.000
TOTAL DÉBITOS DO MÊS                                   8.000

(+) Saldo credor anterior                                500
(=) IPI A RECOLHER = 8.000 − 6.000 − 500 = 1.500 (DARF 5123)
Vencimento: 25/MM+1 (antecipar se não for dia útil)
```
**b) Memória de cálculo** em planilha (ver "Formato de entrega").
**c) DARF 5123** com valor e vencimento.
**d) Checklist**
```
[ ] NCM com 8 dígitos e alíquota da TIPI vigente conferidos
[ ] CSTs corretos (entradas 00–49; saídas 50–99; suspensão = 05/55)
[ ] Suspensão/isenção/imunidade com base legal documentada
[ ] Benefícios conferidos frente à LC nº 224/2025 (redução de 10% desde 01/04/2026)
[ ] Crédito presumido calculado e escriturado, se houver exportação (só para PIS/COFINS cumulativo; aproveitamento de 90% desde 04/2026)
[ ] EFD ICMS/IPI: E520 e E530 batendo com a apuração
[ ] DCTFWeb (MIT) com o débito de IPI igual ao apurado
```

## Erros comuns / pontos de atenção
- Calcular o IPI "por dentro".
- Usar CST errado: 53 é "não tributada" e 55 é "suspensão" (erro frequente).
- Tomar crédito de imobilizado ou de material de uso e consumo.
- Usar TIPI desatualizada.
- Tratar como suspensão o que é isenção (ou o contrário).
- Esquecer a industrialização por encomenda no E520/E530.
- Lançar devolução de venda como débito em vez de crédito.
- Achar que bonificação (5.910) não tem IPI.
- Ignorar a redução de benefícios da LC nº 224/2025 desde 01/04/2026.
- Esquecer que o prazo de pagamento (dia 25) é diferente do prazo da DCTFWeb (último dia útil).

### Casos de borda
- **Importador revendedor**: é equiparado a industrial e recolhe IPI na revenda do produto importado (art. 9º, I, do RIPI). Atacadista comum não recolhe.
- **Drawback integrado (aquisições no mercado interno)**: suspensão também para compras internas (art. 12 da Lei nº 11.945/2009). Conferir o ato concessório.
- **Simples equiparado a industrial**: o IPI segue no DAS; atenção apenas ao IPI na importação.

### Quando escalar
- Recuperação de IPI pago a maior (5 anos) → `recuperacao-creditos-pis-cofins` (lógica de PER/DCOMP).
- Bloco K detalhado → skill de EFD ICMS/IPI.
- Cruzamento ECF × EFD × DCTFWeb → `revisao-fiscal-cruzamento-sped`.
- ICMS-ST interestadual → `calculo-icms-icms-st`.
- Cliente em ZFM → análise específica.

## Perguntas que o usuário costuma fazer
- **"Posso tomar crédito de IPI da máquina que comprei?"** Não. Bem do imobilizado não dá crédito de IPI; só insumos (matéria-prima, produto intermediário e embalagem).
- **"O IPI acaba em 2027?"** As alíquotas vão a zero a partir de 2027, exceto produtos com industrialização incentivada na ZFM. O imposto continua existindo para esses casos.
- **"Se o dia 25 cair no sábado?"** Antecipa para a sexta-feira (último dia útil anterior).

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas a fisco): documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Decreto nº 7.212/2010 (RIPI) — arts. 9º (equiparados), 43 (suspensão), 190 (valor tributável), 226 (créditos), 229 (devolução), 254 (estorno).
- Decreto nº 11.158/2022 (TIPI) e alterações posteriores.
- Lei nº 4.502/1964 — instituição do IPI.
- Constituição Federal, art. 153, § 3º, III — imunidade na exportação.
- Lei nº 9.779/1999, art. 11 — manutenção de crédito em saídas isentas e com alíquota zero.
- Lei nº 9.363/1996 e Lei nº 10.276/2001 — crédito presumido na exportação.
- Lei nº 11.945/2009, art. 12 — drawback integrado (suspensão).
- Lei nº 8.383/1991, art. 52, I, "a" e "c", e §4º (redação da Lei nº 11.933/2009) — prazo de recolhimento.
- Lei nº 10.833/2003, art. 14 — crédito presumido das Leis nº 9.363/1996 e nº 10.276/2001 não se aplica a quem apura PIS/COFINS no não cumulativo.
- Decreto-Lei nº 288/1967 — Zona Franca de Manaus.
- LC nº 87/1996, art. 13, § 2º — IPI na base do ICMS.
- LC nº 123/2006, art. 13, § 1º, XII — IPI na importação para optante do Simples.
- LC nº 224/2025, art. 4º (§1º, V; §2º, II, "c"; §3º, II; §4º, IV), e IN RFB nº 2.305/2025 — redução de 10% dos benefícios federais e limite de 90% dos créditos presumidos.
- IN RFB nº 2.248/2025 — prazo da DCTFWeb.
- EC nº 132/2023 (ADCT, art. 126, III) e LC nº 214/2025 — IPI zero a partir de 2027, exceto ZFM.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
