import streamlit as st

st.title("Cadastramento dos seus dados para o recrutamento")

nome = st.text_input("Digite o seu nome: ")
email = st.text_input("Digite o seu e-mail: ")

if st.button("Cadastrar"):
    if nome and email:
     st.success("Seus dados foram salvos com sucesso")
     st.balloons()
    else:
     st.error("Falta de dados")
    
