# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-27 10:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20171227_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notificacion',
            old_name='permisos',
            new_name='permisos_notificacion',
        ),
    ]