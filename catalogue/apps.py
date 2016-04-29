from django.apps import AppConfig


class CatalogueConfig(AppConfig):
    name = "catalogue"

    def ready(self):
        import catalogue.signals
