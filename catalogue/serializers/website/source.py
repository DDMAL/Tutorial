from rest_framework import serializers
from catalogue.models.source import Source
from catalogue.models.archive import Archive


class SourceArchiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Archive


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    archive = SourceArchiveSerializer()

    class Meta:
        model = Source
