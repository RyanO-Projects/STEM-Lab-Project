from django.urls import path
import accounts.views
from django.contrib import admin


app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", accounts.views.login_page , name="login"),
    path("logout/", accounts.views.user_logout, name="logout"),
    #path("create_account", views.createAccount, name="create_account"),
]