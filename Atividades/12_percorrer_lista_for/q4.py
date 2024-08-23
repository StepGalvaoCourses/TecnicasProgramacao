lista_idades = []

for i in range(10):
    idade = int(input("Digite a idade:"))
    lista_idades.append(idade)



#a)
maiores_idade = 0

for idade in lista_idades:
    if idade>=18:
        maiores_idade +=  1

print(maiores_idade)