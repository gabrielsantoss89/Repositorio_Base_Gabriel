# Aula passada
- Manipulação de arquivos
- Comandos de adição, manipulação e leitura de dados

# Aula de hoje
Manupulação de dados, Venv
Pandas
para instalar coisas no pyton pode ser pelo vs code ou pelo terminal
DF = dataframe
f' - format streaming
Camel Case
Boas praticas de programação
Construção de gráficos 
matplotlib
color.adobe.com
color-hex

# Comandos
 -python -m venv
 - %pip install pandas(pandas é extremamente importante para mecher com dados)
 -import pandas as pd
 -df = pd.read_csv('dados.csv') |essa é a variável do arquivo|
 -print(df.head()) | imprimir somente as linhas que eu quero e indicar as linhas com o número|
 -print(df.dtypes) | mostra os tipos de dados das colunas (object é texto e int64 é número)
 -faturamento = df['valor'].sum() | soma os numeros da planilha|
 -mediaVendas = df['valor'].median() |faz a média dos numeros|
 -vendasVendedor = df.groupby('vendedor')['valor'].sum() | agrupa antes de somar por vendedor|