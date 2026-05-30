import streamlit as st

st.title("Secretaria SENAI Americana") 
st.subheader("Conheça os nossos cursos")   

st.write("I.A - Generativa, Power BI, Empilhadeira, Excel, Eletriscista Instalador")
st.markdown("**Atenção: Verifique se existem vagas disponiveis para o curso desejado**")

nome = st.text_input("Digite o seu nome: ")
idade = st.number_input("Digite a sua idade: ", min_value=16, max_value=99)
curso = st.selectbox("Escolha o curso desejado: ", ["I.A - Generativa", "Power BI", "Empilhadeira", "Excel", "Eletriscista Instalador"])
aceitaTermos = st.checkbox("Ao clicar aqui, Aceito os termos e condições")


if st.button("Enviar"):
    if nome and idade and curso and aceitaTermos:
        st.success(f"Olá {nome}, você tem {idade} anos e se inscreveu no curso de {curso}.")
        st.balloons()
    else:
        st.error("Por favor, preencha todos os campos.")