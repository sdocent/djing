# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-18 16:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0009_auto_20161216_2214'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('-id',), 'permissions': (('can_viewall', '\u0414\u043e\u0441\u0442\u0443\u043f \u043a\u043e \u0432\u0441\u0435\u043c \u0437\u0430\u0434\u0430\u0447\u0430\u043c'), ('can_remind', '\u041d\u0430\u043f\u043e\u043c\u0438\u043d\u0430\u043d\u0438\u044f \u043e \u0437\u0430\u0434\u0430\u0447\u0430\u0445'))},
        )
    ]
