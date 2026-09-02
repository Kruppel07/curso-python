a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair')
    opcao = int(input('Opção: '))

    if opcao == 1:
        soma = a + b
        print(f'a soma de {a} + {b} é {soma}')
    elif opcao == 2:
        multi = a * b
        print(f'a multiplicação de {a} x {b} é {multi}')
    elif opcao == 3:
        if a > b :
            print(f'o número {a} é maior do que {b}')
        elif b > a:
            print(f'o número {b} é maior do que {a}')
        else:
            print(f'eles são IGUAIS')
    elif opcao == 4:
       a = float(input('Novo primeiro valor: '))
       b = float(input('Novo segundo valor: '))
    else:
        print('Até logo!')   

