from django.urls import path
from cadastro.views import entrou, cadastra_usuario

urlpatterns = [
    #path('', home),
    path('entrou/', entrou, name='entrou'),
    path('', cadastra_usuario, name='cadastrar'),
]
