# Generated by Django 5.0.6 on 2024-06-26 00:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(db_column='idProveedor', primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=100)),
                ('fono_proveedor', models.DecimalField(decimal_places=2, max_digits=10, max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
