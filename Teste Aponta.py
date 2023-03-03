from tkinter import*
from tkinter import ttk ## Para chamar o ListBox Treeview
import datetime as dt
import sqlite3

# Criando janela de Apontamento:
root=Tk()

## Aqui são criados as funções CRUD
class Funcs(): ## Cria-se uma classe para cada função Back end
    def limpar_tela(self):
        self.codigo_entry.delete(0,END)
        self.operador_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.maquina_entry.delete(0,END)
        self.op_entry.delete(0,END)
        self.descrição_op_entry.delete(0,END)
        self.cod_ap_entry.delete(0,END)
        self.desp_acerto_entry.delete(0,END)
        self.desp_virando_entry.delete(0,END)
        self.producao_entry.delete(0,END)
    def conecta_db(self): #Criando Banco de dados
        self.conn = sqlite3.connect('apontamentos.bd')
        self.cursor = self.conn.cursor(); print('Conectando ao Banco de dados!!!')
    def desconecta_db(self): #Sair do Banco de dados
        self.conn.close(); print('Desconectando do Banco de dados...')
    def montaTabelas(self):
        self.conecta_db()
        ### Criando a Tabela do Banco de dados
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS apontamentos(
                cod INTEGER PRIMARY KEY,
                operador INTERGER(10) NOT NULL,
                nome CHAR (30) NOT NULL,
                maquina CHAR(10) NOT NULL,
                op INTERGER(10) NOT NULL,
                descrição_op CHAR(30) NOT NULL,
                cod_ap INTERGER(10) NOT NULL,
                desp_acerto INTERGER(15),
                desp_virando INTERGER(15),
                producao INTERGER(15),
                data_horario INTERGER(25)
            );
        """)
        self.conn.commit(); print('Banco de dados criado com Sucessso!!!')
        self.desconecta_db()

    ## Foi criado a função Variaveis para evitar repetir código.
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.operador = self.operador_entry.get()
        self.nome = self.nome_entry.get()
        self.maquina = self.maquina_entry.get()
        self.op = self.op_entry.get()
        self.descrição_op = self.descrição_op_entry.get()
        self.cod_ap = self.cod_ap_entry.get()
        self.desp_acerto = self.desp_acerto_entry.get()
        self.desp_virando = self.desp_virando_entry.get()
        self.producao = self.producao_entry.get()
    def add_apontamento(self):
        self.variaveis()
        self.conecta_db()

        ### Criando a 2ª Tabela do Banco de dados
        # (?) para cada coluna a ser alimentada
        self.cursor.execute(""" INSERT INTO apontamentos (operador, nome, maquina, op, descrição_op, cod_ap,
         desp_acerto, desp_virando, producao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                            (self.operador, self.nome, self.maquina, self.op, self.descrição_op, self.cod_ap,
                             self.desp_acerto, self.desp_virando, self.producao))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista() # Sempre que entrar novo apontamento a lista gera td novamente
        self.limpar_tela() # Limpar Tela

    ### Criando a Tabela do Banco de dados
    ## ORDER BY operador ASC => Colocar em Ordem alfabetica
    def select_lista(self):
        self.listaApont.delete(*self.listaApont.get_children())
        self.conecta_db()
                     #foi retirado a palavra cod, pois não esta atribuindo devido ao erro, arrumar depois
        lista = self.cursor.execute(""" SELECT cod, operador, nome, maquina, op, descrição_op, cod_ap,
         desp_acerto, desp_virando, producao FROM apontamentos ORDER BY cod DESC; """) ## ASC => Crescente
        for i in lista:
            self.listaApont.insert("", END, values=i)
        self.desconecta_db()

    ## Função seleciona linha com duplo click e pucha os dados para memória
    def OnDoubleClick(self, event):  ## Tradução => Ao clicar duas vezes
        self.limpar_tela() # limpa tela antes de selecionar
        self.listaApont.selection() # Seleciona a lista apontamento

        for n in self.listaApont.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9,col10 = self.listaApont.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.operador_entry.insert(END, col2)
            self.nome_entry.insert(END, col3)
            self.maquina_entry.insert(END, col4)
            self.op_entry.insert(END, col5)
            self.descrição_op_entry.insert(END, col6)
            self.cod_ap_entry.insert(END, col7)
            self.desp_acerto_entry.insert(END, col8)
            self.desp_virando_entry.insert(END, col9)
            self.producao_entry.insert(END, col10)

    ## Função Deleta Apontamento
    def deleta_apontamento(self):
        self.variaveis() ## chama a função variaveis
        self.conecta_db()
        self.cursor.execute(""" DELETE FROM apontamentos WHERE cod = ?""", self.codigo)
        self.conn.commit()
        self.desconecta_db()
        self.limpar_tela()
        self.select_lista()
    def alterar_apontamento(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute(""" UPDATE apontamentos SET operador = ?, nome = ?, maquina = ?, op = ?, descrição_op = ?, 
        cod_ap = ?, desp_acerto = ?, desp_virando = ?, producao = ? WHERE cod = ? """,
                            (self.operador, self.nome, self.maquina, self.op, self.descrição_op, self.cod_ap,
                             self.desp_acerto, self.desp_virando, self.producao, self.codigo))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpar_tela()


## Função de Inicialização:
### Sempre que criar um método, precisa chamar ele aqui self...
class Apontamento(Funcs): ## Chama a classe Limpar função Front end
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_janela1() ##Botões Janela1
        self.widgets_janela2() ## Janela2
        self.montaTabelas()
        self.select_lista()
        self.Menus()
        #self.data_criacao = dt.datetime.now()
        #self.data_criacao = self.data_criacao.strftime('%d/%m/%Y %H:%M')

        root.mainloop()

## Criando função configuração tela Principal:
    def tela(self):
        self.root.title('SISTEMA DE APONTAMENTO DE PRODUÇÃO - MARGRAF')
        self.root.configure(background='#e2d9db')
        self.root.geometry("800x500")
        self.root.resizable(True,True) #Responsividade
        self.root.maxsize(width=1100,height=680) # Largura x Altura da Tela principal
        self.root.minsize(width=600, height=400)

## Criando função frames => Janelas:
## Formas de trabalharmos com geometria e posicionamento => Pack;Grid;(Place) este é o melhor.
## Crindo Janela 1 e Janela 2
    def frames_da_tela(self):
        self.janela_1 =Frame(self.root,bd=4,bg='#EAE6E1',
                            highlightbackground='#4A5957',highlightthickness=0.5) #highlightthickness = largura da borda
        self.janela_1.place(relx=0.02,rely=0.03,relwidth=0.96,relheight=0.55) #1=direito, 0=esquerdo => dimensões da janela1.

        self.janela_2= Frame(self.root, bd=4, bg='#EAE6E1',
                             highlightbackground='#4A5957',highlightthickness=0.5)  # highlightthickness = largura da borda
        self.janela_2.place(relx=0.02, rely=0.62, relwidth=0.96,relheight=0.34)  # 1=direito, 0=esquerdo => dimensões da janela1.
    def widgets_janela1(self):
        ## Criando botão Novo
        self.bt_novo = Button(self.janela_1, text='Novo', bd=4, bg='#D9D6D2', fg='#4543BA'
                              , font=('verdana', 8, 'bold'), command=self.add_apontamento)  # bd=Borda, bg=cor de fundo, fg=cor de texto)
        self.bt_novo.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.15)  # place=lugar do botão

        ## Criando botão Limpar
        self.bt_limpar=Button(self.janela_1, text='Limpar',bd=4,bg='#D9D6D2',fg='#4543BA'
                              ,font=('verdana', 8,'bold'), command=self.limpar_tela) # bd=Borda, bg=cor de fundo, fg=cor de texto
        self.bt_limpar.place(relx=0.62,rely=0.05,relwidth=0.1, relheight=0.15) # place=lugar do botão

        ## Criando botão Buscar
        self.bt_buscar = Button(self.janela_1, text='Buscar',bd=4,bg='#D9D6D2',fg='#4543BA'
                              ,font=('verdana', 8,'bold')) # bd=Borda, bg=cor de fundo, fg=cor de texto)
        self.bt_buscar.place(relx=0.16, rely=0.05, relwidth=0.1, relheight=0.15)  # place=lugar do botão

        ## Criando botão Alterar
        self.bt_alterar = Button(self.janela_1, text='Alterar',bd=4,bg='#D9D6D2',fg='#4543BA'
                              ,font=('verdana', 8,'bold'), command=self.alterar_apontamento) # bd=Borda, bg=cor de fundo, fg=cor de texto)
        self.bt_alterar.place(relx=0.73, rely=0.05, relwidth=0.1, relheight=0.15)  # place=lugar do botão

        ## Criando botão Excluir
        self.bt_excluir = Button(self.janela_1, text='Excluir',bd=4,bg='#D9D6D2',fg='#4543BA'
                              ,font=('verdana', 8,'bold'), command=self.deleta_apontamento)
        self.bt_excluir.place(relx=0.84, rely=0.05, relwidth=0.1, relheight=0.15)  # place=lugar do botão

        ###########################################################
        ## Criação da Label e Código
        self.lb_codigo = Label(self.janela_1, text='Código', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_codigo.place(relx=0.05, rely=0.22)
        self.codigo_entry = Entry(self.janela_1)
        self.codigo_entry.place(relx=0.15, rely=0.22, relwidth=0.02)

        ## Criação da Label e Entrada do Operador
        self.lb_operador=Label(self.janela_1, text='Operador',fg='#4543BA',font=('verdana', 8,'bold'))
        self.lb_operador.place(relx=0.05, rely=0.32)
        self.operador_entry=Entry(self.janela_1)
        self.operador_entry.place(relx=0.15, rely=0.32,relwidth=0.08)

        ## Criação da Label e Entrada do Nome
        self.lb_nome = Label(self.janela_1, text='Nome') ## Nome
        self.lb_nome.place(relx=0.24, rely=0.32)
        self.nome_entry = Entry(self.janela_1)
        self.nome_entry.place(relx=0.24, rely=0.32, relwidth=0.40)

        ## Criação da Label e Entrada Equipamento
        self.lb_maquina = Label(self.janela_1, text='Máquina', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_maquina.place(relx=0.71, rely=0.32)
        self.maquina_entry = Entry(self.janela_1)
        self.maquina_entry.place(relx=0.80, rely=0.32, relwidth=0.08)

        ## Criação da Label e Entrada OP
        self.lb_op = Label(self.janela_1, text='Nº OP', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_op.place(relx=0.05, rely=0.5)
        self.op_entry = Entry(self.janela_1)
        self.op_entry.place(relx=0.05, rely=0.6, relwidth=0.08)

        ## Criação da Label e Entrada Descrição OP
        self.lb_descrição_op = Label(self.janela_1, text='Descrição da OP', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_descrição_op.place(relx=0.15, rely=0.5)
        self.descrição_op_entry = Entry(self.janela_1)
        self.descrição_op_entry.place(relx=0.15, rely=0.6, relwidth=0.25)

        ## Criação da Label e Entrada Código Desp. de Acerto
        self.lb_cod_ap = Label(self.janela_1, text='Cod. Apont', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_cod_ap.place(relx=0.05, rely=0.80)
        self.cod_ap_entry = Entry(self.janela_1)
        self.cod_ap_entry.place(relx=0.05, rely=0.90, relwidth=0.07)

        ## Criação da Label e Entrada Desp. de Acerto
        self.lb_desp_acerto = Label(self.janela_1, text='Desp. de Acerto', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_desp_acerto.place(relx=0.20, rely=0.80)
        self.desp_acerto_entry = Entry(self.janela_1)
        self.desp_acerto_entry.place(relx=0.20, rely=0.90, relwidth=0.15)

        ## Criação da Label e Entrada Desp. Virando
        self.lb_desp_virando = Label(self.janela_1, text='Desp. Virando', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_desp_virando.place(relx=0.48, rely=0.80)
        self.desp_virando_entry = Entry(self.janela_1)
        self.desp_virando_entry.place(relx=0.48, rely=0.90, relwidth=0.15)

        ## Criação da Label e Entrada Produção
        self.lb_producao = Label(self.janela_1, text='Qtd. Produzida',fg='#4543BA',font=('verdana', 8,'bold'))
        self.lb_producao.place(relx=0.78, rely=0.80)
        self.producao_entry = Entry(self.janela_1)
        self.producao_entry.place(relx=0.78, rely=0.90, relwidth=0.15)

# Criando a Janela 2
    def widgets_janela2(self):
        self.listaApont=ttk.Treeview(self.janela_2,height=3,columns=("col1","col2","col3","col4","col5","col6",
                                                                     "col7","col8","col9"))
        self.listaApont.heading("#0", text="Cod.")
        self.listaApont.heading("#1", text="Operador")
        self.listaApont.heading("#2", text="Nome")
        self.listaApont.heading("#3", text="Máquina")
        self.listaApont.heading("#4", text="OP")
        self.listaApont.heading("#5", text="Descrição_OP")
        self.listaApont.heading("#6", text="Código")
        self.listaApont.heading("#7", text="Desp_acerto")
        self.listaApont.heading("#8", text="Desp_virando")
        self.listaApont.heading("#9", text="Produção")

        #self.listaApont.heading("#10", text="Horas")


# Criando o Tamanho das colunas
        self.listaApont.column("#0",width=1)
        self.listaApont.column("#1", width=30)
        self.listaApont.column("#2", width=180)
        self.listaApont.column("#3", width=40)
        self.listaApont.column("#4", width=50)
        self.listaApont.column("#5", width=180)
        self.listaApont.column("#6", width=20)
        self.listaApont.column("#7", width=50)
        self.listaApont.column("#8", width=50)
        self.listaApont.column("#9", width=80)


# Criando Posição das colunas
        self.listaApont.place(relx=0.01,rely=0.1,relwidth=0.95,relheight=0.85)

# Criando Barra de rolagem
        self.scroolista=Scrollbar(self.janela_2,orient='vertical')
        self.listaApont.configure(yscroll=self.scroolista.set)
        self.scroolista.place(relx=0.96, rely=0.1,relwidth=0.04,relheight=0.85)

## função duplo click ( event)
        self.listaApont.bind("<Double-1>", self.OnDoubleClick)

    # Criando Menu superior
    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        #Cria-se os menus e as variáveis e os nomes dos menus
        menubar.add_cascade(label= "Opções", menu= filemenu)
        menubar.add_cascade(label= "Sobre", menu= filemenu2)
        # Cria-se os comandos
        filemenu.add_command(label= "Sair", command= Quit)
        filemenu2.add_command(label= "Limpa Tela", command=self.limpar_tela)


Apontamento()
