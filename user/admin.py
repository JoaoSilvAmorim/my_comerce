from django.contrib import admin

# Register your models here.
from .models import User
from django.contrib.auth import admin as auth_admin

admin.site.register(User, auth_admin.UserAdmin)