# Generated by Django 5.0.1 on 2024-02-02 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='pqty',
            new_name='product_qty',
        ),
    ]