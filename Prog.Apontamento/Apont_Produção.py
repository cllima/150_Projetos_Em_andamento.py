from tkinter import *
from tkinter import ttk ## Para chamar o ListBox Treeview
from tkinter import tix # Balão de mensagem
from tkinter import messagebox # Caixa de mensagem
import datetime as dt
import sqlite3
## Gerando Relatório PDF Baixar na página > https://www.reportlab.com/software/opensource/rl-toolkit/download/
# Assistir vídeo # https://www.youtube.com/watch?v=DjxDm1MUbe0
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
from tkinter import messagebox
from PIL import ImageTk, Image  # imagem de botões
import base64


# Criando janela de Apontamento:
root=tix.Tk()

#Curso Tkinter - Aula 24 - Efeito gradiente no frame
class GradientFrame(Canvas):
    def __init__(self, parent, color1='', color2='', **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind('<Configure>', self._draw_gradient)
    def _draw_gradient(self, event=None):
        self.delete('gradient')
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1, g1, b1) = self.winfo_rgb(self._color1)
        (r2, g2, b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
            self.create_line(i,0,i, height, tags=('gradient',), fill=color)
        self.lower('gradient')

    ## Gerando Relatório PDF
    ##("apontamento.pdf") ## Aqui pode colocar a caminho da pasta conforme abaixo
    #E:\Python\pythonProject\ReratApontPDF\Apontamento.pdf

class Relatorios():
    def printApont(self):
        webbrowser.open("E:\Python\pythonProject\ReratApontPDF\Apontamento.pdf")
    def geraRelatApont(self):
# try e except => serve para informar erro
        try:
            self.apont = canvas.Canvas("E:\Python\pythonProject\ReratApontPDF\Apontamento.pdf")

            self.codigoRel = self.codigo_entry.get()
            self.operadorRel = self.operador_entry.get()
            self.nomeRel = self.nome_entry.get()
            self.maquiaRel = self.maquina_entry.get()
            self.opRel = self.op_entry.get()
            self.descrição_opRel = self.descrição_op_entry.get()
            self.cod_apRel = self.cod_ap_entry.get()
            self.desp_acertoRel = self.desp_acerto_entry.get()
            self.desp_virandoRel = self.desp_virando_entry.get()
            self.producaoRel = self.producao_entry.get()
            #self.horarioRel = self.horario_entry.get()

            self.apont.setFont("Helvetica-Bold", 14)
        ## drawString => desenha na tela
            self.apont.drawString(150, 775, 'Ficha de Apontamento - Produção Individual')
        ## Criar corpo do PDF => as descrições
            self.apont.setFont("Helvetica-Bold", 8)
            self.apont.drawString(50, 700, 'Código: ')
            self.apont.drawString(50, 680, 'Operador: ')
            self.apont.drawString(50, 660, 'Nome: ')
            self.apont.drawString(50, 640, 'Máquina: ')
            self.apont.drawString(50, 620, 'OP: ')
            self.apont.drawString(50, 600, 'Descrição da OP: ')
            self.apont.drawString(50, 580, 'Cod. Apontamento: ')
            self.apont.drawString(50, 560, 'Cod. Acerto: ')
            self.apont.drawString(50, 540, 'Cod. Virando: ')
            self.apont.drawString(50, 520, 'Produção: ')
            #self.apont.drawString(50, 500, 'Horário: ')

        ## Criar corpo do PDF a direita => Informações
            self.apont.setFont("Helvetica-Bold", 7)
            self.apont.drawString(150, 700, self.codigoRel)
            self.apont.drawString(150, 680, self.operadorRel)
            self.apont.drawString(150, 660, self.nomeRel)
            self.apont.drawString(150, 640, self.maquiaRel)
            self.apont.drawString(150, 620, self.opRel)
            self.apont.drawString(150, 600, self.descrição_opRel)
            self.apont.drawString(150, 580, self.cod_apRel)
            self.apont.drawString(150, 560, self.desp_acertoRel)
            self.apont.drawString(150, 540, self.desp_virandoRel)
            self.apont.drawString(150, 520, self.producaoRel)
            # self.apont.drawString(150, 500, self.horarioRel)
## Criando Moldura na folha
            self.apont.rect(20,500,550,1,fill=True, stroke=False)

        ## Chamar o PDF
            self.apont.showPage()
            ## Salvar o PDF
            self.apont.save()
            self.printApont()
        except:
            messagebox.showinfo(title="ERRO",message="Erro ao criar arquivo PDF!!!")
            return
        messagebox.showinfo(title="APONTAMENTO-MARGRAF",message="PDF-Criado com Sucesso!!")

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
        #self.horario_entry.delete(0,END)
    def conecta_bd(self): #Criando Banco de dados
        self.conn = sqlite3.connect('apontamentos.db')
        self.cursor = self.conn.cursor(); print('Conectando ao Banco de dados!!!')
    def desconecta_bd(self): #Sair do Banco de dados
        self.conn.close(); print('Desconectando do Banco de dados...')
    def montaTabelas(self):
        self.conecta_bd()
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
                data_horario VARCHAR(25)
            );
        """)
        self.conn.commit(); print('Banco de dados criado com Sucessso!!!')
        self.desconecta_bd()

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
        ## Caixa de Mensagem - estando fazia a caixa operador aparece a mensagem.
        if self.operador_entry.get() == "":
            msg = "Para iniciar um novo Apontamento é necessário \n"
            msg += "que seja digitado o Operador"
            messagebox.showinfo("Cadastro de Apontamento - Aviso!!!", msg)
        else:
            self.conecta_bd()
            ### Criando a 2ª Tabela do Banco de dados
            # (?) para cada coluna a ser alimentada
            self.cursor.execute(""" INSERT INTO apontamentos (operador, nome, maquina, op, descrição_op, cod_ap,
             desp_acerto, desp_virando, producao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                                (self.operador, self.nome, self.maquina, self.op, self.descrição_op, self.cod_ap,
                                 self.desp_acerto, self.desp_virando, self.producao))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista() # Sempre que entrar novo apontamento a lista gera td novamente
            self.limpar_tela() # Limpar Tela

    ### Criando a Tabela do Banco de dados
    ## ORDER BY operador ASC => Colocar em Ordem alfabetica
    def select_lista(self):
        self.listaApont.delete(*self.listaApont.get_children())
        self.conecta_bd()

        lista = self.cursor.execute(""" SELECT cod, operador, nome, maquina, op, descrição_op, cod_ap,
         desp_acerto, desp_virando, producao FROM apontamentos ORDER BY operador ASC; """) ## ASC => Crescente
        for i in lista:
            self.listaApont.insert("", END, values=i)
        self.desconecta_bd()

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
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM apontamentos WHERE cod = ?""", (self.codigo,)) ## <- precisa colocar uma vírgula, pois se trata de uma tupla
        self.conn.commit()
        self.desconecta_bd()
        self.limpar_tela()
        self.select_lista()
    def alterar_apontamento(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE apontamentos SET operador = ?, nome = ?, maquina = ?, op = ?, descrição_op = ?, 
        cod_ap = ?, desp_acerto = ?, desp_virando = ?, producao = ? WHERE cod = ? """,
                            (self.operador, self.nome, self.maquina, self.op, self.descrição_op, self.cod_ap,
                             self.desp_acerto, self.desp_virando, self.producao, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_tela()

## Faz uma busca pelo nome do operador
    def busca_Apontamento(self):
        self.conecta_bd()
        self.listaApont.delete(*self.listaApont.get_children())

        self.nome_entry.insert(END, '%') ## Colocando % na frente do nome
        nome = self.nome_entry.get()
        self.cursor.execute(""" SELECT cod, operador, nome, maquina, op, descrição_op, cod_ap,
         desp_acerto, desp_virando, producao FROM apontamentos WHERE nome LIKE '%s' ORDER BY nome ASC""" % nome)
        buscanomeApont = self.cursor.fetchall()
        for i in buscanomeApont:
            self.listaApont.insert("", END, values=i)
        self.limpar_tela()
        self.desconecta_bd()


    ## Função de Inicialização:
    ### Sempre que criar um método, precisa chamar ele aqui self...
class Apontamento(Funcs, Relatorios): ## Chama a classe Limpar função Front end
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
        self.root.minsize(width=900, height=500)

    ## Criando função frames => Janelas:
    ## Formas de trabalharmos com geometria e posicionamento => Pack;Grid;(Place) este é o melhor.
    ## Crindo Janela 1 e Janela 2
    def frames_da_tela(self):
        self.janela_1 =Frame(self.root,bd=4,bg='#EAE6E1',
                            highlightbackground='#4A5957',highlightthickness=0.5) #highlightthickness = largura da borda
        self.janela_1.place(relx=0.02,rely=0.03,relwidth=0.96,relheight=0.55) #1=direito, 0=esquerdo => dimensões da janela1.

        self.janela_2= Frame(self.root, bd=4, bg='#EAE6E1',
                             highlightbackground='#4A5957',highlightthickness=0.5)  # highlightthickness = largura da borda
        self.janela_2.place(relx=0.02, rely=0.60, relwidth=0.96,relheight=0.38)  # 1=direito, 0=esquerdo => dimensões da janela1.
    def widgets_janela1(self):
        # Criando Abas
        self.abas = ttk.Notebook(self.janela_1)
        self.aba1 = GradientFrame(self.abas, "#DCDCDC", "#A9A9A9")
        self.aba2 = GradientFrame(self.abas, "#808080", "#DCDCDC")
        self.aba3 = GradientFrame(self.abas, "#FFF0F5", "#F0FFFF")
        self.aba4 = Frame(self.abas)
        #Cores das Abas
        self.aba1.configure(background='#EAE6E1')
        self.aba2.configure(background='#DCDCDC')
        self.aba3.configure(background='#DCDCDC')
        self.aba4.configure(background='#DCDCDC')
        # Nome para cada Aba
        self.abas.add(self.aba1, text='Aba 1')
        self.abas.add(self.aba2, text='Aba 2')
        self.abas.add(self.aba3, text='Aba 3')
        self.abas.add(self.aba4, text='Aba 4')
        # Posicionar na Tela
        self.abas.place(relx=0.01, rely=0.0, relwidth=0.98, relheight=0.98)

        ## Caixa de texto Aba2
        self.lb_texto = Label(self.aba2, text='Caixa de Texto:', fg='#4543BA', font=('verdana', 7, 'bold'))
        self.lb_texto.place(relx=0.02, rely=0.10)
        self.texto_entry = Entry(self.aba2)
        self.texto_entry.place(relx=0.02, rely=0.17, height=180, width=500)

        ## Criando botão Novo
        self.bt_novo = Button(self.aba1, text='Novo', bd=4, bg='#D9D6D2', fg='#4543BA', activebackground='#008000', activeforeground='white'
                              , font=('verdana', 8, 'bold'), command=self.add_apontamento)  # bd=Borda, bg=cor de fundo, fg=cor de texto)
        self.bt_novo.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.15)  # place=lugar do botão

        ## Criando botão Limpar
        self.bt_limpar=Button(self.aba1, text='Limpar',bd=4,bg='#D9D6D2',fg='#4543BA',activebackground='#A9A9A9', activeforeground='white'
                              ,font=('verdana', 8,'bold'), command=self.limpar_tela) # bd=Borda, bg=cor de fundo, fg=cor de texto
        self.bt_limpar.place(relx=0.62,rely=0.05,relwidth=0.1, relheight=0.15) # place=lugar do botão

        ## Criando botão Buscar
        self.bt_buscar = Button(self.aba1, text='Buscar',bd=4,bg='#D9D6D2',fg='#4543BA',activebackground='#A9A9A9', activeforeground='white'
                              ,font=('verdana', 8,'bold'), command=self.busca_Apontamento) # bd=Borda, bg=cor de fundo, fg=cor de texto)
        self.bt_buscar.place(relx=0.16, rely=0.05, relwidth=0.1, relheight=0.15)  # place=lugar do botão

        # Variável balão de mensagem = Buscar
        texto_balao_buscar = "Informe o nome que deseja pesquisar"
        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.subwidget('label')['image'] = BitmapImage()  # tira a seta do balão
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg=texto_balao_buscar)

        ## Criando botão Alterar
        self.bt_alterar = Button(self.aba1, text='Alterar',bd=4,bg='#D9D6D2',fg='#4543BA',activebackground='#A9A9A9', activeforeground='white'
                              ,font=('verdana', 8,'bold'), command=self.alterar_apontamento) # bd=Borda, bg=cor de fundo, fg=cor de texto)
        self.bt_alterar.place(relx=0.73, rely=0.05, relwidth=0.1, relheight=0.15)  # place=lugar do botão

        ## Criando botão Excluir
        self.bt_excluir = Button(self.aba1, text='Excluir',bd=4,bg='#D9D6D2',fg='#4543BA',activebackground='#EC2300', activeforeground='white'
                              ,font=('verdana', 8,'bold'), command=self.deleta_apontamento)
        self.bt_excluir.place(relx=0.84, rely=0.05, relwidth=0.1, relheight=0.15)  # place=lugar do botão

        # Variável balão de mensagem = Excluir
        texto_balao_excluir = "Deseja realmente Excluir!!"
        self.balao_excluir = tix.Balloon(self.aba1)
        self.balao_excluir.subwidget('label')['image'] = BitmapImage()  # tira a seta do balão
        self.balao_excluir.bind_widget(self.bt_excluir, balloonmsg=texto_balao_excluir)

        ### Criando Botão para a bucar a Segunda Janela, neste caso deixei na opções
       # self.bt_buscarj = Button(self.aba1, text='2ª Janela', bd=4, bg='#D9D6D2', fg='#4543BA', activebackground='#A9A9A9',
                              #  activeforeground='white', font=('verdana', 8, 'bold'),command=self.segunda_janela)
      # self.bt_buscarj.place(relx=0.40, rely=0.05, relwidth=0.1, relheight=0.15)


        ###########################################################
        ## Criação da Label e Código
        self.lb_codigo = Label(self.aba1, text='Código', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_codigo.place(relx=0.05, rely=0.22)
        self.codigo_entry = Entry(self.aba1)
        self.codigo_entry.place(relx=0.15, rely=0.22, relwidth=0.02)

        ## Criação da Label e Entrada do Operador
        self.lb_operador=Label(self.aba1, text='Operador',fg='#4543BA',font=('verdana', 8,'bold'))
        self.lb_operador.place(relx=0.05, rely=0.32)
        self.operador_entry=Entry(self.aba1)
        self.operador_entry.place(relx=0.15, rely=0.32,relwidth=0.08)

        ## Criação da Label e Entrada do Nome
        self.lb_nome = Label(self.aba1, text='Nome') ## Nome
        self.lb_nome.place(relx=0.24, rely=0.32)
        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx=0.24, rely=0.32, relwidth=0.40)

        ## Criação da Label e Entrada Equipamento
        self.lb_maquina = Label(self.aba1, text='Máquina', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_maquina.place(relx=0.71, rely=0.32)
        self.maquina_entry = Entry(self.aba1)
        self.maquina_entry.place(relx=0.80, rely=0.32, relwidth=0.08)

        ## Criação da Label e Entrada OP
        self.lb_op = Label(self.aba1, text='Nº OP', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_op.place(relx=0.05, rely=0.5)
        self.op_entry = Entry(self.aba1)
        self.op_entry.place(relx=0.05, rely=0.6, relwidth=0.08)

        ## Criação da Label e Entrada Descrição OP
        self.lb_descrição_op = Label(self.aba1, text='Descrição da OP', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_descrição_op.place(relx=0.15, rely=0.5)
        self.descrição_op_entry = Entry(self.aba1)
        self.descrição_op_entry.place(relx=0.15, rely=0.6, relwidth=0.25)

        ## Criação da Label e Entrada Código Desp. de Acerto
        self.lb_cod_ap = Label(self.aba1, text='Cod. Apont', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_cod_ap.place(relx=0.05, rely=0.80)
        self.cod_ap_entry = Entry(self.aba1)
        self.cod_ap_entry.place(relx=0.05, rely=0.90, relwidth=0.07)

        ## Criação da Label e Entrada Desp. de Acerto
        self.lb_desp_acerto = Label(self.aba1, text='Desp. de Acerto', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_desp_acerto.place(relx=0.20, rely=0.80)
        self.desp_acerto_entry = Entry(self.aba1)
        self.desp_acerto_entry.place(relx=0.20, rely=0.90, relwidth=0.15)

        ## Criação da Label e Entrada Desp. Virando
        self.lb_desp_virando = Label(self.aba1, text='Desp. Virando', fg='#4543BA', font=('verdana', 8, 'bold'))
        self.lb_desp_virando.place(relx=0.48, rely=0.80)
        self.desp_virando_entry = Entry(self.aba1)
        self.desp_virando_entry.place(relx=0.48, rely=0.90, relwidth=0.15)

        ## Criação da Label e Entrada Produção
        self.lb_producao = Label(self.aba1, text='Qtd. Produzida',fg='#4543BA',font=('verdana', 8,'bold'))
        self.lb_producao.place(relx=0.78, rely=0.80)
        self.producao_entry = Entry(self.aba1)
        self.producao_entry.place(relx=0.78, rely=0.90, relwidth=0.15)

        #### dropdown button - Criando menu suspenso
        self.Tipvar = StringVar()
        self.TipV = ('Goss', 'M600','Off-Set','Kolbus')
        self.Tipvar.set('Goss')
        self.popupMenu = OptionMenu(self.aba3, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx=0.01, rely=0.02, relwidth=0.1, relheight=0.1)
        self.maquinas = self.Tipvar.get()
        print(self.maquinas)

    # Criando a Janela 2
    def widgets_janela2(self):
        self.listaApont=ttk.Treeview(self.janela_2,height=3,columns=("col1","col2","col3","col4","col5","col6",
                                                                     "col7","col8","col9","col10","col11"))
        self.listaApont.heading("#0", text="")
        self.listaApont.heading("#1", text="Cod.")
        self.listaApont.heading("#2", text="Operador")
        self.listaApont.heading("#3", text="Nome")
        self.listaApont.heading("#4", text="Máquina")
        self.listaApont.heading("#5", text="OP")
        self.listaApont.heading("#6", text="Descrição OP")
        self.listaApont.heading("#7", text="Código")
        self.listaApont.heading("#8", text="Desp. Acerto")
        self.listaApont.heading("#9", text="Desp. Virando")
        self.listaApont.heading("#10", text="Produção")
        self.listaApont.heading("#11", text="Horário")


# Criando o Tamanho das colunas
        self.listaApont.column("#0",width=0)
        self.listaApont.column("#1", width=2)
        self.listaApont.column("#2", width=28)
        self.listaApont.column("#3", width=150)
        self.listaApont.column("#4", width=25)
        self.listaApont.column("#5", width=20)
        self.listaApont.column("#6", width=180)
        self.listaApont.column("#7", width=20)
        self.listaApont.column("#8", width=50)
        self.listaApont.column("#9", width=50)
        self.listaApont.column("#10", width=40)
        self.listaApont.column("#11", width=35)


# Criando Posição das colunas
        self.listaApont.place(relx=0.01,rely=0.02,relwidth=0.956,relheight=0.98)

# Criando Barra de rolagem
        self.scroolLista=Scrollbar(self.janela_2,orient='vertical',command=self.listaApont.yview)
        self.listaApont.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.97, rely=0.02,relwidth=0.025,relheight=0.97)

## função duplo click ( event)
        self.listaApont.bind("<Double-1>", self.OnDoubleClick)

    # Criando Menu superior
    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar,tearoff= 0) ## tearoff= 0 => Elimina os tracejados
        filemenu2 = Menu(menubar,tearoff= 0)

        def Quit(): self.root.destroy()

        #Cria-se os menus e as variáveis e os nomes dos menus
        menubar.add_cascade(label= "Opções", menu= filemenu)
        menubar.add_cascade(label= "Relatórios", menu= filemenu2)

        # Cria-se os comandos
        filemenu.add_command(label= "Sair", command= Quit)
        filemenu.add_command(label= "Limpa Tela", command=self.limpar_tela)
        ## Buscando a 2ª Janela
        filemenu.add_command(label= "Ir para nova janela", command=self.segunda_janela) ## comando abrir_janela2

        filemenu2.add_command(label="Ficha de Apontamento", command=self.geraRelatApont)

    ## Trabalhando com múltiplas janelas - Toplevel
    def segunda_janela(self):
        self.root2 = Toplevel()
        self.root2.title('2ª Janela')
        self.root2.configure(background='#DCDCDC')
        self.root2.geometry('450x200')
        self.root2.resizable(False, False)
        self.root2.transient(self.root)
        self.root2.focus_force()  ## Deixa uma janela na frente da outra
        self.root2.grab_set()  ## Impede que seja apertado algum widget na 1ª janela
        ## Botão fechar
        self.botao_voltar = Button(self.root2,text='Fechar Janela', bd=4, bg='#D9D6D2', fg='#4543BA',
                                 activebackground='#c3d2d6', activeforeground='black'
                                 ,font=('verdana', 7, 'bold'), command=self.root2.destroy) ## .destroy = esse botão é responsável por fechar a janela.
        self.botao_voltar.grid()
        self.botao_voltar.place(relx=0.02, rely=0.05, relwidth=0.20, relheight=0.15) # place=lugar do botão


Apontamento()
