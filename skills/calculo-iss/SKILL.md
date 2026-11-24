---
name: calculo-iss
description: "Apuração mensal de ISS (ISSQN): enquadramento do serviço na lista da LC nº 116/2003, definição do município competente (regra do estabelecimento prestador × exceções do art. 3º), alíquota mínima de 2% e máxima de 5% (LC nº 157/2016), dedução de materiais na construção civil, retenção pelo tomador (art. 6º), ISS de optante do Simples, NFS-e padrão nacional e a transição para o IBS (2029–2033). Acionar quando o usuário disser \"calcular ISS\", \"ISS devido onde\", \"qual município cobra o ISS\", \"item da LC 116\", \"retenção de ISS\", \"ISS retido do Simples\", \"dedução de materiais\", \"obra em outro município\", \"NFS-e nacional\", \"alíquota mínima de 2%\", \"bitributação de ISS\". Entrega: análise de competência, cálculo, guia municipal com vencimento e checklist."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Cálculo e apuração mensal de ISS

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Identifica o item da lista de serviços, decide em qual município o ISS é devido, calcula a base (com as deduções permitidas) e o imposto, verifica se há retenção pelo tomador e orienta a emissão da guia municipal. Trata também o ISS de empresa do Simples e o ISS retido.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

> **Reforma Tributária.** 2026 é ano-teste (CBS 0,9% e IBS 0,1% destacados na nota, sem recolhimento para quem cumpre as obrigações acessórias). O ISS continua integral até 2028; de 2029 a 2032 suas alíquotas caem para 90%, 80%, 70% e 60%, e o ISS é extinto em 2033, substituído pelo IBS (Emenda Constitucional nº 132/2023; Lei Complementar nº 214/2025). Cronograma da NFS-e com IBS/CBS em 2026: skill `reforma-tributaria-transicao`.

## Quando usar
- Prestador de serviço sujeito ao ISS (Lucro Presumido, Lucro Real ou Simples).
- Dúvida sobre qual município cobra, retenção pelo tomador, dedução de materiais, bitributação.
- Conferência da NFS-e e da guia municipal.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade).
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
1. CNPJ do prestador (pode ser de exemplo), competência, valor da NFS-e e descrição do serviço (ou item da LC nº 116/2003).
2. Onde o serviço é executado? Em qual município está o tomador?
3. Construção civil (itens 7.02/7.05): há materiais fornecidos pelo prestador? Subempreitadas?
4. O tomador é obrigado a reter (lei municipal ou art. 6º, § 2º, da LC nº 116/2003)?
5. A empresa é optante do Simples? Qual a faixa e o anexo?

### 2. Lista de serviços — itens que mais geram dúvida
| Item | Serviço | Observação |
|---|---|---|
| 1.04 | Elaboração de programas de computador | Município do prestador |
| 1.05 | Licenciamento ou cessão de uso de software | ISS, não ICMS (STF, ADI 5.659 e ADI 1.945, 2021) |
| 7.02 | Execução de obra de construção civil | Município da obra (art. 3º, III) |
| 7.05 | Reparação, conservação e reforma de edifícios | Município da obra (art. 3º, V) |
| 9.01 | Hospedagem | Prestado no próprio estabelecimento (hotel) |
| 14.05 | Restauração, recondicionamento, beneficiamento de objetos | **Não** é restaurante (fornecimento de alimentação é ICMS) |
| 16.01 / 16.02 | Transporte **municipal** de passageiros / outros transportes municipais | Município da execução (art. 3º, XIX); transporte intermunicipal e interestadual é ICMS |
| 17.05 | Fornecimento de mão de obra, mesmo temporário | Município do estabelecimento do **tomador** (art. 3º, XX) |
| 4.22, 4.23, 5.09, 15.01, 15.09 | Planos de saúde, cartões, leasing | Ver regra do STF abaixo |

### 3. Onde o ISS é devido
**Regra geral**: município do estabelecimento prestador (art. 3º, caput, da LC nº 116/2003).

**Exceções principais (art. 3º, I a XXV)** — o ISS é devido no local da execução ou do tomador, entre outras:
- Importação de serviço: estabelecimento do tomador (inciso I).
- Instalação de andaimes, palcos e estruturas — 3.05 (II); obra de construção civil — 7.02 e 7.19, e também 14.14 pela LC nº 218/2025 (III); demolição — 7.04 (IV); edificações, reparação e reforma — 7.05 (V); coleta e destinação de resíduos — 7.09 (VI); limpeza de vias, logradouros e imóveis — 7.10 (VII); decoração e jardinagem — 7.11 (VIII); controle e tratamento de efluentes — 7.12 (IX); florestamento — 7.16 (XII); escoramento e contenção de encostas — 7.17 (XIII); limpeza e dragagem — 7.18 (XIV).
- Guarda e estacionamento — 11.01 (XV); vigilância e segurança — 11.02 (XVI); armazenamento e depósito — 11.04 (XVII).
- Diversões, lazer e eventos — item 12, exceto 12.13 (XVIII): local do evento.
- Transporte municipal — item 16 (XIX): município onde é executado.
- Fornecimento de mão de obra — 17.05 (XX): estabelecimento do tomador; feiras e congressos — 17.10 (XXI): local do evento; portos, aeroportos e terminais — item 20 (XXII).
- Conferir o inciso exato do art. 3º da LC nº 116/2003, no texto atualizado, antes de concluir.

**Planos de saúde, cartões e leasing (itens 4.22, 4.23, 5.09, 15.01, 15.09)**: a LC nº 157/2016 e a LC nº 175/2020 deslocaram o ISS para o domicílio do tomador, mas o **STF declarou inconstitucional** esse deslocamento (ADI 5.835, ADI 5.862 e ADPF 499, julgamento encerrado em 02/06/2023 — art. 1º da LC nº 157/2016 e, por arrastamento, dispositivos da LC nº 175/2020). Para esses serviços, o ISS volta a ser devido no município do **estabelecimento prestador**.

### 4. Alíquotas e base de cálculo
- Mínima 2% (art. 8º-A da LC nº 116/2003, incluído pela LC nº 157/2016). Isenção, redução de base ou crédito presumido que leve a carga abaixo de 2% é vedado, **exceto** para os itens 7.02, 7.05 e 16.01. A lei municipal que violar o mínimo é nula, e o tomador de outro município pode ser cobrado.
- Máxima 5% (art. 8º, II, da LC nº 116/2003).
- Cada município fixa a alíquota em **lei** municipal (não em decreto).
- **Construção civil (7.02 e 7.05)**: a LC nº 116/2003 permite excluir da base o valor dos **materiais fornecidos pelo prestador** (art. 7º, § 2º, I; STF, RE 603.497, Tema 247). A dedução de **subempreitadas** foi vetada na LC nº 116/2003 e depende da lei municipal.
- Vencimento: definido pela lei de cada município (é comum dia 10 ou 15 do mês seguinte).

### 5. Cálculo (Python, para mostrar a memória)
```python
# ISS: base = serviço - materiais do prestador (7.02/7.05) - outras deduções da lei municipal
def iss(valor_servico, materiais=0, outras_deducoes_lei_municipal=0, aliquota=0.05):
    if not 0.02 <= aliquota <= 0.05:
        raise ValueError('Alíquota fora do intervalo 2% a 5% (LC 116/2003, arts. 8º e 8º-A)')
    base = valor_servico - materiais - outras_deducoes_lei_municipal
    return round(base, 2), round(base * aliquota, 2)

# Obra (item 7.02) executada no MUNICÍPIO EXEMPLO B, alíquota municipal 5%
base, valor = iss(100_000, materiais=30_000, aliquota=0.05)
print(f'Base: R$ {base:,.2f} | ISS: R$ {valor:,.2f}')   # 70.000,00 | 3.500,00
```

### 6. Retenção pelo tomador
- A lei municipal pode atribuir a responsabilidade ao tomador (art. 6º da LC nº 116/2003). O § 2º do art. 6º já torna responsável o tomador, entre outros, dos serviços 3.05, 7.02, 7.04, 7.05, 7.09, 7.10, 7.12, 7.16, 7.17, 7.19, 11.02, 17.05 e 17.10.
- O tomador retém, recolhe por guia do município e entrega o comprovante. O prestador não recolhe de novo o ISS já retido.
- **Prestador do Simples** (art. 21, § 4º, da LC nº 123/2006): a retenção é feita pela alíquota efetiva de ISS a que o prestador estava sujeito no mês anterior, informada na nota (inciso I); no mês de início de atividade, 2% (inciso II); se a alíquota não for informada na nota, 5% (inciso V); se o prestador recolhe ISS em valor fixo mensal no Simples, não há retenção (inciso IV). Diferença entre a alíquota informada e a devida é recolhida pelo prestador em guia do município (incisos III e VI). O prestador declara a receita no PGDAS-D marcando o ISS como retido, para não pagar de novo no DAS. Erro clássico: o tomador reter 5% cheio de uma empresa do Simples.
- Exemplo de percentual efetivo: Anexo III, 4ª faixa, RBT12 de R$ 1.000.000,00 → alíquota efetiva = (1.000.000 × 16% − 35.640) ÷ 1.000.000 = 12,436%; ISS = 32,50% disso = 4,04%. Usar a skill `conferir-apuracao-simples-nacional` para o cálculo exato.

### 7. NFS-e padrão nacional
- O Emissor Nacional de NFS-e é obrigatório para o MEI desde 01/09/2023 (Resolução CGSN nº 169/2022). Para as demais empresas, depende da adesão do município.
- Com a Reforma, a NFS-e passa a levar os campos de IBS/CBS (no cronograma do Ato Conjunto RFB/CGIBS nº 4/2026, a NFS-e de serviços gerais entrou na fase de 01/10/2026; Simples e MEI a partir de 04/01/2027).
- Antes de orientar a emissão, conferir no portal da NFS-e Nacional (gov.br/nfse) se o município do prestador já aderiu ao padrão nacional ou ainda usa emissor próprio.

### 8. Entregável
**a) Análise de competência**
```
NFS-e nº ____  Item LC 116: 7.02  Prestador: EMPRESA EXEMPLO SERVIÇOS LTDA (CNPJ 00.000.000/0001-00)

Município do prestador: MUNICÍPIO EXEMPLO A    Município do tomador: MUNICÍPIO EXEMPLO B
Local da execução: MUNICÍPIO EXEMPLO B (obra)
ISS DEVIDO A: MUNICÍPIO EXEMPLO B (art. 3º, III, da LC nº 116/2003)

Valor do serviço ........................ 100.000,00
(−) Materiais fornecidos pelo prestador .. 30.000,00 (NF de aquisição anexa)
(=) BASE .................................. 70.000,00
Alíquota (lei municipal nº ___/____, art. __): 5%
ISS ....................................... 3.500,00
Retido pelo tomador? [ ] Sim → não recolher de novo   [ ] Não → guia do prestador
Vencimento: __/__/____ (lei municipal)
```
**b) Guia municipal**: portal do município competente → emitir guia → código de receita do ISS → valor → vencimento → citar lei municipal e artigo.
**c) Planilha** de memória (ver "Formato de entrega").
**d) Checklist**
```
[ ] Item da LC nº 116/2003 identificado
[ ] Local de incidência verificado (regra geral × art. 3º; planos de saúde/cartões/leasing pela decisão do STF)
[ ] Alíquota conferida na LEI municipal vigente (entre 2% e 5%)
[ ] Materiais deduzidos com NF; subempreitada só se a lei municipal permitir
[ ] Retenção pelo tomador identificada (e alíquota certa se o prestador for do Simples)
[ ] NFS-e emitida, XML arquivado, campos de IBS/CBS conforme cronograma
```

## Erros comuns / pontos de atenção
- Recolher no município errado (prestador × execução).
- Tratar planos de saúde, cartões e leasing pelo domicílio do tomador (regra derrubada pelo STF em 2023).
- Tratar restaurante como item 14.05 ou transporte intermunicipal como ISS.
- Reter 5% cheio de prestador do Simples.
- Deduzir subempreitada sem previsão na lei municipal.
- Aceitar alíquota ou benefício abaixo de 2% fora dos itens 7.02, 7.05 e 16.01.
- **Bitributação** (dois municípios cobrando): pedir restituição ao município que cobrou indevidamente ou usar a ação de consignação em pagamento (art. 164, III, do CTN). PER/DCOMP é procedimento federal e não serve para ISS.

### Casos de borda
- **Software (licenciamento e SaaS)**: ISS (item 1.05; STF, ADI 5.659 e ADI 1.945). Guardar a jurisprudência em caso de autuação estadual.
- **Prestador em um município, cliente em outro, serviço remoto**: regra geral (estabelecimento prestador), salvo se o item estiver no art. 3º.
- **Matriz e filial**: o ISS segue o estabelecimento que efetivamente presta o serviço.
- **Profissional autônomo e sociedades de profissionais**: ISS fixo conforme lei municipal (Decreto-Lei nº 406/1968, art. 9º, §§ 1º e 3º).
- **Importação de serviço**: ISS devido no município do tomador, que é o responsável (art. 1º, § 1º, e art. 3º, I, da LC nº 116/2003).
- **Cooperativas**: regras próprias do município.

### Quando escalar
- Disputa entre municípios ou autuação → `resposta-fiscalizacao-intimacao`.
- Cliente do Simples (DAS) → `conferir-apuracao-simples-nacional`.
- PIS/COFINS sobre serviços → `calculo-pis-cofins-cumulativo` ou `calculo-pis-cofins-nao-cumulativo`.

## Perguntas que o usuário costuma fazer
- **"Prestei serviço para cliente de outra cidade, pago ISS onde?"** Em regra onde fica o seu estabelecimento. Só muda se o serviço estiver nas exceções do art. 3º (obra, limpeza de imóvel, vigilância, mão de obra etc.).
- **"O município pode cobrar 1%?"** Não, salvo itens 7.02, 7.05 e 16.01. O mínimo é 2%.
- **"O ISS acaba?"** Vai sendo reduzido de 2029 a 2032 e é extinto em 2033, quando o IBS assume.

## Formato de entrega
- Cálculos, apurações e conciliações: planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas a fisco): documento DOCX.
- Este padrão prevalece sobre CSV, MD ou TXT, exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- LC nº 116/2003 — arts. 1º, § 1º (importação), 3º (local de incidência), 6º (responsabilidade do tomador), 7º, § 2º, I (materiais), 8º (alíquota máxima) e 8º-A (alíquota mínima), e lista anexa.
- LC nº 218/2025 — inclusão do subitem 14.14 no art. 3º, III, da LC nº 116/2003.
- LC nº 157/2016 — alíquota mínima de 2% e deslocamento de alguns serviços (art. 1º declarado inconstitucional).
- LC nº 175/2020 — padrão de obrigações acessórias (dispositivos declarados inconstitucionais por arrastamento).
- STF, ADI 5.835, ADI 5.862 e ADPF 499 (2023) — ISS de planos de saúde, cartões e leasing no estabelecimento prestador.
- STF, ADI 5.659 e ADI 1.945 (2021) — ISS sobre software.
- STF, RE 603.497 (Tema 247) — dedução de materiais na construção civil.
- LC nº 123/2006, art. 21, § 4º, I a VI — retenção de ISS de optante do Simples.
- Resolução CGSN nº 169/2022 — NFS-e nacional para o MEI.
- Decreto-Lei nº 406/1968, art. 9º — ISS fixo de profissionais.
- CTN (Lei nº 5.172/1966), art. 164, III — consignação em pagamento.
- EC nº 132/2023 e LC nº 214/2025 — transição ISS → IBS.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
