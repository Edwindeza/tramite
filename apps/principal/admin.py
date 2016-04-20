# Python imports


# Django imports
from django.contrib import admin


# Local imports
from .models import Tramites, Oficinas


# Register your models here.
@admin.register(Tramites)
class TramitesAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
    )


@admin.register(Oficinas)
class OficinasAdmin(admin.ModelAdmin):
    ordering = ['nombre']
