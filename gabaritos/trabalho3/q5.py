# Questão 5: Pedro Maratonista (Horas, Minutos e Segundos)
tempo_total = int(input("Tempo em segundos: "))
horas = tempo_total // 3600
minutos = (tempo_total % 3600) // 60
segundos = tempo_total % 60
print(f"{horas} horas, {minutos} minutos e {segundos} segundos")