import streamlit as st

st.title('Suma tres números')

st.write( 'Usando `st.number_input`')

n1 = st.number_input('Introduce el primer número')
n2 = st.number_input('Introduce el segundo número')
n3 = st.number_input('Introduce el tercer número')

st.write("La suma de los tres números es ", n1+n2+n3)

st.write( 'Usando `st.slider`')

n4 = st.slider('Introduce el primer número')
n5 = st.slider('Introduce el segundo número')
n6 = st.slider('Introduce el tercer número')

st.write("La suma de los tres números es ", n4 + n5 + n6)