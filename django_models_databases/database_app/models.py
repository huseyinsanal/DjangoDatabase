from django.db import models

# Create your models here.

class Musician(models.Model):
    name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f"Name: {self.name}, Instrument: {self.instrument}, Age: {self.age}"