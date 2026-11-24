---
name: esocial-eventos-periodicos
description: "Especialista em eventos periódicos do eSocial — S-1200 (remuneração), S-1210 (pagamentos e IRRF), S-1260 (produção rural PF), S-1270 (avulsos não portuários), S-1280 (informações complementares, desoneração em transição), S-1298 (reabertura) e S-1299 (fechamento, até o dia 15). Confere os totalizadores S-5001, S-5002, S-5003, S-5011, S-5012 e S-5013, que alimentam a DCTFWeb e o FGTS Digital. Use quando o usuário (a) fechou a folha do mês, (b) fala em S-1299, totalizador, fechamento do eSocial, reabertura, divergência com DCTFWeb ou FGTS Digital, (c) tem folha de 13º. Entrega: ordem dos eventos a transmitir + recibos + alerta se o totalizador divergir do cálculo interno."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# eSocial — Eventos Periódicos e Fechamento

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Monta a sequência mensal dos eventos periódicos do eSocial depois que a folha está fechada, confere os totalizadores devolvidos pelo eSocial contra o cálculo interno e indica o que fazer quando há divergência (reabertura, retificação e nova DCTFWeb).

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Fechamento mensal (e anual, do 13º) do eSocial.
- Totalizador S-5011/S-5013 diferente da folha; DCTFWeb ou FGTS Digital sem bater.
- Reabertura de competência já fechada.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Eventos e totalizadores
```
PERIÓDICOS
S-1200  Remuneração do trabalhador (empregados e contribuintes individuais)
S-1202  Remuneração de servidor vinculado a RPPS
S-1207  Benefícios — entes públicos (RPPS)
S-1210  Pagamentos de rendimentos do trabalho (data do pagamento e IRRF)
S-1260  Comercialização da produção rural por pessoa física
S-1270  Contratação de trabalhadores avulsos não portuários
S-1280  Informações complementares (desoneração da folha / atividades concomitantes)
S-1298  Reabertura dos eventos periódicos
S-1299  Fechamento dos eventos periódicos
(No leiaute S-1.3 não existe evento de "solicitação de totalização": os totalizadores
 são devolvidos automaticamente.)

TOTALIZADORES (devolvidos pelo eSocial)
S-5001  Contribuições sociais por trabalhador (após S-1200)
S-5002  IRRF por trabalhador (após S-1210)
S-5003  FGTS por trabalhador
S-5011  Contribuições sociais consolidadas do contribuinte (após S-1299) → DCTFWeb
S-5012  IRRF consolidado (após S-1299) → DCTFWeb
S-5013  FGTS consolidado → FGTS Digital

PRAZOS
S-1200 / S-1210 / S-1299      até o dia 15 do mês seguinte (POSTERGA para o 1º dia útil
                              seguinte se o dia 15 não for dia útil)
DCTFWeb                       até o último dia útil do mês seguinte (IN RFB nº 2.248/2025)
DARF de INSS e de IRRF        dia 20 do mês seguinte (antecipa se não for dia útil)
FGTS Digital                  dia 20 do mês seguinte (art. 15 da Lei nº 8.036/1990); antecipa
                              se não for dia útil
Folha de 13º (período anual)  S-1200 anual e S-1299 anual até 20/12 do próprio ano (ANTECIPA
                              para o dia útil anterior se o dia 20 não for dia útil); DCTFWeb
                              anual também até 20/12
```
Importante: o IRRF da folha é declarado pelo S-1210 e vai para a DCTFWeb; a DIRF foi extinta para fatos a partir de 2025 (informações migraram para eSocial e EFD-Reinf R-4000).

### 2. Entrevista mínima
```
Q1: Empresa + competência + a folha interna está fechada (skill folha-pagamento-mensal)?
Q2: Houve rubrica nova no mês? A S-1010 está atualizada?
Q3: A empresa está na desoneração em transição (Lei nº 14.973/2024)? S-1280 a enviar?
Q4: Houve contribuinte individual, avulso ou aquisição de produção rural de PF?
Q5: Alguma competência anterior foi reaberta (S-1298)? A DCTFWeb foi retificada depois?
```

### 3. Sequência mensal
1. Confirmar a folha interna fechada.
2. Atualizar a S-1010 se houver rubrica nova (incidências de INSS, IRRF e FGTS certas).
3. Enviar os não periódicos pendentes do mês (S-2200, S-2230, S-2299) — o S-1200 depende deles.
4. Enviar S-1200 por trabalhador.
5. Enviar S-1210 (pagamentos, com data real de pagamento — o IRRF segue o regime de caixa).
6. S-1260 / S-1270, se houver.
7. S-1280, se a empresa estiver na desoneração em transição.
8. Conferir S-5001 / S-5002 / S-5003 com a folha.
9. **Enviar S-1299** até o dia 15 (se não for dia útil, até o 1º dia útil seguinte).
10. Conferir S-5011 / S-5012 / S-5013 com o cálculo interno.
11. Divergiu: S-1298 (reabertura) → corrigir → novo S-1299 → DCTFWeb retificadora.
12. Depois de fechada também a EFD-Reinf (R-2099/R-4099), conferir e transmitir a DCTFWeb (skill `dctfweb`); FGTS Digital gera a guia a partir do S-5013.

### 4. Desoneração da folha em transição (Lei nº 14.973/2024)
Em 2026 a empresa da desoneração paga CPRB com 60% da alíquota e mais 10% sobre a folha (a parcela da folha não incide sobre o 13º). O S-1280 informa a situação de desoneração; sem ele, o S-5011 calcula a contribuição patronal cheia e a DCTFWeb sai a maior. Conferir a proporção quando houver atividades desoneradas e não desoneradas juntas.

### 5. Entregável
**a) Ordem dos eventos**
```
COMPETÊNCIA __/____ — Empresa: ______
[ ] Não periódicos do mês enviados
[ ] S-1010 atualizada
[ ] S-1200 enviados (N trabalhadores) — recibos
[ ] S-1210 enviados — recibos
[ ] S-1260 / S-1270 (se houver)
[ ] S-1280 (se desoneração)
[ ] S-5001 / S-5002 / S-5003 conferidos
[ ] S-1299 enviado até o dia 15 — recibo
[ ] S-5011 / S-5012 / S-5013 conferidos com o cálculo interno
[ ] DCTFWeb transmitida até o último dia útil; DARF até o dia 20
[ ] Guia do FGTS Digital paga até o dia 20
```
**b) Recibos** do S-1299 e dos demais eventos.
**c) Alerta de divergência** entre S-5011/S-5013 e o cálculo interno, com a causa provável (rubrica mal parametrizada na S-1010, lotação errada, falta de S-1280, evento não periódico faltando).

## Erros comuns / pontos de atenção
- S-1210 sem o S-1200 correspondente, ou com data de pagamento errada (desloca o IRRF de mês).
- Rubrica nova sem S-1010 (S-1200 rejeitado) ou com incidência errada (totalizador errado).
- Lotação tributária errada (estabelecimento ou obra trocados).
- Desoneração sem S-1280.
- Reabrir com S-1298 depois da DCTFWeb transmitida e não retificar a DCTFWeb.
- Esquecer S-1260 (compra de produção rural de PF) ou S-1270 (avulso).
- Achar que o FGTS ainda vence no dia 7 (desde o FGTS Digital vence no dia 20).

## Casos especiais
- **PLR (Lei nº 10.101/2000):** rubrica própria na S-1010; não integra a base do INSS nem do FGTS (art. 28, § 9º, "j", da Lei nº 8.212/1991); IRRF com tabela exclusiva.
- **13º salário:** folha de período anual (S-1200 com indicador de apuração anual), fechada por S-1299 anual até 20/12; S-5011 totaliza separado. O FGTS da folha anual vence em 20/01 do ano seguinte; se o empregado for desligado em dezembro, o FGTS do 13º passa a seguir o prazo rescisório de 10 dias (Nota Orientativa FGTS Digital nº 11/2025).
- **Empregado afastado no mês:** S-1200 só com a remuneração dos dias pagos pela empresa.

## Quando escalar
- DCTFWeb → `dctfweb`
- INSS da empresa → `calculo-inss-empresa`; FGTS → `fgts-guia-recolhimento`
- EFD-Reinf → `efd-reinf`
- Folha mensal → `folha-pagamento-mensal`

## Perguntas que o usuário costuma fazer
- **"Fechei o S-1299 e o S-5011 veio maior que a folha."** Verificar S-1280 (desoneração), incidências das rubricas novas e lotação.
- **"Preciso reabrir para corrigir um empregado."** S-1298, corrigir o S-1200, novo S-1299 e retificar a DCTFWeb.

## Base legal usada nesta skill
- Decreto nº 8.373/2014 — institui o eSocial.
- Manual de Orientação do eSocial (MOS) versão S-1.3 e leiautes S-1.3 com as notas técnicas vigentes (em nov/2026: NT S-1.3 nº 07/2026, rev. 20/10/2026), publicados em gov.br/esocial — prazos do S-1200, S-1210 e S-1299 (mensal e anual).
- IN RFB nº 2.237/2024, com a redação da IN RFB nº 2.248/2025 — prazo da DCTFWeb mensal (último dia útil do mês seguinte) e da DCTFWeb anual do 13º (20/12).
- Nota Orientativa FGTS Digital nº 11/2025 (SIT/MTE) — FGTS do 13º e na rescisão.
- Lei nº 8.212/1991 — art. 28, § 9º (parcelas fora do salário de contribuição); art. 30, I, "b" (recolhimento até o dia 20).
- Lei nº 8.036/1990 — art. 15 (depósito do FGTS até o dia 20).
- Lei nº 14.973/2024 — transição da desoneração da folha.
- Lei nº 10.101/2000 — PLR.

## Formato de entrega
- Cálculos, apurações e conciliações: entregar SEMPRE planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar SEMPRE documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima neste documento (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
