# Generated by Django 2.2.6 on 2019-10-18 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecomproduct',
            name='availability',
            field=models.CharField(choices=[('in stock', 'In Stock'), ('out of stock', 'Out of Stock'), ('preorder', 'Pre-order')], max_length=255),
        ),
    ]
