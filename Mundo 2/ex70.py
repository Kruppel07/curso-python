print('=-' * 20)
print('LOJÃO DO CAIQUE LUCAS TRIGUEIRO')
print('=-' * 20)

soma = 0
contador = 0
menor_preco = float('inf')
nome_barato = ''

while True:
    produto =input('Nome do produto: ')
    preço =float(input('Preço: R$'))
    soma += preço
    opção =input('Quer continuar? [S/N] ').upper()

    if opção == 'S':
        print('Adicione mais produtos:')

    if preço > 1000:
        contador += 1

    if preço < menor_preco:
        menor_preco = preço
        nome_barato = produto

    if opção == 'N':
        print('=-' * 20)
        print('FIM DO PROGRAMA')
        print('=-' * 20)
        break   
    

print(F'O total da compra foi R${soma}')
print(f'Temos {contador} produtos custando mais de R$1000.0 ')
print(f'O produto mais barato foi {nome_barato} que custa R${menor_preco}')