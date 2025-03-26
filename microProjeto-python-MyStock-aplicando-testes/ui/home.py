from tkinter import *
from tkinter import ttk
from tkinter import tix 

import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ui.telaProduto import telaProduto
from ui.telaEstoque import telaEstoque
from ui.telaCliente import telaCliente
from ui.telaVenda import telaVenda

# cria a janela principal
root = tix.Tk()

class GradientFrame(Canvas):
    def __init__(self, parent, color1= "white", color2= "gray", **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)
    def _draw_gradient(self, event= None):
        self.delete("gradient")
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
            self.create_line(i, 0, i, height, tags=("gradient",), fill=color)
        self.lower("gradient")


class Aplication():

    def __init__(self):
        self.root = root
        self.tela()
        self.frame_principal()
        self.abasHome()
        self.abas.bind("<<NotebookTabChanged>>", self.on_tab_selected)
        root.mainloop()
    
    def tela(self):
        self.root.title("MyStock - Home")
        self.root.configure(background= '#4682B4')
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        self.root.maxsize(width= 900, height=700)
        self.root.minsize(width= 500, height= 400)
    
    def frame_principal(self):
        self.frame_1 = Frame(self.root, bd=4, 
                                        bg="whitesmoke", 
                                        highlightbackground="#708090", highlightthickness=2)
        self.frame_1.place(relx= 0.02,rely= 0.02, relwidth= 0.96, relheight= 0.95)


    def abasHome(self):

        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = GradientFrame(self.abas)
        self.aba2 = GradientFrame(self.abas)
        self.aba3 = GradientFrame(self.abas)
        self.aba4 = GradientFrame(self.abas)

        self.aba1.configure(background= "whitesmoke")
        self.aba2.configure(background= "whitesmoke")
        self.aba3.configure(background= "whitesmoke")
        self.aba4.configure(background= "whitesmoke")

        self.abas.add(self.aba1, text= "Produto")
        self.abas.add(self.aba2, text="Estoque")
        self.abas.add(self.aba3, text="Cliente")
        self.abas.add(self.aba4, text="Venda")

        self.abas.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)
        
        telaProduto(self.aba1)
        self.telaE = telaEstoque(self.aba2)
        telaCliente(self.aba3)
        self.telaV = telaVenda(self.aba4)
    
    def on_tab_selected(self, event): 
        selected_tab = event.widget.tab('current')['text'] 
        if selected_tab == 'Venda': 
            self.telaV.select_lista() # Atualiza a tabela de venda 
        elif selected_tab == 'Estoque': 
            self.telaE.select_lista() # Atualiza a tabela de estoque

Aplication()