from django.conf import settings
from django.db import models

from accounts.models import DeviceType, OperatingSystem, DeviceModel
from core import BaseModel


class Device(BaseModel):
    device_type = models.ForeignKey(to=DeviceType, on_delete=models.CASCADE)
    user = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='devices')
    device_uuid = models.UUIDField(null=True, verbose_name='Device UUID')
    device_os = models.ForeignKey(to=OperatingSystem, on_delete=models.CASCADE)
    device_model = models.ForeignKey(to=DeviceModel, on_delete=models.CASCADE)
    app_version = models.CharField(max_length=50, null=True, blank=True)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    last_login_user_agent = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        db_table = 'devices'
