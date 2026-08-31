dias =int(input('Quanto dias alugado? '))
km =float(input('Quantos km rodados? '))
x1 = dias * 60
x2 = km * 0.15
x3 = x1 + x2
print(f'O total a pagar é R${x3:.2f}')