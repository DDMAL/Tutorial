from django.contrib import admin
from catalogue.models.composition import Composition


@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'composer', 'anonymous')
