# Revisão de conteúdo 
# print = função de sída de dados para o console
# input = função de entrada de dados do usuário via teclado 
# if = estrutura de decisão para  executar o código condicionalmente
# elif = combinação de else + if para verificar múltiplas condições 
# else = parte opcional dee um if que executa código quando a condição do if é falsa 
# for = laço de repetição para interar sobre uma sequencia de elementos 
# while = laço de reeptição para executar código enquanto uma condição for verdadeira 
# operadores matemáticos: *, -, *, /, //, %,**
# operadores de compáração:==, !=, >, <, >=, <=
# print (variável)

# Exemplo 1: com print e ipunt 
# nome = input ("digite seu nome:")
# print(f"Olá,{nome}! Bem-Vindo á aula de python para de densevolvimento de sistemas ")
# Exemplo 2:com if, elif e else 
# nota = float (input("digite a nota do aluno:"))
# if nota >= 7:
#     print("aluno aprovado!")
# elif nota >= 5:
#     print("Aluno em recuperação.")
# else:
#     print (" Aluno repovado.")

# Exemplo 3: com for 
# materiais = ["metal","plástico","vidro"]
# for material in materiais:
#     print(f"processando material: {material}.")
#     print(f"material {material} processado com sucesso!")
#     print (" fim do processamento de materiais")

# # 2. O laço while ( repetições indeterminadas )
# use o while quando você não sabe quando vai parar. ele depende de uma condição 
# ( como um sensor de segurança ou botão de emergência )
# exemplo: monitor de temperatura (loop infinito controlado)
# repete enquanto a temperatura estiver segura 

# import time 
# temperatura = 25
# while temperatura < 40:
#     print(f"temperatura atual: {temperatura}°C. Sistema operando...")
#     time.sleep (1)
#     temperatura+= 3 # simulando o aquecimento da máquina 
#     print(" Alerta! temperatura atingiu o limite.Desligando o motor...")

#     # lista de temperaturas lidas pelo sensor por minuto 
#     leituras = [70, 75, 82, 98, 110, 85, 80]
#     for temp in leituras:
#         while temp > 100:
#             print(f"CRÍTICO: {temp}°C detectado! acionando parada de emergencia.")
#             break # O loop para aqui e Não lê o os próximos valores (85 e 80)
#         print(f"temperatura está em {temp}°C. Operação normal.")
#         print("sistema desligado.aguardando a manutenção.")

#         # produção de peças com controle de material usnado continue 
#         materiais = ["metal","metal","plastico","metal", "vidro","metal"]
#         for peca in materiais:
#             if peca != "metal":
#                 print(f"aviso: peça de {peca} detectada.desviando para descarte...")
#                 continue #pula o restante do código abaixo e vai para a próxima peça
#             # este código só roda se a peça for de metal 
#             print(f" processando peça de {peca}. furando polindo...")
#             print(" fim do lote de produção ")

# # exercício 1 
# tente criar um código que conte de 1 a 10, mas use o continue para não 
# imprimir o número 5 ( simulando uma falha de sensor especifica no item 5)
# for sensor in range (1,11):
#     if sensor == 5:
#         print (f"sensor nº{sensor}com falha")
#         print (f"Sensor {sensor}sem falha ")
#         continue 
#     print("Fim! :)")

#exercício 2
# simule um semáforo com parada de cada cor. determine um tempo que deseja para que quando mudar para tal  cor ele represente uma pausa para cada cor
# use o continue para pular a cor amarela (simulando um semáforo com defeito que não acende a luz amarela)

# cores = ["verde","amarelo","vermelho"]

# for cor in cores:
#     if cor == "amarelo":
#         print(f"o sinal está com {cor} defeito")
#         print(f" o sinal está em funcionamento {cor}")

# exercicio 3 

# total_cosumo =0
# for maq in range (1,6)
# consumo = float(input(f"digite o valor que deseja da {maq}nº"))
# total_consumo += consumo
# print(f"o consumo total da fabrica é de {total_consumo} kW/h")

# exercício 4 

# pecas = [ 50.1,49.8,52.0,50.0,48.5]
# for medida in pecas:
#     if medida >= 50.0:
#         print(f"peça com medida {medida}mm: provada")
#     else:
#         print(f"peça com medida {medida}mm:rejeitada ")
#         print("fim da avaliação de peças.")


# exercício 5
sacos_dl =0
for saco in range (1,7):
    peso = float(input(f"digite o peso do saco (i) (kg) :"))

    if 48<= peso <= 52:
        print(" dentro do limite ( 48 a 52 kg).")
        dentro_do_limite+= 1
    else:
        print("fora do limite(48 a 52 kg).")
        print(f"nquantidade de sacos dentro do limite: {dentro_do_limite} de 6")

        


