from dotenv import load_dotenv


load_dotenv()

chave = load_dotenv()

if chave:
    print(f"Chave foi carregada com sucesso!")
else:
    print("Nenhuma chave de ambiente encontrada.")
