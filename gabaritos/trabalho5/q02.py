altura = float(input("Digite a altura (em cm): "))
idade = int(input("Digite a idade: "))

if (altura > 180 and idade < 20):
    print("Candidato apto para a seleção juvenil")
else:
    print("Candidato fora do perfil para esta categoria")