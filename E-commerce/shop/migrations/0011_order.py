# Generated by Django 4.1.3 on 2022-12-25 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apply_order', to='shop.product')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
