from django.contrib import admin
from models import TutorShift

class TutorAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time', 'notes']