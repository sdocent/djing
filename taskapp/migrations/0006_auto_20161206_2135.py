# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-06 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0005_auto_20161206_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='mode',
            field=models.CharField(choices=[(b'na', '\u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043e'), (b'yt', '\u0436\u0451\u043b\u0442\u044b\u0439 \u0442\u0440\u0435\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a'), (b'rc', '\u043a\u0440\u0430\u0441\u043d\u044b\u0439 \u043a\u0440\u0435\u0441\u0442\u0438\u043a'), (b'ls', '\u0441\u043b\u0430\u0431\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c'), (b'cf', '\u043e\u0431\u0440\u044b\u0432 \u043a\u0430\u0431\u0435\u043b\u044f'), (b'cn', '\u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435'), (b'pf', '\u043f\u0435\u0440\u0435\u043e\u0434\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043f\u0440\u043e\u043f\u0430\u0434\u0430\u043d\u0438\u0435'), (b'cr', '\u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0440\u043e\u0443\u0442\u0435\u0440\u0430'), (b'co', '\u043d\u0430\u0441\u0442\u0440\u043e\u0438\u0442\u044c onu'), (b'fc', '\u043e\u0431\u0436\u0430\u0442\u044c \u043a\u0430\u0431\u0435\u043b\u044c'), (b'ot', '\u0434\u0440\u0443\u0433\u043e\u0435')], default=b'na', max_length=2),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[(b'A', '\u0412\u044b\u0441\u0448\u0438\u0439'), (b'C', '\u0421\u0440\u0435\u0434\u043d\u0438\u0439'), (b'E', '\u041d\u0438\u0437\u043a\u0438\u0439')], default=b'E', max_length=1),
        ),
    ]
