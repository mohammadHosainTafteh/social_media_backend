from django.db import models

from accounts.models import Country


class Province(models.Model):
    id = models.AutoField()
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
