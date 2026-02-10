import requests


def buscar_cnpj(cnpj):

    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
    url = f'https://brasilapi.com.br/api/cnpj/v1/{cnpj}'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"Nome: {dados['razao_social']}")
        print(f"Nome fantasia: {dados['nome_fantasia']}")
        print(f"Logradouro: {dados['logradouro']}, {dados['numero']}")
        return dados
    else:
        print("Erro ao buscar CNPJ. Verifique se o número está correto.")
        return None
buscar_cnpj("39.952.855/0001-58")
