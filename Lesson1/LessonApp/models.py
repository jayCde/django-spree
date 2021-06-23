from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class CustomUser(User) :
    gramps_title = models.CharField(max_length=32)
    residence = models.CharField(max_length=128)
    house_number = models.IntegerField(validators=[MinValueValidator(100, message="Should not be above 100, You do not live in Heaven")], unique=True)
    date_started = models.DateTimeField()
    residence_description = models.TextField()