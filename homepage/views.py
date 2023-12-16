from django.shortcuts import render
from .models import Tutor, TimeSlot

# Create your views here. 
def Homepage_View(request):
    tutors = Tutor.objects.all()
    time_slots = TimeSlot.TIME_CHOICES
    days = [day[0] for day in TimeSlot.DAY_CHOICES]
    context = {"tutors" : tutors, "days" : days, "time_slots" : time_slots}
    return render(request, "homepage/homepage.html", context)