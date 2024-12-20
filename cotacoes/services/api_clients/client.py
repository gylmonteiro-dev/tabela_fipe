import requests

BASE_URL = "https://parallelum.com.br/fipe/api/v1"

def consulta_marcas(tipo_veiculo:str):
    endereco_formatado = f'{BASE_URL}/{tipo_veiculo}/marcas'
    resposta = requests.get(endereco_formatado)
    return resposta.json()

def consulta_modelos(tipo_veiculo:str, id_marca:str):
    endereco_formatado = f'{BASE_URL}/{tipo_veiculo}/marcas/{id_marca}/modelos'
    resposta = requests.get(endereco_formatado)
    return resposta.json()


def consulta_anos_modelo(tipo_veiculo: str, id_marca: str, id_modelo:str):
    endereco_formatado = f"{BASE_URL}/{tipo_veiculo}/marcas/{id_marca}/modelos/{id_modelo}/anos"
    resposta = requests.get(endereco_formatado)
    return resposta.json()

def consulta_valor_ano_modelo(tipo_veiculo: str, id_marca: str, id_modelo:str, id_ano:str):
    endereco_formatado = (
        f"{BASE_URL}/{tipo_veiculo}/marcas/{id_marca}/modelos/{id_modelo}/anos/{id_ano}"
    )
    resposta = requests.get(endereco_formatado)
    return resposta.json()
