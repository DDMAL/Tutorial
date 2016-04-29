from rest_framework import serializers
from catalogue.models.source import Source


class SourceSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ('type',
                  'pk',
                  'shelfmark',
                  'name',
                  'start_date',
                  'end_date',
                  'source_type')

    type = serializers.SerializerMethodField()
    pk = serializers.ReadOnlyField()
    source_type = serializers.Field(source='type')

    def get_type(self, obj):
        return self.Meta.model.__name__.lower()

