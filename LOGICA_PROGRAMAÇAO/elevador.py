# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

# anotações
#  o elevador deve ter uma programação de forma ordenada em relação a definição do local e ordem de chamada ( quem pediu primeiro ou o último a pedir )
# o elevador deve emitir um sinal de alerta avisando para respeitar o limite de peso do elevador 
# o elevador também deve apresentar um aviso de  indisponibilidade caso etsteja em  manutenção 
# o elevador também deve realizar um escaneamento via raio x  para evitar o porte de armas e prevenção dos outros passa

print (" selecione o botão para chamar o elevador ")
print (" aguarde alguns instantes ")


m1 = int (input ("olá informe o andar em que você está "))
m2 = int (input ("informe qual andar você deseja, ( preesione 0 para térreo):"))
m3 = print ("andar ", m1,"indo para o andar ", m2)
print("verificação de pessoas ")
pessoas = int(input(" há quantas pessoas no elevador  "))

if pessoas >= 5:
    print (" alerta: o limite de pessoas foi violado ")
elif pessoas <= 5:
    print(" descendo")

# manutenção 

andar_inicial = input("digite seu andar inicial:")
andar_final = input("digite seu andar final ")
try:
    andar_inicial=  f"{andar_inicial} {andar_final}"
    print(f"olá, estamos em manutenção no momento, agradecemos a compreenção !")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


