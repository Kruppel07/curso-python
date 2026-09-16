valores = []

while True:
    numero = int(input("Digite um valor: "))

    if numero not in valores:
        valores.append(numero)
        print("Valor adicionado!")
    else:
        print("Valor duplicado! Não vou adicionar.")

    continuar = input("Quer continuar? [S/N] ").upper()

    if continuar == "N":
        break

valores.sort()

print(f"Os valores únicos em ordem crescente são: {valores}")