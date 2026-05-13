# Funções são blocos de códigos reutilizáveis. o "f" n python, usado antes das aspas de uma string ( como f"texto {variável}), indica que se trata de uma f-string contém expressões entre chaves{} que devem ser avaliadas em tempo de execução e substituidas pelo seus valores reais
# def saudacao (jonas ):
#     return f"olá,{jonas}!"

# mensagem = saudacao ("jonas")
# print(mensagem)

# def age(idade):
#     return f"sua idade é, {idade}!"
# mensagem = age("16")
# print(mensagem)

# def boas_vindas ( nome, cargo):
#     print(f"Olá,{nome}! você é o novo {cargo}.")

# boas_vindas("Ana","Desenvolvedora")
# boas_vindas("Carlos", "guitarrista")
# boas_vindas(" Bruno", " baterista")


# # Conversões 
# nome = input("Seu nome:")
# idade = int(input("Sua idade: ")) # converte texto para inteiro
# print(f"{ nome }tem {idade} anos")

# Exercícios 
# Exercício 1 
# Criar um algoritmo que calcule suas notas e apresente o resultado final do semestre e do ano formativa e somativa 0 a 100 somativa 1 e a somativa 2/2 - calculo da média apesentar a média dos dois  semestres como resultado final 

# print(" calculo de notas - senai ")
# print("Somativas do primeiro semestre")
# nome = input(" Digite o nome do aluno \n ")
# nt1 = int(input(" digite a primeira somativa 1:\n "))
# nt2 = int(input(" digite a segunda somativa 2: \n "))
# nfinal = (nt1 + nt2) /2
# print ("As somativas do primeiro semestre são: \n", "do aluno", nome , round(nfinal,2))

# # Exercício 2 
# # Criar um algoritmo que calcule o dobro dos valores
# print("calculadora de valores em dobro")
# x = float(input(" Digite o valor que deseja dobrar \n"))
# print ("o valor so dobr ficou: \n , x2")

# Exercício 3 
# mercado senai criar um algoritmo para calcular uma compra realizada. na compra deve conter o nome do produto,o valor e a qauntidade comprada. 
# no final da compra deve ter o total e apresenta um relatório da sau compra realizada

# print(" dobrando o valor ")
# p1 =(input(" digite o nome do produto: \n"))
# p2 = float(input("digite o valor do produto: \n"))
# p3 = float (input("digite o número de unidades adaquiridas: \n "))
# pfinal= (p2*p3)

# print(" o total é de:",pfinal)


# Exercício 4 
# criar um algoritmo para calcular a compra de livros e peça para inserir uma porcenntagem de desconto sobre o produto comprado 
# O algoritmo deve perguntar o nome do livro, o valor, a quantidade e o valor de desconto que será aplicado. no final deve conter o valor total da compra com o desconto aplicado 

# print (" calculando o desconto ") 
# p1 = float (input ("insira o valor do produto:\n"))
# p2 = float (input("insira o valor do desconto: \n"))
# p3 = float (input("insira o número de unidades:\n"))
# pfinal = p1*p3
# pfinal2 = p1/p2
# pfinal3 = pfinal - pfinal2
# print (" o valor final é de:", pfinal)

