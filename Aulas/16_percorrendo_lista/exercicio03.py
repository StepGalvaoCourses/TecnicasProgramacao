# Lista com 15 números inteiros
numeros = [12, 45, 67, 89, 23, 56, 78, 90, 34, 56, 78, 12, 34, 67, 89]

# Exibindo os números que estão nos índices pares
print("Números nos índices pares:")
for i in range(15):
    if i % 2 ==0:
        print(numeros[i])