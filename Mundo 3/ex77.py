palavras = (
    'aprender',
    'programar',
    'python',
    'computador',
    'curso'
)

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais:', end=' ')

    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')