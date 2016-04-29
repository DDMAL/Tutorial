from django.db.models import signals
from catalogue.signals.source_signals import index_source
from catalogue.models.source import Source
from rest_framework.test import APITestCase
from model_mommy import mommy
from catalogue.serializers.search.source import SourceSearchSerializer


class TestSourceSearchSerializer(APITestCase):
    def setUp(self):
        signals.post_save.disconnect(index_source, sender=Source)
        self.source = mommy.make("catalogue.Source",
                                 shelfmark="MS 123",
                                 name="Foo",
                                 surface="paper",
                                 start_date=14,
                                 end_date=15)

    def test_source_serialization(self):
        serialized = SourceSearchSerializer(self.source)
        self.assertEqual(serialized.data['type'], 'source')
        self.assertEqual(serialized.data['shelfmark'], 'MS 123')
        self.assertIsNone(serialized.data['source_type'])

    def tearDown(self):
        pass

