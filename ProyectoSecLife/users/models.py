
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, username,email,password, name,last_name,is_staff,is_admin, is_superuser, **extra_fields):
        user = self.model(
            username=username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_admin = is_admin,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username,email, name,last_name,password=None, **extra_fields):
        return self._create_user(username,email,password, name,last_name,False,False,False, **extra_fields)

    def create_superuser(self,username, email, name,last_name,password=None, **extra_fields):
        return self._create_user(username, email,password, name,last_name,True,True,True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    name = models.CharField('Nombre', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellido', max_length = 255, blank = True, null = True)
    type_document = models.CharField('Tipo de documento', max_length = 255, blank = True, null = True)
    num_document = models.CharField('Numero de documento', max_length = 255, blank = True, null = True)
    phone_number = models.CharField("Numero de telefono", max_length=255, null = True)
    address = models.CharField("Direccion", max_length=30, null = True)
    site_id = models.IntegerField(default= 0)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'

