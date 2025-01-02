from tkinter import filedialog,messagebox
import CTkSpinbox
import customtkinter as ctk
import pandas as pd
import winsound
import app.cor as cor
import app.controller as controller
from app.manual import abrir_manualdeinstrucoes as manual
from app.manual import abrir_link
import update

update.main()

#----------------------------------------
# Imagens
from img import info, pasta

class App(ctk.CTk): 
    def __init__(self):
        super().__init__()
        
        # Configurações da janela
        self.geometry("294x390")  # Define o tamanho da janela
        self.title("Gerar Nomes de Guerra")  # Define o título da janela
        self.resizable(False, False) # Define se a Janela será 
        self.iconbitmap("ico.ico")

        #====================================================
        # Variáveis
        #----------------------------------------------------

        self.archive_columns_list = [""]
        self.dataframe_existsNames = pd.DataFrame()
        self.spin_var = ctk.IntVar()
        self.compare_check_var = ctk.BooleanVar(value=True)  # Define como 'True' para deixar marcado por padrão
        self.random_check_var = ctk.BooleanVar(value=False)  # Define como 'False' para deixar marcado por padrão

        #====================================================
        # Imagens
        #----------------------------------------------------
        self.pasta_image = ctk.CTkImage(pasta.pasta_img, size=(20, 20))
        self.info_image = ctk.CTkImage(info.info_img, size=(20, 20))


        #====================================================
        # Widgets
        #----------------------------------------------------
        
        #Inserir Arquivos com Nomes cadastrados (Existentes)
        # self.update_name_button = ctk.CTkButton(self, text="^", width=30,fg_color="#6D6D6D",hover_color="#3C3F41")
        # self.update_name_button.place(x=215,y=5)

        #Informações e Manual
        self.info_button = ctk.CTkButton(self, image=self.info_image, width=20,height=20,fg_color="#3C3F41",hover_color=cor.cinza,corner_radius=10,border_spacing=0,command=lambda:manual(self))
        self.info_button.place(x=260,y=6)

        #Frame Principal
        self.main_frame = ctk.CTkFrame(self, width=300,height=400,)
        self.main_frame.place(x=0,y=40)
        # self.main_frame.grid_columnconfigure(0, weight=1) # Configurando o layout da janela (opcional)
        #-----------------------------------------------------------------------------------------------------------------------------------
        ctk.CTkLabel(self.main_frame, text="Arquivo com os Nomes").grid(row=0, column=0, padx=5,sticky="w")

        self.name_path = ctk.CTkEntry(self.main_frame, placeholder_text="Caminho do arquivo Excel", width=230,state="readonly")
        self.name_path.grid(row=1, column=0, padx=5, pady=1,sticky="w")

        self.search_path_button = ctk.CTkButton(self.main_frame, image=self.pasta_image, text="", width=40,fg_color=cor.verde,hover_color=cor.verdeclaro, command=lambda:self.search_path())
        self.search_path_button.grid(row=1, column=1, padx=(0,15), pady=1)

        ctk.CTkLabel(self.main_frame, text="Selecionar Coluna").grid(row=2, column=0, padx=5,sticky="w")

        self.select_column_name = ctk.CTkOptionMenu(self.main_frame,width=230,values=self.archive_columns_list, fg_color="gray",text_color="black",button_color=cor.cinzaescuro,button_hover_color=cor.cinza)
        self.select_column_name.grid(row=3, column=0, padx=5, pady=1)

        self.start_gen_button = ctk.CTkButton(self.main_frame, width=200, height=40, text="Iniciar",font=("Arial",18,"bold"),fg_color=cor.verde,hover_color=cor.verdeclaro,command=lambda:self.start_generation())
        self.start_gen_button.grid(row=6, column=0,columnspan=2, pady=10)

        ctk.CTkLabel(self.main_frame, text="Configurações").grid(row=4, column=0,columnspan=2, pady=5)
        licenca = ctk.CTkLabel(self.main_frame, text="© 2024 - Nathan da Cruz Cardoso / Sd Ep Cruz", text_color="gray",cursor="hand2")
        licenca.grid(row=7, column=0,columnspan=2)
        licenca.bind("<Button-1>", abrir_link)
  

        # Frame de Configurações Avançadas
        #-----------------------------------------------------------------------------------------------------------------------------------
        self.config_frame = ctk.CTkFrame(self.main_frame, width=500,height=170)
        self.config_frame.grid(row=5, column=0,columnspan=2)
        # self.config_frame.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self.config_frame, text="Limite de Caracteres").grid(row=0, column=1,pady=(10, 5),padx=(0,10),sticky="w")
        
        self.spinbox = CTkSpinbox.CTkSpinbox(self.config_frame,
                start_value = 15,
                min_value = 6,
                max_value = 30,
                scroll_value = 2,
                width=65,
                height=30,
                font = ('Arial', 11),
                variable = self.spin_var,
                command = None)
        self.spinbox.grid(row=0, column=0,sticky="w",pady=(10, 5),padx=(10,0))

        self.random_check = ctk.CTkCheckBox(self.config_frame, text="Desordernado",fg_color=cor.verde,hover_color=cor.verdeclaro,variable=self.random_check_var,command=self.checkbox_clicked)
        self.random_check.grid(row=1, column=0,pady=(0, 5),padx=(10,0),sticky="w")

        self.compare_check = ctk.CTkCheckBox(self.config_frame, text="Comparar Existentes",fg_color=cor.verde,hover_color=cor.verdeclaro,variable=self.compare_check_var,command=self.checkbox_clicked)
        self.compare_check.grid(row=2, column=0,pady=(0, 5),padx=(10,0),sticky="w")

    #====================================================
    # Funções
    #----------------------------------------------------



    def checkbox_clicked(self):
        # Verificando o estado do checkbox e exibindo no log
        if self.random_check_var.get():
            print("Desorder foi marcado!")
        else:
            print("Desorder foi desmarcado!")

        if self.compare_check_var.get():
            print("Comparer foi marcado!")
        else:
            print("Comparer foi desmarcado!")


    def commit(self):
        path = self.name_path.get()
        df_exists = self.dataframe_existsNames
        column = self.select_column_name.get()
        deorderbool = self.random_check_var.get()
        spinvar = self.spin_var.get()
        resposta = messagebox.askquestion("Atenção!", "Você está prestes a iniciar o processo de geração, gostaria de continuar?")

    
        # Verificando a resposta
        if resposta == 'yes':
            print("Usuário escolheu: Sim")
            try:
                controller.controller_start_gen(path,column,df_exists,deorderbool,spinvar)
                messagebox.showinfo("Aviso","A geração de nomes foi conluída com sucesso.")
                # Aqui você pode colocar o código para iniciar o processo de geração
       
            except PermissionError as e:
                
                # Captura erro de permissão e exibe mensagem apropriada
                messagebox.showerror(f"{e}",f"Erro de Permissão: Não foi possível acessar o arquivo {path}. Verifique se o arquivo está aberto em outro aplicativo ou se você tem permissões adequadas.")

            
            except FileNotFoundError as e:
                # Captura erro de arquivo não encontrado
                 messagebox.showerror(f"{e}",f"Erro: O arquivo {path} não foi encontrado.")

            
            except Exception as e:
                # Captura qualquer outro erro
                 messagebox.showerror(f"{e}",f"Ocorreu um erro desconhecido ao tentar salvar o arquivo {path}.")


        else:
            print("Usuário escolheu: Não")
            # Aqui você pode colocar o código para cancelar ou abortar o processo
                


    def start_generation(self):
        comparebool = self.compare_check_var.get() 

        if comparebool:
            self.abrir_addExistNames()
        else:
            self.commit()

        
        

    def search_path(self):
        # Permite apenas arquivos Excel (com extensões .xlsx e .xls)
        path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx *.xls")])
        if path:
            print(path)
            self.archive_columns_list = self.list_columns(path=path)
            self.update_columns_in_selectbox()  # Atualiza as colunas no selectbox
            
        else:
            print("Nenhum arquivo selecionado.")

    def list_columns(self, path):
        try:
            # Lê o arquivo Excel no caminho fornecido
            df = pd.read_excel(path)
            # Extrai os nomes das colunas para uma lista
            column_list = df.columns.tolist()

            if not column_list:
                messagebox.showerror("Erro", "O arquivo selecionado não possui colunas.")
            else:
                print("Colunas encontradas:", column_list)
                self.name_path.configure(state="normal")
                self.name_path.delete(0, "end")  # Limpa o Entry
                self.name_path.insert(0, path)  # Insere o novo caminho
                self.name_path.configure(state="readonly")
                return column_list  # Retorna a lista de colunas

        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo não encontrado.")
        except ValueError:
            messagebox.showerror("Erro", "O arquivo selecionado não é válido ou não pode ser lido.")
        except Exception as e:
            messagebox.showerror("Erro", f"Um erro ocorreu: {e}")

    def abrir_addExistNames(self):
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        self.janela = ctk.CTkToplevel(self)
        self.janela.title("Adicionar Nomes Existentes")
        self.janela.geometry("290x110")
        self.janela.grab_set()
        self.janela.resizable(False,False)

        ctk.CTkLabel(self.janela, text="Arquivo com os Nomes Existentes").grid(row=0, column=0, padx=5,sticky="w")

        self.existentes_path = ctk.CTkEntry(self.janela, placeholder_text="Caminho do arquivo Excel", width=230,state="readonly")
        self.existentes_path.grid(row=1, column=0, padx=5, pady=1,sticky="w")

        search_existentespath_button = ctk.CTkButton(self.janela, image=self.pasta_image, text="", width=40,fg_color=cor.verde,hover_color=cor.verdeclaro, command=lambda:select_existsPath(self))
        search_existentespath_button.grid(row=1, column=1, padx=(0,15), pady=1)

        confirm_button = ctk.CTkButton(self.janela, text="Ok", width=110,fg_color=cor.cinzaescuro,hover_color=cor.cinza,command=lambda:self.commit(),state="disabled")
        confirm_button.grid(row=5, column=0, padx=(30,0), pady=(15,0),columnspan=2,stick="w")

        cancel_button = ctk.CTkButton(self.janela, text="Cancelar", width=110,fg_color=cor.cinzaescuro,hover_color=cor.cinza,command=lambda:close_window(self))
        cancel_button.grid(row=5, column=0, padx=(0,30), pady=(15,0),columnspan=2,stick="e")

        def close_window(self):
            self.dataframe_existsNames = pd.DataFrame()
            self.janela.destroy()
            ...

        def select_existsPath(self):
            # Permite apenas arquivos Excel (com extensões .xlsx e .xls)
            path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx *.xls")])
            if path:
                print(path)
                try:
                    # Lê o arquivo Excel no caminho fornecido
                    df = pd.read_excel(path)
                    # Extrai os nomes das colunas para uma lista
                    column_list = df.columns.tolist()

                    if not column_list:
                        messagebox.showerror("Erro", "O arquivo selecionado não possui colunas.")
                    else:
                        print("Colunas encontradas:", column_list)
                        self.existentes_path.configure(state="normal")
                        self.existentes_path.delete(0, "end")  # Limpa o Entry
                        self.existentes_path.insert(0, path)  # Insere o novo caminho
                        self.existentes_path.configure(state="readonly")

                        confirm_button.configure(state="normal", fg_color=cor.verde,hover_color=cor.verdeclaro)
                        self.dataframe_existsNames = df
                        pass
                    
                except FileNotFoundError:
                    messagebox.showerror("Erro", "Arquivo não encontrado.")
                except ValueError:
                    messagebox.showerror("Erro", "O arquivo selecionado não é válido ou não pode ser lido.")
                except Exception as e:
                    messagebox.showerror("Erro", f"Um erro ocorreu: {e}")
                
        
 

    def update_columns_in_selectbox(self):
        if self.archive_columns_list:
            self.select_column_name.configure(values=self.archive_columns_list)  # Atualiza o selectbox
            self.select_column_name.set(self.archive_columns_list[0])  # Seta a primeira coluna como valor no selectbox
            self.select_column_name.configure(state="normal")  # Habilita o selectbox
            self.enable_init()


    def enable_init(self):
        if self.archive_columns_list is not None or "":
            self.start_gen_button.configure(state="normal", fg_color=cor.verde,hover_color=cor.verdeclaro)

    
    def disable_init(self):
        self.start_gen_button.configure(state="disabled", fg_color=cor.cinzaescuro,hover_color=cor.cinza)
        self.select_column_name.configure(state="disabled")



# Inicializa o app
if __name__ == "__main__":
    app = App()
    app.disable_init()
    app.mainloop()
