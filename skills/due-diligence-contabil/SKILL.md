---
name: due-diligence-contabil
description: "Conduz due diligence (auditoria de compra) contábil, fiscal, trabalhista e societária antes de compra, venda, fusão ou aporte de investidor. Identifica passivos ocultos e contingências (CPC 25), ajusta o EBITDA (Quality of Earnings) e entrega relatório de achados classificados por gravidade, com sugestões de cláusulas de declarações e garantias e de conta-garantia (escrow). Acionar quando o usuário disser \"due diligence\", \"DD\", \"auditoria de compra\", \"vamos comprar uma empresa\", \"investidor quer olhar os números\", \"data room\", \"passivo oculto\", \"quality of earnings\", \"EBITDA ajustado\", \"sucessão de empresa\"."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# Due diligence contábil, fiscal e trabalhista

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Organiza o trabalho de due diligence (DD) em uma empresa-alvo: define escopo, data de corte e materialidade, monta a lista de documentos, cruza escriturações e quantifica riscos. Entrega os achados classificados (alta, média, baixa), o EBITDA ajustado e sugestões para o contrato (cláusulas de declarações e garantias, ajuste de preço e escrow), para revisão do contador líder e do advogado da operação.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.
> A redação das cláusulas contratuais é atividade do advogado da operação; a skill só sugere o conteúdo econômico.

## Quando usar
- Compra, venda, fusão, incorporação ou aporte (fundo de venture capital ou private equity).
- Entrada de sócio, sucessão familiar, franquia.
- Depois de assinado o acordo de confidencialidade (NDA) e aberto o data room.
- Trabalho típico de 4 a 12 semanas, com data de corte e materialidade definidas.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). Na folha da empresa-alvo, trabalhar com dados agregados ou pseudonimizados sempre que possível.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.
- Sem NDA assinado, não abrir documentos da empresa-alvo. Guardar o material só nas pastas do projeto, nunca em pasta temporária do sistema.

## Passo a passo (instruções para o agente de IA)

### 1. Entrevista mínima
```
P1: O cliente é comprador, vendedor ou assessor? O NDA está assinado?
P2: Empresa-alvo: regime tributário, faturamento, número de empregados, estados onde opera?
P3: Data de corte (cut-off) e materialidade (% do EBITDA ou valor absoluto)?
P4: Acesso ao data room garantido? Por qual ferramenta?
P5: Foco: fiscal, trabalhista, contábil, societário/regulatório ou todos?
P6: Estrutura da operação: compra de quotas/ações ou compra de ativos (estabelecimento)?
    Muda a responsabilidade por sucessão (ver item 3).
```

### 2. Escopo — 4 dimensões
```
1. CONTÁBIL
   Balanços e DREs de 5 anos (auditados, se houver)
   Plano de contas e qualidade da escrituração (ECD)
   Provisões: férias, 13º, FGTS, contingências, perdas de crédito (PCLD), impairment
   Imobilizado: existência, depreciação, impairment
   Estoques: inventário físico × contábil, obsolescência
   Receita: política do CPC 47 e corte de período
   Partes relacionadas; empréstimos com taxa fora de mercado

2. FISCAL
   Regime tributário e comparativo (skill analise-tributaria-regime)
   Apurações dos períodos não decaídos — IRPJ, CSLL, PIS, COFINS, ICMS, ISS
   SPEDs entregues × pagamentos (skill revisao-fiscal-cruzamento-sped)
   PER/DCOMP em aberto ou não homologadas
   Parcelamentos e transações federais, estaduais e municipais
   Autos de infração e defesas
   ST / DIFAL nos estados de operação
   LC nº 224/2025: se Presumido acima de R$ 5 mi, conferir se a majoração foi aplicada
   ou se há liminar (risco de reversão)
   Reforma Tributária: saldos credores de ICMS/PIS/COFINS e preparo para CBS/IBS
   Créditos a recuperar (skill recuperacao-creditos-pis-cofins) — tratar como ativo contingente

3. TRABALHISTA / PREVIDENCIÁRIA
   Folha dos períodos não prescritos
   Reclamações trabalhistas (em curso e encerradas) — provisão pelo CPC 25
   Admissões e desligamentos por amostragem
   Conformidade: eSocial, EFD-Reinf, DCTFWeb, FGTS Digital (desde 03/2024);
   para períodos anteriores, GFIP/SEFIP
   Plano de saúde, PLR (Lei nº 10.101/2000), benefícios, convenções e acordos coletivos
   Estabilidades (gestante, CIPA, acidentado)
   Risco de pejotização (PJ que na prática é empregado)

4. SOCIETÁRIA / REGULATÓRIA
   Contrato social e alterações; atas; quadro societário (controle direto e indireto)
   Acordo de sócios
   Licenças (sanitária, ambiental, Anvisa, Anatel) e alvarás
   Marcas e patentes
   LGPD: encarregado (art. 41 da Lei nº 13.709/2018), política, registro de incidentes
```

### 3. Prazos que limitam o risco (usar na quantificação)
```
Tributos federais (decadência)        5 anos — art. 173, I, do CTN (Lei nº 5.172/1966), ou art. 150, § 4º,
                                      quando houve pagamento antecipado; dolo/fraude: art. 173
Contribuições previdenciárias         5 anos — Súmula Vinculante nº 8 do STF
Cobrança (prescrição)                 5 anos da constituição — art. 174 do CTN
Trabalhista                           5 anos, até 2 anos após o fim do contrato — art. 7º, XXIX, da
                                      Constituição Federal e art. 11 da CLT
FGTS                                  5 anos — STF, ARE 709.212 (Tema 608), com modulação
Responsabilidade do adquirente        arts. 132 e 133 do CTN (sucessão tributária na compra de
                                      fundo de comércio/estabelecimento e em incorporação/fusão)
Sucessão trabalhista                  arts. 10, 448 e 448-A da CLT
```

### 4. Cronograma típico (8 semanas)
```
Sem 1     Kick-off, lista de documentos, acesso ao data room
Sem 2-3   Levantamento e análise dos 5 anos; cruzamento de SPEDs
Sem 4-5   Validação de provisões, inventário físico, entrevistas
Sem 6     Relatório preliminar (alertas vermelhos)
Sem 7     Ajustes ao EBITDA
Sem 8     Relatório final e apresentação
```

### 5. Classificação dos achados
```
Gravidade   Critério                                   Exemplo
Alta        > 5% do EBITDA, risco regulatório ou       Auto de infração de R$ 2 mi; pejotização sistêmica
            passivo iminente
Média       1% a 5% do EBITDA; contingência possível   PCLD subdimensionada em R$ 200 mil
Baixa       < 1% do EBITDA; regularizável              Divergência de DCTFWeb de R$ 5 mil
```
Contingências pelo CPC 25: **provável** = provisionar; **possível** = divulgar e quantificar; **remota** = não registrar. Na DD, quantificar também as possíveis, porque entram na negociação.

### 6. EBITDA ajustado (Quality of Earnings)
```
EBITDA reportado
+ despesas não recorrentes (multas pagas, indenizações isoladas, custos da operação)
− receitas não recorrentes (venda de ativo, ganho cambial não operacional)
± pró-labore ajustado a valor de mercado (sócio que se paga pouco ou muito)
+ despesas pessoais dos sócios lançadas na empresa
± operações com partes relacionadas ajustadas a preço de mercado
± provisões a regularizar
= EBITDA AJUSTADO
```

### 7. Entregáveis
**a) Lista de documentos**
```
A. CONTÁBIL: balanços e DREs de 5 anos (ECD); plano de contas; razão das contas principais;
   inventário físico × contábil; políticas contábeis; demonstrações auditadas (se houver)
B. FISCAL: ECD, ECF, EFD ICMS/IPI, EFD-Contribuições dos últimos 5 anos; DCTFWeb (com MIT a partir
   de 01/2025) e DCTF (até 12/2024); DARFs, GPS, GNRE; PER/DCOMP; autos e defesas; parcelamentos;
   certidões (federal, estadual, municipal, FGTS)
C. TRABALHISTA: eSocial e EFD-Reinf; folha analítica; reclamações (sentenças, acordos);
   convenções coletivas; fiscalizações do Ministério do Trabalho e Emprego (MTE)
D. SOCIETÁRIO: contrato social e alterações; atas; licenças e alvarás; consultas CADIN e
   birôs de crédito; LGPD (política, encarregado, incidentes)
E. CONTRATOS: 20 maiores clientes e fornecedores; empréstimos e financiamentos; locações;
   marcas e patentes; licenças de software
```
**b) Achado por linha** (planilha na pasta do projeto)
```
ID: F-002
Categoria: Fiscal          Gravidade: Alta
Tema: ICMS-ST recolhido a menor
Período: 2022-2024
Valor estimado: R$ ____ (principal + multa conforme a lei estadual + Selic/juros estaduais)
Causa: MVA original aplicada no lugar da MVA ajustada em operação interestadual
Recomendação: provisionar; ajuste de preço; definir quem adere ao parcelamento
Documentos: NFs amostradas, EFD ICMS/IPI, parecer
```
**c) EBITDA ajustado** com memória item a item.
**d) Sugestões para o contrato**: declarações e garantias, ajuste de preço, indenização e escrow dimensionado pelos achados de gravidade alta e média (redação final pelo advogado).
**e) Relatório final** assinado pelo contador líder e apresentação executiva.

## Erros comuns / pontos de atenção
- Escopo aberto demais ("tudo que houver") ou sem data de corte.
- Achados de baixa gravidade no corpo principal do relatório: diluem os críticos (mandar para anexo).
- Não quantificar: "existe risco" não ajuda quem negocia.
- Esquecer a LGPD em SaaS e e-commerce.
- Subestimar a pejotização.
- Ignorar a sucessão tributária e trabalhista na compra de estabelecimento (arts. 132 e 133 do CTN; arts. 10 e 448 da CLT).
- Tratar crédito tributário a recuperar como certo: é ativo contingente até a homologação.
- Não levar os achados para as cláusulas do contrato.

**Casos de borda**
- **Empresa familiar com mistura sócio/empresa**: ajustes grandes no EBITDA.
- **Empresa em recuperação judicial**: passivo do plano e viabilidade depois da RJ (Lei nº 11.101/2005).
- **Transações com partes relacionadas no exterior**: regras de preços de transferência da Lei nº 14.596/2023.
- **DD do lado vendedor (sell-side)**: antecipar os riscos antes do comprador e organizar o data room.

## Perguntas que o usuário costuma fazer
- **"Quantos anos olhar?"** Os períodos não decaídos e não prescritos (em regra, 5 anos), mais o histórico de autos e processos ainda abertos.
- **"Comprar quotas ou ativos muda o risco?"** Sim. Na compra de quotas, os passivos ficam na empresa comprada. Na compra de ativos, ainda pode haver sucessão (art. 133 do CTN; arts. 10 e 448 da CLT).
- **"Crédito de PIS/COFINS a recuperar aumenta o preço?"** Pode entrar como ganho contingente, com cláusula de repasse condicionada à homologação.

## Formato de entrega
- Cálculos, apurações e conciliações: sempre planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios e correspondências (inclusive respostas ao fisco): sempre documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

## Base legal usada nesta skill
- CPC 25 (NBC TG 25) — provisões, passivos e ativos contingentes; CPC 26 — apresentação; CPC 47 — receita.
- Lei nº 5.172/1966 (CTN) — arts. 132 e 133 (sucessão), art. 150, § 4º, e art. 173 (decadência), art. 174 (prescrição).
- Súmula Vinculante nº 8 do STF — prazo de 5 anos para contribuições previdenciárias.
- Constituição Federal, art. 7º, XXIX, e art. 11 da CLT — prescrição trabalhista.
- CLT (Decreto-Lei nº 5.452/1943) — arts. 10, 448 e 448-A (sucessão trabalhista).
- STF, ARE 709.212 (Tema 608) — prescrição do FGTS.
- IN RFB nº 2.005/2021 (DCTFWeb até 12/2024) e IN RFB nº 2.237/2024 (DCTFWeb com MIT a partir de 01/2025).
- Lei nº 10.101/2000 — PLR.
- Lei nº 14.596/2023 — preços de transferência.
- Lei nº 11.101/2005 — recuperação judicial.
- Lei nº 13.709/2018 (LGPD) — art. 41 (encarregado) e art. 48 (comunicação de incidente).
- Lei Complementar nº 224/2025 e IN RFB nº 2.305/2025 — majoração do Presumido acima de R$ 5 mi.

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
