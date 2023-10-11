#Exercício 1: Faça um programa em Python que leia diversos números inteiros positivos quaisquer e ao final apresente o somatório e a média aritmética destes números. Quando terminar de entrar com todos os números, entre com o número zero.

somatorio = 0
quantidade = 0

while True:
    n1 = int(input("Digite um numero:"))
    
    somatorio += n1
    quantidade += 1
    media = somatorio / quantidade

    if n1 == 0:
        break

print (f'Somatório de todos os numeros: {somatorio:.2f}')
print (f'Média aritimética: {media:.2f}')