from datetime import datetime
from django.db import models


class Event(models.Model):
    date = models.DateField(default=datetime.now())
    name = models.CharField(max_length=255)
