from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.models import PhoneNumber


class MyUser(AbstractUser):
    phone_number = models.ForeignKey(
        to=PhoneNumber, on_delete=models.CASCADE, unique=True,
        null=False, blank=False
    )
    email = models.EmailField(
        max_length=255, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)

    def save(self, *args, **kwargs):
        self.username = self.phone_number.full_number
        if not self.id:  # if user is being created
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)
