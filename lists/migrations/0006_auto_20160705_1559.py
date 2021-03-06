# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20160704_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='kali_path',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Kali Install Path'),
        ),
        migrations.AlterField(
            model_name='wordlist',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rn_typelists', to='lists.WordlistType', verbose_name='List Type'),
        ),
    ]
