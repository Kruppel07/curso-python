numero = int(input('Digite um número: '))

fatorial = 1
cont = numero

while cont > 0:
    fatorial = fatorial * cont
    cont = cont - 1

print(f'O fatorial de {numero} é {fatorial}')