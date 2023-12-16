from django.urls import path
from django.contrib import admin
from . import views

app_name = 'homepage'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Homepage_View, name="homepage"),
]
