from django.db import models

from accounts.models import Province
from core import BaseModel


class City(BaseModel):
    province = models.ForeignKey(to=Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        db_table = 'cities'
