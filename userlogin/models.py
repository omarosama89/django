from __future__ import unicode_literals

from django.db import models

# Create your models here.
GENDER = (
	('M', 'Male'),
	('F', 'Female'),
	)
Account_types = (
	('BR', 'Buyer/Renter'),
	('PO', 'Private Owner'),
	('B', 'Broker'),
	('RC', 'Real Estate Company'),
	)


class Client(models.Model):
	uname=models.CharField(max_length=50)
	gender = models.CharField(max_length=50, choices=GENDER)
	country = models.CharField(max_length=50)
	currency = models.CharField(max_length=50)  
	phone_number = models.CharField(max_length=50)
	account_type = models.CharField(max_length=50, choices=Account_types)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)
	name = models.CharField(max_length=100)


