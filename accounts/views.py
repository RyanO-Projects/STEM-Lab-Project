from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from . import forms


def user_logout(request):
    logout(request)
    return render(request, "logout/sign_out.html")

#####
def login_page(request):
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
                message = f'Hello {user.username}, you have been logged in.'
            else:
                message = "Login failed."
    return render(request, 'login/sign_in.html', context={'form' : form, "message" : message})
