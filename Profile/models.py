from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User

class profileModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)
    delete = models.BooleanField(default = False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "profileModel"