# import csv
# import os
#
# arquivo = "clientes.txt"
#
# def arquivo_existe():
#     return os.path.isfile(arquivo)
#
# def proximo_id():
#     with open(arquivo, 'r') as arquivo_clientes:
#         reader = csv.reader(arquivo_clientes)
#         ultima_linha = list(reader)[-1]
#         id = ultima_linha[0]
#         return (int(id)+1)
#
# def escreve_dados(id, nome, cpf, endereco, telefone):
#     with open(arquivo, 'a') as arquivo_clientes:
#         writer = csv.writer(arquivo_clientes)
#         writer.writerow([id, nome, cpf, endereco, telefone])
#
# nome = input("Digite o nome do cliente: ")
# cpf = input("Digite o CPF do cliente:   ")
# endereco = input("Digite o endereco do cliente: ")
# telefone = input("Digite o Telefone do cliente: ")
# if(arquivo_existe()):
#     escreve_dados(str(proximo_id()), nome, cpf, endereco, telefone)
# else:
#     escreve_dados(1, nome ,cpf, endereco, telefone)
str = "     this is string example....wow!!!     ";
print (str.rstrip())
str = "88888888this is string example....wow!!!8888888";
print (str.rstrip('8'))