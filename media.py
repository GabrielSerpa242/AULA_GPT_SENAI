n1 = float(input("Digite a primeira nota: ")) 
n2 = float(input("Digite a segunda nota: ")) 
n3 = float(input("Digite a teceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4)/ 4 

print(f"a sua média é {media}")   

if media >=7:
    print("Parabens voce passou 🥳") 
else:
    print("Você não passou 😫, estude mais ano que vem 🥲")