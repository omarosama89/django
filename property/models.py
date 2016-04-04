from __future__ import unicode_literals

from django.db import models
from userlogin.models import Client


# Create your models here.


class Property(models.Model):
    ptype = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    saleOrRent = models.CharField(max_length=50, default='null')
    government = models.CharField(max_length=50, default='null')
    lang = models.CharField(max_length=50)
    latt = models.CharField(max_length=50)
    price = models.IntegerField()
    area = models.IntegerField()
    img = models.CharField(max_length=100)
    nrooms = models.IntegerField()
    ntoilets = models.IntegerField()
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
