sexo = input('Digite seu sexo [M/F]: ').upper()

while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos. Digite novamente [M/F]: ').upper()

print(f'Sexo {sexo} registrado com sucesso!')