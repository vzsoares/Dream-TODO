from django.contrib import admin

# Register your models here.

from .models import UserTodo

admin.site.register(UserTodo)