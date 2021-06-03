from django.contrib import admin
from sites.models import Site

class SiteAdmin(admin.ModelAdmin):
    list_display = ('id_site','name','administrator','pets_availables')

admin.site.register(Site,SiteAdmin)