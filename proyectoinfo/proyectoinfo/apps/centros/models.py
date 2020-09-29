from django.db import models
from django.utils import timezone
from location_field.models.plain import PlainLocationField


class EnableCenter(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    phone_num = models.IntegerField()
    address = models.CharField(max_length=200)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    business_hours = models.CharField(max_length=200)
