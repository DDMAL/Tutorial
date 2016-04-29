from rest_framework.generics import ListAPIView, RetrieveAPIView
from catalogue.models.source import Source
from catalogue.serializers.website.source import SourceSerializer


class SourceListView(ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class SourceDetailView(RetrieveAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

