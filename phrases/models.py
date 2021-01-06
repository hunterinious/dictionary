from django.db import models
from personal_dictionaries.models import PersonalDictionary
from categories.models import Category
from themes.models import Theme
from languages.models import Language


class Phrase(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    dictionary = models.ForeignKey(PersonalDictionary, related_name='phrases', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='phrases')
    theme = models.ManyToManyField(Theme, related_name='phrases')
    language = models.ForeignKey(Language, related_name='phrases', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'dictionary', 'language'],
                                    name='the phrase name must be unique within the dictionary and language')
        ]
