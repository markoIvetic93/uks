# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170315_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='git',
            field=models.URLField(max_length=1024, null=True),
        ),
    ]
