# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 23:00
from __future__ import unicode_literals

import django.contrib.sites.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_auto_20160704_0433'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='site',
            managers=[
                ('objects', django.contrib.sites.models.SiteManager()),
            ],
        ),
    ]
