numero = int(input('Digite um número: '))

total = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        total += 1

if total == 2:
    print(f'{numero} é um número PRIMO!')
else:
    print(f'{numero} NÃO é um número primo!')