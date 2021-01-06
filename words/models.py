from django.db import models
from django.utils.translation import gettext_lazy as _
from personal_dictionaries.models import PersonalDictionary
from categories.models import Category
from themes.models import Theme
from languages.models import Language
from conjugation_links.models import ConjugationLink


class Word(models.Model):
    class WordType(models.TextChoices):
        NOUN = 'N', _('Noun')
        VERB = 'V', _('Verb')
        ADJECTIVE = 'A', _('Adjective')

    type = models.CharField(max_length=20, choices=WordType.choices)
    dictionary = models.ForeignKey(PersonalDictionary, related_name='words', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='words')
    theme = models.ManyToManyField(Theme, related_name='words')


class Noun(models.Model):
    singular_name = models.CharField(max_length=50)
    plural_name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, related_name='noun_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='nouns', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['singular_name', 'plural_name', 'language'],
                                    name='the noun singular and plural name must be unique within a language')
        ]


class Verb(models.Model):
    name = models.CharField(max_length=50)
    conjugation_link = models.ForeignKey(ConjugationLink, related_name='verbs', on_delete=models.SET_DEFAULT,
                                         default='https://www.verbformen.ru/sprjazhenie/')
    language = models.ForeignKey(Language, related_name='verb_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='verbs', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'language'],
                                    name='the verb name must be unique within a language')
        ]


class Adjective(models.Model):
    name = models.CharField(max_length=50)
    conjugation_link = models.ForeignKey(ConjugationLink, related_name='adjectives', on_delete=models.SET_DEFAULT,
                                         default='https://www.verbformen.ru/sklonenie/prilagatelnye/')
    language = models.ForeignKey(Language, related_name='adjective_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='adjective', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'language'],
                                    name='the adjective name must be unique within a language')
        ]
