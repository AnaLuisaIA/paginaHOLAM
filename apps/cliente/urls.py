from django.conf.urls import url
from apps.cliente.views import pagoBoletos, email

urlpatterns = [
    url(r'^pago$', pagoBoletos.as_view(), name='pago_boletos'),
    url(r'^confirmacion$', email.as_view(), name='email_comprobar'),
]
