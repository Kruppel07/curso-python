num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = num

for i in range(1, 11):
    print(termo, end=' -> ')
    termo += razao

print('ACABOU')