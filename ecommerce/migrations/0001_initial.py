# Generated by Django 5.0.6 on 2024-06-26 00:10

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
        ('proveedor', '0001_initial'),
        ('repartidor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id_agenda', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_agendada', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='idCategoria', primary_key=True, serialize=False)),
                ('nom_categoria', models.CharField(max_length=100)),
                ('des_categoria', models.CharField(blank=True, max_length=100, null=True)),
                ('foto_categoria', models.ImageField(blank=True, null=True, upload_to='img/categoria')),
                ('cat_activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id_entrega', models.AutoField(primary_key=True, serialize=False)),
                ('estado_entrega', models.CharField(max_length=100)),
                ('comentario_entrega', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_entrega', models.DateField()),
                ('hora_entrega', models.TimeField()),
                ('id_repartidor', models.ForeignKey(db_column='id_repatidor', on_delete=django.db.models.deletion.CASCADE, to='repartidor.repartidor')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('comentario_pedido', models.CharField(max_length=200)),
                ('estado_pedido', models.CharField(max_length=100)),
                ('monto_pedido', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('cant_item', models.IntegerField(default=1)),
                ('fecha_pdido', models.DateField(default=datetime.date.today)),
                ('retiro_local', models.BooleanField(default=True)),
                ('id_agenda', models.ForeignKey(blank=True, db_column='id_agenda', null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.agenda')),
                ('id_cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
                ('id_repartidor', models.ForeignKey(blank=True, db_column='id_repatidor', null=True, on_delete=django.db.models.deletion.CASCADE, to='repartidor.repartidor')),
            ],
        ),
        migrations.AddField(
            model_name='agenda',
            name='id_pedido',
            field=models.ForeignKey(db_column='id_pedido', on_delete=django.db.models.deletion.CASCADE, to='ecommerce.pedido'),
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id_plato', models.AutoField(primary_key=True, serialize=False)),
                ('nom_plato', models.CharField(max_length=100)),
                ('descripcion_plato', models.CharField(blank=True, max_length=200, null=True)),
                ('precio_plato', models.DecimalField(decimal_places=2, max_digits=10)),
                ('oferta_plato', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('foto_plato', models.ImageField(blank=True, null=True, upload_to='img/plato')),
                ('fecha_publicacion', models.DateField(default=datetime.date.today)),
                ('descuento_activo', models.BooleanField(default=True)),
                ('plato_activo', models.BooleanField(default=True)),
                ('id_categoria', models.ForeignKey(db_column='idCategoria', on_delete=django.db.models.deletion.CASCADE, to='ecommerce.categoria')),
                ('id_proveedor', models.ForeignKey(db_column='idProveedor', on_delete=django.db.models.deletion.CASCADE, to='proveedor.proveedor')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='plato',
            field=models.ForeignKey(db_column='id_plato', on_delete=django.db.models.deletion.CASCADE, to='ecommerce.plato'),
        ),
    ]
