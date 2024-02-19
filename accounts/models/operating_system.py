from django.db import models

from core import BaseModel


class OperatingSystem(BaseModel):
    id = models.AutoField()
    os_name = models.CharField(max_length=50)
    os_version = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Operating System'
        verbose_name_plural = 'Operating Systems'
        db_table = 'operating_systems'
