---
name: diagnosticar-malha-fina-pf
description: "Diagnostica declaração de IRPF JÁ ENTREGUE que caiu na malha fina. Lê o extrato do processamento no e-CAC (Meu Imposto de Renda), identifica a causa da retenção (rendimento omitido, dedução indevida, dependente, ganho de capital, divergência com a fonte pagadora) e monta o plano de ação — retificar, juntar documentos (antecipação da análise) ou responder intimação. Diferença: a skill 'analisar-irpf' atua ANTES da entrega; esta atua DEPOIS, quando há pendência na Receita. Acionar quando o usuário disser \"caiu na malha fina\", \"declaração com pendência\", \"restituição retida\", \"recebi intimação do IR\", \"notificação de lançamento do IRPF\", \"extrato do IR com pendência\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Diagnóstico de malha fina do IRPF

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Ajuda o contador a entender por que a declaração de Imposto de Renda Pessoa Física (IRPF) ficou retida em malha, decidir entre corrigir (retificar) ou comprovar (apresentar documentos) e preparar o que for preciso: cálculo da diferença, DARF e minuta de resposta. Também alerta sobre prazos e sobre o momento em que o contribuinte perde a espontaneidade.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Lei nº 15.270/2025 — atenção ao ano da declaração.** O redutor que zera o imposto até R$ 5.000/mês (R$ 60.000/ano) e reduz parcialmente até R$ 7.350/mês (R$ 88.200/ano) vale a partir do **ano-calendário 2026** (declaração de 2027). A malha quase sempre trata de anos anteriores (2025 para trás), em que o redutor **não** existe. Usar sempre a tabela do ano-calendário em discussão.

## Quando usar
- Extrato do processamento no e-CAC mostra "pendências de malha".
- Restituição não liberada nos lotes normais.
- Contribuinte recebeu Termo de Intimação Fiscal ou Notificação de Lançamento.
- Verificação preventiva logo após a entrega.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Despesa médica e dado de saúde de dependente são dados sensíveis (art. 5º, II, da LGPD).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- O acesso ao e-CAC do cliente é feito pelo contador com procuração eletrônica válida. A skill não pede nem guarda senha ou código gov.br do cliente.

## Passo a passo (instruções para o agente de IA)

### 1. Ler o extrato
No e-CAC: Meu Imposto de Renda > Extrato do processamento > Pendências. A Receita descreve a pendência por **assunto** (por exemplo "omissão de rendimentos", "dedução de despesa médica", "dependente"). **Não há uma tabela pública de "códigos numéricos de pendência"**; não inventar códigos. Registrar o texto exato da pendência.

Tipos mais frequentes e causas comuns:
```
OMISSÃO DE RENDIMENTOS
- Dois empregos, RPA esquecido, aluguel pago por PJ, pensão, JCP
- Fonte pagadora informou na EFD-Reinf (série R-4000) ou no eSocial e o contribuinte não declarou
  (para anos até 2024, a informação vinha da DIRF; a DIRF foi extinta para fatos a partir de 2025)

DEDUÇÃO INDEVIDA OU NÃO COMPROVADA
- Despesa médica: recibo sem nome, endereço e CPF/CNPJ de quem recebeu
  (art. 73 do Decreto nº 9.580/2018 — RIR/2018); paciente diferente do titular sem identificação
- Médico/clínica informou valor diferente na DMED
- Plano de saúde com dependente que não consta na declaração
- Educação acima do limite: R$ 3.561,50 por ano, por pessoa
  (art. 8º, II, "b", da Lei nº 9.250/1995)
- Pensão alimentícia sem decisão judicial, acordo homologado ou escritura pública
- PGBL acima de 12% da renda tributável, ou sem contribuição ao regime oficial de previdência
  (art. 11 da Lei nº 9.532/1997)

DEPENDENTE
- Mesmo dependente em duas declarações
- Filho acima de 21 anos, ou acima de 24 sem cursar ensino superior ou técnico de 2º grau
  (exceto se incapacitado física ou mentalmente para o trabalho)
- Pais, avós ou bisavós com rendimentos (tributáveis ou não) acima do limite do ano:
  no ano-calendário 2025 (declaração de 2026), R$ 28.467,20. Para outro ano, usar o limite
  do Perguntas e Respostas do IRPF do exercício correspondente

GANHO DE CAPITAL E RENDA VARIÁVEL
- Venda de imóvel sem apurar ganho de capital (GCAP)
- Ações fora da bolsa com lucro; day trade não declarado
- Criptoativos: alienações no Brasil acima de R$ 35 mil no mês sem apuração; ativos no exterior
  seguem a Lei nº 14.754/2023 desde 2024 (15% anual, sem a isenção de R$ 35 mil)
```

### 2. Entrevista mínima
```
P1: Ano-calendário da declaração e texto exato da pendência no extrato?
P2: Já houve Termo de Intimação ou Notificação de Lançamento? Data da ciência?
P3: Há documentos que comprovam o que foi declarado (informe de rendimentos, recibo, escritura)?
P4: O contribuinte reconhece o erro?
P5: A procuração eletrônica do e-CAC para o contador está ativa?
```

### 3. Decidir: retificar ou comprovar
**Retificar** (quando o erro existe):
- Refazer a declaração com o mesmo modelo, ou trocar de modelo só dentro do prazo de entrega (depois do prazo não se troca de completa para simplificada nem o contrário).
- Pagar a diferença com juros Selic e multa de mora (0,33% por dia, limitada a 20% — art. 61 da Lei nº 9.430/1996).
- **Só tem efeito de autorregularização ANTES do início do procedimento fiscal.** Depois da ciência de Termo de Intimação ou início de fiscalização, o contribuinte perde a espontaneidade (art. 138 do CTN (Lei nº 5.172/1966) e art. 7º do Decreto nº 70.235/1972): aí a resposta é atender à intimação, não retificar para "apagar" o problema.

**Comprovar** (quando o declarado está certo):
- Sem intimação: solicitar a antecipação da análise e juntar documentos pelo e-CAC (dossiê digital de atendimento).
- Com intimação: responder no prazo indicado no próprio termo, juntando os documentos.
- Prazo de análise da Receita: variável.

**Se vier Notificação de Lançamento** (imposto lançado de ofício):
- Multa de ofício de 75% (art. 44, I, da Lei nº 9.430/1996), aumentada em metade (112,5%) se o contribuinte não atender à intimação (art. 44, § 2º).
- Pagamento em até 30 dias da ciência reduz a multa de ofício em 50% (art. 6º da Lei nº 8.218/1991).
- Impugnação em 30 dias da ciência (art. 15 do Decreto nº 70.235/1972) — encaminhar à skill de resposta a fiscalização.

### 4. Cálculo da diferença (Python)
O imposto adicional **não** é a tabela aplicada só sobre o valor omitido: refaz-se a declaração inteira e compara-se com a original. Salvar como `.py` e rodar com `python -I -X utf8 arquivo.py`.

```python
# Tabela progressiva ANUAL por ano-calendário: (limite superior, alíquota, parcela a deduzir)
# AC 2025: tabela anual oficial da Receita Federal (página "Tributação de 2025" do
#          Meu Imposto de Renda, exercício 2026).
TABELAS = {
    2025: [(28_467.20, 0.0, 0.0), (33_919.80, 0.075, 2_135.04), (45_012.60, 0.15, 4_679.03),
           (55_976.16, 0.225, 8_054.97), (float("inf"), 0.275, 10_853.78)],
    # Outros anos: preencher com a tabela oficial do ano-calendário em discussão.
}

def imposto_anual(base, ano):
    for limite, aliq, deduz in TABELAS[ano]:
        if base <= limite:
            return max(0.0, base * aliq - deduz)

def diferenca(base_original, base_corrigida, ano):
    return imposto_anual(base_corrigida, ano) - imposto_anual(base_original, ano)

def darf_espontaneo(principal, dias_atraso, selic_acumulada):
    multa = min(principal * 0.0033 * dias_atraso, principal * 0.20)  # art. 61 Lei 9.430/96
    juros = principal * selic_acumulada                                # Selic acumulada + 1% no mês do pagamento
    return principal + multa + juros

# Exemplo fictício: base declarada 60.000; omitido RPA de 30.000 (base corrigida 90.000)
d = diferenca(60_000, 90_000, 2025)
print("IR adicional:", round(d, 2))
print("DARF 0211 estimado:", round(darf_espontaneo(d, 200, 0.10), 2))
# Lembrar: imposto já retido na fonte sobre o valor omitido entra como imposto pago.
```

### 5. Entregável
**a) Extrato decifrado**
```
Pendência: omissão de rendimentos (texto do extrato: "____")
Ano-calendário: ____     Fonte pagadora: EMPRESA EXEMPLO — CNPJ 00.000.000/0001-00
Valor informado pela fonte: R$ ____   Valor declarado: R$ ____
Situação: sem intimação / intimado em __/__/__ (prazo até __/__/__)
Decisão: RETIFICAR (contribuinte reconhece o RPA não declarado)
```
**b) Cálculo da retificadora** (memória acima).
**c) DARF código 0211** (IRPF — quota/saldo) com principal, multa, Selic e vencimento. Se houver Notificação de Lançamento, usar o DARF que acompanha a notificação.
**d) Minuta de resposta (se for comprovar)**
```
À Receita Federal do Brasil
Contribuinte: CONTRIBUINTE EXEMPLO — CPF 000.000.000-00
Ano-calendário: ____   Termo de Intimação nº ____ (se houver)

Em atendimento à intimação / para antecipação da análise, apresentamos:

PENDÊNCIA: dedução de despesas médicas de R$ ____.
DOCUMENTOS: recibos e notas fiscais com nome, endereço e CPF/CNPJ do prestador,
valor, data e identificação do paciente, nos termos do art. 73 do Decreto nº 9.580/2018 (RIR/2018):
  1. Recibo — profissional ____ (CPF/CNPJ ____) — data ____ — R$ ____
  2. Nota fiscal — clínica ____ (CNPJ ____) — data ____ — R$ ____
  3. Comprovantes de pagamento (transferência/cartão), quando houver.

Requer-se o acolhimento dos documentos e o processamento normal da declaração.

Local, data.
Contador ____ CRC ____ — procurador (procuração eletrônica no e-CAC)
```
**e) Checklist**
```
[ ] Extrato consultado no e-CAC e texto da pendência registrado
[ ] Verificado se já houve intimação (data da ciência e prazo)
[ ] Documentos de suporte coletados
[ ] Decisão: retificar / comprovar / impugnar
[ ] Retificadora transmitida e DARF pago (se for o caso)
[ ] Documentos juntados ou intimação respondida
[ ] Procuração eletrônica ativa
[ ] Cliente ciente por escrito
```

## Erros comuns / pontos de atenção
- Retificar antes de entender a pendência — corrige o que não estava errado.
- Retificar depois de intimado achando que encerra o caso: sem espontaneidade, cabe responder à intimação.
- Apresentar recibo sem CPF/CNPJ de quem recebeu — a Receita glosa.
- Perder o prazo da intimação: multa sobe para 112,5% (art. 44, § 2º, da Lei nº 9.430/1996).
- Pagar DARF sem retificar a declaração: o débito continua divergente.
- Aplicar o redutor da Lei nº 15.270/2025 em ano-calendário anterior a 2026.
- Esquecer o IR já retido na fonte sobre o rendimento omitido.

**Casos de borda**
- **Pendência em mais de um ano**: o mesmo erro costuma se repetir; revisar os demais anos ainda não decaídos (5 anos — art. 173 do CTN, ou art. 150, § 4º, quando houve pagamento).
- **Contribuinte sem imposto a pagar** também pode cair em malha (por exemplo, restituição indevida).
- **Contribuinte falecido**: declarações de espólio são entregues com o **CPF do falecido** pelo inventariante.
- **Contribuinte que saiu do país**: Comunicação e Declaração de Saída Definitiva do País, regidas pela IN SRF nº 208/2002 (em vigor, com alterações; a comunicação está no art. 11-A). Conferir o texto consolidado no portal de normas da Receita para o ano da saída.

## Perguntas que o usuário costuma fazer
- **"Retificar tira da malha na hora?"** Não. A retificadora é reprocessada; se resolver a divergência, a declaração sai da malha.
- **"Quanto tempo tenho para responder a intimação?"** O prazo é o que está no termo. Contar da ciência (data em que abriu a mensagem no e-CAC ou do decurso do prazo de leitura).
- **"Vou pagar multa de 75%?"** Só se houver lançamento de ofício. Na retificação espontânea, a multa é a de mora (até 20%).

## Formato de entrega
- Cálculos, apurações e conciliações: sempre planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): sempre documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- Decreto nº 9.580/2018 (RIR/2018) — art. 73 (requisitos da dedução de despesas médicas) e demais regras do IRPF.
- Lei nº 9.250/1995 — art. 8º (deduções: saúde, educação com limite anual, dependentes) e art. 35 (dependentes).
- Lei nº 9.430/1996 — art. 44 (multa de ofício de 75%, agravada em 50% sem atendimento à intimação) e art. 61 (multa de mora de 0,33% ao dia, limite de 20%).
- Lei nº 8.218/1991 — art. 6º (redução de 50% da multa de ofício no pagamento em 30 dias).
- Lei nº 5.172/1966 (CTN) — art. 138 (denúncia espontânea), art. 150, § 4º, e art. 173 (decadência).
- Decreto nº 70.235/1972 — art. 7º (início do procedimento fiscal) e art. 15 (impugnação em 30 dias).
- IN RFB nº 1.500/2014 — normas gerais do IRPF e documentos de comprovação.
- IN RFB nº 2.312/2026 — Declaração de Ajuste Anual do exercício 2026 (ano-calendário 2025). Para outro exercício, usar a IN anual correspondente, publicada pela Receita antes do período de entrega.
- IN SRF nº 208/2002 — saída definitiva do país e tributação do não residente.
- Lei nº 9.532/1997 — art. 11 (limite de 12% para o PGBL).
- Lei nº 14.754/2023 — aplicações e ativos no exterior.
- Lei nº 15.270/2025 — redutor do IR e IRPFM (a partir do ano-calendário 2026).
- Lei nº 11.441/2007 — pensão alimentícia por escritura pública.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
