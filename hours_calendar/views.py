from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *

class Calendar(generic.ListView):
    model = Event
    template_name = 'hours_calendar/calendar.html'
