from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path("", views.Homepage_View, name="homepage"),
]