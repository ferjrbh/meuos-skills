---
name: esocial-rescisao
description: "Especialista no desligamento CLT no eSocial — S-2299 com o motivo correto da Tabela 19 (01 justa causa, 02 sem justa causa, 06 término de contrato a termo, 07 pedido de demissão, 10 falecimento, 17 rescisão indireta, 33 acordo do art. 484-A etc.), prazo de 10 dias (art. 477, § 6º, da CLT), guia rescisória do FGTS Digital (a GRRF foi extinta), seguro-desemprego, estabilidades e plano de saúde (arts. 30 e 31 da Lei nº 9.656/1998 e RN ANS nº 488/2022). Use quando o usuário vai desligar empregado ou fala em TRCT, motivo do S-2299, multa do art. 477, § 8º, FGTS rescisório, seguro-desemprego. NÃO calcula as verbas em dinheiro (use `rescisao-clt-calculo`); esta skill cuida do EVENTO e do roteiro do desligamento."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# eSocial — Desligamento (S-2299)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Conduz o desligamento do empregado do ponto de vista do eSocial e das obrigações acessórias: escolhe o motivo da Tabela 19, organiza prazos (pagamento, S-2299, FGTS Digital), seguro-desemprego, comunicação do plano de saúde e alertas de estabilidade. O cálculo das verbas fica com `rescisao-clt-calculo`.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Qualquer desligamento de empregado (dispensa, pedido, acordo, fim de contrato, falecimento).
- Dúvida sobre o código do motivo no S-2299.
- Conferência do roteiro antes de pagar o TRCT.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Documentos de justa causa e ASO demissional têm acesso restrito.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Justa causa, rescisão indireta e culpa recíproca envolvem avaliação jurídica: a decisão é do cliente com seu advogado (OAB).

## Passo a passo (instruções para o agente de IA)

### 1. Tabela 19 — motivos mais usados (leiaute S-1.3)
```
Cód  Motivo
01   Rescisão com justa causa, por iniciativa do empregador
02   Rescisão sem justa causa, por iniciativa do empregador
03   Rescisão antecipada de contrato a termo, por iniciativa do empregador
04   Rescisão antecipada de contrato a termo, por iniciativa do empregado
05   Rescisão por culpa recíproca
06   Término do contrato a termo (inclui fim da experiência)
07   Rescisão por iniciativa do empregado (pedido de demissão)
08   Rescisão por interesse do(a) empregado(a) nas hipóteses dos arts. 394 e 483, § 1º, da CLT
10   Falecimento do empregado
11   Transferência para empresa do mesmo grupo que assumiu os encargos, sem rescisão
17   Rescisão indireta (art. 483 da CLT — em regra, reconhecida em juízo)
27   Força maior
33   Acordo entre as partes (art. 484-A da CLT)
38   Aposentadoria, exceto por invalidez
41   Rescisão do contrato de aprendizagem por desempenho insuficiente ou inadaptação do aprendiz
42   Rescisão do contrato de aprendizagem por ausência injustificada à escola que implique
     perda do ano letivo
47   Encerramento da empresa, de estabelecimento ou supressão de parte das atividades
48   Falecimento do empregador individual sem continuação da atividade
```
Conferido na Tabela 19 do Anexo I dos leiautes S-1.3 (NT S-1.3 nº 07/2026, rev. 20/10/2026, gov.br/esocial). Os códigos 14 (encerramento) e 18 a 20 (aposentadorias) tiveram a validade encerrada e não devem ser usados em desligamentos atuais. Antes de transmitir, conferir a validade do código e a compatibilidade com a categoria do trabalhador.

### 2. Direitos por modalidade (resumo — cálculo em `rescisao-clt-calculo`)
```
Modalidade              Aviso                    Multa FGTS  Saque FGTS   Seguro-desemprego
Sem justa causa (02)    sim (indeniz. ou trab.)  40%         sim          sim
Justa causa (01)        não                      não         não          não
Pedido (07)             devido PELO empregado    não         não          não
Acordo 484-A (33)       metade, se indenizado    20%         até 80%      não
Término a termo (06)    não                      não         sim          não
Culpa recíproca (05)    metade                   20%         sim          não
Rescisão indireta (17)  sim                      40%         sim          sim
Falecimento (10)        não                      não         sim (dependentes)  não
Encerramento (47)       sim                      40%         sim          sim
```
Férias vencidas + 1/3 são devidas em todas as modalidades, inclusive justa causa (Súmula 171 do TST).

### 3. Entrevista mínima
```
Q1: Trabalhador (matrícula) + data do desligamento + motivo?
Q2 (justa causa): qual falta do art. 482 da CLT e qual a prova documentada?
Q3: Aviso prévio: trabalhado, indenizado ou dispensado? Tempo de casa (Lei nº 12.506/2011)?
Q4: Saldo do FGTS para fins rescisórios (extrato)?
Q5: ASO demissional feito? Plano de saúde com contribuição do empregado?
Q6: Há estabilidade (gestante, CIPA, acidentado, dirigente sindical)?
```

### 4. Sequência
1. Conferir estabilidades (item 6). Se houver, parar e avisar.
2. Calcular as verbas (`rescisao-clt-calculo`).
3. Pagar as verbas e entregar os documentos em até **10 dias** contados a partir do término do contrato (art. 477, § 6º, da CLT). Atraso: multa a favor do empregado no valor do seu salário (art. 477, § 8º) e multa administrativa.
4. Transmitir o **S-2299 até 10 dias a contar do desligamento** (exclui-se o dia do desligamento; se o último dia não for dia útil, ANTECIPA para o dia útil anterior), com o motivo da Tabela 19. Exceção: transferência ou mudança de CPF — até o dia 15 do mês seguinte. Não há evento próprio de aviso prévio no leiaute S-1.3: o aviso indenizado e a data projetada do fim do aviso são informados no próprio S-2299.
5. Recolher o **FGTS rescisório pelo FGTS Digital** (mês da rescisão + mês imediatamente anterior, se ainda não recolhido + aviso indenizado + 13º + multa) em até 10 dias contados do término do contrato (art. 18 da Lei nº 8.036/1990 e Nota Orientativa FGTS Digital nº 11/2025), por PIX. A GRRF do Conectividade Social não é mais usada: desde o FGTS Digital, o débito rescisório é gerado a partir do S-2299.
6. Seguro-desemprego: nos motivos que dão direito, o eSocial é a fonte das informações da dispensa — o S-2299 precisa estar aceito. Conferir no portal gov.br do Ministério do Trabalho e Emprego se o requerimento ainda deve ser emitido pelo empregador no Empregador Web; o trabalhador faz o pedido pela Carteira de Trabalho Digital ou pelo gov.br.
7. Plano de saúde: comunicar por escrito ao empregado, no ato da comunicação do aviso prévio (trabalhado ou indenizado) ou da aposentadoria, o direito de manter o plano (arts. 30 e 31 da Lei nº 9.656/1998). O ex-empregado tem até 30 dias, em resposta a esse comunicado, para optar pela manutenção (RN ANS nº 488/2022); sem resposta no prazo, o empregador pode pedir a exclusão.
8. Homologação no sindicato não é mais obrigatória (o § 1º do art. 477 da CLT foi revogado pela Lei nº 13.467/2017), salvo regra da CCT/ACT.

### 5. Detalhes especiais
- **Justa causa:** precisa de falta prevista no art. 482 da CLT, imediatidade e prova documentada (o ônus da prova é do empregador — art. 818 da CLT). Sem prova, tende a ser revertida.
- **Acordo (art. 484-A da CLT):** metade do aviso indenizado e metade da multa (20%); demais verbas integrais; saque de até 80% do FGTS; sem seguro-desemprego.
- **Aviso prévio proporcional (Lei nº 12.506/2011):** 30 dias + 3 por ano completo, até 90 dias. O acréscimo é direito do empregado; no pedido de demissão, o empregado cumpre ou indeniza 30 dias.
- **Plano de saúde:** demitido sem justa causa que contribuía: manutenção por 1/3 do tempo de plano, mínimo 6 e máximo 24 meses (art. 30 da Lei nº 9.656/1998). Aposentado que contribuiu por 10 anos ou mais: manutenção por prazo indeterminado; menos de 10 anos: 1 ano para cada ano de contribuição (art. 31). Só coparticipação não conta como contribuição. O ex-empregado assume o pagamento integral.

### 6. Estabilidades (não demitir sem justa causa)
- Gestante: da confirmação da gravidez até 5 meses após o parto (art. 10, II, "b", do ADCT), inclusive em contrato a prazo (Súmula 244 do TST).
- Membro eleito da CIPA: da candidatura até 1 ano após o mandato (art. 10, II, "a", do ADCT).
- Acidentado: 12 meses após a cessação do auxílio-doença acidentário (art. 118 da Lei nº 8.213/1991).
- Dirigente sindical: da candidatura até 1 ano após o mandato (art. 543, § 3º, da CLT).
- Membro da Comissão de Conciliação Prévia: até 1 ano após o mandato (art. 625-B, § 1º, da CLT).
- A partir de 01/01/2027: é vedada a dispensa arbitrária ou sem justa causa do empregado desde o início da licença-paternidade até 1 mês após o seu término (art. 4º da Lei nº 15.371/2026).
- Afastado pelo INSS: contrato suspenso; não dispensar sem justa causa durante o benefício.

### 7. Entregável
**a) Resumo do desligamento** (valores vêm de `rescisao-clt-calculo`):
```
TRABALHADOR (matrícula): ___  Admissão: __/__/____  Desligamento: __/__/____
Motivo S-2299: __ — [descrição]
Verbas brutas: R$ __   Descontos (INSS/IRRF): R$ __   Líquido: R$ __
FGTS Digital — guia rescisória: depósitos rescisórios R$ __ + multa __% R$ __
Prazo de pagamento e da guia: __/__/____ (10 dias do término do contrato)
Prazo do S-2299: __/__/____
```
**b) S-2299** com recibo.
**c) Guia rescisória do FGTS Digital** com vencimento.
**d) Orientação do seguro-desemprego**, quando cabível.
**e) Comunicado do plano de saúde** (modelo), entregue junto com o aviso prévio.
**f) Checklist**
```
[ ] Estabilidade verificada
[ ] Motivo da Tabela 19 conferido
[ ] Prova da justa causa arquivada (se for o caso)
[ ] ASO demissional
[ ] TRCT entregue e assinado
[ ] Pagamento em até 10 dias
[ ] Guia rescisória do FGTS Digital paga em até 10 dias
[ ] S-2299 transmitido (recibo)
[ ] Seguro-desemprego orientado (quando cabível)
[ ] Plano de saúde: comunicação por escrito entregue (prazo de 30 dias para a opção)
```

## Erros comuns / pontos de atenção
- Código trocado na Tabela 19: acordo do art. 484-A é 33; pedido de demissão é 07; término de contrato a termo é 06; justa causa é 01.
- Pagar depois de 10 dias (multa do art. 477, § 8º).
- Tentar gerar guia rescisória fora do FGTS Digital.
- Aplicar 40% no acordo do art. 484-A (o correto é 20%).
- Declarar rescisão indireta ou culpa recíproca por conta própria (dependem de reconhecimento judicial).
- Esquecer as férias vencidas na justa causa e no pedido de demissão.
- Deixar o FGTS do mês anterior (ainda não recolhido) fora da guia rescisória.

## Casos especiais
- **Empresa em recuperação judicial:** os créditos trabalhistas seguem o plano de recuperação (Lei nº 11.101/2005); o S-2299 segue o prazo normal.
- **Aposentadoria espontânea:** não extingue o contrato; se o empregador depois dispensar sem justa causa, a multa de 40% incide sobre todos os depósitos do contrato (OJ 361 da SDI-1 do TST).
- **Falecimento (motivo 10):** verbas pagas aos dependentes habilitados no INSS ou, na falta, aos sucessores (Lei nº 6.858/1980).
- **Desligamento em dezembro:** o FGTS do 13º deixa o prazo da folha anual (20/01) e passa a vencer no prazo rescisório de 10 dias; ajustar as rubricas no S-1200 anual e no S-2299 conforme a Nota Orientativa FGTS Digital nº 11/2025.

## Quando escalar
- Cálculo das verbas → `rescisao-clt-calculo`
- FGTS Digital → `fgts-guia-recolhimento`
- Defesa em reclamação trabalhista → parceiro advogado com OAB (atividade privativa).

## Perguntas que o usuário costuma fazer
- **"Qual o código do acordo?"** 33 (art. 484-A da CLT).
- **"O FGTS rescisório vence no dia 20?"** Não: no desligamento, a guia do FGTS Digital vence em 10 dias contados do término do contrato.

## Base legal usada nesta skill
- CLT (Decreto-Lei nº 5.452/1943) — art. 477, §§ 6º e 8º (prazo e multa), art. 482 (justa causa), art. 483 (rescisão indireta), art. 484 (culpa recíproca), art. 484-A (acordo), art. 543, § 3º (dirigente sindical), art. 625-B, § 1º (CCP), art. 818 (ônus da prova).
- Lei nº 12.506/2011 — aviso prévio proporcional.
- Lei nº 8.036/1990 — art. 18 (depósitos rescisórios e multa) e art. 20 (saque).
- Lei nº 9.656/1998 — arts. 30 e 31 (plano de saúde); RN ANS nº 488/2022 (regulamenta os arts. 30 e 31; prazo de 30 dias para a opção).
- Lei nº 8.213/1991 — art. 118 (estabilidade acidentária).
- Lei nº 15.371/2026 — art. 4º (proteção contra dispensa na licença-paternidade, a partir de 01/01/2027).
- ADCT — art. 10, II, "a" e "b".
- Súmulas 171 e 244 do TST; OJ 361 da SDI-1 do TST.
- Lei nº 6.858/1980 — pagamento a dependentes.
- Manual de Orientação do eSocial (MOS) S-1.3 — evento S-2299 (prazo); Tabela 19 do Anexo I dos leiautes S-1.3 (NT S-1.3 nº 07/2026, rev. 20/10/2026).
- Nota Orientativa FGTS Digital nº 11/2025 (SIT/MTE) — FGTS do 13º e na rescisão.

## Formato de entrega
- Cálculos, apurações e conciliações: entregar SEMPRE planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar SEMPRE documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima neste documento (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
