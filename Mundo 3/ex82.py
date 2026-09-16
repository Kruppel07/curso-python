listapar = []
listaimpar = []
listatotal = []

while True:
    numero =int(input('Digite um número: '))

    listatotal.append(numero)

    if numero % 2 == 0:
        listapar.append(numero)
        print('Valor Adicionado!')
    elif numero % 2 != 0 :
        listaimpar.append(numero)
        print('Valor Adicionado')

    continuar = input("Quer continuar? [S/N] ").upper()
        
    if continuar == "N":
        break

listatotal.sort()
listaimpar.sort()
listapar.sort()

print(f'A lista completa é {listatotal}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')
        