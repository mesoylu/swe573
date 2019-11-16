import datetime

from django.db import models
from django.utils import timezone
from datetime import datetime




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
