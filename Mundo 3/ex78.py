valores = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1 }º valor: "))
    valores.append(numero)

maior = max(valores)
menor = min(valores)

print(f"O maior valor foi {maior}, na posição {valores.index(maior) + 1}.")
print(f"O menor valor foi {menor}, na posição {valores.index(menor) + 1}.")