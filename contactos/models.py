from django.db import models


# Create your models here.
class Contacto(models.Model):
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    data_nascimento = models.DateField()

    def __str__(self):
        return f'{self.nome} {self.apelido}'
