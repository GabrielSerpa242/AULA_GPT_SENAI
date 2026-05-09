listaNotas = [] 

print("Bem vindo a IA que compara a nota e a media final")

while True: 
    notas = input("Digite a sua nota que deseja inserir (digite sair para parar): ")

    if notas.lower() == "sair":
        break
    else: 
        listaNotas.append(float(notas)) 
     
media = sum(listaNotas) / len(listaNotas)

if media >= 6:
     print("Parabens voce passou 🥳") 
else:
    print("Você não passou 😫, estude mais ano que vem 🥲")

print(f"A média final do aluno é {media:.2f}")#2f limita 