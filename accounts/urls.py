from django.urls import path
from accounts import views
from django.contrib import admin


app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]