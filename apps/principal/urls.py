# Python imports


# Django imports
from django.conf.urls import url


# Local imports
from .views import (
    GrupoView,
    IndexView,
    OficinasView,
    TramitesView,
    TramiteView,
)

# Create your tests here.


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='principal'),
    url(r'^grupo/$', GrupoView.as_view(), name='grupo'),
    url(r'^oficinas/$', OficinasView.as_view(), name='oficinas'),
    url(r'^tramites/$', TramitesView.as_view(), name='tramites'),
    url(r'^tramites/(?P<id>\d+)/$', TramiteView.as_view(), name='tramite'),
]
