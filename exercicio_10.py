#Exercício 10: Faça um programa em Python que leia um número inteiro positivo e informe se este número é primo ou não.
#12 => divisores: 1,2,3,4,6,12 (não é primo)
#11 => divisores: 1,11 (é primo)

primo = True 

numero = int(input("Digite um numero:"))

for i in range (2, numero):
    if numero % i == 0:
        primo = False
        break

if primo:
    print ("Esse numero é primo")

else: 
    print ("Esse numero não é primo")