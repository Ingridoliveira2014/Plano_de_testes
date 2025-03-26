from tkinter import *
from tkinter import ttk
from tkinter import tix 
from tkinter import messagebox

import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business.produto import Produto

# classe destinada as funções que serão utilizadas na aplicação
class Funcs():

    # limpa todos os campos de inserção 
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.valor_entry.delete(0, END)
        self.descricao_entry.delete(0, END)
    
    # atribui todos os campos a variáveis para 
    # facilitar a utilização

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.valor = self.valor_entry.get()
        self.descricao = self.descricao_entry.get()
    
    # método destinado a adição de itens no banco de dados
    def add_item(self):
        
        self.variaveis()

        # faz verificação se o campo nome, código ou valor está vazio
        # e exibe mensagem alerta caso for o caso
        if(self.nome == "") or (self.codigo == "") or (self.valor == ""):
            msg = "Para cadastrar um novo produto é necessário \n"
            msg += "que seja digitado pelo menos um codigo, nome e valor"
            messagebox.showinfo("Cadastro de produtos - Aviso !!!", msg)
        # faz o cadastro do produto caso os campos estejam corretamente preenchidos
        else:
            novo_item = Produto(self.codigo, self.nome, self.valor, self.descricao)
            novo_item.strConnect()
            novo_item.salvar(1)

            self.select_lista()
            self.limpa_tela()
    
    # faz um select no banco e insere os produtos na lista 
    def select_lista(self):
        self.listaProd.delete(*self.listaProd.get_children())
        p = Produto('','','','')
        p.strConnect()
        lista = p.todos()

        for item in lista:
            self.listaProd.insert("", END, values=(item.codigo, item.nome, f"R${item.valor:.2f}", item.descricao))
    
    # define o método do evento de dois cliques na lista e insere as linhas nos campos
    def OnDoubleClick(self, event):
        self.variaveis()
        self.limpa_tela()
        self.listaProd.selection()

        for n in self.listaProd.selection():
            col1, col2, col3, col4 = self.listaProd.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.valor_entry.insert(END, col3.replace("R$", ""))
            self.descricao_entry.insert(END, col4)
        
    # método que faz a exclusão do produto no banco de dados    
    def deleta_item(self):
        
        self.variaveis()

        novo_item = Produto(self.codigo, self.nome, self.valor, self.descricao)
        novo_item.strConnect()
        novo_item.salvar(3)

        self.select_lista()
        self.limpa_tela()

    # método que faz a edição do produto no banco de dados
    def altera_item(self):
        self.variaveis()
        
        novo_item = Produto(self.codigo, self.nome, self.valor, self.descricao)
        novo_item.strConnect()
        novo_item.salvar(2)

        self.select_lista()
        self.limpa_tela()
    
    # método que faz o select de um produto e trás a informações para os campos 
    def busca_item(self):
        self.listaProd.delete(*self.listaProd.get_children())

        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()

        p = Produto('', '', '', '')
        p.strConnect()
        lista = p.busca(nome)

        for item in lista:
            self.listaProd.insert("", END, values=(item.codigo, item.nome, item.valor, item.descricao))

        self.limpa_tela()

class telaProduto(Funcs):

    def __init__(self, aba1):
        self.aba1 = aba1
        self.widgets_produto()
        self.lista_produto()
        self.select_lista()

    def widgets_produto(self):
        # cria um fundo 3d para os botões
        self.canvas_bt = Canvas(self.aba1, bd= 0, bg='#1e3743', highlightbackground= 'gray', highlightthickness= 4)
        self.canvas_bt.place(relx= 0.19, rely= 0.08, relwidth= 0.22, relheight= 0.09)
        
        ### Criação do botão limpar
        self.bt_limpar = Button(self.aba1, text="Limpar", bd=3, bg= '#4682B4', fg= 'white',
                                activebackground='#108ecb', activeforeground="white",
                                font= ('verdana', 8, 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx= 0.2, rely= 0.09, relwidth=0.1, relheight= 0.07)

        ### Criação do botão buscar
        self.bt_buscar = Button(self.aba1, text="Buscar", bd=3, bg= '#4682B4', fg= 'white',
                                activebackground='#108ecb', activeforeground="white", 
                                font= ('verdana', 8, 'bold'), command= self.busca_item)
        self.bt_buscar.place(relx= 0.3, rely= 0.09, relwidth=0.1, relheight= 0.07)

        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg= "Digite no campo nome o produto que deseja pesquisar")

        self.canvas_bt = Canvas(self.aba1, bd= 0, bg='#1e3743', highlightbackground= 'gray', highlightthickness= 4)
        self.canvas_bt.place(relx= 0.59, rely= 0.08, relwidth= 0.32, relheight= 0.09)

        ### Criação do botão novo
        self.bt_novo = Button(self.aba1, text="Novo", bd=3, bg= '#4682B4', fg= 'white', 
                                font= ('verdana', 8, 'bold'), command= self.add_item)
        self.bt_novo.place(relx= 0.6, rely= 0.09, relwidth=0.1, relheight= 0.07)
        ### Criação do botão alterar
        self.bt_alterar = Button(self.aba1, text="Alterar", bd=3, bg= '#4682B4', fg= 'white', 
                                font= ('verdana', 8, 'bold'), command= self.altera_item)
        self.bt_alterar.place(relx= 0.7, rely= 0.09, relwidth=0.1, relheight= 0.07)

        self.bt_alterar = tix.Balloon(self.aba1)
        self.bt_alterar.bind_widget(self.bt_alterar, balloonmsg= "Dê dois cliques no item da lista para trazer as informações do produto")

        ### Criação do botão apagar
        self.bt_apagar = Button(self.aba1, text="Apagar", bd=3, bg= '#4682B4', fg= 'white', 
                                font= ('verdana', 8, 'bold'), command= self.deleta_item)
        self.bt_apagar.place(relx= 0.8, rely= 0.09, relwidth=0.1, relheight= 0.07)

        ### Criação da label e entrada do codigo
        self.lb_codigo = Label(self.aba1, text= "Código", bg= None, fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_codigo.place(relx= 0.05, rely= 0.05)

        self.codigo_entry = Entry(self.aba1)
        self.codigo_entry.place(relx= 0.05, rely= 0.11, relwidth= 0.10)

        ### Criação da label e entrada do nome
        self.lb_nome = Label(self.aba1, text= "Nome", bg= 'whitesmoke', fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_nome.place(relx= 0.05, rely= 0.2)

        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx= 0.05, rely= 0.25, relwidth= 0.35)

        ### Criação da label e entrada do valor
        self.lb_valor = Label(self.aba1, text= "Valor", bg= 'whitesmoke', fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_valor.place(relx= 0.05, rely= 0.35)

        self.valor_entry = Entry(self.aba1)
        self.valor_entry.place(relx= 0.05, rely= 0.4, relwidth= 0.15)

        ### Criação da label e entrada do descrição
        self.lb_descricao = Label(self.aba1, text= "Descrição", bg= 'whitesmoke', fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_descricao.place(relx= 0.5, rely= 0.25)

        self.descricao_entry = Entry(self.aba1)
        self.descricao_entry.place(relx= 0.5, rely= 0.32, relwidth= 0.4, relheight= 0.15)
    
    def lista_produto(self):
        self.style = ttk.Style() 
        
        self.style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))

        self.listaProd = ttk.Treeview(self.aba1, height= 3, columns= ("col1", "col2", "col3", "col4"), style="Treeview")

        self.listaProd.heading('#0', text="")
        self.listaProd.heading('#1', text="Codigo") 
        self.listaProd.heading('#2', text="Nome")
        self.listaProd.heading('#3', text="Valor")
        self.listaProd.heading('#4', text="Descrição")

        self.listaProd.column("#0", width=0, anchor= "center")
        self.listaProd.column("#1", width=30, anchor= "center")
        self.listaProd.column("#2", width=100, anchor= "center")
        self.listaProd.column("#3", width=40, anchor= "center")
        self.listaProd.column("#4", width=100, anchor= "center")

        self.listaProd.place(relx= 0.01, rely= 0.5, relwidth= 0.95, relheight= 0.49)

        self.scroolLista = Scrollbar(self.aba1, orient='vertical')
        self.listaProd.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.95, rely=0.5, relwidth=0.045, relheight=0.49)

        self.listaProd.bind("<Double-1>", self.OnDoubleClick)