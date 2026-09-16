valores = []
contador = 0

while True:
    numero = int(input("Digite um valor: "))
    contador += 1
    if numero not in valores:
        valores.append(numero)
        print("Valor adicionado!")
    else:
        print("Valor duplicado! Não vou adicionar.")

    continuar = input("Quer continuar? [S/N] ").upper()

    if continuar == "N":
        break

if 5 in valores:
    print("O valor 5 está na lista.")
else:
    print("O valor 5 não está na lista.")
    
valores.sort(reverse=True)

print(f'Você digitou {contador} valores')
print(f"Os valores únicos em ordem decrescente são: {valores}")