# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-05 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abonapp', '0001_initial'),
        ('taskapp', '0004_auto_20161202_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='abon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='abonapp.Abon'),
        )
    ]
