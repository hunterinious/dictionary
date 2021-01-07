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
    language = models.ForeignKey(Language, related_name='noun_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='nouns', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class RussianNoun(Noun):
    plural_name = models.CharField(max_length=50, null=True, blank=True)
    language = models.ForeignKey(Language, related_name='russian_noun_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='russian_nouns', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['plural_name', 'singular_name', 'language'],
                                    name='the noun singular and plural name must be unique within a russian language')
        ]


class EnglishNoun(Noun):
    plural_name = models.CharField(max_length=50, null=True, blank=True)
    language = models.ForeignKey(Language, related_name='english_noun_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='english_nouns', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['plural_name', 'singular_name', 'language'],
                                    name='the noun singular and plural name must be unique within a english language')
        ]


class GermanNoun(Noun):
    class Gender(models.TextChoices):
        MASCULINE = 'der', _('der')
        FEMININE = 'die', _('die')
        NEUTER = 'das', _('das')

    plural_name = models.CharField(max_length=50)
    singular_article = models.CharField(max_length=3, choices=Gender.choices)
    plural_article = models.CharField(max_length=3, default='die')
    language = models.ForeignKey(Language, related_name='german_noun_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='german_nouns', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['plural_name', 'singular_name', 'language'],
                                    name='the noun singular and plural name must be unique within a german language')
        ]


class Verb(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, related_name='verb_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='verbs', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class RussianVerb(Verb):
    language = models.ForeignKey(Language, related_name='russian_verb_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='russian_verbs', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'language'],
                                    name='the verb name must be unique within a russian language')
        ]


class EnglishVerb(Verb):
    language = models.ForeignKey(Language, related_name='english_verb_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='english_verbs', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'language'],
                                    name='the verb name must be unique within a english language')
        ]


class GermanVerb(Verb):
    conjugation_link = models.ForeignKey(ConjugationLink, related_name='german_verbs', on_delete=models.SET_DEFAULT,
                                         default='https://www.verbformen.ru/sprjazhenie/')
    language = models.ForeignKey(Language, related_name='german_verb_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='german_verbs', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'language'],
                                    name='the verb name must be unique within a german language')
        ]


class Adjective(models.Model):
    name = models.CharField(max_length=50)
    language = models.ForeignKey(Language, related_name='adjective_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='adjectives', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class RussianAdjective(Adjective):
    language = models.ForeignKey(Language, related_name='russian_adjective_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='russian_adjectives', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'language'],
                                    name='the adjective name must be unique within a russian language')
        ]


class EnglishAdjective(Adjective):
    language = models.ForeignKey(Language, related_name='english_adjective_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='english_adjectives', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'language'],
                                    name='the adjective name must be unique within a english language')
        ]


class GermanAdjective(Adjective):
    conjugation_link = models.ForeignKey(ConjugationLink, related_name='german_adjectives',
                                         on_delete=models.SET_DEFAULT,
                                         default='https://www.verbformen.ru/sklonenie/prilagatelnye/')
    language = models.ForeignKey(Language, related_name='german_adjective_words', on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='german_adjectives', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'language'],
                                    name='the adjective name must be unique within a german language')
        ]