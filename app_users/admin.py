from django.contrib import admin
from django.contrib.auth import get_user_model
from app_users.models import User
admin.site.register(User)
# Register your models here.
