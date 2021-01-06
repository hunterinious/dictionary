from django.db import models
from users.models import UserProfile


class PersonalDictionary(models.Model):
    user_profile = models.ForeignKey(UserProfile, related_name='dictionaries', on_delete=models.CASCADE)
