from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat  
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools

load_dotenv() 

agente = Agent(
    
    model = OpenAIChat(id="gpt-4o-mini"),
    description = "Agente de Personalidade: Este agente é projetado para responder perguntas e interagir de maneira personalizada, adaptando suas respostas com base no estilo e preferências do usuário. Ele pode fornecer respostas mais informais, usar humor ou adotar um tom mais sério, dependendo do contexto da conversa.",
    add_history_to_context=True,
    tools = [DuckDuckGoTools(), TavilyTools()],
    markdown = True
)

while True:
    perg = input("Digite a sua pergunta: ")
    
    if perg.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o agente. Até mais!")
        break
    else:
        agente.print_response(perg)