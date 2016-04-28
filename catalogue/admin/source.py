from django.contrib import admin
from catalogue.models.source import Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('shelfmark', 'name', 'start_date', 'end_date', 'archive')
