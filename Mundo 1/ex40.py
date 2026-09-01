nota1 =float(input('Primeira nota: '))
nota2 =float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f'Tirando {nota1} e {nota2}, a média do aluno fica {media}')
    print(f'O aluno está APROVADO')
elif 5.0 <= media <= 6.9:
    print(f'Tirando {nota1} e {nota2}, a média do aluno fica {media}')
    print('O aluno fica de RECUPERAÇÃO')
else:
    print(f'Tirando {nota1} e {nota2}, a média do aluno fica {media}')
    print(f'O aluno está REPROVADO')