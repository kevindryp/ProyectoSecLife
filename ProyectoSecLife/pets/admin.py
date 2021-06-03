from django.contrib import admin
from pets.models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ('id_pet','type_pet','name','gender','age','priority','site')

admin.site.register(Pet,PetAdmin)