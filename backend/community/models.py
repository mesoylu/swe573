import datetime
import os

from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.postgres.fields import JSONField
from enum import Enum
from uuid import uuid4
from django.utils.deconstruct import deconstructible


# todo should this function reside here
# todo this function has a reported bug
# def path_and_rename(path):
#     def wrapper(instance, filename):
#         ext = filename.split('.')[-1]
#         # get filename
#         if instance.pk:
#             filename = '{}.{}'.format(instance.pk, ext)
#         else:
#             # set filename as random string
#             filename = '{}.{}'.format(uuid4().hex, ext)
#         # return the whole path to the file
#         return os.path.join(path, filename)
#     return wrapper


@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


path_and_rename = PathAndRename("images")


class DataFieldTypes(Enum):
    str = "string"
    bl = "boolean"
    dec = "decimal"
    fl = "float"
    dur = "duration"
    dt = "dateTime"
    uri = "anyURI"

    @classmethod
    def all(self):
        return self


class User(models.Model):
    username = models.SlugField(
        max_length=100,
        unique=True
    )
    password = models.CharField(
        max_length=32
    )
    email = models.EmailField(
        max_length=200,
        unique=True
    )
    # image_path = models.CharField(
    #     max_length=100,
    #     null=True,
    #     blank=True
    # )
    image = models.ImageField(
        upload_to=path_and_rename,
        blank=True,
        null=True
    )
    date_registered = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.username


class Community(models.Model):
    # todo should we proceed with reddit style naming conventions
    name = models.SlugField(
        max_length=100,
        unique=True
    )
    description = models.TextField(
        max_length=300
    )
    # url = models.CharField(
    #     max_length=100,
    #     unique=True
    # )
    # todo research on audio video image upload on django
    # image_path = models.CharField(
    #     max_length=100,
    #     null=True,
    #     blank=True
    # )
    image = models.ImageField(
        upload_to=path_and_rename,
        blank=True,
        null=True
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    members = models.ManyToManyField(
        User,
        related_name="member"
    )
    date_created = models.DateTimeField(
        auto_now=True
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
    # todo this field would hold information from wikidata item
    data = JSONField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.label


class DataField(models.Model):
    name = models.CharField(
        max_length=50
    )
    # todo i should either use enumeration on type or open a new table for type
    type = models.CharField(
        max_length=3,
        choices=[(tag.name, tag.value) for tag in DataFieldTypes]
    )
    is_required = models.BooleanField()
    # todo OneToOne or ManyToOne // should we add more than one tag to a data field
    wikidata_item = models.ForeignKey(
        WikidataItem,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    community = models.ForeignKey(
        Community,
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
    fields = models.ManyToManyField(
        DataField,
        # todo it is hard to give callable to limit_choices_to property
        # limit_choices_to={'community': 1},
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    community = models.ForeignKey(
        Community,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    data_type = models.ForeignKey(
        DataType,
        on_delete=models.PROTECT
    )
    date_created = models.DateTimeField(
        auto_now=True
    )
    # todo these two should come from vote table, right now it is a placeholder
    upvote_count = models.IntegerField()
    downvote_count = models.IntegerField()
    fields = JSONField(
        blank=True,
        null=True
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )
    community = models.ForeignKey(
        Community,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.data_type.title + " : " + str(self.pk)


#
# class DataFieldType(models.Model):
#     name = models.CharField(
#         max_length=30
#     )
#     type = models.CharField(
#         max_length=30
#     )
#
#     def __str__(self):
#         return self.name
#
#
# class WikidataItem(models.Model):
#     item = models.CharField(
#         max_length=25
#     )
#     label = models.CharField(
#         max_length=100
#     )
#     description = models.CharField(
#         max_length=200
#     )
#
#     def __str__(self):
#         return self.label
#
#
# class User(models.Model):
#     username = models.CharField(
#         max_length=50,
#         unique=True
#     )
#     password = models.CharField(
#         max_length=32
#     )
#     email = models.CharField(
#         max_length=100,
#         unique=True
#     )
#     image_path = models.CharField(
#         max_length=100,
#         null=True,
#         blank=True
#     )
#     date_registered = models.DateTimeField(
#         auto_now=True
#     )
#
#     def __str__(self):
#         return self.username
#
#
# class Community(models.Model):
#     name = models.CharField(
#         max_length=100,
#         unique=True
#     )
#     description = models.TextField(
#         max_length=300
#     )
#     # todo should we proceed with reddit style naming conventions
#     url = models.CharField(
#         max_length=100,
#         unique=True
#     )
#     # todo research on audio video image upload on django
#     image_path = models.CharField(
#         max_length=100,
#         null=True,
#         blank=True
#     )
#     creator = models.ForeignKey(
#         User,
#         on_delete=models.PROTECT,
#         related_name="creator"
#     )
#     members = models.ManyToManyField(
#         User,
#         related_name="member"
#     )
#     date_created = models.DateTimeField(
#         auto_now=True
#     )
#
#     def __str__(self):
#         return self.name
#
#
# class DataField(models.Model):
#     name = models.CharField(
#         max_length=50
#     )
#     # todo i should either use enumeration on type or open a new table for type
#     type = models.ForeignKey(
#         DataFieldType,
#         on_delete=models.PROTECT
#     )
#     is_required = models.BooleanField()
#     # todo OneToOne or ManyToOne // should we add more than one tag to a data field
#     wikidata_item = models.ForeignKey(
#         WikidataItem,
#         null=True,
#         blank=True,
#         on_delete=models.PROTECT
#     )
#     community = models.ForeignKey(
#         Community,
#         on_delete=models.PROTECT,
#         blank=True,
#         null=True
#     )
#
#     def __str__(self):
#         return self.name
#
#
# class DataType(models.Model):
#     title = models.CharField(
#         max_length=100
#     )
#     # todo update class diagram for this property
#     body = models.TextField(
#         max_length=2000
#     )
#     data_fields = models.ManyToManyField(
#         DataField,
#         # todo it is hard to give callable to limit_choices_to property
#         # limit_choices_to={'community': 1},
#     )
#     community = models.ForeignKey(
#         Community,
#         on_delete=models.PROTECT,
#         blank=True,
#         null=True
#     )
#
#     def __str__(self):
#         return self.title
#
#
#
#
# class Post(models.Model):
#     data_type = models.ForeignKey(
#         DataType,
#         on_delete=models.PROTECT
#     )
#     date_created = models.DateTimeField(
#         auto_now=True
#     )
#     # todo these two should come from vote table, right now it is a placeholder
#     upvote_count = models.IntegerField()
#     downvote_count = models.IntegerField()
#     community = models.ForeignKey(
#         Community,
#         on_delete=models.PROTECT
#     )
#
#     def __str__(self):
#         return self.data_type.title + " : " + str(self.pk)
#
#
# # todo this class will be added to diagram
# class FieldValue(models.Model):
#     data_field = models.ForeignKey(
#         DataField,
#         on_delete=models.PROTECT
#     )
#     value = models.CharField(
#         max_length=200
#     )
#     post = models.ForeignKey(
#         Post,
#         on_delete=models.PROTECT
#     )
#
#     def __str__(self):
#         return self.data_field.name + " : " + self.value


#
#
# class User(models.Model):
#    email = models.CharField(max_length=200)
#    password = models.CharField(max_length=200)
#    username = models.CharField(max_length=80)
#    date_registered = models.DateTimeField(auto_now=True)
#    imagePath = models.UUIDField()
#
# class Post(models.Model):
