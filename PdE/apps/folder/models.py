from django.db import models

from apps.career.models import Semester

class Folder(models.Model):
    name = models.CharField(max_length=500)
    link = models.CharField(max_length=3000)
    description = models.CharField(max_length=2000, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True)
    id_semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=False)


    class Meta:
        verbose_name = "Carpeta"
        verbose_name_plural = "Carpetas"
        default_permissions =  ()
        permissions = (
            ('add_folder', 'Agregar Carpeta'),
            ('change_folder', 'Editar Carpeta'),
            ('delete_folder', 'Eliminar Carpeta'),
            ('view_folder', 'Listar Carpetas'))

    def __str__(self):
        """Format name folder"""
        return '{0}'.format(self.name)
