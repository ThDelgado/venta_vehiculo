from django.contrib import admin
from .models import Vehiculo
# Register your models here.


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['marca']
    search_fields = ['serial_carroceria' ] #filtro 
    ordering = ['marca']


