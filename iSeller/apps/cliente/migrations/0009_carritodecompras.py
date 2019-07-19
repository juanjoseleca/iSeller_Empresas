# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-24 20:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0024_auto_20171224_0725'),
        ('cliente', '0008_auto_20171224_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoDeCompras',
            fields=[
                ('idCarrito', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedor.Producto')),
            ],
        ),
    ]