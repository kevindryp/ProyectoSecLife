from django.db import models
from django.db.models.fields import DateField
from sites.models import Site

class Pet(models.Model):
    id_pet = models.AutoField(primary_key=True)
    type_pet = models.IntegerField('Tipo de mascota', blank = True, null = True)
    name = models.CharField('Nombre', max_length = 255, blank = True, null = True)
    gender = models.CharField('Genero', max_length = 255, blank = True, null = True)
    breed =  models.CharField('Raza', max_length = 255, blank = True, null = True)
    age =  models.IntegerField('Edad', blank = True, null = True)
    size= models.CharField('Tamaño',max_length = 30, blank = True, null = True)
    color = models.CharField('Color', max_length = 20, blank = True, null = True)
    weight =models.DecimalField('Peso',max_digits=5, decimal_places=1, blank = True, null = True)
    personality =  models.CharField('Personalidad', max_length = 100, blank = True, null = True)
    description =  models.TextField('Descripcion', max_length = 255, blank = True, null = True)
    priority = models.IntegerField('Prioridad', blank = True, null = True)
    url_image = models.URLField('URL')
    is_adopted = models.BooleanField('Esta adoptado?',default=False)
    site = models.ForeignKey(Site,on_delete=models.CASCADE, verbose_name = 'Ubicación')
    discapacity = models.CharField('Discapacidad', max_length=40 ,default="Ninguna" )
    
    class Meta:
        ordering = ["priority","-age"]
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

    def __str__(self):
        return f'{self.type_pet} {self.name}'


