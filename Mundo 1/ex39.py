ano_nascimento = int(input('Digite o ano de nascimento: '))

idade = 2026 - ano_nascimento

if idade < 18:
    falta = 18 - idade
    print(f'Você tem {idade} anos.')
    print(f'Ainda falta(m) {falta} ano(s) para o alistamento.')

elif idade == 18:
    print(f'Você tem {idade} anos.')
    print('Está na hora de se alistar!')

else:
    passou = idade - 18
    print(f'Você tem {idade} anos.')
    print(f'Você já passou {passou} ano(s) do prazo de alistamento.')