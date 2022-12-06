from django.db import models
from datetime import date

class Customer(models.Model):
    date = models.DateField(("Date"), default=date.today)
    trade_code = models.CharField(max_length=50)
    high = models.CharField(max_length=50)
    low = models.CharField(max_length=50)
    open = models.CharField(max_length=50)
    close = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)

class JsonModel(models.Model):
    date = models.DateField(("Date"), default=date.today)
    trade_code = models.CharField(max_length=50)
    high = models.CharField(max_length=50)
    low = models.CharField(max_length=50)
    open = models.CharField(max_length=50)
    close = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)