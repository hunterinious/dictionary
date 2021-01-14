from django.db import models
from dictionaries.models import Dictionary


class Theme(models.Model):
    name = models.CharField(max_length=50)
    dictionary = models.ForeignKey(Dictionary, related_name='themes', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'dictionary'],
                                    name='the theme name must be unique within the dictionary')
        ]
