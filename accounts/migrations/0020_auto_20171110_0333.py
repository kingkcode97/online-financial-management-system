# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20171110_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='workplaces',
            field=models.ManyToManyField(to='companies.Company'),
        ),
    ]
