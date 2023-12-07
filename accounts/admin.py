from django.contrib import admin
from accounts.models import StudentUser, LoginLogoutRecord
admin.site.register(StudentUser)

# Register your models here.
if not admin.site.is_registered(StudentUser):
    admin.site.register(StudentUser)
    
if admin.site.is_registered(LoginLogoutRecord):
    admin.site.register(LoginLogoutRecord)