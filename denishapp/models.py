from time import time
from django.db import models
from django.utils import timezone

class DenishModel(models.Model):
    name = models.CharField(max_length=10)
    text = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
