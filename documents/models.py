from django.db import models
from vocabs.models import SkosConcept
from places.models import Place
from bib.models import Book


class Institution(models.Model):
    name = models.CharField(max_length=300, blank=True)
    abbreviation = models.CharField(max_length=300, blank=True)
    identifier = models.CharField(max_length=300, blank=True)
    parent_institution = models.ForeignKey('Institution', blank=True)


class Person(models.Model):
    forename = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=300, blank=True)
    institution = models.ForeignKey(Institution, blank=True, null=True)
    identifier = models.CharField(max_length=300, blank=True)


class Document(models.Model):
    path = models.CharField(max_length=300, blank=True)
    filename = models.CharField(max_length=300, blank=True)
    media = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name='media')
    date_analogue = models.CharField(max_length=300, blank=True)
    date_digitization = models.DateField(auto_now=False, blank=True, null=True)
    digital_format = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="digital_format"
    )
    note = models.TextField(blank=True)
    content = models.TextField(blank=True)
    topic_group = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="topic_group"
    )
    place = models.ForeignKey(Place, blank=True, null=True)
    location_analogue = models.CharField(max_length=300, blank=True)
    place_digizization = models.CharField(max_length=300, blank=True)
    curator = models.ForeignKey(Person, blank=True, null=True)
    filesize = models.FloatField(null=True)
    reference = models.ManyToManyField(Book, blank=True)
