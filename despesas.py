import streamlit as st
import pandas as pd
from datetime import date

def despesas():
    st.title("Cadastro de despesas")
    if "despesas" not in st.session_state:
        st.session_state.despesas = []

    with st.form("despesas_form"):
        co1, co2 = st.columns(2)
        with co1:
            data = st.date_input("Data", value=date.today())
            loja = st.text_input("Nome do estabelecimento")
            descricao = st.text_input("Descrição")
        with co2:
            categoria = st.text_input("Produto/serviço")
            valor = st.number_input("Valor", min_value=0.0, step=0.1, format='%.2f')
            status = st.text_input("Pendente/Pago")

        cad_despesa = st.form_submit_button("Cadastrar despesas")

        if cad_despesa:
            st.session_state.despesas.append({
                "Data": data,
                "Fonte": loja,
                "Descrição": descricao,
                "Categoria": categoria,
                "Valor": valor,
                "Status": status
            })

            st.success("Despesa cadastrada com sucesso")
    
    if st.session_state.despesas:
        st.subheader("Histórico de despesas")
        df = pd.DataFrame(st.session_state.despesas)
        st.dataframe(df, use_container_width=True)


if __name__ == '__main__':
    despesas()