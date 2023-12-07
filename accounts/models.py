from django.db import models
from django.contrib.auth.models import AbstractUser

class StudentUser(AbstractUser):
    pass


class LoginLogoutRecord(models.Model):
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True, blank = True)
