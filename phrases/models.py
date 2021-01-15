from django.db import models
from dictionaries.models import Dictionary
from themes.models import Theme
from languages.models import Language


class Phrase(models.Model):
    dictionary = models.ForeignKey(Dictionary, related_name='phrases', on_delete=models.CASCADE)
    themes = models.ManyToManyField(Theme, related_name='phrases')
    extra = models.JSONField(null=True)


class PhraseTranslation(models.Model):
    phrase = models.ForeignKey(Phrase, related_name='phrase_translations', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name='phrase_translations', on_delete=models.CASCADE)
    extra = models.JSONField(null=False)
