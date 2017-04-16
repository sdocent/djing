# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-16 07:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0013_auto_20170413_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='abon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='abonapp.Abon'),
        ),
        migrations.AlterField(
            model_name='task',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
