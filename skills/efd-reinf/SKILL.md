---
name: efd-reinf
description: "Organiza a EFD-Reinf mensal: R-1000 (cadastro), R-1070 (processos), R-2010/R-2020 (retenção de 11% de INSS na cessão de mão de obra, tomador e prestador), R-2050/R-2055 (produção rural), R-2060 (CPRB), R-2099 (fechamento), série R-4000 (IRRF e CSRF sobre pagamentos a PF e PJ, que substitui a DIRF para fatos geradores a partir de 01/01/2025) e R-4099 (fechamento). Prazo: dia 15 do mês seguinte. Acionar quando o usuário disser \"fazer a Reinf\", \"fechar R-2099\", \"R-4010\", \"R-4020\", \"retenção de 11%\", \"aluguel pago a pessoa física\", \"substituiu a DIRF\", \"DCTFWeb não gerou\". Entrega a sequência de eventos a transmitir, controle dos recibos de fechamento, cruzamento com a DCTFWeb e lista de comprovantes para os beneficiários."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# EFD-Reinf mensal

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Monta a sequência de eventos da EFD-Reinf (Escrituração Fiscal Digital de Retenções e Outras Informações Fiscais) da competência, confere se cada retenção ou pagamento está no evento certo e garante os dois fechamentos (R-2099 e R-4099), sem os quais a DCTFWeb não recebe os débitos. Também confirma que os pagamentos que antes iam para a DIRF estão na série R-4000 ou no eSocial.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **DIRF e Reinf: a data certa.** A DIRF foi substituída, para fatos ocorridos a partir de **01/01/2025**, pelos eventos da série R-4000 da EFD-Reinf, pelo evento S-1210 do eSocial (e pelos eventos a que ele remete) e pelo evento S-2501 do eSocial (processo trabalhista) — art. 3º, § 1º, da IN RFB nº 2.043/2021, com redação da IN RFB nº 2.181/2024. A DIRF 2025, referente ao ano-calendário 2024, ainda foi entregue em fevereiro/2025.

## Quando usar
- No fechamento mensal, antes da DCTFWeb.
- Quando houver serviço tomado ou prestado com retenção de 11% de INSS (cessão de mão de obra ou empreitada).
- Quando houver pagamento a PF ou PJ com IRRF ou CSRF, ou retenção sofrida.
- Na comercialização ou aquisição de produção rural, e na CPRB.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Eventos
```
TABELAS
R-1000  Informações do contribuinte (enviar no início; atualizar se mudar cadastro)
R-1050  Tabela de entidades ligadas (fundos/clubes de investimento, SCP)
R-1070  Processos administrativos/judiciais (suspensão de exigibilidade)

PERIÓDICOS (fechados pelo R-2099)
R-2010  Retenção de INSS de 11% — serviços TOMADOS (cessão de mão de obra/empreitada)
R-2020  Retenção de INSS — serviços PRESTADOS (enviado pelo prestador)
R-2030  Recursos recebidos por associação desportiva
R-2040  Recursos repassados a associação desportiva
R-2050  Comercialização da produção por produtor rural PJ/agroindústria
R-2055  Aquisição de produção rural
R-2060  CPRB (contribuição previdenciária sobre a receita bruta)
R-2098  Reabertura dos eventos periódicos
R-2099  FECHAMENTO dos eventos periódicos

SÉRIE R-4000 (IRRF, CSRF — substitui a DIRF para fatos a partir de 01/01/2025)
R-4010  Pagamentos/créditos a beneficiário PESSOA FÍSICA (ex.: aluguel, juros, royalties
        pagos a PF; rendimentos do trabalho ficam no eSocial)
R-4020  Pagamentos/créditos a beneficiário PESSOA JURÍDICA (IRRF e CSRF)
R-4040  Pagamentos a beneficiários não identificados
R-4080  Retenção no recebimento: a PJ que RECEBE de outras PJ comissões e corretagens
        (relacionadas na IN SRF nº 153/1987) informa os rendimentos e as retenções;
        quem pagou fica dispensado de informar (art. 3º, §§ 3º e 4º, da IN RFB nº 2.043/2021)
R-4099  FECHAMENTO da série R-4000

PRAZO: até o dia 15 do mês seguinte (art. 6º, caput, da IN RFB nº 2.043/2021).
Se o dia 15 não for dia útil para fins fiscais, o prazo passa para o primeiro dia útil
seguinte (art. 6º, § 2º, da IN RFB nº 2.043/2021, redação da IN RFB nº 2.163/2023).
Lucros e dividendos isentos de retenção: até o dia 15 do 2º mês seguinte ao trimestre
(art. 6º, § 3º). Espetáculo desportivo: até 2 dias úteis após o evento (art. 6º, § 1º).
```

### 2. Entrevista mínima
```
Q1: "CNPJ + competência. O R-1000 está enviado e atualizado?"
Q2: "Tomou serviços com retenção de 11% de INSS? Prestou serviços e sofreu retenção?"
Q3: "Pagou PF (aluguel, juros, royalties) ou PJ (serviços com IRRF/CSRF)?"
Q4: "Atividade rural (R-2050/R-2055)? Empresa na CPRB (R-2060)?"
Q5: "O eSocial da competência (S-1299) está fechado? A DCTFWeb depende dos dois."
```

### 3. Sequência mensal
1. Conferir o R-1000 (atualizar se mudou o cadastro).
2. R-1050 / R-1070, se aplicável.
3. R-2010 (serviços tomados com retenção), por prestador e estabelecimento/obra.
4. R-2020 (serviços prestados com retenção), se a empresa for prestadora.
5. R-2050/R-2055 (rural), se aplicável.
6. R-2060 (CPRB), se a empresa estiver na desoneração em transição.
7. R-4010 (PF) e R-4020 (PJ) para cada pagamento com retenção ou que deva ser informado.
8. **R-2099** — fecha os periódicos.
9. **R-4099** — fecha a série R-4000.
10. Conferir se os débitos chegaram à DCTFWeb (skill `dctfweb`).

### 4. R-2010 — estrutura (ilustrativa)
O trecho abaixo serve só para mostrar a lógica (tomador, prestador, nota, base e retenção). Não é o leiaute oficial. Para gerar XML, seguir o leiaute vigente publicado no portal SPED.
```xml
<evtServTom>
  <ideEvento>
    <indRetif>1</indRetif>          <!-- 1 original; 2 retificação -->
    <perApur>2026-03</perApur>
  </ideEvento>
  <ideContri>
    <tpInsc>1</tpInsc>              <!-- 1 = CNPJ -->
    <nrInsc>12345678</nrInsc>       <!-- raiz do CNPJ de exemplo -->
  </ideContri>
  <!-- estabelecimento/obra do tomador > prestador > notas fiscais -->
  <!-- vlrBruto 10000.00 | vlrBaseRet 10000.00 | vlrRetencao 1100.00 (11%) -->
</evtServTom>
```

### 5. Entregável obrigatório

**a) Sequência de eventos a transmitir**
```
COMPETÊNCIA __/____ — CNPJ __

[ ] R-1000 OK (último envio __/__/__)
[ ] R-1070 com processos, se houver
[ ] R-2010 (tomador): N notas com retenção de 11%
[ ] R-2020 (prestador): M notas
[ ] R-2050/R-2055: K eventos rurais (se aplicável)
[ ] R-2060: CPRB (se aplicável)
[ ] R-4010: P pagamentos a PF
[ ] R-4020: Q pagamentos a PJ
[ ] R-2099 — recibo: __
[ ] R-4099 — recibo: __

Débitos chegaram à DCTFWeb? SIM/NÃO. Se NÃO, qual fechamento falta?
```

**b) Recibos do R-2099 e do R-4099** arquivados.

**c) Cruzamento com a DCTFWeb**: INSS retido (R-2010) e IRRF/CSRF (R-4010/R-4020) devem aparecer na DCTFWeb da competência.

**d) Comprovantes de retenção** para os beneficiários (prestadores PJ e PF), que precisam deles para compensar o imposto retido.

## Erros comuns / pontos de atenção
- Não fechar o R-2099 ou o R-4099: os débitos não chegam à DCTFWeb.
- Enviar evento periódico sem R-1000.
- Esquecer o R-2055 na aquisição de produção rural.
- Reter 11% de prestador do Simples fora das hipóteses legais (cessão de mão de obra ou empreitada; no Simples, em regra só atividades do Anexo IV) — conferir a IN RFB nº 2.110/2022.
- Informar no R-4010 rendimentos do trabalho que já estão no eSocial (duplicidade).
- Continuar procurando "DIRF" para fatos de 2025 em diante: não existe mais.
- Reabrir com R-2098 depois da DCTFWeb transmitida e não conferir a DCTFWeb retificadora.
- **Multa** (art. 7º da IN RFB nº 2.043/2021): atraso ou falta de entrega, 2% ao mês-calendário ou fração sobre os tributos informados, ainda que pagos, limitada a 20%; informação incorreta ou omitida, R$ 20,00 por grupo de 10 informações; mínimo de R$ 500,00. Redução de 50% se entregar antes de procedimento de ofício e de 25% se entregar no prazo da intimação; para MEI (90%) e ME/EPP do Simples Nacional (50%) há reduções próprias, que substituem essas.

### Casos de borda
- **Aluguel pago por PJ a PF**: R-4010 a cada pagamento com IRRF (código 3208).
- **Agroindústria**: R-2050 e R-2055 conforme o caso.
- **Cooperativa de trabalho**: a contribuição de 15% sobre a nota da cooperativa (art. 22, IV, da Lei nº 8.212/1991) foi declarada inconstitucional pelo STF (RE 595.838); não há retenção a informar por esse motivo.
- **Pagamento a beneficiário no exterior** (royalties, juros, serviços): série R-4000 com os campos de residente no exterior; alíquota conforme a legislação e eventual tratado.
- **Prestador optante do Simples Nacional**: não há retenção de CSRF (art. 32, III, da Lei nº 10.833/2003), desde que o prestador apresente a declaração de optante. A forma de informar (ou não) esse pagamento no R-4020 segue o Manual de Orientação do Usuário da EFD-Reinf da versão em uso.

### Quando encaminhar para outra skill
- DCTFWeb depois dos fechamentos → `dctfweb`
- Retificar DIRF de anos até 2024 → PGD próprio da DIRF (fora deste pacote)
- Cálculo das retenções do tomador → `retencoes-tributarias-tomador`
- Folha → `folha-pagamento-mensal`
- Cruzamento geral → `revisao-fiscal-cruzamento-sped`

### Autoavaliação
- [ ] R-1000 OK?
- [ ] Eventos R-2000 enviados para todos os tomadores/prestadores?
- [ ] R-4010/R-4020 enviados e sem duplicar o eSocial?
- [ ] R-2099 e R-4099 fechados, com recibos?
- [ ] Débitos chegaram à DCTFWeb?
- [ ] Comprovantes entregues aos beneficiários?

## Perguntas que o usuário costuma fazer
- **"Pago autônomo por RPA. Vai no R-4010?"** Em regra, não: o contribuinte individual é informado no eSocial (S-1200/S-1210), e o IRRF dele sai de lá. O R-4010 é para pagamentos a PF que não estão no eSocial (aluguel, juros, royalties etc.).
- **"Não tive movimento. Preciso enviar algo?"** Conferir no Manual da EFD-Reinf a regra de fechamento sem movimento; a DCTFWeb depende do fechamento.
- **"A DIRF de 2024 tem erro. E agora?"** Retificação da DIRF continua possível para anos até 2024 pelo PGD próprio.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): documento DOCX.
- Este padrão prevalece sobre outros formatos citados acima, exceto arquivos técnicos de importação de sistemas.

## Base legal usada nesta skill
- IN RFB nº 2.043/2021 — EFD-Reinf: art. 3º, § 1º (substituição da DIRF), §§ 3º e 4º (R-4080); art. 6º (prazo dia 15 e prorrogação); art. 7º (multas).
- IN RFB nº 2.181/2024 — fixou a substituição da DIRF para fatos a partir de 01/01/2025.
- IN RFB nº 2.163/2023 — prorrogação para o primeiro dia útil seguinte e prazo trimestral de lucros e dividendos isentos.
- IN RFB nº 2.110/2022 — retenção de 11% de INSS na cessão de mão de obra e empreitada.
- Lei nº 8.212/1991, art. 31 — retenção de 11%; art. 22, IV — contribuição sobre cooperativas (RE 595.838 do STF).
- Lei nº 10.833/2003, art. 32, III — sem retenção de CSRF para optante do Simples Nacional.
- Lei nº 14.973/2024 — CPRB em transição.
- Manual de Orientação do Usuário da EFD-Reinf (versão vigente no portal SPED).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
