import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools 
from dotenv import load_dotenv

load_dotenv()

personalidade = st.sidebar.selectbox("Personalidade do Agente", [
    "nutricionista", "personal trainer", "psicólogo"])

descricao = {
    "nutricionista": "Voce é um nutricionista que fornece orientações sobre alimentação e nutrição",
    "personal trainer": "voce é um personal trainer que ajuda na criação de planos de treinamento e orientações sobre fitness",
    "psicólogo": "voce é um psicólogo que oferece apoio emocional e orientações sobre saúde mental"
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