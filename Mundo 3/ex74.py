from random import randint

numeros = (
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10)
)

print('Os números sorteados foram:', end=' ')

for numero in numeros:
    print(numero, end=' ')

print(f'\nO menor número foi {min(numeros)}')
print(f'O maior número foi {max(numeros)}')