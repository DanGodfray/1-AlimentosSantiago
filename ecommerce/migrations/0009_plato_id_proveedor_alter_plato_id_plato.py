# Generated by Django 5.0.6 on 2024-06-15 02:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_alter_plato_id_plato'),
        ('usuarios', '0007_remove_venta_id_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='id_proveedor',
            field=models.ForeignKey(db_column='idProveedor', default=1, on_delete=django.db.models.deletion.CASCADE, to='usuarios.proveedor'),
        ),
        migrations.AlterField(
            model_name='plato',
            name='id_plato',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
