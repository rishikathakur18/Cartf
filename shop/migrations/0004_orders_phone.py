# Generated by Django 4.2.6 on 2024-04-26 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_orders_alter_product_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=30),
        ),
    ]