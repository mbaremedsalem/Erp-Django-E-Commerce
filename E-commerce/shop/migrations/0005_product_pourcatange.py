# Generated by Django 4.1.4 on 2022-12-16 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pourcatange',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]