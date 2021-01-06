from django.db import models
from personal_dictionaries.models import PersonalDictionary


class Category(models.Model):
    name = models.CharField(max_length=50)
    dictionary = models.ForeignKey(PersonalDictionary, related_name='categories', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'dictionary'],
                                    name='the category name must be unique within the dictionary')
        ]
