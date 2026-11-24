---
name: malha-fina-pj-diagnostico
description: "Diagnostica comunicações do fisco a empresas — comunicado de autorregularização ou inconsistência, Termo de Intimação Fiscal (TIF), Auto de Infração, Despacho Decisório de PER/DCOMP e cobrança de débito declarado — da Receita Federal, Sefaz ou prefeitura. Identifica a divergência (SPEDs × DCTFWeb × eSocial × EFD-Reinf), o prazo e a estratégia (retificar, defender ou parcelar) e prepara minuta de resposta e cronograma. Acionar quando o usuário disser \"recebi intimação\", \"termo de intimação\", \"auto de infração\", \"despacho decisório\", \"compensação não homologada\", \"pendência na certidão\", \"CND travada\", \"malha PJ\", \"comunicado da Receita\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Diagnóstico de malha e intimações de pessoa jurídica

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Lê o documento recebido do fisco, identifica o tipo, o tributo, o período, o valor, o fundamento e o prazo, descobre a causa da divergência e propõe a estratégia. Prepara a minuta de resposta (ou o roteiro da impugnação, que fica com o advogado quando exigir tese jurídica) e o cronograma das retificações na ordem certa.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.
> Impugnação de auto de infração com tese jurídica e medidas judiciais são encaminhadas a advogado com OAB.

## Quando usar
- Empresa recebeu intimação, comunicado ou auto da Receita Federal, Sefaz ou prefeitura.
- Pendência que impede a certidão de regularidade fiscal.
- Suspeita de divergência antes de o fisco perceber (verificação preventiva).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Prazo é o ponto mais crítico: registrar a **data da ciência** (abertura da mensagem na Caixa Postal do e-CAC ou fim do prazo de leitura) e calcular o vencimento logo no início.

## Passo a passo (instruções para o agente de IA)

### 1. Identificar o documento
```
Documento                          O que é                                   Prazo
Comunicado de autorregularização   Aviso antes de fiscalização; o            O indicado no comunicado. Corrigir antes
/ inconsistência (malha PJ)        contribuinte ainda é espontâneo            do início do procedimento mantém a
                                                                              espontaneidade (art. 138 do CTN)
Termo de Intimação Fiscal (TIF)    Pede esclarecimentos/documentos;          O fixado no termo.
                                   já é procedimento fiscal                   Prorrogação só a pedido fundamentado,
                                                                              a critério da autoridade
Auto de Infração / Notificação     Lançamento: tributo + multa + juros        30 dias da ciência para impugnar
de Lançamento                                                                 (art. 15 do Decreto nº 70.235/1972)
Despacho Decisório (PER/DCOMP)     Decide restituição/compensação            30 dias para manifestação de inconformidade
                                                                              (art. 74, § 9º, da Lei nº 9.430/1996)
Cobrança de débito declarado       Débito confessado em DCTFWeb e não pago    Pagar, compensar ou parcelar; não cabe
                                                                              impugnação (já é confissão)
```
Depois da ciência do TIF ou do início da fiscalização, o contribuinte **perde a espontaneidade** (art. 7º do Decreto nº 70.235/1972; art. 138, parágrafo único, do CTN (Lei nº 5.172/1966)).

### 2. Causas mais comuns
```
1. Receita ECF × EFD-Contribuições × DCTFWeb
   - receita financeira tratada de forma diferente
   - ICMS (Tema 69) excluído em uma escrituração e não em outra
2. DCTFWeb × eSocial / EFD-Reinf
   - eventos retificados sem reabrir e retransmitir a DCTFWeb
3. DCTFWeb (MIT) × EFD-Contribuições / ECF
   - desde 01/2025 IRPJ, CSLL, PIS, COFINS e IPI são declarados no MIT dentro da DCTFWeb
     (IN RFB nº 2.237/2024); retificar a EFD não corrige o MIT sozinho
4. Compensação não homologada (PER/DCOMP)
   - crédito insuficiente ou sem a retificação da escrituração que o comprova
5. Falta de pagamento de débito confessado
6. Cadastro divergente (endereço, quadro societário, CNAE)
7. Informação de terceiros: tomador informou retenção na EFD-Reinf (R-4020) e o prestador
   não declarou a receita (para anos até 2024, a fonte era a DIRF)
8. Simples Nacional acima do sublimite com ICMS/ISS "por fora" não pago
```

### 3. Entrevista mínima
```
P1: Tipo do documento? Posso ler o PDF?
P2: Tributo, período, valor e fundamento legal indicados pelo fisco?
P3: Data da ciência? (para calcular o prazo)
P4: O cliente concorda com a divergência ou tem prova em contrário?
P5: Procuração eletrônica do e-CAC ativa para o contador?
```

### 4. Estratégia (decidida com o cliente)
- **(a) Retificar e pagar a diferença**: o erro é da empresa e não há defesa.
- **(b) Defesa documental**: o fisco partiu de premissa errada e há prova.
- **(c) Pagar ou parcelar** (skill `parcelamento-receita-federal`): débito correto, sem caixa. Em auto de infração, pagar ou parcelar dentro do prazo de impugnação dá redução da multa de ofício (art. 6º da Lei nº 8.218/1991: 50% no pagamento em 30 dias; 40% no parcelamento).

### 5. Multas — o que contestar
- Multa de ofício: 75% (art. 44, I, da Lei nº 9.430/1996).
- **Multa qualificada** (sonegação, fraude, conluio): desde a Lei nº 14.689/2023 é **100%**, e 150% só na reincidência (art. 44, § 1º, VI, e § 1º-A, da Lei nº 9.430/1996). Não cabe sem individualização e prova do dolo (§ 1º-C). Fatos anteriores: a redução retroage (art. 106, II, "c", do CTN). STF, Tema 863 (RE 736.090, julgado em 03/10/2024): até lei complementar sobre o tema, a multa qualificada fica limitada a 100% do débito, podendo chegar a 150% na reincidência (art. 44, § 1º-A, da Lei nº 9.430/1996).
- Multa agravada (não atendimento à intimação): a multa aumenta em metade (art. 44, § 2º).
- Multa de mora (pagamento espontâneo em atraso): 0,33% ao dia, até 20% (art. 61 da Lei nº 9.430/1996).
- **Compensação não homologada**: a multa isolada de 50% do art. 74, § 17, da Lei nº 9.430/1996 foi declarada inconstitucional pelo STF (Tema 736, RE 796.939). Continua cabendo multa isolada de 75%, majorada nos casos de falsidade (art. 18, § 2º, da Lei nº 10.833/2003, combinado com o art. 44, I e § 1º, da Lei nº 9.430/1996), quando a compensação é **considerada não declarada** (art. 18 da Lei nº 10.833/2003).

### 6. Modelo de resposta a TIF
```
À Delegacia da Receita Federal do Brasil em ____

Contribuinte: EMPRESA EXEMPLO LTDA — CNPJ 00.000.000/0001-00
Termo de Intimação Fiscal nº ____ — Período: ____

Em atendimento ao Termo de Intimação:

I. DOS FATOS
[O que a Receita questiona, com valores]

II. ANÁLISE
A divergência de R$ ____ decorre de [causa identificada].

III. DOCUMENTOS ANEXOS
3.1 EFD-Contribuições retificadora — competências ____ (recibos ____)
3.2 DCTFWeb retificadora — recibo ____
3.3 DARF complementar — código ____ — R$ ____ — pago em ____
3.4 Memória de cálculo

IV. PEDIDO
Requer-se o acolhimento dos esclarecimentos e o encerramento da intimação.

Local, data.
Representante legal / procurador
Contador ____ CRC ____
```

### 7. Pedido de prorrogação de prazo
Não há artigo que garanta a prorrogação: é pedido fundamentado, decidido pela autoridade fiscal. Protocolar **antes** do vencimento e continuar trabalhando como se não fosse deferido.
```
Requer-se a prorrogação, por ____ dias, do prazo fixado no Termo de Intimação Fiscal nº ____,
em razão do volume de documentos do período de ____ a ____, em atenção ao contraditório e à
ampla defesa (art. 5º, LV, da Constituição Federal) e ao art. 3º da Lei nº 9.784/1999.
```

### 8. Entregáveis
**a) Documento decifrado** (tributo, período, valor, fundamento, data da ciência, prazo final).
**b) Plano de ação**
```
Estratégia: ____            Prazo final: __/__/__
[ ] Semana 1: cruzar escriturações (skill revisao-fiscal-cruzamento-sped) e achar a causa
[ ] Semana 2: retificar eSocial/EFD-Reinf (se aplicável) e depois a DCTFWeb
[ ] Semana 3: retificar EFDs, ECD e ECF, na ordem origem → destino
[ ] Semana 3: pagar a diferença com Selic
[ ] Semana 4: protocolar a resposta no e-CAC (antes do prazo)
```
**c) Minuta de resposta** (TIF) ou roteiro técnico da impugnação (auto), para o advogado quando houver tese.
**d) Cronograma** com data de cada ação.
**e) Checklist**
```
[ ] Documento lido: prazo, valor, fundamento mapeados
[ ] Escriturações e declarações do período coletadas
[ ] Causa raiz identificada
[ ] Estratégia escolhida (retificar / defender / pagar ou parcelar)
[ ] Retificações feitas na ordem certa
[ ] Diferença paga (se houver)
[ ] Resposta protocolada no e-CAC
[ ] Acompanhamento da decisão agendado
[ ] Cliente ciente por escrito; procuração válida
[ ] Honorários contratados (cláusula de êxito, se cabível)
```

## Erros comuns / pontos de atenção
- Perder o prazo: no TIF, gera multa agravada; no auto, perde a fase administrativa.
- Retificar uma escrituração sem alinhar DCTFWeb (MIT) e ECF: cria nova divergência.
- Pagar a mais por insegurança: só volta via PER/DCOMP, com demora.
- Aceitar o auto sem análise: pode ser parcialmente improcedente (decadência, base errada, multa qualificada sem prova de dolo).
- Responder sem procuração eletrônica válida.
- Impugnar auto sem fundamentação: a DRJ (Delegacia de Julgamento) nega.

**Casos de borda**
- **Decadência**: 5 anos (art. 150, § 4º, do CTN com pagamento; art. 173, I, sem pagamento ou com dolo). Lançamento fora do prazo: crédito extinto (art. 156, V, do CTN).
- **Compensação não homologada**: ver item 5 (Tema 736).
- **Empresa em recuperação judicial**: parcelamento especial em até 120 meses e transação (arts. 10-A e 10-C da Lei nº 10.522/2002, incluídos pela Lei nº 14.112/2020).
- **Intimação estadual ou municipal**: prazos e multas seguem a lei do ente; ler a legislação local.

## Perguntas que o usuário costuma fazer
- **"Posso só retificar e ignorar o TIF?"** Não. Depois do TIF a retificação não é espontânea; é preciso responder ao termo, juntando a retificação se for o caso.
- **"A multa de 150% ainda existe?"** Só na reincidência. A regra geral da qualificada é 100% (Lei nº 14.689/2023).
- **"Compensação não homologada gera multa?"** A multa isolada de 50% caiu (Tema 736). Mas a compensação considerada não declarada tem multa de 75%.

## Formato de entrega
- Cálculos, apurações e conciliações: sempre planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): sempre documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Decreto nº 70.235/1972 (Processo Administrativo Fiscal) — art. 7º (início do procedimento), art. 15 (impugnação em 30 dias), art. 23 (formas de intimação e data da ciência).
- Lei nº 5.172/1966 (CTN) — art. 106, II, "c" (retroatividade benigna), art. 138 (denúncia espontânea), arts. 150, § 4º, 156, V, 173 e 174.
- Lei nº 9.430/1996 — art. 44 (multas de ofício, qualificada e agravada, com redação da Lei nº 14.689/2023), art. 61 (multa de mora), art. 74 (compensação; § 9º manifestação de inconformidade).
- Lei nº 14.689/2023 — multa qualificada de 100% (150% na reincidência).
- STF, RE 736.090 (Tema 863) — limite da multa qualificada; STF, RE 796.939 (Tema 736) — inconstitucionalidade da multa isolada por compensação não homologada.
- Lei Complementar nº 225/2026 — Código de Defesa do Contribuinte (direitos do contribuinte no procedimento fiscal; ler o texto antes de invocar um direito específico).
- Lei nº 10.833/2003 — art. 18 (multa isolada na compensação não declarada).
- Lei nº 8.218/1991 — art. 6º (redução da multa de ofício).
- Lei nº 9.784/1999 — processo administrativo federal (aplicação subsidiária).
- Lei nº 10.522/2002 — arts. 10-A e 10-C (empresa em recuperação judicial), incluídos pela Lei nº 14.112/2020.
- IN RFB nº 2.237/2024 — DCTFWeb com MIT (fatos a partir de 01/2025).
- Constituição Federal — art. 5º, LV (contraditório e ampla defesa).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
