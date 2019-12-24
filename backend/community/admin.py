from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(WikidataItem)

admin.site.register(DataType)

admin.site.register(User)

admin.site.register(Community)

admin.site.register(Post)

admin.site.register(Membership)
