from fastapi import FastAPI, HTTPException
from app.auth import obter_token
from app.produtos import listar_produtos
from app.estoque import buscar_sku
from app.pedidos import criar_pedido
from app.hooks import registrar_hook

app = FastAPI(title="API Muven Integrada", version="1.0.0")


@app.get("/produtos")
def get_produtos():
    token = obter_token()
    if not token:
        raise HTTPException(status_code=401, detail="Token inválido.")
    produtos = listar_produtos(token)
    return produtos


@app.get("/estoque/{sku}")
def get_estoque(sku: str):
    token = obter_token()
    if not token:
        raise HTTPException(status_code=401, detail="Token inválido.")
    quantidade = buscar_sku(token, sku)
    return {
        "sku": sku,
        "quantidade": quantidade if quantidade is not None else "Estoque não registrado"
    }


@app.post("/pedidos")
def post_pedido(pedido: dict):
    token = obter_token()
    if not token:
        raise HTTPException(status_code=401, detail="Token inválido.")
    resposta = criar_pedido(token, pedido)
    if resposta is None:
        raise HTTPException(status_code=400, detail="Erro ao criar pedido.")
    return resposta


@app.post("/hooks")
def post_hook(payload: dict):
    token = obter_token()
    if not token:
        raise HTTPException(status_code=401, detail="Token inválido.")
    url = payload.get("url")
    seller_id = payload.get("sellerId")

    if not url or not seller_id:
        raise HTTPException(status_code=422, detail="Campos obrigatórios ausentes.")

    resposta = registrar_hook(token, url, seller_id)
    if resposta is None:
        raise HTTPException(status_code=400, detail="Erro ao registrar hook.")
    return resposta
