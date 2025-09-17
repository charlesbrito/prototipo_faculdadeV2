import streamlit as st
import pandas as pd

def fornecedores():
    st.title("Cadastre aqui seus fornecedores")
    if 'fornecedores' not in st.session_state:
        st.session_state.fornecedores = []
    with st.form('form_fornecedores'):
        co1,co2 = st.columns(2)
        with co1:
            n_fornecedor = st.text_input("Nome do fornecedor")
            endereco = st.text_input("Endereço")
            cnpj = st.text_input("CNPJ")
        with co2:
            telefone = st.text_input("Telefone")
            email = st.text_input("Email")

        cadastrar = st.form_submit_button("Registrar fornecedor")

        if cadastrar:
            st.session_state.fornecedores.append({
                "Nome do cliente": n_fornecedor,
                "Endereço": endereco,
                "CNPJ": cnpj,
                "Telefone": telefone,
                "Email": email
            })
            st.success("Fornecedor cadastrado com sucesso")
    if st.session_state.fornecedores:
        st.subheader("Fornecedores")
        df = pd.DataFrame(st.session_state.fornecedores)
        st.dataframe(df, use_container_width=True)
 

if __name__ == '__main__':
    fornecedores()