import csv
from django.core.management.base import BaseCommand
from catalogue.models.source import Source
from catalogue.models.archive import Archive
from catalogue.models.composer import Composer
from catalogue.models.composition import Composition


class Command(BaseCommand):

    def _get_source(self, row):
        source, created = Source.objects.get_or_create(shelfmark=row['shelfMark'])

        # fill out the record and save it
        if created:
            if row['sourceName']:
                source.name = row['sourceName']
            if row['startdate']:
                source.start_date = row['startdate']
            if row['enddate']:
                source.end_date = row['enddate']
            if row['sourceType']:
                source.type = row['sourceType']
            if row['dateComments']:
                source.date_comments = row['dateComments']
            if row['surface']:
                source.surface = row['surface']
            source.save()

        return source

    def _get_archive(self, row):
        archive, created = Archive.objects.get_or_create(siglum=row['siglum'])

        if created:
            if row['archiveCity']:
                archive.city = row['archiveCity']
            if row['archiveCountry']:
                archive.country = row['archiveCountry']
            if row['archiveName']:
                archive.name = row['archiveName']
            archive.save()

        return archive

    def _get_composer(self, row):
        composer, created = Composer.objects.get_or_create(name=row['composer'])
        return composer

    def _get_composition(self, row):
        composition, created = Composition.objects.get_or_create(title=row['composition_name'])
        return composition

    def handle(self, *args, **options):
        with open('diamm_excerpt.csv', 'r') as csvfile:
            contents = csv.DictReader(csvfile)
            for row in contents:
                print(row)
                anonymous = False
                if row['composer'] == 'no composer/anon':
                    anonymous = True

                source = self._get_source(row)
                archive = self._get_archive(row)

                if not source.archive:
                    # The archive for this source has not been set.
                    source.archive = archive
                    source.save()

                # every row should contain a unique composition
                composition = self._get_composition(row)

                if not anonymous and composition.composer is None:
                    # if the piece is not anonymous but the composer has not been set.
                    composer = self._get_composer(row)
                    composition.composer = composer
                elif anonymous and composition.anonymous is False:
                    # if the piece is anonymous but the composition record has false for the value of anonymous
                    composition.anonymous = True
                else:
                    # corner case: if we've seen the piece before (unlikely)
                    continue

                composition.save()








