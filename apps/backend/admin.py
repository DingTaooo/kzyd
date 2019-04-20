from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import UserInfo
from .models import Books

admin.site.register(UserInfo)
admin.site.register(Books)