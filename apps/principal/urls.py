from django.conf.urls import url
from apps.principal.views import index, mostrar_grafo

urlpatterns = [
    url(r'^$', index,name='principal'),
    url(r'^grafo$', mostrar_grafo,name='grafo'),
]
