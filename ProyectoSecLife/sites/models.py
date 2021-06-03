from django.db import models
from users.models import User


class Site(models.Model):
    id_site = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length = 255, blank = True, null = True)
    location = models.CharField('Localidad',max_length = 30, blank = True, null = True)
    address = models.CharField('Direccion',max_length = 30, blank = True, null = True)
    phone_number = models.CharField('Número telefonico',max_length = 15, blank = True, null = True)
    administrator = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name = 'Administrador')
    pets_availables = models.IntegerField('Mascotas disponibles', blank = True, null = True)
    
    class Meta:
        verbose_name = 'Sitio de adopción'
        verbose_name_plural = 'Sitios de adopción'

    def __str__(self):
        return f' {self.name}'