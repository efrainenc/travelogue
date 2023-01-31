from django.contrib import admin
from .models import Trip, Budget, ListCategory, ListItem

# Register your models here.
admin.site.register(Trip)
admin.site.register(Budget)
admin.site.register(ListCategory)
admin.site.register(ListItem)