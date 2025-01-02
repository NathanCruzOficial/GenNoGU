# Lista de 10 nomes completos para exemplo
import pandas as pd
import random
# import curses

# Função para gerar nomes de guerra exclusivos
def gerar_nomes_de_guerra(lista_nomes_novos, lista_nomes_existentes,spinvar):
    nomes_de_guerra = []
    preposicoes = {"da", "de", "do", "das", "dos"}
    
    for nome in lista_nomes_novos:
        partes_nome = nome.split()
        nome_de_guerra = None
        
        # 1ª Fase: Nome único (ignora preposições)
        for i in range(len(partes_nome) - 1, -1, -1):
            if partes_nome[i].lower() not in preposicoes:
                nome_de_guerra = partes_nome[i]
                if nome_de_guerra not in nomes_de_guerra and nome_de_guerra not in lista_nomes_existentes.values:
                    break  # Nome único disponível, sai da fase 1
                else:
                    nome_de_guerra = None  # Nome já existe, tenta próxima fase

        # 2ª Fase: Combinação com preposições
        if not nome_de_guerra:
            for i in range(len(partes_nome) - 1):
                if partes_nome[i].lower() in preposicoes:
                    nome_de_guerra = f"{partes_nome[i]} {partes_nome[i + 1]}"
                    if nome_de_guerra not in nomes_de_guerra and nome_de_guerra not in lista_nomes_existentes.values:
                        break  # Combinação com preposição disponível
                    else:
                        nome_de_guerra = None  # Combinação já existe, tenta próxima fase

        # 3ª Fase: Combinar dois nomes (no máximo) próximos, ignorando preposições
        if not nome_de_guerra:
            for i in range(len(partes_nome) - 1):
                if partes_nome[i].lower() not in preposicoes:
                    for j in range(i + 1, len(partes_nome)):
                        if partes_nome[j].lower() not in preposicoes:
                            nome_de_guerra = f"{partes_nome[i]} {partes_nome[j]}"
                            if len(nome_de_guerra) > spinvar:
                                # Abrevia se o nome combinado for maior que 15 caracteres
                                nome_de_guerra = f"{partes_nome[i][0]}. {partes_nome[j]}"
                            if nome_de_guerra not in nomes_de_guerra and nome_de_guerra not in lista_nomes_existentes.values:
                                break  # Combinação curta disponível
                            else:
                                nome_de_guerra = None  # Combinação já existe, tenta próxima
                if nome_de_guerra:
                    break  # Nome válido encontrado

        # Se todas as fases falharem
        if not nome_de_guerra:
            nome_de_guerra = "NAO FOI POSSIVEL CRIAR NOME"


        # Adiciona o nome de guerra encontrado
        nomes_de_guerra.append(nome_de_guerra)
    return nomes_de_guerra

def gerar_nomes_de_guerra_desordenado(lista_nomes_novos, lista_nomes_existentes, spinvar):
    nomes_de_guerra = []
    preposicoes = {"da", "de", "do", "das", "dos"}
    
    for nome in lista_nomes_novos:
        partes_nome = nome.split()
        nome_de_guerra = None

        # 1ª Fase: Nome único (ignorando preposições e seleção aleatória)
        random.shuffle(partes_nome)  # Embaralha os nomes
        for parte in partes_nome:
            if parte.lower() not in preposicoes:
                nome_de_guerra = parte
                if nome_de_guerra not in nomes_de_guerra and nome_de_guerra not in lista_nomes_existentes.values:
                    break  # Nome único disponível
                else:
                    nome_de_guerra = None  # Nome já existe, tenta próximo

        # 2ª Fase: Combinação com preposições (preposição à esquerda, nome aleatório à direita)
        if not nome_de_guerra:
            for parte in partes_nome:
                if parte.lower() in preposicoes:
                    preposicao = parte
                    # Embaralha as partes do nome e tenta combinar a preposição com outro nome aleatório
                    random.shuffle(partes_nome)
                    for nome in partes_nome:
                        if nome.lower() not in preposicoes and nome != preposicao:
                            nome_de_guerra = f"{preposicao} {nome}"
                            if nome_de_guerra not in nomes_de_guerra and nome_de_guerra not in lista_nomes_existentes.values:
                                break  # Combinação com preposição válida
                            else:
                                nome_de_guerra = None  # Combinação já existe, tenta próximo
                    if nome_de_guerra:
                        break

        # 3ª Fase: Combinação de 2 nomes aleatórios (ignora preposições)
        if not nome_de_guerra:
            nomes_validos = [parte for parte in partes_nome if parte.lower() not in preposicoes]
            random.shuffle(nomes_validos)
            for i in range(len(nomes_validos) - 1):
                for j in range(i + 1, len(nomes_validos)):
                    nome_de_guerra = f"{nomes_validos[i]} {nomes_validos[j]}"
                    if len(nome_de_guerra) > spinvar:
                        # Abrevia o nome se for maior que spinvar (por exemplo, "CARDOSO NATHAN" vira "C. NATHAN")
                        nome_de_guerra = f"{nomes_validos[i][0]}. {nomes_validos[j]}"
                    if nome_de_guerra not in nomes_de_guerra and nome_de_guerra not in lista_nomes_existentes.values:
                        break  # Combinação válida
                    else:
                        nome_de_guerra = None  # Combinação já existe, tenta próxima
                if nome_de_guerra:
                    break  # Nome válido encontrado

        # Se todas as fases falharem
        if not nome_de_guerra:
            nome_de_guerra = "NAO FOI POSSIVEL CRIAR NOME"

        # Adiciona o nome de guerra encontrado
        nomes_de_guerra.append(nome_de_guerra)
    
    return nomes_de_guerra
    

# Função para carregar o arquivo Excel e listar as colunas
def carregar_arquivo_excel(file_path):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None

# Função para validar a coluna selecionada
def validar_coluna(df, coluna):
    if coluna not in df.columns:
        print("Erro: Coluna selecionada não existe no arquivo.")
        return False

    if df[coluna].isnull().any():
        print(f"A coluna '{coluna}' contém valores nulos.")
    else:
        print(f"A coluna '{coluna}' não contém valores nulos.")

    return True

def coluna_para_lista(df, coluna):
    if coluna in df.columns:
        return df[coluna].dropna().tolist()  # Remove valores nulos e converte para lista
    else:
        print("Erro: A coluna não existe no DataFrame.")
        return []
    
def inserir_coluna_excel(caminho_arquivo, coluna_referencia, dados):
    # Carrega a primeira planilha do arquivo
    df = pd.read_excel(caminho_arquivo, sheet_name=0)

    # Localiza a posição da coluna de referência e insere uma nova coluna à direita
    pos_coluna = df.columns.get_loc(coluna_referencia) + 1
    nova_coluna_nome = f"Nova_Coluna_{pos_coluna}"

    # Garante que o nome da coluna seja único
    contador = 1
    while nova_coluna_nome in df.columns:
        nova_coluna_nome = f"Gerador_Nomes_{pos_coluna}_{contador}"
        contador += 1

    # Insere a nova coluna no DataFrame
    df.insert(pos_coluna, nova_coluna_nome, dados)

     # Tenta abrir o arquivo Excel e salvar as mudanças
    with pd.ExcelWriter(caminho_arquivo, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        # Converte writer.sheets.keys() para uma lista e acessa a primeira planilha
        primeira_planilha = list(writer.sheets.keys())[0]
        df.to_excel(writer, sheet_name=primeira_planilha, index=False)
