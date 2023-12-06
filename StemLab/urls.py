from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hours_calendar.urls')),
    path('', include('homepage.urls')),
    path('', include('sign_in.urls')),
]
