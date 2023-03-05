import sqlite3
from tkinter import messagebox

# Conectando ao Banco de Dados
### Criando Banco de Dados
class BackEnd():
    def conecta_db(self):
        self.conn = sqlite3.connect('Cadastro_login.db')
        self.cursor = self.conn.cursor()
        print('\33[1:32mBanco de Dados conectado com Sucesso!\33[m')

    # Desconectando do Banco de dados
    def desconecta_db(self):
        self.conn.close()
        print("\33[1:33mDesconectando do Banco de Dados..!\33[m")

    # Criando Tabela Banco de dados
    def cria_tabela(self):
        self.conecta_db()
        ### Criando tabela
        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS Usuarios(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL,
                Email TEXT NOT NULL,
                Senha TEXT NOT NULL,
                Confirma_Senha TEXT NOT NULL
            );
        """)
        self.conn.commit()
        print("\33[1:34mBanco de dados criado com SUCESSO!!!\33[m")
        self.desconecta_db()

    ## Foi criado a função Variaveis para evitar repetir código.
    def variaveis(self):
        self.username_cadastro = self.username_cadastro_entry.get()
        self.email_cadastro = self.email_cadastro_entry.get()
        self.password_cadastro = self.password_cadastro_entry.get()
        self.conf_password = self.conf_password_entry.get()

    ## Criando função para Salvar usuário
    # Adicionar Cadastro
    def add_cadastro(self):
        self.variaveis()

        #print(self.username_cadastro) # Aparece o nome na RUN
        self.conecta_db()

         # Inserindo na Tabela Usuarios o Nome, Email, Senha e Confirma Senha
        self.cursor.execute("""
            INSERT INTO Usuarios (Username, Email, Senha, Confirma_Senha)
            VALUES (?, ?, ?, ?)""", (self.username_cadastro, self.email_cadastro, self.password_cadastro, self.conf_password))

        ##Tratamento de erros:
        try:
            if (self.username_cadastro == "" or self.email_cadastro == "" or self.password_cadastro == ""
                    or self.conf_password == ""):
                messagebox.showerror(title='Sistema de Login', message='ERRO!!!\nPor favor preencha todos os campos!')
            elif (len(self.username_cadastro) < 4):
                messagebox.showinfo(title='Sistema de Login', message='O nome do usuário deve ter pelo menos, 4 caracteres.')
            elif (self.password_cadastro != self.conf_password):
                messagebox.showerror(title='Sistema de Login', message='ERRO!!!\nAs senhas informadas não são iguais.')

            elif (len(self.password_cadastro) < 4):
                messagebox.showinfo(title='Sistema de Login', message='A senha deve ter pelo menos, 4 digitos.')
            else:
                self.conn.commit()
                messagebox.showinfo(title='Sistema de Login', message=f'Parabéns {self.username_cadastro}'
                                                                      f'\nOs seus dados foram cadastrados com SUCESSO!!!')
                self.desconecta_db()
                self.limpa_cadastro()

        except:
            messagebox.showerror(title='Sistema de Login', message='Erro no processamento do seu Cadastro\nPor favor tente novamente!')
            self.desconecta_db()

        print("\33[1:35mDados cadastrados com SUCESSO!!!\33[m")

    #Verificando Login
    def verifica_login(self):
        self.username_login = self.username_login_entry.get()
        self.password_login = self.password_login_entry.get()

        #Checando se a senha aparece no terminal e se apaga os dados da tela de login após confirmar
        #print(self.username_login, self.password_login)
        #self.limpa_login()

        ##Verificando se o Usuário esta cadastrado no Banco de Dados.
        self.conecta_db()
        self.cursor.execute("""SELECT * FROM Usuarios WHERE (Username = ? AND Senha = ?)""", (self.username_login, self.password_login))

        ## Percorrendo no Banco de Dados os dados dos Usuários.
        self.verifica_dados = self.cursor.fetchone()

        try:
            if (self.username_login == '' or self.password_login == ''):
                messagebox.showwarning(title='Sistema de Login', message='Por favor, preencha todos os campos!')
            elif (self.username_login in self.verifica_dados and self.password_login in self.verifica_dados):
                messagebox.showinfo(title='Sistema de Login', message=f'Parabens {self.username_login}\nLogin feito com SUCESSO!')
                self.desconecta_db()
                self.limpa_login()
        except:
            messagebox.showerror(title='Sistema de Login', message='ERRO!!!\nDados não encontrado no Sistema, verifique!\nPor favor, '
                                                                   'verifique os seus dados ou Cadastre-se em nosso Sistema')
            self.desconecta_db()










