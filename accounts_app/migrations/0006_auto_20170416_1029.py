# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-16 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0005_auto_20170222_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photo_app.Photo'),
        ),
    ]