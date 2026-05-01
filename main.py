import sys
print(f"DEBUG: O Python que está rodando é: {sys.executable}")
import requests

from fastapi import FastAPI, Query, HTTPException
import requests
app = FastAPI()

@app.get("/api/hello")
def hello():
    '''
    Endpoint de exemplo para testar a API.
    '''
    return {"message": "Hello, World!"}

@app.get("/api/restaurantes/")
def listar_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para listar os restaurantes e seus cardápios.
    '''
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"
    response = requests.get(url)

    if response.status_code == 200:
        restaurantes = response.json()
        if restaurante is None:
            return {"Dados dos restaurantes": restaurantes}
        
        dados_restaurantes = []
        for item in restaurantes:
            if item["Company"].lower() == restaurante.lower():
                dados_restaurantes.append({
                            "item": item["Item"],
                            "preco": item["price"],
                            "descricao": item["description"]
                        })
        return {"Restaurante": restaurante, "Cardápio": dados_restaurantes}

    else:
        raise HTTPException(status_code=response.status_code, detail="Erro ao buscar dados da API externa")