from django.contrib import admin
from hours_calendar.models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['tutor', 'subjects', 'start_time', 'end_time']

admin.site.register(Event, EventAdmin)