from rest_framework import serializers
from .models import Announcement


class AnnouncementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
