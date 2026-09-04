soma = 0
contador = 0
num = int(input('Digite um número [999 para parar]: '))

while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número [999 para parar]: '))

print(f'Você usou {contador} número e a soma deles é {soma}')    