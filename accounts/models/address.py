from django.contrib.gis.db import models

from core import BaseModel


class Address(BaseModel):
    address = models.TextField(max_length=1000, null=True, blank=True)
    location = models.PointField(null=True, blank=True)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        db_table = 'addresses'
