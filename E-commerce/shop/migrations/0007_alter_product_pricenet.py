# Generated by Django 4.1.4 on 2022-12-16 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_pricenet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pricenet',
            field=models.FloatField(blank=True, null=True),
        ),
    ]