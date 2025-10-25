import time

print('\nSISTEMA DE PAGAMENTO DE COMISSÃO PARA VENDEDORES\n')

#Input vai receber o nome do vendedor e guardar
#essa informação na variável "vendedor"
#nao é bom colocar acentuação em nome de variaveis
#é importante programar com boas práticas para não recusarem o projeto
#o F vai fazer o texto pegar as informações das variaveis
#\n para colocar na linha de baixo
#digitar python, colocar a primeira letra do arquivo e apertar tab para por o nome completo dele
#a ordem dos códigos é importante pos ele é lido de cima para baixo
#a conta só vai ser calculada se a condição for verdadeira
#time.sleep serve para dar um intervalo de tempo antes de mostrar o próximo código

vendedor = input('Nome do vendedor: ')
meta = 5000
comissao = 0.03
faturamentoVendedor = float(input('Faturamento de Maio: '))

print('\nCalculando Comissão do vendedor ......')
time.sleep(4)


if faturamentoVendedor >= meta:

    valorComissão = faturamentoVendedor * comissao
    print('\nResultado Final!!')
    print(f'\nVendedor: {vendedor}\nFaturamento: R${faturamentoVendedor}\nPagar Comissão: R${valorComissão}\n')

else:
    print(f'\n{vendedor},não atingiu a meta.\nFavor se esforce mais em Junho')
time.sleep(1)
print('\nObrigado por usar o nosso aplicativo.\nBy Projeto Fábrica de Programadores')
