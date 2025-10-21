
from django.db import models

class Reservering(models.Model):
    naam = models.CharField(max_length=100)
    email = models.EmailField()
    datum = models.DateField()

    def __str__(self):
        return self.naam

