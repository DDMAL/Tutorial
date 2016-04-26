from django.contrib import admin
from catalogue.models.archive import Archive


@admin.register(Archive)
class ArchiveAdmin(admin.ModelAdmin):
    pass
