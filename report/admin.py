from django.contrib import admin

# Register your models here.

from report import models

admin.site.register(models.NoteModel)
admin.site.register(models.CotationModel)
admin.site.register(models.PeriodModel)
