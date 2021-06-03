from django.contrib.auth.models import User
from django.urls import path
from pets.api.api_pets import *

urlpatterns = [
    path('list/',pet_list, name = 'mascota_list_api'),
    path('list/<int:pk>/',pets_list_all, name = 'mascota_list_api'),
    path('listSite/<int:pk>/',pets_list_site, name = 'mascota_list_api'),
    path('count/',pets_count, name = 'mascota_cantidad_api'),
    path('list_dog/',pet_list_dogs, name = 'mascota_list_api'),
    path('list_cat/',pet_list_cats, name = 'mascota_list_api'),
    path('add/',pet_add, name = 'mascota_add_api'),
    path('edit/<int:pk>/',pet_edit, name = 'mascota_edit_api'),
    path('delete/<int:pk>/',pet_adopt, name = 'mascota_delete_api'),
    path('pet/<int:pk>/',get_pet, name = 'mascota_get_api'),
    path('count_site/<int:pk>/',pet_count_site, name = 'mascota_cantidad_sitio_api'),
]


