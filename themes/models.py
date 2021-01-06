from django.db import models
from personal_dictionaries.models import PersonalDictionary


class Theme(models.Model):
    name = models.CharField(max_length=50)
    dictionary = models.ForeignKey(PersonalDictionary, related_name='themes', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'dictionary'],
                                    name='the theme name must be unique within the dictionary')
        ]
