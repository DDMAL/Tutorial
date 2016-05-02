from django.db.models import signals
from catalogue.signals.source_signals import index_source
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from model_mommy import mommy

from catalogue.models.source import Source


class SourceViewTest(APITestCase):
    def setUp(self):
        signals.post_save.disconnect(index_source, sender=Source)

        self.source = mommy.make("catalogue.Source")
        self.archive = mommy.make("catalogue.Archive")
        self.source.archive = self.archive
        self.source.save()

    def test_fetches_html_detail_with_success(self):
        url = reverse('source-detail', kwargs={"pk": self.source.pk})
        response = self.client.get(url, HTTP_ACCEPT="text/html")
        content_type = response['Content-Type'].split(";")[0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content_type, 'text/html')
        self.assertTrue(response.content.startswith(b'<'))

    def test_fetches_json_detail_with_success(self):
        url = reverse('source-detail', kwargs={"pk": self.source.pk})
        response = self.client.get(url, HTTP_ACCEPT="application/json")
        content_type = response['Content-Type'].split(";")[0]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content_type, "application/json")
        self.assertTrue(str(response.data).startswith("{"))

    # Failures, especially not-found failures, should respond with the appropriate status & content type
    def test_fetches_html_detail_with_failure(self):
        url = reverse('source-detail', kwargs={"pk": "123456"})
        response = self.client.get(url, HTTP_ACCEPT="text/html")
        content_type = response['Content-Type'].split(";")[0]

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(content_type, 'text/html')

    def test_fetches_json_detail_with_failure(self):
        url = reverse('source-detail', kwargs={"pk": "123456"})
        response = self.client.get(url, HTTP_ACCEPT="application/json")
        content_type = response['Content-Type'].split(";")[0]

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(content_type, 'application/json')


    def tearDown(self):
        pass
