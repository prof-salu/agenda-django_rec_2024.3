from django.urls import path
from contatos.views.ContatoView import lista_contatos


urlpatterns = [
    path("", lista_contatos, name='contatos'),
]