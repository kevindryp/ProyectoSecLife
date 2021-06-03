from django.db import models
from users.models import User
from pets.models import Pet
from sites.models import Site

class Request(models.Model):
    id_request = models.AutoField(primary_key=True)
    date = models.DateField(auto_now=False, auto_now_add=True)
    applicant = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name = 'Solicitante')
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE, verbose_name = 'Mascota')
    site = models.ForeignKey(Site,on_delete=models.CASCADE, verbose_name = 'Sitio')
    state = models.CharField('Estado', max_length = 255, blank = True, null = True, default="Pendiente")
    comments = models.CharField('Comentarios', max_length = 255, blank = True, null = True)
    is_active = models.BooleanField('Esta activa?',default=True)
 
    class Meta:
        ordering = ["-date",]
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'

    def __str__(self):
        return f'{self.date} {self.applicant}'



