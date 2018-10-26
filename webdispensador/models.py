import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Raspberry(models.Model):
    id_usr =models.ForeignKey(User, on_delete=models.CASCADE)
    ip_addr = models.CharField(max_length=20)