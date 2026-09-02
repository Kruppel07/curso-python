frase = input('Digite uma frase: ')

frase = frase.replace(' ', '').upper()

if frase == frase[::-1]:
    print('A frase é um PALÍNDROMO!')
else:
    print('A frase NÃO é um palíndromo!')