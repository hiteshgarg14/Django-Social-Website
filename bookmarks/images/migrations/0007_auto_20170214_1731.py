# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_auto_20170214_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='total_likes',
            field=models.IntegerField(db_index=True, default=5),
        ),
    ]
