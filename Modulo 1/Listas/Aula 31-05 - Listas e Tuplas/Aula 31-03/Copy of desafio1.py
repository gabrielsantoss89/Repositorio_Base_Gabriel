#criar um aplicativo que permite a entrada na balada apenas para maiores de 18 anos
print('Entrada apenas para maiores de 18 anos')


nome = input('qual o seu nome?')
idade = int('qual a sua idade? ')

if idade <=12:
    print(f'Cade seus pais {nome}??volte para sua casa')
elif idade <=17:
    print(f'volte para casa {nome}, voce não tem idade para entrar na festa')
else:
    print(f'voce pode entrar na festa {nome}, aproveite!!')