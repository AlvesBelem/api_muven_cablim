import requests

def registrar_hook(token, url_callback, seller_id):
    """
    Registra um webhook para notificações da Muven.

    :param token: token de autenticação OAuth
    :param url_callback: URL da sua aplicação que receberá notificações POST
    :param seller_id: identificador único do cliente
    :return: resposta da API ou None em caso de erro
    """
    url = "https://muven-channel-api.c2bsoftware.com.br/api/v1/hooks"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "url": url_callback,
        "sellerId": seller_id
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha ao registrar hook: {e}")
        return None
