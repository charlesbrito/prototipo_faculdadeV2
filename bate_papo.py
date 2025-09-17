import streamlit as st

def bate_papo():
    st.title("Seu assistente")
    if 'assistente' not in st.session_state:
        st.session_state.assistente = []

    for massage in st.session_state.assistente:
        with st.chat_message(massage["role"]):
            st.markdown(massage["content"])
    
    if prompt := st.chat_input("Em que posso te ajudar ?"):
        st.session_state.assistente.append({"user": "role", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        resposta = f"Sua mensagem: {prompt}"
        st.session_state.assistente.append({'role':'assistant', 'content': resposta})
        with st.chat_message("assistant"):
            st.markdown(resposta)

if __name__ == '__main__':
    bate_papo()