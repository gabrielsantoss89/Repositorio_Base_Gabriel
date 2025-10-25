# AULA 10 - REVISÃO BANCO DE DADOS SQLITE E SQL

## CRUD

    Proposta é criar e testar um crud completo com código SQL utilizando o banco de dados SQLlite (nativo do python) sem servidor

### C - Create
    Criar novos registros no banco de dados 
    Exemplo: cadastro de um anúncio, post em redes sociais . . .
```SQL
    CREATE TABLE produtos("
    id INTEGER PRIMARY KEY AUTOINVREMENT,
    nome TEXT NOT NULL,
    quantidade INTEGER NOT NULL"
    );
INSERT INTO produtos('nome','quantidade') VALUES(?,?,?), ('Notebook',50);
```


### R - Read 
    Carregar/ler/consultar dados de um banco de dados
```SQL
SELECT * FROM produtos;
```


### U - Update

    Atualiza um dado já cadastrado no banco


### D - Delete
    Apaga um registro do banco de dados

