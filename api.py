from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
import pandas

app = FastAPI()

# Criar uma classe com dados de entrada que virtão no request body com os tipos esperados

class requestBody(BaseModel):
    tempo_na_empresa: int
    nivel_na_empresa: int

# Carregar o modelo para realizar a predição

modelo = joblib.load('modelo_poly_grau4.pkl')

# Criar a função que faz a predição
@app.post('/predict')
def predict(data: requestBody):
    input = {'tempo_na_empresa': data.tempo_na_empresa, 'nivel_na_empresa': data.nivel_na_empresa}
    df = pandas.DataFrame(input, index=[0])
    y_pred = modelo.predict(df)[0].astype(float)
    return {'salario_em_reais': y_pred}