from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    deleted_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted_time = timezone.now()
        self.is_active = False
        self.save()
