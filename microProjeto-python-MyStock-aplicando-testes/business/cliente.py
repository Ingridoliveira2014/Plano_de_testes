from database.base import Base
from typing import List
from datetime import date

class Cliente(Base):

    primary_keys = ('cpf',)

    def __init__(self, cpf: str, nome: str, telefone: str, endereco: str):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
    
    def strConnect(self):
        super().__init__()