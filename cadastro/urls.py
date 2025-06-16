from django.urls import path
from cadastro.views import entrou, cadastra_usuario, excluir_usuario, editar_usuario

urlpatterns = [
    #path('', home),
    path('entrou/', entrou, name='entrou'),
    path('', cadastra_usuario, name='cadastrar'),
    path('excluir/<int:id>/', excluir_usuario, name='excluir_usuario'),  
    path('editar/<int:id>/', editar_usuario, name='editar_usuario'),
]
