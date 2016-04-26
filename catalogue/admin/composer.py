from django.contrib import admin
from catalogue.models.composer import Composer


@admin.register(Composer)
class ComposerAdmin(admin.ModelAdmin):
    pass
