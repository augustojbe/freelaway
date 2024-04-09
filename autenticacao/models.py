from django.db import models

class usuario(models.Model):
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=6, null=True, blank=True)
    confirmar_senha = models.CharField(max_length=6, null=True, blank=True)
