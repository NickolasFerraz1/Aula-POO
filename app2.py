import requests 
import json
url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)
print(response)

if response.status_code == 200:
    restaurantes = response.json()
    dados_restaurantes = {}
    for item in restaurantes:
        nome_do_restaurante = item["Company"]
        if nome_do_restaurante not in dados_restaurantes:
            dados_restaurantes[nome_do_restaurante] = []

        dados_restaurantes[nome_do_restaurante].append({
                    "item": item["Item"],
                    "preco": item["price"],
                    "descricao": item["description"]
                })
else:
    print("Não foi possível obter os dados dos restaurantes.")

for nome_do_restaurante, itens in dados_restaurantes.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo:
        json.dump(itens, arquivo, indent=4)