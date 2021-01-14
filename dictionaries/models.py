from django.db import models
from users.models import UserProfile


class Dictionary(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='dictionaries', on_delete=models.CASCADE)
