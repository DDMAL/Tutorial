from django.db import models


class Source(models.Model):
    class Meta:
        app_label = "catalogue"

    shelfmark = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    surface = models.CharField(max_length=128, blank=True, null=True)
    start_date = models.IntegerField(blank=True, null=True)
    end_date = models.IntegerField(blank=True, null=True)
    date_comments = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=128, blank=True, null=True)
    archive = models.ForeignKey("catalogue.Archive", blank=True, null=True)

    def __str__(self):
        return self.display_name

    @property
    def display_name(self):
        if self.name:
            return "{0} ({1})".format(self.shelfmark, self.name)
        else:
            return "{0}".format(self.shelfmark)
