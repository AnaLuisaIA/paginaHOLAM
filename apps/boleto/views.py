from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

def index_boletos(request):
    return render(request, 'boletos/conciertos.html')

def concierto1(request):
    return render(request, 'boletos/asiecon1.html')

def concierto2(request):
    return render(request, 'boletos/asiecon2.html')

def concierto3(request):
    return render(request, 'boletos/asiecon3.html')

def metodoPago(request):
    return render(request, 'boletos/pagocon2.html')
