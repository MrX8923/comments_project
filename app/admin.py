from django.contrib import admin
from .models import *


mods = (Comment, Movie)

for mod in mods:
    admin.site.register(mod, admin.ModelAdmin)
