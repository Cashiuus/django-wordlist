# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 04:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='family',
            options={'ordering': ('name',), 'verbose_name': 'Family', 'verbose_name_plural': 'Families'},
        ),
        migrations.AlterModelOptions(
            name='format',
            options={'ordering': ('name',), 'verbose_name': 'Format', 'verbose_name_plural': 'Formats'},
        ),
        migrations.AlterModelOptions(
            name='wordlisttype',
            options={'ordering': ('name',), 'verbose_name': 'Wordlist Type', 'verbose_name_plural': 'Wordlist Types'},
        ),
        migrations.AlterField(
            model_name='wordlist',
            name='format',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rn_formatlists', to='lists.Format'),
        ),
    ]
