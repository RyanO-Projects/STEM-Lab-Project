from django.urls import path
import accounts.views
from django.contrib import admin


app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", accounts.views.user_login, name="login"),
    path("logout/", accounts.views.user_logout, name="logout"),
]