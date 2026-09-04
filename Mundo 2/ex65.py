soma = 0
contador = 0
maior = 0
menor = 0

while True:
    numero = int(input('Digite um número: '))

    soma += numero
    contador += 1

    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

    continuar = input('Quer continuar? [S/N] ').upper()

    if continuar == 'N':
        break

media = soma / contador

print(f'A média dos valores foi {media:.2f}')
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')