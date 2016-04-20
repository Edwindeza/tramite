# Python imports


# Django imports
from django.views.generic.base import TemplateView


# Local imports
from .models import Oficinas, Tramites


# Create your views here.
class IndexView(TemplateView):
    template_name = 'principal/index.html'


class GrupoView(TemplateView):
    template_name = 'principal/grupo.html'


class OficinasView(TemplateView):
    template_name = 'principal/oficinas.html'

    def get_context_data(self, **kwargs):
        oficinas = Oficinas.objects.all()
        contexto = {'oficinas': oficinas}
        return contexto


class TramitesView(TemplateView):
    template_name = 'principal/tramites.html'

    def get_context_data(self, **kwargs):
        tramites = Tramites.objects.all()
        contexto = {'tramites': tramites}
        return contexto


class TramiteView(TemplateView):
    template_name = 'principal/tramite.html'

    def get_context_data(self, **kwargs):
        tramite = Tramites.objects.get(id=self.kwargs['id'])
        contexto = {'tramite': tramite}
        return contexto
