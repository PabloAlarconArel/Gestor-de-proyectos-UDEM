from django.db import models

# Create your models here.

class Escuela(models.Model):
    nombre=models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre de Escuela')
    direccion=models.CharField(max_length=100, null=True, blank=True, verbose_name='Dirección de Escuela')
    correo = models.EmailField(max_length=100, null=True , blank=True , verbose_name='Correo')
    telefono = models.CharField(max_length=50, null=True, blank=True, verbose_name='Teléfono')
    estado=models.CharField(max_length=100, null=True, blank=True, default='Activado')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha Actualización')

    class Meta:
        verbose_name = 'Escuela'
        verbose_name_plural = 'Escuelas'
        ordering = ['nombre']   
    def __str__(self):
        return self.nombre