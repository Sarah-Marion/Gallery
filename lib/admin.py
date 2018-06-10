from django.contrib import admin
from .models import LibGroup, Technique, Location , Category, Image


# Register your models here.

admin.site.register(LibGroup)
admin.site.register(Technique)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Image)