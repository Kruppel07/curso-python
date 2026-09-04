num =int(input('Digite um número: '))

while num >= 0:
    for i in range(1, 11):
       tabuada = num * i
       print(f'{num} x {i} = {tabuada}')
    num = int(input('Digite outro número: '))