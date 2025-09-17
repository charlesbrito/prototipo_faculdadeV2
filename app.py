import streamlit as st
from streamlit_option_menu import option_menu
from dashboard import dashboard
from clientes import cliente
from nf_e import nfe
from receitas import receitas
from home import home
from impostos import impostos
from despesas import despesas
from fornecedores import fornecedores
from bate_papo import bate_papo

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
    selected = option_menu("Menu", ["Home", "Dashboard", "Clientes", "NF-E", "Receitas", "Despesas", "Impostos", "Fornecedores", "Bate-Papo"],
                           icons=['house', 'graph-up', 'people', 'file-earmark-text', 'currency-dollar', 'clipboard-data', 'receipt', 'tag', 'bi-chat'], menu_icon='cast', default_index=1)
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
elif selected == "Impostos":
    impostos()
elif selected == "Despesas":
    despesas()
elif selected == "Fornecedores":
    fornecedores()
elif selected == "Bate-Papo":
    bate_papo()