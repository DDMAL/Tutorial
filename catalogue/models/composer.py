from django.db import models


class Composer(models.Model):
    class Meta:
        app_label = "catalogue"

    name = models.CharField(max_length=255)

    def __str__(self):
        return "{0}".format(self.name)
