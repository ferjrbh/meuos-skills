---
name: esocial-admissao
description: "Especialista em admissão no eSocial — S-2200 (admissão completa) ou S-2190 (registro preliminar, só em urgência), cadastros prévios (S-1000, S-1005, S-1010, S-1020), categoria correta da Tabela 01 (101 geral, 103 aprendiz, 104 doméstico, 106 temporário, 111 intermitente), CPF válido, ASO admissional antes do início e dependentes para IRRF. Use quando o usuário (a) vai contratar empregado CLT, aprendiz, intermitente, temporário ou doméstico, (b) menciona S-2190, S-2200, ASO, categoria eSocial, registro de empregado, CTPS Digital. Entrega: checklist de documentos + sequência de eventos com prazos + recibos + alerta de risco se faltar requisito."
version: 1.0
author: Fernando Lúcio · Aion Group
homepage: https://www.meuos.com.br
instagram: https://instagram.com/fernandolucio.ia
---

# eSocial — Admissão (S-2190 / S-2200)

> Criada por **Márcia Almeida**, contadora, para a trilha Contábil do MeuOS.

## O que esta skill faz
Organiza a admissão do empregado no eSocial: confere os cadastros prévios do empregador, os documentos e o ASO, escolhe a categoria certa e monta a sequência de eventos com prazo. Entrega o checklist para o cliente e o alerta quando algo impede o início do trabalho.

> **Limite.** Apoio técnico ao contador. Não substitui a conferência do profissional
> responsável (CRC) nem a leitura da norma vigente. Valores e prazos mudam: conferir a data
> de atualização no fim do arquivo.

## Quando usar
- Admissão de empregado CLT, aprendiz, intermitente, temporário ou doméstico.
- Dúvida entre S-2190 (registro preliminar) e S-2200 (admissão completa).
- Para o cálculo da primeira folha, use `folha-pagamento-mensal`.

## Regras de segurança (valem durante toda a skill)
- Antes de abrir arquivos de cliente, confirmar de qual cliente e contexto são (nunca cruzar clientes).
- Dados pessoais (CPF, salário, saúde, dependentes) são tratados como sensíveis: usar só o necessário e não repetir na resposta (art. 6º, III, da Lei nº 13.709/2018 (LGPD) — necessidade). O ASO é dado de saúde (dado sensível, art. 5º, II, da Lei nº 13.709/2018 (LGPD)): registrar só "apto/inapto" e a data.
- Não transmitir, enviar nem pagar nada: a skill prepara, e o contador confere e transmite.
- Não executar scripts baixados sem que o usuário veja o que fazem.

## Passo a passo (instruções para o agente de IA)

### 1. Eventos envolvidos (leiaute S-1.3)
```
CADASTROS PRÉVIOS (uma vez por empregador; atualizar quando mudar)
S-1000  Informações do empregador
S-1005  Estabelecimentos / obras (CNPJ, CAEPF, CNO)
S-1010  Tabela de rubricas
S-1020  Lotações tributárias
S-1070  Processos administrativos/judiciais (se houver)
Não há tabela de cargos nem de funções no leiaute S-1.3: cargo e CBO são informados
no próprio S-2200.

ADMISSÃO
S-2190  Registro preliminar do trabalhador — opcional, com dados mínimos (CPF, nascimento,
        data de admissão, categoria). Prazo: até o final do dia anterior ao início das
        atividades.
S-2200  Cadastramento inicial do vínculo e admissão — todos os dados (inclusive dependentes).
        Prazo: até o dia anterior ao início das atividades (D-1).
        Se foi enviado o S-2190, ou se é admissão por transferência: o S-2200 pode ir até
        o dia 15 do mês seguinte ao da admissão, e sempre antes de qualquer outro evento
        não periódico desse trabalhador.
        Trabalhador temporário (Lei nº 6.019/1974): até 5 dias úteis após o início.
S-2205  Alteração de dados cadastrais do trabalhador
S-2206  Alteração contratual
S-2220  Monitoramento da saúde (ASO) — até o dia 15 do mês seguinte ao do exame
S-2240  Condições ambientais do trabalho (quando aplicável)
```

### 2. Categorias principais (Tabela 01 do eSocial)
```
101  Empregado — geral (inclui o empregado público contratado pela CLT)
102  Empregado — trabalhador rural por pequeno prazo (Lei nº 11.718/2008)
103  Empregado — aprendiz
104  Empregado — doméstico (eSocial Doméstico)
105  Empregado — contrato a termo da Lei nº 9.601/1998
106  Trabalhador temporário (Lei nº 6.019/1974)
111  Empregado — contrato de trabalho intermitente
901  Estagiário (não é empregado: vai em S-2300, não em S-2200)
```
Mensalista e horista NÃO são categorias: a diferença vai no campo de unidade do salário do S-2200.

### 3. Entrevista mínima
```
Q1: Empresa (CNPJ) + data prevista de início + o trabalhador já tem CPF regular?
Q2: Cargo/CBO + salário + jornada (44h, 40h, 12x36...) + tipo de contrato (indeterminado,
    experiência, intermitente, aprendiz, temporário)?
Q3: Documentos recebidos (lista abaixo)?
Q4: ASO admissional já feito e "apto"? PCMSO vigente?
Q5: Dependentes para IRRF e salário-família (com CPF)? Opta pelo vale-transporte?
Q6: Cadastros prévios do eSocial em dia (S-1000, S-1005, S-1010, S-1020)?
Q7: Piso e regras da CCT/ACT da categoria conferidos?
```

### 4. Validações críticas (antes de transmitir)
- CPF regular na Receita Federal. O CPF é o identificador do trabalhador: desde a versão 1.0 do leiaute (simplificado), o campo NIS foi retirado e o eSocial valida os dados só pelo CPF, na base da Receita Federal.
- ASO admissional "apto" ANTES de o trabalhador começar (art. 168 da CLT e NR-7).
- CBO compatível com a função real.
- Categoria correta (tabela acima) e lotação tributária certa.
- Dependentes com CPF.

### 5. Sequência
**Admissão planejada (regra):**
1. Validar tudo do item 4.
2. Transmitir o S-2200 até o dia anterior ao início (D-1).
3. Assinar contrato; o S-2200 alimenta a CTPS Digital.

**Urgência (dados incompletos e início amanhã):**
1. Validar CPF e garantir ASO apto.
2. Transmitir o S-2190 até o final do dia anterior ao início.
3. Completar com o S-2200 até o dia 15 do mês seguinte, antes de qualquer outro evento não periódico (afastamento, desligamento etc.).

### 6. Entregável
**a) Checklist de documentos**
```
TRABALHADOR (matrícula/iniciais): ______   Início: __/__/____

DOCUMENTOS
[ ] Documento de identidade e CPF
[ ] CTPS Digital (consultada no app/gov.br)
[ ] Comprovante de endereço
[ ] Comprovante de escolaridade
[ ] Título de eleitor e certificado de reservista (praxe; a falta não impede a admissão)
[ ] CNH (se motorista) e curso MOPP (se transporta carga perigosa)
[ ] Certidão de nascimento e CPF dos dependentes (IRRF e salário-família)
[ ] Para salário-família: atestado de vacinação obrigatória (anual, filhos até 6 anos) e
    comprovante de frequência escolar (semestral, a partir de 4 anos) — art. 67 da
    Lei nº 8.213/1991 e art. 84 do Decreto nº 3.048/1999
[ ] Termo de opção ou recusa do vale-transporte
[ ] Dados bancários
[ ] Termo de ciência de tratamento de dados (Lei nº 13.709/2018 — LGPD)

ASO E eSOCIAL
[ ] ASO admissional em __/__/____ — apto
[ ] S-2190 enviado em __/__/____ recibo: ____ (só se urgência)
[ ] S-2200 enviado em __/__/____ recibo: ____
[ ] S-2220 (ASO) até o dia 15 do mês seguinte ao exame
[ ] Contrato assinado
```

**b) Sequência de eventos com prazos:** `S-2200 até D-1` (ou `S-2190 até D-1 → S-2200 até dia 15 do mês seguinte`) `→ S-2220 até dia 15 do mês seguinte ao exame → S-2240 se aplicável`.

**c) Recibos do eSocial arquivados.**

**d) Alerta de risco**, quando faltar requisito: "PARE: manter empregado sem registro sujeita a empresa à multa de R$ 3.000,00 por empregado não registrado, acrescida de igual valor em cada reincidência (R$ 800,00 por empregado para ME e EPP), conforme art. 47 da CLT. Não inicie sem ASO apto e sem S-2200 (ou S-2190) transmitido."

## Erros comuns / pontos de atenção
- Começar a trabalhar antes do ASO ou antes do envio do S-2200/S-2190.
- Código de categoria errado: intermitente é 111, aprendiz é 103, temporário é 106 (conferir na Tabela 01).
- Confundir o prazo do S-2200 (D-1) com o do S-2220 (dia 15 do mês seguinte ao exame).
- CBO incompatível com a função real.
- Dependente sem CPF.
- Esquecer que o S-2190 precisa ser completado pelo S-2200.

## Casos especiais
- **Estagiário (Lei nº 11.788/2008):** não é empregado; categoria 901 no S-2300 (trabalhador sem vínculo de emprego). Exige termo de compromisso e seguro contra acidentes pessoais (art. 9º, IV, da Lei nº 11.788/2008).
- **Aprendiz (art. 428 da CLT; Lei nº 10.097/2000; Decreto nº 9.579/2018):** categoria 103; FGTS de 2% (art. 15, § 7º, da Lei nº 8.036/1990); informar a entidade formadora.
- **Intermitente (art. 452-A da CLT):** categoria 111. Não existe evento próprio de convocação no leiaute S-1.3: os dias trabalhados em cada mês são informados no S-1200 da competência. No desligamento, usar o S-2299 com o motivo correspondente da Tabela 19.
- **Temporário (Lei nº 6.019/1974):** categoria 106; S-2200 até 5 dias úteis após o início das atividades.
- **Doméstico (LC nº 150/2015):** categoria 104, pelo módulo eSocial Doméstico (gov.br).
- **Transferência entre empresas do mesmo grupo, sem rescisão:** S-2299 com motivo 11 na empresa de origem e S-2200 como admissão por transferência na de destino — ambos até o dia 15 do mês seguinte. Não é nova admissão com rescisão.

## Quando escalar
- Folha do novo empregado → `folha-pagamento-mensal`
- Eventos periódicos S-1200/S-1210 → `esocial-eventos-periodicos`
- Desligamento → `esocial-rescisao`
- Afastamento → `esocial-afastamentos`

## Perguntas que o usuário costuma fazer
- **"Posso mandar o S-2200 no mesmo dia em que ele começa?"** A regra é até o dia anterior. Em urgência, use o S-2190 até o dia anterior e complete com o S-2200 até o dia 15 do mês seguinte.
- **"Preciso do PIS para admitir?"** Não para o eSocial: o identificador é o CPF, e o campo NIS não existe mais no leiaute.

## Base legal usada nesta skill
- CLT (Decreto-Lei nº 5.452/1943) — art. 29 (anotação na CTPS em 5 dias úteis), art. 41 (registro), art. 47 (multa por empregado não registrado), art. 168 (exame admissional), art. 428 (aprendiz), art. 452-A (intermitente).
- Decreto nº 8.373/2014 — institui o eSocial.
- Portaria MTP nº 671/2021 — CTPS Digital e registro eletrônico.
- Manual de Orientação do eSocial (MOS) versão S-1.3 e leiautes S-1.3 com as notas técnicas vigentes (em nov/2026: NT S-1.3 nº 07/2026, rev. 20/10/2026), publicados em gov.br/esocial — prazos dos eventos S-2190, S-2200 e S-2220; Tabela 01.
- NR-7 — PCMSO e ASO.
- Lei nº 8.036/1990 — art. 15, § 7º (FGTS do aprendiz).
- Lei nº 8.213/1991 — art. 67 e Decreto nº 3.048/1999 — art. 84 (documentos do salário-família).
- Lei nº 6.019/1974 — trabalho temporário.
- Lei nº 11.788/2008 — estágio.
- LC nº 150/2015 — empregado doméstico.

## Formato de entrega
- Cálculos, apurações e conciliações: entregar SEMPRE planilha XLSX com aba de memória de cálculo e aba de resumo executivo.
- Diagnósticos, pareceres, relatórios, holerites e correspondências (inclusive respostas a fisco): entregar SEMPRE documento DOCX.
- Este padrão prevalece sobre qualquer formato citado acima neste documento (CSV, MD, TXT), exceto arquivos técnicos de importação de sistemas (ex.: TXT de importação do seu sistema contábil).

---
> Skill criada por Marcia — contadora. Versão 1.0 · validada em 15/11/2026. Parâmetros válidos para 2026.

---

> Skill oficial do **MeuOS** · [www.meuos.com.br](https://www.meuos.com.br) · Fernando Lúcio · Aion Group · [@fernandolucio.ia](https://instagram.com/fernandolucio.ia)
