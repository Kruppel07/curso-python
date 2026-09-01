valorcasa =float(input('Qual o valor da casa: R$'))
salario =float(input('Qual o salário do comprador? R$'))
anos =int(input('Quanto tempo do financiamento? '))

meses = anos * 12
prestacao = valorcasa / meses
limite = salario * 0.30

if prestacao <= limite:
    print('Empréstimo CONCEDIDO')
    print(f'Para pagar a casa de {valorcasa:.0f}, a parcela será de R${prestacao:.2f}')
else:
    print('Emprestimo recusado')
    print(f'Para pagar a casa de {valorcasa:.0f}, a parcela será de R${prestacao:.2f}')