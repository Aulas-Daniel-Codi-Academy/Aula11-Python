# Importa a biblioteca requests, usada para fazer requisições HTTP
import requests

# Função que recebe um CEP e busca o endereço correspondente na BrasilAPI
def buscar_endereco(cep):
    # Monta a URL da requisição usando o CEP informado
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    
    try:
        # Realiza a requisição GET para a API
        response = requests.get(url)

        # Lança erro se o status HTTP for 4xx ou 5xx
        response.raise_for_status()

        # Converte a resposta JSON para um dicionário Python
        dados = response.json()
        
        # Exibe os dados do endereço encontrados
        print("\n📍 Endereço Encontrado:")
        print(f"CEP: {dados.get('cep')}")
        print(f"Rua: {dados.get('street')}")
        print(f"Bairro: {dados.get('neighborhood')}")
        print(f"Cidade: {dados.get('city')}")
        print(f"Estado: {dados.get('state')}")

    # Captura erros HTTP, como CEP não encontrado
    except requests.exceptions.HTTPError:
        print("❌ CEP não encontrado ou inválido.")

    # Captura outros tipos de erros na requisição
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar a API: {e}")

# Bloco principal: executado quando o script é rodado diretamente
if __name__ == "__main__":
    print("=== Buscar Endereço pelo CEP ===")
    
    # Pede ao usuário que digite o CEP
    cep = input("Digite um CEP (somente números): ").strip()
    
    # Remove traços e espaços do CEP (caso o usuário digite com "-")
    cep = cep.replace("-", "").replace(" ", "")

    # Verifica se o CEP tem 8 dígitos numéricos
    if len(cep) == 8 and cep.isdigit():
        # Chama a função para buscar o endereço
        buscar_endereco(cep)
    else:
        # Informa que o CEP está inválido
        print("❌ CEP inválido. Digite exatamente 8 dígitos.")
