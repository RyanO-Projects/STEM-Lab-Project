from django.contrib import admin
from accounts.models import User, LoginLogoutRecord

# Register your models here.

if not admin.site.is_registered(User):
    admin.site.register(User)
    
if admin.site.is_registered(LoginLogoutRecord):
    admin.site.register(LoginLogoutRecord)