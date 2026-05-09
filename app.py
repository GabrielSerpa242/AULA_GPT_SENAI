print("-=-"*15)
print('\t\nBem-Vindo ao coletor de dados do GPT 🤖😎')
print("-=-"*15)

nome = input('qual é o seu nome: ') #o input recebe dados do usuario
email = input('Digite o seu email: ')
cid = input('Onde voce mora: ')
estado = input('Qual é o seu estado: ')
pais = input('Qual é o seu pais: ')
idadeAtual = int(input('Qual é a sua idade: '))
idadeFut = idadeAtual + 1
ano = int(input("Qual é o ano atual: "))
nasc = ano - idadeAtual



print(f"""\tOlá {nome}, 
        o seu email é {email}, 
        voce mora em {cid}, 
        o seu estado é {estado}, 
        o seu país é {pais}, 
        a sua idade atual é {idadeAtual}, 
        daqui um ano você vai ter {idadeFut}
        o ano atual é {ano}
        e o ano que voce nasceu foi {nasc}""")#o f minusculo serve para formatar a variavel na frase
