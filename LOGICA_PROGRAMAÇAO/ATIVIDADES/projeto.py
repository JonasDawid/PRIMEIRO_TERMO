#  Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado 
# Se possuir erros informar ao usuario

# Passo 2:
# Verificar tempo de permanencia
# Valor a ser cobrado

# Passo 3:
# Saida como sera?
# Calcular tempo de permanencia
# Se for tag gerar na fatura da tag
# Pagar ticket
# Devolver ticket na saida

# Passo 4:
# Gerar relatorio de entradas e saidas
# Tratamento de Erros
# Revisão do código



print (" olá bem vindo ao shopping ")

print( input("isira as informações do seu veículo"))
print (" pretende ficar quanto tempo ? didgite em  ")

visita = ["compras,passeio,descarga"]
for  vsita  in visita :
    print(f"gerando ticket: {visita}.")
    print(f"ticket {visita} processado com sucesso!")
    print (" retire o ticket e boa visita ")