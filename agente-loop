from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat  

load_dotenv() 

agente = Agent(
    
    model = OpenAIChat(id="gpt-4o-mini"),
    markdown = True
)

while True:
    perg = input("Digite a sua pergunta: ")
    
    if perg.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o agente. Até mais!")
        break
    else:
        agente.print_response(perg)