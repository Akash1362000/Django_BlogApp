from django.db import models

# Create your models here.
class Announcement(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='announcement_images/', null=True, blank=True)

    def __str__(self):
        return self.title
