from django.db import models

from accounts.models import Country


class Province(models.Model):
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
