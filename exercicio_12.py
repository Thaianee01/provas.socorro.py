#Exercício 12: Faça um programa em Python que leia as alturas (em metros) de 2 pessoas A e B, onde altura de A > altura de B, e as suas respectivas taxas de crescimento anuais (em centímetros), onde taxa de B > taxa de A. O algoritmo deve informar quantos anos a pessoa B levará para alcançar ou ultrapassar a altura da pessoa A.

A = float(input("digite sua altura em metros:")) #metros
B = float(input("Digite sua altura em metros:"))

taxa_a = int(input("Digite a taxa de crescimento de A:")) #cm/ano
taxa_b = int(input("Digite a taxa de crescimento de B:"))

if A > B and taxa_a < taxa_b:
    taxa_total = (taxa_b - taxa_a)/100
    diferença_altura = (A - B)/ 100

    anos = diferença_altura / taxa_total 
    
    print(f'Levará {anos:.2f} anos para B alcançar ou ultrapassar a altura de A.')

else:
    print("As condições não estão corretas para calcular o tempo necessário.")