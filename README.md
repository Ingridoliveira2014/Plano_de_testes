# Plano de Teste

**MyStock**

*versão 1.0*

## Histórico das alterações

   Data    | Versão |    Descrição   | Autor(a)
-----------|--------|----------------|-----------------
16/03/2025 |  1.0   | Release incial | Ingrid Oliveira
23/03/2025 |  1.0   | Release final  | Thiago Lima

## Integrantes da Equipe
Adilson Gonzaga, Ingrid Oliveira, Talita Munis e Thiago de Lima Chagas.

## 1 - Introdução

### 1.1. Objetivo do Documento
Este documento descreve o plano de testes do sistema MyStock, especificando os requisitos a serem testados, os tipos de testes definidos, os recursos necessários e o cronograma de execução. Ele serve como uma referência para acompanhar a evolução dos testes e garantir a qualidade do software.

### 1.2. Visão Geral do Projeto
O MyStock é um sistema de gerenciamento de estoque e vendas desenvolvido em Python. Suas principais funcionalidades incluem o cadastro de produtos, controle de estoque, registro de clientes e acompanhamento de vendas. Para assegurar seu funcionamento correto e confiável, serão realizados diversos testes automatizados utilizando pytest, abrangendo testes funcionais, unitários e de integração.

Com este documento, buscamos:

- Identificar os componentes do sistema que serão testados.
- Definir e descrever as estratégias de teste adotadas.
- Listar os requisitos que serão verificados durante os testes.
- Identificar os recursos necessários para a execução dos testes.
- Registrar os resultados obtidos ao longo do processo de teste.
- Este plano de testes permitirá um acompanhamento eficiente da qualidade do sistema MyStock, garantindo que ele atenda aos requisitos definidos e ofereça uma experiência confiável aos usuários.

## 2 - Requisitos a Testar

Esta seção apresenta os requisitos funcionais e não funcionais do sistema MyStock que serão verificados ao longo do processo de testes. Os testes serão baseados nos requisitos do sistema, garantindo que suas funcionalidades operem conforme esperado. Sempre que novos requisitos forem identificados, esta seção será atualizada para manter a organização e clareza do plano de testes.

### Casos de uso:

Identificador do caso de uso | Nome do caso de uso
-----------------------------|------------------------------------
id UC1                       |  Cadastro de Produto
id UC2                       |  Edição de Produto
id UC3                       |  Exclusão de Produto
id UC4                       |  Cadastro de Produto no Estoque
id UC5                       |  Edição de Produto no Estoque
id UC6                       |  Exclusão de Produto no Estoque
                 

### Requisitos não-funcionais:

Identificador do requisito   | Nome do requisito
-----------------------------|---------------------------------------------------------------
id req1                      |      Implementação em Python
id req2                      |      Interface simples e intuitiva
id req3                      |      Código comentado para fácil manutenção e extensibilidade
id req4                      |      Conexão estável com banco de dados
id req5                      |      Desempenho razoável ao realizar uma consulta no 


## 3 - Tipos de teste

Esta seção descreve os principais tipos de testes que serão aplicados ao sistema MyStock para garantir seu funcionamento correto e atender aos requisitos definidos.

### 3.1. Testes Funcionais
Esses testes validarão se as principais funcionalidades do sistema operam corretamente, incluindo:

Cadastro de produtos, clientes e vendas
Gerenciamento de estoque
Registro e consulta de vendas

### 3.2. Testes de Unidade
Serão realizados testes automatizados com pytest para verificar o correto funcionamento de funções individuais do sistema.

### 3.3. Testes de Integração
Avaliarão a comunicação entre os módulos do sistema, garantindo que o fluxo de dados entre cadastro de produtos, estoque e vendas funcione corretamente.

### 3.4. Testes de Desempenho
Serão executados testes básicos para medir o tempo de resposta das principais operações do sistema, garantindo eficiência nas transações.

## 4 - Recursos
Esta seção descreve os recursos necessários para a execução dos testes do sistema MyStock, incluindo ambiente de teste (hardware e software) e ferramentas utilizadas no processo.

### 4.1 - Ambiente de Teste - Software e Hardware
Os testes do sistema MyStock serão executados em um ambiente com a seguinte configuração:

Hardware:
- Processador: Intel Core i5 ou superior
- Memória RAM: 8GB ou superior
- Armazenamento: SSD com pelo menos 50GB livres
- Software:
- Sistema Operacional: Windows 10 ou superior
- Editor de Código: Visual Studio Code
-- Linguagem de Programação: Python 3.10 ou superior
- Gerenciador de Pacotes: pip
- Bibliotecas utilizadas: pytest, sqlite3 

### 4.2 - Ferramenta de Teste
Os testes do MyStock serão conduzidos utilizando a seguinte ferramenta:

- pytest: Framework para execução de testes automatizados em Python, permitindo a validação de funcionalidades e integração entre módulos.
