import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools 
from dotenv import load_dotenv

load_dotenv()

personalidade = st.sidebar.selectbox("Personalidade do Agente", ["Professor de python", "Professor de historia", "cientista maluco"])

descricao = {
    "Professor de python":"Voce é um professor de python que responde com exemplos e contexto",
    "Professor de historia": "voce é um professor de historia que ensina de forma clara, simples e objetiva", 
    "cientista maluco": "voce é cientista maluco que sempre esta em busca de novas inovações e projetos"
}

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description=descricao[personalidade],
    tools=[WikipediaTools(), DuckDuckGoTools()],
    markdown=True
)

if "mensagens" not in st.session_state:
    st.session_state.mensagem = []
    
for msg in st.session_state.mensagem:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if st.sidebar.button("Limpar Conversa"):
    st.session_state.mensagem = []
    st.rerun()
    
st.title("Sistema MultiAgente")

pergunta = st.chat_input("Digite sua mensagem: ")

if pergunta:
    
    with st.chat_message("user"):
        st.markdown(pergunta)
        st.session_state.mensagem.append({"role":"user", "content":pergunta})
    with st.chat_message("assistant"):
        with st.spinner("Gerando resposta..."):
            resposta = agente.run(pergunta)
            st.markdown(resposta.content)
            
        st.session_state.mensagem.append({"role":"assistant", "content":resposta.content})