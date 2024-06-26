# Generated by Django 5.0.6 on 2024-06-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_rename_desc_activo_plato_descuento_activo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plato',
            old_name='desc_plato',
            new_name='descripcion_plato',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='foto_categoria',
            field=models.ImageField(blank=True, null=True, upload_to='img/categoria'),
        ),
        migrations.AlterField(
            model_name='plato',
            name='foto_plato',
            field=models.ImageField(blank=True, null=True, upload_to='img/plato'),
        ),
    ]
