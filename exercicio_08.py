#Exercício 8: Faça um programa em Python que leia, no máximo, 10 números inteiros positivos quaisquer e ao final apresente o somatório e a média aritmética destes números. Se desejar terminar antes da leitura dos 10 números, entre com o número zero. Caso nenhum número seja somado, não apresente a soma e a média.

somatorio = 0
quantidade = 0

for i in range (10):
    numero = int(input("Digite um numero:"))
    
    if numero == 0:
        break

    elif numero > 0:
        somatorio += numero
        quantidade += 1
        media = somatorio / quantidade
    
print (f'O somatório dos termos é = {somatorio:.2f}')
print (f'A média aritimetica é de = {media:.2f}')