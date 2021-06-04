from django.db import models


# Create your models here.
class Show(models.Model):
    name = models.TextField()
    description = models.TextField()