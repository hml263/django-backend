import uuid

from django.conf import settings
from django.db import models

from useraccount.models import User
# Create your models here.

class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    team_image = models.ImageField(upload_to='uploads/teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def image_url(self):
         return f'{settings.WEBSITE_URL}{self.team_image.url}'