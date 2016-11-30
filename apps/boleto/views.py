from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from apps.boleto.forms import Boleto1Form, Boleto2Form, Boleto3Form
from apps.boleto.models import Boleto
# Create your views here.

def index_boletos(request):
    return render(request, 'boletos/conciertos.html')

def pago_boletos(request):
    return render(request, 'boletos/pago_boleto.html')

class BoletoAgregar1(CreateView):
    model = Boleto
    form_class= Boleto1Form
    template_name= 'boletos/elegir_asientos.html'
    #success_url= reverse_lazy('index_productos')

class BoletoAgregar2(CreateView):
    model = Producto
    form_class= ProductoForm
    template_name= 'boletos/elegir_asientos.html'
    #success_url= reverse_lazy('index_productos')

class BoletoAgregar3(CreateView):
    model = Producto
    form_class= ProductoForm
    template_name= 'boletos/elegir_asientos.html'
    #success_url= reverse_lazy('index_productos')
