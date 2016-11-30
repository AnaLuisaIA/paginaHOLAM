from django.conf.urls import url
from apps.boleto.views import index_boletos, pago_boletos \
    BoletoAgregar1, BoletoAgregar2, BoletoAgregar3

urlpatterns = [
    url(r'^$', index_boletos, name='index_boletos'),
    url(r'^pago$', pago_boletos, name='pago_boletos'),
    url(r'^primer_concierto$', BoletoAgregar1.as_view(), name='boleto_agregar1'),
    url(r'^segundo_concierto$', BoletoAgregar2.as_view(), name='boleto_agregar2'),
    url(r'^tercer_concierto$', BoletoAgregar3.as_view(), name='boleto_agregar3'),
    #url(r'^modificar/(?P<pk>\d+)/$', ProductoUpdate.as_view(), name='producto_modificar'),
    #url(r'^eliminar/(?P<pk>\d+)/$', ProductoDelete.as_view(), name='producto_eliminar'),
]
