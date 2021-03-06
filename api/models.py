from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, null=True)
    date_of_birth = models.DateField(null=True)
    profile_photo = models.ImageField(upload_to="profile_images", null=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'date_of_birth', 'gender', 'profile_photo']

    def __str__(self):
        return self.email, self.first_name, self.last_name



