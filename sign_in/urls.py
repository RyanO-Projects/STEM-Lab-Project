from django.urls import path
from . import views

app_name = 'sign_in'
urlpatterns = [
    path("sign_in/", views.Sign_In_View, name="sign_in"),
    path("sign_out/", views.Sign_Out_View, name="sign_out"),
]