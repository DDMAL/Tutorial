from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.source import Source
from catalogue.serializers.search.source import SourceSearchSerializer
from catalogue.helpers.solr_helpers import solr_index, solr_delete


@receiver(post_save, sender=Source)
def index_source(sender, instance, created, **kwargs):
    solr_index(SourceSearchSerializer, [instance])


@receiver(post_delete, sender=Source)
def delete_source(sender, instance, **kwargs):
    solr_delete([instance])


