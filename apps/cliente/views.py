from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView, FormView
from django.core.urlresolvers import reverse_lazy

from apps.cliente.forms import TarjetaForm, EmailForm
from apps.cliente.models import Cliente

class pagoBoletos(FormView):
    form_class=TarjetaForm
    template_name='boletos/pago_boleto.html'
    success_url = reverse_lazy('email_comprobar')

class email(CreateView):
    model = Cliente
    form_class= EmailForm
    template_name = 'boletos/confirmar_correo.html'
    success_url = reverse_lazy('principal')
