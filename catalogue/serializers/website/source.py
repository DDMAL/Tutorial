from rest_framework import serializers
from catalogue.models.source import Source


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
