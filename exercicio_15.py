#Exercício 15: Uma lanchonete fast food apresenta a seguinte relação de produtos: código descrição preço: 

#hamburger 14,50
#cheeseburger 15,50
#cachorro quente 14,00
#sanduiche 13,50
#refrigerante 7,00
#suco de laranja 10,00
#milk shake 10,50
#sundae 15,00
#casquinha 8,00

#Cada cliente deve pedir um item de alimentação (1 a 4), uma bebida (5 ou 6) e uma sobremesa (7 a 9). Faça um programa em Python que leia, para um ou mais clientes, o código de alimentação, o código de bebida e o código de sobremesa, e informe a descrição e preço de cada item, e o preço final a pagar. A leitura encerra quando um código da alimentação for igual a zero.

while True:
    cliente = input("Digite o seu nome:")

    produtos = [
        ("Hamburguer", 14.50),
        ("Cheeseburguer", 15.50),
        ("Cachorro Quente", 14.00),
        ("Sanduíche", 13.50),
        ("Refrigerante", 7.00),
        ("Suco de Laranja", 10.00),
        ("Milk Shake", 10.50),
        ("Sundae", 15.00),
        ("Casquinha", 8.00)
    ]
    
    if cliente == '0':
        break

    alimento = int(input("Digite o código de alimentação (1-4):"))
    bebida = int(input("Digite o código de bebida (5-6):"))
    sobremesa = int(input("Digite o código de sobremesa (7-9):"))

    if (alimento < 1 or alimento > 4 or bebida < 5 or bebida > 6 or sobremesa < 7 or sobremesa > 9):
        print("Códigos inválidos. Tente novamente.")
        continue  # Volta ao início do loop para o próximo cliente

    preco_alimentacao = produtos[alimento - 1][1]
    preco_bebida = produtos[bebida- 1][1]
    preco_sobremesa = produtos[sobremesa - 1][1]

    preco_total = preco_alimentacao + preco_bebida + preco_sobremesa

    print(f"Cliente: {cliente}")
    print(f"Alimentação: {produtos[alimento - 1][0]} - R${preco_alimentacao:.2f}")
    print(f"Bebida: {produtos[bebida - 1][0]} - R${preco_bebida:.2f}")
    print(f"Sobremesa: {produtos[sobremesa - 1][0]} - R${preco_sobremesa:.2f}")
    print(f"Preço Total: R${preco_total:.2f}")