from django.contrib.auth.models import User
from django.urls import path
from sites.api.api import get_site_ad,site_admin_delete, sites_list, change_admin, site_add, get_site_administrator, get_site

urlpatterns = [
    path('list/',sites_list, name = 'sitio_list_api'),
    path('get/<int:pk>/',get_site, name = 'sitio_get_gen_api'),
    path('site/<int:pk>/',get_site_ad, name = 'sitio_get_api'),
    path('administrator/<int:pk>/',get_site_administrator, name = 'sitio_get_api'),
    path('siteValidate/<int:pk>/',site_admin_delete, name = 'sitio_validate_api'),
    path('siteChangeAdmin/',change_admin, name = 'sitio_cambiar_administrador_api'),
    path('create/',site_add, name = 'sitio_cambiar_administrador_api'),
]


