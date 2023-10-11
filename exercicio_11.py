#Exercício 11: Faça um programa em Python que leia 2 números inteiros positivos (dividendo e divisor), onde dividendo > divisor, e determine o quociente através de uma sequência de subtrações.

dividendo = int(input("Digite o dividendo (número maior): "))
divisor = int(input("Digite o divisor (número menor): "))

if dividendo <= 0 or divisor <= 0 or dividendo <= divisor:
    print("Por favor, insira valores no qual o dividendo é maior que o divisor.")
    
else:
    quociente = 0
    subtracoes = 0

    while dividendo >= divisor:
        dividendo -= divisor
        subtracoes += 1

    print(f"O quociente da divisão é: {subtracoes}")