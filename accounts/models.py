from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class LoginLogoutRecord(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    last_login_time = models.DateTimeField(auto_now_add=True)
    last_logout_time = models.DateTimeField(null=True, blank = True)
    total_time = models.FloatField(default = 0)

    def __str__(self):
        return self.first_name + " " + self.last_name