#Exercício 3: Faça um programa em Python que leia diversos números inteiros positivos quaisquer e ao final informe qual o maior número lido. Quando terminar de entrar com todos os números, entre com o número zero.

numero = 0
maior_numero = 0

while True:
    numero = int(input("digite um numero:"))
    
    if numero > maior_numero:
        maior_numero = numero
    
    if numero == 0:
        break

print (f'O maior valor lido foi: {maior_numero:.2f}')