import datetime

from django.db import models
from django.utils import timezone


class DataField(models.Model):
    name = models.CharField(max_length=300)
    # todo i should either use enumeration on type or open a new table for type
    type = models.CharField(max_length=50)
    is_required = models.BooleanField()
    wikidata_item = models.OneToOneField(WikidataItem,null=true)

class DataType(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)

class WikidataItem(models.Model):
    item = models.CharField(max_length=20)
    label = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

class User(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=80)
    date_registered = models.DateTimeField(auto_now=True)
    imagePath = models.UUIDField()

#class Post(models.Model):
