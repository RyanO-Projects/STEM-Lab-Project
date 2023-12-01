from django.urls import path
from StemLab import views

urlpatterns = [
    path("", views.home, name="calendar"),
]