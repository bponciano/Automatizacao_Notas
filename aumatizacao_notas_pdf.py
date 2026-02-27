## Extração de dados de notas ##

#Pacotes
import pdfplumber
import pandas as pd
import os
import re
import shutil

# Caminhos 
entrada = "/workspaces/automatizacao_nota/dados_brutos"
processados = "/workspaces/automatizacao_nota/dados_processados"
planilha = "/workspaces/automatizacao_nota/notas.xlsx"

# Scanner
def extrair_dados_da_nota(caminho_do_pdf):
    with pdfplumber.open(caminho_do_pdf) as pdf:
        primeira_pagina = pdf.pages[0]
        texto_completo = primeira_pagina.extract_text()
        
        cnpj_forn = re.search(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}", texto_completo)
        cnpj = cnpj_forn.group(0) if cnpj_forn else "Não identificado"
        
        data_busca = re.search(r"\d{2}/\d{2}/\d{4}", texto_completo)
        data = data_busca.group(0) if data_busca else "00/00/0000"

        nota_busca = re.search(r"(?:N[o|º|°|.\s]+)\s?(\d+[\.\d+]*)", texto_completo, re.IGNORECASE)
        num_nota = nota_busca.group(1) if nota_busca else "000"

        fornecedor = "Não identificado"
        linhas_topo = texto_completo.split('\n')[:10]
        for l in linhas_topo:
            if len(l) > 10 and not any(x in l.upper() for x in ["DANFE", "RECEBEMOS", "NOTA FISCAL", "IDENTIFICAÇÃO"]):
                fornecedor = l.strip()
                break

        tabela = primeira_pagina.extract_table()
        itens_da_nota = []

        if tabela:
            for linha in tabela:
                l = [str(c).replace('\n', ' ').strip() if c else "" for c in linha]
                
                if len(l) >= 7:
                    produto = l[1]
                    qtd = l[6] if len(l) > 6 else ""
                    valor_total = l[-1]

                    if not produto or len(produto) < 5: continue
                    if any(x in produto.upper() for x in ["DESCRIÇÃO", "VALOR", "CÓDIGO", "TOTAL", "ICMS", "BASE", "SUB"]):
                        continue

                    if not re.search(r"\d", valor_total): continue

                    itens_da_nota.append({
                        "CNPJ": cnpj,
                        "Fornecedor": fornecedor,
                        "Produtos faturados": produto,
                        "Quantidade": qtd,
                        "Valor": valor_total,
                        "Data": data,
                        "Nº Nota": num_nota
                    })

        return itens_da_nota
    
#Loop e Movimentação
arquivos = os.listdir(entrada)

lista_consolidada = []

#Loop
for arquivo in arquivos:
    if arquivo.lower().endswith(".pdf"):
        caminho_full_entrada = os.path.join(entrada,arquivo)
        print(f'Lendo os dados da nota: {arquivo}')
        
        dados_da_nota = extrair_dados_da_nota(caminho_full_entrada)

        lista_consolidada.extend(dados_da_nota)
        
        #Movimentação
        caminho_full_destino = os.path.join(processados, arquivo)
        shutil.move(caminho_full_entrada, caminho_full_destino)
        print(f"Arquivo {arquivo} movido para a pasta de processados.")

print("Fase de Leitura e Movimentação Concluída.")

#Atualização de planilha
if lista_consolidada:
    df_novos = pd.DataFrame(lista_consolidada)

    if os.path.exists(planilha):
        df_antigo = pd.read_excel(planilha)
        df_final = pd.concat([df_antigo, df_novos], ignore_index=True)
        print(f"Adicionando novos itens à planilha existente...")
    
    else:
        df_final = df_novos
        print("Criando a nova planilha de controle")
    
    df_final.to_excel(planilha, index=False)
    print(f"Sucesso! Planilha atualizada com {len(lista_consolidada)} novos itens")
else:
    print("Nenhum arquivo pdf foi encontrado para processar.")