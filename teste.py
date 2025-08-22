from app.auth import obter_token
from app.estoque import obter_estoques

if __name__ == "__main__":
    token = obter_token()
    estoques = obter_estoques(token)

    print(f"\nTotal de itens de estoque encontrados: {len(estoques)}\n")
    for item in estoques:
        print(f"SKU: {item.get('skuCode')} | Quantidade: {item.get('stockQty')}")