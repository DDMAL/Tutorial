from django.db import models


class Archive(models.Model):
    class Meta:
        app_label = "catalogue"

    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    siglum = models.CharField(max_length=255)
