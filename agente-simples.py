from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat 

# Carregar as variáveis de ambiente do arquivo .env E A FUNÇÃO load_dotenv() É CHAMADA PARA CARREGAR AS VARIÁVEIS DE AMBIENTE DO ARQUIVO .env
load_dotenv() 

agente = Agent(
    #essa linha define o modelo de linguagem a ser utilizado pelo agente.
    model = OpenAIChat(id="gpt-4o-mini"),
    markdown = True
)

perg = input("Me fale algo: ")
resposta = agente.print_response(perg)
print(resposta)