from django.contrib import admin
from .models import Tutor, Subject, TimeSlot


if not admin.site.is_registered(Tutor):
    admin.site.register(Tutor)

if not admin.site.is_registered(TimeSlot):
    admin.site.register(TimeSlot)

if not admin.site.is_registered(Subject):
    admin.site.register(Subject)