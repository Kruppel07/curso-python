frase =input('Digite uma frase ? ')

frase.strip()

count = frase.upper().count('A')
print(f'a letra A aparece {count} vezes')

searchF =  frase.strip().lower().find('a')
print(f'A letra A aparece pela primeira vez na posição {searchF + 1}')

searchL = frase.strip().lower().rfind('a')
print(f'A letra A aparece pela ultima vez na posição {searchL + 1}')