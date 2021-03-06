# Generated by Django 2.1 on 2018-11-15 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def fill_last_tariff(apps, _):
    Abon = apps.get_model('abonapp', 'Abon')
    for abon in Abon.objects.exclude(current_tariff=None):
        abon.last_connected_tariff = abon.current_tariff.tariff
        abon.save(update_fields=('last_connected_tariff',))


class Migration(migrations.Migration):

    dependencies = [
        ('tariff_app', '0003_auto_20181115_1206'),
        ('abonapp', '0007_auto_20181101_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='abon',
            name='last_connected_tariff',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tariff_app.Tariff', verbose_name='Last connected service'),
        ),
        migrations.AlterField(
            model_name='abonlog',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RunPython(fill_last_tariff)
    ]
