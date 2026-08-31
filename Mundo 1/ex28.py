from random import randint

computador = randint(0, 5)
jogador = int(input('Digite um número entre 0 e 5: '))

if jogador == computador:
    print('Você venceu!')
else:
    print(f'Você perdeu!, eu pensei no numero {computador}')