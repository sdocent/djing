# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-06 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0006_auto_20161206_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='abon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='abonapp.Abon'),
        )
    ]
