from django.contrib import admin

# Register your models here.
from .models import UserAccounts

admin.site.register(UserAccounts)