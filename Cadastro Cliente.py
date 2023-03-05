from tkinter import *
from tkinter import ttk
import sqlite3


import webbrowser
from PIL import ImageTk , Image
import base64

root = Tk()

class Relatorios():
    def printCliente(self):
        webbrowser.open("cliente.pdf")
    def geraRelatCliente(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.foneRel = self.fone_entry.get()
        self.cidadeRel = self.cidade_entry.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, 'Codigo: ')
        self.c.drawString(50, 670, 'Nome: ')
        self.c.drawString(50, 630, 'Telefone: ')
        self.c.drawString(50, 600, 'Cidade: ')

        self.c.setFont("Helvetica", 18)
        self.c.drawString(150, 700, self.codigoRel)
        self.c.drawString(150, 670, self.nomeRel)
        self.c.drawString(150, 630, self.foneRel)
        self.c.drawString(150, 600, self.cidadeRel)

        self.c.rect(20, 720, 550, 200, fill= False, stroke=True)

        self.c.showPage()
        self.c.save()
        self.printCliente()

class Funcs():
    def limpa_cliente(self):
        self.codigo_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.nome_entry.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")
    def montaTabelas(self):
        self.conecta_bd()
        ### Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)               
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
    def OnDoubleClick(self, event):
        self.limpa_cliente()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.fone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ? """,
                            (self.nome, self.fone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo,))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_cliente()
        self.select_lista()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()
    def busca_cliente(self):
        self.conecta_bd()
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, cidade FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("", END, values=i)
        self.limpa_cliente()
        self.desconecta_bd()
    def images_base64(self):
        self.btnovo_base64 = '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'

class Application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.images_base64()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background= '#1e3743')
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height= 700)
        self.root.minsize(width=500, height= 400)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg= '#dfe3ee',
                             highlightbackground= '#759fe6', highlightthickness=3 )
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    def widgets_frame1(self):
        self.canvas_bt = Canvas(self.frame_1, bd=0, bg='#1e3743', highlightbackground = 'gray',
            highlightthickness=5)
        self.canvas_bt.place(relx= 0.19, rely= 0.08, relwidth= 0.22, relheight=0.19)

        ### Criação do botao limpar
        self.bt_limpar = Button(self.frame_1, text= "Limpar", bd=2, bg = '#107db2',fg = 'white',
                                activebackground='#108ecb', activeforeground="white"
                                , font = ('verdana', 8, 'bold'), command= self.limpa_cliente)
        self.bt_limpar.place(relx= 0.2, rely=0.1, relwidth=0.1, relheight= 0.15)
        ### Criação do botao buscar
        self.bt_limpar = Button(self.frame_1, text="Buscar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command = self.busca_cliente)
        self.bt_limpar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao novo
        ## imgNovo
        self.btnovo = PhotoImage(data=base64.b64decode(self.btnovo_base64))
        self.btnovo = self.btnovo.subsample(2, 2)

        self.bt_novo = Button(self.frame_1, bd =0, image = self.btnovo, command= self.add_cliente)
        self.bt_novo.place(relx=0.58, rely=0.1, width=60, height=30)

        ### Criação do botao alterar
        self.bt_limpar = Button(self.frame_1, text="Alterar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.altera_cliente)
        self.bt_limpar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botao apagar
        self.bt_limpar = Button(self.frame_1, text="Apagar", bd=2, bg = '#107db2',fg = 'white'
                                , font = ('verdana', 8, 'bold'), command=self.deleta_cliente)
        self.bt_limpar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ## Criação da label e entrada do codigo
        self.lb_codigo = Label(self.frame_1, text = "Código", bg= '#dfe3ee', fg = '#107db2')
        self.lb_codigo.place(relx= 0.05, rely= 0.05 )

        self.codigo_entry = Entry(self.frame_1 )
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.08)

        ## Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text="Nome", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        ## Criação da label e entrada do telefone
        self.lb_nome = Label(self.frame_1, text="Telefone", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.05, rely=0.6)

        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        ## Criação da label e entrada da cidade
        self.lb_nome = Label(self.frame_1, text="Cidade", bg= '#dfe3ee', fg = '#107db2')
        self.lb_nome.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3,
                                     column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)
        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label= "Opções", menu=filemenu)
        menubar.add_cascade(label="Relatorios", menu=filemenu2)

        filemenu.add_command(label="Sair", command=Quit)
        filemenu.add_command(label="Limpa cliente", command= self.limpa_cliente)

        filemenu2.add_command(label="Ficha do cliente", command=self.geraRelatCliente)


Application()