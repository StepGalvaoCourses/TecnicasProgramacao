# Questão 9: Caixa Eletrônico (Menor quantidade de notas)
valor = int(input("Valor do saque: "))

# Notas de 100
qtd100 = valor // 100
valor = valor % 100

# Notas de 50
qtd50 = valor // 50
valor = valor % 50

# Notas de 20
qtd20 = valor // 20
valor = valor % 20

# Notas de 10
qtd10 = valor // 10
valor = valor % 10

# Notas de 5
qtd5 = valor // 5
valor = valor % 5

# Notas de 2
qtd2 = valor // 2
valor = valor % 2

# Notas de 1 (O que sobrar é nota de 1)
qtd1 = valor

print(f"{qtd100} nota(s) de R$ 100")
print(f"{qtd50} nota(s) de R$ 50")
print(f"{qtd20} nota(s) de R$ 20")
print(f"{qtd10} nota(s) de R$ 10")
print(f"{qtd5} nota(s) de R$ 5")
print(f"{qtd2} nota(s) de R$ 2")
print(f"{qtd1} nota(s) de R$ 1")