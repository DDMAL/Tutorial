from django.db import models


class Composition(models.Model):
    class Meta:
        app_label = "catalogue"

    title = models.CharField(max_length=64)
    composer = models.ForeignKey("catalogue.Composer", blank=True, null=True)
    anonymous = models.BooleanField(default=False)

    def __str__(self):
        return "{0}".format(self.title)
