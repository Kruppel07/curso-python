soma = 0
contador = 0

while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    contador += 1

print(f'Você usou {contador} número e a soma deles é {soma}')