from django.db import models
from django.conf import settings

from accounts.models.city import City


class IranianPhoneNumberValidator:
    pass


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, null=False, blank=False,
                                    unique=True, validators=IranianPhoneNumberValidator)
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)

