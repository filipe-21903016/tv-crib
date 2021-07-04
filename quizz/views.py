from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import QuizzForm


# Create your views here.
def getPontuacao(respostas):
    valid_answers = [2016, "ação", "justin roiland", "comédia", "série", 12, "jake peralta", "chris kyle", 12, 5]
    pontuacao = 0

    for r, a in zip(respostas, valid_answers):
        r = str(r).lower() if type(a) == str else r
        if r == a:
            pontuacao += 10
    return pontuacao


def quizz(request):
    form = QuizzForm(request.POST or None)
    if form.is_valid():
        respostas = [
            form.cleaned_data.get('resposta1'),
            form.cleaned_data.get('resposta2'),
            form.cleaned_data.get('resposta3'),
            form.cleaned_data.get('resposta4'),
            form.cleaned_data.get('resposta5'),
            form.cleaned_data.get('resposta6'),
            form.cleaned_data.get('resposta7'),
            form.cleaned_data.get('resposta8'),
            form.cleaned_data.get('resposta9'),
            form.cleaned_data.get('resposta10'),
        ]
        pontuacao = getPontuacao(respostas)
        form.pontuacao = pontuacao
        form.save()
        return render(request, 'quizz.html', {'form': form, 'resultado': pontuacao})

    return render(request, 'quizz.html', {'form': form})
