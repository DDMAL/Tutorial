from django.contrib import admin
from catalogue.models.source import Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass
