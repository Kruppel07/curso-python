salario = float(input('Digite o salário do funcionário: '))

if salario > 1250:
    aumento = salario * 10 / 100
else:
    aumento = salario * 15 / 100

novo_salario = salario + aumento

print(f'O valor do aumento foi de R${aumento:.2f}')
print(f'O novo salário será de R${novo_salario:.2f}')