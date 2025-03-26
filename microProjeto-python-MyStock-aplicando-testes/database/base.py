import sqlite3
from typing import List, Any
from database.ibase import IBase

class Base(IBase):

    primary_keys = ('codigo',)

    # definindo o método que contém a string de conexão
    def __init__(self):
        self.connection_string = "MyStockDb.sqlite"

    # definindo o método salvar para Adicionar, Editar ou Remover um item da tabela
    def salvar(self, acao : int):

        with sqlite3.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            colunas = []
            valores = []

            # _dict_ -> mapeia todos os atributos de instância do objeto atual
            # _items() -> fornece um par de chaves atributo e valor
            # o loop percorre cada par atributo/valor do objeto atual e adiciona na lista valores
            for attr, value in self.__dict__.items():
                if value != "MyStockDb.sqlite" and attr != "strConnect":
                    valores.append(f"'{value}'")
                    colunas.append(f"{attr}")

            # Filtro de ação desejada do CRUD
            # self._class_._name_ -> retorna o nome da Classe para ser inserido como nome da tabela no banco
            # join -> concatena os valores da lista separando-os por vírgulas
            if acao == 1:
                query = f"INSERT INTO {self.__class__.__name__} ({','.join(colunas)}) VALUES ({','.join(valores)})"
            elif acao == 2:
                col_val_str = ', '.join([f"{coluna}={valor}" for coluna, valor in zip(colunas, valores)])
                primary_key_conditions = ' AND '.join([f"{key}='{getattr(self, key)}'" for key in self.primary_keys])
                query = f"UPDATE {self.__class__.__name__} SET {col_val_str} WHERE {primary_key_conditions}"
            elif acao == 3:
                primary_key_conditions = ' AND '.join([f"{key}='{getattr(self, key)}'" for key in self.primary_keys])
                query = f"DELETE FROM {self.__class__.__name__} WHERE {primary_key_conditions}"
            
            cursor.execute(query)
            connection.commit()
            
    # definindo o método que retorna todos os items de uma classe
    def todos(self) -> List[IBase]:
        lista = []
        with sqlite3.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.__class__.__name__}"
            cursor.execute(query)
            # retorna todas as linhas da tabela e armazena na variável rows
            rows = cursor.fetchall()

            colunas = [description[0] for description in cursor.description]

            for row in rows:
                data = dict(zip(colunas, row))
                obj = self.__class__.__new__(self.__class__)
                obj.__dict__.update(data)
                lista.append(obj)
            return lista
        
    def busca(self, nome: str) -> List[IBase]:
        lista = []
        with sqlite3.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.__class__.__name__} WHERE nome LIKE '%{nome}' ORDER BY nome ASC"
            cursor.execute(query)
            rows = cursor.fetchall()

            colunas = [description[0] for description in cursor.description]

            for row in rows:
                data = dict(zip(colunas, row))
                obj = self.__class__.__new__(self.__class__)
                obj.__dict__.update(data)
                lista.append(obj)
            return lista
        
    def buscaCodigo(self, codigo: str) -> List[IBase]:
        lista = []
        with sqlite3.connect(self.connection_string) as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.__class__.__name__} WHERE codigo = '{codigo}'"
            cursor.execute(query)
            rows = cursor.fetchall()

            colunas = [description[0] for description in cursor.description]

            for row in rows:
                data = dict(zip(colunas, row))
                obj = self.__class__.__new__(self.__class__)
                obj.__dict__.update(data)
                lista.append(obj)
            return lista
    

