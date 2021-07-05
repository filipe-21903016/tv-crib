from django.db import models
import hashlib

# Create your models here.
def get_movie_cover_name(instance, filename):
    return f'{hashlib.sha224(bytes(instance.name, "utf-8")).hexdigest()}/movie_cover.jpg'

def get_card_cover_name(instance, filename):
    return f'{hashlib.sha224(bytes(instance.name, "utf-8")).hexdigest()}/card_cover.jpg'

def get_actor_file_name(instance, filename):
    return f'cast_photos/{hashlib.sha224(bytes(instance.name, "utf-8")).hexdigest()}.jpg'

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CastMember(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(null=True, blank=True, upload_to=get_actor_file_name)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=30)
    castMember = models.ForeignKey(CastMember, on_delete=models.CASCADE, related_name="castMember")

    def __str__(self):
        return self.name


class Show(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=900)
    year = models.IntegerField()
    pg = models.IntegerField(default=None)
    type = models.CharField(max_length=10)
    category = models.ManyToManyField(Category, related_name="shows")
    characters = models.ManyToManyField(Character, related_name="character")
    trailerLink = models.CharField(max_length=250)
    movieCover = models.ImageField(null=True, blank=True, upload_to=get_movie_cover_name)
    cardCover = models.ImageField(null=True, blank=True, upload_to=get_card_cover_name)

    def __str__(self):
        return self.name


class Comentario(models.Model):
    clareza = models.IntegerField()
    rigor = models.IntegerField()
    significancia = models.IntegerField()
    originalidade = models.IntegerField()
    logica = models.IntegerField()
    precisao = models.IntegerField()
    comentario = models.TextField(max_length=500)
    classificacaoGlobal = models.IntegerField()

    def __str__(self):
        return self.comentario


