from database.base import Base
from typing import List

class Estoque(Base):

    primary_keys = ('codigo',)

    def __init__(self, codigo: str, nome: str, quantidade: int, quantMax: int, quantMin: int):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.quantMax = quantMax
        self.quantMin = quantMin
    
    def strConnect(self):
        super().__init__()