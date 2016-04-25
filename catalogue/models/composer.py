from django.db import models


class Composer(models.Model):
    class Meta:
        app_label = "catalogue"

    name = models.CharField(max_length=255)
