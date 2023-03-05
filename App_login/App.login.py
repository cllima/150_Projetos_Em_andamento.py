import customtkinter as ctk
from tkinter import *
import database


## Coloca tudo dentro da class App.
class App(ctk.CTk, database.BackEnd):
    def __init__(self):
        super().__init__()
        self.configuracoes_da_janela_inicial()
        self.tema()
        self.tela_login()
        self.cria_tabela()
        self.show_password_login()

    #Configurando a janela principal
    def configuracoes_da_janela_inicial(self):
        self.title('Sistema de Login by Clayton Lima')
        self.geometry('700x400+600+60')
        self.maxsize(width=720, height=420)
        self.minsize(width=680, height=380)
        self.resizable(False, False) ## False=Evita de minimizar

    # Tema da cor da Janela Principal
    def tema(self):
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')


    # Trabalhando com imagens tela a esquerda e Tela de login
    def tela_login(self):
        self.img = PhotoImage(file='rafiki.png')
        self.label_img = ctk.CTkLabel(self, text=None, image=self.img)
        self.label_img.grid(row=1, column=0, padx=30, pady=30)

        ## Título da nossa Plataforma
        self.title = ctk.CTkLabel(self, text='Faça o seu Login ou Cadastre-se\n na nossa plataforma para acessar\n os nossos serviços!',
                                          font=('Roboto', 16,'bold'),text_color='#00B0F0') # ou Letra=> Century Gothic bold
        self.title.grid(row=0, column=0, pady=10)

        # Criando Frame do formulário de Login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=10)

        #Criando widgets dentro do frame  = Formulário de Login
        self.label_title = ctk.CTkLabel(self.frame_login, text='Faça seu Login', font=('Roboto', 18, 'bold'),
                                       text_color= ('white'))
        self.label_title.grid(row=0, column=0, padx=10, pady=20)

        ## Caixa de texto 1 => Nome Usuário
        self.username_login_entry = ctk.CTkEntry(self.frame_login,placeholder_text='Nome do usuário', width=300,font=('Roboto',12),
                                                 corner_radius=10,border_color='#1866a5')
        self.username_login_entry.grid(row=1, column=0, padx=10, pady=10)

        ## Caixa de texto 2 => Senha usuário
        self.password_login_entry = ctk.CTkEntry(self.frame_login,placeholder_text='Senha de usuário', width=300,font=('Roboto', 12),
                                                 corner_radius=10, border_color='#1866a5', show='*')
        self.password_login_entry.grid(row=2, column=0, padx=10, pady=10)

        ## Botão de Chekbox
        self.ver_password = ctk.CTkCheckBox(self.frame_login, text='Clique para ver a Senha', font=('Roboto', 12),
                                            corner_radius=10, command=self.show_password_login)
        self.ver_password.grid(row=3, column=0, pady=10)

        # Botão de Login
        self.btn_login = ctk.CTkButton(self.frame_login, text='Login'.upper(), width=300, font=('Roboto', 12, 'bold'), corner_radius=10,
                                       command=self.verifica_login)
        self.btn_login.grid(row=4, column=0, padx=10, pady=15)

        #Caso não tenha o cadastro
        self.span = ctk.CTkLabel(self.frame_login, text='Se não tem conta, click no botão abaixo para se\n Cadastrar em nosso Sistema!',
                                font=('Roboto', 10))
        self.span.grid(row=5, column=0, padx=10, pady=10)

        #Botão de Cadastro
        self.btn_cadastro = ctk.CTkButton(self.frame_login, text='Faça seu Cadastro'.upper(), width=300, fg_color='green', hover_color='#050',
                                       font=('Roboto', 12, 'bold'), corner_radius=10, command=self.tela_cadastro)
        self.btn_cadastro.grid(row=6, column=0, padx=10, pady=15)

    #Função para deixar a senha visível e no Botão de Chekbox chama => command=self.show_password_login
    def show_password_login(self):
        if self.password_login_entry.cget("show") == "*":
            self.password_login_entry.configure(show="")
        else:
            self.password_login_entry.configure(show="*")

        # Função para Limpar dados do Login
    def limpa_login(self):
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

############ Botão de Cadastrar novo Usuário ######################
    def tela_cadastro(self):
        #Primeiro remove o formulário de login
        self.frame_login.place_forget() ## Faz desaparecer a tela de login

        # Criando Frame do formulário de Cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=10)

        ## Título da Tela de Cadastro
        self.label_title = ctk.CTkLabel(self.frame_cadastro, text='Faça seu Cadastro', font=('Roboto', 18, 'bold'),text_color=('white'))
        self.label_title.grid(row=0, column=0, padx=10, pady=5)

        # Criando a Tela de Cadastro de usuários
        #Nome usuário
        self.username_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, placeholder_text='Nome do usuário', width=300,
                                                 font=('Roboto', 12),corner_radius=10, border_color='#1866a5')
        self.username_cadastro_entry.grid(row=1, column=0, padx=10, pady=10)

        #Email
        self.email_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, placeholder_text='E-mail do usuário', width=300,
                                                 font=('Roboto', 12), corner_radius=10, border_color='#1866a5')
        self.email_cadastro_entry.grid(row=2, column=0, padx=10, pady=10)

        #Senha
        self.password_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, placeholder_text='Criar Senha', width=300,
                                                 font=('Roboto', 12),corner_radius=10, border_color='#1866a5', show='*')
        self.password_cadastro_entry.grid(row=3, column=0, padx=10, pady=10)

        #Confirma Senha
        self.conf_password_entry = ctk.CTkEntry(self.frame_cadastro, placeholder_text='Confirmar Senha', width=300,
                                                 font=('Roboto', 12), corner_radius=10, border_color='#1866a5',show='*')
        self.conf_password_entry.grid(row=4, column=0, padx=10, pady=5)

        ## span = serve para colocar um recado na tela
        self.span = ctk.CTkLabel(self.frame_cadastro, text='Preencha todos os campos obrigatórios corretamente.',
                            font=('Roboto', 11), text_color='green')
        self.span.grid(row=5, column=0, padx=1, pady=1)

        #Botão de Cadastrar
        ## Botão de Chekbox
        self.ver_password = ctk.CTkCheckBox(self.frame_cadastro, text='Clique para ver a Senha', font=('Roboto', 12),
                                            corner_radius=10, command=self.show_password_cadastro)
        self.ver_password.grid(row=6, column=0, pady=5)

        # Botão de cadastrar_Usuário
        self.btn_cadastrar_user = ctk.CTkButton(self.frame_cadastro, text='Cadastrar'.upper(), width=300, fg_color='green', hover_color='#050',
                                          font=('Roboto', 12, 'bold'),corner_radius=10, command=self.add_cadastro)
        self.btn_cadastrar_user.grid(row=7, column=0, padx=10, pady=5)

        #Botão Voltar para a tela de Login
        self.btn_login_back = ctk.CTkButton(self.frame_cadastro, text='voltar p/ login'.upper(), width=300, font=('Roboto', 12, 'bold'),corner_radius=10,
                                            fg_color='#444', hover_color='#333', command=self.tela_login)
        self.btn_login_back.grid(row=8, column=0, padx=10, pady=5)

    # Função para Limpar dados do cadastro
    def limpa_cadastro(self):
        self.username_cadastro_entry.delete(0, END)
        self.email_cadastro_entry.delete(0, END)
        self.password_cadastro_entry.delete(0, END)
        self.conf_password_entry.delete(0, END)

    # Função para deixar a senha visível e no Botão de Chekbox chama => command=self.show_password_cadastro
    def show_password_cadastro(self):
        if self.password_cadastro_entry.cget("show") == "*":
            self.password_cadastro_entry.configure(show="")
        else:
            self.password_cadastro_entry.configure(show="*")


if __name__=="__main__":
    app = App()
    app.mainloop()