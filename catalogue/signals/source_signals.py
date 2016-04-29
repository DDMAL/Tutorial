from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from catalogue.models.source import Source


@receiver(post_save, sender=Source)
def index_source(sender, instance, created, **kwargs):
    print('index source')
    pass


@receiver(post_delete, sender=Source)
def delete_source(sender, instance, **kwargs):
    print('delete source')
    pass

