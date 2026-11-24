---
name: revisao-fiscal-cruzamento-sped
description: "Cruza as escriturações e declarações da empresa — ECD, ECF, EFD ICMS/IPI, EFD-Contribuições, eSocial, EFD-Reinf e DCTFWeb (com o MIT desde 2025) — para achar divergências antes da malha fiscal ou durante diligência. Entrega espelho de divergências por valor e criticidade, causa de cada uma e plano de retificação na ordem correta (da origem para o destino). Acionar quando o usuário disser \"cruzar SPED\", \"conferir ECD com ECF\", \"bater DCTFWeb com eSocial\", \"revisão fiscal\", \"auditoria interna trimestral\", \"antes de transmitir a ECF\", \"divergência entre declarações\", \"preparar para due diligence\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Revisão fiscal por cruzamento de SPEDs

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Monta o espelho de cruzamento entre as escriturações digitais da empresa no período, mede cada diferença, classifica por valor e criticidade e explica a causa. Depois propõe a correção na ordem certa: primeiro os eventos de origem (eSocial e EFD-Reinf), depois a DCTFWeb, as EFDs, a ECD e por último a ECF.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Auditoria interna trimestral.
- Antes de transmitir a ECF (depois da ECD).
- Due diligence de compra ou venda de empresa.
- Intimação recebida ou suspeita de divergência.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Arquivos do eSocial trazem dados de empregados: trabalhar com totais.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
P1: Período (ano) e regime? Tenho ECD, ECF, EFDs, DCTFWeb (e DCTF até 2024), eSocial e EFD-Reinf?
P2: Objetivo: cruzamento antes da ECF, due diligence ou resposta a intimação?
P3: Tolerância: 0,1% da receita é aceitável? Ou valor absoluto?
P4: Relatório executivo (5 maiores divergências) ou analítico (todas)?
```

### 2. Cruzamentos obrigatórios
```
1. RECEITA: ECD (DRE, J150) × ECF (L300 no Lucro Real; P150/P200 no Presumido)
   × EFD-Contribuições (bloco M e registros de receita) × DCTFWeb/MIT (débitos)
   Blocos da ECF usados aqui (Manual da ECF): K = saldos das contas contábeis e referenciais;
   L = lucro líquido (Lucro Real; L300 = DRE); M = e-Lalur e e-Lacs; N = cálculo do IRPJ e
   da CSLL no Real; P = Lucro Presumido (P150 = DRE; P200 = base do IRPJ)
   Tolerância: até 0,1%. Acima de 1% acende alerta.
   Causas comuns: ICMS (Tema 69) excluído numa escrituração e não em outra; exportação tratada
   de forma diferente; receita financeira composta de forma diferente.

2. CMV / CUSTO DOS SERVIÇOS: ECD × ECF × Bloco K da EFD ICMS/IPI (produção e estoque)

3. FOLHA: eSocial S-5011 × DCTFWeb × despesa de pessoal na ECD
   - S-5011 (totalizador das contribuições) = débitos previdenciários da DCTFWeb
   - Folha do eSocial = despesa de pessoal da ECD ± provisões do mês
   - INSS retido de terceiros (EFD-Reinf R-2010) = retenção confessada na DCTFWeb

4. RETENÇÕES: notas fiscais × EFD-Reinf (série R-4000) × DCTFWeb
   - IRRF (folha, PJ, PF) = R-4010/R-4020 = DCTFWeb (códigos 0561, 1708 etc.)
   - Para anos até 2024, conferir também a DIRF (extinta para fatos a partir de 2025)

5. ICMS: EFD ICMS/IPI (E110 — saldo a recolher) = ICMS a recolher na ECD = guias pagas

6. PIS/COFINS: EFD-Contribuições (M200/M600) = PIS/COFINS a recolher na ECD = DCTFWeb/MIT
   (até 12/2024: DCTF)

7. IRPJ/CSLL: ECF (bloco N no Real; P no Presumido) × DCTFWeb/MIT × DARFs pagos

8. IMOBILIZADO: aquisições na ECD × Bloco G da EFD ICMS/IPI (CIAP, G125)

9. REFORMA TRIBUTÁRIA (2026): CBS/IBS destacados nas notas × escrituração do ano-teste
   (LC nº 214/2025) — divergência ainda sem efeito de caixa, mas indica erro de cadastro
```

### 3. Espelho de divergências
```
EMPRESA EXEMPLO — CNPJ 00.000.000/0001-00 — Período: ____
Legenda de situação: OK / REVISAR / URGENTE

DIMENSÃO         ECD     ECF     EFD-C   DCTFWeb  OUTRA       SITUAÇÃO
Receita bruta    ____    ____    ____    ____     ____        REVISAR
Receita export.  ____    ____    ____    n/a      ____        OK
CMV              ____    ____    ____    n/a      Bloco K     OK
Folha total      ____    ____    n/a     ____     eSocial     URGENTE
INSS retido      n/a     ____    n/a     ____     Reinf       OK
PIS              ____    ____    ____    ____     n/a         REVISAR
COFINS           ____    ____    ____    ____     n/a         REVISAR
ICMS débito      ____    n/a     n/a     n/a      EFD ICMS    OK
IRPJ             ____    ____    n/a     ____     DARF        OK
```

### 4. Ordem de retificação (sempre da origem para o destino)
```
1. Origem: eSocial e EFD-Reinf (reabrir e fechar de novo: S-1299, R-2099, R-4099)
2. Aguardar os totalizadores
3. DCTFWeb (gerada a partir dos eventos) e MIT (IRPJ, CSLL, PIS, COFINS, IPI desde 01/2025): retificar
4. EFD-Contribuições / EFD ICMS/IPI: retificar
5. ECD: substituir (se o erro é contábil), com os requisitos da IN RFB nº 2.003/2021
6. ECF: retificar por último (importa os saldos da ECD)
7. Pagar a diferença com Selic, quando houver
```

### 5. Entregáveis
**a) Espelho de divergências** (acima).
**b) Causa de cada divergência**
```
Divergência 1 — Folha eSocial × ECD: R$ ____
- Causa: provisão de férias não lançada na ECD do mês X
- Correção: lançar a provisão (CPC 33) e substituir a ECD
- Risco se não corrigir: passivo subavaliado

Divergência 2 — PIS DCTFWeb/MIT × EFD-Contribuições: R$ ____
- Causa: EFD retificada sem retificar o MIT/DCTFWeb
- Correção: retificar a DCTFWeb da competência
- Risco: cobrança da diferença com Selic
```
**c) Plano de ação** com cronograma
```
Semana 1: retificar eventos do eSocial/EFD-Reinf
Semana 2: retificar DCTFWeb/MIT
Semana 3: retificar EFDs
Semana 4: substituir a ECD do mês com a provisão
Semana 5: pagar a diferença de IRPJ com Selic e retificar a ECF
```
**d) Memória do trabalho** (relatório assinado, anexos, cálculos) — útil em auditoria, fiscalização e M&A.

## Erros comuns / pontos de atenção
- Concluir "está tudo certo" porque a DCTFWeb foi entregue: o débito pode estar errado.
- Chamar diferença de "imaterial" sem critério definido (fixar a tolerância antes).
- Retificar a EFD de meses antigos sem retificar a DCTF/DCTFWeb correspondente.
- Esquecer que, desde 01/2025, PIS/COFINS/IRPJ/CSLL entram pelo MIT: a EFD-Contribuições não alimenta a DCTFWeb sozinha.
- Cruzar à mão em planilha, sem validador nem trilha de conferência.
- Não documentar a causa de cada divergência.
- Retificar depois do início de fiscalização achando que recupera a espontaneidade (não recupera — art. 7º do Decreto nº 70.235/1972).

**Casos de borda**
- **Filiais**: transferências entre estabelecimentos do mesmo titular não têm incidência de ICMS (STF, ADC 49), com a transferência de créditos regulada pela LC nº 204/2023 e pela legislação de cada estado.
- **Empresa em recuperação judicial**: débitos antigos no plano; correntes na DCTFWeb normal.
- **Mudança de regime no meio do ano** (exclusão do Simples, por exemplo): cruzar por período.

## Perguntas que o usuário costuma fazer
- **"Por onde começo a retificar?"** Sempre pela origem: eSocial e EFD-Reinf, depois DCTFWeb, EFDs, ECD e ECF.
- **"Qual tolerância usar?"** 0,1% da receita como referência; acima de 1% é alerta. Definir com o responsável técnico.
- **"A DIRF ainda entra no cruzamento?"** Só para anos até 2024.

## Formato de entrega
- Cálculos, apurações e conciliações: sempre planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): sempre documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- IN RFB nº 2.003/2021 — ECD (inclusive substituição).
- IN RFB nº 2.004/2021 — ECF; Manual da ECF publicado no portal do SPED (leiaute dos blocos K, L, M, N e P).
- IN RFB nº 2.043/2021 — EFD-Reinf.
- IN RFB nº 2.005/2021 — DCTFWeb (fatos até 12/2024) e IN RFB nº 2.237/2024 — DCTFWeb com MIT (fatos desde 01/2025).
- IN RFB nº 1.252/2012 — EFD-Contribuições.
- Convênio ICMS nº 143/2006 e Ajuste SINIEF nº 2/2009 — EFD ICMS/IPI.
- Decreto nº 8.373/2014 — eSocial.
- Decreto nº 70.235/1972 — art. 7º (perda da espontaneidade).
- STF, ADC 49, e LC nº 204/2023 — transferência entre estabelecimentos do mesmo titular.
- CPC 33 (NBC TG 33) — benefícios a empregados (provisões de férias e 13º).
- Emenda Constitucional nº 132/2023 e LC nº 214/2025 — CBS/IBS no ano-teste de 2026.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
