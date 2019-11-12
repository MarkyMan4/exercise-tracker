from django.contrib import admin
from .models import Entry, Exercise, EntryLookup

admin.site.register(Entry)
admin.site.register(Exercise)
admin.site.register(EntryLookup)
