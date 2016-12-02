from django.db import models
from apps.cliente.models import Cliente

# Create your models here.
class Boleto(models.Model):
    idBoleto = models.AutoField(primary_key=True)
    #asiento = models.TextField(max_length=6)
    asientos1 = (
    ('a1','A1'),
    ('a2','A2'),
    ('a3','A3'),
    ('a4','A4'),
    ('a5','A5'),
    ('a6','A6'),
    ('a7','A7'),
    ('a8','A8'),
    ('a9','A9'),
    ('b5','B5'),
    ('b6','B6'),
    ('b7','B7'),
    ('b8','B8'),
    ('b9','B9'),
    ('b10','B10'),
    )
    asiento1= models.CharField(max_length=3, choices=asientos1)

    asientos2 = (
    ('2016-1','2016-1'),
    ('2016-2','2016-2'),
    ('2016-3','2016-3'),
    ('2016-4','2016-4'),
    ('2016-5','2016-5'),
    ('2016-6','2016-6'),
    ('2016-7','2016-7'),
    ('2016-8','2016-8'),
    ('2016-9','2016-9'),
    ('2016-10','2016-10'),
    ('2016-11','2016-11'),
    ('2016-12','2016-12'),
    ('2016-13','2016-13'),
    ('2016-14','2016-14'),
    )
    asiento2= models.CharField(max_length=6, choices=asientos2)

    asientos3 = (
        ('e21','E21'),
        ('e22','E22'),
        ('e23','E23'),
        ('e24','E24'),
        ('e25','E25'),
        ('e26','E26'),
        ('e27','E27'),
        ('e28','E28'),
        ('e29','E29'),
        ('k01','K01'),
        ('k02','K02'),
        ('k03','K03'),
        ('k04','K04'),
        ('k05','K05'),
        )
    asiento3= models.CharField(max_length=3, choices=asientos3)

class Compra(models.Model):
    id_boleto= models.ForeignKey(Boleto,on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
