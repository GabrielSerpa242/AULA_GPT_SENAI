# Coleta de informações
p1 = input("Onde ele estava ontem à noite? ").lower()
p2 = input("O que ele estava fazendo? ").lower()
p3 = input("Quem estava com ele? ").lower()

print("-" * 30)





if "biblioteca" in p1 and "estudando" in p2:
    print("Veredito: Ele é inocente. Apenas um estudante dedicado.")

elif "banco" in p1 and "correndo" in p2:
    print("Veredito: ATENÇÃO! Ele é o principal suspeito do assalto!")

elif "casa" in p1 and "dormindo" in p2:
    if "ninguém" in p3 or "sozinho" in p3:
        print("Veredito: Álibi fraco. Precisamos investigar mais.")
    else:
        print(f"Veredito: O depoimento de {p3} confirma a história. Limpo.")

else:
    print("Veredito: Informações inconclusivas. Continue a vigilância.")