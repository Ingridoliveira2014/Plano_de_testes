from abc import ABC, abstractmethod

class IBase(ABC):

    @abstractmethod
    def salvar(self, acao: int):
        pass

    @abstractmethod
    def todos (self) -> list:
        pass

    @abstractmethod
    def busca(self, id_buscar: str) -> list:
        pass