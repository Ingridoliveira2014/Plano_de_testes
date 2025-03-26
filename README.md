# Plano de Teste

**MyStock**

_versão 1.0_

## Histórico das alterações

| Data       | Versão | Descrição      | Autor(a)        |
| ---------- | ------ | -------------- | --------------- |
| 16/03/2025 | 1.0    | Release incial | Ingrid Oliveira |
| 23/03/2025 | 1.0    | Release final  | Thiago Lima     |

## Integrantes da Equipe

Adilson Gonzaga, Ingrid Oliveira, Talita Munis e Thiago de Lima Chagas.

## 1 - Introdução

### 1.1. Objetivo do Documento

Este documento descreve o plano de testes do sistema MyStock, especificando os requisitos a serem testados, os tipos de testes definidos, os recursos necessários e o cronograma de execução. Ele serve como uma referência para acompanhar a evolução dos testes e garantir a qualidade do software.

link repositório original: [https://github.com/ThiagoLimaC/microProjeto-python-MyStock.git]

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

| Identificador do caso de uso | Nome do caso de uso            |
| ---------------------------- | ------------------------------ |
| id UC1                       | Cadastro de Produto            |
| id UC2                       | Edição de Produto              |
| id UC3                       | Exclusão de Produto            |
| id UC4                       | Cadastro de Produto no Estoque |
| id UC5                       | Edição de Produto no Estoque   |
| id UC6                       | Exclusão de Produto no Estoque |

### Requisitos não-funcionais:

| Identificador do requisito | Nome do requisito                                        |
| -------------------------- | -------------------------------------------------------- |
| id req1                    | Implementação em Python                                  |
| id req2                    | Interface simples e intuitiva                            |
| id req3                    | Código comentado para fácil manutenção e extensibilidade |
| id req4                    | Conexão estável com banco de dados                       |
| id req5                    | Desempenho razoável ao realizar uma consulta no          |

## 3 - Tipos de teste

Esta seção descreve os principais tipos de testes que serão aplicados ao sistema MyStock para garantir seu funcionamento correto e atender aos requisitos definidos.

### 3.1. Testes Funcionais

Esses testes validarão se as principais funcionalidades do sistema operam corretamente, incluindo:

Cadastro de produtos, clientes e vendas
Gerenciamento de estoque
Registro e consulta de vendas

_test_sistema_completo_

Objetivo do Teste: Validar o funcionamento completo do sistema de vendas, incluindo a integração entre a interface do usuário, a manipulação de estoque, o cadastro de vendas e a atualização das informações exibidas na tela.

Cenários de Teste:

Cadastro de nova venda:
-Preencher os campos de código do produto, CPF do cliente, quantidade, data da venda e valor total.
-Verificar se o sistema valida corretamente a quantidade disponível no estoque.
-Garantir que a venda seja registrada corretamente e que o estoque seja atualizado.

Alteração de venda existente:
-Alterar informações de uma venda previamente cadastrada.
-Verificar se as alterações refletem corretamente na interface do usuário e no banco de dados.

Exclusão de venda:
-Excluir uma venda existente e verificar se o sistema remove corretamente os dados do banco.

Busca de venda:
-Buscar vendas por nome do produto ou nome do cliente.
-Verificar se o sistema retorna as vendas corretas.

Interface e usabilidade:

-Garantir que os dados sejam exibidos corretamente na tabela de vendas.
-Verificar a interação do usuário com os campos e botões.

Resultados Esperados:

O sistema deve permitir o cadastro de uma venda, realizar as devidas validações e atualizar o estoque.
A alteração de vendas deve refletir corretamente no banco de dados e na interface do usuário.
A exclusão de vendas deve ser realizada corretamente.
A busca de vendas deve retornar resultados corretos.
A interface deve ser responsiva e refletir as mudanças no banco de dados de forma precisa.

Erros Encontrados:

Validação de Campos no Cadastro de Venda:

Erro: O sistema não está validando adequadamente os campos obrigatórios como código do produto, CPF do cliente, quantidade e data da venda.

Verificação de Estoque:

Erro: A validação do estoque não está funcionando corretamente, permitindo que o usuário registre vendas de produtos com quantidade insuficiente em estoque.

Atualização de Estoque Após Venda:

Erro: A atualização do estoque após a venda não está sendo realizada corretamente. Embora o código tente atualizar a quantidade do produto no estoque, a mudança não reflete corretamente no banco de dados.

Alteração de Vendas:

Erro: Ao tentar alterar uma venda, o sistema não reflete corretamente a atualização nos dados armazenados. As alterações feitas na interface não são corretamente salvas no banco de dados.

Exibição de Dados na Interface:

Erro: Alguns dados, como o valor total da venda, não são exibidos corretamente na interface após o cadastro ou alteração de uma venda.

Resumo do Resultado: Os erros encontrados justificam o fracasso do teste de sistema completo, pois afetam diretamente a integridade dos dados e a interação entre os componentes do sistema. A falta de validação de campos essenciais, a falha na atualização do estoque e a exibição incorreta de dados comprometem o funcionamento do sistema de vendas como um todo.

### 3.2. Testes de Unidade

Serão realizados testes automatizados com pytest para verificar o correto funcionamento de funções individuais do sistema.

_test_insercaoProduto_

Objetivo do teste: Verificar se a inserção de um novo produto no banco de dados ocorre corretamente e se o produto é encontrado na busca pelo código.

Resultado Esperado: Após a execução do teste, o produto deve ser inserido no banco de dados e, ao realizar a busca com o código " ", deve-se encontrar exatamente um registro.

Resultado Real: O teste verificou a inserção de um produto e sua presença no banco de dados após a operação. O comportamento foi conforme o esperado, ou seja, o produto foi corretamente registrado e localizado.

_test_atualizacaoProduto_

Objetivo do Teste: Testar a atualização de um produto no sistema, garantindo que as informações do produto sejam alteradas corretamente no banco de dados após a execução da operação de atualização.

Resultado Esperado: A Entrada Inicial: Produto com código "P0021", nome "Calculadora", valor 50 e descrição "Calculadora científica" deve ser atualizada para: Nome: "Calculadora científica”; “Valor: 60”; “Descrição: Calculadora científica Casio"

Resultado Real: O teste verificou a atualização do produto, e os dados no banco de dados foram modificados corretamente, conforme esperado.

_test_exclusaoProduto_

Objetivo do teste: Verificar se a exclusão de um produto da base de dados ocorre corretamente, garantindo que o produto não possa ser encontrado após a exclusão.

Resultado esperado: Após excluir o produto com código " ", o banco de dados não deve retornar nenhum registro relacionado a esse código.

Resultado real: O teste passou com sucesso, indicando que o produto foi excluído corretamente.

_test_insercaoEstoque_

Objetivo do Teste: Testar a inserção de um produto e seu respectivo estoque no sistema, garantindo que ambos sejam registrados corretamente no banco de dados.

Resultado Esperado:

Exemplo:

Entrada Inicial: Produto "P0022" (Lápis, R$3,50, "Lápis preto").
Ação: Inserção do produto e estoque com os seguintes dados:
Produto: Código "P0022", Nome "Lápis", Valor R$3,50, Descrição "Lápis preto".
Estoque: Código "P0022", Nome "Lápis", Quantidade 10, Mínima 20, Máxima 5.
Resultado: O banco de dados deve registrar o estoque do produto "P0022" com as quantidades definidas.

Resultado Real: O teste verificou a inserção de um novo produto e do estoque associado no banco de dados. Ambos foram registrados corretamente.

_test_atualizacaoEstoque_

Objetivo do teste: Verificar se a atualização do estoque de um produto no banco de dados está funcionando corretamente.

Resultado esperado: O sistema deve ser capaz de atualizar a quantidade, quantidade máxima e mínima do estoque de um produto. O código do produto deve ser identificado corretamente e os dados do estoque devem refletir as mudanças.

Resultado real: O estoque foi atualizado com sucesso no banco de dados. As informações do produto e do estoque foram corretamente salvas e alteradas conforme esperado.

_test_exclusaoEstoque_

Objetivo do Teste: Verificar se o processo de exclusão de um item de estoque está funcionando corretamente, garantindo que o produto seja removido da base de dados após a execução da ação de exclusão.

Resultado Esperado: O produto deve ser excluído do estoque; o banco de dados não deve retornar o produto " " após a exclusão; a busca pelo código " " deve retornar um resultado vazio (sem registros).

Resultado Real: O teste confirmou que a exclusão do item de estoque foi realizada corretamente. A busca retornou um resultado vazio, o que indica que o item foi removido com sucesso da base de dados.

_test_atualizavendaEstoque_

Objetivo do Teste: Verificar a atualização correta da quantidade de estoque após uma venda, garantindo que a quantidade do produto no estoque seja reduzida corretamente.

Resultado Esperado:

Exemplo:  
O estoque de "Borracha" (código "P0025") deve ser atualizado corretamente, e a quantidade no estoque após a venda deve ser 5 (10 - 5 = 5).

Resultado Real: A quantidade no estoque foi 10, o que não corresponde ao esperado (deveria ser 5).

Resumo do Resultado: O teste falhou, pois a quantidade no estoque não foi atualizada corretamente após a venda. A quantidade continuou como 10 em vez de ser reduzida para 5.

Erros:

1. Atualização do Estoque Após a Venda:

Problema: O método add_item() faz uma verificação de quantidade de estoque antes de realizar a venda, mas o código que atualiza o estoque após a venda (pAtualizado = prod e pAtualizado.salvar(2)) pode estar falhando ao não atualizar corretamente os objetos de estoque.

2. Verificação de Quantidade Insuficiente no Estoque

Problema: O método estoque_baixo() não verifica corretamente se a quantidade de estoque disponível é suficiente para realizar a venda. O valor de quantidade_entry não é verificado quanto à sua natureza numérica antes de realizar a operação de subtração.

3. Uso de prodBusca

Problema: A variável prodBusca parece ser uma lista de produtos retornada por e.buscaCodigo(codigoP), mas não está claro se o método realmente retorna uma lista com objetos corretamente populados.

4. Manipulação de messagebox

Problema: Ao ocorrer uma condição de erro, o método messagebox.showinfo() é usado para exibir uma mensagem informativa. No entanto, a mensagem pode não ser exibida corretamente antes da continuação da execução do código.

5. Problemas Potenciais com o Layout da UI

Problema: Pode haver problemas na interação entre a interface do usuário e os dados, fazendo com que os campos de entrada não sejam atualizados corretamente.

### 3.3. Testes de Integração

Avaliarão a comunicação entre os módulos do sistema, garantindo que o fluxo de dados entre cadastro de produtos, estoque e vendas funcione corretamente.

_test_conexao_banco_

Objetivo do Teste: Validar se a conexão com o banco de dados é realizada corretamente.

Resultado Esperado: A conexão deve ser estabelecida com sucesso, sem erros ou falhas.

Resultado Real: O teste de conexão com o banco de dados passou sem problemas.

### 3.4. Testes de Desempenho

Serão executados testes básicos para medir o tempo de resposta das principais operações do sistema, garantindo eficiência nas transações.

_test_benchmark_consulta_

Objetivo do teste: Avaliar o desempenho da consulta no banco de dados, medindo o tempo de execução e a consistência do comportamento ao longo das execuções.

Resultado esperado: O tempo de execução da consulta deve ser estável, sem grandes variações entre as execuções. A média de tempo deve ser relativamente baixa, com poucas variações (outliers) e sem impactos no desempenho.

Resultado real:O teste de benchmark para a consulta no banco de dados foi executado com sucesso. Embora a média de tempo de execução seja aceitável, a presença de alguns outliers (valores atípicos) pode indicar que, em algumas execuções, o tempo foi significativamente maior do que o esperado.

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
