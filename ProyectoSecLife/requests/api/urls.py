from django.contrib.auth.models import User
from django.urls import path
from requests.api.api import *

urlpatterns = [
    path('add/',request_add, name = 'añadir_solicitud_api'),
    path('get_list/<int:pk>/',get_requests_user, name = 'obtener_solicitudes_usuario_api'),
    path('cancelar/<int:pk>/',cancelar_request_user, name = 'cancelar_solicitudes_usuario_api'),
    path('programar/<int:pk>/',programar_request_user, name = 'cancelar_solicitudes_usuario_api'),
    path('rechazar/<int:pk>/',rechazar_request_user, name = 'cancelar_solicitudes_usuario_api'),
    path('aceptar/<int:pk>/',aceptar_request_user, name = 'cancelar_solicitudes_usuario_api'),
    path('get_list_all_site/<int:pk>/',get_requests_site_all, name = 'obtener_todas_solicitudes_sitio_api'),
    path('get_list_site/<int:pk>/',get_requests_site, name = 'obtener_solicitudes_sitio_api'),
]


