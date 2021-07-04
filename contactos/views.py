from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Contacto


# Create your views here.

def lista(request):
    return render(request, 'lista.html', {'contactos': Contacto.objects.all()})


def add(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    if request.method == 'POST':
        nome = request.POST['nome']
        apelido = request.POST['apelido']
        telefone = request.POST['telefone']
        email = request.POST['email']
        birthday = request.POST['birthday']
        contacto = Contacto(nome=nome, apelido=apelido, telefone=telefone, email=email, data_nascimento=birthday)
        contacto.save()
        return HttpResponseRedirect(reverse('contactos:lista'))

    return render(request, "add.html", context={})


def edit(request, contacto_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    contacto = Contacto.objects.get(pk=contacto_id)

    if request.method == 'POST':
        contacto.nome = request.POST['nome']
        contacto.apelido = request.POST['apelido']
        contacto.telefone = request.POST['telefone']
        contacto.email = request.POST['email']
        contacto.data_nascimento = request.POST['birthday']
        contacto.save()
        return HttpResponseRedirect(reverse('contactos:lista'))

    return render(request, 'edit.html', {'contacto_id': contacto_id})


def remove(request, contacto_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))

    contacto = Contacto.objects.get(pk=contacto_id)
    Contacto.delete(contacto)
    return HttpResponseRedirect(reverse('contactos:lista'))
