from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    confirm_account = models.BooleanField(default=False)