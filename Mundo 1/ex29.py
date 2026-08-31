velocidade =float(input('Qual velocidade atual do seu carro ? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'MULTADO!, você terá que pagar R${multa:.2f}')
else:
    print('Tudo certo!,dirija com segurança')
