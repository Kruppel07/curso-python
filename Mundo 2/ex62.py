num = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
contador = 0
termo = num

while contador < 10:
    print(termo, end=' -> ')
    termo += razao
    contador += 1

mais = int(input('\nQuantos termos a mais quer ver? '))
total = 10

while mais != 0:
    total += mais
    cont_extra = 0
    while cont_extra < mais:
        print(termo, end=' -> ')
        termo += razao
        cont_extra += 1
    mais = int(input('\nQuantos termos a mais quer ver? '))

print(f'Você viu {total} termos no total.')
    