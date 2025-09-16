import streamlit as st
import pandas as pd

def impostos():
    st.title("Calcule seus impostos")
    with st.form("Impostos_form"):
          salario = st.number_input("Salário minimo", format='%.2f') 
          trabalho = st.radio("Escolha seu tipo de trabalho", ['Prestação de serviço', 'comércio']) 
          st.write("Depois de inserir as informações, clique em calcular")

          submit = st.form_submit_button("Calcular")

          if submit:
              if trabalho == "Prestação de serviço":
                  inss = salario * 0.05
                  icms = 1
                  total = inss + icms
                  st.write("Você vai pagar:")
                  st.write(f"R$ {inss} em INSS")
                  st.write(f"R$ {icms} em ICMS")
                  st.write(f"Total: R$ {total}")
                  st.warning("Fique atento as datas de pagamento, se possivel, fale com um contador")
              elif trabalho == "comércio":
                  inss = salario * 0.05
                  iss = 5
                  total = inss + iss
                  st.write("Você vai pagar:")
                  st.write(f"R$ {inss} em INSS")
                  st.write(f"R$ {iss} em ICMS")
                  st.write(f"Total: R$ {total}")
                  st.warning("Fique atento as datas de pagamento, se possivel, fale com um contador")

                  
                  

       
    




if __name__ == '__main__':
   impostos()

