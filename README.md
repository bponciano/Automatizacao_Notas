# 📊 Automatizador de Notas Fiscais (NF-e)

> Pipeline de ingestão e normalização de dados fiscais em XML com persistência relacional e consolidação analítica em Excel.

Este projeto simula um fluxo real de engenharia de dados, realizando parsing de XML estruturado, modelagem relacional em SQLite e geração incremental de dataset para análise.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## 🎯 Objetivo do Projeto

Automatizar o processamento de Notas Fiscais Eletrônicas (NF-e) para:

- Eliminar digitação manual
- Garantir integridade relacional
- Evitar duplicidade de registros
- Criar base estruturada para análise de dados
- Simular pipeline de dados de ponta a ponta

Projeto desenvolvido como prática aplicada de **Engenharia de Dados com foco em ingestão, modelagem e consolidação analítica.**

## 🏗 Arquitetura da Solução

```
XML (dados_brutos)
↓
Parsing (ElementTree)
↓
Transformação e Classificação
↓
Persistência Relacional (SQLite)
↓
Consolidação incremental (Pandas)
↓
Exportação estruturada (Excel)
↓
Movimentação para dados_processados
```

## ⚙️ Stack Tecnológica

- Python 3.x
- xml.etree.ElementTree (Parsing XML)
- SQLite3 (Banco relacional embarcado)
- Pandas (Estruturação e consolidação)
- Openpyxl (Manipulação e formatação Excel)
- OS / Shutil (Automação de arquivos)

## 🔄 Pipeline de Dados

### 1️⃣ Ingestão

- Leitura automática de arquivos `.xml` na pasta `dados_brutos`
- Identificação de estrutura válida NF-e
- Uso de namespace oficial da NF-e

---

### 2️⃣ Extração

Campos extraídos:

- CNPJ
- Razão Social
- Endereço completo
- Número da nota
- Data de emissão
- Valor total da nota
- CFOP
- Itens (produto, quantidade, valor unitário e total)

---

### 3️⃣ Transformação

- Conversão de tipos (float, date)
- Classificação automática por CFOP:

| Prefixo CFOP | Tipo |
|--------------|------|
| 11, 21, 51, 61 | VENDA |
| 19, 29, 59, 69 | REMESSA |
| Outros | OUTROS |

---

### 4️⃣ Persistência Relacional

Modelagem normalizada com 5 entidades:

- Enderecos
- Fornecedores
- Notas
- Produtos
- Compras (tabela fato)

Boas práticas aplicadas:

- `INSERT OR IGNORE` para evitar duplicidade
- Controle transacional com `commit()` e `rollback()`
- Relacionamentos via chave estrangeira
- Separação entre dimensões e fato

---

### 5️⃣ Consolidação Analítica

- Criação incremental de DataFrame
- Atualização automática da planilha
- Manutenção de tabela formatada
- Atualização dinâmica do range da tabela Excel

Output:
Formato estruturado e pronto para BI.

---

### 6️⃣ Automação do Fluxo

Após processamento:

- XML movido para `dados_processados`
- Evita reprocessamento
- Mantém histórico organizado

## 🧠 Conceitos Aplicados

- Parsing de XML estruturado
- Normalização relacional
- Integridade de dados
- Controle transacional
- Data wrangling
- Automação de processos
- Pipeline incremental
- Integração SQL + Excel

## 📊 Aplicações Analíticas

- Análise de compras por fornecedor
- Volume por período
- Classificação por tipo de operação
- Base para dashboards (Power BI / Tableau)
- Auditoria fiscal interna

## 🚀 Evoluções Futuras

- Parametrização de caminhos via variável de ambiente
- Logging estruturado
- Containerização com Docker
- Migração para PostgreSQL
- API para ingestão automatizada
- Dashboard integrado ao banco SQLite
- Agendamento automático (cron / scheduler)

## 👨‍💻 Autor

**Breno Ponciano**  
Foco em Engenharia e Análise de Dados