from django.db import models

# Create your models here.
class AutorDB(models.Model):
    nombre = models.CharField(max_length=75, verbose_name="Nombre")
    fecha_naciemiento = models.DateField(verbose_name="Fecha Nacimiento", null=False, blank=False)
    fecha_fallecimiento = models.DateField(verbose_name="Fecha Fallecimiento", null=True, blank=True)
    profesion = models.CharField(verbose_name="Profesion", max_length=50)
    nacionalidad = models.CharField(verbose_name="Nacionalidad", max_length=50)

    class Meta:
        db_table = "Autores"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self) -> str:
        return self.nombre


class FraseDB(models.Model):
    cita = models.TextField(verbose_name="Cita", max_length=400)
    autor_fk = models.ForeignKey(AutorDB, on_delete=models.CASCADE)