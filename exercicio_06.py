#Exercício 6: Faça um programa em Python que leia, para cada aluno de uma turma, o seu nome e as notas das suas 3 provas, até que seja digitado o nome 'FIM'. O programa deve mostrar, para cada aluno, a sua média ponderada e uma mensagem "Aprovado", caso MP > = 5.75, e uma mensagem "Reprovado", caso contrário. A sua média ponderada é calculada como segue: MP = ( P1*1 + P2*2 + P3*3 ) / 6 Ao final, mostre a média geral da turma.

somatorio = 0
quantidade = 0

while True:
    nome = input("nome = ")
    
    if nome == "FIM":
        break

    n1 = float(input("digite a nota 1:"))
    n2 = float(input("digite a nota 2:"))
    n3 = float(input("digite a nota 3:"))

    media_ponderada = (n1*1 + n2 *2 + n3 *3) /6
    somatorio += media_ponderada
    quantidade += 1
    total = somatorio / quantidade

    if media_ponderada >= 5.75:
        print ("aluno: {}".format (nome))
        print ("Aprovado")
    
    else:
        print ("aluno: {}" .format (nome))
        print ("Reprovado")
    
print (f'media geral = {total:.2f}')