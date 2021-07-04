import os

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *


# Create your views here.

def home(request):
    context = {
        'heroshots': [hero.split('.')[0] for hero in os.listdir('tvcrib/static/imgs/heroshots')],
        'categorias': Category.objects.all(),
    }
    return render(request, 'home.html', context=context)


def show(request, show_id):
    show = Show.objects.get(pk=show_id)
    categorias = show.category.all()

    context = {
        'show': show,
        'categoria': categorias[0],
        'pk': str(show.pk),
    }
    return render(request, 'show.html', context=context)


def all_movies(request):
    context = {
        'shows': Show.objects.filter(type='movie')
    }
    return render(request, 'show-grid.html', context)


def all_series(request):
    context = {
        'shows': Show.objects.filter(type='series')
    }
    return render(request, 'show-grid.html', context)


def about(request):
    return render(request, 'about.html')


def comentarios(request):
    if request.method == 'POST':
        clareza = request.POST['cla']
        rigor = request.POST['ri']
        significancia = request.POST['sig']
        originalidade = request.POST['ori']
        logica = request.POST['log']
        precisao = request.POST['preci']
        classificacao = request.POST['global']
        comentario = request.POST['comment']

        comment_form = Comentario(clareza=clareza, rigor=rigor,
                                  significancia=significancia, originalidade=originalidade,
                                  logica=logica, precisao=precisao, classificacaoGlobal=classificacao,
                                  comentario=comentario)
        comment_form.save()
        return render(request, "comentarios.html", {'comments': Comentario.objects.all()})

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    return render(request, "comentarios.html", {'comments': Comentario.objects.all()})
