from rest_framework.generics import ListAPIView, RetrieveAPIView
from catalogue.models.source import Source
from catalogue.serializers.website.source import SourceSerializer


class SourceListView(ListAPIView):
    template_name = "source/source_list.html"
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class SourceDetailView(RetrieveAPIView):
    template_name = "source/source_detail.html"
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

