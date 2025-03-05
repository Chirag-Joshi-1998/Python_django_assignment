from django.contrib import admin
from .models import Doctor
# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_dispaly=('id','name','specialty','experience','contact')