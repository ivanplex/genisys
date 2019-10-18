# Generated by Django 2.2.6 on 2019-10-18 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assembly', '0003_auto_20191017_1409'),
        ('eCommerce', '0002_auto_20191018_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecomproduct',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='assembly_product', to='assembly.Product'),
            preserve_default=False,
        ),
    ]
