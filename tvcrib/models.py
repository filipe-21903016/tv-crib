from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CastMember(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=20)
    castMember = models.ForeignKey(CastMember, on_delete=models.CASCADE, related_name="castMember")

    def __str__(self):
        return self.name


class Show(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    year = models.IntegerField()
    pg = models.IntegerField(default=None)
    category = models.ManyToManyField(Category, related_name="category")
    character = models.ManyToManyField(Character, related_name="character")
    trailerLink = models.CharField(max_length=250)
    movieCover = models.ImageField(null=True, blank=True)
    cardCover = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

