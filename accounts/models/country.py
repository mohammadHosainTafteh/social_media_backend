from django.db import models

from core import BaseModel


class Country(BaseModel):
    id = models.SmallAutoField()
    name = models.CharField(max_length=100, null=False, blank=False)
    small_name = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        db_table = 'countries'
