from django.db import models

# Create your models here.


class Stand (models.Model):
    localizacao = models.CharField(max_length=150) 
    valor = models.FloatField()

    def __str__(self):
        return self.localizacao

class Reserva(models.Model):
    cnpj = models.CharField(max_length=150) 
    nome_empresa = models.CharField(max_length=150)
    categoria_empresa =  models.CharField(max_length=150)
    quitado = models.BooleanField()
    data = models.DateTimeField(auto_now_add=True)  
    stand = models.ForeignKey(Stand, blank=True, on_delete=models.CASCADE, null=True)

