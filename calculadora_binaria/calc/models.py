from django.db import models

class Calculo(models.Model):
    sentenca = models.CharField(max_length=255)

    def __str__(self):
        return self.sentenca
