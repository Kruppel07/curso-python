import math
co =float(input('comprimento do cateto oposto: '))
ca =float(input('comprimento do cateto adjacente: '))
h1 = math.pow(co, 2) + math.pow(ca, 2) 
h2 = math.sqrt(h1)
print(f'A hipotenusa é igual a {h2:.2f}')