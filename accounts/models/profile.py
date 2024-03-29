from django.db import models
from django.conf import settings

from accounts.models import Address, PhoneNumber
from accounts.models.city import City
from core import BaseModel


class IranianPhoneNumberValidator:
    pass


class Profile(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.ForeignKey(
        to=PhoneNumber, null=False, blank=False, unique=True)
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)
    address = models.ManyToManyField(to=Address, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        db_table = 'profiles'

