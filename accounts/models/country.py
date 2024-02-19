from django.db import models


class Country(models.Model):
    id = models.SmallAutoField()
    name = models.CharField(max_length=100, null=False, blank=False)
    small_name = models.CharField(max_length=5, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=False, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
