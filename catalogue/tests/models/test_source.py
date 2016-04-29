from django.db.models import signals
from catalogue.signals.source_signals import index_source
from catalogue.models.source import Source
from rest_framework.test import APITestCase
from model_mommy import mommy


class SourceTest(APITestCase):
    def setUp(self):
        signals.post_save.disconnect(index_source, sender=Source)

    def test_display_name_shelfmark_only(self):
        shelfmark = "Q. 123"
        source = mommy.make("catalogue.Source",
                            shelfmark=shelfmark)

        self.assertEqual(source.display_name, shelfmark)

    def test_display_name_with_name(self):
        shelfmark = "Q. 123"
        name = "Lorem Ipsum"
        source = mommy.make("catalogue.Source",
                            shelfmark=shelfmark,
                            name=name)

        self.assertEqual(source.display_name, "{0} ({1})".format(shelfmark, name))

    def tearDown(self):
        pass
