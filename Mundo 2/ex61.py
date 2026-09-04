num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 0
termo = num

while contador < 10:
     print(termo, end=' -> ')
     termo += razao
     contador += 1
print('FIM')