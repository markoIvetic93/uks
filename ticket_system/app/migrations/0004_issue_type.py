# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170202_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='type',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
