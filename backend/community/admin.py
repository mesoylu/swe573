from django.contrib import admin

# Register your models here.
from .models import DataFieldType, DataField, WikidataItem, DataType, User, Community, Post, FieldValue

admin.site.register(DataFieldType)

admin.site.register(WikidataItem)

admin.site.register(DataField)

admin.site.register(DataType)

admin.site.register(User)

admin.site.register(Community)

admin.site.register(Post)

admin.site.register(FieldValue)
