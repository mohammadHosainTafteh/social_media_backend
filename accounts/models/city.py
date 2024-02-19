from django.db import models

from accounts.models import Province


class City(models.Model):
    province = models.ForeignKey(to=Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
