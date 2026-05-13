# Exercício 1
# criar um algoritmo para realizar a locação de filmes séries seguir o modelo anterior.Ao escolher a opção você  deverá perguntar o nome do cliente do filme ou série e quantidade que deseja assim como o valor de aluguel
# Para filmes R$ 5,00 e para séries R$ 10,00


# print("Menu de Opção")
# print("Escolha uma das opções")
# print (" Filmes F séries S e X para sair")

# escolha = input("insira seu nome:")
# escolha = input("Digite uma opção ")


# if escolha == "F":
#         print("Você escolheu Filmes")
#         filmes = input(" qual filme deseja ?")
#         quantidade = int(input("qual quantidade deseja ?"))
#         valor = 5
#         total = quantidade*valor
#         print (input("o valor é de ",total))

# elif escolha == "S" :
#         print (" você escolheu Séries ")
        
# else:
#         print("Você saiu do programa")


# exercício 2 
# loja de comida de doces 
# criar um algoritmo para compra de produto
# 1-comida
#2- bebida 
# 3- doces 
# ao escolher as opções cada um terá um valor d eporcentagem, comida= 10%, bebida = 5%, doces = 2% 
# calcular pocentagem valor/ 100 ou valor * valor / 100

# exercicio 3 
# calculadora com operadores 
# sua calculadora deverá perguntar qual operador ele deseja e calcular os valores desejados.
# operador + -/ *

#  #exercico 2 
# print ("bem vindo a loja ")
# print ("temos comida bebida e doces")
# print ("digite o que você tem interesse")
# print ("pressione 1 para comida ")
# print (" pressione 2 para bebidas")
# print ("pressione 3 para doces ")

# opcao = int(input("digite sua opção"))
# if  opcao == 1:
#     print(" você está em comida ")
#     print("temos PF, la carte")
#     comida = input(" o que deseja ?")
#     valor = float (input(" digite o valor da comida "))
#     desconto = valor * 10/100
#     total = valor - desconto
#     print(" sua compra total foi de: ", total)

# if opcao == 2:
#     print (" você está em bebidas ")
#     print (" temos refrigerantes e sucos")
#     bebida = input(" o que deseja ?")
#     valor = float (input("digite o valor da bebida "))
#     desconto = valor * 5/100
#     total = valor - desconto
#     print (" sua compra total foi de:", total)

# if opcao == 3:
#     print (" você está em doces ")
#     print (" temos chocolates,balas e muito mais  ")
#     doce = input(" o que deseja ?")
#     valor = float (input("digite o que deseja"))
#     desconto = valor * 2/100
#     total = valor - desconto 
#     print (" sua compra é de:",total)

# else:
#     print (" obrigado e bom apetite")

# exercicio 3 
# print(" bem vindo a calculadora com opeadores")
# print (" digite 1 para adição ")
# print (" digite 2 para subtração ")
# print ( " digite 3 para multiplicação")
# print (" digite 4 para multiplicação ")

# print (input(" qual sua operador deseja calcula ?"))
# opcao = int(input("qual valor operador deseja calcular "))
# if  opcao == 1:
#     print(" você está em adição ")
#     valor = float (input(" digite o valor  "))
#     valor2 = float ( input(" digite o outro valor"))
#     total = valor + valor2
#     print(" seu valor é de : ", total)

#     if  opcao == 2:
#      print(" você está em subtração ")
#     valor = float (input(" digite o valor  "))
#     valor2 = float ( input(" digite o outro valor"))
#     total = valor - valor2
#     print(" seu valor é de : ", total)

#     if  opcao == 3:
#      print(" você está em multipicação ")
#     valor = float (input(" digite o valor  "))
#     valor2 = float ( input(" digite o outro valor"))
#     total = valor * valor2
#     print(" seu valor é de : ", total)

#     if  opcao == 4:
#      print(" você está em multiplicação ")
#     valor = float (input(" digite o valor  "))
#     valor2 = float ( input(" digite o outro valor"))
#     total = valor/valor2
#     print(" seu valor é de : ", total)

# else:
#   print("bons estudos,foi um prazer  ajudar")

  # exercicio 4 
  # calculo de notas 
  # nossas atividades são por base de calculo em somativa 1 e somativa 2 no final temos uma média 
  # acima ou igual a 50 o aluno será aprovado caso contrario reprovado 
  # o programa devera perguntar o nome e as notas e apresentar o resultado final do aluno 

print(" calculo de notas - senai ")
print("Somativas do primeiro semestre")
nome = input(" Digite o nome do aluno \n ")
nt1 = int(input(" digite a primeira somativa 1:\n "))
nt2 = int(input(" digite a segunda somativa 2: \n "))
nfinal = (nt1 + nt2) /2
print ("As somativas do primeiro semestre são: \n", "do aluno", nome , round(nfinal,2))
if nfinal > 50:
  print("aprovado")

if nfinal< 50:
  print ("reprovado")

else:
  ("foi um prazer ajudar")
  
print(" calculo de notas senai")
