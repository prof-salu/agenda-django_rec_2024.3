from django.shortcuts import render
from contatos.models import Contato


def lista_contatos(request):

    contato = Contato.objects.all

    context = {'contatos': contato}
    return render(request, 'contato/lista_contatos.html', context)
