from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('''SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)

print('-=' * 15)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 15)

if jogador == computador:
    print('EMPATE!')

elif jogador == 0 and computador == 2:
    print('JOGADOR VENCE!')

elif jogador == 1 and computador == 0:
    print('JOGADOR VENCE!')

elif jogador == 2 and computador == 1:
    print('JOGADOR VENCE!')

elif jogador in [0, 1, 2]:
    print('COMPUTADOR VENCE!')

else:
    print('JOGADA INVÁLIDA!')