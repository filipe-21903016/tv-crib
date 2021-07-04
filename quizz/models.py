from django.db import models


# Create your models here.

class Quizz(models.Model):
    nome = models.CharField(max_length=20)
    resposta1 = models.IntegerField()
    resposta2 = models.CharField(max_length=20)
    resposta3 = models.CharField(max_length=20)
    resposta4 = models.CharField(max_length=20)
    resposta5 = models.CharField(max_length=20)
    resposta6 = models.IntegerField()
    resposta7 = models.CharField(max_length=20)
    resposta8 = models.CharField(max_length=20)
    resposta9 = models.IntegerField()
    resposta10 = models.IntegerField()
    pontuacao = models.IntegerField()

    def __str__(self):
        return self.nome

