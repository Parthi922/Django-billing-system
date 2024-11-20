# Generated by Django 5.0.7 on 2024-08-02 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0003_products_category_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category_reference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventory.category'),
        ),
    ]