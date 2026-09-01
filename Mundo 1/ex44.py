compras =float(input('Preço das compras: R$'))
opcao = int(input('''FORMAS DE PAGAMENTO:
[1] - à vista dinheiro/cheque
[2] - à vista cartão
[3] - 2x no cartão
[4] - 3x ou mais no cartão
Opção: '''))

if opcao == 1:
    total = compras - (compras * 10 / 100)
    print(f'Valor com desconto: R$ {total:.2f}')

elif opcao == 2:
    total = compras - (compras * 5 / 100)
    print(f'Valor com desconto: R$ {total:.2f}')

elif opcao == 3:
    total = compras
    parcela = total / 2
    print(f'Valor total: R$ {total:.2f}')
    print(f'2 parcelas de R$ {parcela:.2f}')

elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = compras + (compras * 20 / 100)
    parcela = total / parcelas

    print(f'Valor total com juros: R$ {total:.2f}')
    print(f'{parcelas} parcelas de R$ {parcela:.2f}')

else:
    print('Opção inválida!')