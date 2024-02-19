from django.db import models

from accounts.models import Country
from core import BaseModel


class Province(BaseModel):
    id = models.AutoField()
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'
        db_table = 'provinces'
