from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True)
    national_flag = models.ImageField(upload_to='national_flags', null=True, blank=True)
