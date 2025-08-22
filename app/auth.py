import os
import requests
from dotenv import load_dotenv

load_dotenv()

AUTH_URL = "https://muven-channel-api.c2bsoftware.com.br/auth/realms/c2b/protocol/openid-connect/token"

def obter_token():
    """
    Autentica via OAuth2 (grant_type: password) e retorna o access_token.
    """
    payload = {
        'client_id': os.getenv('CLIENT_ID'),
        'client_secret': os.getenv('CLIENT_SECRET'),
        'username': os.getenv('API_USERNAME'),
        'password': os.getenv('API_PASSWORD'),
        'grant_type': 'password',
        'scope': 'profile'
    }

    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        response = requests.post(AUTH_URL, headers=headers, data=payload)
        response.raise_for_status()
        token = response.json().get('access_token')
        return token
    except requests.exceptions.RequestException as e:
        print(f"[ERRO] Falha ao obter token: {e}")
        return None
