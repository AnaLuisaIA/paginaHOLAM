from django import forms
from apps.cliente.models import Cliente
from captcha.fields import ReCaptchaField

class EmailForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields=[
        'correoElectronico',
        ]
        labels={
        'correoElectronico': 'Correo electrónico',
        }
        widgets={
        'correoElectronico': forms.EmailInput(attrs=None),
        }


class TarjetaForm(forms.Form):
    tarjeta = forms.RegexField(
        regex=r'^\d{16}$',
        error_messages= {'invalid' : ("La tarjeta debe contar con 16 dígitos"), 'required':("El número de tarjeta es necesario")},
        required=True, label="Número de Tarjeta")
    cod_seguridad = forms.RegexField(
        regex=r'^\d{3}$',
        error_messages={'invalid': ("Número de seguridad debe de ser de 3 dígitos"), 'required':("El código de seguridad es necesario")},
        required=True, label="Código de Seguridad")
    captcha = ReCaptchaField(attrs={'theme' : 'clean'},error_messages={'required': ("CAPTCHA es necesario")}, label="")
