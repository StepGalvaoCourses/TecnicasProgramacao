# Questão 4: Temperatura
c = float(input("Temperatura em Celsius: "))
f = (c * 1.8) + 32
k = (f - 32) / 1.8 + 273.15
print(f"Celsius {c}")
print(f"Fahrenheit = {f}")
print(f"Kelvin = {k}")
