from rest_framework.pagination import PageNumberPagination


class AnnouncementSetPagination(PageNumberPagination):
    page_size = 6
