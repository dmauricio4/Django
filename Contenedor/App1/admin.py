from django.contrib import admin
from .models import AutorDB, FraseDB

# Register your models here.

class AutorAdmin(admin.ModelAdmin):
    fields = ["nombre", " fecha_naciemiento", "fecha_fallecimiento", "profesion", "nacionalidad"]
    list_display = ["nombre", "fecha_naciemiento"]

admin.site.register(AutorDB, AutorAdmin)