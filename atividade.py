import math
n1 =int(input('digite um numero: '))
n2 =int(input('digite um numero: '))
S = n1 + n2
Sub = n1 - n2
M = n1 * n2
D = n1 / n2
Di = n1 // n2
P = n1 ** n2
R = math.sqrt(n1)
print(f'a soma é {S}')
print(f'a subtração é {Sub}')
print(f'a multiplicação é {M}')
print(f'a divisão é {D}')
print(f'a divisão inteira é {Di}')
print(f'a potencia é {P}')
print(f'a raiz é {math.ceil(R)}')