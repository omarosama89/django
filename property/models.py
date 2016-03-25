from __future__ import unicode_literals

from django.db import models
from userlogin.models import Client
# Create your models here.


class Property(models.Model):
	ptype = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	lang = models.IntegerField()
	latt = models.IntegerField()
	price = models.IntegerField()
	area = models.IntegerField()
	img = models.CharField(max_length=100)
	nrooms = models.IntegerField()
	ntoilets = models.IntegerField()
	owner = models.ForeignKey(Client,on_delete=models.CASCADE)
