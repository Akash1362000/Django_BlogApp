from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import AnnouncementViewSet, AnnouncementDetailViewSet

router = DefaultRouter()
router.register(r'announcements', AnnouncementViewSet, basename='announcement-list')
router.register(r'announcement', AnnouncementDetailViewSet, basename='announcement-detail')

urlpatterns = [
    path('', include(router.urls)),
]


