# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_auto_20160705_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordlist',
            name='online_source',
            field=models.URLField(blank=True, null=True, verbose_name='Online Source'),
        ),
    ]