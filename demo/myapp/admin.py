from django.contrib import admin
from .models import TodoItem

# Register your models here. This file allows to register your database models so you can view them on your Admin panel. 
admin.site.register(TodoItem)
