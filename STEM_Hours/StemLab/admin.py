from django.contrib import admin
from StemLab.models import TutorShift
admin.site.register(TutorShift)

class TutorAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time', 'notes']