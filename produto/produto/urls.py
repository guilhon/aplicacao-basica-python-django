from django.contrib import admin
from django.urls import path
from meus_produtos.views import lista_produtos, cadastra_produtos, editar_produtos, excluir_produtos

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', lista_produtos, name='listagem'),
    path('cadastra_produtos/', cadastra_produtos),
    path('cadastra_produtos/<int:id>', editar_produtos, name='editar'),
    path('/<int:id>', excluir_produtos, name='excluir'),
]

