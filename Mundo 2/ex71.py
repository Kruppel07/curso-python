print('=-' * 20)
print('BANCO KAELISON')
print('=-' * 20)

valor = int(input('Valor do saque: R$ '))

cedulas50 = valor // 50
valor %= 50

cedulas20 = valor // 20
valor %= 20

cedulas10 = valor // 10
valor %= 10

cedulas1 = valor // 1
valor %= 1

print(f'Total de cédulas de R$50: {cedulas50}')
print(f'Total de cédulas de R$20: {cedulas20}')
print(f'Total de cédulas de R$10: {cedulas10}')
print(f'Total de cédulas de R$1: {cedulas1}')