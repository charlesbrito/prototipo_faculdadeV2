import streamlit as st
import streamlit_shadcn_ui as ui
import streamlit_antd_components as sac

def home():
    st.title("Seja bem vindo, microempreendedor")
    st.write("Aqui estão seus avisos")

    co1, co2, co3  = st.columns(3)
    with co1:
        ui.metric_card(title='Contas pendentes', content="R$ 4.000,00", description="Clientes em pendência")

    with co2:
        ui.metric_card(title="Contas a pagar", content="R$1.000,00", description="Divida com fornecedores" )

    with co3:
        ui.metric_card(title="Impostos", content="R$500,00", description="Impostos pendentes")

    sac.alert(label="Atenção", description=" Procure um contador para mais orientações", banner=True, icon=True, closable=True)



if __name__ == '__main__':
    home()