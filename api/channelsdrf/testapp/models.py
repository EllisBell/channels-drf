from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
