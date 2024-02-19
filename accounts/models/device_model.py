from django.db import models

from core import BaseModel


class DeviceModel(BaseModel):
    id = models.SmallAutoField()
    type_name = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name = 'Device Model'
        verbose_name_plural = 'Device Models'
        db_table = 'device_models'
