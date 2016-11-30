from django import forms
from apps.boleto.models import Boleto

class Boleto1Form(forms.ModelForm):
    class Meta:
        model=Boleto

        fields=[
        'asiento1',
        ]
        labels={
        'asiento1': 'Escoger asiento',
        }
        widgets={
        'asiento1': forms.Select(attrs={}),
        }

class Boleto2Form(forms.ModelForm):
    class Meta:
        model=Boleto

        fields=[
        'asiento2',
        ]
        labels={
        'asiento2': 'Escoger asiento',
        }
        widgets={
        'asiento2': forms.Select(attrs={}),
        }

class Boleto3Form(forms.ModelForm):
    class Meta:
        model=Boleto

        fields=[
        'asiento3',
        ]
        labels={
        'asiento3': 'Escoger asiento',
        }
        widgets={
        'asiento3': forms.Select(attrs={}),
        }
