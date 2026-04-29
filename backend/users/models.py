from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    middle_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
