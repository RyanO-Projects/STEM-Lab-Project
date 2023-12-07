from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path("sign_in/", views.user_login, name="login"),
    path("sign_out/", views.user_logout, name="logout"),
    #path("create_account", views.createAccount, name="create_account"),
]