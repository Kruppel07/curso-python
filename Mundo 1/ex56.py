
soma_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
mulheres_menores_20 = 0

for i in range(1, 5):
    nome = input(f'Nome da {i}ª pessoa: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').upper()

    soma_idade += idade

    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome

    if sexo == 'F':
        if idade < 20:
            mulheres_menores_20 += 1

media = soma_idade / 4

print(f'A média de idade do grupo é {media:.1f} anos.')
print(f'O homem mais velho é {nome_homem_mais_velho}.')
print(f'Ao todo são {mulheres_menores_20} mulheres com menos de 20 anos.')
