from django.contrib.auth.models import User
from django.db import models


class MyUser(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    phone_number = models.CharField(null=False, blank=False, max_length=11)


