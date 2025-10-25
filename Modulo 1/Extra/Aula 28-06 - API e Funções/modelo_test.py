import time
from dolar import yahoo


# cotação do dia 14/06
cotacao = yahoo()
print('\n                Conversor de Moeda\n')
print('\nPainel:')
print(f'          Dólar Americano Comercial: R$ {cotacao} reais\n')

print('''\n Selecione as opções:
       
               1 - PARA COMPRAR DÓLARES
               2 - PARA COMPRAR REAIS 
               0 - PARA SAIR 
      
      ''')

# perguntar pro usuário o que ele quer

while True:
    try:
        opcao = int(input('Digite a opção desejada: '))
        if opcao == 1:

            valorReal = float(input('Quantos reais será convertido para Dólar: '))
            realDolar = round(valorReal / cotacao,2)
            print('\ncalculando...\n')
            time.sleep(2)
            print(f'Com {valorReal} reais vou comprar {realDolar} dólares\n')

        elif opcao == 2:

            valorDolar = float(input('Quantos dólares serão convertidos para reais: '))
            dolarReal = round(valorDolar * cotacao,2)
            print('\ncalculando...\n')
            time.sleep(1.5)
            print(f'Com {valorDolar} dólares vou comprar {dolarReal} reais\n')

        elif opcao == 0:
            print('\nObrigado por usar nosso sistema\n')
            break

        else:
            print('''\n Selecione as opções:
        
                1 - PARA COMPRAR DÓLARES
                2 - PARA COMPRAR REAIS 
                0 - PARA SAIR 
        
        ''')
    except ValueError:
        print('''\n Selecione as opções:
        
                1 - PARA COMPRAR DÓLARES
                2 - PARA COMPRAR REAIS 
                0 - PARA SAIR 
        
        ''')
