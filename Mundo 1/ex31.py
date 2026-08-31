distancia = float(input('Qual a distância da viagem? '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'O preço da passagem será R${preco:.2f}')