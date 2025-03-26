from tkinter import *
from tkinter import ttk
from tkinter import tix 
from tkinter import messagebox

import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business.cliente import Cliente

class Funcs():

    # limpa todos os campos de inserção 
    def limpa_tela(self):
        self.cpf_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.endereco_entry.delete(0, END)
    
    # atribui todos os campos a variáveis para 
    # facilitar a utilização

    def variaveis(self):
        self.cpf = self.cpf_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.endereco = self.endereco_entry.get()
    
    # método destinado a adição de itens no banco de dados
    def add_item(self):
        
        self.variaveis()

        # faz verificação se o campo nome, código ou valor está vazio
        # e exibe mensagem alerta caso for o caso
        if(self.nome == "") or (self.cpf == ""):
            msg = "Para cadastrar um novo cliente é necessário \n"
            msg += "que seja digitado pelo menos um CPF e nome"
            messagebox.showinfo("Cadastro de clientes - Aviso !!!", msg)
        # faz o cadastro do produto caso os campos estejam corretamente preenchidos
        else:
            novo_item = Cliente(self.cpf, self.nome, self.telefone, self.endereco)
            novo_item.strConnect()
            novo_item.salvar(1)

            self.select_lista()
            self.limpa_tela()
    
    # faz um select no banco e insere os produtos na lista 
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        c = Cliente('','','','')
        c.strConnect()
        lista = c.todos()

        for item in lista:
            self.listaCli.insert("", END, values=(item.cpf, item.nome, item.telefone, item.endereco))
    
    # define o método do evento de dois cliques na lista e insere as linhas nos campos
    def OnDoubleClick(self, event):
        self.variaveis()
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.cpf_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.endereco_entry.insert(END, col4)
        
    # método que faz a exclusão do produto no banco de dados    
    def deleta_item(self):
        
        self.variaveis()

        novo_item = Cliente(self.cpf, self.nome, self.telefone, self.endereco)
        novo_item.strConnect()
        novo_item.salvar(3)

        self.select_lista()
        self.limpa_tela()

    # método que faz a edição do produto no banco de dados
    def altera_item(self):
        self.variaveis()
        
        novo_item = Cliente(self.cpf, self.nome, self.telefone, self.endereco)
        novo_item.strConnect()
        novo_item.salvar(2)

        self.select_lista()
        self.limpa_tela()
    
    # método que faz o select de um produto e trás a informações para os campos 
    def busca_item(self):
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()

        c = Cliente('', '', '', '')
        c.strConnect()
        lista = c.busca(nome)

        for item in lista:
            self.listaCli.insert("", END, values=(item.cpf, item.nome, item.telefone, item.endereco))

        self.limpa_tela()


class telaCliente(Funcs):

    def __init__(self, aba1):
        self.aba1 = aba1
        self.widgets_cliente()
        self.lista_cliente()
        self.select_lista()

    def widgets_cliente(self):
        # cria um fundo 3d para os botões
        self.canvas_bt = Canvas(self.aba1, bd= 0, bg='#1e3743', highlightbackground= 'gray', highlightthickness= 4)
        self.canvas_bt.place(relx= 0.30, rely= 0.08, relwidth= 0.22, relheight= 0.09)
        
        ### Criação do botão limpar
        self.bt_limpar = Button(self.aba1, text="Limpar", bd=3, bg= '#4682B4', fg= 'white',
                                activebackground='#108ecb', activeforeground="white",
                                font= ('verdana', 8, 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx= 0.31, rely= 0.09, relwidth=0.1, relheight= 0.07)

        ### Criação do botão buscar
        self.bt_buscar = Button(self.aba1, text="Buscar", bd=3, bg= '#4682B4', fg= 'white',
                                activebackground='#108ecb', activeforeground="white", 
                                font= ('verdana', 8, 'bold'), command= self.busca_item)
        self.bt_buscar.place(relx= 0.41, rely= 0.09, relwidth=0.1, relheight= 0.07)

        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg= "Digite no campo nome o cliente que deseja pesquisar")

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
        self.bt_alterar.bind_widget(self.bt_alterar, balloonmsg= "Dê dois cliques no item da lista para trazer as informações do cliente")

        ### Criação do botão apagar
        self.bt_apagar = Button(self.aba1, text="Apagar", bd=3, bg= '#4682B4', fg= 'white', 
                                font= ('verdana', 8, 'bold'), command= self.deleta_item)
        self.bt_apagar.place(relx= 0.8, rely= 0.09, relwidth=0.1, relheight= 0.07)

        ### Criação da label e entrada do codigo
        self.lb_cpf = Label(self.aba1, text= "CPF", bg= None, fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_cpf.place(relx= 0.05, rely= 0.05)

        self.cpf_entry = Entry(self.aba1)
        self.cpf_entry.place(relx= 0.05, rely= 0.11, relwidth= 0.2)

        ### Criação da label e entrada do nome
        self.lb_nome = Label(self.aba1, text= "Nome", bg= 'whitesmoke', fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_nome.place(relx= 0.05, rely= 0.2)

        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx= 0.05, rely= 0.25, relwidth= 0.35)

        ### Criação da label e entrada do valor
        self.lb_telefone = Label(self.aba1, text= "Telefone", bg= 'whitesmoke', fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_telefone.place(relx= 0.05, rely= 0.35)

        self.telefone_entry = Entry(self.aba1)
        self.telefone_entry.place(relx= 0.05, rely= 0.4, relwidth= 0.35)

        ### Criação da label e entrada do descrição
        self.lb_endereco = Label(self.aba1, text= "Endereço", bg= 'whitesmoke', fg= '#107db2', font=("Helvetica", 10, "bold"))
        self.lb_endereco.place(relx= 0.5, rely= 0.25)

        self.endereco_entry = Entry(self.aba1)
        self.endereco_entry.place(relx= 0.5, rely= 0.32, relwidth= 0.4, relheight= 0.15)
    
    def lista_cliente(self):
        self.style = ttk.Style() 
        
        self.style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))

        self.listaCli = ttk.Treeview(self.aba1, height= 3, columns= ("col1", "col2", "col3", "col4"), style="Treeview")

        self.listaCli.heading('#0', text="")
        self.listaCli.heading('#1', text="CPF") 
        self.listaCli.heading('#2', text="Nome")
        self.listaCli.heading('#3', text="Telefone")
        self.listaCli.heading('#4', text="Endereço")

        self.listaCli.column("#0", width=0, anchor= "center")
        self.listaCli.column("#1", width=50, anchor= "center")
        self.listaCli.column("#2", width=55, anchor= "center")
        self.listaCli.column("#3", width=150, anchor= "center")
        self.listaCli.column("#4", width=100, anchor= "center")

        self.listaCli.place(relx= 0.01, rely= 0.5, relwidth= 0.95, relheight= 0.49)

        self.scroolLista = Scrollbar(self.aba1, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.95, rely=0.5, relwidth=0.045, relheight=0.49)

        self.listaCli.bind("<Double-1>", self.OnDoubleClick)