# Ryggz Lucca Santos Kruppel
# Matricula: XXXXXX
# Mini-Trabalho: Sistema de Analise Academica - Algoritmos e Estrutura de Dados
 
# ===== ENTRADA =====
print("===== ANALISE ACADEMICA =====")
nome = input("Nome do aluno: ")
matricula = input("Matricula: ")
disciplina = input("Disciplina: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
frequencia = float(input("Frequencia (%): "))
 
# ===== VALIDACAO =====
if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10 or frequencia < 0 or frequencia > 100:
    print("--------------------------------------")
    print("valor invalido!")
    print("As notas devem estar entre 0 e 10 e a frequencia entre 0 e 100.")
    print("--------------------------------------")
else:
    # ===== PROCESSAMENTO =====
    media = (nota1 + nota2 + nota3) / 3
 
    # Situacao (condicional aninhada)
    if media >= 7.0:
        if frequencia >= 75:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado por falta"
    else:
        if frequencia >= 75:
            situacao = "Reprovado por nota"
        else:
            situacao = "Reprovado por nota e falta"
 
    # Conceito (elif)
    if media >= 9.0:
        conceito = "A"
    elif media >= 7.0:
        conceito = "B"
    elif media >= 5.0:
        conceito = "C"
    else:
        conceito = "D"
 
    # Maior nota (if/elif, sem max())
    if nota1 >= nota2 and nota1 >= nota3:
        maior = nota1
    elif nota2 >= nota1 and nota2 >= nota3:
        maior = nota2
    else:
        maior = nota3
 
    # Menor nota (if/elif, sem min())
    if nota1 <= nota2 and nota1 <= nota3:
        menor = nota1
    elif nota2 <= nota1 and nota2 <= nota3:
        menor = nota2
    else:
        menor = nota3
 
    # ===== SAIDA =====
    print("--------------------------------------")
    print("RELATORIO DO ALUNO")
    print("--------------------------------------")
    print(f"Aluno......: {nome} ({matricula})")
    print(f"Disciplina.: {disciplina}")
    print(f"Media......: {media:.2f}")
    print(f"Frequencia.: {frequencia:.2f}%")
    print(f"Conceito...: {conceito}")
    print(f"Maior nota.: {maior}")
    print(f"Menor nota.: {menor}")
    print(f"Situacao...: {situacao}")
 
    # Quanto falta para passar
    if media < 7.0:
        faltam = 7.0 - media
        print(f"Faltaram {faltam:.2f} ponto(s) para atingir a media 7.0")
    else:
        print("Parabens! Voce atingiu a media necessaria.")
    print("--------------------------------------")
