from django.db import models

from accounts.models import Country
from core import BaseModel
from core.validators import country_phone_code_validator


class CountryPhoneCode(BaseModel):
    id = models.SmallAutoField()
    country = models.OneToOneField(to=Country, on_delete=models.CASCADE)
    code = models.CharField(
        max_length=4, validators=[country_phone_code_validator])
