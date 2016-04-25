from django.db import models


class Composition(models.Model):
    class Meta:
        app_label = "catalogue"

    name = models.CharField(max_length=64)
    composer = models.ForeignKey("catalogue.Composer")
