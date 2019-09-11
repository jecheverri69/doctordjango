from django.db import models

# Create your models here.
class Usuarios(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombres= models.CharField(max_length=50, default='')
    usuario = models.CharField(max_length=45)
    clave = models.CharField(max_length=50)
    ROLES=(
        ('1','empleado'),
        ('2','administrador'),
        ('3','usuario')
    )
    Rol= models.CharField(max_length=1, choices=ROLES, default='1')
    
    #METODOS
    def __str__(self):
        return self.usuario
        
    
    