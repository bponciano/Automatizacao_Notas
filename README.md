# 🚀 Automatizador de Notas Fiscais Eletrônicas (NF-e)

Pipeline automatizada para ingestão, normalização relacional e consolidação de dados fiscais (XML NF-e) utilizando **Python + SQLite + Excel**.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

---
### 📌 Visão Geral

Este projeto automatiza o processo de:

- Leitura e parsing de arquivos XML de NF-e
- Extração estruturada de dados fiscais
- Persistência em banco relacional (SQLite)
- Consolidação incremental em planilha Excel formatada
- Organização automática dos arquivos processados

O objetivo é eliminar digitação manual, reduzir erros operacionais e estruturar os dados para análise e BI.

---

### 🏗 Arquitetura da Solução

#### Fluxo de Processamento
```
dados_brutos (XML)
↓
Parsing (ElementTree)
↓
Normalização Relacional (SQLite)
↓
Consolidação (Pandas)
↓
Exportação formatada (Excel)
↓
Movimentação para dados_processados
```
---
#### 📂 Estrutura do Projeto
```
automatizacao_nota/
├── dados_brutos/             # Entrada dos XMLs
├── dados_processados/        # XMLs já processados
├── automatizacao_notas.py    # Script principal
├── Metalica_DataBase.db      # Banco SQLite
├── notas.xlsx                # Planilha consolidada
└── README.md
```

---

### 🛠 Stack Tecnológica

- Python 3.x
- xml.etree.ElementTree → Parsing XML
- sqlite3 → Banco relacional embarcado
- pandas → Estruturação de dados
- openpyxl → Manipulação e formatação Excel
- os / shutil → Automação de arquivos

---

### 🧠 Modelagem de Dados

O banco SQLite segue normalização relacional básica.

### Tabelas

#### Enderecos
- ID_Endereco (PK)
- Rua
- Numero
- Bairro
- Cidade
- Estado

#### Fornecedores
- ID_Fornecedor (PK)
- CNPJ (Unique)
- Razao_Social
- ID_Endereco (FK)

#### Notas
- ID_Nota (PK)
- Num_Nota
- Data
- Valor
- ID_Fornecedor (FK)
- Tipo_Nota

#### Produtos
- ID_Produto (PK)
- Nome (Unique)

#### Compras (Tabela Fato)
- ID_Nota (FK)
- ID_Fornecedor (FK)
- ID_Produto (FK)
- Data
- Quantidade
- Valor_Unitario
- Valor_Total

---

### ⚙️ Funcionamento Técnico


#### 1️⃣ Parsing XML

Utiliza namespace oficial da NF-e:

```python
ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
```
Dados extraídos:

- CNPJ

- Razão Social

- Endereço completo

- Número da nota

- Data de emissão

- Valor total

- CFOP

- Itens (produto, quantidade, valor unitário e total)

---
#### 2️⃣ Classificação Automática por CFOP

A tipificação da nota é baseada no prefixo do CFOP:

| Prefixo        | Tipo    |
| -------------- | ------- |
| 11, 21, 51, 61 | VENDA   |
| 19, 29, 59, 69 | REMESSA |
| Outros         | OUTROS  |

---
#### 3️⃣ Persistência Relacional

Uso de INSERT OR IGNORE para evitar duplicidade

Controle transacional com:

- commit() em sucesso

- rollback() em erro

Garante integridade e idempotência parcial.

---
#### 4️⃣ Consolidação Incremental no Excel

Cenários tratados:

✔ Se a planilha não existir:

- Criação automática

- Inserção de tabela estruturada

- Aplicação de estilo formatado

✔ Se já existir:

- Append de novos registros

- Atualização dinâmica da referência da tabela

- Preservação da formatação

---
#### 5️⃣ Automação de Arquivos

Após processamento bem-sucedido:
```python
shutil.move(caminho_completo, processados)
```
Evita reprocessamento e mantém organização.

---
### 🔐 Tratamento de Erros

- Try/Except por arquivo

- Rollback em falhas

- Continuidade do processamento

- Log informativo no terminal

----
### ▶️ Como Executar
1. Clone o repositório
```
git clone <url-do-repositorio>
```
2. Instale as dependências
```
pip install pandas openpyxl
```
3. Execute o script
```
python automatizacao_notas.py
```
Coloque os XMLs na pasta dados_brutos/.

---
### 📊 Aplicações

- Controle de compras

- Análise de fornecedores

- Base para Power BI

- Auditoria fiscal interna

- Estruturação de dados para BI

----
### 🚀 Possíveis Evoluções

- Interface gráfica (Streamlit)

- API para ingestão automática

- Logs estruturados

- Containerização com Docker

- Integração direta com Power BI

----
### 👨‍💻 Autor

Breno Ponciano