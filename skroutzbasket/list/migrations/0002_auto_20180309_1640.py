# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='token',
            field=models.CharField(blank=True, max_length=17),
        ),
    ]