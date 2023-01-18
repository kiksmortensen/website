from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Appointment(models.Model):
    date = models.DateTimeField('Date signed up for')
    location = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50, default="None")

    def appointment_soon(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self) -> str:
        return self.name