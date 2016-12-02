from django.conf.urls import url
from apps.boleto.views import index_boletos,concierto1,concierto2,concierto3, metodoPago

urlpatterns = [
    url(r'^$', index_boletos, name='index_boletos'),
    url(r'^forma_pago$', metodoPago, name='forma_de_pago'),
    url(r'^primer_concierto$', concierto1, name='boleto_agregar1'),
    url(r'^segundo_concierto$', concierto2, name='boleto_agregar2'),
    url(r'^tercer_concierto$', concierto3 , name='boleto_agregar3'),
    #url(r'^modificar/(?P<pk>\d+)/$', ProductoUpdate.as_view(), name='producto_modificar'),
    #url(r'^eliminar/(?P<pk>\d+)/$', ProductoDelete.as_view(), name='producto_eliminar'),
]
