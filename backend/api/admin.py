from django.contrib import admin
from .models import Entry, County, Constituency, Ward, PollingStation

admin.site.register(County)
admin.site.register(Constituency)
admin.site.register(Ward)
admin.site.register(PollingStation)
admin.site.register(Entry)