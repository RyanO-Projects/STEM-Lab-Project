from django.contrib import admin
from hours_calendar.models import Event

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)