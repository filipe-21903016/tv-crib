from django import forms
from django.forms import ModelForm
from .models import Quizz


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'resposta1': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:400px;', 'min': '0'}),
            'resposta2': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'resposta3': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'resposta4': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'resposta5': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'resposta6': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:400px;', 'min': '0'}),
            'resposta7': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'resposta8': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
            'resposta9': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:400px;', 'min': '0'}),
            'resposta10': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:400px;', 'min': '0'}),
            'pontuacao': forms.HiddenInput(attrs={'class': 'form-control', 'style': 'width:400px;'}),
        }

        labels = {
            'nome': 'Nome',
            'resposta1': 'Quando foi feito o filme "Deadpool" ?',
            'resposta2': 'Qual o tipo do filme "Indiana Jones" ?',
            'resposta3': 'Quem foi o ator de "Rick" na série "Rick and Morty" ?',
            'resposta4': 'Qual o tipo do filme "Borat" ?',
            'resposta5': '"James May: Our man in Japan" é um filme ou uma série?',
            'resposta6': 'Qual a restrição de idade da série "The Flash" ?',
            'resposta7': 'Qual o nome do protagonista de "Brooklyn 99" ?',
            'resposta8': 'Qual é o personagem representado por Bradley Cooper em "Sniper Americano" ?',
            'resposta9': 'Quantos filmes possui o nosso site ?',
            'resposta10': 'Quantas filmes/séries de Ficção Científica existem no site ?',
        }
