# Criar a aplicação FastAPI

# Definir os endpoints (rotas)

# Receber textos do front

# Chamar a lógica de similaridade

# Retornar o resultado em JSON

from fastapi import FastAPI
from pydantic import BaseModel
from app.text_analysis import calcular_similaridade
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API de Similaridade Textual",
    description="API para cálculo de similaridade entre textos usando TF-IDF",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois a gente restringe
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextosEntrada(BaseModel):
    texto1: str
    texto2: str


@app.post("/similaridade")
def calcular(textos: TextosEntrada):
    resultado = calcular_similaridade(textos.texto1, textos.texto2)

    return {
        "similaridade_percentual": resultado
    }
