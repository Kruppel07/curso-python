preço = (float(input('Qual o valor do produto? ')))
desconto = preço - (preço * 5 / 100)
print(f'o produto que custava R${preço}, na promoção com desconto de 5% vai custar R${desconto:.2f}')