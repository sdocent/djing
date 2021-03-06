# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 13:18
from __future__ import unicode_literals

from django.db import migrations
from djing.fields import MyGenericIPAddressField


class Migration(migrations.Migration):
    dependencies = [
        ('devapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'ordering': ['id'],
                     'verbose_name': 'Device', 'verbose_name_plural': 'Devices'},
        ),
        migrations.AlterField(
            model_name='device',
            name='ip_address',
            field=MyGenericIPAddressField(blank=True, max_length=8, null=True, protocol='ipv4',
                                                 verbose_name='Ip address'),
        ),
    ]
