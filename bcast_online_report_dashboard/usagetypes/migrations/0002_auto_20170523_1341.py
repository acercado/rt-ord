# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 05:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usagetypes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dashboardlastsession',
            table='ord_bcast_dashboard_last_session',
        ),
    ]