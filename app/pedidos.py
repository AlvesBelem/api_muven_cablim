import requests

def criar_pedido(token, pedido_data):
    """
    Envia um novo pedido para a API Muven.
    
    :param token: token de acesso OAuth
    :param pedido_data: dicionário com os dados completos do pedido
    :return: resposta da API ou None em caso de erro
    """
    url = "https://muven-channel-api.c2bsoftware.com.br/api/v1/orders"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=pedido_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha ao criar pedido: {e}")
        return None
