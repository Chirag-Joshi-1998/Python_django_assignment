from django.contrib import admin
from .models import Doctor
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_dispaly=('name','specialty','experience','contact')
    list_filter = ('specialty', 'availability')
    search_fields = ('name', 'specialty', 'clinic_address')

admin.site.register(Doctor, DoctorAdmin)
