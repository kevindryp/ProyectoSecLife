from django.contrib.auth.models import User
from django.urls import path
from users.api.api import user_list, user_add, user_delete, user_count, user_change_password, user_list_admin, user_list_staff
from users.views import Login, Logout, UserToken

urlpatterns = [
    path('list/',user_list, name = 'usuario_list_api'),
    path('list_admin/',user_list_admin, name = 'usuario_list_admin_api'),
    path('list_staff/<int:pk>/',user_list_staff, name = 'usuario_list_staff_api'),
    path('count/',user_count, name = 'usuario_cantidad_api'),
    path('add/',user_add, name = 'usuario_add_api'),
    path('delete/<int:pk>/',user_delete, name = 'usuario_delete_api'),
    path('login/',Login.as_view(), name = 'usuario_login_api'),
    path('logout/',Logout.as_view(), name = 'usuario_logout_api'),
    path('validate_token/', UserToken.as_view(), name = 'usuario_validate_api' ),
    path('change_password/<int:pk>/', user_change_password, name = 'usuario_change_api' ),
]


