# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='lang',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='latt',
            field=models.FloatField(),
        ),
    ]
