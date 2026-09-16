valores = []

for i in range(5):
    numero = int(input("Digite um valor: "))

    if i == 0 or numero > valores[-1]:
        valores.append(numero)
        print("Adicionado ao final da lista.")
    else:
        pos = 0

        while pos < len(valores) and numero > valores[pos]:
            pos += 1

        valores.insert(pos, numero)
        print(f"Adicionado na posição {pos}.")

print(f"Os valores em ordem são: {valores}")