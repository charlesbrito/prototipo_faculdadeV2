import streamlit as st
from streamlit_option_menu import option_menu
from dashboard import dashboard
from clientes import cliente
from nf_e import nfe
from receitas import receitas
from home import home

st.markdown(
    """
    <style>
        /* Ajusta a largura da barra lateral */
        [data-testid="stSidebar"] {
            min-width: 250px;
            max-width: 250px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
    selected = option_menu("Menu", ["Home", "Configurações", "Dashboard", "Clientes", "Perfil", "NF-E", "Receitas", "Despesas"],
                           icons=['house', 'gear', 'graph-up', 'people', 'person', 'file-earmark-text', 'currency-dollar', 'clipboard-data'], menu_icon='cast', default_index=1)
    selected

if selected == "Dashboard":
    dashboard()
elif selected == "Clientes":
    cliente()
elif selected == "NF-E":
    nfe()
elif selected == "Receitas":
    receitas()
elif selected == "Home":
    home()