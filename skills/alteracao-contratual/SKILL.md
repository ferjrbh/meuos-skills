---
name: alteracao-contratual
description: "Prepara alterações contratuais pela REDESIM — entrada e saída de sócios (cessão onerosa, com ganho de capital do cedente pessoa física em DARF 4600, ou gratuita, com ITCMD), apuração de haveres, aumento e redução de capital, mudança de objeto/CNAE, mudança de endereço (outra UF exige nova inscrição estadual) e transformação societária (LTDA ↔ S.A., mantém o CNPJ). Considera o quórum atual das LTDAs e os reflexos da Lei nº 15.270/2025 sobre lucros a partir de 2026. Acionar quando o usuário disser \"alteração contratual\", \"entrada de sócio\", \"saída de sócio\", \"cessão de quotas\", \"aumento de capital\", \"redução de capital\", \"mudar CNAE\", \"mudar endereço da empresa\", \"transformar em S.A.\". Entrega: cláusulas da alteração, roteiro do DBE, cálculo do ganho de capital ou do ITCMD, lançamentos e lista de comunicações."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Alteração contratual

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Roteiriza qualquer alteração do contrato social de uma sociedade limitada (e, no que couber, de outras sociedades): define o tipo de alteração, o quórum exigido, a redação da cláusula, os tributos envolvidos (ganho de capital, ITCMD, IRRF sobre lucros) e os registros e comunicações posteriores.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Mudança no quadro societário, no capital, no objeto, no endereço ou na administração.
- Transformação de tipo societário.
- Não usar para abertura (`abertura-empresa-cnpj`) nem para baixa (`encerramento-empresa-baixa`).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Nos modelos de cláusula, usar SÓCIO A, SÓCIO B, EMPRESA EXEMPLO LTDA.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: Qual alteração? (cessão de quotas, haveres, aumento/redução de capital, CNAE, endereço,
    administração, transformação)
Q2: Documentos e qualificação dos novos sócios/administradores?
Q3: Nova redação desejada da cláusula e motivo?
Q4: Cessão onerosa: preço e custo de aquisição das quotas (declaração de bens do cedente)?
    Cessão gratuita: UF do doador e valor das quotas (para ITCMD)?
Q5: Percentual de capital que aprova a alteração? Contrato tem regra própria de quórum?
Q6: Há lucros apurados a partir de 2026 que serão capitalizados ou pagos ao retirante?
```

### 2. Tipos de alteração
```
1. CESSÃO DE QUOTAS (entrada/saída de sócio)
   Livre entre sócios; a terceiro, se não houver oposição de titulares de mais de 1/4
   do capital, salvo regra diversa do contrato (art. 1.057 do CC).
   O cedente responde solidariamente com o cessionário, por até 2 anos depois de averbada
   a cessão, pelas obrigações que tinha como sócio (art. 1.003, parágrafo único, do CC).
   Onerosa: cedente PF apura ganho de capital (preço − custo declarado), alíquotas de
     15% a 22,5% (Lei nº 13.259/2016), DARF 4600 até o último dia útil do mês seguinte
     (skill `irpf-ganho-capital`).
   Gratuita (doação): ITCMD estadual, progressivo (art. 155, § 1º, VI, da Constituição,
     incluído pela Emenda Constitucional nº 132/2023), teto de 8% (Resolução do Senado
     Federal nº 9/1992). Alíquotas variam por UF.

2. APURAÇÃO DE HAVERES (saída por retirada, exclusão ou morte)
   Balanço especial na data da resolução, salvo critério diferente no contrato;
   pagamento em 90 dias da liquidação, salvo acordo ou contrato (art. 1.031 do CC).

3. AUMENTO DE CAPITAL
   Em dinheiro: D Banco / C Capital social.
   Em bens (LTDA): avaliação pelos sócios, que respondem solidariamente pela exata estimação
     por 5 anos (art. 1.055, § 1º, do CC). Na S.A., laudo de 3 peritos ou empresa
     especializada (art. 8º da Lei nº 6.404/1976).
     Sócio PF que integraliza bem: pode transferir pelo valor da declaração de bens (sem
     ganho) ou de mercado (a diferença é ganho de capital) (art. 23 da Lei nº 9.249/1995).
   Capitalização de lucros/reservas: D Reservas/Lucros / C Capital.
     ATENÇÃO 2026: a Lei nº 15.270/2025 incluiu o art. 6º-A na Lei nº 9.250/1995: lucros e
     dividendos "pagos, creditados, empregados ou entregues" por uma mesma PJ a uma mesma PF
     residente, acima de R$ 50.000,00 no mês, sofrem retenção de 10% sobre o TOTAL do mês,
     sem deduções. Ficam fora os lucros de resultados apurados até 2025 cuja distribuição foi
     aprovada pelo órgão societário até 31/12/2025 e paga nas condições aprovadas.
     Posição da Receita Federal (Perguntas e Respostas sobre a tributação de altas rendas —
     lucros e dividendos, dez/2025, orientação não vinculante): incorporar lucros ao capital é
     "emprego" dos lucros, sujeito à retenção de 10% e ao IRPFM do sócio. O documento foi
     atualizado com entendimentos mais restritivos (inclusive sobre lucros de 2025 capitalizados
     e prazo entre capitalização e devolução): conferir a versão vigente no gov.br antes de
     orientar, e registrar o risco ao cliente.
   Ágio na subscrição: C Capital (valor nominal) + C Reserva de capital (excedente).

4. REDUÇÃO DE CAPITAL
   Por perdas irreparáveis: depois de integralizado o capital, com alteração do contrato
     (art. 1.082, I, e art. 1.083 do CC) — não é "automática".
   Por capital excessivo: credor quirografário pode se opor em 90 dias da publicação da ata
     (art. 1.082, II, e art. 1.084 do CC).
   Devolução ao sócio em bens: a PJ escolhe valor contábil ou de mercado; se de mercado, o
     ganho é tributado NA PJ, e a diferença NÃO é tributada na PF (art. 22, §§ 1º e 4º,
     da Lei nº 9.249/1995; pergunta 606 do Perguntas e Respostas IRPF 2026).
   Devolução em DINHEIRO: se o valor recebido superar o custo de aquisição das quotas na
     declaração do sócio PF, a Receita trata o excesso como ganho de capital (DARF 4600 —
     skill `irpf-ganho-capital`); a devolução de capital formado por lucros isentos (regra de
     transição) não sofre a nova tributação de dividendos. Conferir a origem do capital
     devolvido (integralização em dinheiro × lucros capitalizados, e de que ano).

5. MUDANÇA DE OBJETO / CNAE
   Zoneamento, inscrição estadual, anexo do Simples, licenças, RAT, retenções.

6. MUDANÇA DE ENDEREÇO
   Mesmo município: alteração cadastral (conferir alvará).
   Outro município: nova inscrição municipal e alvará; IE pode mudar.
   Outra UF: nova inscrição estadual obrigatória; ajustar eSocial (S-1005 do estabelecimento).

7. TRANSFORMAÇÃO SOCIETÁRIA (LTDA ↔ S.A.)
   Não há dissolução: mesmo CNPJ, saldos migram (arts. 1.113 a 1.115 do CC).
   Exige consentimento de todos os sócios, salvo previsão no contrato, garantido o direito
   de retirada ao dissidente (art. 1.114 do CC).
   Sociedade simples → empresária: o registro passa do Cartório para a Junta Comercial.
```

### 3. Quórum na LTDA (art. 1.076 do CC, com redação da Lei nº 14.451/2022)
```
Modificação do contrato social, incorporação, fusão, dissolução  → mais da metade do capital
Designação/destituição de administrador, remuneração             → mais da metade do capital
Demais matérias                                                   → maioria dos presentes
Transformação                                                     → unanimidade, salvo contrato
```
Sempre conferir se o contrato da empresa tem quórum maior.

### 4. Cláusulas-modelo
```
CLÁUSULA __ — CESSÃO DE QUOTAS
O SÓCIO A cede e transfere ao SÓCIO B a totalidade de suas [N] quotas, no valor nominal
de R$ __, pelo preço de R$ __ (__), pago em __. Com a cessão, o capital fica assim
distribuído: SÓCIO B __ quotas (__%); SÓCIO C __ quotas (__%).
O cedente dá plena quitação, salvo as obrigações expressamente ressalvadas, observado o
art. 1.003, parágrafo único, do Código Civil.

CLÁUSULA __ — AUMENTO DE CAPITAL
O capital social, de R$ __, é aumentado para R$ __, com a criação de [N] novas quotas de
R$ __ cada, subscritas e integralizadas em [moeda corrente / bens descritos no Anexo I,
avaliados pelos sócios, que respondem solidariamente pela exata estimação, nos termos do
art. 1.055, § 1º, do Código Civil], na proporção das participações atuais.
```

### 5. Lançamentos contábeis
```
Aumento em dinheiro:          D Banco c/c ............ X   C Capital social ........ X
Cessão entre sócios:          sem lançamento na PJ (atualizar cadastro de sócios e DMPL)
Haveres a pagar:              D Capital social (parte do retirante) + D Reservas/Lucros
                              C Haveres a pagar / Banco
Capitalização de reservas:    D Reserva de lucros ...... X   C Capital social ........ X
```

### 6. Fluxo REDESIM
1. Minuta da alteração com contrato consolidado.
2. Assinaturas digitais de todos os signatários necessários.
3. Viabilidade (se mudar nome, endereço ou CNAE) e DBE de alteração.
4. Protocolo na Junta Comercial (ou Cartório).
5. CNPJ atualizado pela integração; atualizar IE, IM e alvará quando aplicável.
6. Comunicar bancos, fornecedores, clientes e contratos.
7. Atualizar procuração eletrônica no e-CAC e responsáveis no eSocial.

### 7. Entregável obrigatório
a) Minuta da alteração + contrato consolidado.
b) Roteiro do DBE.
c) Cálculo do ganho de capital do cedente PF e DARF 4600 (`irpf-ganho-capital`), se onerosa com ganho.
d) Cálculo do ITCMD, se gratuita (lei da UF).
e) Lançamentos contábeis.
f) Lista de comunicações:
```
[ ] Bancos (quadro societário e poderes)
[ ] Fornecedores e clientes principais
[ ] Cartório de Registro de Imóveis (se a empresa tem imóveis e mudou nome)
[ ] Procuração eletrônica e-CAC
[ ] eSocial (S-1000/S-1005 se mudou endereço ou estabelecimento)
```
g) Checklist:
```
[ ] Quórum conferido (lei e contrato)
[ ] Documentos dos sócios que entram/saem
[ ] Apuração de haveres / ganho de capital / ITCMD
[ ] Minuta assinada digitalmente
[ ] DBE / REDESIM / protocolo na Junta
[ ] CNPJ, IE, IM e alvará atualizados
[ ] Recibo de quitação ao sócio retirante
[ ] Cláusula de não concorrência (se negociada)
[ ] DARF de ganho de capital pago (pelo cedente)
[ ] Reflexo da Lei nº 15.270/2025 avaliado (lucros de 2026 pagos ou capitalizados)
```

## Erros comuns / pontos de atenção
- Cessão gratuita sem ITCMD.
- Sócio retirante sem recibo de quitação: risco de ação de haveres.
- Esquecer que o cedente continua responsável por 2 anos (art. 1.003 do CC).
- Aumento com bens sem avaliação documentada.
- Usar o quórum antigo de 3/4 do capital: desde a Lei nº 14.451/2022, basta mais da metade para alterar o contrato.
- Mudar CNAE para atividade impeditiva do Simples sem avaliar a exclusão.
- Mudar para outra UF sem nova IE.
- Pagar haveres com lucros de 2026 acima de R$ 50.000,00/mês sem considerar a retenção de 10% da Lei nº 15.270/2025.
- Capitalizar lucros de 2026 sem reter os 10% quando o valor do sócio no mês passar de R$ 50.000,00.

## Perguntas que o usuário costuma fazer
- **"Vendi minhas quotas pelo mesmo valor que paguei. Tenho imposto?"** Não há ganho, mas a operação deve ser informada no GCAP/Declaração.
- **"Preciso da assinatura de todos os sócios?"** Para alterar o contrato, basta mais da metade do capital (salvo contrato com quórum maior); a transformação exige unanimidade, salvo previsão contratual.
- **"Capitalizar lucro paga imposto?"** Para a Receita Federal, sim: capitalizar é "empregar" o lucro, e acima de R$ 50.000,00 no mês, por PJ e por sócio, há retenção de 10% (art. 6º-A da Lei nº 9.250/1995), além de o valor entrar no IRPFM. Lucros na regra de transição (apurados até 2025, distribuição aprovada até 31/12/2025) ficam fora, mas conferir a versão vigente das Perguntas e Respostas da Receita sobre a capitalização desses lucros. O tema é questionado; documentar a orientação dada.

## Casos de borda
- Empresa em recuperação judicial: alteração possível, observado o plano.
- Venda de 100% da empresa: `due-diligence-contabil` para o comprador.
- Morte de sócio: herdeiros entram ou não conforme o contrato; na falta, liquidação da quota (art. 1.028 do CC).

## Quando escalar
- Fim de vida da empresa → `encerramento-empresa-baixa`
- M&A, litígio entre sócios, acordo de quotistas → advogado parceiro com OAB
- Mudança de regime após troca de CNAE → `analise-tributaria-regime`

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei nº 10.406/2002 (Código Civil) — art. 1.003 (responsabilidade do cedente), art. 1.028 (morte de sócio), art. 1.031 (haveres), art. 1.055 (integralização em bens), art. 1.057 (cessão de quotas), art. 1.076 (quórum, com redação da Lei nº 14.451/2022), arts. 1.082 a 1.084 (redução de capital), arts. 1.113 a 1.115 (transformação).
- Lei nº 14.451/2022 — novo quórum das LTDAs.
- Lei nº 6.404/1976 — art. 8º (avaliação de bens na S.A.).
- Lei nº 9.249/1995 — art. 10 (lucros e dividendos), art. 22 (devolução de capital em bens), art. 23 (integralização com bens pela PF).
- Lei nº 9.250/1995 — art. 6º-A (retenção de 10% sobre lucros acima de R$ 50.000,00/mês, incluído pela Lei nº 15.270/2025).
- Lei nº 15.270/2025 — tributação de lucros e dividendos a partir de 2026 (retenção mensal e IRPFM).
- Receita Federal — Perguntas e Respostas sobre a tributação de altas rendas (lucros e dividendos), dez/2025 e atualizações — capitalização como "emprego" e devolução de capital (orientação não vinculante).
- Lei nº 13.259/2016 — alíquotas do ganho de capital (15% a 22,5%).
- Constituição Federal — art. 155, § 1º, VI (ITCMD progressivo, Emenda Constitucional nº 132/2023); Resolução do Senado Federal nº 9/1992 (teto de 8%).
- Lei nº 11.598/2007 e Lei nº 14.195/2021 — REDESIM e simplificação do registro.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
