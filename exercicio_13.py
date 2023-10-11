#Exercício 13: Faça um programa em Python que calcule a seguinte série numérica, dado o valor de N: S(N) = 1 + 1 / 2 + 1 / 3 + . . . + 1 / N

numero = int(input("Digite o valor de inicio da serie:"))
soma = 0.0

for i in range(1, numero + 1):
    termo = 1.0 / i  # Calcula o termo atual da série
    soma += termo  # Soma o termo à soma total

print(f"S({numero}) = {soma:.2f}")