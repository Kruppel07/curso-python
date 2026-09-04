from random import randint
print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 20)

jogador =int(input('Digite um valor: '))

parimpar =input('PAR OU ÍMPAR [P/I]: ').upper()

while parimpar != 'P' and parimpar != 'I':
    parimpar =input('Dado inválido.PAR OU ÍMPAR [P/I]: ').upper()

computador = randint(0, 10)
contador = 0

while True:
    computador = randint(0, 10)
    soma = jogador + computador
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total deu {soma}')
    if (soma % 2 == 0 and parimpar == 'P') or (soma % 2 != 0 and parimpar == 'I'):
        print('VOCÊ VENCEU')
        print('Vamos jogar novamente...')
        jogador = int(input('Digite um valor: '))
        parimpar = input('PAR OU ÍMPAR [P/I]: ').upper()
        contador += 1
    else:
        print('Você PERDEU')
        break
    

print(F'GAME OVER! Você venceu {contador} vezes.')