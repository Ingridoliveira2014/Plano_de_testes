import pytest
import sqlite3
from business.produto import Produto
from business.estoque import Estoque
from business.venda import Venda

# Testes de Unidade para o módulo de produto

@pytest.mark.addProduto
def test_insercaoProduto():
    produto = Produto("P020", "Apagador", 20, "Apagador preto")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir
    row = produto.buscaCodigo("P020")
    assert len(row) == 1

@pytest.mark.editProduto
def test_atualizacaoProduto():
    produto = Produto("P0021", "Calculadora", 50, "Calculadora cientifica")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir
    produto.nome = "Calculadora cientifica"
    produto.valor = 60
    produto.descricao = "Calculadora cientifica casio"
    produto.salvar(acao=2)  # Atualizar
    row = produto.buscaCodigo("P0021")
    assert len(row) == 1
    assert row[0].nome == "Calculadora cientifica"
    assert row[0].valor == 60
    assert row[0].descricao == "Calculadora cientifica casio"

@pytest.mark.deleteProduto
def test_exclusaoProduto():
    produto = Produto("P0015", "Caneta", 15.50, "Caneta azul")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir
    produto.salvar(acao=3)  # Excluir
    row = produto.buscaCodigo("P0015")
    assert len(row) == 0

# Testes de Unidade para o módulo de estoque

@pytest.mark.addEstoque
def test_insercaoEstoque():
    produto = Produto("P0022", "Lapis", 3.50, "Lapis preto")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir

    estoque = Estoque("P0022", "Lapis", 10, 20, 5)
    estoque.strConnect()
    estoque.salvar(acao=1)  # Inserir
    row = estoque.buscaCodigo("P0022")
    assert len(row) == 1

@pytest.mark.editEstoque
def test_atualizacaoEstoque():
    produto = Produto("P0023", "Caderno", 10, "Caderno universitario")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir

    estoque = Estoque("P0023", "Caderno", 10, 20, 5)
    estoque.strConnect()
    estoque.salvar(acao=1)  # Inserir

    estoque.quantidade = 15
    estoque.quantMax = 10
    estoque.quantMin = 25
    estoque.salvar(acao=2)  # Atualizar
    
    row = estoque.buscaCodigo("P0023")
    assert len(row) == 1
    assert row[0].quantidade == 15
    assert row[0].quantMax == 10
    assert row[0].quantMin == 25

@pytest.mark.deleteEstoque
def test_exclusaoEstoque():
    produto = Produto("P0024", "Borracha", 5.50, "Borracha preta")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir

    estoque = Estoque("P0024", "Borracha", 10, 20, 5)
    estoque.strConnect()
    estoque.salvar(acao=1)  # Inserir

    estoque.salvar(acao=3)  # Excluir
    row = estoque.buscaCodigo("P0024")
    assert len(row) == 0

# Testes de Unidade para o módulo de venda

@pytest.mark.editVendaEstoque    
def test_atualizaVendaEstoque():
    produto = Produto("P0025", "Borracha", 5.50, "borracha preta")
    produto.strConnect()
    produto.salvar(acao=1)  # Inserir

    estoque = Estoque("P0025", "Borracha", 10, 20, 5)
    estoque.strConnect()
    estoque.salvar(acao=1)  # Inserir

    venda = Venda("P0025", "12345678901", 5, '2024-11-20', 5.50)
    venda.strConnect()
    venda.salvar(acao=1)  # Inserir

    row = estoque.buscaCodigo("P0025")
    estoque = row[0]
    assert len(row) == 1
    assert row[0].quantidade == 5

# Testes de integridade 

#retorna a string conexão com o banco de dados
@pytest.fixture
def conexao_banco():
    connection = sqlite3.connect("MyStockDb.sqlite")
    return connection

# Testa a conexão com o banco de dados
@pytest.mark.conexaoBanco
def test_conexao_banco(conexao_banco):
    try:
        cursor = conexao_banco.cursor()
        cursor.execute("SELECT 1") # teste básico para validar conexão
        assert True
    except Exception as e:
        pytest.fail(f"Erro de conexão: {e}")
    finally:
        conexao_banco.close()

# Testes de desempenho

# Consulta ao banco de dados
def consulta_banco(conexao_banco):
    cursor = conexao_banco.cursor()
    cursor.execute("SELECT * FROM Produto")
    _ = cursor.fetchall()

# Testa o desempenho da consulta ao banco de dados
@pytest.mark.desempConsulta
def test_benchmark_consulta(benchmark, conexao_banco):
    benchmark(consulta_banco, conexao_banco)

