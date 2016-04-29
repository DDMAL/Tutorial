from django.conf import settings
from rest_framework.test import APITestCase
from model_mommy import mommy
import pysolr


class TestSourceIndexing(APITestCase):
    def setUp(self):
        self.server = pysolr.Solr(settings.SOLR['SERVER'])

    def test_solr_index_on_create(self):
        # Should create a source object *and* store it in Solr
        source = mommy.make("catalogue.Source")

        # check to see if it made it to solr...
        q = self.server.search("*:*", fq=["type:source", "pk:{0}".format(source.pk)])
        # ensure that more than one record was returned
        self.assertTrue(q.hits > 0)

    def test_solr_delete_on_delete(self):
        pass

    def tearDown(self):
        pass
