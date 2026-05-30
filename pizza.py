import streamlit as st 

st.image("pizza.png")

nome = st.text_input("Digite o seu nome: ")
cid = st.text_input("Digite a sua cidade: ")
bairro = st.text_input("Digite o seu bairro: ")
sabor = st.selectbox("Escolha o sabor da pizza: ", ["Calabresa", "Mussarela", "Frango com Catupiry", "Portuguesa", "Quatro Queijos"])

if st.button("Confirmar Pedido🤤"):
    if nome and cid and bairro and sabor:
        st.success(f"Olá {nome}, você mora em {cid} no bairro {bairro} e escolheu a pizza de {sabor}.")
        st.balloons()
    else:        
        st.error("Por favor, preencha todos os campos.")