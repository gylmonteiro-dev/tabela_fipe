from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='pagina-incial'),
    path("marcas/", views.marcas_veiculos, name='marcas'),
    path("modelos/", views.modelos_marca ,name='modelos'),
    path("anos/",views.anos_modelo, name='anos'),
    path("valor/", views.valor_ano_modelo, name='valor-veiculo')
    ]
