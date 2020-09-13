from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class cliente(models.Model):
    id_cliente = models.CharField(max_length=15)
    nombres = models.CharField( max_length=50)
    apellidos = models.CharField( max_length=50)
    direccion = models.CharField( max_length=50) 
    num_telefono = models.IntegerField()
    correo = models.EmailField(max_length=254)
    edad = models.IntegerField()
    estado = models.IntegerField(default= 1 )
    

    class Meta:
        db_table = "tr_cliente"
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return self.nombres




class Especializacion(models.Model):
    especialidad = models.CharField( max_length=50)
    estado = models.IntegerField(default =1 )
    f_creacion = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "tr_especializacion"
        verbose_name = "Especializacion"
        verbose_name_plural = "Especializacions"

    def __str__(self):
        return self.especialidad


class medico(models.Model):
    id_medico = models.CharField(max_length=15)
    id_especialida = models.OneToOneField(Especializacion, on_delete=models.CASCADE)
    nombres = models.CharField( max_length=50)
    apellidos = models.CharField( max_length=50)
    direccion = models.CharField( max_length=100)
    num_telefono = models.IntegerField()
    estado = models.IntegerField(default = 1 )
    f_creacion = models.DateTimeField( auto_now_add=True)

    class Meta:
        db_table = "tr_medico"
        verbose_name = "medico"
        verbose_name_plural = "medicos"

    def __str__(self):
        return self.nombres + ' ' + self.apellidos + ' ' + self.especialidad

class cita(models.Model):
    numero_cita = models.CharField(max_length=100)
    fecha = models.CharField( max_length=100)
    hora = models.CharField( max_length=100)
    cliente_id = models.ForeignKey(cliente, on_delete=models.CASCADE)
    medico_id = models.ForeignKey(medico, on_delete=models.CASCADE)
    estado = models.IntegerField(default = 2)
    class Meta:
        db_table = "tr_citas"
        verbose_name = "cita"
        verbose_name_plural = "citas"

    def __str__(self):
        return self.fecha + ' ' + self.id_cliente


