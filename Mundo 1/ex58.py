from random import randint

computador = randint(0, 10)

palpite = int(input('Digite seu palpite: '))
tentativas = 1

while palpite != computador:

    if palpite < computador:
        print('Mais! Tente um número maior.')
    else:
        print('Menos! Tente um número menor.')

    palpite = int(input('Digite outro palpite: '))
    tentativas += 1

print('Parabéns! Você acertou!')
print(f'O computador pensou no número {computador}.')
print(f'Você precisou de {tentativas} palpites.')