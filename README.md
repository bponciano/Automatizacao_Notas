## Automatizador de Notas Fiscais (NF-e) - Metálica

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

Este projeto automatiza o fluxo de extração e armazenamento de dados de Notas Fiscais Eletrônicas (XML). Ele realiza o parsing dos arquivos, organiza as informações em um banco de dados relacional (SQLite) e consolida os dados em uma planilha Excel formatada para análise gerencial, dentro disso decidi usar o SQLite para um estudo, montei um banco de dados para estudo a ser preenchido divindo as informações nas seguintes tabelas:

```python
├── enderecos                 # Armazena locais únicos de fornecedores.
├── fornecedores              # Vincula o CNPJ à razão social e endereço.
├── notas                     # Dados de cabeçalho (Número, Data, Valor Total, Tipo).
├── produtos                  # Cadastro único de itens de estoque/consumo.
└── compras                   # Tabela contendo os itens de cada nota (Quantidade, Valor Unitário, etc).
```

## Objetivo

O objetivo desse projeto é diminuir o trabalho braçal e o tempo gasto do corpo de funcionários do recebimento que passam horas digitando em uma planilha nota por nota do que foi recebido, o fluxo completo é:

## Fluxo de Trabalho/Estrutura dos Arquivos

```python
├── dados_brutos                    # Pasta de entrada dos xml's
├── dados_processados               # Pasta de armazenamentos dos xml's
├── automatização_notas.py          # Código que fará o trabalho de leitura
├── notas.xlsx                      # Planilha a ser preenchida
├── Metalica_DataBase.db            # Base de dados do SQLite
└── README.md                       # Documentação
```
## Funcionalidades

Extração Inteligente: Realiza a leitura de arquivos XML (NF-e) usando a biblioteca xml.etree.ElementTree.

Classificação Automática: Identifica o tipo de operação (VENDA, REMESSA ou OUTROS) baseando-se no CFOP do primeiro item da nota.

Banco de Dados Relacional: Armazena dados de Fornecedores, Endereços, Notas e Itens em um banco SQLite, garantindo integridade e evitando duplicidade (INSERT OR IGNORE).

Integração com Excel: Exporta os dados processados para uma planilha .xlsx com tabelas formatadas automaticamente via openpyxl.

Gestão de Arquivos: Move automaticamente os arquivos processados da pasta de entrada para uma pasta de histórico, mantendo o ambiente organizado.

## Tecnologias Utilizadas

Python 3.x

Pandas: Manipulação de dados e exportação para Excel.

SQLite3: Armazenamento persistente de dados.

ElementTree: Parsing de estruturas XML complexas.

Openpyxl: Formatação avançada de planilhas e tabelas.

Shutil/OS: Automação de sistema de arquivos.

## Como Utilizar

1. Configuração: Clone o repositório e ajuste os caminhos das pastas no script (variáveis entrada, processados, data_base, planilha).

2. Input: Coloque os arquivos .xml das notas fiscais na pasta dados_brutos.

3. Execução: Rode o script principal:

```python
python automatizador_notas.py
```

4. Resultado: Os dados serão inseridos no Metalica_DataBase.db.

   - A planilha notas.xlsx será criada ou atualizada com os novos itens.

   - Os XMLs originais serão movidos para dados_processados.

## Próximos Passos (Roadmap)

- Criar um Dashboard no Power BI conectado ao banco SQLite.
- Adicionar suporte para leitura de NFSe (Notas de Serviço).

---
Desenvolvido por: 

Breno Ponciano
---