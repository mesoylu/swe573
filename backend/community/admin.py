from django.contrib import admin

# Register your models here.
from .models import DataFieldType, DataField, WikidataItem, DataType

admin.site.register(DataFieldType)

admin.site.register(WikidataItem)

admin.site.register(DataField)

admin.site.register(DataType)
