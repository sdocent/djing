# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-30 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_auto_20161006_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='attachment',
            field=models.ImageField(blank=True, null=True, upload_to='task_attachments/%Y.%m.%d'),
        )
    ]
