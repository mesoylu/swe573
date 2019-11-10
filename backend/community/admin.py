from django.contrib import admin

# Register your models here.
from .models import DataFieldType, DataField

admin.site.register(DataFieldType)

admin.site.register(DataField)
