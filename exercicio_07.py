#Exercício 7: Uma pesquisa sobre algumas características físicas da população coletou os seguintes dados referentes a cada habitante:
    #sexo ('M', 'F')
    #cor dos olhos ('azul', 'castanho', 'preto')
    #cor dos cabelos ('louro', 'castanho', 'preto')
#Faça um programa em Python que leia estes dados para cada habitante e informe, ao final, os percentuais, por sexo, por cor dos olhos e por cor dos cabelos. Antes de cada leitura o programa deve perguntar se (mais) um habitante deseja ser informado ('S' ou 'N').

habitantes = 0
mulheres = 0
homens = 0
olhos_azuis = 0
olhos_castanhos = 0
olhos_pretos = 0
cabelo_louro = 0
cabelo_castanho = 0
cabelo_preto = 0

while True:
    pergunta = input("Deseja informar os dados de um habitante? (S/N)")

    if pergunta == "S":
        nome = input ("Digite o seu nome:")
        sexo = input ("Digite o sexo: (F ou M)")
        olhos = input("Digite a cor dos olhos: (azul, castanho, preto)")
        cabelo = input("Digite a cor dos cabelos: (louro, castanho, preto)")
        
        habitantes += 1
        
        if sexo == "F":
            mulheres += 1
            
        elif sexo == "M":
            homens += 1
    
        if olhos == "azul":
            olhos_azuis +=1

        elif olhos == "castanho":
            olhos_castanhos += 1
    
        elif olhos == "preto":
            olhos_pretos +=1
        
        if cabelo == "louro":
            cabelo_louro += 1
        
        elif cabelo == "castanho":
            cabelo_castanho +=1
        
        elif cabelo == "preto":
            cabelo_preto +=1

    elif pergunta == "N":
        break

#porcentagem
percentual_homens = (homens / habitantes) * 100
percentual_mulheres = (mulheres / habitantes) * 100
percentual_olhos_azuis = (olhos_azuis/ habitantes) * 100
percentual_olhos_castanhos = (olhos_castanhos/ habitantes) * 100
percentual_olhos_pretos = (olhos_pretos / habitantes) * 100
percentual_cabelo_louro = (cabelo_louro/habitantes) * 100
percentual_cabelo_castanho = (cabelo_castanho/habitantes) * 100
percentual_cabelo_preto = (cabelo_preto/habitantes)* 100

print (f'O percentual de habitantes homens foi de: {percentual_homens:.2f}')
print (f'O percentual de habitantes mulheres foi de: {percentual_mulheres:.2f}')
print (f'O percentual de habitantes com olhos azuis foi de: {percentual_olhos_azuis:.2f}')
print (f'O percentual de habitantes com olhos castanhos foi de: {percentual_olhos_castanhos:.2f}')
print (f'O percentual de habitantes com olhos pretos foi de: {percentual_olhos_pretos:.2f}')
print (f'O percentual de habitantes com cabelo louro foi de: {percentual_cabelo_louro:.2f}')
print (f'O percentual de habitantes com cabelo castanho foi de: {percentual_cabelo_castanho:.2f}')
print (f'O percentual de habitantes com cabelo preto foi de: {percentual_cabelo_preto:.2f}')