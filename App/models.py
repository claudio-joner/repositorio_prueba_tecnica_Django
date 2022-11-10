from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length = 25)
    apellido = models.CharField(max_length = 25)
    correo = models.CharField(max_length = 50)

    def __str__(self) -> str:
        texto = "nombre:{0} apellido:{1} Correo:{2}"
        return texto.format(self.nombre,self.apellido,self.correo)