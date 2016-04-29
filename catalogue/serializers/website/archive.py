from rest_framework import serializers
from catalogue.models.archive import Archive


class ArchiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Archive
