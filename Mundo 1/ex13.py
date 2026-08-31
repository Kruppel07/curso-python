salario = (float(input('Qual o valor do salario?R$ ')))
aumento = salario + (salario * 15 / 100)
print(f'o salario que custava R${salario}, com o aumento de 15% vai ficar R${aumento:.2f}')