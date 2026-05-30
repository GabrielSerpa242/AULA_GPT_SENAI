import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools 

load_dotenv()

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description=" Voce é um copyrighter de conteudo de redes sociais, especializado em vendas de qualquer coisa, e tem como objetivo criar conteudo para redes sociais, como instagram, facebook, linkedin, etc. O conteudo deve ser voltado para vendas de produtos ou serviços, e deve ser criativo, persuasivo e envolvente. O conteudo deve ser criado com base nas informações fornecidas pelo usuario, e deve ser adaptado para o publico alvo do usuario. O conteudo deve ser criado com base nas tendencias atuais das redes sociais, e deve ser otimizado para gerar engajamento e conversao.",
    tools=[WikipediaTools(), DuckDuckGoTools()],
    markdown=True
)


st.title("Agente Copyrighter de Conteúdo")

pergunta = st.chat_input("Faça uma pergunta: ")

if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
        with st.spinner("Gerando resposta..."):
            resposta = agente.run(pergunta)
            st.markdown(resposta.content)