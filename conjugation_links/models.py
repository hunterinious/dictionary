from django.db import models


class ConjugationLink(models.Model):
    url = models.URLField(max_length=2048, unique=True)
