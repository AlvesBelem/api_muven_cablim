import requests

def listar_produtos(token):
    """
    Lista todos os produtos disponíveis no canal.
    """
    url = "https://muven-channel-api.c2bsoftware.com.br/api/v1/products?version=0"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        produtos = response.json()
        return produtos
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha ao obter produtos: {e}")
        return []
