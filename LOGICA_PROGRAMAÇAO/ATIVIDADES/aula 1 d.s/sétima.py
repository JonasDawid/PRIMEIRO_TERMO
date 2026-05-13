# atividade 1 

# print(" Registro de veículo ")
# modelo = input (" qual é o veículo ?")
# placa = input (" qual é placa do veículo")
# print(f" veículo {modelo} de placa {placa} registrado no sistema. Boa viagem!")

# # atividade 2 

# print("cálcuo de autonomia ")
# tanque = float(input(" qual é a capacidade de seu tanque em litros "))
# consumo= float(input("digite o consumo médio por caminhão em km/L "))
# total = tanque/consumo 
# print(f"seu caminhão pode percorrer {total:.2f} em km/l")
# print (" seu caminhão pode percorrer",round(total,2)," em km/l")

# atividade 3 
# print(" conversor de moeda (frete internacional)")
# valor_reais = float(input(" qual é o valor em Reais que será convertido ?..."))
# taxa_dolar = float(input(" qual é o valor da taxa  em dolar ?"))
# total = valor_reais / taxa_dolar 
# print(f" o valor total convertido é...{total:.2f}")


# # 4 atividade 
# print (" média de entrega")
# tempo1 = int(input(" qual foi o tempo para concluir a rota 1 em horas"))
# tempo2 = int(input("qual foi o tempo para concluir a rota 2 em horas"))
# tempo3 = int(input("qual foi o tempo para concluir a rota 3 em horas"))
# media = (tempo1 + tempo2 + tempo3) /3
# print (f"A média {media:.2f} de tempo das entregas ")

 # atividade 5 
# print (" Monitor de Carga ")
# peso = float(input(" qual é o peso atual do seu caminhão..."))
# if peso < 10:
#     print("carga leve ")
# elif peso <= 25:
#     print ("carga padrão")
# else: 
#     print("ALERTA:" \
#     "Excesso de peso!")

# # atividade 6 

# print (" classificador de destino ")
# print (" regiões = N -  Região Norte, S - Região Sul, qualquer outra - Internacional ")
# região = input(" inserir o código da região: ").lower() 
# if região =="N".upper() or região == "n" .lower:
#     print  (" região norte ")
# elif região == "S":
#  print(" região Sul")
# else:
#    print("região internacional ")

#    # atividade 7 

#    print(" liberação de saída ")
#    checklist = input(" o checklist foi concluído? [ sim ou não ]")
#    motorista = input (" o motorista foi identificado [sim ou não ]")
#    if checklist == "concluído" and motorista == "sim":
#       print(" veículo autorizado a iniciar a rota ")
#       else :
#       print (" veeículo NÃo autroizado a iniciar  ROTA. VERIFICAR CHECKLIST E IDENTIFICAÇÃO DO MOTORISTA ")

# # ATIVIDADE 8

# print(" cálculo de atrasos ")
# total_entregas = int(input(" total de entregas agendadas:..."))
# total_atrasos = int(input(" total de entregas e atrasos:..."))
# if total_atrasos > total_entregas * 0.1:
#  print(" necessário otimizar rotas ")
# else:
#  print("logistica eficiente ")
 
# # ATIVIDADE 9
# print(" validação de calibragem ")
# pressao = float(input(" digite a pressão de um pneu em PSI:..."))
# if 100 <= pressao <= 110:
#  print("dentro do padrão")
# elif pressao < 100:
#  print("abaixo do recomendado ")
# else:
#  print ("acima do recomendado")

# ATIVIDADE 11

# print(" somatório de frete (acumulador)")
# faturamento_total = 0
# valor_frete = -1
# while valor_frete != float(input(" valor do frete ou 0 para encerrar ")):
#      faturamento_total += valor_frete
# print(f" faturamento acumulado:R$ {faturamento_total}")
# print("cálculo executado com sucesso")

# # Atividade 12

# print (" monitoramento de frota")
# maior_km = 0
# for frota in range(1,6):
#     km = float(input(f"Digite a quilometragem do veículo {frota}:"))
# if km > maior_km:
#     maior_km = km 
# print(f"A maior quilometragem registrada é: {maior_km} km.")

# # ATIVIDADE 13
# print ("sistema de rastreio ")
# codigo_correto = "track99"
# tentativas = 0
# max_tentativas =3 
# while tentativas < max_tentativas:
#     código_input = input("código de acesso para o rastreador:  :)")
#     if código_input == codigo_correto:
#         print("acesso permitido.iniciando o rastreamento...")
#         break
#     else:
#         tentativas += 1
#         print("acesso negado ")
#         if tentativas < max_tentativas:
#             print(f"tentativas restantes: {max_tentativas-tentativas}")
# else: 
#     print(" rastreamento bloqueado")

