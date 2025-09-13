import streamlit as st
import pandas as pd
from datetime import date

def receitas():
    st.title("Cadastro de receitas")
    if "receitas" not in st.session_state:
        st.session_state.receitas = []

    with st.form("receitas_form"):
        co1, co2 = st.columns(2)
        with co1:
            data = st.date_input("Data", value=date.today())
            cliente_fonte = st.text_input("Cliente/fonte")
            descricao = st.text_input("Descrição")
        with co2:
            categoria = st.text_input("Produto/serviço")
            valor = st.number_input("Valor", min_value=0.0, step=0.1, format='%.2f')
            status = st.text_input("Pendente/Pago")

        cad_receita = st.form_submit_button("Cadastrar receita")

        if cad_receita:
            st.session_state.receitas.append({
                "Data": data,
                "Fonte": cliente_fonte,
                "Descrição": descricao,
                "Categoria": categoria,
                "Valor": valor,
                "Status": status
            })

            st.success("Receita cadastrada com sucesso")
    
    if st.session_state.receitas:
        st.subheader("Histórico de receitas")
        df = pd.DataFrame(st.session_state.receitas)
        st.dataframe(df, use_container_width=True)



if __name__ == '__main__':
    receitas()