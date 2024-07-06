# Generated by Django 5.0.6 on 2024-06-26 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repartidor',
            fields=[
                ('id_repartidor', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=12)),
                ('nombre_repartidor', models.CharField(max_length=100)),
                ('fono_repartidor', models.CharField(max_length=15)),
                ('apellido_repartidor', models.CharField(blank=True, max_length=100, null=True)),
                ('email_repartidor', models.EmailField(max_length=100)),
                ('password_repartidor', models.CharField(max_length=100)),
            ],
        ),
    ]