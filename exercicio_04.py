#Exercício 4: Faça um programa em Python que leia diversos números inteiros e informe a média de números pares e ímpares lidos. Para terminar, entre com o número zero, que não deverá ser considerado no cálculo das médias. Exemplo de formatação: print("media pares = {0:.2f}".format(media)

soma_par = 0
par = 0
soma_impar = 0
impar = 0

while True:
    numero = int(input("Digite um numero:"))
    
    if numero == 0:
        break 

    if numero % 2 == 0:
        soma_par += numero
        par += 1
        media_par = soma_par / par

    else:
        soma_impar += numero
        impar += 1
        media_impar = soma_impar / impar

print (f'A media de numeros pares foi de: {media_par:.2f}')
print (f'A media de numeros impares foi de: {media_impar:.2f}')

