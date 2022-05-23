from statistics import mode
from django.db import models

# Create your models here.
class Career(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=2000, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
        default_permissions =  ()
        permissions = (
            ('add_career', 'Agregar Carrera'),
            ('change_career', 'Editar Carrera'),
            ('delete_career', 'Eliminar Carrera'),
            ('view_career', 'Listar Carreras'))

    def __str__(self):
        """Format name career"""
        return '{0}'.format(self.name)


class Semester(models.Model):
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=2000, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True)
    id_career = models.ForeignKey('Career', on_delete=models.CASCADE, null=False)


    class Meta:
        verbose_name = "Semestre"
        verbose_name_plural = "Semestres"
        default_permissions =  ()
        permissions = (
            ('add_semester', 'Agregar Semestre'),
            ('change_semester', 'Editar Semestre'),
            ('delete_semester', 'Eliminar Semestre'),
            ('view_semester', 'Listar Semestre'))

    def __str__(self):
        """Format name career"""
        return '{0}'.format(self.name)


