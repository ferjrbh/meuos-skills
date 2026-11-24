---
name: encerramento-empresa-baixa
description: "Conduz a baixa de empresa pela REDESIM — baixa regular ou com débitos pendentes (art. 7º-A da Lei nº 11.598/2007: a baixa não extingue os débitos e gera responsabilidade solidária de titulares, sócios e administradores), distrato com liquidante, encerramento contábil (realizar ativo, pagar passivo, partilhar acervo), declarações de situação especial (ECD, ECF, DEFIS, DCTFWeb, EFD-Reinf, eSocial S-2299 dos empregados) e efeitos no IRPF do sócio na devolução de capital e na partilha de lucros (Lei nº 9.249/1995 e Lei nº 15.270/2025). Acionar quando o usuário disser \"encerrar empresa\", \"dar baixa no CNPJ\", \"fechar empresa\", \"distrato\", \"empresa parada\", \"baixa com débito\". Entrega: distrato, cronograma, lista de declarações finais e plano de comunicação aos credores."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Encerramento de empresa (baixa)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Planeja e controla o fechamento de uma empresa: escolhe o caminho (baixa regular, baixa com débitos, dissolução judicial ou falência), roteiriza distrato e liquidação, lista as declarações de situação especial e calcula o reflexo para o sócio pessoa física.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Cliente decidiu encerrar a empresa.
- Empresa parada que acumula obrigações acessórias e multas por atraso.
- Não usar para saída de um sócio com a empresa continuando (`alteracao-contratual`).

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Explicar ao cliente, por escrito, que a baixa com débitos NÃO apaga a dívida (ver passo 2) antes de protocolar.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: CNPJ, regime tributário, motivo e data prevista do encerramento?
Q2: Há débitos (RFB, PGFN, Estado, Município, FGTS)? Parcelamentos ativos?
Q3: Empregados ativos? Folha ou rescisões pendentes?
Q4: Bens a partilhar (estoque, imobilizado, imóveis, veículos)? Saldo de lucros acumulados?
    De que ano são esses lucros e se a distribuição foi aprovada até 31/12/2025?
Q5: Filiais? Atividade regulamentada (conselho profissional)?
Q6: Quem será o liquidante?
```

### 2. Tipos de encerramento
```
1. Baixa regular: obrigações entregues, tributos pagos ou parcelados, empregados desligados.
2. Baixa com débitos (art. 7º-A da Lei nº 11.598/2007; para ME/EPP também art. 9º da
   LC nº 123/2006): o registro da baixa não depende de certidão negativa, MAS os débitos
   continuam exigíveis, e titulares, sócios e administradores respondem solidariamente
   pelos tributos e multas do período dos fatos geradores.
3. Dissolução judicial: litígio entre sócios → advogado parceiro.
4. Falência (Lei nº 11.101/2005): insolvência → advogado parceiro.
```

### 3. Sequência operacional
```
1. Ato de dissolução/distrato: designa liquidante e data (arts. 1.033, 1.038 e 1.102 a
   1.112 do CC). Na LTDA, a dissolução exige mais da metade do capital (art. 1.076 do CC,
   red. Lei nº 14.451/2022), salvo contrato com quórum maior.
2. Liquidação contábil:
   - balanço de abertura da liquidação e balanço final;
   - realizar o ativo (vender estoque COM nota fiscal, receber clientes);
   - pagar o passivo (fornecedores, tributos, folha, rescisões);
   - partilhar o acervo líquido entre os sócios na proporção das quotas.
3. Rescisão de empregados e eSocial S-2299; S-1299 do último mês; FGTS Digital quitado.
4. Declarações de situação especial (extinção) — ver passo 5.
5. Cancelamento de inscrição estadual, municipal, alvarás e conselho profissional.
6. Baixa via REDESIM (DBE de baixa) + registro do distrato na Junta (ou Cartório).
7. Comprovante de baixa do CNPJ.
8. Guarda de livros e documentos (passo 7).
```

### 4. Partilha do acervo — efeitos para o sócio pessoa física
```
Acervo líquido = ativo realizado − passivo pago = capital + reservas + lucros acumulados

a) Parcela de LUCROS/RESERVAS DE LUCROS:
   - resultados até 2025 com distribuição aprovada até 31/12/2025 e paga conforme o ato:
     isentos (art. 10 da Lei nº 9.249/1995);
   - resultados de 2026 em diante: retenção de 10% se a PJ pagar ao mesmo sócio PF mais
     de R$ 50.000,00 no mês (art. 6º-A da Lei nº 9.250/1995, incluído pela Lei nº 15.270/2025),
     e o valor entra no cálculo do IRPFM do sócio se a renda dele passar de R$ 600.000,00.

b) DEVOLUÇÃO DE CAPITAL EM BENS:
   - a PJ escolhe valor contábil ou de mercado (art. 22 da Lei nº 9.249/1995);
   - se de mercado, o ganho é tributado NA EMPRESA (§ 1º) e a diferença NÃO é tributada
     na pessoa física (§ 4º); o sócio declara o bem pelo valor atribuído (§ 3º).
   - Perguntas e Respostas IRPF 2026, pergunta 606.

c) DEVOLUÇÃO EM DINHEIRO:
   - separar o acervo em capital, reservas de capital e lucros (com o ano de apuração);
   - a parte que corresponde a lucros segue a regra do item a);
   - se o valor recebido como devolução de capital superar o custo de aquisição das quotas
     na declaração do sócio PF, a Receita trata o excesso como ganho de capital (alíquotas
     de 15% a 22,5% da Lei nº 13.259/2016, DARF 4600 até o último dia útil do mês seguinte —
     skill `irpf-ganho-capital`); devolução de capital formado por lucros isentos (regra de
     transição) não sofre a nova tributação de dividendos (Perguntas e Respostas da Receita
     sobre tributação de altas rendas — lucros e dividendos, dez/2025, orientação não
     vinculante: conferir a versão vigente no gov.br).

d) Bens partilhados: transferir registro (imóvel em cartório, veículo no Detran);
   ITBI pode incidir na transferência de imóvel ao sócio (lei municipal).
```

### 5. Declarações finais (situação especial: extinção)
```
Regime            Declaração                         Observação
Todos             DCTFWeb e EFD-Reinf até a          EFD-Reinf R-4000 substitui a DIRF
                  competência da baixa               (DIRF extinta para fatos a partir de 2025)
Todos             eSocial: S-2299, S-1299 final,     Fechar eventos antes do DBE de baixa
                  encerramento do empregador
Simples           DEFIS de situação especial         evento de jan a abr: até o último dia de
                                                     junho; demais: último dia do mês seguinte
                                                     ao evento (art. 72, § 2º, da Resolução
                                                     CGSN nº 140/2018)
Simples           PGDAS-D até o mês da extinção
Presumido/Real    ECD de situação especial           evento de jan a mai: último dia útil de
                                                     junho do mesmo ano; de jun a dez: último
                                                     dia útil do mês seguinte ao evento
Presumido/Real    ECF de situação especial           evento de jan a abr: último dia útil de
                                                     julho do mesmo ano; de mai a dez: último
                                                     dia útil do 3º mês seguinte ao evento
Presumido/Real    EFD-Contribuições e EFD ICMS/IPI   até a última competência
                  (quando obrigada)
```
Prazos de ECD e ECF conforme as Perguntas Frequentes do SPED da Receita Federal (gov.br, ECD e ECF), com base na IN RFB nº 2.003/2021 (ECD) e na IN RFB nº 2.004/2021 (ECF). A Resolução CGSN nº 190/2026 altera a Resolução CGSN nº 140/2018 a partir de 01/01/2027: para extinção ocorrida em 2027 em diante, conferir o prazo da DEFIS na redação vigente. Detalhes de geração → skills `ecd-escrituracao-contabil-digital` e `ecf-escrituracao-contabil-fiscal`.

### 6. Distrato — modelo
```
DISTRATO SOCIAL DA EMPRESA EXEMPLO LTDA

SÓCIO A, [qualificação], e SÓCIO B, [qualificação], únicos sócios da EMPRESA EXEMPLO LTDA,
CNPJ __, NIRE __, resolvem dissolver e liquidar a sociedade:

1. Data da dissolução: __/__/__.
2. Liquidante: SÓCIO __, com os poderes e deveres dos arts. 1.103 a 1.105 do Código Civil.
3. Balanço final em __/__/__: Ativo R$ __ | Passivo R$ __ | Acervo líquido R$ __.
4. Partilha: SÓCIO A R$ __ (bens/dinheiro: __) | SÓCIO B R$ __ (bens/dinheiro: __).
5. Responsabilidade: os sócios ficam cientes de que eventuais débitos remanescentes
   continuam exigíveis e de que respondem nos termos da lei (art. 7º-A da Lei nº 11.598/2007).
6. Guarda dos livros e documentos: __, pelo prazo legal.

[Local, data] — [Assinaturas]
[Visto de advogado: dispensado para ME/EPP (art. 9º, § 2º, da LC nº 123/2006)]
```

**Regra de uso — visto de advogado:** toda vez que gerar o distrato, PERGUNTAR ao contador "A empresa é ME ou EPP e posso dispensar o visto de advogado? (sim/não)". Sem a confirmação, manter a linha do visto no modelo. O art. 1º, § 2º, da Lei nº 8.906/1994 exige o visto nos atos constitutivos, e o art. 9º, § 2º, da LC nº 123/2006 o dispensa para ME e EPP; para empresa que não seja ME/EPP, conferir na Junta Comercial (ou no Cartório) da UF se o visto é exigido no distrato.

### 7. Entregável obrigatório
**a) Cronograma**
```
EMPRESA EXEMPLO LTDA — encerramento previsto __/__/__

PRÉ-BAIXA
[ ] Distrato aprovado e assinado
[ ] Balanço final levantado
[ ] Ativo realizado (estoque vendido com NF)
[ ] Passivo pago ou parcelado (cliente ciente da responsabilidade)
[ ] Empregados rescindidos (`rescisao-clt-calculo`) e S-2299 enviados
[ ] Contratos (aluguel, sistemas, telefonia) encerrados

OBRIGAÇÕES FINAIS
[ ] DCTFWeb e EFD-Reinf da última competência
[ ] EFDs da última competência (se obrigada)
[ ] DEFIS (Simples) ou ECD/ECF de situação especial (Presumido/Real)
[ ] eSocial S-1299 final
[ ] FGTS Digital quitado ou parcelado
[ ] Certidões (federal, estadual, municipal, FGTS) — se baixa regular

CANCELAMENTOS
[ ] Inscrição estadual
[ ] Inscrição municipal e alvará
[ ] Conselho profissional
[ ] Procurações e certificados digitais

REDESIM
[ ] DBE de baixa
[ ] Registro do distrato na Junta / Cartório
[ ] Comprovante de baixa do CNPJ

PÓS-BAIXA
[ ] Conta bancária PJ encerrada
[ ] Clientes e fornecedores comunicados
[ ] Partilha registrada; tributos do sócio avaliados (passo 4)
[ ] Bens transferidos (cartório / Detran)
[ ] Documentos arquivados
```
b) Distrato (modelo do passo 6).
c) Lista de declarações finais com responsável e prazo.
d) Memória da partilha por sócio com o tratamento tributário de cada parcela.

### 8. Guarda de documentos
Guardar livros e documentos enquanto não prescritas as ações relativas aos atos neles registrados (art. 1.194 do CC) e, no mínimo, até o fim do prazo de decadência e prescrição tributárias (arts. 173 e 174 do CTN — Lei nº 5.172/1966). Na prática, orientar o arquivo por pelo menos 5 anos contados do 1º dia do exercício seguinte ao último fato gerador, e por mais tempo se houver débito, parcelamento ou processo em andamento.

## Erros comuns / pontos de atenção
- Deixar empresa parada "esperando": continuam as obrigações acessórias e as multas por atraso.
- Dar baixa sem fechar o eSocial: o encerramento trava.
- Estoque partilhado sem nota fiscal: autuação estadual.
- Partilhar lucros de 2026 acima de R$ 50.000,00/mês ao sócio sem reter os 10%.
- Achar que a baixa com débitos "zera" a dívida: ela passa a ser cobrada dos responsáveis.
- Parcelamento ativo abandonado: rescisão e inscrição em dívida ativa.
- Imóvel ou veículo da empresa partilhado sem transferir o registro.

## Casos de borda
- **Recuperação judicial ou insolvência**: advogado parceiro (falência ou convolação).
- **Bens financiados**: quitar ou transferir com anuência do credor.
- **Filiais**: baixar as filiais antes da matriz.
- **Sócio sem renda que recebe acervo alto**: o valor recebido justifica o acréscimo patrimonial no IRPF se bem documentado.

## Perguntas que o usuário costuma fazer
- **"Posso fechar com dívida?"** Pode registrar a baixa, mas a dívida continua e os sócios/administradores respondem solidariamente.
- **"O que eu recebo na partilha paga imposto?"** Depende: lucros até 2025 na regra de transição, isentos; lucros de 2026 acima de R$ 50.000,00/mês, retenção de 10%; devolução de capital em bens, sem IR na PF; devolução em dinheiro acima do custo das quotas, ganho de capital.

## Quando escalar
- Insolvência / litígio → advogado parceiro com OAB
- Ganho de capital do sócio → `irpf-ganho-capital`
- Parcelar antes de encerrar → `parcelamento-receita-federal`
- ECD/ECF de situação especial → `ecd-escrituracao-contabil-digital` e `ecf-escrituracao-contabil-fiscal`

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências: documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Lei nº 11.598/2007 — art. 7º-A (baixa independente de regularidade; responsabilidade solidária).
- Lei Complementar nº 123/2006 — art. 9º (baixa de ME/EPP; visto de advogado).
- Lei nº 10.406/2002 (Código Civil) — arts. 1.033 a 1.038 (dissolução), 1.076 (quórum), 1.102 a 1.112 (liquidação), 1.194 (guarda de documentos).
- Lei nº 14.451/2022 — quórum das LTDAs.
- Lei nº 9.249/1995 — art. 10 (lucros) e art. 22 (devolução de capital em bens).
- Lei nº 9.250/1995 — arts. 6º-A e 16-A (incluídos pela Lei nº 15.270/2025).
- Lei nº 15.270/2025 — tributação de lucros a partir de 2026.
- Lei nº 13.259/2016 — alíquotas do ganho de capital.
- Lei nº 5.172/1966 (CTN) — arts. 173 e 174 (decadência e prescrição).
- Lei nº 11.101/2005 — falência e recuperação.
- Resolução CGSN nº 140/2018 — art. 72, § 2º (DEFIS de situação especial) e PGDAS-D.
- Instrução Normativa RFB nº 2.003/2021 (ECD) e nº 2.004/2021 (ECF) — prazos de situação especial conforme Perguntas Frequentes do SPED (Receita Federal).
- Perguntas e Respostas IRPF 2026 — pergunta 606 (devolução de capital em bens).
- Receita Federal — Perguntas e Respostas sobre a tributação de altas rendas (lucros e dividendos), dez/2025 — devolução de capital e ganho de capital (orientação não vinculante).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
