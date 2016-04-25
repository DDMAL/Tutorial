from rest_framework.test import APITestCase
from model_mommy import mommy
from catalogue.models.source import Source


class SourceTest(APITestCase):
    def setUp(self):
        pass

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
