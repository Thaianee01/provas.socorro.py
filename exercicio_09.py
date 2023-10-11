#Exercício 9: Faça um programa em Python que leia um número inteiro positivo e informe o número de dígitos que este número possui.Exemplos: 152 => 3 dígitos; 12453 => 5 dígitos; 34 => 2 dígitos

numero = int(input("digite um numero = "))

if numero > 0:
    digitos = 0

    while numero > 0:
        numero //= 10
        digitos += 1
        
    print (f'numero de digitos = {digitos}')