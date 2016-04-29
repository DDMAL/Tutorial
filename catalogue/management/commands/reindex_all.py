from django.core.management import BaseCommand
from catalogue.models.source import Source


class Command(BaseCommand):

    def handle(self, *args, **options):
        for s in Source.objects.all():
            print('Indexing: {0}'.format(s.shelfmark))
            s.save()
