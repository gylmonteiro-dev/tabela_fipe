from django.shortcuts import render
from .services.api_clients.client import consulta_marcas, consulta_modelos, consulta_anos_modelo, consulta_valor_ano_modelo
# Create your views here.
def home(request):
    return render(request, 'home.html')

def marcas_veiculos(request):
    tipo_veiculo = request.POST.get('veiculo')
    resposta = consulta_marcas(tipo_veiculo=tipo_veiculo)
    return render(request, 'marcas.html', {'tipo_veiculo': tipo_veiculo, 'lista_marcas': resposta})

def modelos_marca(request):

    # dados do formulário
    tipo_veiculo = request.POST.get('tipo_veiculo')
    id_marca = request.POST.get('id_marca')
    nome_marca = request.POST.get('nome_marca')     
    
    resposta = consulta_modelos(tipo_veiculo=tipo_veiculo, id_marca=id_marca)['modelos']
    
    return render(request, 'modelos.html', {'lista_modelos': resposta,'tipo_veiculo': tipo_veiculo, 'id_marca': id_marca, 'nome_marca': nome_marca})

def anos_modelo(request):
    tipo_veiculo = request.POST.get("tipo_veiculo")
    id_marca = request.POST.get("id_marca")
    nome_modelo = request.POST.get("nome_modelo") # Somente para renderizar no titulo do template
    id_modelo = request.POST.get("id_modelo")
    
    resposta = consulta_anos_modelo(tipo_veiculo=tipo_veiculo, id_marca=id_marca, id_modelo=id_modelo)


    return render(request, "anos_modelo.html", {'tipo_veiculo': tipo_veiculo, 'nome_modelo': nome_modelo,'id_modelo': id_modelo,'id_marca': id_marca,'lista_anos_modelo': resposta})

def valor_ano_modelo(request):
    tipo_veiculo = request.POST.get("tipo_veiculo")
    id_marca = request.POST.get("id_marca")
    id_modelo = request.POST.get("id_modelo")
    id_ano = request.POST.get("id_ano")
    
    
    resposta = consulta_valor_ano_modelo(tipo_veiculo=tipo_veiculo, id_marca=id_marca, id_modelo=id_modelo, id_ano=id_ano)

    
    return render(request, "valor_ano_modelo.html", resposta)
