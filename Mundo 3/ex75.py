a =int(input('Digite um número: '))
b =int(input('Digite outro número: '))
c =int(input('Digite mais um número: '))
d =int(input('Digite o último número: '))

tupla = (a , b , c , d)
print(f'Você digitou os valores {tupla}')

print(f'O número 9 apareceu {tupla.count(9)} vezes.')

if 3 in tupla:
    print(f'O primeiro número 3 apareceu na posição {tupla.index(3) + 1}.')
else:
    print('O número 3 não foi digitado.')

print('Os números pares:', end=' ')
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end=' ')

print('\nOs números ímpares:', end=' ')
for numero in tupla:
    if numero % 2 != 0:
        print(numero, end=' ')