from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .models import StudentUser, LoginLogoutRecord
from django.utils import timezone

def createAccount(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'createAccount/createAccount.html', {'form', form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)
            LoginLogoutRecord.objects.create(student=user)
            return redirect('homepage')
        else:
            # ROAD WORK AHEAD
            pass
    return render(request, 'login/sign_in.html')


def user_logout(request):
    if request.user.is_authenticated:
        logout_time = timezone.now()
        logout_record = LoginLogoutRecord.objects.filter(student=request.user, logout_time__isnull=True).first()
        if logout_record:
            logout_record.output_time = logout_time
            logout_record.save()
        logout(request)
    return redirect('login')