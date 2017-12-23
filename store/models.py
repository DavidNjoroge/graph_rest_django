from django.db import models

# Create your models here.
class Invetory(models.Model):
    category = models.CharField(max_length=100)
    price = models.FloatField()
    stocked = models.BooleanField()
    name = models.CharField(max_length=100)
    