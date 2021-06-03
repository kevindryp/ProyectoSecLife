from django.contrib import admin
from requests.models import Request

class RequestAdmin(admin.ModelAdmin):
    list_display = ('id_request','date','applicant','pet','site','state','comments','is_active')

admin.site.register(Request,RequestAdmin)
