import os

from django.shortcuts import render
from .models import *


# Create your views here.

def home(request):
    context = {
        'heroshots': [hero.split('.')[0] for hero in os.listdir('tvcrib/static/imgs/heroshots')],
        'categorias': Category.objects.all(),
    }
    return render(request, 'home.html', context=context)
