num =int(input('Digite um número inteiro '))
opcao = int(input('''Escolha a base de conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal
Opção: '''))

if opcao == 1:
    print(f'A forma binária do {num} é {bin(num)[2:]}')
elif opcao == 2:
    print(f'A forma octal do {num} é {oct(num)[2:]}')
elif opcao == 3:
    print(f'A forma hexadecimal do {num} é {hex(num)[2:]}')
else:
    print('OPÇÃO INVÁLIDA')