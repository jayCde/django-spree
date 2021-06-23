from django.contrib import admin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "username", "email", "password", 
                    "gramps_title", "residence", "house_number", "date_started", 
                    "residence_description")