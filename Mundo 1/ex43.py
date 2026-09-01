peso =float(input('Digite seu peso(KG): '))
altura =float(input('Digite sua altura(M): '))

imc = peso / (altura ** 2)
print(f'o IMC dessa pessoa é {imc:.2f}')

if imc < 18.5:
    print(f'Você está ABAIXO DO PESO')

elif 18.6 <= imc <= 25:
    print(f'Você está no PESO IDEAL')

elif 25.1 <= imc <= 30:
    print(f'Você está com SOBREPESO')

elif 30.1 <= imc <= 40: 
    print(f'Você está OBESO')

else:
    print(f'Você está com OBESIDADE MORBÍDA')
   