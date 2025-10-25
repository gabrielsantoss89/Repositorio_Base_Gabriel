# Passo 1 - Importar o SQLite
import sqlite3 # não precisa instalar
# Passo 2 - Criar o banco de dados
conexao = sqlite3.connect('cofre.db')
# Passo 3 - Criar um cursor (para executar comando SQL)

cursor = conexao.cursor()

# Passo 4 - Criar uma tabela dentro do banco de dados
cursor.execute('''
        CREATE TABLE IF NOT EXISTS segredo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        dono TEXT NOT NULL,
        valor DECIMAL NOT NULL
    );


  ''')

conexao.commit()
conexao.close()

print('tabela criada com sucesso')

# Passo 5 - Inserir dados dentro da tabela que está dentro do banco de dados
conexao = sqlite3.connect('cofre.db')
cursor = conexao.cursor()
#cursor.execute("INSERT INTO segredo('nome','dono','valor')VALUES(?,?,?);",('CARRO','Gabriel',500000))
# Passo 6 - Ler, consultar os dados cadastrados
ler = cursor.execute("select * from segredo;")

for dados in ler.fetchall():
    print(dados)

# Passo 7 - Atualizar um dado cadastrado
# Passo 8 - Apagar um dado registrado na tabela
