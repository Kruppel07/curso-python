nome = input ('Digite seu nome completo? ')
print('Analisando seu nome...')

nomeM = nome.upper()
print(f'Seu nome em maiúsculo é {nomeM}')

nomem = nome.lower()
print(f'Seu nome em minúsculos é {nomem}')

nomeL = len(nome.replace(' ', ''))
print(f'Seu nome ao todo tem {nomeL} Letras')

nomeP = nome.split()[0]
letras = len(nomeP)
print(f'Seu primeiro nome é {nomeP} e tem {letras} Letras')
