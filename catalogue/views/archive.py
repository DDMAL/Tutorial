from rest_framework.generics import ListAPIView, RetrieveAPIView
from catalogue.models.archive import Archive
from catalogue.serializers.website.archive import ArchiveSerializer


class ArchiveListView(ListAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer


class ArchiveDetailView(RetrieveAPIView):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer
