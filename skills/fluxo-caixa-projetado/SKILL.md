---
name: fluxo-caixa-projetado
description: "Monta o fluxo de caixa pelo método direto, realizado e projetado — diário (4 semanas), semanal (3 meses) e mensal (12 meses) — com 3 cenários (otimista, realista, pessimista), entradas e saídas pela data de recebimento e pagamento (regime de caixa), calendário de tributos e folha, linhas de crédito disponíveis e identificação de déficits e sobras. Acionar quando o usuário disser \"fluxo de caixa\", \"projeção de caixa\", \"vai faltar dinheiro\", \"capital de giro\", \"antecipar recebíveis\", \"quando o caixa fica negativo\", \"sazonalidade\" ou \"planejar dezembro e janeiro\". Entrega: planilha semanal ou mensal com 3 cenários, déficits e sobras sinalizados e plano de ação para o cliente decidir."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Fluxo de caixa projetado

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Mostra semana a semana (ou mês a mês) quanto dinheiro entra, quanto sai e quanto sobra, pelas datas reais de recebimento e pagamento. Antecipa os buracos de caixa para o cliente decidir com tempo: negociar prazo, antecipar recebíveis, usar linha de crédito ou adiar investimento.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Não é recomendação de investimento.** A skill aponta sobras e faltas de caixa e lista as
> alternativas. A escolha de aplicação financeira ou de crédito é do cliente, com o banco ou
> com profissional habilitado.

## Quando usar
- Cliente com sazonalidade forte ou prazos de recebimento maiores que os de pagamento.
- Antes de dezembro (13º, férias coletivas) e de meses de tributos anuais.
- Decisão de compra de máquina, contratação ou empréstimo.
- A DFC oficial (CPC 03) do período encerrado sai do fechamento (`fechamento-mensal`); esta skill trata do caixa gerencial e da projeção.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Folha entra pelo total, não por empregado.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e apresenta ao cliente.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
Q1: Cliente (CNPJ) e saldo inicial (caixa + bancos + aplicações de resgate imediato)?
Q2: Recebíveis com vencimento (clientes a vencer, cartões a receber, boletos)?
Q3: Contas a pagar com vencimento (fornecedores, tributos, folha, empréstimos)?
Q4: Compromissos fixos: aluguel, folha, encargos, tributos, parcelas?
Q5: Linhas de crédito disponíveis (cheque especial, capital de giro, antecipação)?
Q6: Sazonalidade — como foram, no histórico, os meses fortes e fracos (ex.: dezembro × janeiro)?
Q7: Regime tributário (Simples, Presumido, Real) — define o calendário dos tributos.
```

### 2. Estrutura — método direto
```
SALDO INICIAL DO PERÍODO

(+) ENTRADAS (pela data do dinheiro na conta)
  Recebimentos de clientes (boletos, PIX, transferências)
  Repasses de cartões (valor líquido, na data do repasse)
  Adiantamentos e sinais
  Empréstimos captados
  Aporte de sócio
  Outras

(−) SAÍDAS
  Fornecedores (vencimentos)
  Folha (líquido) e adiantamento quinzenal
  Encargos da folha: DARF de INSS e IRRF (DCTFWeb) dia 20; FGTS Digital dia 20
  Tributos: DAS dia 20; PIS/COFINS dia 25; IRPJ/CSLL conforme o regime;
            ICMS e ISS conforme estado e município
  13º salário: 1ª parcela até 30/11 e 2ª até 20/12
  Aluguel, contas de consumo, marketing
  Pró-labore e distribuição de lucros
  Empréstimos (juros + amortização)
  Investimentos (máquinas, obras, sistemas)
  Anuais: IPTU, IPVA, seguros, licenças, dissídio da categoria

= SALDO FINAL DO PERÍODO

(+) Disponibilidades complementares
  Cheque especial não usado: R$ __
  Antecipação de recebíveis disponível: R$ __
  Capital de giro contratado e não sacado: R$ __
= LIQUIDEZ TOTAL DISPONÍVEL
```
Datas que caem em dia não útil:
- DARF de INSS e IRRF da folha (dia 20) e de PIS/COFINS (dia 25): antecipados para o dia útil anterior (art. 10 da Lei nº 10.637/2002 e art. 11 da Lei nº 10.833/2003, com a redação da Lei nº 11.933/2009, para PIS e COFINS).
- FGTS Digital (dia 20): antecipado para o dia útil anterior, conforme a orientação da CAIXA para o FGTS Digital.
- DAS do Simples Nacional (dia 20): segue regra própria do Simples (art. 40 da Resolução CGSN nº 140/2018) e não deve ser tratado como DARF; conferir a data do mês no Portal do Simples Nacional.
- Conferir sempre na Agenda Tributária do ano, que também traz prorrogações extraordinárias.

### 3. Cálculo (semanal, 8 semanas)
No Windows, gravar o código em arquivo `.py` e rodar com `python -I -X utf8 arquivo.py`. Mostrar o código ao usuário antes de rodar.
```python
# Fluxo semanal: saldo acumulado semana a semana
def fluxo_semanal(saldo_inicial, entradas, saidas, semanas=8):
    saldo = saldo_inicial
    print(f"{'Semana':<8}{'Entradas':>14}{'Saidas':>14}{'Saldo':>14}  Situacao")
    for s in range(1, semanas + 1):
        ent = entradas.get(s, 0)
        sai = saidas.get(s, 0)
        saldo = saldo + ent - sai
        situacao = "OK" if saldo >= 0 else "DEFICIT - avaliar alternativa"
        print(f"S{s:<7}{ent:>14,.2f}{sai:>14,.2f}{saldo:>14,.2f}  {situacao}")

fluxo_semanal(
    saldo_inicial=50_000,
    entradas={1: 30_000, 2: 35_000, 3: 40_000, 4: 25_000, 5: 30_000, 6: 50_000, 7: 30_000, 8: 30_000},
    saidas={1: 25_000, 2: 20_000, 3: 35_000, 4: 60_000, 5: 30_000, 6: 55_000, 7: 80_000, 8: 25_000},
)
```

### 4. Três cenários
- **Otimista:** receita conforme orçamento e prazos de recebimento curtos.
- **Realista:** histórico ajustado, com a inadimplência histórica do próprio cliente.
- **Pessimista:** receita −20% e recebimento 15 dias mais lento.
Os percentuais são ponto de partida; ajustar ao histórico do cliente e registrar a premissa usada.

### 5. Sinalizações para decisão (o cliente decide)
- **Sobra recorrente acima de 1,5 vez as saídas mensais:** sinalizar ao cliente que há excedente; a escolha de onde aplicar é dele, com o banco ou assessor habilitado. Lembrar de manter reserva para os meses fracos.
- **Déficit previsto em menos de 4 semanas:** listar alternativas com o custo de cada uma (antecipação de recebíveis, capital de giro, negociação de prazo com fornecedor, adiamento de investimento). O custo da antecipação vem da proposta da credenciadora ou do banco, não de percentual de mercado.
- **Fornecedor estratégico com prazo curto:** sugerir negociação de prazo.
- **Investimento que estoura o caixa:** comparar compra à vista, financiamento e arrendamento.

### 6. Entregável
**a) Planilha semanal** salva na pasta do cliente:
```
semana,entradas,saidas,saldo,situacao,valor_a_cobrir
S1,30000,25000,55000,OK,
S2,35000,20000,70000,OK,
...
```
**b) Tabela semanal:**
```
                S1   S2   S3   S4   S5   S6   S7   S8
SALDO INICIAL   __   __   __   __   __   __   __   __
ENTRADAS        __   __   __   __   __   __   __   __
SAÍDAS          __   __   __   __   __   __   __   __
SALDO FINAL     __   __   __   __   __   __   __   __
DÉFICIT?        não  não  não  SIM  não  não  SIM  não
VALOR A COBRIR   -    -    -   R$X   -    -   R$Y   -
```
**c) Três cenários comparados.**
**d) Plano de ação** para o cliente decidir, por exemplo:
- Semana 4: déficit de R$ X — alternativas e custo de cada uma.
- Semana 7: negociar prazo com o fornecedor Z.
- Semanas 1 a 3: sobra de R$ Y — avaliar com o cliente.

## Erros comuns / pontos de atenção
- Projetar receita pela data da nota (competência): fluxo de caixa é pela data do dinheiro.
- Esquecer pagamentos não mensais (IPTU, IPVA, seguros, 13º, férias, dissídio).
- Cartões: lançar a venda bruta na semana da venda; o certo é o repasse líquido na semana do repasse.
- Ignorar a inadimplência histórica.
- Pessimismo excessivo que leva a contratar crédito desnecessário.
- Fluxo que nunca é comparado com o extrato real vira só estimativa: confrontar realizado × projetado toda semana.
- FGTS no dia 7: regra antiga. Desde o FGTS Digital, o vencimento é dia 20.

### Casos de borda
- **Reclamatória trabalhista em andamento:** incluir a saída provável no cenário (a avaliação de provisão segue o CPC 25).
- **Cliente em recuperação judicial:** parcelas do plano entram como saída fixa.
- **Vendas ou dívidas em moeda estrangeira:** projetar a taxa de câmbio em cenários.

### Quando escalar
- Impacto de regime tributário no caixa → `analise-tributaria-regime`
- Cliente em crise ou com cobrança judicial → encaminhar a advogado parceiro com OAB (atividade privativa)
- Antecipação de cartões → `conciliacao-cartoes-credenciadora`
- Parcelamento de tributos → `parcelamento-receita-federal`

### Autoavaliação
- [ ] Saldo inicial = bancos + caixa + aplicações de resgate imediato (conferido no extrato)?
- [ ] Recebíveis e pagáveis pela data de vencimento?
- [ ] Tributos e FGTS pelo calendário de 2026?
- [ ] Folha, 13º e encargos?
- [ ] Investimentos previstos?
- [ ] 3 cenários com premissas escritas?
- [ ] Linhas de crédito mapeadas?
- [ ] Atualização semanal combinada com o cliente?

## Formato de entrega
- Cálculos, apurações e conciliações: entregar sempre planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar sempre documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Perguntas que o usuário costuma fazer
- **"Fluxo de caixa é o mesmo que DFC?"** Não. A DFC (CPC 03) é a demonstração oficial do que já aconteceu. O fluxo projetado é ferramenta de gestão do futuro.
- **"Qual o dia do FGTS?"** Dia 20, pelo FGTS Digital (art. 15 da Lei nº 8.036/1990, redação da Lei nº 14.438/2022).
- **"Onde aplico a sobra?"** A skill não indica produto financeiro; aponta o valor e o prazo em que a sobra existe para o cliente decidir com o banco ou assessor.

## Base legal usada nesta skill
- CPC 03 (R2) — Demonstração dos Fluxos de Caixa (método direto como referência de estrutura).
- CPC 25 — provisões e passivos contingentes (reclamatórias).
- Art. 15 da Lei nº 8.036/1990, com a redação da Lei nº 14.438/2022 — FGTS até o dia 20.
- Art. 21, III, da Lei Complementar nº 123/2006 e art. 40 da Resolução CGSN nº 140/2018 — DAS até o dia 20.
- Art. 10 da Lei nº 10.637/2002 e art. 11 da Lei nº 10.833/2003 (redação da Lei nº 11.933/2009) — PIS e COFINS até o dia 25, antecipando para o dia útil anterior.
- Arts. 1º e 2º da Lei nº 4.749/1965 — prazos do 13º salário (até 30/11 e até 20/12).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
