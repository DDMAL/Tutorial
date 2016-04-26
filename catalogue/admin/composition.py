from django.contrib import admin
from catalogue.models.composition import Composition


@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    pass
