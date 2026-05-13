# print("perfil de gamer - seja bem - vindo jogador")
# nome_jogador = input("qual é o nick do jogador: ? ")
# nível_jogador = input (" qual é o nível do jogador ")
# print(f" o jogador{nome_jogador} está no nível {nível_jogador} e pronto para a partida " )

# print("calculadora de mesada ")
# valor_semana = float(input("qual é seu valor que recebeu ?"))
# total_mes = valor_semana * 4
# print(f" sua mesada no final do mês será de...{total_mes}")

# manipulação de arquivos e texto
# manipular_texto = "  Python é Muito Legal!  "
# print(manipular_texto.strip().upper()) #PYTHON
# print(manipular_texto.strip().lower())#python
# print(manipular_texto.strip().startswith("A"))# "Começar com letra inicial "

# print(manipular_texto.strip().capitalize()) # letras inicial
# print(manipular_texto.strip().title())# título 
# print(manipular_texto.strip().replace(" "," ")) # preencher vazios 
# print(manipular_texto.strip().split()) # separar palavras 

# # exercício 1 
# frase = input(" digite a frase:")
# print( frase.strip().lower())

# manipular arquivos:
# escrevendo 
# with open ("notas.txt ","w",encoding="utf-8") as texto:
#     texto.write("estudar python hoje!")
#     texto.write("\nLer sobre Clean Code.")
#     texto.write("\n Estanos evoluindo.")

# #lendo 
# with open("notas.txt","r", encoding="utf=-8") as texto:
#     conteudo = texto.read()
#     print(conteudo)

# exemplo 1 
# crie um programa que leia o conteúdo de um arquivo de texto e conte quantas vezes a palavra "python" aparece no arquivo 
# exiba o resultado para o usuário

# print("contagem de palavras em arquivo")
# with open ("notas.txt","r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     contagem = conteudo.count("Python")
#     print(f"A contagem de palavras {contagem} é de...")



# print("contagem de palavras em arquivo")
# with open ("notas.txt","r", encoding="utf-8") as texto:
#     conteudo = texto.read()
#     contagem = conteudo.count("Python")
#     contagem = conteudo.upper().count("PYTHON") # contar a palavra "python"
#     contagem = conteudo.lower(). count("python")
#     print(f"A contagem de palavras {contagem} é de...")




