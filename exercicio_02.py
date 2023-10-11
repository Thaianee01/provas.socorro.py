#Exercício 2: Faça um programa em Python que leia diversos números inteiros quaisquer e ao final apresente o somatório e a média aritmética destes números. Antes da leitura de cada número o programa deve perguntar se deseja ler (mais) um número ('S' ou 'N'). Quando um 'N' for lido a leitura termina e as médias são exibidas

somatorio = 0
quantidade = 0

while True:
    pergunta = input("Deseja ler um numero? (S/N)")
    
    if pergunta == "S":
        n1 = int(input("Digite um numero:"))
        
        somatorio += n1
        quantidade += 1
        media = somatorio / quantidade
    
    if pergunta == "N":
        break

print (f'Somatório de todos os numeros: {somatorio:.2f}')
print (f'Média aritimética: {media:.2f}')