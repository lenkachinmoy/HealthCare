# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 07:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patient_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='is_favorite',
        ),
        migrations.AlterField(
            model_name='patient',
            name='report',
            field=models.FileField(upload_to=''),
        ),
    ]
