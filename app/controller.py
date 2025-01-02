import app.func as func
from tkinter import messagebox

# #IMPORTA O ARQUIVO PARA O SISTEMA
def controller_start_gen(path,column,df_exists,deorderbool,spinvar):
    file_path_completos = path

    df_nomes_completos = func.carregar_arquivo_excel(file_path_completos)

    #SELECINA A COLUNA COM OS NOMES COMPLETOS
    nomes_completos = func.coluna_para_lista(df_nomes_completos,column)

    #CONVERTE OS NOMES PARA "MAIÚSCULA"
    nomes_completos = [item.upper() for item in nomes_completos]
    if not df_exists.empty:
        df_exists = df_exists.apply(lambda col: col.apply(lambda x: str(x).upper() if isinstance(x, str) else x))

        
    
    #COMEÇA A GERAR OS NOMES
    if not deorderbool:
        novos_nomes = func.gerar_nomes_de_guerra(nomes_completos, df_exists,spinvar)
    else:
        novos_nomes = func.gerar_nomes_de_guerra_desordenado(nomes_completos, df_exists,spinvar)

    # Exemplo de uso
    caminho_arquivo = file_path_completos
    coluna_referencia = column  # Define ao lado de qual coluna os dados serão inseridos

    func.inserir_coluna_excel(caminho_arquivo, coluna_referencia, novos_nomes)