import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

def cliente():
    st.title("Cadastre aqui seus clientes")
    if 'clientes' not in st.session_state:
        st.session_state.clientes = []
    with st.form('form_cliente'):
        co1,co2 = st.columns(2)
        with co1:
            n_cliente = st.text_input("Nome do cliente")
            endereco = st.text_input("Endereço")
            cnpj_cpf = st.text_input("CNPJ/CPF")
        with co2:
            telefone = st.text_input("Telefone")
            email = st.text_input("Email")

        cadastrar = st.form_submit_button("Registrar cliente")

        if cadastrar:
            st.session_state.clientes.append({
                "Nome do cliente": n_cliente,
                "Endereço": endereco,
                "CNPJ/CPF": cnpj_cpf,
                "Telefone": telefone,
                "Email": email
            })
            st.success("Cliente cadastrado com sucesso")
    if st.session_state.clientes:
        st.subheader("Lista de clientes")
        df = pd.DataFrame(st.session_state.clientes)
        if not df.empty:
            gb = GridOptionsBuilder.from_dataframe(df)
            gb.configure_default_column(editable=True) 
            gb.configure_selection(selection_mode="single", use_checkbox=True)
            grid_options = gb.build()

            grid_response = AgGrid(
                df,
                gridOptions=grid_options,
                update_mode=GridUpdateMode.MODEL_CHANGED,
                height=300,
                fit_columns_on_grid_load=True
            )

            


if __name__ == '__main__':
    cliente()