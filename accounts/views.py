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
            first = form.cleaned_data["first_name"]
            last = form.cleaned_data["last_name"]
            student = LoginLogoutRecord.objects.get_or_create(first_name = first, last_name = last)[0]
            student.last_login_time = timezone.now()
            student.save()
            return redirect("homepage:homepage")
    return render(request, "login/sign_in.html", context={"form" : form, "message" : message})

def user_logout(request):
    form = forms.LogoutForm()
    message = ""
    if request.method == "POST":
        form = forms.LogoutForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data["first_name"]
            last = form.cleaned_data["last_name"]
            student = LoginLogoutRecord.objects.get_or_create(first_name = first, last_name = last)[0]
            student.last_logout_time = timezone.now()
            student.total_time += (student.last_logout_time - student.last_login_time).seconds
            student.save()
            return redirect("homepage:homepage")
    return render(request, "logout/sign_out.html", context={"form" : form, "message" : message})