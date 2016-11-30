from django.db import models

# Create your models here.
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True,null=False,default=1)
    correoElectronico = models.EmailField()
