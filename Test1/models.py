from django.db import models
from django.utils import timezone

class testModel(models.Model):
    testName = models.CharField(max_length=255, null=True)
    testPate = models.CharField(max_length=255, null=True)
    testMate = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.testName

    class Meta:
        db_table = "testModel"
# Create your models here.
