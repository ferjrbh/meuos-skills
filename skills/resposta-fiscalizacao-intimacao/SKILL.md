---
name: resposta-fiscalizacao-intimacao
description: "Prepara a resposta a fiscalizações e cobranças federais (e, no que couber, estaduais e municipais) — termo de intimação fiscal (prazo fixado no termo, em geral 20 dias), auto de infração (impugnação em 30 dias à DRJ — art. 15 do Decreto nº 70.235/1972), despacho decisório de PER/DCOMP (manifestação de inconformidade em 30 dias — art. 74 da Lei nº 9.430/1996), recurso voluntário ao CARF (30 dias). Levanta decadência (arts. 150, § 4º, e 173 do CTN), prescrição (art. 174 do CTN), denúncia espontânea (art. 138 do CTN, Súmula 360 do STJ) e a multa qualificada atual (100%, ou 150% na reincidência — Lei nº 14.689/2023). Acionar quando o usuário disser \"intimação\", \"termo de intimação\", \"TIF\", \"auto de infração\", \"impugnação\", \"despacho decisório\", \"manifestação de inconformidade\", \"fiscalização\", \"CARF\", \"prorrogar prazo\"."
version: 1.1
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Resposta a fiscalização e intimação

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Decifra o documento recebido do fisco (tipo, tributo, período, valor, fundamento e prazo), define a estratégia (atender, retificar, impugnar, pagar ou parcelar) e redige a minuta da resposta com fundamentação, cronograma e checklist de protocolo.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Recebimento de termo de início, termo de intimação, auto de infração, notificação de lançamento, despacho decisório ou aviso de cobrança.
- Pedido de prorrogação de prazo.
- Preparação de impugnação, manifestação de inconformidade ou recurso voluntário.
- Pendência de malha de pessoa física: usar `diagnosticar-malha-fina-pf`. Divergências entre SPEDs: `revisao-fiscal-cruzamento-sped`.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Entregar ao fisco só o que foi pedido (escopo do termo); documentos com dados de terceiros (empregados, clientes) vão com o mínimo necessário.
- Defesa na esfera administrativa pode ser assinada pelo contribuinte ou procurador. Ação judicial (mandado de segurança, anulatória, embargos) exige advogado: encaminhar a um advogado.

## Passo a passo (instruções para o agente de IA)

### 1. Tipos de documento e prazos (esfera federal)
```
Documento                          O que é                                  Prazo
Termo de início / TDPF             Abre o procedimento fiscal; tira a       —
                                   espontaneidade (art. 7º do Decreto
                                   nº 70.235/1972)
Termo de intimação fiscal          Pede documentos/esclarecimentos          o fixado no termo
                                                                            (usual: 20 dias)
Comunicado / carta de              Alerta preventivo (malha), sem           o indicado no documento
inconsistência                     lançamento
Auto de infração / notificação     Lançamento de tributo + multa            30 dias da ciência para
de lançamento                                                               impugnar (art. 15 do
                                                                            Decreto nº 70.235/1972)
Despacho decisório (PER/DCOMP)     Não homologa compensação ou nega         30 dias para pagar ou
                                   restituição                              apresentar manifestação
                                                                            de inconformidade (art. 74,
                                                                            §§ 7º e 9º, da Lei nº 9.430/1996)
Acórdão da DRJ desfavorável        Decisão de 1ª instância                  30 dias para recurso
                                                                            voluntário ao CARF (art. 33
                                                                            do Decreto nº 70.235/1972)
Aviso de cobrança                  Débito declarado e não pago              pagar, parcelar ou
                                                                            demonstrar pagamento
```
Estados e municípios têm leis próprias de processo administrativo: conferir prazos na legislação do ente.

### 2. Rito federal (Decreto nº 70.235/1972)
```
Termo de início → termos de intimação → Termo de Verificação Fiscal → Auto de Infração
→ Impugnação (30 dias; arts. 15 e 16) → DRJ (1ª instância)
→ Recurso voluntário ao CARF (30 dias; art. 33)
→ Recurso especial à CSRF (divergência entre turmas)
Sem impugnação no prazo: revelia e cobrança (art. 21).
```

### 3. Entrevista mínima
```
Q1: Tipo do documento, número e DATA DA CIÊNCIA (Domicílio Tributário Eletrônico/e-CAC,
    correio ou pessoal)?
Q2: Tributo, período, valor e fundamento legal indicados pelo fisco?
Q3: A causa já é conhecida (cruzamento de SPED, DCTFWeb, EFD-Reinf, eSocial)?
Q4: Estratégia preliminar: atender, retificar, impugnar, pagar com redução ou parcelar?
Q5: Procuração eletrônica ativa no e-CAC (e nos portais estadual/municipal)?
```

### 4. Teses e cálculos de defesa
**Decadência (prazo para o fisco lançar)**
- Tributo lançado por homologação **com pagamento** (ainda que parcial) e sem dolo, fraude ou simulação: 5 anos contados do fato gerador (art. 150, § 4º, do CTN — Lei nº 5.172/1966).
- **Sem pagamento**, ou com dolo/fraude/simulação: 5 anos contados do 1º dia do exercício seguinte àquele em que o lançamento poderia ser feito (art. 173, I, do CTN; Súmula 555 do STJ).
- Auto lavrado depois desse prazo: crédito extinto (art. 156, V, do CTN).

**Prescrição (prazo para cobrar)**: 5 anos da constituição definitiva do crédito (art. 174 do CTN).

**Denúncia espontânea (art. 138 do CTN)**: pagamento integral do tributo + juros ANTES de qualquer procedimento fiscal afasta a multa (de ofício e de mora, conforme jurisprudência do STJ). Não se aplica a tributo declarado e pago fora do prazo (Súmula 360 do STJ). Se o fisco ficar mais de 60 dias sem praticar ato no procedimento, a espontaneidade é recuperada (art. 7º, § 2º, do Decreto nº 70.235/1972).

**Multas de ofício (art. 44 da Lei nº 9.430/1996, com redação da Lei nº 14.689/2023)**
```
Regra geral (falta de pagamento, declaração inexata) ............... 75%
Qualificada (sonegação, fraude ou conluio — arts. 71 a 73 da
  Lei nº 4.502/1964) ............................................... 100%
Qualificada na reincidência ......................................... 150%
Isolada (carnê-leão ou estimativa não recolhidos) .................. 50%
```
Defesa usual: afastar a qualificação demonstrando ausência de dolo (a multa volta a 75%). Não existe redução "para 20%": 20% é o teto da multa de MORA (art. 61 da Lei nº 9.430/1996).

**Redução da multa de ofício por pagamento ou parcelamento** (art. 6º da Lei nº 8.218/1991): 50% se pago em 30 dias da ciência do auto; 40% se parcelado nesse prazo; percentuais menores após a decisão de 1ª instância. Comparar com a chance de êxito na impugnação.

**Voto de qualidade no CARF** (Decreto nº 70.235/1972, com redação da Lei nº 14.689/2023):
- julgamento resolvido pelo voto de qualidade a favor da Fazenda: ficam excluídas as multas e cancelada a representação fiscal para fins penais (art. 25, § 9º-A);
- se o contribuinte manifestar a intenção de pagar em 90 dias, ficam excluídos os juros de mora até a data do acordo; o pagamento pode ser em até 12 parcelas mensais, com uso de prejuízo fiscal e base negativa da CSLL (inclusive de controladora, controlada ou sob controle comum) e de precatórios; se as parcelas não forem pagas, os juros voltam (art. 25-A);
- sem manifestação para pagar, o crédito vai à dívida ativa em até 90 dias, sem o encargo do Decreto-Lei nº 1.025/1969; a regra vale só para a parcela controvertida decidida pelo voto de qualidade.

**Multa qualificada — reincidência e dolo** (art. 44, §§ 1º-A e 1º-C, da Lei nº 9.430/1996): reincidência = nova conduta dos arts. 71 a 73 da Lei nº 4.502/1964 em até 2 anos contados do lançamento anterior; a qualificação não se aplica sem conduta dolosa comprovada ou com absolvição penal de mérito.

**Outras teses**: nulidade (vício de competência, falta de motivação, cerceamento de defesa — art. 59 do Decreto nº 70.235/1972); erro de fato; precedentes vinculantes (STF/STJ em repercussão geral/repetitivos) e súmulas do CARF; tributo já confessado/parcelado lançado em duplicidade.

### 5. Modelo — resposta a termo de intimação
```
À Receita Federal do Brasil — [unidade]
EMPRESA EXEMPLO LTDA — CNPJ __ — Termo de Intimação nº __ — Período __

I. DOS FATOS — o que foi solicitado e quando houve a ciência.
II. DOS DOCUMENTOS APRESENTADOS — lista numerada, cada item com explicação curta.
III. DOS ESCLARECIMENTOS — resposta objetiva a cada item do termo.
IV. DA FUNDAMENTAÇÃO — normas aplicáveis (sempre lei + artigo) e soluções de consulta.
V. DO PEDIDO — receber os documentos, considerar atendida a intimação e encerrar a
   diligência sem lançamento.
[Local, data] — [Contribuinte / procurador]
```

### 6. Modelo — impugnação de auto de infração (DRJ)
```
ILUSTRÍSSIMO(A) SENHOR(A) DELEGADO(A) DA DELEGACIA DE JULGAMENTO DA RECEITA FEDERAL DO BRASIL

EMPRESA EXEMPLO LTDA, CNPJ __, apresenta IMPUGNAÇÃO ao Auto de Infração nº __ (processo __):

I. DA TEMPESTIVIDADE — ciência em __/__/__; protocolo dentro de 30 dias (art. 15 do
   Decreto nº 70.235/1972).
II. DOS FATOS — resumo.
III. DAS RAZÕES
   III.1 Preliminar de nulidade (art. 59 do Decreto nº 70.235/1972), se houver.
   III.2 Decadência (art. 150, § 4º, ou art. 173, I, do CTN), se houver.
   III.3 Mérito — tese a tese, com lei, súmula e precedente.
   III.4 Multa — afastamento da qualificação (art. 44, § 1º, da Lei nº 9.430/1996).
IV. DAS PROVAS — documentos anexos numerados; pedido de perícia/diligência, se for o caso,
   com quesitos (art. 16, IV, do Decreto nº 70.235/1972).
V. DO PEDIDO — acolher a impugnação e cancelar o lançamento; subsidiariamente, afastar
   a multa qualificada.
[Local, data] — [Contribuinte / procurador]
```
Toda matéria e prova devem ir na impugnação: o que não for contestado é considerado não impugnado (art. 17 do Decreto nº 70.235/1972), e prova posterior só nas hipóteses do art. 16, § 4º.

### 7. Pedido de prorrogação (termo de intimação)
```
Solicita-se a prorrogação, por __ dias, do prazo fixado no Termo de Intimação nº __, em razão
do volume de documentos do período __ (descrever), comprometendo-se o contribuinte a entregar
parcialmente os itens já disponíveis até __/__/__.
```
A prorrogação é decisão do auditor (não há direito automático). Pedir ANTES do vencimento e entregar o que já houver. Prazo de impugnação de auto de infração é legal e **não** se prorroga.

### 8. Entregável obrigatório
a) Análise do documento (tipo, tributo, período, valor, fundamento, data de ciência, prazo final).
b) Plano estratégico (atender / retificar / impugnar / pagar com redução / parcelar / recorrer), com comparação de custo.
c) Minuta (modelos acima).
d) Cronograma com data de cada ação e prazo fatal destacado.
e) Documentos anexos numerados.
f) Protocolo (e-CAC — processo digital; nos entes locais, conforme o portal).
g) Checklist:
```
[ ] Data de ciência confirmada e prazo final calculado
[ ] Tributo, período, valor e fundamento mapeados
[ ] Decadência verificada (art. 150, § 4º × art. 173, I, do CTN)
[ ] Causa raiz identificada
[ ] Decisão: prorrogar / atender / impugnar / pagar / parcelar
[ ] Minuta com fundamentação (lei + artigo)
[ ] Provas numeradas
[ ] Protocolo confirmado e comprovante salvo
[ ] Acompanhamento do processo agendado
[ ] Cliente ciente por escrito da estratégia e dos riscos
```

## Erros comuns / pontos de atenção
- Perder o prazo: revelia (art. 21 do Decreto nº 70.235/1972).
- Impugnar sem fundamento ou sem prova: a DRJ mantém o lançamento.
- Aceitar a multa qualificada sem discutir o dolo.
- Usar percentuais antigos (150% como regra da qualificada, ou "redução para 20%").
- Achar que denúncia espontânea vale depois do termo de início, ou para tributo declarado pago em atraso.
- Esquecer prova na impugnação (preclusão).
- Procuração eletrônica sem o serviço de processos digitais.
- Não guardar o histórico (e-mails, mensagens) do caso com o cliente.

## Casos de borda
- **Débito já parcelado ou confessado autuado de novo**: pedir o cancelamento do lançamento em duplicidade.
- **Decadência operada**: preliminar na impugnação.
- **Cobrança já inscrita ou execução fiscal**: advogado parceiro (embargos, exceção de pré-executividade).
- **Código de Defesa do Contribuinte (Lei Complementar nº 225/2026, de 08/01/2026, DOU de 09/01/2026)**: usar na fundamentação da resposta, entre outros, o direito de ser intimado e de impugnar atos que imponham deveres ou sanções e de recorrer ao menos uma vez (art. 4º), a vedação de exigir pagamento, garantia ou custas prévias para exercer esses direitos, salvo previsão em lei (art. 4º, § 2º), a presunção de boa-fé do contribuinte (art. 3º, VII) e o direito de autorregularizar tributos e obrigações acessórias antes da lavratura do auto de infração (art. 3º, XX). A lei também cria a figura do **devedor contumaz** (art. 11; na esfera federal, créditos irregulares a partir de R$ 15.000.000,00 e acima de 100% do patrimônio conhecido, com inadimplência reiterada), com notificação prévia e 30 dias para regularizar ou se defender, com efeito suspensivo (art. 12, III). O devedor contumaz fica sujeito às medidas do art. 13 (por exemplo, impedimento de benefícios fiscais e de licitações, e inaptidão cadastral), e editais de transação podem excluí-lo (ex.: Edital de Transação Conjunto PGFN/RFB nº 4/2026). Conferir no texto da lei o dispositivo exato antes de citar na peça.

## Perguntas que o usuário costuma fazer
- **"Posso pedir mais prazo para o auto de infração?"** Não: os 30 dias são legais. Mais prazo só em termo de intimação, a critério do auditor.
- **"Se eu pagar agora, a multa cai?"** No auto de infração, paga em 30 dias da ciência, a multa de ofício cai 50% (art. 6º da Lei nº 8.218/1991).
- **"Contador pode assinar a impugnação?"** Na esfera administrativa, o procurador constituído pode; na judicial, só advogado.

## Quando escalar
- CARF com tese complexa, ação judicial → advogado parceiro com OAB
- Pagar ou parcelar → `parcelamento-receita-federal`
- Recuperação de créditos → `recuperacao-creditos-pis-cofins`
- Cruzamento para achar a causa → `revisao-fiscal-cruzamento-sped`

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Decreto nº 70.235/1972 (processo administrativo fiscal) — art. 7º (espontaneidade), arts. 15 a 17 (impugnação), art. 21 (revelia), art. 33 (recurso voluntário), art. 59 (nulidades).
- Lei nº 5.172/1966 (CTN) — art. 138 (denúncia espontânea), art. 150, § 4º, e art. 173 (decadência), art. 156, V (extinção), art. 174 (prescrição).
- Lei nº 9.430/1996 — art. 44 (multas de ofício, com redação da Lei nº 14.689/2023), art. 61 (multa de mora), art. 74 (PER/DCOMP, manifestação de inconformidade).
- Lei nº 14.689/2023 — multa qualificada de 100%/150% e voto de qualidade no CARF.
- Lei nº 8.218/1991 — art. 6º (redução da multa de ofício).
- Lei nº 4.502/1964 — arts. 71 a 73 (sonegação, fraude, conluio).
- Lei nº 9.784/1999 — processo administrativo federal (aplicação subsidiária).
- Lei nº 13.988/2020 — transação.
- Súmulas 360 e 555 do STJ.
- Lei Complementar nº 225/2026 — Código de Defesa do Contribuinte (arts. 3º e 4º, direitos e garantias; arts. 11 a 15, devedor contumaz).
- Decreto nº 70.235/1972 — art. 25, § 9º-A, e art. 25-A (voto de qualidade, incluídos pela Lei nº 14.689/2023).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
