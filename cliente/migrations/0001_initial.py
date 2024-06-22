# Generated by Django 5.0.6 on 2024-06-21 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('rut_cliente', models.CharField(max_length=12)),
                ('saldo_cliente', models.DecimalField(decimal_places=2, max_digits=10)),
                ('empresa', models.CharField(max_length=100)),
            ],
        ),
    ]
