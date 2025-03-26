import sqlite3

def enable_foreign_keys(conn): 
    cursor = conn.cursor() 
    cursor.execute("PRAGMA foreign_keys = ON") 
    cursor.close()

connection = sqlite3.connect("MyStockDb.sqlite")
cursor = connection.cursor()

query1 = '''
CREATE TABLE IF NOT EXISTS Produto (
    codigo VARCHAR(7) PRIMARY KEY,
    nome TEXT NOT NULL,
    valor REAL NOT NULL,
    descricao TEXT
)
'''
query2 = '''
CREATE TABLE IF NOT EXISTS Estoque (
    codigo VARCHAR(7) PRIMARY KEY,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    quantMax INTEGER NOT NULL,
    quantMin INTEGER NOT NULL, 
    FOREIGN KEY (codigo) REFERENCES Produto (codigo),
    FOREIGN KEY (nome) REFERENCES Produto (nome)
)
'''

query3 = '''
CREATE TABLE IF NOT EXISTS Cliente (
    cpf VARCHAR(11) PRIMARY KEY,
    nome TEXT NOT NULL,
    telefone VARCHAR(14) NOT NULL,
    endereco TEXT
)
'''

query4 = '''
CREATE TABLE IF NOT EXISTS Venda (
    idVenda INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo VARCHAR(7) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    quantidade INT NOT NULL,
    dataVenda DATE NOT NULL,
    valor REAL NOT NULL,
    FOREIGN KEY (codigo) REFERENCES Produto(codigo),
    FOREIGN KEY (cpf) REFERENCES Cliente(cpf)
)
'''

query5 = '''
INSERT INTO Produto (codigo, nome, valor, descricao) VALUES
('P001', 'Notebook Dell', 3500.00, 'Notebook Dell Inspiron 15 3000'),
('P002', 'Smartphone Samsung', 2200.00, 'Samsung Galaxy S20'),
('P003', 'Monitor LG', 1200.00, 'Monitor LG UltraWide 29'),
('P004', 'Teclado Mecânico', 450.00, 'Teclado Mecânico Corsair K95'),
('P005', 'Mouse Logitech', 300.00, 'Mouse Logitech MX Master 3'),
('P006', 'Impressora HP', 800.00, 'Impressora HP LaserJet Pro M15w'),
('P007', 'Headset HyperX', 550.00, 'Headset HyperX Cloud Alpha'),
('P008', 'Webcam Logitech', 350.00, 'Webcam Logitech C920 HD'),
('P009', 'Cadeira Gamer', 950.00, 'Cadeira Gamer DXRacer'),
('P010', 'HD Externo Seagate', 450.00, 'HD Externo Seagate 2TB');
'''

query6 = '''
INSERT INTO Cliente (cpf, nome, telefone, endereco) VALUES
('12345678901', 'Ana Silva', '11987654321', 'Rua A, 123, São Paulo, SP'),
('23456789012', 'Bruno Sousa', '21987654321', 'Av. B, 456, Rio de Janeiro, RJ'),
('34567890123', 'Carla Dias', '31987654321', 'R. C, 789, Belo Horizonte, MG'),
('45678901234', 'Daniel Lima', '51987654321', 'Travessa D, 101, Porto Alegre, RS'),
('56789012345', 'Elisa Costa', '41987654321', 'Rua E, 112, Curitiba, PR'),
('67890123456', 'Felipe Almeida', '71987654321', 'Alameda F, 123, Salvador, BA'),
('78901234567', 'Gabriela Torres', '81987654321', 'Rua G, 456, Fortaleza, CE'),
('89012345678', 'Hugo Rocha', '92987654321', 'Estrada H, 789, Manaus, AM'),
('90123456789', 'Isabela Mendes', '61987654321', 'Av. I, 1010, Brasília, DF'),
('01234567890', 'Júlio Neves', '22987654321', 'Rua J, 1122, Recife, PE');

'''

query7 = '''
INSERT INTO Estoque (codigo, nome, quantidade, quantMax, quantMin) VALUES
('P001', 'Notebook Dell', 50, 100, 10),
('P002', 'Smartphone Samsung', 30, 80, 5),
('P003', 'Monitor LG', 70, 150, 15),
('P004', 'Teclado Mecânico', 60, 120, 10),
('P005', 'Mouse Logitech', 90, 200, 20),
('P006', 'Impressora HP', 40, 100, 10),
('P007', 'Headset HyperX', 80, 160, 15),
('P008', 'Webcam Logitech', 100, 250, 25),
('P009', 'Cadeira Gamer', 20, 60, 5),
('P010', 'HD Externo Seagate', 55, 130, 10);
'''

query8 = '''
INSERT INTO Venda (codigo, cpf, quantidade, dataVenda, valor) VALUES
('P001', '12345678901', 1, '2024-11-20', 3500.00),  -- Notebook Dell, 1 unidade, valor total = 1 * 3500.00
('P002', '23456789012', 2, '2024-11-21', 4400.00),  -- Smartphone Samsung, 2 unidades, valor total = 2 * 2200.00
('P003', '34567890123', 1, '2024-11-22', 1200.00),  -- Monitor LG, 1 unidade, valor total = 1 * 1200.00
('P004', '45678901234', 3, '2024-11-23', 1350.00),  -- Teclado Mecânico, 3 unidades, valor total = 3 * 450.00
('P005', '56789012345', 1, '2024-11-24', 300.00),   -- Mouse Logitech, 1 unidade, valor total = 1 * 300.00
('P006', '67890123456', 1, '2024-11-25', 800.00),   -- Impressora HP, 1 unidade, valor total = 1 * 800.00
('P007', '78901234567', 2, '2024-11-26', 1100.00),  -- Headset HyperX, 2 unidades, valor total = 2 * 550.00
('P008', '89012345678', 1, '2024-11-27', 350.00),   -- Webcam Logitech, 1 unidade, valor total = 1 * 350.00
('P009', '90123456789', 1, '2024-11-28', 950.00),   -- Cadeira Gamer, 1 unidade, valor total = 1 * 950.00
('P010', '01234567890', 2, '2024-11-29', 900.00);   -- HD Externo Seagate, 2 unidades, valor total = 2 * 450.00
'''

query9 = '''

'''

cursor.execute(query8)
enable_foreign_keys(connection)
connection.commit()
connection.close()
