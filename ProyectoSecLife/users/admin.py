from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','last_name','is_staff','is_admin','is_superuser')


admin.site.register(User, UserAdmin)
# Register your models here.
