# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_issue_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='type',
            field=models.CharField(default='Greška', max_length=50),
        ),
    ]