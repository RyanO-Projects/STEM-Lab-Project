from django.urls import path
from django.contrib import admin
from TimeTable import views

app_name = "timetable"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.timeTable_view, name="timesheet")
]