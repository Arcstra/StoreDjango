from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = "user"

    username = models.CharField(max_length=255, unique=True)
    username_display = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_joined = models.DateField(auto_now=True)
    confirmed_email = models.BooleanField(default=False)
    first_name = None
    last_name = None

    def __str__(self):
        return self.username_display
