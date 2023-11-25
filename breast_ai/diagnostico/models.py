from django.db import models

class Predicao(models.Model):
    campo1 = models.FloatField()
    campo2 = models.FloatField()
    campo3 = models.FloatField()
    campo4 = models.FloatField()
    campo5 = models.FloatField()
    resultado = models.CharField(max_length=255)
