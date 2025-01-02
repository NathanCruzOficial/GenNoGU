import os
import requests
import sys
import shutil
from tkinter import messagebox

# Função para verificar a versão no GitHub
def verificar_versao():
    usuario = "NathanCruzOficial"  # Substitua pelo seu nome de usuário no GitHub
    repositorio = "GenNoGU"  # Substitua pelo nome do seu repositório
    url = f"https://api.github.com/repos/{usuario}/{repositorio}/releases/latest"  # API para pegar o release mais recente
    
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        versao_nova = dados['tag_name']  # A versão estará no 'tag_name' do release
        update_url = dados['assets'][0]['browser_download_url']  # Pega o URL do arquivo executável
        return versao_nova, update_url
    else:
        print("Erro ao verificar a versão no GitHub.")
        return None, None

# Função para realizar o download e substituir o arquivo
def atualizar_programa(update_url):
    arquivo_atual = sys.argv[0]  # O caminho do programa atual
    nome_arquivo_novo = "novo_programa.exe"  # Nome do arquivo a ser salvo

    # Baixar o novo arquivo
    resposta = requests.get(update_url)
    with open(nome_arquivo_novo, 'wb') as f:
        f.write(resposta.content)
    
    # Substituir o arquivo atual pelo novo
    try:
        shutil.move(nome_arquivo_novo, arquivo_atual)
    except Exception as e:
        print(f"Erro ao substituir o arquivo: {e}")
        return False
    return True

# Função para reiniciar o programa
def reiniciar_programa():
    arquivo_atual = sys.argv[0]
    os.startfile(arquivo_atual)  # Reexecuta o programa
    sys.exit()  # Fecha o programa atual

# Função principal
def main():
    versao_atual = "1.0.0"  # Versão atual do programa
    versao_nova, update_url = verificar_versao()
    
    if versao_nova and versao_nova != versao_atual:
        print(f"Nova versão disponível: {versao_nova}")
        resposta = messagebox.askyesno("Atualização Disponível", "Uma nova atualização do sistema foi publicada, gostaria de atualizar agora?")

        if resposta:
            # Lógica para atualizar
             if atualizar_programa(update_url):
                print("Atualização concluída. Reiniciando o programa...")
                reiniciar_programa()

    else:
        print("Você já está usando a versão mais recente.")

if __name__ == "__main__":
    main()
