---
name: fechamento-mensal
description: "Roteiro completo do fechamento contábil mensal em até 5 dias úteis (D+1 a D+5) — conferência de entradas, conciliações (banco, cartões, fornecedores, clientes, tributos), provisões (CPC 33), perdas esperadas (CPC 48), depreciação e arrendamentos (CPC 27 e CPC 06 R2), apropriações financeiras, encerramento do resultado, balancete, DRE, BP, DFC (CPC 03) e pacote ao cliente. Acionar quando o usuário disser \"fechar o mês\", \"fechamento mensal\", \"fechamento contábil\", \"checklist de fechamento\", \"montar o pacote do cliente\", \"o que falta para fechar a competência\" ou pedir balancete, DRE e DFC do mês. Entrega: checklist mestre, demonstrações do mês e pacote ao cliente."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Fechamento contábil mensal

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Conduz o fechamento do mês em ordem, do recebimento dos documentos ao pacote entregue ao cliente, com uma trava em cada etapa: não se avança com documento faltando, conciliação com diferença ou provisão não lançada. Segue um roteiro de D+1 a D+5 e delega as conciliações e análises às skills específicas.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Todo mês, para cada cliente com escrituração completa.
- Cliente novo no primeiro fechamento (checar também saldos de abertura).
- Antes de gerar demonstrações para banco, licitação ou sócios.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). No pacote ao cliente, folha aparece por total, nunca por empregado.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere, transmite as obrigações e envia o pacote.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: Cliente (CNPJ), competência, tipo societário (Ltda./S.A.) e norma contábil adotada (CPCs completos, NBC TG 1000, NBC TG 1001 ou NBC TG 1002)?
Q2: Status: notas lançadas, folha processada, apurações de tributos lançadas?
Q3: Ficou pendência da conciliação do mês anterior?
Q4: O cliente contratou pacote analítico (DRE gerencial, indicadores, reunião)?
```

### 2. Roteiro D+1 a D+5

**D+1 — Documentos e lançamentos primários**
- Notas de entrada e saída completas (XML, cruzar com a EFD).
- Extratos bancários integrais.
- Folha processada e holerites.
- Apurações do mês (ICMS, ISS, PIS, COFINS, IRPJ, CSLL ou DAS).
- Lançar notas, folha, tributos, pagamentos e recebimentos (`lancamentos-contabeis-padrao`).
- **Trava:** não avançar com documento faltando (competência errada é o erro nº 1).

**D+2 — Conciliações**
- Bancos → `conciliar-extrato-razao`
- Cartões → `conciliacao-cartoes-credenciadora`
- Maiores fornecedores → `conciliacao-fornecedores`
- Maiores clientes e perdas esperadas → `conciliacao-clientes`
- Tributos a recolher: razão × DCTFWeb, GIA/EFD, PGDAS-D.
- **Trava:** nenhuma diferença "para regularizar depois".

**D+3 — Provisões, depreciação e apropriações**
- Provisão de férias + 1/3 + encargos e de 13º + encargos (CPC 33).
- Revisão da perda esperada com clientes (CPC 48; matriz pelo histórico do próprio cliente — `conciliacao-clientes`).
- Depreciação e amortização bem a bem (CPC 27 e CPC 04) → `ativo-imobilizado-depreciacao`.
- Arrendamentos (CPC 06 R2): amortização do direito de uso + juros do passivo de arrendamento.
- Juros de empréstimos (custo amortizado, CPC 48), variação cambial e rendimentos de aplicações, pela competência.
- **Trava:** bem não depreciado ou provisão não lançada distorce lucro e passivo.

**D+4 — Encerramento do resultado e balancete**
- Antes de encerrar: IRPJ e CSLL do período já lançados (despesa do próprio período).
- Encerramento (códigos de um plano-modelo, só como referência; usar o plano do cliente):
```
D 4.x Receitas                  | C 6.1.1.01 Apuração do Resultado (ARE)
D 6.1.1.01 ARE                  | C 5.x Custos e Despesas (inclui IRPJ/CSLL)
D 6.1.1.01 ARE                  | C 3.5.1.01 Lucros Acumulados      (se lucro)
D 3.5.1.02 Prejuízos Acumulados | C 6.1.1.01 ARE                    (se prejuízo)
```
- O encerramento mensal do resultado é opção da empresa: a lei exige as demonstrações ao fim do exercício (art. 176 da Lei nº 6.404/1976; art. 1.065 da Lei nº 10.406/2002 (Código Civil)). Encerrando só no fim do ano, o resto do roteiro continua mensal.
- S.A.: o saldo de Lucros Acumulados é transitório e tem de ser destinado (art. 202, § 6º, da Lei nº 6.404/1976).
- Conferir no balancete: Ativo = Passivo + PL; grupos 4 e 5 zerados (se encerramento mensal); ARE zerada; saldos invertidos; variações acima da materialidade combinada (na falta dela, 20% como corte provisório) com justificativa (`balancete-analise`).

**D+5 — Demonstrações e pacote ao cliente**
- DRE (mês e acumulado), BP, DFC e DMPL/DLPA quando exigidas.
- DFC (CPC 03 R2), método direto ou indireto. Fazer o "teste dos 4 cantos": a variação de caixa da DFC tem de ser igual à variação de caixa e equivalentes no BP.
- Relatório executivo e indicadores.
- Arquivamento digital por competência + cópia em nuvem e local.

### 3. Entregável
**a) Checklist mestre** (pode ir ao cliente para acompanhamento):
```
COMP __/____ — CNPJ __ — Cliente __

ENTRADAS
[ ] Notas de entrada (#) ___
[ ] Notas de saída (#) ___
[ ] Apuração de tributos lançada
[ ] Folha processada e lançada
[ ] Pagamentos e recebimentos do mês

CONCILIAÇÕES
[ ] Banco c/c 1: diferença zero
[ ] Banco c/c 2: diferença zero
[ ] Cartões: vendas × repasses
[ ] Maiores fornecedores
[ ] Maiores clientes
[ ] Tributos a recolher: razão × DCTFWeb / EFD / PGDAS-D

PROVISÕES E AJUSTES
[ ] Férias + 1/3 + encargos
[ ] 13º + encargos
[ ] Perda esperada (PCLD) revisada
[ ] Depreciação do imobilizado
[ ] Amortização do intangível
[ ] Direito de uso e juros de arrendamento (CPC 06 R2)
[ ] Juros de empréstimos
[ ] Variação cambial
[ ] IRPJ/CSLL do período lançados antes do encerramento

RELATÓRIOS
[ ] Balancete
[ ] DRE mês + acumulado
[ ] BP
[ ] DFC (teste dos 4 cantos)

OBRIGAÇÕES DO MÊS (conferir na Agenda Tributária oficial)
[ ] DCTFWeb: até o último dia útil do mês seguinte (IN RFB nº 2.248/2025)
[ ] eSocial S-1299 e EFD-Reinf R-2099/R-4099: dia 15 do mês seguinte
[ ] EFD-Contribuições: até o 10º dia útil do 2º mês seguinte (art. 7º da IN RFB nº 1.252/2012)
[ ] EFD ICMS/IPI: prazo fixado pela UF — conferir no regulamento do ICMS do estado do cliente
[ ] DARF de INSS e IRRF da folha: dia 20 (antecipa para o dia útil anterior se não houver expediente bancário); FGTS Digital: dia 20 (também antecipa)

REPORT
[ ] Pacote enviado
[ ] Reunião agendada
[ ] Pasta arquivada
```
**b) Balancete, DRE e BP** estruturados.
**c) DFC (CPC 03 R2)** — direto ou indireto.
**d) Pacote ao cliente** (documento):
```
FECHAMENTO __/____  Cliente __

DESTAQUES
* Receita líquida: R$ __ (var. __% contra o mês anterior)
* Margem bruta: __% (contra __% no mês anterior)
* Lucro operacional: R$ __ (margem __%)
* Lucro líquido: R$ __
* Caixa: R$ __ + aplicações R$ __

PRINCIPAIS VARIAÇÕES
1. __
2. __
3. __

INDICADORES
- Liquidez corrente: __
- Endividamento: __%
- PMR: __ dias  PMP: __ dias
- Giro de estoque: __ vezes/ano
- ROE acumulado: __%

PONTOS DE ATENÇÃO
[ ] __

RECOMENDAÇÕES
1. __
```

## Erros comuns / pontos de atenção
- Fechar antes de receber todas as notas do mês: competência errada no SPED e no IR.
- Esquecer provisão de férias e 13º: passivo subestimado, lucro e IR inflados.
- Não rodar a depreciação: ativo superavaliado, lucro maior.
- Conciliação com diferença "para o mês que vem": bola de neve.
- Encerrar o resultado sem lançar IRPJ/CSLL: lucro transferido ao PL maior que o real.
- ARE com saldo depois do encerramento.
- DFC que não fecha com o BP.
- Não lançar o encerramento quando o cliente adota regime mensal: resultado acumula e distorce o balancete.

### Quem é obrigado à DFC
- S.A. de capital aberto e S.A. fechada com PL de R$ 2.000.000,00 ou mais na data do balanço (art. 176, § 6º, da Lei nº 6.404/1976: a fechada com PL inferior a esse valor está dispensada).
- Sociedade de grande porte (art. 3º da Lei nº 11.638/2007).
- Entidade que adota a NBC TG 1000 (R1) (PME): a DFC faz parte do conjunto completo de demonstrações.
- Pequena empresa que adota a NBC TG 1001 (receita bruta anual acima de R$ 4,8 milhões até R$ 78 milhões): a DFC faz parte do conjunto completo (item 3.5 da norma).
- Microentidade que adota a NBC TG 1002 (receita bruta anual até R$ 4,8 milhões, limite do art. 3º, II, da Lei Complementar nº 123/2006): o conjunto completo é balanço patrimonial, demonstração do resultado e demonstração dos lucros ou prejuízos acumulados (item 3.6 da norma); a DFC não é exigida.
- As NBC TG 1001 e 1002 valem para exercícios iniciados a partir de 01/01/2023. A ITG 1000 atual traz modelos de plano de contas e de demonstrações para microentidade e pequena empresa.

### Casos de borda
- **Empresa com filiais:** consolidar; transferência entre estabelecimentos do mesmo titular não tem ICMS (ADC 49 do STF; Lei Complementar nº 204/2023).
- **Cliente em recuperação judicial:** passivo sujeito ao plano reclassificado conforme o plano homologado.
- **PME (NBC TG 1000) e pequenas e microentidades (NBC TG 1001 e 1002):** simplificações permitidas por cada norma; o encerramento do resultado pode ser só no fim do exercício.
- **2026, ano-teste da Reforma Tributária:** CBS e IBS destacados nos documentos (Lei Complementar nº 214/2025); quem cumpre as obrigações acessórias fica dispensado do recolhimento (art. 348, § 1º, da mesma lei). Em 15/11/2026 não foi localizada norma ou orientação técnica do CFC ou do CPC que fixe um tratamento contábil único para os valores destacados: o contador responsável define o critério, registra a política adotada e a mantém igual todos os meses.

### Quando escalar
- DRE gerencial → `dre-gerencial`
- Análise de balancete → `balancete-analise`
- Fluxo de caixa projetado → `fluxo-caixa-projetado`
- Cruzamento de SPEDs → `revisao-fiscal-cruzamento-sped`
- Prazos de obrigações → a agenda de prazos do seu escritório

### Autoavaliação
- [ ] Entradas completas?
- [ ] Conciliações com diferença zero?
- [ ] Provisões, depreciação e IRPJ/CSLL lançados?
- [ ] Resultado encerrado e ARE zerada?
- [ ] Relatórios gerados e DFC × BP conferidos?
- [ ] Análise gerencial preparada?
- [ ] Obrigações do mês conferidas na Agenda Tributária?
- [ ] Pacote ao cliente?

### Arquivamento
Pasta digital por competência, cópia em nuvem e local. Guardar livros e documentos enquanto não prescritos os créditos tributários (parágrafo único do art. 195 da Lei nº 5.172/1966 (CTN)), o que na prática é **no mínimo 5 anos** (arts. 173 e 174 do CTN), e por mais tempo quando houver prazo específico (trabalhista e previdenciário).

## Formato de entrega
- Cálculos, apurações e conciliações: entregar sempre planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar sempre documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Perguntas que o usuário costuma fazer
- **"Preciso zerar o resultado todo mês?"** Não é obrigatório; a lei exige as demonstrações ao fim do exercício. O restante do fechamento é mensal.
- **"Qual o prazo da DCTFWeb?"** Último dia útil do mês seguinte (IN RFB nº 2.248/2025). Conferir sempre a Agenda Tributária do ano.
- **"Ltda. pequena precisa de DFC?"** Depende da norma adotada: NBC TG 1000 e NBC TG 1001 exigem; NBC TG 1002 (microentidade) não exige.

## Base legal usada nesta skill
- Arts. 176 (§ 6º, dispensa da DFC), 177 (competência), 187 (DRE) e 202, § 6º (destinação dos lucros), da Lei nº 6.404/1976.
- Art. 3º da Lei nº 11.638/2007 — sociedades de grande porte.
- CPC 26 (R1) — apresentação; CPC 03 (R2) — DFC; CPC 33 (R1) — benefícios a empregados; CPC 48 — instrumentos financeiros e perdas esperadas; CPC 27 — imobilizado; CPC 04 (R1) — intangível; CPC 06 (R2) — arrendamentos.
- NBC TG 1000 (R1) — PME; NBC TG 1001 — pequenas empresas (item 3.5, conjunto de demonstrações); NBC TG 1002 — microentidades (item 3.6, conjunto de demonstrações); ITG 1000 — modelos para microentidade e pequena empresa; ITG 2000 (R1) — escrituração.
- Art. 1.065 da Lei nº 10.406/2002 (Código Civil) — balanço patrimonial e de resultado ao fim do exercício (sociedade limitada).
- IN RFB nº 2.248/2025 — prazo da DCTFWeb; art. 7º da IN RFB nº 1.252/2012 — prazo da EFD-Contribuições.
- Art. 15 da Lei nº 8.036/1990 (redação da Lei nº 14.438/2022) — FGTS até o dia 20.
- Lei Complementar nº 214/2025, art. 348, § 1º — dispensa do recolhimento de CBS e IBS em 2026 para quem cumpre as obrigações acessórias.
- Arts. 173, 174 e 195, parágrafo único, da Lei nº 5.172/1966 (CTN) — decadência, prescrição e guarda de livros.
- ADC 49 do STF e Lei Complementar nº 204/2023 — transferência entre estabelecimentos sem ICMS.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
