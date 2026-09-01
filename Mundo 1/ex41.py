nascimento =int(input('Ano do nascimento: '))
idade = 2026 - nascimento

if idade <= 9:
    print(f'O atleta tem {idade} anos')
    print(f'Classificação: MIRIM')
elif 10 <= idade <= 14:
     print(f'O atleta tem {idade} anos')
     print(f'Classificação: INFANTIL')
elif 15 <= idade  <= 19:
     print(f'O atleta tem {idade} anos')
     print(f'Classificação: JUNIOR')
elif 20 <= idade <= 25:
     print(f'O atleta tem {idade} anos')
     print(f'Classificação: SENIOR')
else:
     print(f'O atleta tem {idade} anos')
     print(f'Classificação: MASTER')