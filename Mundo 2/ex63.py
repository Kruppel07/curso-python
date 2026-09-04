num =int(input('Quantos termos você quer mostrar? '))
a = 0
b = 1
contador = 0

while contador < num:
    print(a, end=' -> ')
    proximo = a + b
    a = b
    b = proximo
    contador += 1