# Generated by Django 5.0.6 on 2024-06-15 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_alter_venta_id_proveedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='id_proveedor',
        ),
    ]
