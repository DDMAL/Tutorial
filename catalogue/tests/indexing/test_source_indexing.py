from django.conf import settings
from django.test import override_settings
from rest_framework.test import APITestCase
from model_mommy import mommy
import pysolr


class TestSourceIndexing(APITestCase):
    @override_settings(SOLR={'SERVER': 'http://localhost:8983/solr/test_catalogue/'})
    def setUp(self):
        self.server = pysolr.Solr(settings.SOLR['SERVER'])
        # empty solr before every run.
        # self.server.delete(q="*:*")

    @override_settings(SOLR={'SERVER': 'http://localhost:8983/solr/test_catalogue/'})
    def test_solr_index_on_create(self):
        # Should create a source object *and* store it in Solr
        source = mommy.make("catalogue.Source", _fill_optional=['name'])

        # check to see if it made it to solr...
        q = self.server.search("*:*", fq=["type:source", "pk:{0}".format(source.pk)])
        # ensure that more than one record was returned
        self.assertTrue(q.hits > 0)

    @override_settings(SOLR={'SERVER': 'http://localhost:8983/solr/test_catalogue/'})
    def test_solr_delete_on_delete(self):
        source = mommy.make("catalogue.Source", _fill_optional=['name'])
        source_pk = source.pk
        fq = ["type:source", "pk:{0}".format(source_pk)]
        q = self.server.search("*:*", fq=fq)
        self.assertTrue(q.hits > 0)

        # on delete the signal should remove the record from solr
        source.delete()
        q = self.server.search("*:*", fq=fq)
        self.assertTrue(q.hits == 0)

    @override_settings(SOLR={'SERVER': 'http://localhost:8983/solr/test_catalogue/'})
    def test_solr_index_on_update(self):
        source = mommy.make("catalogue.Source", _fill_optional=['name'])
        source_pk = source.pk
        fq = ["type:source", "pk:{0}".format(source_pk)]

        # Check that the name is *not* the source_name. (name will be randomly generated from model mommy)
        source_name = "foo"
        q = self.server.search("*:*", fq=fq)
        self.assertTrue(q.hits > 0)
        self.assertFalse(q.docs[0].get('name_s') == source_name)

        # Change the name and trigger a save. This should update the index.
        source.name = source_name
        source.save()
        q = self.server.search("*:*", fq=fq)
        self.assertTrue(q.docs[0]['name_s'] == source_name)

    def tearDown(self):
        pass
