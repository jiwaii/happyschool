from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Note)
admin.site.register(models.Classe)
admin.site.register(models.ClasseGroup)
admin.site.register(models.Cotation)
admin.site.register(models.Course)
admin.site.register(models.Period)
admin.site.register(models.StudentLevel)
admin.site.register(models.StudentLevelCourse)
admin.site.register(models.ScholarYear)


