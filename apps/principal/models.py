# Python imports


# Django imports
from django.db import models


# Local imports


# Create your models here.
class Oficinas(models.Model):
    nombre = models.CharField(
        max_length=100,
        verbose_name="Nombre de la oficina"
        )

    class Meta:
        verbose_name = "Oficina"

    def __str__(self):
        return self.nombre


class Tramites(models.Model):
    oficinas = models.ManyToManyField(Oficinas)
    nombre = models.CharField(
        max_length=100,
        verbose_name='Nombre del trámite'
        )
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now=True)
    descripcion = models.TextField(verbose_name="Descripción del trámite")

    class Meta:
        verbose_name = "Trámite"
        verbose_name_plural = "Trámites"

    def __str__(self):
        return self.nombre
