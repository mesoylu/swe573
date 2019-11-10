from django.contrib import admin

# Register your models here.
from .models import DataFieldType, DataField, WikidataItem

admin.site.register(DataFieldType)

admin.site.register(WikidataItem)

admin.site.register(DataField)
