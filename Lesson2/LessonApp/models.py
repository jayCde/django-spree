from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
# class CustomUserManager(BaseUserManager) :
#     def create_user(self):

class CustomUser(AbstractUser) :
    location = models.CharField(max_length=32)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'username' ]