from django.db import models

from accounts.models import CountryPhoneCode
from core import BaseModel
from core.validators import iranian_phone_number_validator


class PhoneNumber(BaseModel):
    country_code = models.ForeignKey(
        to=CountryPhoneCode, on_delete=models.CASCADE)
    phone_number = models.CharField(
        max_length=16, validators=[iranian_phone_number_validator])

    @property
    def full_number(self):
        return f'{self.country_code}{self.phone_number}'
