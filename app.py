import streamlit as st
import json
import requests

# Título
st.title('Modelo de Predição de Salário')

# Inputs dop Usuário: tempo na empresa e nível na empresa using sliders

st.write("Quantos meses o profissional está na empresa?")
tempo_empresa = st.slider('Tempo na Empresa', min_value=0, max_value=120, value=60, step=1)

st.write("Qual nível do profissional na empresa?")
nivel_empresa = st.slider('Nível na Empresa', min_value=0, max_value=10, value=5, step=1)



# Preparar dados para api

input_features = {
    'tempo_na_empresa': tempo_empresa,
    'nivel_na_empresa': nivel_empresa
}

# Criar um botão e capturar um evento para disparar a API

botao = st.button('Estimar salário')

if botao:
    # Fazer a requisição para a API
    response = requests.post('http://127.0.0.1:8000/predict', data=json.dumps(input_features))
    # Mostrar o resultado
    if response.status_code == 200:
        st.success(f'O salário estimado é: R$ {round(response.json()['salario_em_reais'],2)}')
    else:
        st.error(f'Ocorreu um erro: {response.status_code}')
