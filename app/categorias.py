import requests

def obter_categorias(token: str):
    url = "https://muven-channel-api.c2bsoftware.com.br/api/v1/categories?version=0"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"[ERRO] Falha ao obter categorias: {response.status_code} - {response.text}")
