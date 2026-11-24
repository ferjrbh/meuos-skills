---
name: analisar-notas-fiscais
description: "Lê XMLs de NF-e (entrada e saída) e NFS-e, confere o lançamento contábil esperado por CFOP e aponta inconsistências fiscais, com foco em empresas do Simples Nacional. Use quando o usuário enviar XML de nota fiscal ou disser \"NF-e\", \"NFS-e\", \"nota fiscal\", \"CFOP\", \"DANFE\", \"nfeProc\", \"tomador/prestador\", \"analisar notas\", \"escriturar notas\", \"conferir notas\". Acione também para revisar tributos destacados (ICMS, PIS, COFINS, ISS, IRRF, INSS, CBS/IBS do ano-teste 2026), retenções de NFS-e, ou quando perguntarem se o lançamento de uma nota está correto, mesmo sem citar a norma (NBC TG 47, NBC TG 16, LC 123/2006)."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Analisar Notas Fiscais (Área Fiscal)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Lê os XMLs de NF-e e NFS-e, extrai os campos principais, sugere o lançamento contábil esperado pelo CFOP (Código Fiscal de Operações e Prestações, que diz que tipo de operação a nota registra) e confere tributos e retenções. Devolve um relatório nota a nota com status (Aprovada / Aprovada com ressalvas / Reprovada) e um resumo final. A skill só analisa: não lança nada no sistema.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Lote de XMLs de compras, vendas ou serviços tomados para conferir antes da escrituração.
- Dúvida se o CFOP e o lançamento de uma nota estão corretos.
- Conferência de retenções em NFS-e de serviços tomados.
- Conferência dos grupos de CBS/IBS (ano-teste 2026) nas notas de fornecedores do regime normal.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Nota emitida para pessoa física traz CPF e endereço: no relatório, mascarar o CPF (ex.: 123.***.***-09).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Confirmar o cenário
Pergunte (se não vier junto): regime tributário da empresa analisada (Simples Nacional, Presumido ou Real), UF, atividade, e se as notas são de entrada, saída ou serviço tomado. Esta skill foi escrita para empresas do Simples; para Presumido e Real, os pontos de crédito de ICMS/PIS/COFINS mudam (ver passo 5).

### 2. Tipos de documento aceitos
- NF-e de entrada e de saída (modelo 55): XML com a tag `<nfeProc>` ou `<NFe>`.
- NFS-e (serviços): XML no padrão nacional (gov.br/nfse) ou no padrão do município.

### 3. Campos a extrair de cada XML
- Número, série, data de emissão e chave de acesso (44 dígitos).
- CNPJ do emitente e do destinatário; CRT do emitente (1, 2 ou 4 = Simples/MEI; 3 = regime normal).
- Natureza da operação e CFOP de cada item; NCM; CST ou CSOSN.
- Valor total da nota e dos itens.
- Tributos destacados: ICMS, ICMS-ST, IPI, PIS, COFINS, ISS, IRRF, INSS, CSRF e, a partir de 2026, os grupos de CBS/IBS.

### 4. Tabela de lançamentos esperados por CFOP

**Entradas**

| CFOP | Operação | Débito | Crédito |
|---|---|---|---|
| 1.102 / 2.102 | Compra para comercialização | Estoque de mercadorias | Fornecedores |
| 1.403 / 2.403 | Compra para comercialização de mercadoria sujeita a ICMS-ST (empresa é substituída) | Estoque de mercadorias | Fornecedores |
| 1.101 / 2.101 | Compra para industrialização | Estoque de matéria-prima | Fornecedores |
| 1.556 / 2.556 | Compra de material para uso ou consumo | Despesa (ou estoque de material de consumo) | Fornecedores |
| 1.551 / 2.551 | Compra de bem para o ativo imobilizado | Imobilizado | Fornecedores |
| 1.933 / 2.933 | Serviço tributado pelo ISS tomado em NF-e conjugada | Despesa com serviços | Fornecedores |

Serviço tomado com NFS-e normalmente não tem CFOP: classificar pela descrição e pelo item da lista da LC nº 116/2003.

**Saídas**

| CFOP | Operação | Débito | Crédito |
|---|---|---|---|
| 5.102 / 6.102 | Venda de mercadoria adquirida de terceiros | Clientes | Receita de vendas |
| 5.405 | Venda de mercadoria recebida com ICMS-ST já retido (substituído) | Clientes | Receita de vendas |
| 5.101 / 6.101 | Venda de produção do estabelecimento | Clientes | Receita de vendas |
| 5.933 / 6.933 | Prestação de serviço tributado pelo ISS em NF-e conjugada | Clientes | Receita de serviços |
| 5.202 / 6.202 | Devolução de compra para comercialização | Fornecedores | Estoque de mercadorias |

Atenção: 1.922/2.922 e 5.922/6.922 são "simples faturamento" de compra ou venda para entrega futura, não são serviço. Nota com esses CFOPs não movimenta estoque; o estoque entra ou sai na nota de remessa (1.116/1.117 ou 5.116/5.117).

### 5. Validações normativas

**Receitas — NBC TG 47 (Receita de contrato com cliente)**
- A receita é reconhecida quando o controle do bem ou serviço passa ao cliente (cumprimento da obrigação de desempenho).
- O valor deve ser mensurável (preço da transação, líquido de descontos incondicionais e devoluções).
- Empresa que adota a NBC TG 1000 (contabilidade para pequenas e médias empresas) segue a seção 23 dessa norma.

**Estoques — NBC TG 16**
- Custo = preço de compra + frete + seguro + custos diretos de aquisição.
- Descontos comerciais e abatimentos são deduzidos.
- Tributos recuperáveis não entram no custo. **No Simples Nacional, em regra, o ICMS, o PIS e a COFINS das compras não são recuperáveis, então integram o custo do estoque.**

**Simples Nacional — LC nº 123/2006**
- Entradas: PIS/COFINS destacados pelo fornecedor não geram crédito para a optante. ICMS só gera crédito se a optante estiver fora do ICMS do DAS (sublimite estourado).
- Saídas: os tributos são pagos no DAS e não se destacam como no regime normal. Exceção: a optante pode informar crédito de ICMS ao comprador contribuinte (CSOSN 101), na forma do art. 23 da LC nº 123/2006.
- Reforma Tributária (Emenda Constitucional nº 132/2023 e LC nº 214/2025): em 2026, ano-teste, as notas do regime normal (CRT 3) devem trazer CBS 0,9% e IBS 0,1%; desde 03/08/2026 a NF-e do regime normal sem esses grupos é rejeitada. Para optantes do Simples e MEI (CRT 1, 2 e 4), a rejeição começa em 04/01/2027 (Ato Conjunto RFB/CGIBS nº 4/2026). Na entrada, conferir se a nota de fornecedor CRT 3 trouxe os grupos; a falta não muda o lançamento contábil de 2026, mas é ressalva.

**NFS-e — retenções (serviço tomado de pessoa jurídica)**
- ISS: retém quando a lei do município do tomador manda, ou nos casos do art. 6º, §2º, da LC nº 116/2003. Prestador do Simples: reter pela alíquota informada na nota (art. 21, §4º, da LC nº 123/2006).
- IRRF: 1,5% em serviços profissionais (art. 714 do RIR/2018 — Decreto nº 9.580/2018) ou 1% em limpeza, conservação, segurança, vigilância e locação de mão de obra (art. 716 do RIR/2018). Dispensado quando o valor do imposto for de até R$ 10,00 (art. 67 da Lei nº 9.430/1996), avaliado a cada pagamento pelo total pago naquela ocasião, ainda que cubra mais de uma nota (Solução de Consulta Cosit nº 258/2024); a 1,5%, equivale a pagamento de até R$ 666,66. Comissões e corretagens: 1,5%, código 8045 (art. 718 do RIR/2018).
- CSRF (PIS + COFINS + CSLL, 4,65%): dispensada quando a retenção do pagamento for de até R$ 10,00 (pagamento de até R$ 215,05), avaliando pagamento a pagamento, sem somar o mês (Lei nº 10.833/2003, arts. 30 a 32, com a Lei nº 13.137/2015).
- INSS 11%: só em cessão de mão de obra ou empreitada de serviço listado nos arts. 111 e 112 da IN RFB nº 2.110/2022 (art. 31 da Lei nº 8.212/1991). Prestador do Simples: só o Anexo IV sofre a retenção (arts. 166 e 167 da IN RFB nº 2.110/2022). MEI não sofre a retenção.
- Prestador optante do Simples que entrega a declaração de optante fica dispensado de IRRF (art. 1º da IN RFB nº 765/2007) e de CSRF (art. 32, III, da Lei nº 10.833/2003; art. 3º, II, da IN SRF nº 459/2004).
- Empresa analisada optante do Simples, como tomadora: não é obrigada a reter a CSRF (art. 30, § 2º, da Lei nº 10.833/2003).
- Serviço prestado por pessoa física (autônomo) não é NFS-e de PJ: segue RPA, com desconto de 11% do contribuinte individual e CPP de 20% da empresa (regras próprias).

### 6. Formato de saída
Para cada nota: identificação (número, série, CNPJ emitente mascarado quando for PF, data), CFOP, lançamento esperado (D/C/valor), tributos conferidos, retenções esperadas × destacadas e status final (Aprovada / Aprovada com ressalvas / Reprovada) com justificativa. Ao final: resumo com totais por CFOP, totais retidos e principais alertas.

### 7. Restrições
- Não registrar nem lançar nenhuma nota: apenas analisar.
- XML corrompido ou ilegível: informar e passar para o próximo.
- Nunca omitir notas: todas aparecem no relatório, inclusive as reprovadas.

## Erros comuns / pontos de atenção
- Tratar 1.922/5.922 como serviço (são simples faturamento de entrega futura).
- Usar 1.403 como compra para industrialização (1.403 é comercialização com ST; industrialização é 1.101).
- Somar ICMS/PIS/COFINS das compras como crédito em empresa do Simples.
- Somar os pagamentos do mês para testar a dispensa da CSRF (a regra do acúmulo foi revogada).
- Reter INSS 11% de serviço que não está na lista da IN RFB nº 2.110/2022.
- Esquecer de pedir a declaração de optante ao prestador do Simples antes de dispensar IRRF/CSRF.

## Perguntas que o usuário costuma fazer
- "Nota de fornecedor do Simples me dá crédito de ICMS?" Só se vier com CSOSN 101 e o percentual informado, e se a sua empresa for do regime normal.
- "Preciso destacar CBS/IBS na minha nota do Simples em 2026?" Não é exigido sob rejeição antes de 04/01/2027.
- "Por que o IRRF não foi retido nesta NFS-e?" Verifique se o imposto ficaria até R$ 10,00 ou se o prestador é do Simples com declaração.

## Base legal usada nesta skill
- LC nº 123/2006 (Simples Nacional): art. 21, §4º (ISS retido de optante); art. 23 (crédito de ICMS).
- LC nº 116/2003 (ISS): art. 6º (responsabilidade do tomador).
- Decreto nº 9.580/2018 (RIR/2018): arts. 714, 716 e 718 (IRRF sobre serviços e comissões).
- Lei nº 9.430/1996: art. 67 (dispensa de IRRF de até R$ 10,00); Solução de Consulta Cosit nº 258/2024.
- Lei nº 10.833/2003: arts. 30 a 32 (CSRF); Lei nº 13.137/2015 (fim do acúmulo mensal).
- Lei nº 8.212/1991: art. 31; IN RFB nº 2.110/2022, arts. 110 a 112, 166 e 167 (retenção de 11%).
- IN RFB nº 765/2007, art. 1º, e IN SRF nº 459/2004, art. 3º (dispensa para optante do Simples).
- Emenda Constitucional nº 132/2023 e LC nº 214/2025 (CBS/IBS, ano-teste 2026); Ato Conjunto RFB/CGIBS nº 4/2026 (cronograma).
- NBC TG 47 (receita), NBC TG 16 (estoques), NBC TG 1000 seção 23 (PME).
- Ajuste SINIEF/Convênio S/Nº de 1970 (tabela de CFOP).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
