import datetime

from django.db import models
from django.utils import timezone


class DataFieldType(models.Model):
    name = models.CharField(
        max_length=30
    )
    type = models.CharField(
        max_length=30
    )

    def __str__(self):
        return self.name


class WikidataItem(models.Model):
    item = models.CharField(
        max_length=25
    )
    label = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.label

class DataField(models.Model):
    name = models.CharField(
        max_length=50
    )
    # todo i should either use enumeration on type or open a new table for type
    type = models.OneToOneField(
        DataFieldType,
        on_delete=models.PROTECT
    )
    is_required = models.BooleanField()
    # todo OneToOne or ManyToOne // should we add more than one tag to a data field
    wikidata_item = models.ForeignKey(
        WikidataItem,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name


class DataType(models.Model):
    title = models.CharField(
        max_length=100
    )
    # todo update class diagram for this property
    body = models.TextField(
        max_length=2000
    )
    data_fields = models.ManyToManyField(
        DataField
    )

    def __str__(self):
        return self.title

#
#
#class User(models.Model):
#    email = models.CharField(max_length=200)
#    password = models.CharField(max_length=200)
#    username = models.CharField(max_length=80)
#    date_registered = models.DateTimeField(auto_now=True)
#    imagePath = models.UUIDField()
#
#class Post(models.Model):
