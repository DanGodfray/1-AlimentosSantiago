# Generated by Django 5.0.6 on 2024-07-12 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_remove_pedido_cant_item_remove_pedido_plato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='comentario_pedido',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
