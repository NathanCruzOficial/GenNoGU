import customtkinter as ctk
import winsound
import app.cor as cor
from app.instrucoes import v
import webbrowser

def abrir_manualdeinstrucoes(self):
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        self.manual = ctk.CTkToplevel(self)
        self.manual.title("info")
        self.manual.geometry("350x450")
        self.manual.resizable(False,False)

        ctk.CTkLabel(self.manual, text="Manual de Instruções:").pack()

        text_box = ctk.CTkScrollableFrame(self.manual,width=310,height=360)
        text_box.pack()

        text_inbox = ctk.CTkLabel(
        text_box,
        text=v,
        justify="left",
        font=("calibri",13),
        wraplength=300,)
        text_inbox.pack()
        
        ajuda = ctk.CTkLabel(
        text_box,
        text="Ainda Precisa de Ajuda? - Clique Aqui!",
        justify="left",
        font=("calibri",15),
        wraplength=300,
        text_color="lightblue")
        ajuda.pack()
        ajuda.bind("<Button-1>", abrir_link)

        close_button = ctk.CTkButton(self.manual, text="Entendido", width=340,fg_color=cor.cinzaescuro,hover_color=cor.cinza,command=lambda:self.manual.destroy())
        close_button.pack(pady=10)

def abrir_link(self):
        # URL que será aberta
        webbrowser.open("https://linktr.ee/nathan_cruz")