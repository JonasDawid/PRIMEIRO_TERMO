# tratamento de erros e depuração 
# try e except são usados para lidar com erros de forma controlada,
#  evitando que o progrma quebre . o código dentro do bloco try é executado normalmente,
# mas se ocorrer um erro, o controle é passado para o bloco except onde podemos lidar com
# a situação de froma propriada 

# try :
#     numero = int(input("digite um número: "))
#     resultado=10 / numero
#     print ("O resultado é:", resultado)

# except ValueError:
#     print("Erro: Você deve digitar um número válido")

# except ZeroDivisionError:
#     print("Erro: nã é possível dividir por zero.")

# except KeyboardInterrupt:
#     print("\n programa corrompido")

# except TypeError:
#     print("Erro: tipo de dado inválido.")

# except Exception as erro:
#     print("Erro inesperado", erro)

#     # exercício 1 
#     # ecreva um programa que solicite ao usuário calcule a média de três números
#     # o programa deve lidar com possíveis erros, com a entrada de valores não numéricos 
#     # ou a divisão por zero.

#     num1 = float(input(" digite o primeiro valor: "))
#     num2 = float(input("digite o segundo valor:"))
#     num3 = float(input("digite o terceiro valor:"))

#     media =(num1 + num2 +num3)/3
#     print(f"A média é:{media}")
# except ValueError :
#     print(" Erro: você deve digitar um número válido ")


#     #  Explicação def: a palvra-chave "def" é usada para definir uma função em python
# uma função é um bloco de código reutilizável que realza uma tarefa específica 
# em python uma função é u, bloco de código reutilizavel que realiza uma tarefa especifica um valor para 
# o local onde a função foi chamada o valor retornado pode ser usado posteriormente no código

# # def nome_da_função(parametro1, parametro, 2)
# corpo da função ( código que será executado )
# resultado = parametro1 + parametro2
# return resultado



# # exemplo 1 
# def saudacao(nome):
#     return f"olá, {nome}!"
# print(saudacao("jonas"))

# # exemplo 2 

# def calcularr_media(num1, num2, num3):
#     try:
#         media = (num1 + num2 + num3 ) /3
#         return media
#     except TypeError:
#         return "Erro: todos os valores devem ser números."
    






#     # exemplo 3 
#     def valores():
#         print(" digite três valores:")
#     a = int(input("digite o primeiro valor:"))
#     b = int(input(" digite o segundo valor:"))
#     c = int(input("digite o terceiro valor:"))
#     return a,b,c 
# print (f" o  maior valor é : {max(valores)}")

# # exemplo 4 
# def calcular_dobro():
#     try:
#         valor_digitado = int(input(" digite o valor que deseja :"))