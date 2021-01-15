from django.db import models
from django.utils.translation import gettext_lazy as _
from dictionaries.models import Dictionary
from themes.models import Theme
from languages.models import Language


class PartOfSpeech(models.TextChoices):
    NOUN = 'N', _('Noun')
    VERB = 'V', _('Verb')
    ADJECTIVE = 'Adj', _('Adjective')
    ADVERB = 'Adv', _('Adverb')
    NUMERAL = 'Num', _('Numeral')
    PREPOSITION = 'Prep', _('Preposition')
    PRONOUN = 'Pron', _('Pronoun')
    UNION = 'U', _('Union')
    PARTICLE = 'Part', _('Particle')
    ARTICLE = 'Art', _('Article')


class Word(models.Model):
    dictionary = models.ForeignKey(Dictionary, related_name='words', on_delete=models.CASCADE)
    themes = models.ManyToManyField(Theme, related_name='words')
    extra = models.JSONField(null=True)


class WordTranslation(models.Model):
    part_of_speech = models.CharField(max_length=30, choices=PartOfSpeech.choices)
    word = models.ForeignKey(Word, related_name='word_translations', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name='word_translations', on_delete=models.CASCADE)
    extra = models.JSONField(null=False)

