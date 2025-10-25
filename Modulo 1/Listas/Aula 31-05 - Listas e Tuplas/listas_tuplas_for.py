# Tupla
# Tuplas são listas IMUTÁVEIS (não altera)
import time

comidas = ('macarão', 'churrasco', 'sanduiche', 'hamburguer', 'pizza')


#print(comidas)

for i in comidas:
    print(i)

print()

# Laço For com range
# range (primeiro,último,saltos)
#teste: contador 1 até 10

'''
for contagem in range(10,-1,-1):
    print(contagem)
    time.sleep(1)

'''

# Listas 
# Listas podem ser manipuladas
# Criar listas com [ ]

nomes = ['Enzo', 'Henrique', 'Fernanda', 'Carlos']

for chamada in nomes:
    print(chamada)
    time.sleep(0.4)


nomes.append('Luiz') #append insere um novo objeto na lista
print()

for chamada in nomes:
    print(chamada)
    time.sleep(0.4)

print()

print(nomes[1]) # o primeiro endereço da lista é zero e assim sucessivamente

nomes.remove('Enzo') #remove um item específico da lista

print()

for chamada in nomes:
    print(chamada)
    time.sleep(0.4)


