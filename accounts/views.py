from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone
from accounts.models import LoginLogoutRecord
from . import forms


def user_login(request):
    form = forms.LoginForm()
    message = ""
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"]
                )
            if user is not None:
                login(request, user)
                LoginLogoutRecord.objects.create(student=user, login_time=timezone.now())
                return redirect("homepage:homepage")
            else:
                message = "Login Failed."
    return render(request, "login/sign_in.html", context={"form" : form, "message" : message})


def user_logout(request):
    if request.user.is_authenticated:
        logout_time = timezone.now()
        logout_record = LoginLogoutRecord.objects.filter(student=request.user, logout_time__isnull=True).first()
        if logout_record:
            logout_record.logout_time = logout_time
            logout_record.save()
        logout(request)
    else:
        return render(request, "logout/error.html")

    return render(request, "logout/sign_out.html")