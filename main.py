import logging
from app.auth import obter_token
from app.produtos import listar_produtos
from app.estoque import buscar_sku
from app.pedidos import criar_pedido
from app.hooks import registrar_hook

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def menu():
    print("\n=== API Muven CLI ===")
    print("1. Listar produtos")
    print("2. Ver estoque por SKU")
    print("3. Criar pedido")
    print("4. Registrar webhook")
    print("0. Sair")

def executar():
    token = obter_token()
    if not token:
        logging.error("❌ Não foi possível obter o token de autenticação.")
        return

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produtos = listar_produtos(token)
            print(f"\n🛒 Total de produtos: {len(produtos)}")
            for p in produtos:
                print(f"📦 {p.get('name')} | SKU: {p.get('sku')}")

        elif opcao == "2":
            sku = input("Informe o SKU: ")
            quantidade = buscar_sku(token, sku)
            if quantidade == "Estoque não registrado":
                print("ℹ️ Estoque não registrado para este SKU.")
            else:
                print(f"📦 Estoque disponível: {quantidade}")

        elif opcao == "3":
            print("\n⚠️ Criação de pedido ainda não está interativa.")
            print("🔧 Use um script separado para montar o JSON do pedido.")
            print("💡 Consulte app/pedidos.py para exemplo.")

        elif opcao == "4":
            url = input("Informe a URL do seu webhook (ex: https://exemplo.com/webhook): ")
            seller_id = input("Informe o sellerId: ")
            resposta = registrar_hook(token, url, seller_id)
            if resposta:
                print("✅ Hook registrado com sucesso!")
            else:
                print("❌ Falha ao registrar hook.")

        elif opcao == "0":
            print("👋 Saindo...")
            break

        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    executar()
