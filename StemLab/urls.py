from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hours_calendar/', include('hours_calendar.urls')),
    path('homepage/', include('homepage.urls')),
    path('accounts/', include('accounts.urls')),
]
