nomeUser = input("Digite seu nome: ") 
senhaUser = input("Digite sua senha: ") 

if nomeUser.capitalize() == "Gabriel" and senhaUser == "1234":
    print("Acesso liberado") 
else:
    print("Acesso negado! Verifique as informaçõe de login e tente novamente")