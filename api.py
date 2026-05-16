# Instalar bibliotecas necessárias
#pip install 

#segundo passo: ADICIONAR/importar ao codigo 
import requests 


nome = input("Digite o seu nome: ")
email = input("Digite o seu email: ")
tel = input("Digite o seu telefone: ")
cep = input("Digite o seu CEP: ")

#cria uma variavel atribui o resultado do link da API, onde o {cep} é o valor do cep que o usuario digitou, e o json() é para transformar a resposta em um dicionário python
url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url).json()


print(f"Bem - vindo, ao Mercado LIVRE, {nome}! \nSeu email é: {email} \nSeu telefone é: {tel} \nSeu CEP é: {cep}. \nVocê mora na rua: \n{dados['logradouro']}, \nbairro: {dados['bairro']}, \ncidade: {dados['localidade']} - {dados['uf']}")
# rua = dados['logradouro']
# bairro = dados['bairro']
# cidade = dados['localidade']
# estado = dados['uf']

# print(f"Rua: {rua}")
# print(f"Bairro: {bairro}")
# print(f"Cidade: {cidade}")
# print(f"Estado: {estado}")