# Questão 8: Gincana Tecnológica (Divisão de Grupos)
chamada = int(input("Número da chamada (1 a 50): "))
resto = chamada % 10
grupo = resto + 1
print(f"Aluno{chamada}  GRUPO {grupo}.")