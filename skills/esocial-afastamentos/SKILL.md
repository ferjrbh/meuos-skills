---
name: esocial-afastamentos
description: "Especialista em afastamentos no eSocial — S-2230 com o motivo correto da Tabela 18 (01 acidente/doença do trabalho, 03 doença comum, 15 férias, 17 licença-maternidade, 18 prorrogação Empresa Cidadã etc.) e CAT pelo S-2210 (até o 1º dia útil seguinte ao acidente; imediata em caso de morte). Cobre os 15 primeiros dias pagos pela empresa, benefício do INSS a partir do 16º dia, soma de atestados da mesma doença em 60 dias, quando o S-2230 é obrigatório ou facultativo, estabilidade acidentária de 12 meses, licença-maternidade 120/180 dias, nova licença-paternidade a partir de 2027 e ASO de retorno. Use quando o usuário receber atestado, falar de CAT, S-2210, S-2230, auxílio por incapacidade temporária, B31, B91, licença-maternidade ou paternidade, alta médica. Entrega: S-2230 estruturado + CAT se acidente + cálculo dos 15 dias + alertas."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# eSocial — Afastamentos (S-2230) e CAT (S-2210)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Classifica o afastamento do empregado (doença comum, acidente de trabalho, maternidade, férias, licenças), escolhe o código da Tabela 18, diz se o envio é obrigatório, calcula os dias que a empresa paga e organiza os eventos S-2230 e, no acidente, a CAT (S-2210), com prazos e alertas de estabilidade.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Atestado médico, acidente de trabalho, doença ocupacional.
- Licença-maternidade, prorrogação Empresa Cidadã, licença não remunerada, férias no eSocial.
- Retorno do afastamento (término do S-2230 e ASO de retorno).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Atestado, CID e laudo são **dados de saúde (dado sensível, art. 5º, II, da Lei nº 13.709/2018 (LGPD))**: não transcrever o CID na resposta nem em arquivos de trabalho além do campo exigido pelo evento.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Tabela 18 — motivos mais usados (leiaute S-1.3)
```
Cód  Motivo
01   Acidente/doença do trabalho
03   Acidente/doença NÃO relacionada ao trabalho (doença comum)
06   Aposentadoria por invalidez (incapacidade permanente)
07   Licença para acompanhamento de membro da família enfermo
15   Gozo de férias ou recesso
16   Licença remunerada (lei, liberalidade da empresa ou CCT/ACT)
17   Licença-maternidade
18   Licença-maternidade — prorrogação de 60 dias (Empresa Cidadã, Lei nº 11.770/2008)
19   Licença-maternidade — aborto não criminoso
20   Licença-maternidade — cônjuge sobrevivente, adoção ou guarda judicial
21   Licença não remunerada ou suspensão por obrigação legal incompatível com o serviço
24   Mandato sindical
25   Mulher vítima de violência (art. 9º, § 2º, II, da Lei nº 11.340/2006 — Lei Maria da Penha)
27   Suspensão do contrato para qualificação (art. 476-A da CLT)
29   Serviço militar obrigatório
35   Licença-maternidade — antecipação/prorrogação por atestado médico
53   Afastamento da gestante/lactante de atividade insalubre sem local salubre (art. 394-A, § 3º, da CLT)
```
Conferido na Tabela 18 do Anexo I dos leiautes S-1.3 (NT S-1.3 nº 07/2026, rev. 20/10/2026, gov.br/esocial). Antes de transmitir, conferir sempre a validade do código na versão do leiaute em produção.

**Licença-paternidade (Lei nº 15.371/2026, em vigor a partir de 01/01/2027):** a licença passa a 10 dias em 2027 e 15 dias em 2028; os 20 dias a partir de 2029 dependem do cumprimento da meta fiscal prevista no art. 11 da lei. A lei cria o salário-paternidade, pago pela empresa ao empregado e compensado conforme o art. 248 da Constituição e o regulamento (arts. 73-A a 73-H da Lei nº 8.213/1991, incluídos pela Lei nº 15.371/2026). A Tabela 18 traz códigos próprios (46 a 52) válidos a partir de 01/01/2027. **Até 31/12/2026 vale a regra atual:** 5 dias (art. 10, § 1º, do ADCT), mais 15 dias pela Empresa Cidadã (Lei nº 11.770/2008). Antes de processar a primeira licença de 2027, conferir se já saiu o regulamento da compensação.

### 2. Prazos e obrigatoriedade (MOS S-1.3)
```
CAT (S-2210)  Até o 1º dia útil seguinte ao acidente; em caso de morte, imediatamente
              (art. 22 da Lei nº 8.213/1991).

S-2230 — QUANDO É OBRIGATÓRIO (empregados, categorias 1XX)
  Motivo 01 (acidente/doença do trabalho): sempre, qualquer duração.
  Motivo 03 (doença comum): só quando
    a) dura mais de 15 dias; ou
    b) somados os afastamentos pela mesma doença em 60 dias, passa de 15 dias; ou
    c) ocorre em até 60 dias do retorno de afastamento anterior pela mesma doença que
       gerou benefício do INSS.
    Nos demais casos (atestado curto, sem soma), o envio é FACULTATIVO.
  Motivo 15 (férias), 17/18/19/20/35 (maternidade): obrigatório.

S-2230 — PRAZOS
  Acidente/doença do trabalho de até 15 dias: até o dia 15 do mês seguinte.
  Acidente/doença (do trabalho ou não) com mais de 15 dias: até o 16º dia do afastamento.
  Mesma doença comum em 60 dias somando mais de 15 dias: cada afastamento, até o dia
    em que se completam 16 dias de afastamento.
  Novo afastamento em até 60 dias do retorno de benefício pela mesma doença: no 1º dia
    do novo afastamento.
  Demais afastamentos (férias, licenças): até o dia 15 do mês seguinte.
  Término do afastamento: até o dia 15 do mês seguinte ao do retorno.
  Prazo em dia não útil: posterga para o 1º dia útil seguinte.
```
O eSocial não aceita afastamentos simultâneos: para iniciar um novo motivo (ex.: parto durante as férias), informar antes o término do afastamento anterior. Férias podem ser informadas com até 60 dias de antecedência.

### 3. Entrevista mínima
```
Q1: Trabalhador (matrícula) + data de início + duração prevista + motivo?
Q2: É acidente ou doença DO TRABALHO? (se sim: CAT obrigatória)
Q3: Atestado com médico, CRM e dias? Houve outro atestado da mesma doença nos últimos 60 dias?
Q4: A empresa aderiu ao Programa Empresa Cidadã (Lei nº 11.770/2008)?
Q5: PCMSO em dia? (ASO de retorno se afastamento ≥ 30 dias por doença ou acidente — NR-7)
```

### 4. Acidente ou doença do trabalho
1. CAT pelo S-2210 até o 1º dia útil seguinte (morte: imediata). A falta gera multa entre o limite mínimo e o máximo do salário de contribuição (art. 22 da Lei nº 8.213/1991).
2. Empresa paga os 15 primeiros dias (art. 60, § 3º, da Lei nº 8.213/1991).
3. Do 16º dia em diante: benefício acidentário do INSS (espécie B91).
4. S-2230 com motivo 01, qualquer que seja a duração.
5. FGTS continua sendo depositado durante o afastamento acidentário (art. 15, § 5º, da Lei nº 8.036/1990).
6. Estabilidade de 12 meses após a cessação do auxílio-doença acidentário (art. 118 da Lei nº 8.213/1991).

### 5. Doença comum
1. Até 15 dias: empresa paga (art. 60, § 3º, da Lei nº 8.213/1991); S-2230 motivo 03 facultativo (salvo soma em 60 dias, item 2).
2. Mais de 15 dias: empresa paga 15; o INSS paga a partir do 16º (B31). S-2230 obrigatório até o 16º dia.
3. Afastamentos pela mesma doença em até 60 dias: somam para o 16º dia; a empresa não paga novos 15 dias (art. 75 do Decreto nº 3.048/1999).
4. Do 16º dia em diante: contrato suspenso, sem salário e sem FGTS.
5. ASO de retorno se o afastamento for igual ou maior que 30 dias (NR-7).

### 6. Licença-maternidade
- 120 dias (art. 392 da CLT; art. 7º, XVIII, da Constituição) — motivo 17; +60 dias pela Empresa Cidadã (Lei nº 11.770/2008) — motivo 18.
- Salário-maternidade: a empresa paga e compensa com as contribuições previdenciárias incidentes sobre a folha (art. 72, § 1º, da Lei nº 8.213/1991), via DCTFWeb.
- Incidências: a contribuição PATRONAL sobre o salário-maternidade foi declarada inconstitucional pelo STF (Tema 72, RE 576.967); a contribuição da empregada continua devida (o salário-maternidade é salário de contribuição — art. 28, § 2º, da Lei nº 8.212/1991) e o FGTS também (art. 28, IV, do Decreto nº 99.684/1990). Parametrizar a rubrica na S-1010 com o código de incidência próprio de salário-maternidade indicado no MOS e conferir se o sistema da folha exclui a parcela patronal na DCTFWeb.
- Prorrogação Empresa Cidadã: os 60 dias são pagos pela empresa; a dedução no IRPJ vale só para o Lucro Real (art. 5º da Lei nº 11.770/2008).
- Estabilidade da gestante: da confirmação da gravidez até 5 meses após o parto (art. 10, II, "b", do ADCT).

### 7. Entregável
**a) S-2230 estruturado** (ilustrativo — o arquivo real é gerado pelo sistema de folha conforme o XSD vigente):
```
Evento: S-2230 (afastamento temporário)
  Trabalhador: CPF ___ | matrícula ___
  Início: data do efetivo afastamento
  Motivo: código da Tabela 18 (ex.: 03)
  Mesmo motivo de afastamento anterior em 60 dias? S/N
  (dados do atestado conforme leiaute: emitente, CRM/UF)
  Término (envio posterior): último dia afastado (não a data do retorno)
```
**b) CAT (S-2210)**, se acidente — evento separado, no prazo.
**c) Cálculo dos 15 dias pagos pela empresa** (salário/30 × dias) + aviso ao cliente: "O INSS assume a partir do 16º dia."
**d) Alerta de estabilidade:** se motivo 01 com B91: "Estabilidade de 12 meses após a alta (art. 118 da Lei nº 8.213/1991). Não demitir sem justa causa."
**e) Checklist**
```
[ ] Atestado/CAT arquivado (acesso restrito — dado de saúde)
[ ] Código da Tabela 18 conferido
[ ] Envio obrigatório ou facultativo verificado (item 2)
[ ] S-2210 no prazo (se acidente)
[ ] S-2230 no prazo
[ ] 15 primeiros dias pagos na folha
[ ] Soma de atestados em 60 dias verificada
[ ] Retorno: término no S-2230 + ASO de retorno (≥ 30 dias) + S-2220
[ ] Estabilidade registrada (acidente / gestante)
```

## Erros comuns / pontos de atenção
- CAT fora do prazo: o prazo é o 1º dia útil seguinte ao acidente, e a multa varia entre o limite mínimo e o máximo do salário de contribuição.
- Usar código inexistente para doença comum: o código correto é 03 (B31 e B91 são espécies de benefício do INSS, não códigos da Tabela 18).
- Não somar atestados da mesma doença em 60 dias.
- Esquecer o FGTS no afastamento acidentário (é devido).
- Informar o término com a data do retorno (o correto é o último dia afastado).
- Suspensão disciplinar por mais de 30 dias consecutivos equivale a dispensa injusta (art. 474 da CLT); a suspensão disciplinar não é informada no S-2230.
- Empresa Cidadã sem adesão formal ao programa.

## Casos especiais
- **Doença ocupacional** (ex.: LER/DORT): equiparada a acidente do trabalho (art. 20 da Lei nº 8.213/1991) — CAT, B91 e estabilidade.
- **Aposentadoria por invalidez:** motivo 06; contrato suspenso, não rescindido (art. 475 da CLT).
- **Estagiário:** não é empregado; segue as regras do S-2300 e do termo de compromisso.

## Quando escalar
- Folha do mês com afastamento → `folha-pagamento-mensal`
- Eventos periódicos → `esocial-eventos-periodicos`
- Discussão judicial sobre estabilidade → parceiro advogado com OAB (atividade privativa).

## Perguntas que o usuário costuma fazer
- **"Atestado de 3 dias precisa de S-2230?"** Doença comum de até 15 dias, sem outro atestado da mesma doença nos 60 dias anteriores: o envio é facultativo. Se for acidente ou doença do trabalho, é obrigatório (até o dia 15 do mês seguinte).
- **"Dois atestados de 10 dias da mesma doença?"** Somam 20 dias em 60: a empresa paga só até o 15º dia e o INSS assume; cada afastamento vai no S-2230 até o dia em que se completam 16 dias.

## Base legal usada nesta skill
- Lei nº 8.213/1991 — arts. 19 e 20 (acidente e doença do trabalho), art. 22 (CAT e multa), art. 60, § 3º (15 primeiros dias), art. 72, § 1º (salário-maternidade e compensação), arts. 73-A a 73-H (salário-paternidade, a partir de 2027), art. 118 (estabilidade acidentária).
- Lei nº 8.212/1991 — art. 28, § 2º (salário-maternidade é salário de contribuição).
- STF — Tema 72 (RE 576.967): contribuição patronal sobre o salário-maternidade.
- Decreto nº 3.048/1999 — art. 75 (mesma doença em 60 dias).
- CLT (Decreto-Lei nº 5.452/1943) — art. 392 (licença-maternidade), art. 394-A (gestante e lactante em atividade insalubre), art. 474 (suspensão disciplinar), art. 475 (aposentadoria por invalidez), art. 476-A (qualificação).
- ADCT — art. 10, II, "b" (gestante) e § 1º (paternidade).
- Lei nº 11.770/2008 — Empresa Cidadã.
- Lei nº 15.371/2026 — nova licença-paternidade e salário-paternidade (vigência a partir de 01/01/2027).
- Lei nº 8.036/1990 — art. 15, § 5º (FGTS na licença por acidente do trabalho e no serviço militar).
- Decreto nº 99.684/1990 — art. 28 (FGTS nas interrupções do contrato, inclusive licença à gestante).
- NR-7 — ASO de retorno.
- Manual de Orientação do eSocial (MOS) S-1.3 — evento S-2230 (prazos e quadro de obrigatoriedade) e S-2210; Tabela 18 do Anexo I dos leiautes S-1.3 (NT S-1.3 nº 07/2026, rev. 20/10/2026).

## Formato de entrega
- Cálculos, apurações e conciliações: entregar SEMPRE planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar SEMPRE documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima neste documento (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
