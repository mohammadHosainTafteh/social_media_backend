from django.db import models

from core import BaseModel


class DeviceType(BaseModel):
    id = models.SmallAutoField()
    type_name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Device Type'
        verbose_name_plural = 'Device Types'
        db_table = 'device_types'
