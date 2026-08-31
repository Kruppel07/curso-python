altura =float(input('Altura da parede: '))
largura =float(input('Largura da parede: '))
area = altura * largura
tinta = area / 2
print(f'Sua parede tem a dimensão de {altura}x{largura} e sua area é de {area}m²')
print(f'para pintar essa parede, você precisará de {tinta}L de tinta')