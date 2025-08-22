import requests

def obter_estoques(token):
    """
    Retorna a lista de estoques de todos os produtos (em massa).
    """
    url = "https://muven-channel-api.c2bsoftware.com.br/api/v1/products/stocks?version=0"  # note o "stocks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha ao obter estoques: {e}")
        return []

def criar_mapa_estoque(lista_estoques):
    """
    Cria um dicionário mapeando SKU para quantidade.
    """
    return {item["skuCode"]: item["stockQty"] for item in lista_estoques}

def buscar_sku(token, sku):
    """
    Busca a quantidade de estoque de um SKU específico.
    Se o SKU não estiver presente na listagem, retorna 'Estoque não registrado'.
    """
    estoques = obter_estoques(token)
    for item in estoques:
        if item.get("skuCode") == sku:
            return item.get("stockQty")
    return "Estoque não registrado"