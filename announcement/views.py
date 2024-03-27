from rest_framework import viewsets, filters
from rest_framework.response import Response
from .models import Announcement
from .serializers import AnnouncementSerializers
from .pagination import AnnouncementSetPagination
from django.shortcuts import get_object_or_404


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializers
    pagination_class = AnnouncementSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  


class AnnouncementDetailViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Announcement.objects.all()
        announcement = get_object_or_404(queryset, pk=pk)
        serializer = AnnouncementSerializers(announcement)
        return Response(serializer.data)
